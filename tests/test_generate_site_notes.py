"""Note-level conversion: macros, \\input, titles, image lookup, figures and PDF pages."""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPO_ROOT / "tools" / "web" / "generate_site.py"


def run_generator(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GENERATOR), "--root", str(root), "--output", str(root / ".web-build"), *extra],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )


def page_of(root: Path, route: str) -> str:
    return (root / ".web-build" / "docs" / route / "index.md").read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_pdf(path: Path, content: bytes, *, page_extra: bytes = b"", resources: bytes = b"<< >>", extra: list[bytes] = ()) -> None:
    """Minimal one-page PDF; objects 1-4 are catalog, pages, page and content stream."""
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 100] " + page_extra + b" /Resources " + resources + b" /Contents 4 0 R >>",
        b"<< /Length %d >>\nstream\n" % len(content) + content + b"\nendstream",
        *extra,
    ]
    data = b"%PDF-1.4\n"
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(data))
        data += b"%d 0 obj\n" % number + body + b"\nendobj\n"
    xref = len(data)
    data += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    data += b"".join(b"%010d 00000 n \n" % offset for offset in offsets)
    data += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objects) + 1, xref)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_two_color_bitmap_pdf(path: Path, *, crop_left_half: bool) -> None:
    """A bitmap-dominated page: left half red, right half blue (noisy so it stays a bitmap in SVG)."""
    width, height = 200, 100
    pixels = bytearray()
    for y in range(height):
        for x in range(width):
            noise = (x * 7 + y * 13) % 23
            pixels += bytes((220 - noise, noise, noise)) if x < width // 2 else bytes((noise, noise, 220 - noise))
    image = (
        b"<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceRGB /BitsPerComponent 8 /Length %d >>\nstream\n"
        % (width, height, len(pixels))
        + bytes(pixels)
        + b"\nendstream"
    )
    write_pdf(
        path,
        b"q 200 0 0 100 0 0 cm /Im0 Do Q",
        page_extra=b"/CropBox [0 0 100 100]" if crop_left_half else b"",
        resources=b"<< /XObject << /Im0 5 0 R >> >>",
        extra=[image],
    )


def test_expands_macros_from_input_preamble_without_reviving_comments(tmp_path: Path) -> None:
    write(
        tmp_path / "course" / "course-preamble.tex",
        r"""
\newcommand{\figsource}[1]{\par{\footnotesize\color{gray}\emph{来源：#1}}\par}
\newcommand{\lecturefigure}[3]{%
\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{#1}
\caption{#2}
\figsource{#3}
\end{figure}
}
\newcommand{\teachervoice}[1]{\begin{knowledgebox}{课堂提示}#1\end{knowledgebox}}
\newcommand{\term}[1]{\textbf{#1}}
""",
    )
    (tmp_path / "course" / "lecture01").mkdir(parents=True)
    Image.new("RGB", (400, 200), (10, 120, 200)).save(tmp_path / "course" / "lecture01" / "plot.png")
    write(
        tmp_path / "course" / "lecture01" / "lecture01-notes.tex",
        r"""
\documentclass{article}
\input{../course-preamble.tex}
\newcommand{\notetitle}{宏展开}
\begin{document}
\section{正文}
这是一个\term{术语}。
\teachervoice{老师强调的要点。}
\lecturefigure{plot.png}{示意图}{课堂幻灯片第 3 页}
% \lecturefigure{hidden.png}{不应出现}{注释掉的宏}
\end{document}
""",
    )

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    page = page_of(tmp_path, "course/lecture01")
    assert "这是一个**术语**。" in page
    assert '!!! info "课堂提示"\n    老师强调的要点。' in page
    assert re.search(r'<img src="plot\.png\.webp" alt="示意图" width="400" height="200"', page)
    assert '<span class="ai-notes-figure__source">来源：课堂幻灯片第 3 页</span>' in page
    assert "不应出现" not in page and "hidden.png" not in page
    for raw in (r"\term", r"\teachervoice", r"\lecturefigure", r"\figsource"):
        assert raw not in page


def test_code_listings_keep_percent_lines_and_unexpanded_macros(tmp_path: Path) -> None:
    write(
        tmp_path / "course" / "lecture01" / "lecture01-notes.tex",
        r"""
\documentclass{article}
\newcommand{\term}[1]{\textbf{#1}}
\begin{document}
\begin{lstlisting}[language=TeX]
% a LaTeX comment inside a code sample
\term{kept}
\end{lstlisting}
\end{document}
""",
    )

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    page = page_of(tmp_path, "course/lecture01")
    assert "```tex\n% a LaTeX comment inside a code sample\n\\term{kept}\n```" in page


def test_titles_use_last_definition_or_title_page(tmp_path: Path) -> None:
    write(
        tmp_path / "course" / "lecture01" / "lecture01-notes.tex",
        r"""
\documentclass{article}
\newcommand{\notetitle}{占位标题}
\renewcommand{\notetitle}{真正的标题}
\begin{document}
正文
\end{document}
""",
    )
    write(
        tmp_path / "course" / "lecture02" / "lecture02-notes.tex",
        r"""
\documentclass{article}
\begin{document}
\begin{titlepage}
{\large 张小珺商业访谈录\par}
{\huge\bfseries 封面上的标题：Agent 与创业}\par
\end{titlepage}
正文
\end{document}
""",
    )

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    assert "\n# 真正的标题\n" in page_of(tmp_path, "course/lecture01")
    assert "\n# 封面上的标题：Agent 与创业\n" in page_of(tmp_path, "course/lecture02")


def test_book_note_inlines_chapters_and_serves_as_its_course_page(tmp_path: Path) -> None:
    write(tmp_path / "book" / "lecture01" / "lecture01-chapter.tex", r"\section{第一章}" + "\n第一章的正文。")
    write(
        tmp_path / "book" / "book-notes.tex",
        r"""
\documentclass{article}
\newcommand{\notetitle}{一本书}
\begin{document}
\IfFileExists{lecture01/lecture01-chapter.tex}{\input{lecture01/lecture01-chapter.tex}}{}
\IfFileExists{lecture02/lecture02-chapter.tex}{\input{lecture02/lecture02-chapter.tex}}{}
\end{document}
""",
    )

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    page = page_of(tmp_path, "book")
    assert "\n# 一本书\n" in page
    assert "## 第一章" in page and "第一章的正文。" in page
    assert "共 1 份讲义" not in page
    nav = (tmp_path / ".web-build" / "mkdocs.yml").read_text(encoding="utf-8")
    assert nav.count('"book/index.md"') == 1


def test_resolves_graphicspath_and_renders_every_image_in_and_outside_figures(tmp_path: Path) -> None:
    lecture = tmp_path / "course" / "lecture01"
    (lecture / "figs").mkdir(parents=True)
    for name, color in (("left.png", (200, 0, 0)), ("right.jpg", (0, 0, 200)), ("plot.png", (0, 150, 0)), ("slide.png", (90, 90, 90))):
        Image.new("RGB", (300, 150), color).save(lecture / "figs" / name)
    write(
        lecture / "lecture01-notes.tex",
        r"""
\documentclass{article}
\graphicspath{{figs/}}
\begin{document}
\begin{figure}[H]
\begin{minipage}[t]{0.48\textwidth}\includegraphics[width=\linewidth]{left}\caption{左图}\end{minipage}\hfill
\begin{minipage}[t]{0.48\textwidth}\includegraphics[width=\linewidth]{right.jpg}\end{minipage}
\caption{两张图的总图注 $x^2$}
\end{figure}
\begin{center}
\includegraphics[width=0.9\textwidth]{slide.png}
\end{center}
\end{document}
""",
    )

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    assert "Missing assets" not in result.stdout
    page = page_of(tmp_path, "course/lecture01")
    figure = re.search(r'<figure class="ai-notes-figure ai-notes-figure--group">.*?</figure>', page, re.S)
    assert figure, page
    assert re.findall(r'<img src="([^"]+)"', figure.group(0)) == ["figs/left.png.webp", "figs/right.jpg.webp"]
    assert '<figcaption>两张图的总图注 <span class="arithmatex">\\(x^2\\)</span>' in figure.group(0)
    assert 'src="figs/slide.png.webp"' in page
    assert r"\includegraphics" not in page


@pytest.mark.skipif(shutil.which("pdftocairo") is None, reason="pdftocairo is not installed")
def test_pdf_pages_respect_cropbox_brace_page_and_unsupported_options(tmp_path: Path) -> None:
    lecture = tmp_path / "course" / "lecture01"
    write_two_color_bitmap_pdf(lecture / "cropped.pdf", crop_left_half=True)
    write_two_color_bitmap_pdf(lecture / "trimmed.pdf", crop_left_half=False)
    pages = [Image.new("RGB", (400, 200), color) for color in ((220, 30, 30), (30, 30, 220))]
    pages[0].save(lecture / "deck.pdf", save_all=True, append_images=pages[1:])
    write(
        lecture / "lecture01-notes.tex",
        r"""
\documentclass{article}
\begin{document}
\begin{figure}\includegraphics[width=\textwidth]{cropped.pdf}\caption{裁剪}\end{figure}
\begin{figure}\includegraphics[page={2},width=0.5\linewidth]{deck.pdf}\caption{第二页}\end{figure}
\begin{figure}\includegraphics[trim=0 0 100 0,clip,width=\textwidth]{trimmed.pdf}\caption{局部}\end{figure}
\end{document}
""",
    )

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    out_dir = tmp_path / ".web-build" / "docs" / "course" / "lecture01"
    page = page_of(tmp_path, "course/lecture01")
    previews = dict((alt, src) for src, alt in re.findall(r'<img src="(figures-web/[^"]+)" alt="([^"]+)"', page))
    with Image.open(out_dir / previews["裁剪"]) as cropped:
        # The CropBox keeps only the red left half, as in the PDF output.
        assert cropped.width == cropped.height
        red, _green, blue = cropped.convert("RGB").getpixel((cropped.width - 5, cropped.height // 2))
        assert red > 150 and blue < 100
    with Image.open(out_dir / previews["第二页"]) as second:
        red, _green, blue = second.convert("RGB").getpixel((second.width // 2, second.height // 2))
        assert blue > 150 and red < 100
    assert 'style="width: 50%"' in page
    assert "局部" not in previews
    assert "[打开 PDF 图示]" in page

    strict = run_generator(tmp_path, "--strict", "--fail-on-pdf-figure-warnings")
    assert strict.returncode == 1
    assert "trim/viewport/angle" in strict.stdout


def test_source_preparation_follows_tex_semantics(tmp_path: Path) -> None:
    write(tmp_path / "course" / "shared.tex", r"\newcommand{\shared}{共享宏}")
    write(tmp_path / "course" / "lecture01" / "chapter.tex", "被注释的 input 不应出现")
    write(
        tmp_path / "course" / "lecture01" / "lecture01-notes.tex",
        r"""
\documentclass{article}
\input{../shared.tex}
\newcommand{\term}[1]{\textbf{#1}}
\renewcommand{\term}[1]{\emph{#1}}
\renewcommand{\arraystretch}{1.3}
\newcommand{\definer}[1]{\newcommand{\inner}[1]{##1-#1}}
\begin{document}
\shared；\term{改写后的宏}；\verb|\term{原样}|
% \input{chapter.tex}
\input{/etc/hosts}
\IfFileExists{missing.tex}{\input{missing.tex}}{{缺失分支}}
\begin{figure}
\begin{center}
\includegraphics[width=0.5\textwidth]{plot.png}
\end{center}
\caption{居中的图}
{\footnotesize 来源：$\pi_{0.7}$ 论文}
\end{figure}
\end{document}
""",
    )
    Image.new("RGB", (200, 100), (0, 0, 0)).save(tmp_path / "course" / "lecture01" / "plot.png")

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    page = page_of(tmp_path, "course/lecture01")
    assert "共享宏；*改写后的宏*；" in page
    assert r"\term{原样}" in page
    assert "被注释的 input 不应出现" not in page
    assert "localhost" not in page
    assert "缺失分支" in page and r"\IfFileExists" not in page
    figure = re.search(r'<figure class="ai-notes-figure">.*?</figure>', page, re.S)
    assert figure and 'src="plot.png.webp"' in figure.group(0)
    assert "<figcaption>居中的图" in figure.group(0)
    assert '<span class="ai-notes-figure__source">来源：<span class="arithmatex">\\(\\pi_{0.7}\\)</span> 论文</span>' in figure.group(0)


def test_full_build_prunes_unused_cache_entries(tmp_path: Path) -> None:
    lecture = tmp_path / "course" / "lecture01"
    lecture.mkdir(parents=True)
    Image.new("RGB", (200, 100), (0, 0, 0)).save(lecture / "plot.png")
    write(lecture / "lecture01-notes.tex", r"\documentclass{article}\begin{document}\begin{figure}\includegraphics{plot.png}\caption{图}\end{figure}\end{document}")
    image_cache = tmp_path / ".web-build" / ".cache" / "images"
    image_cache.mkdir(parents=True)
    (image_cache / "image-stale.jpg").write_bytes(b"old")

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    assert [path.suffix for path in image_cache.iterdir()] == [".webp"]

import shutil
import subprocess
import sys
import importlib.util
from pathlib import Path

from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPO_ROOT / "tools" / "web" / "generate_site.py"


def load_generator_module():
    spec = importlib.util.spec_from_file_location("generate_site", GENERATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_image(path: Path, size: tuple[int, int], mode: str = "RGB") -> None:
    if mode == "RGBA":
        image = Image.new("RGBA", size, (40, 120, 160, 220))
    else:
        image = Image.new("RGB", size, (40, 120, 160))
    image.save(path)


def write_sample_repo(root: Path) -> None:
    (root / "sample-course" / "lecture01").mkdir(parents=True)
    (root / "sample-course" / "lecture01" / "images").mkdir(parents=True)
    write_image(root / "sample-course" / "lecture01" / "cover.jpg", (2000, 1000))
    write_image(root / "sample-course" / "lecture01" / "diagram.jpg", (2000, 1000))
    write_image(root / "sample-course" / "lecture01" / "images" / "fallback.png", (1800, 900), mode="RGBA")
    (root / "sample-course" / "lecture01" / "lecture01-notes.pdf").write_bytes(b"%PDF-1.4")
    (root / "sample-course" / "lecture01" / "slides.pdf").write_bytes(b"%PDF-1.4")
    (root / "README.md").write_text(
        """
# AI Course Notes

### Test Courses

| 课程 | 主题 | 讲数 | 讲者 |
|------|------|------|------|
| [**Sample Course**](sample-course/) | Testing conversion | 1 | Test Teacher |
""".strip(),
        encoding="utf-8",
    )
    (root / "sample-course" / "lecture01" / "lecture01-notes.tex").write_text(
        r"""
\documentclass[a4paper]{article}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\newcommand{\notetitle}{Sample Lecture \& Agents}
\newcommand{\noteauthors}{基于 Test Teacher 授课内容整理}
\newcommand{\videopublishdate}{2026-05-04}
\newcommand{\videochannel}{Sample Channel}
\newcommand{\videourl}{https://example.com/watch}
\newcommand{\videocoverpath}{cover.jpg}
\begin{document}
\tableofcontents
\newpage

\section{第一节：为什么需要网页阅读}
这是一个 \textbf{粗体} 段落，包含 inline math $a+b=c$。

\begin{importantbox}{核心概念}
LaTeX 是唯一源文稿，网页由构建脚本生成。
\end{importantbox}

\begin{warningbox}{GQA 压缩比 $\neq$ 推理加速比}
标题里的单符号数学不能吞掉后面的正文转换。
\end{warningbox}

\begin{importantbox}{盒子里的公式}
公式后面的正文不能被 Markdown 当成代码块。
\[
x = y + z
\]
公式后的解释仍然应该留在盒子正文里。
\end{importantbox}

\begin{knowledgebox}{嵌套列表}
\begin{itemize}
    \item 第一层条目
    \begin{itemize}
        \item 第二层条目
    \end{itemize}
\end{itemize}
\end{knowledgebox}

\[
E = mc^2
\]

$$\text{SFT（模仿）: } \hat{p}(y|x) \approx p^*(y|x)$$

其中 $p^*$ 是某个参考分布。单行 display math 之间的正文不应该被吞进公式块。

$$\text{RLHF（优化）: } \max_p \mathbb{E}_p[R(y,x)]$$

\[
\texttt{decode}(\texttt{encode}(x)) = x
\]

行内数学里的等宽命令也要保留：\(\texttt{encode}(x)\)。

\resizebox{0.7\textwidth}{!}{Wrapped LaTeX content}

\[
\text{compression ratio} =
\frac{\text{number of UTF-8 bytes}}{\text{number of tokens}}
\]

\[
M = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix},\quad
v = \begin{pmatrix}1 \\ 2\end{pmatrix}
\]

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{diagram.jpg}
\caption{示意图：网页阅读器结构，缩放 $\sqrt{\text{layers}}$\protect\footnotemark}
\end{figure}
\footnotetext{测试来源。}

数学 caption 后的 \textbf{粗体} 也要继续转换。

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{missing.png}
\caption{缺失图片}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{fallback.png}
\caption{子目录图片}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{slides.pdf}
\caption{PDF 图示}
\end{figure}

\begin{tikzpicture}
\begin{axis}[width=4cm,height=3cm]
\addplot coordinates {(0,0) (1,1)};
\end{axis}
\end{tikzpicture}

\begin{figure}[H]
\centering
\begin{tikzpicture}
\node[draw]{Figure TikZ};
\end{tikzpicture}
\caption{Figure 中的 TikZ}
\end{figure}

参见 \href{../../QUALITY.md}{本地质量文档}，以及 [本地 Markdown 链接](../../QUALITY.md)。

这里有一段带 LaTeX 引号的等宽文本：``\texttt{key1:val1 query:key2}''，后面的列表仍然要正常转换。

普通 LaTeX 英文引号：``From scratch'' 不应该在网页里露出反引号。

嵌套链接：\href{https://example.com/docs}{\nolinkurl{https://example.com/docs}}。

可见空格：\texttt{the\textvisiblespace cat}。

\[
\texttt{a\textvisiblespace b}
\]

%% 这是一行 LaTeX 注释，不应该出现在网页正文。

\begin{itemize}
\item 引号后的列表
\end{itemize}

\begin{tabular}{ll}
\textbf{字段} & \textbf{含义} \\
Title & 页面标题 \\
\end{tabular}

\begin{table}[H]
\centering
\begin{tabular}{ll}
\textbf{包装} & \textbf{结果} \\
table & Markdown 表格 \\
math & $\sim 4\times$ \\
visible & \texttt{a\textvisiblespace b} \\
\multicolumn{2}{l}{\textbf{合计行}} \\
\end{tabular}
\caption{包装表格}
\end{table}

\begin{table}[H]
| 已是 Markdown | 说明 |
| --- | --- |
| table wrapper | 不应回退 |
\end{table}

\begin{center}
\begin{tabular}{ll}
\textbf{中心} & \textbf{内容} \\
A & B \\
\end{tabular}
\end{center}

\begin{quote}
这是一段引用内容。
\end{quote}

\begin{description}
\item[术语] 解释文本。
\item[另一个术语] 更多说明。
\end{description}

\begin{longtable}{ll}
\textbf{Long} & \textbf{Table} \\
A & B \\
\end{longtable}

\begin{tabularx}{\textwidth}{ll}
\textbf{TabularX} & \textbf{Table} \\
X & Y \\
\end{tabularx}

\begin{lstlisting}[language=Python,caption={示例代码}]
print("hello")
\end{lstlisting}

\begin{mystery}
unknown environment body
\end{mystery}
\end{document}
""".strip(),
        encoding="utf-8",
    )


def run_generator(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(GENERATOR),
            "--root",
            str(root),
            "--output",
            str(root / ".web-build"),
            *extra,
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )


def test_generates_mkdocs_site_from_latex_notes(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    build = tmp_path / ".web-build"
    assert (build / "mkdocs.yml").is_file()
    assert (build / "docs" / "index.md").is_file()
    assert (build / "docs" / "sample-course" / "index.md").is_file()
    assert (build / "docs" / "sample-course" / "lecture01" / "index.md").is_file()

    mkdocs_yml = (build / "mkdocs.yml").read_text(encoding="utf-8")
    assert "theme:" in mkdocs_yml
    assert "material" in mkdocs_yml
    assert "https://hqhq1025.github.io/ai-course-notes/" in mkdocs_yml
    assert "repo_name: hqhq1025/ai-course-notes" in mkdocs_yml
    assert "sample-course/index.md" in mkdocs_yml
    assert "sample-course/lecture01/index.md" in mkdocs_yml

    css = (build / "docs" / "assets" / "stylesheets" / "ai-notes.css").read_text(encoding="utf-8")
    assert ".md-grid" in css
    assert "max-width: min(96rem, calc(100vw - 2 * var(--ai-notes-page-gutter)))" in css
    assert ".ai-notes-sidebar-toggle--primary" in css
    assert "body.ai-notes-nav-collapsed .md-sidebar--primary" in css
    assert "body.ai-notes-toc-collapsed .md-sidebar--secondary" in css
    assert ".md-typeset h2" in css
    assert ".md-typeset .arithmatex" in css
    assert ".md-typeset .admonition" in css
    assert ".md-typeset table:not([class])" in css

    sidebar_js = (build / "docs" / "assets" / "javascripts" / "ai-notes.js").read_text(encoding="utf-8")
    assert "ai-notes-sidebar-nav-collapsed" in sidebar_js
    assert "ai-notes-sidebar-toc-collapsed" in sidebar_js
    assert "localStorage" in sidebar_js
    assert "ai-notes-scroll:" in sidebar_js
    assert "history.scrollRestoration" in sidebar_js
    assert "sessionStorage" in sidebar_js
    assert "location.hash" in sidebar_js
    assert "pagehide" in sidebar_js
    assert "DOMContentLoaded" in sidebar_js
    assert "assets/javascripts/ai-notes.js" in mkdocs_yml

    home = (build / "docs" / "index.md").read_text(encoding="utf-8")
    assert "Test Courses" in home
    assert "Sample Course" in home
    assert "1 份讲义" in home
    assert "(sample-course/index.md)" in home

    course = (build / "docs" / "sample-course" / "index.md").read_text(encoding="utf-8")
    assert "# Sample Course" in course
    assert "Sample Lecture & Agents" in course
    assert "lecture01/index.md" in course


def test_converts_latex_constructs_into_readable_markdown(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    page = (
        tmp_path
        / ".web-build"
        / "docs"
        / "sample-course"
        / "lecture01"
        / "index.md"
    ).read_text(encoding="utf-8")

    assert "# Sample Lecture & Agents" in page
    assert "基于 Test Teacher 授课内容整理" in page
    assert "[观看视频](https://example.com/watch)" in page
    assert "[备用 PDF](https://github.com/hqhq1025/ai-course-notes/raw/main/sample-course/lecture01/lecture01-notes.pdf)" in page
    assert "[LaTeX 源码](lecture01-notes.tex)" in page
    assert "## 第一节：为什么需要网页阅读" in page
    assert "**粗体**" in page
    assert "$a+b=c$" in page
    assert '!!! important "核心概念"' in page
    assert '!!! warning "GQA 压缩比 $≠$ 推理加速比"' in page
    assert "标题里的单符号数学不能吞掉后面的正文转换。" in page
    assert '!!! important "盒子里的公式"' in page
    assert "    公式后的解释仍然应该留在盒子正文里。" in page
    assert "    $$" in page
    assert "```\n公式后的解释仍然应该留在盒子正文里。" not in page
    assert '!!! info "嵌套列表"' in page
    assert "第一层条目" in page
    assert "第二层条目" in page
    assert "未转换的 LaTeX 环境：itemize" not in page
    assert "$$" in page and "E = mc^2" in page
    assert r"\text{SFT（模仿）: } \hat{p}(y|x) \approx p^*(y|x)" in page
    assert "其中 $p^*$ 是某个参考分布。单行 display math 之间的正文不应该被吞进公式块。" in page
    assert r"\text{RLHF（优化）: } \max_p \mathbb{E}_p[R(y,x)]" in page
    assert (
        "$$\n"
        r"\text{SFT（模仿）: } \hat{p}(y|x) \approx p^*(y|x)"
        "\n$$\n\n其中 $p^*$ 是某个参考分布。单行 display math"
    ) in page
    assert (
        "不应该被吞进公式块。\n\n$$\n"
        r"\text{RLHF（优化）: } \max_p \mathbb{E}_p[R(y,x)]"
        "\n$$"
    ) in page
    assert r"\texttt{decode}(\texttt{encode}(x)) = x" in page
    assert r"\(\texttt{encode}(x)\)" in page
    assert "Wrapped LaTeX content" in page
    assert r"\resizebox" not in page
    assert r"\text{compression ratio}" in page
    assert r"\frac{\text{number of UTF-8 bytes}}{\text{number of tokens}}" in page
    assert "`decode`(`encode`(x)) = x" not in page
    assert r"\frac{number of UTF-8 bytes}{number of tokens}" not in page
    assert r"\begin{bmatrix}" in page
    assert "未转换的 LaTeX 环境：bmatrix" not in page
    assert "未转换的 LaTeX 环境：pmatrix" not in page
    assert f"![示意图：网页阅读器结构，缩放 $√layers$](diagram.jpg)" in page
    assert "测试来源。" in page
    assert "数学 caption 后的 **粗体** 也要继续转换。" in page
    assert r"数学 caption 后的 \textbf" not in page
    assert "图片资源缺失" in page
    assert "未转换的 LaTeX 环境：figure" not in page
    assert "![子目录图片](images/fallback.png)" in page
    assert "PDF 图示资源" in page
    assert "[打开 PDF 图示](https://github.com/hqhq1025/ai-course-notes/raw/main/sample-course/lecture01/slides.pdf)" in page
    assert "[本地质量文档](../../QUALITY.md)" not in page
    assert "本地质量文档" in page
    assert "[本地 Markdown 链接](../../QUALITY.md)" not in page
    assert "本地 Markdown 链接" in page
    assert "`key1:val1 query:key2`" in page
    assert "“From scratch” 不应该在网页里露出反引号。" in page
    assert "``From scratch''" not in page
    visible_space = "\u2423"
    assert "[https://example.com/docs](https://example.com/docs)" in page
    assert r"\href{" not in page
    assert r"\nolinkurl{" not in page
    assert f"`the{visible_space} cat`" in page
    assert rf"\texttt{{a{visible_space} b}}" in page
    assert r"\textvisiblespace" not in page
    assert "这是一行 LaTeX 注释" not in page
    assert "- 引号后的列表" in page
    assert r"\begin{itemize}" not in page
    assert "| 字段 | 含义 |" in page
    assert "| --- | --- |" in page
    assert "| 包装 | 结果 |" in page
    assert "| table | Markdown 表格 |" in page
    assert "| math | $≈ 4×$ |" in page
    assert f"| visible | a{visible_space} b |" in page
    assert "| 合计行 |" in page
    assert "2l合计行" not in page
    assert '<figcaption class="ai-notes-table-caption">包装表格</figcaption>' in page
    assert "*包装表格*" not in page
    assert "| 已是 Markdown | 说明 |" in page
    assert "| table wrapper | 不应回退 |" in page
    assert "| 中心 | 内容 |" in page
    assert "> 这是一段引用内容。" in page
    assert "- **术语**：解释文本。" in page
    assert "- **另一个术语**：更多说明。" in page
    assert "| Long | Table |" in page
    assert "| TabularX | Table |" in page
    assert "未转换的 LaTeX 环境：table" not in page
    assert "未转换的 LaTeX 环境：center" not in page
    assert "未转换的 LaTeX 环境：quote" not in page
    assert "未转换的 LaTeX 环境：description" not in page
    assert "未转换的 LaTeX 环境：longtable" not in page
    assert "未转换的 LaTeX 环境：tabularx" not in page
    assert '```python title="示例代码"' in page
    assert 'print("hello")' in page
    assert "??? quote \"未转换的 LaTeX 环境：mystery\"" in page

    assert (tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "diagram.jpg").is_file()
    assert (tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "images" / "fallback.png").is_file()
    assert not (tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "lecture01-notes.pdf").exists()
    assert not (tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "slides.pdf").exists()
    assert (tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "lecture01-notes.tex").is_file()


def test_compresses_image_copies_without_touching_sources(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)
    source = tmp_path / "sample-course" / "lecture01" / "diagram.jpg"
    before_size = source.stat().st_size

    result = run_generator(tmp_path, "--strict", "--image-max-width", "640", "--jpeg-quality", "70")

    assert result.returncode == 0, result.stderr
    generated = tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "diagram.jpg"
    with Image.open(source) as image:
        assert image.size == (2000, 1000)
    with Image.open(generated) as image:
        assert image.width == 640
    assert source.stat().st_size == before_size


def test_reuses_compressed_image_cache_without_recompressing(tmp_path: Path, monkeypatch) -> None:
    generator = load_generator_module()
    source = tmp_path / "source.jpg"
    write_image(source, (2000, 1000))
    ctx = generator.BuildContext(
        root=tmp_path,
        output=tmp_path / ".web-build",
        docs_dir=tmp_path / ".web-build" / "docs",
        cache_dir=tmp_path / ".web-build" / ".cache" / "tikz",
        render_tikz=True,
        compress_images=True,
        image_max_width=640,
        jpeg_quality=70,
        image_cache_dir=tmp_path / ".web-build" / ".cache" / "images",
    )
    first_dest = tmp_path / "first" / "source.jpg"
    second_dest = tmp_path / "second" / "source.jpg"

    generator.copy_image_asset(ctx, source, first_dest)

    cache_files = list(ctx.image_cache_dir.glob("image-*.jpg"))
    assert len(cache_files) == 1

    def fail_open(*_args, **_kwargs):
        raise AssertionError("cached image copy should not recompress")

    monkeypatch.setattr(generator.Image, "open", fail_open)

    generator.copy_image_asset(ctx, source, second_dest)

    assert second_dest.read_bytes() == first_dest.read_bytes()


def test_can_disable_image_compression(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict", "--no-compress-images")

    assert result.returncode == 0, result.stderr
    generated = tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01" / "diagram.jpg"
    with Image.open(generated) as image:
        assert image.size == (2000, 1000)


def test_tikz_blocks_render_to_svg_when_tex_tools_are_available(tmp_path: Path) -> None:
    if not shutil.which("xelatex") or not shutil.which("dvisvgm"):
        return

    write_sample_repo(tmp_path)
    tex_path = tmp_path / "sample-course" / "lecture01" / "lecture01-notes.tex"
    tex = tex_path.read_text(encoding="utf-8")
    tex = tex.replace(
        r"\begin{mystery}",
        r"\begin{tikzpicture}\node[draw]{TikZ Test};\end{tikzpicture}" + "\n" + r"\begin{mystery}",
    )
    tex_path.write_text(tex, encoding="utf-8")

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    page = (
        tmp_path
        / ".web-build"
        / "docs"
        / "sample-course"
        / "lecture01"
        / "index.md"
    ).read_text(encoding="utf-8")
    assert "tikz-" in page
    assert ".svg" in page
    assert "Figure 中的 TikZ" in page
    assert r"\caption{Figure 中的 TikZ}" not in page
    assert list((tmp_path / ".web-build" / "docs" / "sample-course" / "lecture01").glob("tikz-*.svg"))


def test_tikz_fallback_does_not_look_like_an_unconverted_error(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict", "--skip-tikz")

    assert result.returncode == 0, result.stderr
    page = (
        tmp_path
        / ".web-build"
        / "docs"
        / "sample-course"
        / "lecture01"
        / "index.md"
    ).read_text(encoding="utf-8")
    assert "TikZ 图暂未渲染" in page
    assert "未转换的 LaTeX 环境：tikzpicture" not in page


def test_tikz_cache_status_reports_missing_then_complete(tmp_path: Path) -> None:
    generator = load_generator_module()
    write_sample_repo(tmp_path)
    ctx = generator.BuildContext(
        root=tmp_path,
        output=tmp_path / ".web-build",
        docs_dir=tmp_path / ".web-build" / "docs",
        cache_dir=tmp_path / ".web-build" / ".cache" / "tikz",
        render_tikz=True,
        compress_images=True,
        image_max_width=1600,
        jpeg_quality=82,
        image_cache_dir=tmp_path / ".web-build" / ".cache" / "images",
    )
    notes = generator.discover_notes(tmp_path)
    entries = generator.tikz_cache_entries(ctx, notes)

    assert len(entries) == 2
    assert generator.print_tikz_cache_status(ctx, notes) == 1

    for entry in entries:
        entry.parent.mkdir(parents=True, exist_ok=True)
        entry.write_text("<svg></svg>", encoding="utf-8")

    assert generator.print_tikz_cache_status(ctx, notes) == 0


def test_can_fail_build_when_tikz_falls_back(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict", "--skip-tikz", "--fail-on-tikz-warnings")

    assert result.returncode == 1
    assert "TikZ diagrams skipped" in result.stdout


def test_tikz_renderer_uses_pdf_pipeline_for_tikz_drawing_specials(tmp_path: Path, monkeypatch) -> None:
    generator = load_generator_module()
    root = tmp_path / "repo"
    note_dir = root / "sample-course" / "lecture01"
    out_dir = tmp_path / "out"
    note_dir.mkdir(parents=True)
    out_dir.mkdir()
    tex_path = note_dir / "lecture01-notes.tex"
    tex_path.write_text(
        r"""
\documentclass{article}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta}
\begin{document}
\end{document}
""".strip(),
        encoding="utf-8",
    )
    note = generator.Note(
        root=root,
        tex_path=tex_path,
        route_dir=Path("sample-course/lecture01"),
        course_dir=Path("sample-course"),
        title="Sample",
    )
    ctx = generator.BuildContext(
        root=root,
        output=tmp_path / "build",
        docs_dir=tmp_path / "build" / "docs",
        cache_dir=tmp_path / "build" / ".cache" / "tikz",
        render_tikz=True,
        compress_images=True,
        image_max_width=1600,
        jpeg_quality=82,
        current_note=note,
        current_out_dir=out_dir,
    )
    block = generator.EnvBlock(
        env="tikzpicture",
        start=0,
        end=0,
        args=[],
        optional_args=[],
        body=r"\node[draw]{A};",
        source=r"\begin{tikzpicture}\node[draw]{A};\end{tikzpicture}",
    )
    calls = []

    def fake_run(cmd, cwd, check, stdout, stderr, text, timeout):
        calls.append(cmd)
        if cmd[0] == "xelatex":
            assert "-no-pdf" not in cmd
            (cwd / "tikz.pdf").write_text("%PDF", encoding="utf-8")
        elif cmd[0] == "dvisvgm":
            assert "--pdf" in cmd
            assert "tikz.pdf" in cmd
            (cwd / "tikz.svg").write_text("<svg></svg>", encoding="utf-8")
        return subprocess.CompletedProcess(cmd, 0)

    monkeypatch.setattr(generator.shutil, "which", lambda name: f"/usr/bin/{name}")
    monkeypatch.setattr(generator.subprocess, "run", fake_run)

    markdown = generator.render_tikz_to_svg(ctx, block)

    assert "TikZ 图暂未渲染" not in markdown
    assert "tikz-" in markdown and ".svg" in markdown
    assert (out_dir / markdown.split("(")[1].split(")")[0]).is_file()
    assert calls[0][0] == "xelatex"
    assert calls[1][0] == "dvisvgm"


def test_tikz_renderer_does_not_reuse_cache_from_old_pipeline(tmp_path: Path, monkeypatch) -> None:
    generator = load_generator_module()
    root = tmp_path / "repo"
    note_dir = root / "sample-course" / "lecture01"
    out_dir = tmp_path / "out"
    note_dir.mkdir(parents=True)
    out_dir.mkdir()
    tex_path = note_dir / "lecture01-notes.tex"
    tex_path.write_text(
        r"""
\documentclass{article}
\usepackage{tikz}
\begin{document}
\end{document}
""".strip(),
        encoding="utf-8",
    )
    note = generator.Note(
        root=root,
        tex_path=tex_path,
        route_dir=Path("sample-course/lecture01"),
        course_dir=Path("sample-course"),
        title="Sample",
    )
    ctx = generator.BuildContext(
        root=root,
        output=tmp_path / "build",
        docs_dir=tmp_path / "build" / "docs",
        cache_dir=tmp_path / "build" / ".cache" / "tikz",
        render_tikz=True,
        compress_images=True,
        image_max_width=1600,
        jpeg_quality=82,
        current_note=note,
        current_out_dir=out_dir,
    )
    block = generator.EnvBlock(
        env="tikzpicture",
        start=0,
        end=0,
        args=[],
        optional_args=[],
        body=r"\node[draw]{A};",
        source=r"\begin{tikzpicture}\node[draw]{A};\end{tikzpicture}",
    )
    preamble = generator.tikz_preamble_for_note(ctx, note)
    old_digest = generator.hashlib.sha256((preamble + "\n" + block.source).encode("utf-8")).hexdigest()[:16]
    ctx.cache_dir.mkdir(parents=True)
    (ctx.cache_dir / f"tikz-{old_digest}.svg").write_text("<svg>old renderer</svg>", encoding="utf-8")
    calls = []

    def fake_run(cmd, cwd, check, stdout, stderr, text, timeout):
        calls.append(cmd)
        if cmd[0] == "xelatex":
            (cwd / "tikz.pdf").write_text("%PDF", encoding="utf-8")
        elif cmd[0] == "dvisvgm":
            (cwd / "tikz.svg").write_text("<svg>new renderer</svg>", encoding="utf-8")
        return subprocess.CompletedProcess(cmd, 0)

    monkeypatch.setattr(generator.shutil, "which", lambda name: f"/usr/bin/{name}")
    monkeypatch.setattr(generator.subprocess, "run", fake_run)

    markdown = generator.render_tikz_to_svg(ctx, block)
    generated = (out_dir / markdown.split("(")[1].split(")")[0]).read_text(encoding="utf-8")

    assert calls
    assert "new renderer" in generated
    assert "old renderer" not in generated


def test_tikz_renderer_rejects_svg_with_page_footer_artifacts(tmp_path: Path, monkeypatch) -> None:
    generator = load_generator_module()
    root = tmp_path / "repo"
    note_dir = root / "sample-course" / "lecture01"
    out_dir = tmp_path / "out"
    note_dir.mkdir(parents=True)
    out_dir.mkdir()
    tex_path = note_dir / "lecture01-notes.tex"
    tex_path.write_text(
        r"""
\documentclass{article}
\usepackage{tikz}
\begin{document}
\end{document}
""".strip(),
        encoding="utf-8",
    )
    note = generator.Note(
        root=root,
        tex_path=tex_path,
        route_dir=Path("sample-course/lecture01"),
        course_dir=Path("sample-course"),
        title="Sample",
    )
    ctx = generator.BuildContext(
        root=root,
        output=tmp_path / "build",
        docs_dir=tmp_path / "build" / "docs",
        cache_dir=tmp_path / "build" / ".cache" / "tikz",
        render_tikz=True,
        compress_images=True,
        image_max_width=1600,
        jpeg_quality=82,
        current_note=note,
        current_out_dir=out_dir,
    )
    block = generator.EnvBlock(
        env="tikzpicture",
        start=0,
        end=0,
        args=[],
        optional_args=[],
        body=r"\node[draw]{A};",
        source=r"\begin{tikzpicture}\node[draw]{A};\end{tikzpicture}",
    )

    def fake_run(cmd, cwd, check, stdout, stderr, text, timeout):
        if cmd[0] == "xelatex":
            (cwd / "tikz.pdf").write_text("%PDF", encoding="utf-8")
        elif cmd[0] == "dvisvgm":
            (cwd / "tikz.svg").write_text(
                f"<svg><a xlink:href='{generator.REPO_URL}'>AI Course Notes</a></svg>",
                encoding="utf-8",
            )
        return subprocess.CompletedProcess(cmd, 0)

    monkeypatch.setattr(generator.shutil, "which", lambda name: f"/usr/bin/{name}")
    monkeypatch.setattr(generator.subprocess, "run", fake_run)

    markdown = generator.render_tikz_to_svg(ctx, block)

    assert "TikZ 图暂未渲染" in markdown
    assert any(warning.kind == "tikz_failed" for warning in ctx.warnings)


def test_inline_triple_backticks_do_not_mark_rest_as_fenced_code() -> None:
    generator = load_generator_module()
    text = "考虑关联检索任务：```key1:val1 key2:val2`'' 后面还有正文\n\\begin{itemize}\n"

    assert not generator.inside_fenced_code(text, text.index(r"\begin{itemize}"))


def test_default_output_summarizes_warnings_without_flooding(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict")

    assert result.returncode == 0, result.stderr
    assert "Warning summary:" in result.stdout
    assert "Missing assets: 1" in result.stdout
    assert "missing.png" not in result.stdout
    assert "--verbose-warnings" in result.stdout


def test_verbose_warnings_show_detailed_messages(tmp_path: Path) -> None:
    write_sample_repo(tmp_path)

    result = run_generator(tmp_path, "--strict", "--verbose-warnings")

    assert result.returncode == 0, result.stderr
    assert "missing.png" in result.stdout


def test_pages_workflow_installs_tikz_font_dependencies_and_fails_on_fallback() -> None:
    workflow = (REPO_ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")

    assert "cancel-in-progress: true" in workflow
    assert "cache: pip" in workflow
    assert "actions/cache@v4" in workflow
    assert ".web-build/.cache" in workflow
    assert "--check-tikz-cache" in workflow
    assert "if: steps.tikz-cache.outputs.complete != 'true'" in workflow
    assert "mupdf-tools" in workflow
    assert "texlive-fonts-recommended" in workflow
    assert "--fail-on-tikz-warnings" in workflow
    assert "--verbose-warnings" in workflow

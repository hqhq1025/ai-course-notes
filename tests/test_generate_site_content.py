"""Body-content conversion: display math, tables, lists, headings, prose commands and the leak check.

The assertions look at the HTML that Python-Markdown produces with the site's extensions, because most of
these defects were valid-looking Markdown that rendered as raw text or flattened structure.
"""

import importlib.util
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPO_ROOT / "tools" / "web" / "generate_site.py"


def load_generator_module():
    spec = importlib.util.spec_from_file_location("generate_site", GENERATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


generator = load_generator_module()

# MkDocs always adds toc, tables and fenced_code; the rest mirrors generate_mkdocs_yml.
SITE_EXTENSIONS = [
    "toc",
    "tables",
    "fenced_code",
    "admonition",
    "attr_list",
    "md_in_html",
    "pymdownx.details",
    "pymdownx.superfences",
    "pymdownx.arithmatex",
]


class Node:
    def __init__(self, tag: str, attrs: dict[str, str], parent: "Node | None") -> None:
        self.tag = tag
        self.attrs = attrs
        self.parent = parent
        self.children: list["Node | str"] = []

    @property
    def classes(self) -> list[str]:
        return (self.attrs.get("class") or "").split()

    def find_all(self, tag: str | None = None, cls: str | None = None) -> list["Node"]:
        found = []
        for child in self.children:
            if isinstance(child, Node):
                if (tag is None or child.tag == tag) and (cls is None or cls in child.classes):
                    found.append(child)
                found.extend(child.find_all(tag, cls))
        return found

    def text(self) -> str:
        return "".join(child if isinstance(child, str) else child.text() for child in self.children)


class TreeBuilder(HTMLParser):
    VOID = {"br", "img", "hr", "input", "meta", "link", "source"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {}, None)
        self.current = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, {key: value or "" for key, value in attrs}, self.current)
        self.current.children.append(node)
        if tag not in self.VOID:
            self.current = node

    def handle_endtag(self, tag):
        node = self.current
        while node is not None and node.tag != tag:
            node = node.parent
        if node is not None and node.parent is not None:
            self.current = node.parent

    def handle_data(self, data):
        self.current.children.append(data)


def render(markdown_text: str) -> tuple[Node, list[dict]]:
    md = markdown.Markdown(extensions=SITE_EXTENSIONS, extension_configs={"pymdownx.arithmatex": {"generic": True}})
    html = md.convert(markdown_text)
    builder = TreeBuilder()
    builder.feed(html)
    return builder.root, md.toc_tokens


def flat_toc(tokens: list[dict]) -> list[str]:
    names = []
    for token in tokens:
        names.append(token["name"])
        names.extend(flat_toc(token["children"]))
    return names


def make_ctx(tmp_path: Path):
    return generator.BuildContext(
        root=tmp_path,
        output=tmp_path / "out",
        docs_dir=tmp_path / "out" / "docs",
        cache_dir=tmp_path / "cache",
        render_tikz=False,
        compress_images=False,
        image_max_width=1600,
        jpeg_quality=82,
    )


def convert(fragment: str, tmp_path: Path) -> str:
    return generator.convert_latex_fragment(fragment, make_ctx(tmp_path))


def prose_text(root: Node) -> str:
    """Visible text outside math and code."""
    parts = []

    def walk(node: Node) -> None:
        for child in node.children:
            if isinstance(child, str):
                parts.append(child)
            elif child.tag not in {"code", "pre"} and "arithmatex" not in child.classes:
                walk(child)

    walk(root)
    return "".join(parts)


def test_display_math_glued_to_text_and_other_formulas_renders_as_blocks(tmp_path: Path) -> None:
    page = convert(
        "就是：\n$$\nQ=XW_Q,\\qquad K=XW_K.\n$$\n后面的说明。\n$$a_1 = 1$$\n$$b_2 = 2$$\n"
        "\\begin{itemize}\n\\item 条目\n\\end{itemize}\n",
        tmp_path,
    )
    root, _ = render(page)

    blocks = root.find_all("div", "arithmatex")
    assert [block.text().split() for block in blocks] == [
        ["\\[", "Q=XW_Q,\\qquad", "K=XW_K.", "\\]"],
        ["\\[", "a_1", "=", "1", "\\]"],
        ["\\[", "b_2", "=", "2", "\\]"],
    ]
    assert "$" not in prose_text(root)
    assert [p.text() for p in root.find_all("p")] == ["就是：", "后面的说明。"]


def test_display_math_inside_list_items_stays_in_the_item_and_is_wrapped_once(tmp_path: Path) -> None:
    page = convert(
        "\\begin{enumerate}\n"
        "\\item 更新权重：\\[ W \\leftarrow W - \\eta g \\] 其中 $\\eta$ 是学习率\n"
        "\\item 联合目标\n\\begin{align}\nx &= 1 \\\\\ny &= 2\n\\end{align}\n"
        "\\item 重复步骤 2--3 直到收敛\n"
        "\\end{enumerate}\n",
        tmp_path,
    )
    root, _ = render(page)

    (ordered,) = root.find_all("ol")
    items = [child for child in ordered.children if isinstance(child, Node) and child.tag == "li"]
    assert len(items) == 3
    first_math = items[0].find_all("div", "arithmatex")
    assert len(first_math) == 1 and "\\leftarrow" in first_math[0].text()
    assert "其中" in items[0].text() and "学习率" in items[0].text()
    second_math = items[1].find_all("div", "arithmatex")
    assert len(second_math) == 1
    assert second_math[0].text().count("\\begin{align}") == 1 and "$" not in second_math[0].text()
    assert "重复步骤 2–3 直到收敛" in items[2].text()


def test_nested_lists_render_as_nested_html_lists(tmp_path: Path) -> None:
    page = convert(
        "\\begin{enumerate}\n"
        "\\item \\textbf{特征学习阶段}：\n"
        "  \\begin{itemize}\n  \\item 通过卷积学习特征\n  \\item 通过池化降低维度\n  \\end{itemize}\n"
        "\\item \\textbf{分类阶段}：输出概率\n"
        "\\end{enumerate}\n",
        tmp_path,
    )
    root, _ = render(page)

    (ordered,) = root.find_all("ol")
    items = [child for child in ordered.children if isinstance(child, Node) and child.tag == "li"]
    assert len(items) == 2
    (nested,) = items[0].find_all("ul")
    assert [li.text().strip() for li in nested.find_all("li")] == ["通过卷积学习特征", "通过池化降低维度"]
    assert items[1].find_all("ul") == []


def test_table_cells_keep_math_and_formatting_and_split_only_on_real_ampersands(tmp_path: Path) -> None:
    page = convert(
        "表格紧跟在这一行后面：\n"
        "\\begin{tabular}{lll}\n\\toprule\n"
        "函数 & 公式 & 说明 \\\\\n\\midrule\n"
        "Sigmoid & $\\frac{1}{1+e^{-z}}$ & \\textbf{平滑} \\\\\n"
        "Norm & $\\left\\| x \\right\\|$ 与 $|x|$ & Chen \\& Manning \\\\\n"
        "代码 & \\texttt{a|b} & 竖线 a | b \\\\\n"
        "单位成本 & \\texttt{每次调用成本 $\\times$ 调用次数} & x \\\\\n"
        "\\multicolumn{2}{l}{\\emph{合计}} & 3 \\\\\n"
        "\\bottomrule\n\\end{tabular}\n",
        tmp_path,
    )
    root, _ = render(page)

    (table,) = root.find_all("table")
    assert [th.text() for th in table.find_all("th")] == ["函数", "公式", "说明"]
    rows = [tr for tr in table.find_all("tr") if tr.find_all("td")]
    assert all(len(row.find_all("td")) == 3 for row in rows)
    cells = [[td for td in row.find_all("td")] for row in rows]
    assert cells[0][1].find_all("span", "arithmatex")[0].text() == "\\(\\frac{1}{1+e^{-z}}\\)"
    assert cells[0][2].find_all("strong")[0].text() == "平滑"
    norm_math = [span.text() for span in cells[1][1].find_all("span", "arithmatex")]
    assert len(norm_math) == 2 and "\\left\\|" in norm_math[0] and "x" in norm_math[1]
    assert cells[1][2].text() == "Chen & Manning"
    assert cells[2][1].find_all("code")[0].text() == "a|b"
    assert cells[2][2].text() == "竖线 a | b"
    # Math inside \texttt stays math between the code spans, as LaTeX prints it.
    assert [code.text() for code in cells[3][1].find_all("code")] == ["每次调用成本", "调用次数"]
    assert cells[3][1].find_all("span", "arithmatex")[0].text() == "\\(\\times\\)"
    assert cells[4][0].find_all("em")[0].text() == "合计" and cells[4][1].text() == "" and cells[4][2].text() == "3"


def test_longtable_keeps_one_header_and_shows_its_caption(tmp_path: Path) -> None:
    page = convert(
        "\\begin{longtable}{ll}\n"
        "\\caption{术语表，含 $\\alpha$}\\\\\n\\toprule\n\\textbf{术语} & \\textbf{解释} \\\\\n\\midrule\n\\endfirsthead\n"
        "\\toprule\n\\textbf{术语} & \\textbf{解释} \\\\\n\\midrule\n\\endhead\n"
        "Agent & 行动者 \\\\\nTool & 工具 \\\\\n\\bottomrule\n\\end{longtable}\n",
        tmp_path,
    )
    root, _ = render(page)

    (table,) = root.find_all("table")
    assert [th.text() for th in table.find_all("th")] == ["术语", "解释"]
    assert [[td.text() for td in tr.find_all("td")] for tr in table.find_all("tr")[1:]] == [["Agent", "行动者"], ["Tool", "工具"]]
    (caption,) = root.find_all("figcaption")
    assert caption.text().startswith("术语表，含") and caption.find_all("span", "arithmatex")[0].text() == "\\(\\alpha\\)"


def test_headings_and_box_titles_keep_math_and_nested_braces(tmp_path: Path) -> None:
    page = convert(
        "\\section{Claude vs.\\ Codex：AI $\\supset$ ML $\\supset$ DL}\n正文。\n"
        "\\subsection{\\texorpdfstring{$\\pi_{0.7}$}{pi0.7}：多模态 \\textbf{context {in} use}}\n正文。\n"
        "\\begin{importantbox}{GQA 压缩比 $\\neq$ 推理加速比}\n盒子正文。\n\\end{importantbox}\n",
        tmp_path,
    )
    root, toc = render(page)

    (h2,) = root.find_all("h2")
    assert [span.text() for span in h2.find_all("span", "arithmatex")] == ["\\(\\supset\\)", "\\(\\supset\\)"]
    (h3,) = root.find_all("h3")
    assert h3.find_all("span", "arithmatex")[0].text() == "\\(\\pi_{0.7}\\)"
    assert h3.find_all("strong")[0].text() == "context in use"
    # The sidebar TOC is plain text, so math headings carry a readable label instead of raw TeX.
    assert h2.text().startswith("Claude vs. Codex：AI ")
    assert flat_toc(toc) == ["Claude vs. Codex：AI ⊃ ML ⊃ DL", "pi0.7：多模态 context in use"]
    (title,) = root.find_all("p", "admonition-title")
    assert title.find_all("span", "arithmatex")[0].text() == "\\(\\neq\\)"
    assert "\\section" not in page and "\\texorpdfstring" not in page


def test_prose_commands_become_text_instead_of_leaking(tmp_path: Path) -> None:
    page = convert(
        "第一行\\\\\n第二行\\\\[0.3em]\n第三行\\\\\n\n"
        "引用 {[}1{]}；Tobias L\\\"{u}tke、Na\\\"ive、entart\\'{e}、von K\\'arm\\'an。\n\n"
        "\\begingroup\\footnotesize 小字说明\\endgroup\n"
        "\\renewcommand{\\baselinestretch}{0.92}\\selectfont\n"
        "模型回答：280 \\quad {\\color{red}（错误）}，填空 \\underline{\\hspace{1cm}}。\n\n"
        "标签 \\verb|builtin_gelu| 与 \\texttt{\\~{}/.codex/agents.md}，规模 10\\^{}10，"
        "格式 \\textbackslash n，路径 \\path{django/contrib/admin/sites.py}，集合 \\{a, b\\}，字段 `task\\_id`。\n",
        tmp_path,
    )
    root, _ = render(page)

    assert generator.latex_command_leaks(page) == {}
    paragraphs = root.find_all("p")
    assert [child for child in paragraphs[0].children if isinstance(child, str)] == ["第一行", "\n第二行", "\n第三行"]
    assert len(paragraphs[0].find_all("br")) == 2
    text = root.text()
    assert "引用 [1]；Tobias Lütke、Naïve、entarté、von Kármán。" in text
    assert "小字说明" in text and "baselinestretch" not in text and "0.92" not in text
    assert "模型回答：280 （错误）" in " ".join(text.split())
    assert [code.text() for code in root.find_all("code")] == [
        "builtin_gelu",
        "~/.codex/agents.md",
        "django/contrib/admin/sites.py",
        "task_id",
    ]
    assert "规模 10^10" in text and "格式 \\n" in text and "集合 {a, b}" in text
    assert root.find_all("u")


def test_latex_dashes_become_unicode_dashes_only_in_prose(tmp_path: Path) -> None:
    page = convert(
        "步骤 2--3，1974--1980 年，90\\%--95\\%，encoder--decoder，编码器--解码器，新前沿 I -- Diffusion，"
        "ICLR 2014 --- VAE，机制---只在需要时加载，第三类范式------强化学习。"
        "命令 \\texttt{git log --oneline} 和 run --depth 2，箭头 A --> B，"
        "链接 \\url{https://example.com/a--b} 与 \\href{https://example.com/c--d}{文档}。\n\n"
        "\\begin{tabular}{ll}\nA & B \\\\\n1--2 & x \\\\\n\\end{tabular}\n",
        tmp_path,
    )
    root, _ = render(page)

    text = root.find_all("p")[0].text()
    for converted in ["步骤 2–3", "1974–1980 年", "90%–95%", "encoder–decoder", "编码器–解码器", "新前沿 I – Diffusion",
                      "ICLR 2014 — VAE", "机制—只在需要时加载", "第三类范式——强化学习"]:
        assert converted in text
    assert "run --depth 2" in text and "A --> B" in text
    assert [code.text() for code in root.find_all("code")] == ["git log --oneline"]
    assert [a.attrs["href"] for a in root.find_all("a")] == ["https://example.com/a--b", "https://example.com/c--d"]
    (table,) = root.find_all("table")
    assert [td.text() for td in table.find_all("td")] == ["1–2", "x"]


def test_preamble_tcolorbox_becomes_admonition_and_multicols_passes_content_through(tmp_path: Path) -> None:
    note_dir = tmp_path / "articles" / "sample"
    note_dir.mkdir(parents=True)
    tex_path = note_dir / "sample-notes.tex"
    tex_path.write_text(
        "\\documentclass{article}\n"
        "\\newtcolorbox{translationbox}[1]{\n  enhanced, colback=black!2!white, title=#1, breakable\n}\n"
        "\\newtcolorbox{plainbox}{colback=white}\n"
        "\\begin{document}\n\\end{document}\n",
        encoding="utf-8",
    )
    ctx = make_ctx(tmp_path)
    ctx.current_note = generator.parse_note(tmp_path, tex_path)

    page = generator.convert_latex_fragment(
        "\\begin{translationbox}{原文主线编译：$x^2$}\n译文 \\textbf{重点}。\n\\end{translationbox}\n"
        "\\begin{plainbox}\n无标题盒子。\n\\end{plainbox}\n"
        "\\begin{multicols}{2}\n\\begin{itemize}\n\\item 思考题一\n\\columnbreak\n\\item 思考题二\n\\end{itemize}\n\\end{multicols}\n",
        ctx,
    )
    root, _ = render(page)

    assert "未转换的 LaTeX 环境" not in page
    boxes = root.find_all("div", "admonition")
    assert len(boxes) == 2
    (title,) = boxes[0].find_all("p", "admonition-title")
    assert title.text().startswith("原文主线编译：") and title.find_all("span", "arithmatex")
    assert boxes[0].find_all("strong")[0].text() == "重点"
    assert boxes[1].find_all("p", "admonition-title") == [] and "无标题盒子。" in boxes[1].text()
    assert [li.text().strip() for li in root.find_all("li")] == ["思考题一", "思考题二"]


def test_math_and_code_protection_restores_nested_placeholders() -> None:
    # \(...\) is protected first; the inline $...$ around it is protected later and holds that placeholder.
    text = "前文 $a + \\(b\\) + c$ 后文 \\(d\\)"

    result = generator.transform_outside_math_and_code(text, lambda prose: prose.replace("前文", "PRE"))

    assert result == "PRE $a + \\(b\\) + c$ 后文 \\(d\\)"
    assert "@@AI_NOTES" not in result


def write_leak_repo(root: Path) -> None:
    note_dir = root / "course" / "lecture01"
    note_dir.mkdir(parents=True)
    (note_dir / "lecture01-notes.tex").write_text(
        "\\documentclass{article}\n\\newcommand{\\notetitle}{Leak Lecture}\n\\begin{document}\n"
        "正文里有未知命令 \\foobar{参数}，数学 $\\alpha$ 与代码 \\verb|\\notaleak| 不算。\n"
        "\\begin{lstlisting}\n\\alsonotaleak\n\\end{lstlisting}\n"
        "\\end{document}\n",
        encoding="utf-8",
    )


def run_generator(root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GENERATOR), "--root", str(root), "--output", str(root / ".web-build"), *extra],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )


def test_build_reports_latex_left_in_prose_and_can_fail_on_it(tmp_path: Path) -> None:
    write_leak_repo(tmp_path)

    report = run_generator(tmp_path, "--strict", "--verbose-warnings")
    failing = run_generator(tmp_path, "--strict", "--fail-on-latex-leaks")

    assert report.returncode == 0, report.stderr
    assert "Pages with LaTeX commands left in prose: 1" in report.stdout
    detail = [line for line in report.stdout.splitlines() if "LaTeX commands left in prose of" in line]
    assert detail == ["- 1 LaTeX commands left in prose of course/lecture01/lecture01-notes.tex: \\foobar×1"]
    assert failing.returncode == 1


def test_math_with_less_than_before_a_letter_does_not_swallow_the_next_figure(tmp_path: Path) -> None:
    from PIL import Image

    note_dir = tmp_path / "course" / "lecture01"
    note_dir.mkdir(parents=True)
    Image.new("RGB", (40, 20), (40, 120, 160)).save(note_dir / "frame.jpg")
    (note_dir / "lecture01-notes.tex").write_text(
        "\\documentclass{article}\n\\newcommand{\\notetitle}{Angle Lecture}\n\\begin{document}\n"
        "静态序列建模学习 $p(x_t\\mid x_{<t})$，决策序列建模学习\n"
        "\\[\np(a_t\\mid s_{\\le t},a_{<t}).\n\\]\n"
        "\\begin{figure}[H]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{frame.jpg}\n"
        "\\caption{序列建模示意}\n\\end{figure}\n"
        "图后的正文：当 batch size $< $ noise scale。\n\\end{document}\n",
        encoding="utf-8",
    )

    result = run_generator(tmp_path, "--strict")
    page = (tmp_path / ".web-build" / "docs" / "course" / "lecture01" / "index.md").read_text(encoding="utf-8")
    root, _ = render(page)

    assert result.returncode == 0, result.stderr
    (figure,) = root.find_all("figure")
    assert figure.parent is root
    (image,) = figure.find_all("img")
    assert image.attrs["alt"] == "序列建模示意"
    inline = root.find_all("span", "arithmatex")[0].text()
    display = root.find_all("div", "arithmatex")[0].text()
    assert inline.replace(" ", "") == "\\(p(x_t\\midx_{<t})\\)"
    assert "a_{<" in display.replace(" ", "")
    # Arithmatex does not close $...$ after a space, so "$< $" must lose that space to render.
    last = root.find_all("p")[-1]
    assert last.text().startswith("图后的正文：当 batch size")
    assert [span.text() for span in last.find_all("span", "arithmatex")] == ["\\(<\\)"]

"""Render Argon's finished interview notes as TeX and Markdown."""

import argparse
import importlib.util
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


EPISODE = Path(__file__).resolve().parent.parent
REPO = EPISODE.parents[2]
STEM = "BV1CAHV6PEPM-notes"
SOURCE_URL = "https://www.bilibili.com/video/BV1CAHV6PEPM/"
NOTE_DATE = "2026-10-26"
HOST = "Koji 杨远骋"
GUEST = "李磊（香港大学在读博士、小米 MiMo 研究员）"

_spec = importlib.util.spec_from_file_location(
    "course_render", REPO / "tools/scripts/nju_gse_argon/render_notes.py"
)
_renderer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_renderer)
esc = _renderer.esc


def prose(text):
    """Keep display math, Markdown emphasis, and lists in Argon's prose."""
    parts = re.split(r"(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\])", str(text))
    return "\n".join(
        "\\[\n" + part[2:-2].strip() + "\n\\]"
        if part.startswith(("$$", r"\["))
        else re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\\textit{\1}", _renderer.prose(part))
        for part in parts
        if part
    )


def web_image(path):
    image = Path(path)
    if image.suffix.lower() in {".png", ".jpg", ".jpeg"}:
        return image.as_posix()
    for suffix in (".png", ".jpg", ".jpeg"):
        candidate = image.with_suffix(suffix)
        if (EPISODE / candidate).is_file():
            return candidate.as_posix()
    raise ValueError(f"Web figure needs a PNG or JPEG: {path}")


def validate_figure(figure):
    for key in ("path", "caption", "before", "reading", "after"):
        if not isinstance(figure.get(key), str) or not figure[key].strip():
            raise ValueError(f"Figure is missing {key}")
    path = figure["path"]
    image = (EPISODE / path).resolve()
    if not image.is_relative_to(EPISODE) or not image.is_file():
        raise ValueError(f"Missing local figure: {path}")
    if re.search(r"[^A-Za-z0-9_./-]", path):
        raise ValueError(f"Figure path needs a portable ASCII filename: {path}")
    if figure.get("source_interval") and not isinstance(figure["source_interval"], str):
        raise ValueError("source_interval must be a timestamp interval string")
    web_image(path)


def validate(book):
    for key in ("title", "lead", "conclusion"):
        if not isinstance(book.get(key), str) or not book[key].strip():
            raise ValueError(f"Missing text: {key}")
    if not book.get("sections"):
        raise ValueError("No sections")
    for number, section in enumerate(book["sections"], 1):
        for key in ("title", "intro", "summary"):
            if not isinstance(section.get(key), str) or not section[key].strip():
                raise ValueError(f"Section {number}: missing {key}")
        if not section.get("units"):
            raise ValueError(f"Section {number}: no units")
        for unit in section["units"]:
            if not unit.get("title") or not unit.get("paragraphs") or not all(
                isinstance(p, str) and p.strip() for p in unit["paragraphs"]
            ):
                raise ValueError(f"Section {number}: incomplete unit")
            for figure in unit.get("figures", []):
                validate_figure(figure)
        for box in section.get("boxes", []):
            if box["kind"] not in {"importantbox", "knowledgebox", "warningbox"}:
                raise ValueError(f"Unknown box kind: {box['kind']}")
        table = section.get("table")
        if table and (
            not table["headers"]
            or any(len(row) != len(table["headers"]) for row in table["rows"])
        ):
            raise ValueError(f"Section {number}: uneven table")
        if section.get("figure"):
            validate_figure(section["figure"])
    for reference in book.get("references", []):
        if not re.match(r"^https?://[^\s{}\\]+$", reference["url"]):
            raise ValueError(f"Invalid reference URL: {reference['url']}")


def append_figure(tex, md, figure):
    tex += [
        prose(figure["before"]),
        r"\par\noindent\begin{minipage}{\linewidth}",
        r"\setlength{\intextsep}{3pt}",
    ]
    interval = figure.get("source_interval")
    if interval:
        tex += [
            r"\videofigure{" + figure["path"] + "}{" + esc(figure["caption"])
            + "}{" + esc(interval) + "}"
        ]
    else:
        tex += [
            r"\begin{figure}[H]\centering",
            r"\includegraphics[width=\linewidth,height=.58\textheight,keepaspectratio]{"
            + figure["path"] + "}",
            r"\caption{" + esc(figure["caption"]) + "}",
            r"\end{figure}",
        ]
    tex += [
        r"\begin{knowledgebox}[breakable=false]{读图}", prose(figure["reading"]),
        r"\end{knowledgebox}", r"\end{minipage}\par", prose(figure["after"]),
    ]
    md += [
        figure["before"], "",
        "![" + figure["caption"] + "](" + web_image(figure["path"]) + ")", "",
    ]
    if interval:
        md += [f"来源：[原视频]({SOURCE_URL})，讲解区间 {interval}。", ""]
    md += ["> 读图", ">", "> " + figure["reading"].replace("\n", "\n> "), "", figure["after"], ""]


def append_table(tex, md, table):
    columns = len(table["headers"])
    width = rf"\dimexpr(\linewidth-{2 * columns}\tabcolsep)/{columns}\relax"
    spec = (r">{\raggedright\arraybackslash}p{" + width + "}") * columns
    header = " & ".join(esc(h) for h in table["headers"]) + r"\\\midrule"
    tex += [
        r"\begingroup\small\setlength{\LTcapwidth}{\linewidth}",
        r"\begin{longtable}{" + spec + "}",
        r"\caption{" + esc(table["caption"]) + r"}\\",
        r"\toprule", header, r"\endfirsthead", r"\toprule", header, r"\endhead",
    ]
    tex += [" & ".join(esc(cell) for cell in row) + r"\\[4pt]" for row in table["rows"]]
    tex += [r"\bottomrule\end{longtable}\endgroup"]
    cell = lambda value: str(value).replace("|", "\\|").replace("\n", "<br>")
    md += [table["caption"], "", "| " + " | ".join(map(cell, table["headers"])) + " |", "|" + "---|" * columns]
    md += ["| " + " | ".join(map(cell, row)) + " |" for row in table["rows"]] + [""]


def render(book_path):
    book = json.loads(book_path.read_text(encoding="utf-8"))
    validate(book)
    info = json.loads((EPISODE / "sources/source.info.json").read_text(encoding="utf-8"))
    public_date = datetime.fromtimestamp(info["pubdate"], ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
    preamble = _renderer.PREAMBLE.replace("南京大学 · 生成式软件工程 2026", "十字路口 · 访谈学习笔记")
    preamble = preamble.replace(
        r"\newtcolorbox{knowledgebox}[1]{enhanced,breakable,colback=teal!3,colframe=teal!50!black,title={#1},fonttitle=\bfseries}",
        r"\newtcolorbox{knowledgebox}[2][]{enhanced,breakable,colback=teal!3,colframe=teal!50!black,title={#2},fonttitle=\bfseries,#1}",
    )
    # Captions can be measured twice, so emit the local footnote after the caption.
    videofigure = r"""\newcommand{\videofigure}[4][1]{%
\begin{figure}[H]\centering
\begin{minipage}{\linewidth}\centering
\includegraphics[width=#1\linewidth,height=.50\textheight,keepaspectratio]{#2}
\caption[#3]{#3\textsuperscript{\textit{a}}}
\footnotetext[1]{视频讲解区间：#4。}
\end{minipage}
\end{figure}}
"""
    macros = {
        "notetitle": esc(book["title"]), "videocoverpath": "cover.jpg",
        "videourl": SOURCE_URL, "videochannel": "十字路口",
        "videopublishdate": public_date, "notedate": NOTE_DATE,
        "noteauthors": esc(HOST + "、李磊"), "sourceurl": SOURCE_URL,
    }
    definitions = "\n".join("\\newcommand{\\" + key + "}{" + value + "}" for key, value in macros.items())
    preamble = preamble.replace(r"\begin{document}", definitions + "\n" + videofigure + r"\begin{document}")
    tex = [
        preamble, r"\begin{titlepage}\centering\vspace*{4mm}",
        r"{\Large 十字路口 · 访谈学习笔记\par}\vspace{8mm}",
        r"{\LARGE\bfseries \notetitle\par}\vspace{7mm}",
        r"\includegraphics[width=.86\linewidth,height=.27\textheight,keepaspectratio]{cover.jpg}",
        r"\par\vspace{6mm}{\small 原节目：" + esc(info["title"]) + r"\par}",
        r"\vspace{4mm}主持：" + esc(HOST) + r"\par",
        r"{\small 嘉宾：" + esc(GUEST) + r"\par}",
        r"\vfill 发布：" + public_date + r"\par",
        "整理：" + NOTE_DATE + r"\quad 正文：Gemini Argon\quad 配图与编校：Codex\par",
        r"\vspace{4mm}\url{" + SOURCE_URL + "}", r"\end{titlepage}",
        r"\begingroup\small\setlength{\parskip}{0pt}\tableofcontents\endgroup\clearpage",
        r"\section*{导读}\addcontentsline{toc}{section}{导读}", prose(book["lead"]),
    ]
    md = [
        "# " + book["title"], "", "原节目：" + info["title"], "",
        f"主持：{HOST}。嘉宾：{GUEST}。", "",
        f"发布：{public_date}。整理：{NOTE_DATE}。", "",
        "正文：Gemini Argon。配图与编校：Codex。", "",
        f"[观看原节目]({SOURCE_URL})", "", "## 导读", "", book["lead"], "",
    ]
    for section in book["sections"]:
        tex += [r"\needspace{6\baselineskip}\section{" + esc(section["title"]) + "}", prose(section["intro"])]
        md += ["## " + section["title"], "", section["intro"], ""]
        for unit in section["units"]:
            tex += [r"\needspace{5\baselineskip}\subsection{" + esc(unit["title"]) + "}"]
            md += ["### " + unit["title"], ""]
            for paragraph in unit["paragraphs"]:
                tex += [prose(paragraph), ""]
                md += [paragraph, ""]
            for figure in unit.get("figures", []):
                append_figure(tex, md, figure)
        for box in section.get("boxes", []):
            tex += [r"\begin{" + box["kind"] + "}{" + esc(box["title"]) + "}", prose(box["text"]), r"\end{" + box["kind"] + "}"]
            md += ["> **" + box["title"] + "**", ">", "> " + box["text"].replace("\n", "\n> "), ""]
        if section.get("table"):
            append_table(tex, md, section["table"])
        if section.get("figure"):
            append_figure(tex, md, section["figure"])
        tex += [r"\needspace{4\baselineskip}\subsection{本章小结}", prose(section["summary"])]
        md += ["### 本章小结", "", section["summary"], ""]
    tex += [r"\needspace{6\baselineskip}\section{总结与延伸}", prose(book["conclusion"])]
    md += ["## 总结与延伸", "", book["conclusion"], ""]
    if book.get("references"):
        tex += [r"\subsection{拓展阅读}", "节目与相关资料：", r"\begin{itemize}"]
        md += ["### 拓展阅读", ""]
        for reference in book["references"]:
            tex += [r"\item " + esc(reference["title"]) + r"：\url{" + reference["url"] + "}"]
            md += ["- [" + reference["title"] + "](" + reference["url"] + ")"]
        tex += [r"\end{itemize}"]
    tex += [r"\end{document}"]
    for filename, lines in ((STEM + ".tex", tex), ("source.md", md)):
        target = EPISODE / filename
        target.write_text("\n".join(line.rstrip() for line in "\n".join(lines).splitlines()) + "\n", encoding="utf-8")
        print(target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book", type=Path, nargs="?", default=EPISODE / "generation/book-final.json")
    render(parser.parse_args().book)

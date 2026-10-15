#!/usr/bin/env python3
"""Generate a MkDocs reading site from AI Course Notes LaTeX files."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import subprocess
import tempfile
import unicodedata
from collections import Counter
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable
from urllib.parse import quote

from PIL import Image, ImageOps


SITE_URL = "https://hqhq1025.github.io/ai-course-notes/"
REPO_URL = "https://github.com/hqhq1025/ai-course-notes"
RAW_BASE_URL = f"{REPO_URL}/raw/main"
BLOB_BASE_URL = f"{REPO_URL}/blob/main"
# MathJax is vendored instead of loaded from a CDN: unpkg/jsDelivr are unreliable from mainland
# China, and a synchronous CDN script there delays DOMContentLoaded by more than a minute.
# Source: https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz
# (integrity sha512-Bt+SSVU8eBG27zChVewOicYs7Xsdt40qm4+UpHyX7k0/O9NliPc+x77k1/FEsPsjKPZGJvtRZM1vO+geW0OhGw==).
# Subset: es5/tex-chtml.js, es5/input/tex/extensions/ (autoloaded by \boldsymbol, \cancel, ...),
# es5/output/chtml/fonts/woff-v2/, and LICENSE. 3.2.2 is the final MathJax 3 release.
MATHJAX_VENDOR_DIR = Path(__file__).resolve().parent / "vendor" / "mathjax"
MATHJAX_SITE_DIR = Path("assets") / "vendor" / "mathjax"
# Course folders that README.md does not list: (navigation title, README course they sit next to).
# Without this, the 37 Zhang Xiaojun episode notes fall into "其他" under the folder name.
UNLISTED_COURSES = {
    "youtube/zhangxiaojun": ("张小珺商业访谈录 · 节目笔记", "interviews/zhang-xiaojun"),
    "youtube": ("YouTube 单集笔记", ""),
}
# Home page reading routes; each step links to a course or note route relative to the site root.
READING_ROUTES = (
    (
        "入门 LLM",
        (
            ("CS336", "cs336"),
            ("CS224R L09 RLHF", "cs224r/lecture09"),
            ("CS25 V2 Karpathy：Transformer 入门", "cs25/lecture11"),
        ),
    ),
    (
        "深入 Agent",
        (
            ("Berkeley F24 姚顺雨：Agent 概述", "talks/berkeley-llm-agents/f24/lecture11"),
            ("CS329A", "cs329a"),
            ("Modern Agent", "modern-agent"),
            ("Agentic RL", "agentic-rl"),
        ),
    ),
    (
        "模型架构",
        (
            ("LLM Architect", "llm-architect"),
            ("CS25 V4 Mixtral", "cs25/lecture29"),
            ("CS336 L04 MoE", "cs336/lecture04"),
        ),
    ),
    (
        "前沿洞察",
        (
            ("Ilya Sutskever", "talks/dwarkesh-patel/ilya-age-of-research"),
            ("Dario Amodei", "talks/lex-fridman/dario-amodei-claude"),
            ("State of AI 2026", "talks/lex-fridman/state-of-ai-2026"),
        ),
    ),
)
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
PDF_EXTENSIONS = {".pdf"}
TIKZ_RENDERER_VERSION = "pdf-v2"
IMAGE_CACHE_VERSION = "image-v1"
PDF_FIGURE_RENDERER_VERSION = "pdf-figure-v1"
# Keep a PDF figure as SVG only when it is mostly vector. Many "PDF figures" are bitmaps
# wrapped in PDF; as SVG they become base64 blobs about 6x larger than a 1600px JPEG.
PDF_FIGURE_MAX_BITMAP_SHARE = 0.2
VISIBLE_SPACE_SYMBOL = "\u2423"
FENCE_LINE_PATTERN = re.compile(r"^[ \t]*```", re.M)
FENCED_CODE_BLOCK_PATTERN = re.compile(r"^[ \t]*```.*?^[ \t]*```[ \t]*$", re.M | re.S)
PASSTHROUGH_LATEX_ENVIRONMENTS = {
    "align",
    "align*",
    "aligned",
    "bmatrix",
    "cases",
    "equation",
    "equation*",
    "gather",
    "gather*",
    "matrix",
    "multline",
    "multline*",
    "pmatrix",
    "smallmatrix",
    "split",
    "vmatrix",
}


@dataclass
class CatalogEntry:
    category: str
    title: str
    path: Path
    topic: str = ""
    speaker: str = ""


@dataclass
class Note:
    root: Path
    tex_path: Path
    route_dir: Path
    course_dir: Path
    title: str
    authors: str = ""
    date: str = ""
    channel: str = ""
    video_url: str = ""
    cover_path: str = ""
    graphics_paths: tuple[str, ...] = ()

    @property
    def pdf_path(self) -> Path:
        return self.tex_path.with_suffix(".pdf")

    @property
    def rel_tex_path(self) -> Path:
        return self.tex_path.relative_to(self.root)


@dataclass
class WarningEvent:
    kind: str
    message: str


@dataclass
class BuildContext:
    root: Path
    output: Path
    docs_dir: Path
    cache_dir: Path
    render_tikz: bool
    compress_images: bool
    image_max_width: int
    jpeg_quality: int
    image_cache_dir: Path | None = None
    pdf_cache_dir: Path | None = None
    warnings: list[WarningEvent] = field(default_factory=list)
    tikz_preambles: dict[Path, str] = field(default_factory=dict)
    tikz_collector: list[Path] | None = None
    current_note: Note | None = None
    current_out_dir: Path | None = None

    def warn(self, kind: str, message: str) -> None:
        self.warnings.append(WarningEvent(kind=kind, message=message))


@dataclass
class EnvBlock:
    env: str
    start: int
    end: int
    args: list[str]
    optional_args: list[str]
    body: str
    source: str


def natural_key(value: str | Path) -> list[object]:
    parts = re.split(r"(\d+)", str(value))
    return [int(part) if part.isdigit() else part.lower() for part in parts]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def read_braced(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "{":
        raise ValueError("expected braced LaTeX argument")
    depth = 0
    body_start = start + 1
    index = start
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[body_start:index], index + 1
        index += 1
    raise ValueError("unterminated LaTeX argument")


def read_bracketed(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "[":
        raise ValueError("expected bracketed LaTeX argument")
    depth = 0
    body_start = start + 1
    index = start
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return text[body_start:index], index + 1
        index += 1
    raise ValueError("unterminated LaTeX optional argument")


def extract_newcommand(tex: str, name: str) -> str:
    # The last definition wins, as in LaTeX (e.g. a placeholder \newcommand later \renewcommand-ed).
    matches = list(re.finditer(rf"\\(?:re)?newcommand\s*\{{\s*\\{re.escape(name)}\s*\}}", tex))
    if not matches:
        return ""
    match = matches[-1]
    index = match.end()
    while index < len(tex) and tex[index].isspace():
        index += 1
    if index >= len(tex) or tex[index] != "{":
        return ""
    try:
        value, _ = read_braced(tex, index)
    except ValueError:
        return ""
    return clean_latex_text(value)


def extract_command_arg(text: str, command: str) -> str:
    pattern = re.compile(rf"\\{re.escape(command)}(?:\[[^\]]*\])?")
    match = pattern.search(text)
    if not match:
        return ""
    index = match.end()
    while index < len(text) and text[index].isspace():
        index += 1
    if index >= len(text) or text[index] != "{":
        return ""
    try:
        value, _ = read_braced(text, index)
    except ValueError:
        return ""
    return value


def replace_simple_command(text: str, command: str, replacement: str) -> str:
    return re.sub(rf"\\{command}\b", replacement, text)


def replace_braced_command(
    text: str,
    command: str,
    arg_count: int,
    repl: Callable[[list[str]], str],
) -> tuple[str, int]:
    pattern = re.compile(rf"\\{re.escape(command)}\b")
    pos = 0
    pieces: list[str] = []
    replacements = 0
    while True:
        match = pattern.search(text, pos)
        if not match:
            pieces.append(text[pos:])
            break
        index = match.end()
        args: list[str] = []
        ok = True
        for _ in range(arg_count):
            while index < len(text) and text[index].isspace():
                index += 1
            if index >= len(text) or text[index] != "{":
                ok = False
                break
            try:
                value, index = read_braced(text, index)
            except ValueError:
                ok = False
                break
            args.append(value)
        if not ok:
            pieces.append(text[pos : match.end()])
            pos = match.end()
            continue
        pieces.append(text[pos : match.start()])
        pieces.append(repl(args))
        replacements += 1
        pos = index
    return "".join(pieces), replacements


def expand_videofigure_commands(text: str) -> str:
    pattern = re.compile(r"\\videofigure\b")
    pos = 0
    pieces: list[str] = []
    while True:
        match = pattern.search(text, pos)
        if not match:
            pieces.append(text[pos:])
            break
        index = match.end()
        while index < len(text) and text[index].isspace():
            index += 1
        width = "0.95"
        if index < len(text) and text[index] == "[":
            try:
                width, index = read_bracketed(text, index)
            except ValueError:
                pieces.append(text[pos : match.end()])
                pos = match.end()
                continue
        args: list[str] = []
        for _ in range(3):
            while index < len(text) and text[index].isspace():
                index += 1
            if index >= len(text) or text[index] != "{":
                break
            try:
                value, index = read_braced(text, index)
            except ValueError:
                break
            args.append(value)
        if len(args) != 3:
            pieces.append(text[pos : match.end()])
            pos = match.end()
            continue
        image_ref, caption, interval = args
        pieces.append(text[pos : match.start()])
        pieces.append(
            "\n\\begin{figure}[H]\n"
            "\\centering\n"
            f"\\includegraphics[width={width}\\textwidth]{{{image_ref}}}\n"
            f"\\caption{{{caption}}}\n"
            "\\end{figure}\n"
            f"\\footnotetext{{视频讲解区间：{interval}。}}\n"
        )
        pos = index
    return "".join(pieces)


def replace_one_arg_commands(text: str, replacements: dict[str, str]) -> str:
    changed = True
    while changed:
        changed = False
        for command, template in replacements.items():
            text, count = replace_braced_command(text, command, 1, lambda args, template=template: template.format(args[0]))
            changed = changed or count > 0
    return text


def replace_latex_symbol_commands(text: str) -> str:
    return text.replace(r"\textvisiblespace", VISIBLE_SPACE_SYMBOL)


def unwrap_latex_layout_commands(text: str) -> str:
    changed = True
    while changed:
        text, count = replace_braced_command(text, "resizebox", 3, lambda args: args[2])
        changed = count > 0
    return text


def replace_latex_quotes(text: str) -> str:
    text = re.sub(r"``([^`\n]+?)''", r"“\1”", text)
    text = re.sub(r"`([^`\n]+?)'", r"‘\1’", text)
    return text.replace("''", "”")


def replace_multicolumn_commands(text: str) -> str:
    pattern = re.compile(r"\\multicolumn\b")
    pos = 0
    pieces: list[str] = []
    while True:
        match = pattern.search(text, pos)
        if not match:
            pieces.append(text[pos:])
            break
        index = match.end()
        args: list[str] = []
        ok = True
        for _ in range(3):
            while index < len(text) and text[index].isspace():
                index += 1
            if index >= len(text) or text[index] != "{":
                ok = False
                break
            try:
                value, index = read_braced(text, index)
            except ValueError:
                ok = False
                break
            args.append(value)
        if not ok:
            pieces.append(text[pos : match.end()])
            pos = match.end()
            continue
        pieces.append(text[pos : match.start()])
        pieces.append(args[2])
        pos = index
    return "".join(pieces)


def clean_latex_text(text: str) -> str:
    text = text.replace(r"\protect", "")
    text = replace_latex_symbol_commands(text)
    text = replace_latex_quotes(text)
    text = replace_multicolumn_commands(text)
    text = re.sub(r"\\footnotemark(?:\[[^\]]*\])?", "", text)
    text = re.sub(r"\\footnote\{([^{}]*)\}", r"\1", text)
    text = replace_one_arg_commands(
        text,
        {
            "textbf": "{}",
            "textit": "{}",
            "emph": "{}",
            "texttt": "{}",
            "text": "{}",
            "mathrm": "{}",
            "mathbf": "{}",
            "mathcal": "{}",
            "sqrt": "√{}",
            "nolinkurl": "{}",
            "url": "{}",
        },
    )
    text, _ = replace_braced_command(
        text,
        "frac",
        2,
        lambda args: f"{clean_latex_text(args[0])}/{clean_latex_text(args[1])}",
    )
    text, _ = replace_braced_command(text, "href", 2, lambda args: clean_latex_text(args[1]))
    text = text.replace(r"\'{e}", "e").replace(r'\"{o}', "o")
    replacements = {
        r"\&": "&",
        r"\%": "%",
        r"\$": "$",
        r"\#": "#",
        r"\_": "_",
        r"\{": "{",
        r"\}": "}",
        r"\neq": "≠",
        r"\ne": "≠",
        r"\approx": "≈",
        r"\sim": "≈",
        r"\times": "×",
        r"\cdot": "·",
        r"\leq": "≤",
        r"\geq": "≥",
        r"\le": "≤",
        r"\ge": "≥",
        r"\pm": "±",
        r"\infty": "∞",
        r"\Theta": "Θ",
        r"\theta": "θ",
        r"\alpha": "α",
        r"\beta": "β",
        r"\eta": "η",
        r"\sigma": "σ",
        r"\rightarrow": "→",
        r"\to": "→",
        r"\ldots": "…",
        r"\dots": "…",
        r"~": " ",
        "---": "—",
        "--": "–",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = replace_simple_command(text, "LaTeX", "LaTeX")
    text = replace_simple_command(text, "TeX", "TeX")
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    text = re.sub(r"\$\s*\$", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def convert_inline_latex(text: str) -> str:
    text = text.replace(r"\protect", "")
    text = replace_latex_symbol_commands(text)
    text = replace_latex_quotes(text)
    text = replace_multicolumn_commands(text)
    text = re.sub(r"\\footnotemark(?:\[[^\]]*\])?", "", text)
    # Web pages have no footnote area, so keep the note inline; the argument may contain \href.
    text, _ = replace_braced_command(text, "footnote", 1, lambda args: f"（{args[0].strip().rstrip('。')}）")
    # Cross-reference numbers exist only in the PDF; "（图 \ref{fig:x}）" reads as "（图）" on the web.
    text = re.sub(r"[ \t~]*\\ref\{[^{}]*\}", "", text)
    text = remove_latex_command_with_arg(text, "label")
    text, _ = replace_braced_command(text, "paragraph", 1, lambda args: f"**{args[0].strip()}** " if args[0].strip() else "")

    def href_repl(args: list[str]) -> str:
        url = clean_latex_text(args[0])
        label_source, _ = replace_braced_command(args[1], "nolinkurl", 1, lambda inner: inner[0])
        label_source, _ = replace_braced_command(label_source, "url", 1, lambda inner: inner[0])
        label = convert_inline_latex(label_source).strip()
        if re.match(r"^(https?:|mailto:|#)", url):
            return f"[{label}]({url})"
        return label

    text, _ = replace_braced_command(text, "href", 2, href_repl)

    text = replace_one_arg_commands(
        text,
        {
            "textbf": "**{}**",
            "textit": "*{}*",
            "emph": "*{}*",
            "texttt": "`{}`",
        },
    )
    text = replace_one_arg_commands(
        text,
        {
            "mathrm": "{}",
            "mathbf": "{}",
            "mathcal": "{}",
            "text": "{}",
        },
    )

    def url_repl(args: list[str]) -> str:
        url = args[0]
        if re.match(r"^(https?:|mailto:)", url):
            return f"<{url}>"
        return url

    text, _ = replace_braced_command(text, "url", 1, url_repl)
    text, _ = replace_braced_command(text, "nolinkurl", 1, url_repl)
    text = text.replace(r"\&", "&")
    text = text.replace(r"\%", "%")
    text = text.replace(r"\$", "$")
    text = text.replace(r"\#", "#")
    text = text.replace(r"\_", "_")
    text = text.replace(r"\{", "{")
    text = text.replace(r"\}", "}")
    text = text.replace("~", " ")
    text = re.sub(r"\\setlength\s*\{\\[A-Za-z@]+\}\s*\{[^{}]*\}", "", text)
    text = re.sub(r"\\(small|normalsize|centering|noindent|bfseries|itshape|allowbreak)\b", "", text)
    text = re.sub(r"\\par\b", "\n\n", text)
    return text


def parse_begin_args(text: str, index: int) -> tuple[list[str], list[str], int]:
    args: list[str] = []
    optional_args: list[str] = []
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        if index < len(text) and text[index] == "[":
            value, index = read_bracketed(text, index)
            optional_args.append(value)
            continue
        if index < len(text) and text[index] == "{":
            value, index = read_braced(text, index)
            args.append(value)
            continue
        break
    return args, optional_args, index


def inside_fenced_code(text: str, pos: int) -> bool:
    return sum(1 for _match in FENCE_LINE_PATTERN.finditer(text, 0, pos)) % 2 == 1


def next_fence_end(text: str, pos: int) -> int:
    match = FENCE_LINE_PATTERN.search(text, pos)
    return len(text) if match is None else match.end()


def find_env_block(text: str, env: str, start_pos: int = 0) -> EnvBlock | None:
    begin_pattern = re.compile(rf"\\begin\{{{re.escape(env)}\}}")
    while True:
        begin_match = begin_pattern.search(text, start_pos)
        if not begin_match:
            return None
        if inside_fenced_code(text, begin_match.start()):
            start_pos = next_fence_end(text, begin_match.end())
            continue
        break
    args, optional_args, body_start = parse_begin_args(text, begin_match.end())
    token_pattern = re.compile(rf"\\(?:begin|end)\{{{re.escape(env)}\}}")
    depth = 1
    scan = body_start
    while True:
        token = token_pattern.search(text, scan)
        if not token:
            return None
        if token.group(0).startswith(r"\begin"):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                end = token.end()
                return EnvBlock(
                    env=env,
                    start=begin_match.start(),
                    end=end,
                    args=args,
                    optional_args=optional_args,
                    body=text[body_start : token.start()],
                    source=text[begin_match.start() : end],
                )
        scan = token.end()


def replace_environment(text: str, env: str, handler) -> str:
    pieces: list[str] = []
    pos = 0
    while True:
        block = find_env_block(text, env, pos)
        if not block:
            pieces.append(text[pos:])
            break
        pieces.append(text[pos : block.start])
        pieces.append(handler(block))
        pos = block.end
    return "".join(pieces)


def parse_options(options: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for part in re.split(r",\s*", options or ""):
        if not part:
            continue
        if "=" in part:
            key, value = part.split("=", 1)
            parsed[key.strip().lower()] = value.strip().strip("{}")
        else:
            parsed[part.strip().lower()] = ""
    return parsed


def remove_latex_command_with_arg(text: str, command: str) -> str:
    pattern = re.compile(rf"\\{re.escape(command)}(?:\[[^\]]*\])?")
    pos = 0
    pieces: list[str] = []
    while True:
        match = pattern.search(text, pos)
        if not match:
            pieces.append(text[pos:])
            break
        index = match.end()
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text) or text[index] != "{":
            pieces.append(text[pos : match.end()])
            pos = match.end()
            continue
        try:
            _, end = read_braced(text, index)
        except ValueError:
            pieces.append(text[pos:])
            break
        pieces.append(text[pos : match.start()])
        pos = end
    return "".join(pieces)


def strip_latex_layout_commands(body: str) -> str:
    body = re.sub(r"\\(centering|raggedleft|raggedright|small|footnotesize|scriptsize|normalsize)\b", "", body)
    body = re.sub(r"\\renewcommand\s*\{\\arraystretch\}\s*\{[^{}]*\}", "", body)
    body = re.sub(r"\\setlength\s*\{\\tabcolsep\}\s*\{[^{}]*\}", "", body)
    body = re.sub(r"\\vspace\*?\s*\{[^{}]*\}", "", body)
    return body


def markdown_table_from_tabular(body: str) -> str:
    body = strip_latex_layout_commands(body)
    body = replace_multicolumn_commands(body)
    body = re.sub(r"\\(toprule|midrule|bottomrule|hline)\b", "", body)
    body = re.sub(r"\\(endfirsthead|endhead|endfoot|endlastfoot)\b", "", body)
    rows = [row.strip() for row in re.split(r"\\\\", body) if row.strip()]
    parsed_rows: list[list[str]] = []
    for row in rows:
        cells = [clean_latex_text(cell.strip()) for cell in row.split("&")]
        if any(cells):
            parsed_rows.append(cells)
    if not parsed_rows:
        return ""
    width = max(len(row) for row in parsed_rows)
    parsed_rows = [row + [""] * (width - len(row)) for row in parsed_rows]
    header = parsed_rows[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in parsed_rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n\n"


def split_latex_items(body: str) -> list[tuple[str, str]]:
    # \b keeps list spacing commands such as \setlength{\itemsep}{...} from starting a bogus item.
    token_pattern = re.compile(r"\\(?:begin|end)\{[A-Za-z*]+\}|\\item\b(?:\[[^\]]*\])?")
    items: list[tuple[str, str]] = []
    current_start: int | None = None
    current_label = ""
    depth = 0
    for token in token_pattern.finditer(body):
        value = token.group(0)
        if value.startswith(r"\begin"):
            depth += 1
            continue
        if value.startswith(r"\end"):
            depth = max(0, depth - 1)
            continue
        if depth != 0:
            continue
        if current_start is not None:
            items.append((current_label, body[current_start : token.start()]))
        label_match = re.match(r"\\item(?:\[([^\]]*)\])?", value)
        current_label = label_match.group(1) if label_match and label_match.group(1) else ""
        current_start = token.end()
    if current_start is not None:
        items.append((current_label, body[current_start:]))
    return items


def markdown_code_from_listing(block: EnvBlock) -> str:
    options = parse_options(block.optional_args[0] if block.optional_args else "")
    language = options.get("language", "").lower()
    language = {"python": "python", "bash": "bash", "c": "c"}.get(language, language)
    caption = clean_latex_text(options.get("caption", ""))
    title = f' title="{caption}"' if caption else ""
    return f"\n```{language}{title}\n{block.body.strip()}\n```\n\n"


def should_compress_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS


def is_pdf_asset(path: Path) -> bool:
    return path.suffix.lower() in PDF_EXTENSIONS


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def image_cache_path(ctx: BuildContext, src: Path) -> Path | None:
    if ctx.image_cache_dir is None:
        return None
    source_digest = file_sha256(src)
    cache_digest = hashlib.sha256(
        "\n".join(
            [
                IMAGE_CACHE_VERSION,
                src.suffix.lower(),
                str(ctx.image_max_width),
                str(ctx.jpeg_quality),
                source_digest,
            ]
        ).encode("utf-8")
    ).hexdigest()[:24]
    return ctx.image_cache_dir / f"image-{cache_digest}{src.suffix.lower()}"


def external_asset_url(ctx: BuildContext, src: Path) -> str:
    try:
        return raw_github_url(src.relative_to(ctx.root))
    except ValueError:
        return src.as_posix()


def copy_image_asset(ctx: BuildContext, src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not ctx.compress_images or not should_compress_image(src):
        shutil.copy2(src, dest)
        return
    cached_image = image_cache_path(ctx, src)
    if cached_image is not None and cached_image.exists():
        shutil.copy2(cached_image, dest)
        return
    try:
        with Image.open(src) as image:
            image = ImageOps.exif_transpose(image)
            if image.width > ctx.image_max_width:
                height = max(1, round(image.height * ctx.image_max_width / image.width))
                image = image.resize((ctx.image_max_width, height), Image.Resampling.LANCZOS)
            suffix = src.suffix.lower()
            if suffix in {".jpg", ".jpeg"}:
                if image.mode not in {"RGB", "L"}:
                    image = image.convert("RGB")
                image.save(dest, format="JPEG", quality=ctx.jpeg_quality, optimize=True, progressive=True)
            elif suffix == ".png":
                image.save(dest, format="PNG", optimize=True)
            else:
                shutil.copy2(src, dest)
        if cached_image is not None:
            cached_image.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dest, cached_image)
    except Exception as exc:
        shutil.copy2(src, dest)
        if ctx.current_note is not None:
            ctx.warn(
                "image_compression_failed",
                f"Image compression failed for {ctx.current_note.rel_tex_path}: {src} ({exc})",
            )


def copy_asset(ctx: BuildContext, src: Path, relative_name: str) -> str | None:
    if ctx.current_note is None or ctx.current_out_dir is None:
        return relative_name
    if is_pdf_asset(src):
        return None
    safe_rel = Path(relative_name)
    if safe_rel.is_absolute() or ".." in safe_rel.parts:
        safe_rel = Path(src.name)
    dest = ctx.current_out_dir / safe_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    if src.is_file():
        copy_image_asset(ctx, src, dest)
    else:
        ctx.warn("missing_asset", f"Missing asset referenced by {ctx.current_note.rel_tex_path}: {src}")
        return None
    return safe_rel.as_posix()


GRAPHICS_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg")


def extract_graphics_paths(tex: str) -> tuple[str, ...]:
    match = re.search(r"\\graphicspath\s*\{((?:\s*\{[^{}]*\})+)\s*\}", tex)
    return tuple(re.findall(r"\{([^{}]*)\}", match.group(1))) if match else ()


def resolve_asset(note: Note, asset_ref: str) -> tuple[Path, str]:
    raw = Path(asset_ref)
    if raw.is_absolute():
        return raw, raw.name
    base = note.tex_path.parent
    folders = ["", *note.graphics_paths]
    if len(raw.parts) == 1:
        folders += ["images", "slides-images", "frames"]
    for folder in folders:
        candidate = base / folder / raw
        # Like LaTeX, an extensionless \includegraphics tries the usual graphics extensions.
        options = [candidate] if raw.suffix else [candidate.with_name(candidate.name + ext) for ext in GRAPHICS_EXTENSIONS]
        for option in options:
            if option.is_file():
                return option, (Path(folder) / raw.parent / option.name).as_posix()
    return base / raw, raw.as_posix()


def markdown_pdf_figure(ctx: BuildContext, src: Path, caption: str) -> str:
    link = external_asset_url(ctx, src)
    caption_line = f"    {caption}\n\n" if caption else ""
    return (
        '\n??? info "PDF 图示资源"\n'
        + caption_line
        + f"    [打开 PDF 图示]({link})\n\n"
    )


def render_pdf_figure(ctx: BuildContext, src: Path, page: int) -> Path | None:
    """Render one PDF page to a cached SVG (mostly vector) or JPEG (bitmap-heavy)."""
    note_path = ctx.current_note.rel_tex_path if ctx.current_note else src
    cache_dir = ctx.pdf_cache_dir
    if cache_dir is None:
        return None
    key = hashlib.sha256(
        "\n".join(
            [PDF_FIGURE_RENDERER_VERSION, file_sha256(src), str(page), str(ctx.image_max_width), str(ctx.jpeg_quality)]
        ).encode("utf-8")
    ).hexdigest()[:24]
    for suffix in (".svg", ".jpg"):
        cached = cache_dir / f"pdf-{key}{suffix}"
        if cached.exists():
            return cached
    if not shutil.which("pdftocairo"):
        ctx.warn("pdf_figure_skipped", f"pdftocairo unavailable for {note_path}; linking {src.name} instead")
        return None
    page_args = ["-f", str(page), "-l", str(page)]
    try:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            svg_path = tmp_path / "figure.svg"
            subprocess.run(
                ["pdftocairo", "-svg", *page_args, str(src), str(svg_path)],
                check=True, capture_output=True, timeout=180,
            )
            svg = svg_path.read_text(encoding="utf-8", errors="ignore")
            bitmap_bytes = sum(len(data) for data in re.findall(r"base64,([A-Za-z0-9+/=]+)", svg))
            cache_dir.mkdir(parents=True, exist_ok=True)
            if bitmap_bytes < PDF_FIGURE_MAX_BITMAP_SHARE * len(svg):
                target = cache_dir / f"pdf-{key}.svg"
                shutil.copy2(svg_path, target)
                return target
            subprocess.run(
                [
                    "pdftocairo", "-png", "-singlefile", "-scale-to-x", str(ctx.image_max_width), "-scale-to-y", "-1",
                    *page_args, str(src), str(tmp_path / "figure"),
                ],
                check=True, capture_output=True, timeout=180,
            )
            target = cache_dir / f"pdf-{key}.jpg"
            with Image.open(tmp_path / "figure.png") as image:
                image.convert("RGB").save(target, format="JPEG", quality=ctx.jpeg_quality, optimize=True, progressive=True)
            return target
    except (subprocess.SubprocessError, OSError, ValueError) as exc:
        detail = exc.stderr.decode("utf-8", "replace").strip() if isinstance(exc, subprocess.CalledProcessError) and exc.stderr else exc
        ctx.warn("pdf_figure_failed", f"PDF figure rendering failed for {note_path}: {src} page {page} ({detail})")
        return None


def includegraphics_width_percent(options: str) -> int | None:
    match = re.search(r"width\s*=\s*([0-9]*\.?[0-9]*)\s*\\(?:textwidth|linewidth|columnwidth)", options)
    if not match:
        return None
    factor = float(match.group(1)) if match.group(1) not in {"", "."} else 1.0
    return max(10, min(100, round(factor * 100)))


INCLUDEGRAPHICS_PATTERN = re.compile(r"\\includegraphics\s*(?:\[([^\]]*)\])?\s*\{([^{}]+)\}")
INLINE_MATH_PATTERN = re.compile(r"(?<!\\)\$(?!\$)((?:\\.|[^$])+?)(?<!\\)\$|\\\((.+?)\\\)", re.S)


def caption_html(raw: str) -> str:
    """Escape a LaTeX caption for raw HTML while keeping inline math renderable by MathJax."""
    pieces: list[str] = []
    pos = 0
    for match in INLINE_MATH_PATTERN.finditer(raw):
        pieces.append(html.escape(clean_inline_fragment(raw[pos : match.start()])))
        math = match.group(1) if match.group(1) is not None else match.group(2)
        pieces.append(f'<span class="arithmatex">\\({html.escape(math.strip())}\\)</span>')
        pos = match.end()
    pieces.append(html.escape(clean_inline_fragment(raw[pos:])))
    return "".join(pieces).strip()


def clean_inline_fragment(text: str) -> str:
    """clean_latex_text for a fragment between math spans, keeping its edge spaces."""
    cleaned = clean_latex_text(text)
    if not cleaned:
        return " " if text[:1].isspace() or text[-1:].isspace() else ""
    return (" " if text[:1].isspace() else "") + cleaned + (" " if text[-1:].isspace() else "")


def last_command_arg(text: str, command: str) -> str:
    """The figure's own caption follows any subfigure captions, so take the last one."""
    value = ""
    for match in re.finditer(rf"\\{re.escape(command)}\*?(?:\[[^\]]*\])?\s*\{{", text):
        try:
            value, _ = read_braced(text, match.end() - 1)
        except ValueError:
            continue
    return value


def figure_source_text(body: str) -> str:
    """Text left in a figure besides images and caption, e.g. a \\figsource line."""
    text = INCLUDEGRAPHICS_PATTERN.sub(" ", body)
    for command in ("caption", "label", "vspace", "hspace", "color", "subcaption"):
        text = remove_latex_command_with_arg(text, command)
    text = re.sub(r"\\(?:begin|end)\{(?:minipage|subfigure)\}(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", text)
    text = re.sub(r"\\(?:centering|hfill|par|protect|footnotemark|noindent)\b", " ", text)
    return clean_latex_text(text)


def figure_image_entry(ctx: BuildContext, note: Note, options: str, image_ref: str, label: str) -> dict[str, str] | str | None:
    """Preview data for one \\includegraphics; fallback Markdown (str) or None when it cannot be shown."""
    if image_ref == r"\videocoverpath":
        image_ref = note.cover_path
    src, relative_name = resolve_asset(note, image_ref)
    if is_pdf_asset(src) and src.is_file():
        page_match = re.search(r"page\s*=\s*(\d+)", options)
        rendered = render_pdf_figure(ctx, src, int(page_match.group(1)) if page_match else 1)
        if rendered is None or ctx.current_out_dir is None:
            return markdown_pdf_figure(ctx, src, label)
        preview = f"figures-web/{rendered.name}"
        (ctx.current_out_dir / "figures-web").mkdir(parents=True, exist_ok=True)
        shutil.copy2(rendered, ctx.current_out_dir / preview)
        width = includegraphics_width_percent(options)
        return {
            "preview": preview,
            "href": preview,
            "original": external_asset_url(ctx, src),
            "original_label": "下载 PDF 原图",
            "aria": "查看大图",
            "style": f' style="width: {width}%"' if width else "",
            "pdf": "1",
        }
    rel = None if is_pdf_asset(src) else copy_asset(ctx, src, relative_name)
    if rel is None:
        return None
    original = external_asset_url(ctx, src)
    return {"preview": rel, "href": original, "original": original, "original_label": "查看原图", "aria": "查看原图", "style": "", "pdf": ""}


def markdown_figure_html(entries: list[dict[str, str]], caption: str, alt: str, source: str) -> str:
    classes = "ai-notes-figure"
    if all(entry["pdf"] for entry in entries):
        classes += " ai-notes-figure--pdf"
    if len(entries) > 1:
        classes += " ai-notes-figure--group"
    lines = [f'\n<figure class="{classes}">']
    for entry in entries:
        lines.append(
            f'  <a class="ai-notes-figure__preview" href="{html.escape(entry["href"], quote=True)}"{entry["style"]} '
            f'target="_blank" rel="noopener noreferrer" aria-label="{entry["aria"]}">'
        )
        lines.append(
            f'    <img src="{html.escape(entry["preview"], quote=True)}" alt="{html.escape(alt, quote=True)}" '
            'loading="lazy" decoding="async">'
        )
        lines.append("  </a>")
    links = []
    for index, entry in enumerate(entries, start=1):
        label = entry["original_label"] if len(entries) == 1 else f'{entry["original_label"]} {index}'
        links.append(
            f'<a class="ai-notes-figure__original" href="{html.escape(entry["original"], quote=True)}" '
            f'target="_blank" rel="noopener noreferrer">{label}</a>'
        )
    source_html = f'<br><span class="ai-notes-figure__source">{html.escape(source)}</span>' if source else ""
    lines.append(f"  <figcaption>{caption} {' '.join(links)}{source_html}</figcaption>")
    lines.append("</figure>\n\n")
    return "\n".join(lines)


def missing_figure_markdown(block: EnvBlock) -> str:
    return (
        '\n??? warning "图片资源缺失"\n'
        "    ```latex\n"
        + "\n".join(f"    {line}" for line in block.source.strip().splitlines())
        + "\n    ```\n\n"
    )


def markdown_figure_from_block(ctx: BuildContext, block: EnvBlock) -> str:
    note = ctx.current_note
    if note is None:
        return ""
    includes = list(INCLUDEGRAPHICS_PATTERN.finditer(block.body))
    if not includes:
        caption = clean_latex_text(extract_command_arg(block.body, "caption"))
        body = remove_latex_command_with_arg(block.body, "caption")
        content = convert_latex_fragment(body, ctx).strip()
        if caption:
            content = (content + "\n\n" if content else "") + f"*{caption}*"
        return f"\n{content}\n\n" if content else ""
    raw_caption = last_command_arg(block.body, "caption")
    alt = clean_latex_text(raw_caption) or Path(includes[0].group(2).strip()).name
    entries: list[dict[str, str]] = []
    fallbacks: list[str] = []
    for include in includes:
        entry = figure_image_entry(ctx, note, include.group(1) or "", include.group(2).strip(), alt)
        if entry is None:
            fallbacks.append(missing_figure_markdown(block))
        elif isinstance(entry, str):
            fallbacks.append(entry)
        else:
            entries.append(entry)
    if not entries:
        return "".join(dict.fromkeys(fallbacks))
    caption = caption_html(raw_caption) if raw_caption else html.escape(alt)
    return markdown_figure_html(entries, caption, alt, figure_source_text(block.body)) + "".join(dict.fromkeys(fallbacks))


def markdown_passthrough_from_block(ctx: BuildContext, block: EnvBlock) -> str:
    body = strip_latex_layout_commands(block.body)
    content = convert_latex_fragment(body, ctx).strip()
    return f"\n{content}\n\n" if content else ""


def markdown_table_wrapper_from_block(ctx: BuildContext, block: EnvBlock) -> str:
    caption = clean_latex_text(extract_command_arg(block.body, "caption"))
    body = remove_latex_command_with_arg(block.body, "caption")
    body = strip_latex_layout_commands(body)
    content = convert_latex_fragment(body, ctx).strip()
    if caption:
        caption_html = f'<figcaption class="ai-notes-table-caption">{html.escape(caption)}</figcaption>'
        content = (content + "\n\n" if content else "") + caption_html
    return f"\n{content}\n\n" if content else ""


def markdown_quote_from_block(ctx: BuildContext, block: EnvBlock) -> str:
    content = convert_latex_fragment(block.body, ctx).strip()
    if not content:
        return ""
    lines = [f"> {line}" if line else ">" for line in content.splitlines()]
    return "\n" + "\n".join(lines) + "\n\n"


def markdown_box_from_block(ctx: BuildContext, block: EnvBlock, kind: str) -> str:
    title = clean_latex_text(block.args[0]) if block.args else ""
    content = convert_latex_fragment(block.body, ctx).strip()
    indented = "\n".join(f"    {line}" for line in content.splitlines())
    return f'\n!!! {kind} "{title}"\n{indented}\n\n'


def markdown_list_from_block(ctx: BuildContext, block: EnvBlock, ordered: bool) -> str:
    items = split_latex_items(block.body)
    lines: list[str] = []
    for index, (_label, item) in enumerate(items, start=1):
        content = convert_latex_fragment(item, ctx).strip()
        prefix = f"{index}. " if ordered else "- "
        content_lines = content.splitlines()
        while content_lines and not content_lines[0].strip():
            content_lines.pop(0)
        while content_lines and not content_lines[-1].strip():
            content_lines.pop()
        if not content_lines:
            continue
        lines.append(prefix + content_lines[0].strip())
        continuation = " " * len(prefix)
        for line in content_lines[1:]:
            lines.append(continuation + line if line.strip() else "")
    return "\n" + "\n".join(lines) + "\n\n"


def markdown_description_from_block(ctx: BuildContext, block: EnvBlock) -> str:
    lines: list[str] = []
    for label, item in split_latex_items(block.body):
        term = clean_latex_text(label) if label else "说明"
        content = convert_latex_fragment(item, ctx).strip()
        content_lines = [line for line in content.splitlines() if line.strip()]
        if not content_lines:
            continue
        lines.append(f"- **{term}**：{content_lines[0].strip()}")
        for line in content_lines[1:]:
            lines.append(f"  {line}")
    return "\n" + "\n".join(lines) + "\n\n" if lines else ""


def tikz_preamble_for_note(ctx: BuildContext, note: Note) -> str:
    cached = ctx.tikz_preambles.get(note.tex_path)
    if cached is not None:
        return cached
    tex = read_text(note.tex_path)
    begin = re.search(r"\\begin\{document\}", tex)
    preamble = tex[: begin.start()] if begin else tex
    standalone = r"\documentclass[tikz,border=3pt]{standalone}"
    if re.search(r"\\documentclass(?:\[[^\]]*\])?\{[^}]+\}", preamble):
        preamble = re.sub(
            r"\\documentclass(?:\[[^\]]*\])?\{[^}]+\}",
            lambda _match: standalone,
            preamble,
            count=1,
        )
    else:
        preamble = standalone + "\n" + preamble
    ctx.tikz_preambles[note.tex_path] = preamble
    return preamble


def iter_env_blocks(text: str, env: str) -> list[EnvBlock]:
    blocks: list[EnvBlock] = []
    pos = 0
    while True:
        block = find_env_block(text, env, pos)
        if block is None:
            break
        blocks.append(block)
        pos = block.end
    return blocks


def tikz_svg_filename(ctx: BuildContext, note: Note, block: EnvBlock) -> str:
    preamble = tikz_preamble_for_note(ctx, note)
    digest = hashlib.sha256((TIKZ_RENDERER_VERSION + "\n" + preamble + "\n" + block.source).encode("utf-8")).hexdigest()[:16]
    return f"tikz-{digest}.svg"


def tikz_cache_entries(ctx: BuildContext, notes: list[Note]) -> list[Path]:
    entries: list[Path] = []
    previous_note = ctx.current_note
    previous_out_dir = ctx.current_out_dir
    previous_collector = ctx.tikz_collector
    ctx.tikz_collector = entries
    ctx.current_out_dir = None
    try:
        for note in notes:
            ctx.current_note = note
            convert_latex_fragment(note_body_source(note), ctx)
    finally:
        ctx.current_note = previous_note
        ctx.current_out_dir = previous_out_dir
        ctx.tikz_collector = previous_collector
    return entries


def print_tikz_cache_status(ctx: BuildContext, notes: list[Note]) -> int:
    entries = tikz_cache_entries(ctx, notes)
    missing = [entry for entry in entries if not entry.exists()]
    if missing:
        cached = len(entries) - len(missing)
        print(f"TikZ cache incomplete: {cached}/{len(entries)} diagrams cached; {len(missing)} missing.")
        return 1
    print(f"TikZ cache complete: {len(entries)} diagrams cached.")
    return 0


def render_tikz_to_svg(ctx: BuildContext, block: EnvBlock) -> str:
    note = ctx.current_note
    if note is None:
        return fallback_tikz_environment(block)
    if ctx.tikz_collector is not None:
        ctx.tikz_collector.append(ctx.cache_dir / tikz_svg_filename(ctx, note, block))
        return ""
    if ctx.current_out_dir is None:
        return fallback_tikz_environment(block)
    filename = tikz_svg_filename(ctx, note, block)
    cached_svg = ctx.cache_dir / filename
    if not ctx.render_tikz:
        ctx.warn("tikz_skipped", f"TikZ rendering disabled for {note.rel_tex_path}; keeping source block")
        return fallback_tikz_environment(block)
    if not cached_svg.exists():
        if not shutil.which("xelatex") or not shutil.which("dvisvgm"):
            ctx.warn("tikz_skipped", f"TikZ tools unavailable for {note.rel_tex_path}; keeping source block")
            return fallback_tikz_environment(block)
        preamble = tikz_preamble_for_note(ctx, note)
        tex = "\n".join(
            [
                preamble,
                r"\begin{document}",
                r"\pagestyle{empty}",
                r"\thispagestyle{empty}",
                block.source,
                r"\end{document}",
            ]
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "tikz.tex").write_text(tex, encoding="utf-8")
            try:
                subprocess.run(
                    ["xelatex", "-interaction=nonstopmode", "tikz.tex"],
                    cwd=tmp_path,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=45,
                )
                subprocess.run(
                    ["dvisvgm", "--pdf", "-n", "-o", "tikz.svg", "tikz.pdf"],
                    cwd=tmp_path,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=30,
                )
                validate_tikz_svg(tmp_path / "tikz.svg")
            except (subprocess.SubprocessError, FileNotFoundError, ValueError) as exc:
                ctx.warn("tikz_failed", f"TikZ render failed for {note.rel_tex_path}: {format_subprocess_error(exc)}")
                return fallback_tikz_environment(block)
            ctx.cache_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(tmp_path / "tikz.svg", cached_svg)
    shutil.copy2(cached_svg, ctx.current_out_dir / filename)
    return f"\n![TikZ diagram]({filename})\n\n"


def format_subprocess_error(exc: BaseException) -> str:
    if isinstance(exc, subprocess.CalledProcessError):
        output = "\n".join(part for part in [exc.stdout, exc.stderr] if part)
        tail = "\n".join(output.splitlines()[-12:])
        return f"{exc}; output tail: {tail}" if tail else str(exc)
    return str(exc)


def validate_tikz_svg(svg_path: Path) -> None:
    if not svg_path.is_file() or svg_path.stat().st_size == 0:
        raise ValueError("dvisvgm did not produce a non-empty SVG")
    svg = read_text(svg_path)
    if REPO_URL in svg or "AI Course Notes" in svg:
        raise ValueError("rendered SVG contains page footer/link artifacts")


def fallback_tikz_environment(block: EnvBlock) -> str:
    source = block.source.strip().replace("```", "``\\`")
    return (
        '\n??? info "TikZ 图暂未渲染"\n'
        "    当前构建环境没有成功生成 SVG，保留原始 TikZ 源码。\n\n"
        "    ```latex\n"
        + "\n".join(f"    {line}" for line in source.splitlines())
        + "\n    ```\n\n"
    )


def fallback_environment(block: EnvBlock) -> str:
    if block.env == "tikzpicture":
        return fallback_tikz_environment(block)
    source = block.source.strip().replace("```", "``\\`")
    return (
        f'\n??? quote "未转换的 LaTeX 环境：{block.env}"\n'
        "    ```latex\n"
        + "\n".join(f"    {line}" for line in source.splitlines())
        + "\n    ```\n\n"
    )


def replace_unknown_environments(text: str) -> str:
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@AI_NOTES_PROTECTED_{len(protected) - 1}@@"

    text = FENCED_CODE_BLOCK_PATTERN.sub(protect, text)
    text = re.sub(r"\$\$.*?\$\$", protect, text, flags=re.S)
    pattern = re.compile(r"\\begin\{([A-Za-z*]+)\}")
    pos = 0
    pieces: list[str] = []
    while True:
        match = pattern.search(text, pos)
        if not match:
            pieces.append(text[pos:])
            break
        env = match.group(1)
        if env in PASSTHROUGH_LATEX_ENVIRONMENTS:
            pieces.append(text[pos : match.end()])
            pos = match.end()
            continue
        block = find_env_block(text, env, match.start())
        if not block:
            pieces.append(text[pos:])
            break
        pieces.append(text[pos : block.start])
        pieces.append(fallback_environment(block))
        pos = block.end
    output = "".join(pieces)
    for index, value in enumerate(protected):
        output = output.replace(f"@@AI_NOTES_PROTECTED_{index}@@", value)
    return output


MACRO_DEFINITION_PATTERN = re.compile(
    r"\\(?:newcommand|providecommand)\*?\s*(?:\{\s*\\([A-Za-z@]+)\s*\}|\\([A-Za-z@]+))\s*(?:\[(\d)\])?\s*"
)
VERBATIM_BLOCK_PATTERN = re.compile(r"\\begin\{(lstlisting|verbatim|minted)\}.*?\\end\{\1\}", re.S)


INPUT_PATTERN = re.compile(
    r"\\IfFileExists\s*\{([^{}]+)\}\s*\{\s*\\input\s*\{([^{}]+)\}\s*\}\s*\{[^{}]*\}|\\input\s*\{([^{}]+)\}"
)


def inline_inputs(tex: str, base_dir: Path, seen: frozenset[Path] = frozenset()) -> str:
    """Inline \\input files (shared preambles, book chapters); paths resolve from the main file's directory."""

    def repl(match: re.Match[str]) -> str:
        ref = (match.group(2) or match.group(3)).strip()
        path = (base_dir / ref).resolve()
        if not path.is_file() and path.suffix != ".tex":
            path = path.with_name(path.name + ".tex")
        if not path.is_file() or path in seen:
            return ""
        return inline_inputs(read_text(path), base_dir, seen | {path})

    return INPUT_PATTERN.sub(repl, tex)


def read_note_source(tex_path: Path) -> str:
    return inline_inputs(read_text(tex_path), tex_path.parent, frozenset({tex_path.resolve()}))


def collect_macro_definitions(preamble: str) -> dict[str, tuple[int, str]]:
    """Read \\newcommand definitions with only mandatory arguments."""
    macros: dict[str, tuple[int, str]] = {}
    for match in MACRO_DEFINITION_PATTERN.finditer(preamble):
        index = match.end()
        # Optional-argument macros (e.g. \\videofigure) are handled by dedicated converters.
        if index >= len(preamble) or preamble[index] != "{":
            continue
        try:
            body, _ = read_braced(preamble, index)
        except ValueError:
            continue
        macros[match.group(1) or match.group(2)] = (int(match.group(3) or 0), body)
    return macros


def expand_note_macros(tex: str) -> str:
    """Expand the note's own simple macros (e.g. \\lecturefigure, \\teachervoice) before conversion."""
    begin = re.search(r"\\begin\{document\}", tex)
    if not begin:
        return tex
    macros = collect_macro_definitions(tex[: begin.start()])
    body = tex[begin.start() :]
    # A commented-out multi-line macro would otherwise leak its later lines as live content.
    body = "\n".join(line for line in body.splitlines() if not line.lstrip().startswith("%"))
    if not macros:
        return tex[: begin.start()] + body
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@AI_NOTES_VERBATIM_{len(protected) - 1}@@"

    body = VERBATIM_BLOCK_PATTERN.sub(protect, body)

    def substitute(template: str, args: list[str]) -> str:
        return re.sub(r"#([1-9])", lambda m: args[int(m.group(1)) - 1] if int(m.group(1)) <= len(args) else m.group(0), template)

    for _ in range(6):
        changed = 0
        for name, (arg_count, template) in macros.items():
            if arg_count:
                body, count = replace_braced_command(body, name, arg_count, lambda args, t=template: substitute(t, args))
            else:
                body, count = re.subn(rf"\\{re.escape(name)}(?![A-Za-z@])", lambda _m, t=template: t, body)
            changed += count
        if not changed:
            break
    for index, value in enumerate(protected):
        body = body.replace(f"@@AI_NOTES_VERBATIM_{index}@@", value)
    return tex[: begin.start()] + body


def note_body_source(note: Note) -> str:
    return strip_document_shell(expand_note_macros(read_note_source(note.tex_path)))


def strip_document_shell(tex: str) -> str:
    begin = re.search(r"\\begin\{document\}", tex)
    if begin:
        tex = tex[begin.end() :]
    end = re.search(r"\\end\{document\}", tex)
    if end:
        tex = tex[: end.start()]
    tex = re.sub(r"\\begin\{titlepage\}.*?\\end\{titlepage\}", "", tex, flags=re.S)
    tex = re.sub(r"\\(?:makelecturetitle|maketitle)\b", "", tex)
    for command in ("special", "hypersetup", "pagenumbering"):
        tex = remove_latex_command_with_arg(tex, command)
    tex = re.sub(r"\\tableofcontents\b", "", tex)
    tex = re.sub(r"\\(newpage|clearpage)\b", "", tex)
    return tex


def convert_display_math(text: str) -> str:
    text = re.sub(r"\\\[(.*?)\\\]", lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text, flags=re.S)
    text = re.sub(r"(?m)^(?![ \t])\$\$([^\n]*?)\$\$[ \t]*$", lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text)

    def env_math(match: re.Match[str]) -> str:
        env = match.group(1)
        body = match.group(2).strip()
        return f"\n$$\n\\begin{{{env}}}\n{body}\n\\end{{{env}}}\n$$\n"

    return re.sub(r"\\begin\{(align|equation|gather|multline)\*?\}(.*?)\\end\{\1\*?\}", env_math, text, flags=re.S)


def convert_sections(text: str) -> str:
    for command, prefix in [("section", "##"), ("subsection", "###"), ("subsubsection", "####")]:
        pattern = re.compile(rf"\\{command}\*?\{{([^{{}}]*(?:\{{[^{{}}]*\}}[^{{}}]*)*)\}}")
        text = pattern.sub(lambda m: f"\n{prefix} {clean_latex_text(m.group(1))}\n", text)
    return text


def sanitize_local_markdown_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()
        if re.match(r"^(https?:|mailto:|#)", target):
            return match.group(0)
        if target.endswith((".pdf", ".tex", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg")) and not target.startswith("/"):
            return match.group(0)
        if target.endswith("index.md") and not target.startswith(("/", "..")):
            return match.group(0)
        return label

    return re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", repl, text)


def strip_latex_comment_lines(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))


def transform_outside_math_and_code(text: str, transform: Callable[[str], str]) -> str:
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@AI_NOTES_MATH_OR_CODE_{len(protected) - 1}@@"

    patterns = [
        FENCED_CODE_BLOCK_PATTERN,
        re.compile(r"^[ \t]*\$\$.*?^[ \t]*\$\$", re.M | re.S),
        re.compile(r"\$\$.*?\$\$", re.S),
        re.compile(r"^[ \t]*\\\[.*?^[ \t]*\\\]", re.M | re.S),
        re.compile(r"\\\[.*?\\\]", re.S),
        re.compile(r"\\\(.*?\\\)", re.S),
        re.compile(r"(?<!\\)\$(?!\$)(?:\\.|[^\n$])+(?<!\\)\$(?!\$)"),
    ]
    for pattern in patterns:
        text = pattern.sub(protect, text)

    text = transform(text)
    for index, value in enumerate(protected):
        text = text.replace(f"@@AI_NOTES_MATH_OR_CODE_{index}@@", value)
    return text


def normalize_markdown(text: str) -> str:
    text = transform_outside_math_and_code(text, strip_latex_comment_lines)
    text = transform_outside_math_and_code(text, convert_inline_latex)
    text = transform_outside_math_and_code(text, sanitize_local_markdown_links)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_latex_fragment(fragment: str, ctx: BuildContext) -> str:
    text = replace_latex_symbol_commands(fragment)
    text = unwrap_latex_layout_commands(text)
    text = expand_videofigure_commands(text)
    text = replace_environment(text, "lstlisting", markdown_code_from_listing)
    text = replace_environment(text, "table", lambda block: markdown_table_wrapper_from_block(ctx, block))
    text = replace_environment(text, "center", lambda block: markdown_passthrough_from_block(ctx, block))
    # minipage often wraps an lstlisting; falling back to a fenced block would nest code fences.
    text = replace_environment(text, "minipage", lambda block: markdown_passthrough_from_block(ctx, block))
    text = replace_environment(text, "quote", lambda block: markdown_quote_from_block(ctx, block))
    text = replace_environment(text, "sloppypar", lambda block: markdown_passthrough_from_block(ctx, block))
    text = replace_environment(text, "tikzpicture", lambda block: render_tikz_to_svg(ctx, block))
    text = replace_environment(text, "figure", lambda block: markdown_figure_from_block(ctx, block))
    text = replace_environment(text, "importantbox", lambda block: markdown_box_from_block(ctx, block, "important"))
    text = replace_environment(text, "knowledgebox", lambda block: markdown_box_from_block(ctx, block, "info"))
    text = replace_environment(text, "warningbox", lambda block: markdown_box_from_block(ctx, block, "warning"))
    text = replace_environment(text, "dialoguebox", lambda block: markdown_box_from_block(ctx, block, "quote"))
    text = replace_environment(text, "longtable", lambda block: markdown_table_from_tabular(block.body))
    text = replace_environment(text, "tabularx", lambda block: markdown_table_from_tabular(block.body))
    text = replace_environment(text, "tabular", lambda block: markdown_table_from_tabular(block.body))
    text = replace_environment(text, "itemize", lambda block: markdown_list_from_block(ctx, block, ordered=False))
    text = replace_environment(text, "enumerate", lambda block: markdown_list_from_block(ctx, block, ordered=True))
    text = replace_environment(text, "description", lambda block: markdown_description_from_block(ctx, block))
    text = convert_display_math(text)
    text = convert_sections(text)
    text = re.sub(r"\\footnotetext\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", lambda m: f"\n> 来源：{clean_latex_text(m.group(1))}\n", text)
    text = replace_unknown_environments(text)
    return normalize_markdown(text)


def parse_note(root: Path, tex_path: Path) -> Note:
    tex = read_note_source(tex_path)
    route_dir = tex_path.parent.relative_to(root)
    parent_name = route_dir.name
    if re.match(r"^(lecture|week|verl)\d+$", parent_name):
        course_dir = route_dir.parent
    else:
        course_dir = route_dir.parent if route_dir.parent != Path(".") else route_dir
    title = extract_newcommand(tex, "notetitle") or extract_titlepage_title(tex) or humanize_path(route_dir)
    return Note(
        root=root,
        tex_path=tex_path,
        route_dir=route_dir,
        course_dir=course_dir,
        title=title,
        authors=extract_newcommand(tex, "noteauthors"),
        date=extract_newcommand(tex, "notedate") or extract_newcommand(tex, "videopublishdate"),
        channel=extract_newcommand(tex, "videochannel"),
        video_url=extract_newcommand(tex, "videourl"),
        cover_path=extract_newcommand(tex, "videocoverpath"),
        graphics_paths=extract_graphics_paths(tex),
    )


def extract_titlepage_title(tex: str) -> str:
    """Fallback for notes whose title only appears as the large bold line of the title page."""
    page = re.search(r"\\begin\{titlepage\}(.*?)\\end\{titlepage\}", tex, re.S)
    if not page:
        return ""
    match = re.search(r"\\(?:Huge|huge|LARGE)\s*\\bfseries\s*", page.group(1))
    if not match:
        return ""
    line = re.split(r"\\par\b|\n\s*\n", page.group(1)[match.end() :], maxsplit=1)[0]
    return clean_latex_text(line)


def humanize_path(path: Path) -> str:
    special = {
        "6s191": "MIT 6.S191",
        "agentic-rl": "Agentic RL",
        "articles": "技术文章笔记",
        "20vc": "20VC with Harry Stebbings",
        "aitime": "AITIME 论道",
        "alibaba-cloud": "阿里云",
        "cs146s": "CS146S",
        "cs153": "CS153",
        "cs224n": "CS224N",
        "cs224r": "CS224R",
        "cs231n": "CS231N",
        "cs25": "CS25",
        "cs329a": "CS329A",
        "cs336": "CS336",
        "cs336-2026": "CS336 2026",
        "interviews": "访谈笔记",
        "cleo-abram": "Cleo Abram",
        "dwarkesh-patel": "Dwarkesh Patel Podcast",
        "greg-isenberg": "Greg Isenberg",
        "ungrounded": "Ungrounded 不着边际",
        "whynot-tv": "WhynotTV",
        "zhang-xiaojun": "张小珺商业访谈录",
        "kaist-cs492d": "KAIST CS492D",
        "lex-fridman": "Lex Fridman Podcast",
        "llm-architect": "LLM Architect",
        "modern-agent": "Modern Agent",
        "no-priors": "No Priors Podcast",
        "nvidia-gtc": "NVIDIA GTC",
        "qingke": "青稞社区",
        "talks": "演讲与访谈",
    }
    text = path.as_posix()
    if text in special:
        return special[text]
    name = path.name
    if name in special:
        return special[name]
    if re.match(r"cs\d", name):
        return name.upper()
    return name.replace("-", " ").replace("_", " ").title()


def discover_notes(root: Path) -> list[Note]:
    notes: list[Note] = []
    for tex_path in sorted(root.rglob("*-notes.tex"), key=natural_key):
        rel = tex_path.relative_to(root)
        if ".git" in rel.parts or ".web-build" in rel.parts or rel.parts[:2] == ("tools", "templates"):
            continue
        notes.append(parse_note(root, tex_path))
    return notes


def strip_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text.strip()


def parse_readme_catalog(root: Path) -> list[CatalogEntry]:
    readme = root / "README.md"
    if not readme.is_file():
        return []
    entries: list[CatalogEntry] = []
    category = "课程"
    for line in read_text(readme).splitlines():
        heading = re.match(r"^###\s+(.+)$", line)
        if heading:
            category = strip_markdown(heading.group(1))
            continue
        if not line.startswith("|") or "](" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        for title, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", cells[0]):
            if href.startswith("http") or href == ".":
                continue
            path = Path(href.strip("/"))
            entries.append(
                CatalogEntry(
                    category=category,
                    title=strip_markdown(title),
                    path=path,
                    topic=strip_markdown(cells[1]) if len(cells) > 1 else "",
                    speaker=strip_markdown(cells[3]) if len(cells) > 3 else "",
                )
            )
    return entries


def course_title(course_dir: Path, catalog: dict[str, CatalogEntry]) -> str:
    key = course_dir.as_posix()
    if key == "cs336-2026":
        return "CS336 2026"
    if key in catalog:
        return catalog[key].title
    if key in UNLISTED_COURSES:
        return UNLISTED_COURSES[key][0]
    return humanize_path(course_dir)


def infer_category(course_dir: Path, entries: list[CatalogEntry]) -> str:
    key = course_dir.as_posix()
    exact = [entry for entry in entries if entry.path.as_posix() == key]
    if exact:
        return exact[0].category
    prefixed = [entry for entry in entries if entry.path.parts and course_dir.parts and entry.path.parts[0] == course_dir.parts[0]]
    if prefixed:
        return prefixed[0].category
    top = course_dir.parts[0] if course_dir.parts else ""
    if top == "articles":
        return "📝 技术文章笔记"
    if top in {"talks", "interviews"}:
        return "🎤 演讲与访谈"
    return "其他"


def topic_for_course(course_dir: Path, entries_by_path: dict[str, CatalogEntry]) -> str:
    entry = entries_by_path.get(course_dir.as_posix())
    return entry.topic if entry else ""


def category_label(category: str) -> str:
    """README category headings end with a hand-written count such as "(169 份)" that goes stale."""
    return re.sub(r"\s*[(（][^()（）]*\d[^()（）]*[)）]\s*$", "", category).strip()


def nav_category_label(category: str) -> str:
    """Sidebar section label: the category without its count or leading emoji."""
    label = category_label(category)
    return re.sub(r"^[^\w\s]+\s*", "", label) or label


def group_courses(courses: OrderedDict[Path, list[Note]], catalog_entries: list[CatalogEntry]) -> OrderedDict[str, list[Path]]:
    """Group course folders by README category, in README order.

    The home page and the sidebar share this grouping so both show the same structure.
    Folders that README.md does not list are placed after the course they belong with.
    """
    entry_rank: dict[str, int] = {}
    category_rank: dict[str, int] = {}
    for index, entry in enumerate(catalog_entries):
        entry_rank.setdefault(entry.path.as_posix(), index)
        category_rank.setdefault(entry.category, index)
    last = len(catalog_entries)

    def anchor_of(course_dir: Path) -> Path:
        key = course_dir.as_posix()
        if key not in entry_rank and UNLISTED_COURSES.get(key, ("", ""))[1]:
            return Path(UNLISTED_COURSES[key][1])
        return course_dir

    def course_rank(course_dir: Path) -> tuple[int, int, list[object]]:
        anchor = anchor_of(course_dir).as_posix()
        listed = course_dir.as_posix() in entry_rank
        return (entry_rank.get(anchor, last), 0 if listed else 1, natural_key(course_dir))

    groups: dict[str, list[Path]] = {}
    for course_dir in courses:
        groups.setdefault(infer_category(anchor_of(course_dir), catalog_entries), []).append(course_dir)
    ordered: OrderedDict[str, list[Path]] = OrderedDict()
    for category in sorted(groups, key=lambda name: category_rank.get(name, last + (name == "其他"))):
        ordered[category] = sorted(groups[category], key=course_rank)
    return ordered


NAV_SEQUENCE_PATTERNS = (
    (re.compile(r"^lecture(\d+)$"), "L{:02d}"),
    (re.compile(r"^week(\d+)$"), "W{:02d}"),
    (re.compile(r"^ep(\d+)-"), "#{}"),
)
NAV_COURSE_PREFIX = re.compile(
    r"^(?:(?:MIT|Stanford|KAIST|CMU|Berkeley)\s+)?(?:CS\s?\d+[A-Z]?|6\.S\d+)(?:\s+\d{4}|\s+V\d+)?"
    r"(?:\s+(?:Guest\s+)?(?:Lecture|Week)\s*\d+)?\s*[:：]\s*"
)
NAV_KIND_PREFIX = re.compile(r"^(?:文章笔记|访谈笔记|读书笔记|课程笔记)\s*[:：]\s*")
NAV_SUBTITLE_SEPARATOR = re.compile(r"\s*——\s*|\s+—\s+")
NAV_LABEL_MAX_WIDTH = 44  # about 1.5 sidebar lines
NAV_LABEL_HARD_MAX_WIDTH = 62  # beyond this a label wraps to three or more lines


def display_width(text: str) -> int:
    """Approximate rendered width: CJK and full-width characters count twice."""
    return sum(2 if unicodedata.east_asian_width(char) in "WF" else 1 for char in text)


def nav_label(note: Note) -> str:
    """Short sidebar label for a note; the page H1 and <title> keep the full title.

    The lecture number moves into a compact prefix ("L03"), the repeated course prefix
    ("CS336 2026 Lecture 3：") is dropped, and a long "——" subtitle is cut.
    """
    label = re.sub(r"^\[[^\]]*\]\s*", "", note.title.strip())
    label = NAV_KIND_PREFIX.sub("", label)
    sequence = ""
    for pattern, template in NAV_SEQUENCE_PATTERNS:
        match = pattern.match(note.route_dir.name)
        if match:
            number = int(match.group(1))
            sequence = template.format(number)
            # Strip "<course> Lecture 3：" only when the number before the colon is this lecture's number.
            label = re.sub(rf"^.{{0,40}}?(?<![\d.])0*{number}\s*[:：]\s*", "", label, count=1)
            break
    label = NAV_COURSE_PREFIX.sub("", label)
    if display_width(label) > NAV_LABEL_MAX_WIDTH:
        head = NAV_SUBTITLE_SEPARATOR.split(label, maxsplit=1)[0]
        if head != label and display_width(head) >= 8:
            label = head
    if display_width(label) > NAV_LABEL_HARD_MAX_WIDTH:
        # "<topic>：<long list of details>" keeps the topic when it is descriptive on its own.
        head = re.split(r"\s*[:：]\s*", label, maxsplit=1)[0]
        if head != label and display_width(head) >= 12:
            label = head
    label = label.strip() or note.title
    return f"{sequence} {label}" if sequence else label


def nav_labels(notes: list[Note]) -> dict[Path, str]:
    """Labels for one course; fall back to the full title where shortening makes two labels equal."""
    labels = {note.route_dir: nav_label(note) for note in notes}
    counts = Counter(labels.values())
    return {route: (label if counts[label] == 1 else next(n.title for n in notes if n.route_dir == route)) for route, label in labels.items()}


def relative_dir_target(from_dir: Path, to_dir: Path) -> str:
    if from_dir == to_dir:
        return ""
    try:
        rel = to_dir.relative_to(from_dir)
        return rel.as_posix() + "/"
    except ValueError:
        return to_dir.as_posix() + "/"


def markdown_page_target(from_dir: Path, to_dir: Path) -> str:
    return relative_dir_target(from_dir, to_dir) + "index.md"


def raw_github_url(path: Path) -> str:
    return f"{RAW_BASE_URL}/{quote(path.as_posix(), safe='/')}"


def github_blob_url(path: Path) -> str:
    """GitHub's file view; Pages serves .tex as application/x-tex, which downloads instead of showing."""
    return f"{BLOB_BASE_URL}/{quote(path.as_posix(), safe='/')}"


def note_unit(course_dir: Path) -> str:
    return "篇" if course_dir.parts[:1] == ("articles",) else "份讲义"


def copy_note_static_files(ctx: BuildContext, note: Note, out_dir: Path) -> tuple[str, str, str]:
    ctx.current_note = note
    ctx.current_out_dir = out_dir
    pdf_link = ""
    if note.pdf_path.is_file():
        pdf_link = raw_github_url(note.pdf_path.relative_to(note.root))
    shutil.copy2(note.tex_path, out_dir / note.tex_path.name)
    tex_link = note.tex_path.name
    cover_link = ""
    if note.cover_path:
        cover_src, cover_rel = resolve_asset(note, note.cover_path)
        if cover_src.is_file():
            cover_link = copy_asset(ctx, cover_src, cover_rel) or ""
    return pdf_link, tex_link, cover_link


def note_page_markdown(ctx: BuildContext, note: Note) -> str:
    out_dir = ctx.docs_dir / note.route_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_link, _tex_link, cover_link = copy_note_static_files(ctx, note, out_dir)
    body = convert_latex_fragment(note_body_source(note), ctx)
    lines = note_header_markdown(note, pdf_link, cover_link)
    lines.append(body)
    return "\n".join(lines)


def note_header_markdown(note: Note, pdf_link: str, cover_link: str) -> list[str]:
    """Title plus a compact header: one metadata line, one link line and a small cover.

    The sidebar shows a shortened label (see nav_label); front matter keeps the full
    title for <title>, the header bar and search.
    """
    actions = []
    if note.video_url:
        actions.append(f"[观看视频]({note.video_url})")
    if pdf_link:
        actions.append(f"[备用 PDF]({pdf_link})")
    actions.append(f"[LaTeX 源码]({github_blob_url(note.rel_tex_path)})")
    metadata = [value for value in (note.authors, note.channel, note.date) if value]
    lines = ["---", f"title: {yaml_quote(note.title)}", "---", "", f"# {note.title}", ""]
    lines.extend(['<div class="ai-notes-note-header" markdown>', '<div class="ai-notes-note-header__text" markdown>', ""])
    if metadata:
        lines.extend([" · ".join(metadata), "{: .ai-notes-note-header__meta }", ""])
    lines.extend([" · ".join(actions), "{: .ai-notes-note-header__actions }", "", "</div>"])
    if cover_link:
        cover = f"![视频封面]({cover_link})"
        if note.video_url:
            cover = f"[{cover}]({note.video_url})"
        lines.extend(["", cover, "{: .ai-notes-note-header__cover }"])
    lines.extend(["", "</div>", ""])
    return lines


def is_single_page_course(course_dir: Path, notes: list[Note]) -> bool:
    """A top-level note such as a book shares its route with the course; its page is the course page."""
    return len(notes) == 1 and notes[0].route_dir == course_dir


def course_page_markdown(course_dir: Path, notes: list[Note], title: str, topic: str) -> str:
    lines = [f"# {title}", ""]
    if topic:
        lines.extend([topic, ""])
    # A source column that repeats one value on every row only adds noise; state it once instead.
    channels = {note.channel for note in notes}
    shared_channel = next(iter(channels)) if len(channels) == 1 else None
    summary = f"共 {len(notes)} {note_unit(course_dir)}"
    if shared_channel:
        summary += f"，来源：{shared_channel}"
    header = ["讲义", "日期"] + ([] if shared_channel is not None else ["来源"]) + ["资源"]
    lines.extend(
        [
            f"{summary}。",
            "",
            '<div class="ai-notes-course-table" markdown>',
            "",
            "| " + " | ".join(header) + " |",
            "|" + " --- |" * len(header),
        ]
    )
    for note in sorted(notes, key=lambda item: natural_key(item.route_dir)):
        page_rel = markdown_page_target(course_dir, note.route_dir)
        resources = [f"[LaTeX]({github_blob_url(note.rel_tex_path)})"]
        if note.pdf_path.is_file():
            resources.append(f"[备用 PDF]({raw_github_url(note.pdf_path.relative_to(note.root))})")
        cells = [f"[{note.title}]({page_rel})", note.date or "—"]
        if shared_channel is None:
            cells.append(note.channel or "—")
        cells.append(" · ".join(resources))
        lines.append("| " + " | ".join(cells) + " |")
    lines.extend(["", "</div>"])
    return "\n".join(lines)


def reading_route_markdown(known_routes: set[str]) -> list[str]:
    lines = ["## 推荐阅读路线", ""]
    for name, steps in READING_ROUTES:
        parts = [f"[{label}]({route}/index.md)" if route in known_routes else label for label, route in steps]
        lines.append(f"- {name}：" + " → ".join(parts))
    return lines


def home_markdown(
    notes: list[Note],
    courses: OrderedDict[Path, list[Note]],
    catalog_entries: list[CatalogEntry],
    entries_by_path: dict[str, CatalogEntry],
) -> str:
    lines = [
        "# AI Course Notes",
        "",
        f"这里是从 `{len(notes)}` 份 LaTeX 讲义自动生成的网页阅读站。正文直接由 `.tex` 渲染成网页，适合浏览、搜索和连续阅读。",
        "",
    ]
    known_routes = {course_dir.as_posix() for course_dir in courses} | {note.route_dir.as_posix() for note in notes}
    lines.extend(reading_route_markdown(known_routes))
    lines.extend(["", "## 课程地图", ""])
    for category, course_dirs in group_courses(courses, catalog_entries).items():
        lines.extend([f"### {category_label(category)}", "", '<div class="course-grid" markdown>', ""])
        for course_dir in course_dirs:
            title = course_title(course_dir, entries_by_path)
            topic = topic_for_course(course_dir, entries_by_path)
            count = len(courses[course_dir])
            detail = f"<br><span>{html.escape(topic)}</span>" if topic else ""
            lines.append(f"-   [**{title}**]({course_dir.as_posix()}/index.md){detail}<br><small>{count} {note_unit(course_dir)}</small>")
        lines.extend(["", "</div>", ""])
    return "\n".join(lines)


def css_content() -> str:
    return """
:root {
  /* theme.font is false: system fonts only. Latin faces come first so Latin text keeps them;
     CJK text falls through to the first CJK face installed on the platform. */
  --md-text-font: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial,
    "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", "Source Han Sans SC",
    "WenQuanYi Micro Hei", sans-serif;
  --md-code-font: SFMono-Regular, Menlo, Consolas, "Liberation Mono", "PingFang SC", "Microsoft YaHei",
    monospace;
  --ai-notes-card-border: rgba(28, 86, 87, 0.18);
  --ai-notes-page-gutter: clamp(0.8rem, 2vw, 2rem);
  --ai-notes-rule-color: color-mix(in srgb, var(--md-default-fg-color), transparent 86%);
  /* 46em of the 0.8rem body text: about 46 CJK characters per line. */
  --ai-notes-measure: 36.8rem;
  --ai-notes-important-color: #7c4dff;
  --md-admonition-icon--important: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.62L12 2 9.19 8.62 2 9.24l5.45 4.73L5.82 21z"/></svg>');
}

[data-md-color-scheme="slate"] {
  --ai-notes-card-border: color-mix(in srgb, var(--md-default-fg-color), transparent 78%);
}

@media screen and (min-width: 76.25em) {
  .md-grid {
    max-width: min(96rem, calc(100vw - 2 * var(--ai-notes-page-gutter)));
  }

  .md-main__inner {
    width: 100%;
  }

  /* Keep prose at a readable measure, centred in the content column. --ai-notes-gap is the
     space left beside the measure; figures may use up to 8rem of it on each side. Browsers
     without container query units ignore these rules and keep the full-width column. */
  .md-content {
    container-type: inline-size;
    --ai-notes-gap: max(0px, calc((100cqi - 2.4rem - var(--ai-notes-measure)) / 2));
    --ai-notes-bleed: min(var(--ai-notes-gap), 8rem);
  }

  .md-content > .md-content__inner,
  .md-content > .md-path {
    padding-left: var(--ai-notes-gap);
    padding-right: var(--ai-notes-gap);
  }

  /* Material sizes figures to fit-content within 100%; let top-level figures span the bleed. */
  .md-content__inner.md-typeset > figure {
    margin-left: calc(-1 * var(--ai-notes-bleed));
    margin-right: calc(-1 * var(--ai-notes-bleed));
    max-width: none;
    width: auto;
  }

  /* PDF figures carry LaTeX widths (a share of \\textwidth), so they stay on the text measure. */
  .md-content__inner.md-typeset > figure.ai-notes-figure--pdf {
    margin-left: auto;
    margin-right: auto;
  }
}

.md-typeset .ai-notes-course-table td:last-child {
  white-space: nowrap;
}

.md-typeset .course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
  gap: 0.75rem;
  margin: 0.75rem 0 1.5rem;
}

.md-typeset .course-grid > ul {
  display: contents;
}

[dir] .md-typeset .course-grid li {
  list-style: none;
  border: 1px solid var(--ai-notes-card-border);
  border-radius: 0.35rem;
  padding: 0.8rem 0.9rem;
  margin: 0;
  background: color-mix(in srgb, var(--md-default-bg-color), var(--md-primary-fg-color) 4%);
  position: relative;
  transition: border-color 140ms ease, box-shadow 140ms ease;
}

/* The title link covers the whole card, so any click on the card opens the course. */
.md-typeset .course-grid li > a:first-child::after {
  content: "";
  inset: 0;
  position: absolute;
}

.md-typeset .course-grid li:hover,
.md-typeset .course-grid li:focus-within {
  border-color: var(--md-accent-fg-color);
  box-shadow: var(--md-shadow-z1);
}

.md-typeset .course-grid small {
  color: var(--md-default-fg-color--light);
}

.md-typeset .ai-notes-note-header {
  align-items: flex-start;
  display: flex;
  gap: 1.2rem;
  justify-content: space-between;
  margin: -0.35rem 0 1.6rem;
}

.md-typeset .ai-notes-note-header p {
  margin: 0;
}

.md-typeset .ai-notes-note-header__meta {
  color: var(--md-default-fg-color--light);
  font-size: 0.72rem;
}

.md-typeset .ai-notes-note-header__actions {
  font-size: 0.72rem;
  margin-top: 0.3rem !important;
}

.md-typeset .ai-notes-note-header__cover {
  flex: 0 0 auto;
}

.md-typeset .ai-notes-note-header__cover img {
  aspect-ratio: 16 / 9;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.3rem;
  display: block;
  object-fit: cover;
  width: 8.4rem;
}

.md-typeset h1 {
  color: var(--md-default-fg-color);
  font-size: 2.05rem;
  font-weight: 700;
  letter-spacing: 0;
  line-height: 1.18;
  margin-bottom: 1.15rem;
}

.md-typeset h2 {
  border-top: 1px solid var(--ai-notes-rule-color);
  color: var(--md-default-fg-color);
  font-size: 1.45rem;
  font-weight: 680;
  letter-spacing: 0;
  line-height: 1.28;
  margin-top: 2.4rem;
  padding-top: 1.05rem;
}

.md-typeset h3 {
  color: var(--md-default-fg-color);
  font-size: 1.08rem;
  font-weight: 680;
  letter-spacing: 0;
  line-height: 1.38;
  margin-top: 1.7rem;
}

.md-typeset h4 {
  color: var(--md-default-fg-color--light);
  font-size: 0.92rem;
  font-weight: 700;
  letter-spacing: 0;
  margin-top: 1.25rem;
  text-transform: none;
}

.md-typeset p,
.md-typeset li {
  line-height: 1.78;
}

.md-typeset code {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.22rem;
  font-size: 0.86em;
  padding: 0.04rem 0.24rem;
}

.md-typeset .highlight {
  margin: 1rem 0 1.35rem;
}

.md-typeset .highlight pre {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.4rem;
}

.md-typeset .arithmatex {
  overflow-x: auto;
}

.md-typeset > .arithmatex,
.md-typeset .admonition > .arithmatex {
  background: color-mix(in srgb, var(--md-default-bg-color), var(--md-primary-fg-color) 3%);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.42rem;
  margin: 1.1rem 0 1.25rem;
  padding: 0.7rem 0.9rem;
}

.md-typeset .admonition,
.md-typeset details {
  border-radius: 0.45rem;
  box-shadow: none;
  /* Material uses 0.64rem (12.8px); boxes hold about a third of the text on many pages. */
  font-size: 0.76rem;
  margin: 1rem 0 1.3rem;
}

.md-typeset .admonition.important,
.md-typeset details.important {
  border-color: var(--ai-notes-important-color);
}

.md-typeset .important > .admonition-title,
.md-typeset .important > summary {
  background-color: color-mix(in srgb, var(--ai-notes-important-color), transparent 90%);
}

.md-typeset .important > .admonition-title::before,
.md-typeset .important > summary::before {
  background-color: var(--ai-notes-important-color);
  -webkit-mask-image: var(--md-admonition-icon--important);
  mask-image: var(--md-admonition-icon--important);
}

.md-typeset .admonition-title {
  font-weight: 700;
  letter-spacing: 0;
}

.md-typeset table:not([class]) {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.38rem;
  display: table;
  /* em, not rem: tables inside boxes follow the box text size. */
  font-size: 0.94em;
  line-height: 1.55;
  margin: 1rem 0 1.1rem;
  overflow: hidden;
  width: 100%;
}

.md-typeset table:not([class]) th {
  background: color-mix(in srgb, var(--md-default-bg-color), var(--md-primary-fg-color) 6%);
  font-weight: 700;
}

.md-typeset table:not([class]) th,
.md-typeset table:not([class]) td {
  padding: 0.62rem 0.75rem;
  vertical-align: top;
}

.md-typeset blockquote {
  border-left: 0.18rem solid var(--md-accent-fg-color);
  color: var(--md-default-fg-color--light);
}

.md-typeset img {
  border-radius: 0.25rem;
}

.md-typeset .ai-notes-figure {
  margin: 1.2rem auto 1.45rem;
  text-align: center;
}

.md-typeset .ai-notes-figure__preview {
  display: inline-block;
  cursor: zoom-in;
}

.md-typeset .ai-notes-figure__preview img {
  display: block;
  height: auto;
  margin: 0 auto;
  max-width: 100%;
}

.md-typeset .ai-notes-figure--pdf .ai-notes-figure__preview img {
  width: 100%;
  /* PDF pages render with a transparent background; keep dark text readable in dark mode. */
  background: #fff;
}

.md-typeset figcaption {
  /* Material italicizes captions; CJK fonts have no italic, so browsers slant the glyphs. */
  font-style: normal;
}

.md-typeset .ai-notes-figure figcaption {
  color: var(--md-default-fg-color--light);
  max-width: var(--ai-notes-measure);
  font-size: 0.78rem;
  line-height: 1.55;
  margin-top: 0.45rem;
}

.md-typeset .ai-notes-figure__original {
  font-size: 0.72rem;
  margin-left: 0.35rem;
  white-space: nowrap;
}

.md-typeset .ai-notes-figure__source {
  color: var(--md-default-fg-color--lighter);
  font-size: 0.68rem;
}

/* Slide pairs and subfigures: equal-width images side by side, wrapping when the column is narrow. */
.md-typeset .ai-notes-figure--group {
  align-items: flex-start;
  display: flex;
  flex-flow: row wrap;
  gap: 0.6rem;
  justify-content: center;
}

.md-typeset .ai-notes-figure--group > .ai-notes-figure__preview {
  flex: 1 1 0;
  min-width: min(14rem, 100%);
}

.md-typeset .ai-notes-figure--group > .ai-notes-figure__preview img {
  width: 100%;
}

.md-typeset .ai-notes-figure--group > figcaption {
  flex-basis: 100%;
}

.md-typeset .ai-notes-table-caption {
  margin: -0.55rem 0 1.25rem;
  color: var(--md-default-fg-color--light);
  font-size: 0.78rem;
  line-height: 1.55;
  text-align: center;
}
""".strip()


def sidebar_script() -> str:
    """Reader script: remember the scroll position of each page across reloads in this tab."""
    return """
(function () {
  function scrollKey() {
    return "ai-notes-scroll:" + location.origin + location.pathname + location.search;
  }

  function saveScrollPosition() {
    try {
      sessionStorage.setItem(scrollKey(), String(Math.round(window.scrollY || window.pageYOffset || 0)));
    } catch (_error) {
      return;
    }
  }

  function restoreScrollPosition() {
    if (location.hash) {
      return;
    }
    var value;
    try {
      value = sessionStorage.getItem(scrollKey());
    } catch (_error) {
      return;
    }
    var y = Number(value);
    if (!Number.isFinite(y) || y <= 0) {
      return;
    }
    if ("scrollRestoration" in history) {
      history.scrollRestoration = "manual";
    }
    requestAnimationFrame(function () {
      window.scrollTo({ top: y, left: 0, behavior: "auto" });
      setTimeout(function () {
        window.scrollTo({ top: y, left: 0, behavior: "auto" });
      }, 120);
    });
  }

  function installScrollMemory() {
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) {
        return;
      }
      ticking = true;
      requestAnimationFrame(function () {
        saveScrollPosition();
        ticking = false;
      });
    }, { passive: true });
    window.addEventListener("pagehide", saveScrollPosition);
    restoreScrollPosition();
  }

  document.addEventListener("DOMContentLoaded", installScrollMemory);
})();
""".strip()


def mathjax_config() -> str:
    """MathJax settings plus a loader that fetches the vendored copy only on pages with math."""
    script = "../" + MATHJAX_SITE_DIR.relative_to("assets").as_posix() + "/tex-chtml.js"
    return """
window.MathJax = {
  tex: {
    inlineMath: [["$", "$"], ["\\\\(", "\\\\)"]],
    displayMath: [["$$", "$$"], ["\\\\[", "\\\\]"]],
    processEscapes: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// About a quarter of the pages have no math; they skip MathJax entirely. On the others the
// script loads asynchronously, so the text renders first and the formulas follow.
(function () {
  if (!document.querySelector(".arithmatex")) {
    return;
  }
  var script = document.createElement("script");
  script.src = new URL("__MATHJAX_SCRIPT__", document.currentScript.src).href;
  script.async = true;
  document.head.appendChild(script);
})();
""".strip().replace("__MATHJAX_SCRIPT__", script)


def search_index_hook() -> str:
    """MkDocs hook that stores the search index as UTF-8 instead of \\uXXXX escapes."""
    return """
# Generated by tools/web/generate_site.py.
# MkDocs writes search/search_index.json with every CJK character escaped as \\uXXXX.
# Rewriting it as UTF-8 cuts the index from 21.0 MB to 12.9 MB on this site.

import json
from pathlib import Path


def on_post_build(config, **kwargs):
    path = Path(config["site_dir"]) / "search" / "search_index.json"
    if not path.is_file():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
""".lstrip()


def theme_main_override() -> str:
    """Material template override that delays the search index download until search is used."""
    return """
{% extends "base.html" %}

{% block scripts %}
<script>
/* Material downloads search/search_index.json (about 4.6 MB gzip) with XMLHttpRequest on
   every page load. Hold that one request until the reader focuses or clicks the search box.
   If Material changes how it loads the index (another URL, fetch()), nothing is intercepted
   and search keeps its default behavior. */
(function () {
  var proto = window.XMLHttpRequest && XMLHttpRequest.prototype;
  if (!proto || !window.URLSearchParams) {
    return;
  }
  var params = new URLSearchParams(location.search);
  /* ?q= opens search on load and ?h= highlights a search hit: both need the index now. */
  if (params.has("q") || params.has("h")) {
    return;
  }
  var indexUrl = /\\/search\\/search_index\\.json(?:[?#]|$)/;
  var open = proto.open;
  var send = proto.send;
  var held = [];
  var released = false;

  function release() {
    if (released) {
      return;
    }
    released = true;
    proto.open = open;
    proto.send = send;
    document.removeEventListener("focusin", onFocus, true);
    document.removeEventListener("pointerdown", onPointerDown, true);
    held.splice(0).forEach(function (request) {
      send.apply(request.xhr, request.args);
    });
  }

  function onFocus(event) {
    var target = event.target;
    if (target && target.matches && target.matches("[data-md-component=search-query]")) {
      release();
    }
  }

  function onPointerDown(event) {
    var target = event.target;
    if (target && target.closest && target.closest("label[for=__search], .md-search")) {
      release();
    }
  }

  proto.open = function (method, url) {
    this.__aiNotesHoldIndex = indexUrl.test(String(url));
    return open.apply(this, arguments);
  };
  proto.send = function () {
    if (released || !this.__aiNotesHoldIndex) {
      return send.apply(this, arguments);
    }
    held.push({ xhr: this, args: arguments });
  };
  document.addEventListener("focusin", onFocus, true);
  document.addEventListener("pointerdown", onPointerDown, true);
})();
</script>
{{ super() }}
{% endblock %}
""".lstrip()


def yaml_quote(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def nav_course_lines(course_dir: Path, notes: list[Note], title: str, indent: str) -> list[str]:
    """One course in the sidebar; with navigation.indexes the section title opens the course page."""
    index_page = yaml_quote(course_dir.as_posix() + "/index.md")
    if is_single_page_course(course_dir, notes):
        return [f"{indent}- {yaml_quote(title)}: {index_page}"]
    labels = nav_labels(notes)
    lines = [f"{indent}- {yaml_quote(title)}:", f"{indent}    - {index_page}"]
    for note in sorted(notes, key=lambda item: natural_key(item.route_dir)):
        lines.append(f"{indent}    - {yaml_quote(labels[note.route_dir])}: {yaml_quote(note.route_dir.as_posix() + '/index.md')}")
    return lines


def generate_mkdocs_yml(
    courses: OrderedDict[Path, list[Note]],
    entries_by_path: dict[str, CatalogEntry],
    catalog_entries: list[CatalogEntry],
) -> str:
    lines = [
        "site_name: AI Course Notes",
        f"site_url: {SITE_URL}",
        f"repo_url: {REPO_URL}",
        "repo_name: hqhq1025/ai-course-notes",
        "docs_dir: docs",
        "site_dir: site",
        "theme:",
        "  name: material",
        "  custom_dir: overrides",
        # Material loads Roboto from Google Fonts by default; the stylesheet blocks first paint for
        # minutes where fonts.googleapis.com is unreachable, and Roboto has no CJK glyphs anyway.
        "  font: false",
        "  language: zh",
        "  palette:",
        "    - scheme: default",
        "      primary: teal",
        "      accent: amber",
        "      toggle:",
        "        icon: material/weather-night",
        "        name: 切换到深色模式",
        "    - scheme: slate",
        "      primary: teal",
        "      accent: amber",
        "      toggle:",
        "        icon: material/weather-sunny",
        "        name: 切换到浅色模式",
        "  features:",
        "    - content.code.copy",
        "    - navigation.footer",
        "    - navigation.indexes",
        "    - navigation.path",
        # Without prune every page embeds all ~450 sidebar links (about 70% of each HTML file).
        "    - navigation.prune",
        "    - navigation.sections",
        "    - navigation.top",
        "    - navigation.tracking",
        "    - search.highlight",
        "    - search.suggest",
        "    - toc.follow",
        "plugins:",
        "  - search:",
        "      lang:",
        "        - zh",
        "        - en",
        "hooks:",
        "  - hooks/search_index_utf8.py",
        "markdown_extensions:",
        "  - admonition",
        "  - attr_list",
        "  - md_in_html",
        "  - pymdownx.details",
        "  - pymdownx.superfences",
        "  - pymdownx.arithmatex:",
        "      generic: true",
        "extra_css:",
        "  - assets/stylesheets/ai-notes.css",
        "extra_javascript:",
        "  - assets/javascripts/ai-notes.js",
        "  - assets/javascripts/mathjax.js",
        "nav:",
        "  - 首页: index.md",
    ]
    for category, course_dirs in group_courses(courses, catalog_entries).items():
        label = nav_category_label(category)
        titles = {course_dir: course_title(course_dir, entries_by_path) for course_dir in course_dirs}
        if len(course_dirs) == 1 and titles[course_dirs[0]] == label:
            # One collection named like its category (the articles): avoid repeating the name, and
            # keep its 25 links collapsed so they are pruned from every other page's sidebar.
            only = course_dirs[0]
            titles[only] = f"全部 {len(courses[only])} {note_unit(only)}"
        lines.append(f"  - {yaml_quote(label)}:")
        for course_dir in course_dirs:
            lines.extend(nav_course_lines(course_dir, courses[course_dir], titles[course_dir], "      "))
    return "\n".join(lines) + "\n"


def print_warning_report(warnings: list[WarningEvent], *, verbose: bool) -> None:
    if not warnings:
        return
    labels = {
        "missing_asset": "Missing assets",
        "image_compression_failed": "Image compression fallbacks",
        "tikz_failed": "TikZ diagrams kept as source",
        "tikz_skipped": "TikZ diagrams skipped",
        "pdf_figure_failed": "PDF figures kept as links (render failed)",
        "pdf_figure_skipped": "PDF figures kept as links (pdftocairo unavailable)",
    }
    counts = Counter(warning.kind for warning in warnings)
    print("\nWarning summary:")
    for kind, count in sorted(counts.items(), key=lambda item: labels.get(item[0], item[0])):
        print(f"- {labels.get(kind, kind)}: {count}")
    if verbose:
        print("\nWarning details:")
        for warning in warnings:
            print(f"- {warning.message}")
    else:
        print("- Run with --verbose-warnings for details.")


def resolve_cache_root(output: Path, cache_root: Path | None) -> Path:
    return (cache_root if cache_root is not None else output / ".cache").resolve()


def prepare_output(output: Path, cache_root: Path | None = None) -> tuple[Path, Path, Path]:
    docs_dir = output / "docs"
    resolved_cache_root = resolve_cache_root(output, cache_root)
    cache_dir = resolved_cache_root / "tikz"
    image_cache_dir = resolved_cache_root / "images"
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)
    mkdocs_yml = output / "mkdocs.yml"
    if mkdocs_yml.exists():
        mkdocs_yml.unlink()
    for generated_dir in (output / "hooks", output / "overrides"):
        if generated_dir.exists():
            shutil.rmtree(generated_dir)
    return docs_dir, cache_dir, image_cache_dir


def build_site(
    root: Path,
    output: Path,
    *,
    strict: bool,
    fail_on_tikz_warnings: bool,
    fail_on_pdf_figure_warnings: bool,
    render_tikz: bool,
    verbose_warnings: bool,
    compress_images: bool,
    image_max_width: int,
    jpeg_quality: int,
    cache_root: Path | None,
) -> int:
    root = root.resolve()
    output = output.resolve()
    docs_dir, cache_dir, image_cache_dir = prepare_output(output, cache_root)
    ctx = BuildContext(
        root=root,
        output=output,
        docs_dir=docs_dir,
        cache_dir=cache_dir,
        render_tikz=render_tikz,
        compress_images=compress_images,
        image_max_width=image_max_width,
        jpeg_quality=jpeg_quality,
        image_cache_dir=image_cache_dir,
        pdf_cache_dir=image_cache_dir.parent / "pdf-figures",
    )
    catalog_entries = parse_readme_catalog(root)
    entries_by_path = {entry.path.as_posix(): entry for entry in catalog_entries}
    notes = discover_notes(root)
    if not notes:
        print("No LaTeX notes found.")
        return 1
    courses: OrderedDict[Path, list[Note]] = OrderedDict()
    for note in sorted(notes, key=lambda item: natural_key(item.route_dir)):
        courses.setdefault(note.course_dir, []).append(note)
        page = note_page_markdown(ctx, note)
        write_text(docs_dir / note.route_dir / "index.md", page)
    for course_dir, course_notes in courses.items():
        if is_single_page_course(course_dir, course_notes):
            continue
        if any(note.route_dir == course_dir for note in course_notes):
            ctx.warn("route_conflict", f"Course page {course_dir}/index.md would overwrite a note page")
        title = course_title(course_dir, entries_by_path)
        topic = topic_for_course(course_dir, entries_by_path)
        write_text(docs_dir / course_dir / "index.md", course_page_markdown(course_dir, course_notes, title, topic))
    write_text(docs_dir / "index.md", home_markdown(notes, courses, catalog_entries, entries_by_path))
    write_text(docs_dir / "assets" / "stylesheets" / "ai-notes.css", css_content())
    write_text(docs_dir / "assets" / "javascripts" / "ai-notes.js", sidebar_script())
    write_text(docs_dir / "assets" / "javascripts" / "mathjax.js", mathjax_config())
    shutil.copytree(MATHJAX_VENDOR_DIR, docs_dir / MATHJAX_SITE_DIR)
    write_text(output / "hooks" / "search_index_utf8.py", search_index_hook())
    write_text(output / "overrides" / "main.html", theme_main_override())
    write_text(output / "mkdocs.yml", generate_mkdocs_yml(courses, entries_by_path, catalog_entries))
    print(f"Generated {len(notes)} note pages across {len(courses)} course pages in {output}")
    print_warning_report(ctx.warnings, verbose=verbose_warnings)
    if strict and not notes:
        return 1
    if fail_on_tikz_warnings and any(warning.kind in {"tikz_failed", "tikz_skipped"} for warning in ctx.warnings):
        return 1
    if fail_on_pdf_figure_warnings and any(warning.kind.startswith("pdf_figure_") for warning in ctx.warnings):
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root")
    parser.add_argument("--output", type=Path, default=Path(".web-build"), help="Generated MkDocs workspace")
    parser.add_argument("--cache-dir", type=Path, default=None, help="Persistent cache root for generated TikZ SVGs and compressed images")
    parser.add_argument("--check-tikz-cache", action="store_true", help="Return zero when every TikZ diagram already has a cached SVG")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if no notes can be generated")
    parser.add_argument("--skip-tikz", action="store_true", help="Keep TikZ source blocks instead of rendering SVG")
    parser.add_argument("--fail-on-tikz-warnings", action="store_true", help="Return non-zero if TikZ diagrams fall back to source blocks")
    parser.add_argument("--fail-on-pdf-figure-warnings", action="store_true", help="Return non-zero if PDF figures fall back to links")
    parser.add_argument("--verbose-warnings", action="store_true", help="Print detailed warning messages")
    parser.add_argument("--no-compress-images", action="store_true", help="Copy JPG/PNG assets without resizing or recompressing")
    parser.add_argument("--image-max-width", type=int, default=1600, help="Maximum width for copied JPG/PNG assets")
    parser.add_argument("--jpeg-quality", type=int, default=82, help="JPEG quality for copied JPG assets")
    args = parser.parse_args()
    if args.check_tikz_cache:
        root = args.root.resolve()
        output = args.output.resolve()
        cache_root = resolve_cache_root(output, args.cache_dir)
        docs_dir = output / "docs"
        ctx = BuildContext(
            root=root,
            output=output,
            docs_dir=docs_dir,
            cache_dir=cache_root / "tikz",
            render_tikz=True,
            compress_images=not args.no_compress_images,
            image_max_width=args.image_max_width,
            jpeg_quality=args.jpeg_quality,
            image_cache_dir=cache_root / "images",
        )
        notes = discover_notes(root)
        if args.strict and not notes:
            print("No LaTeX notes found.")
            return 1
        return print_tikz_cache_status(ctx, notes)
    return build_site(
        args.root,
        args.output,
        strict=args.strict,
        fail_on_tikz_warnings=args.fail_on_tikz_warnings,
        fail_on_pdf_figure_warnings=args.fail_on_pdf_figure_warnings,
        render_tikz=not args.skip_tikz,
        verbose_warnings=args.verbose_warnings,
        compress_images=not args.no_compress_images,
        image_max_width=args.image_max_width,
        jpeg_quality=args.jpeg_quality,
        cache_root=args.cache_dir,
    )


if __name__ == "__main__":
    raise SystemExit(main())

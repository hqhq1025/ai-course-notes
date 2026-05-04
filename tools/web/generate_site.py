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
from collections import Counter
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

from PIL import Image, ImageOps


SITE_URL = "https://hqhq1025.github.io/ai-course-notes/"
REPO_URL = "https://github.com/hqhq1025/ai-course-notes"
RAW_BASE_URL = f"{REPO_URL}/raw/main"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
PDF_EXTENSIONS = {".pdf"}
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
    warnings: list[WarningEvent] = field(default_factory=list)
    tikz_preambles: dict[Path, str] = field(default_factory=dict)
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
    match = re.search(rf"\\newcommand\s*\{{\s*\\{re.escape(name)}\s*\}}", tex)
    if not match:
        return ""
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


def replace_one_arg_commands(text: str, replacements: dict[str, str]) -> str:
    changed = True
    while changed:
        changed = False
        for command, template in replacements.items():
            pattern = re.compile(rf"\\{command}\{{([^{{}}]*)\}}")

            def repl(match: re.Match[str]) -> str:
                nonlocal changed
                changed = True
                return template.format(match.group(1))

            text = pattern.sub(repl, text)
    return text


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
        },
    )
    text = re.sub(r"\\href\{([^{}]*)\}\{([^{}]*)\}", r"\2", text)
    text = re.sub(r"\\url\{([^{}]*)\}", r"\1", text)
    text = text.replace(r"\'{e}", "e").replace(r'\"{o}', "o")
    replacements = {
        r"\&": "&",
        r"\%": "%",
        r"\$": "$",
        r"\#": "#",
        r"\_": "_",
        r"\{": "{",
        r"\}": "}",
        r"\sim": "≈",
        r"\times": "×",
        r"\leq": "≤",
        r"\geq": "≥",
        r"\rightarrow": "→",
        r"\to": "→",
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
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def convert_inline_latex(text: str) -> str:
    text = text.replace(r"\protect", "")
    text = replace_multicolumn_commands(text)
    text = re.sub(r"\\footnotemark(?:\[[^\]]*\])?", "", text)
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
    def href_repl(match: re.Match[str]) -> str:
        url = match.group(1)
        label = match.group(2)
        if re.match(r"^(https?:|mailto:|#)", url):
            return f"[{label}]({url})"
        return label

    def url_repl(match: re.Match[str]) -> str:
        url = match.group(1)
        if re.match(r"^(https?:|mailto:)", url):
            return f"<{url}>"
        return url

    text = re.sub(r"\\href\{([^{}]*)\}\{([^{}]*)\}", href_repl, text)
    text = re.sub(r"\\url\{([^{}]*)\}", url_repl, text)
    text = text.replace(r"\&", "&")
    text = text.replace(r"\%", "%")
    text = text.replace(r"\$", "$")
    text = text.replace(r"\#", "#")
    text = text.replace(r"\_", "_")
    text = text.replace(r"\{", "{")
    text = text.replace(r"\}", "}")
    text = text.replace("~", " ")
    text = re.sub(r"\\(small|normalsize|centering|noindent|bfseries|itshape)\b", "", text)
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
    token_pattern = re.compile(r"\\(?:begin|end)\{[A-Za-z*]+\}|\\item(?:\[[^\]]*\])?")
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


def external_asset_url(ctx: BuildContext, src: Path) -> str:
    try:
        return raw_github_url(src.relative_to(ctx.root))
    except ValueError:
        return src.as_posix()


def copy_image_asset(ctx: BuildContext, src: Path, dest: Path) -> None:
    if not ctx.compress_images or not should_compress_image(src):
        shutil.copy2(src, dest)
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


def resolve_asset(note: Note, asset_ref: str) -> tuple[Path, str]:
    raw = Path(asset_ref)
    if raw.is_absolute():
        return raw, raw.name
    base = note.tex_path.parent
    direct = base / raw
    if direct.is_file():
        return direct, raw.as_posix()
    if len(raw.parts) == 1:
        for folder in ["images", "slides-images", "frames"]:
            candidate = base / folder / raw.name
            if candidate.is_file():
                return candidate, f"{folder}/{raw.name}"
    return direct, raw.as_posix()


def markdown_pdf_figure(ctx: BuildContext, src: Path, caption: str) -> str:
    link = external_asset_url(ctx, src)
    caption_line = f"    {caption}\n\n" if caption else ""
    return (
        '\n??? info "PDF 图示资源"\n'
        + caption_line
        + f"    [打开 PDF 图示]({link})\n\n"
    )


def markdown_figure_from_block(ctx: BuildContext, block: EnvBlock) -> str:
    note = ctx.current_note
    if note is None:
        return ""
    include = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^{}]+)\}", block.body)
    if not include:
        caption = clean_latex_text(extract_command_arg(block.body, "caption"))
        body = remove_latex_command_with_arg(block.body, "caption")
        content = convert_latex_fragment(body, ctx).strip()
        if caption:
            content = (content + "\n\n" if content else "") + f"*{caption}*"
        return f"\n{content}\n\n" if content else ""
    image_ref = include.group(1).strip()
    if image_ref == r"\videocoverpath":
        image_ref = note.cover_path
    caption = clean_latex_text(extract_command_arg(block.body, "caption")) or Path(image_ref).name
    src, relative_name = resolve_asset(note, image_ref)
    if is_pdf_asset(src):
        if src.is_file():
            return markdown_pdf_figure(ctx, src, caption)
        return (
            '\n??? warning "图片资源缺失"\n'
            "    ```latex\n"
            + "\n".join(f"    {line}" for line in block.source.strip().splitlines())
            + "\n    ```\n\n"
        )
    rel = copy_asset(ctx, src, relative_name)
    if rel is None:
        return (
            '\n??? warning "图片资源缺失"\n'
            "    ```latex\n"
            + "\n".join(f"    {line}" for line in block.source.strip().splitlines())
            + "\n    ```\n\n"
        )
    return f"\n![{caption}]({rel})\n\n"


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
        content = (content + "\n\n" if content else "") + f"*{caption}*"
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
    indented = "\n".join(f"    {line}" if line else "" for line in content.splitlines())
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


def render_tikz_to_svg(ctx: BuildContext, block: EnvBlock) -> str:
    note = ctx.current_note
    if note is None or ctx.current_out_dir is None:
        return fallback_tikz_environment(block)
    preamble = tikz_preamble_for_note(ctx, note)
    digest = hashlib.sha256((preamble + "\n" + block.source).encode("utf-8")).hexdigest()[:16]
    filename = f"tikz-{digest}.svg"
    cached_svg = ctx.cache_dir / filename
    if not ctx.render_tikz:
        ctx.warn("tikz_skipped", f"TikZ rendering disabled for {note.rel_tex_path}; keeping source block")
        return fallback_tikz_environment(block)
    if not cached_svg.exists():
        if not shutil.which("xelatex") or not shutil.which("dvisvgm"):
            ctx.warn("tikz_skipped", f"TikZ tools unavailable for {note.rel_tex_path}; keeping source block")
            return fallback_tikz_environment(block)
        tex = "\n".join([preamble, r"\begin{document}", block.source, r"\end{document}"])
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "tikz.tex").write_text(tex, encoding="utf-8")
            try:
                subprocess.run(
                    ["xelatex", "-no-pdf", "-interaction=nonstopmode", "tikz.tex"],
                    cwd=tmp_path,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=45,
                )
                subprocess.run(
                    ["dvisvgm", "-n", "-o", "tikz.svg", "tikz.xdv"],
                    cwd=tmp_path,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=30,
                )
            except (subprocess.SubprocessError, FileNotFoundError) as exc:
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


def strip_document_shell(tex: str) -> str:
    begin = re.search(r"\\begin\{document\}", tex)
    if begin:
        tex = tex[begin.end() :]
    end = re.search(r"\\end\{document\}", tex)
    if end:
        tex = tex[: end.start()]
    tex = re.sub(r"\\begin\{titlepage\}.*?\\end\{titlepage\}", "", tex, flags=re.S)
    tex = re.sub(r"\\tableofcontents\b", "", tex)
    tex = re.sub(r"\\(newpage|clearpage)\b", "", tex)
    return tex


def convert_display_math(text: str) -> str:
    text = re.sub(r"\\\[(.*?)\\\]", lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text, flags=re.S)
    text = re.sub(r"\$\$(.*?)\$\$", lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text, flags=re.S)

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


def normalize_markdown(text: str) -> str:
    text = convert_inline_latex(text)
    text = sanitize_local_markdown_links(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_latex_fragment(fragment: str, ctx: BuildContext) -> str:
    text = fragment
    text = replace_environment(text, "lstlisting", markdown_code_from_listing)
    text = replace_environment(text, "table", lambda block: markdown_table_wrapper_from_block(ctx, block))
    text = replace_environment(text, "center", lambda block: markdown_passthrough_from_block(ctx, block))
    text = replace_environment(text, "quote", lambda block: markdown_quote_from_block(ctx, block))
    text = replace_environment(text, "sloppypar", lambda block: markdown_passthrough_from_block(ctx, block))
    text = replace_environment(text, "tikzpicture", lambda block: render_tikz_to_svg(ctx, block))
    text = replace_environment(text, "figure", lambda block: markdown_figure_from_block(ctx, block))
    text = replace_environment(text, "importantbox", lambda block: markdown_box_from_block(ctx, block, "important"))
    text = replace_environment(text, "knowledgebox", lambda block: markdown_box_from_block(ctx, block, "info"))
    text = replace_environment(text, "warningbox", lambda block: markdown_box_from_block(ctx, block, "warning"))
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
    tex = read_text(tex_path)
    route_dir = tex_path.parent.relative_to(root)
    parent_name = route_dir.name
    if re.match(r"^(lecture|week|verl)\d+$", parent_name):
        course_dir = route_dir.parent
    else:
        course_dir = route_dir.parent if route_dir.parent != Path(".") else route_dir
    title = extract_newcommand(tex, "notetitle") or humanize_path(route_dir)
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
    )


def humanize_path(path: Path) -> str:
    special = {
        "6s191": "MIT 6.S191",
        "agentic-rl": "Agentic RL",
        "articles": "技术文章笔记",
        "cs146s": "CS146S",
        "cs153": "CS153",
        "cs224n": "CS224N",
        "cs224r": "CS224R",
        "cs231n": "CS231N",
        "cs25": "CS25",
        "cs336": "CS336",
        "cs336-2026": "CS336 2026",
        "interviews": "访谈笔记",
        "kaist-cs492d": "KAIST CS492D",
        "llm-architect": "LLM Architect",
        "modern-agent": "Modern Agent",
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
    pdf_link, tex_link, cover_link = copy_note_static_files(ctx, note, out_dir)
    body = convert_latex_fragment(strip_document_shell(read_text(note.tex_path)), ctx)
    actions = []
    actions.append(f"[LaTeX 源码]({tex_link})")
    if pdf_link:
        actions.append(f"[备用 PDF]({pdf_link})")
    if note.video_url:
        actions.append(f"[观看视频]({note.video_url})")
    metadata_rows = [
        ("作者/整理", note.authors),
        ("来源", note.channel),
        ("日期", note.date),
    ]
    lines = [f"# {note.title}", "", " · ".join(actions), ""]
    if any(value for _, value in metadata_rows):
        lines.extend(["| 字段 | 内容 |", "| --- | --- |"])
        for key, value in metadata_rows:
            if value:
                lines.append(f"| {key} | {value} |")
        lines.append("")
    if cover_link:
        lines.extend([f"![{note.title}]({cover_link})", ""])
    lines.append(body)
    return "\n".join(lines)


def course_page_markdown(course_dir: Path, notes: list[Note], title: str, topic: str) -> str:
    lines = [f"# {title}", ""]
    if topic:
        lines.extend([topic, ""])
    lines.extend([f"共 {len(notes)} 份讲义。", "", "| 讲义 | 日期 | 来源 | 资源 |", "| --- | --- | --- | --- |"])
    for note in sorted(notes, key=lambda item: natural_key(item.route_dir)):
        page_rel = markdown_page_target(course_dir, note.route_dir)
        dir_rel = relative_dir_target(course_dir, note.route_dir)
        resources = [f"[阅读]({page_rel})"]
        resources.append(f"[LaTeX]({dir_rel}{note.tex_path.name})")
        if note.pdf_path.is_file():
            resources.append(f"[备用 PDF]({raw_github_url(note.pdf_path.relative_to(note.root))})")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"[{note.title}]({page_rel})",
                    note.date or "—",
                    note.channel or "—",
                    " · ".join(resources),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def home_markdown(
    notes: list[Note],
    courses: OrderedDict[Path, list[Note]],
    catalog_entries: list[CatalogEntry],
    entries_by_path: dict[str, CatalogEntry],
) -> str:
    groups: OrderedDict[str, list[Path]] = OrderedDict()
    for course_dir in courses:
        category = infer_category(course_dir, catalog_entries)
        groups.setdefault(category, []).append(course_dir)
    lines = [
        "# AI Course Notes",
        "",
        f"这里是从 `{len(notes)}` 份 LaTeX 讲义自动生成的网页阅读站。正文直接由 `.tex` 渲染成网页，适合浏览、搜索和连续阅读。",
        "",
        "## 课程地图",
        "",
    ]
    for category, course_dirs in groups.items():
        lines.extend([f"### {category}", "", '<div class="course-grid" markdown>', ""])
        for course_dir in sorted(course_dirs, key=natural_key):
            title = course_title(course_dir, entries_by_path)
            topic = topic_for_course(course_dir, entries_by_path)
            count = len(courses[course_dir])
            detail = f"<br><span>{html.escape(topic)}</span>" if topic else ""
            lines.append(f"-   [**{title}**]({course_dir.as_posix()}/index.md){detail}<br><small>{count} 份讲义</small>")
        lines.extend(["", "</div>", ""])
    lines.extend(
        [
            "## 推荐阅读路线",
            "",
            "- 入门 LLM：CS336 → CS224R L09 → CS25 Karpathy Transformer 入门",
            "- 深入 Agent：Berkeley LLM Agents → Modern Agent → Agentic RL",
            "- 模型架构：LLM Architect → CS25 Mixtral → CS336 MoE",
            "- 前沿洞察：Ilya → Dario → State of AI 2026",
        ]
    )
    return "\n".join(lines)


def css_content() -> str:
    return """
:root {
  --ai-notes-card-border: rgba(28, 86, 87, 0.18);
}

.md-typeset .course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: 0.75rem;
  margin: 0.75rem 0 1.5rem;
}

.md-typeset .course-grid > ul {
  display: contents;
}

.md-typeset .course-grid li {
  list-style: none;
  border: 1px solid var(--ai-notes-card-border);
  border-radius: 0.35rem;
  padding: 0.8rem 0.9rem;
  margin: 0;
  background: color-mix(in srgb, var(--md-default-bg-color), var(--md-primary-fg-color) 4%);
}

.md-typeset .course-grid small {
  color: var(--md-default-fg-color--light);
}

.md-typeset img {
  border-radius: 0.25rem;
}
""".strip()


def mathjax_config() -> str:
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
""".strip()


def yaml_quote(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def generate_mkdocs_yml(courses: OrderedDict[Path, list[Note]], entries_by_path: dict[str, CatalogEntry]) -> str:
    lines = [
        "site_name: AI Course Notes",
        f"site_url: {SITE_URL}",
        f"repo_url: {REPO_URL}",
        "docs_dir: docs",
        "site_dir: site",
        "theme:",
        "  name: material",
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
        "    - navigation.tracking",
        "    - navigation.top",
        "    - search.highlight",
        "    - search.suggest",
        "plugins:",
        "  - search:",
        "      lang:",
        "        - zh",
        "        - en",
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
        "  - assets/javascripts/mathjax.js",
        "  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js",
        "nav:",
        "  - 首页: index.md",
        "  - 课程:",
    ]
    for course_dir, notes in courses.items():
        title = course_title(course_dir, entries_by_path)
        lines.append(f"      - {yaml_quote(title)}:")
        lines.append(f"          - 概览: {yaml_quote(course_dir.as_posix() + '/index.md')}")
        for note in sorted(notes, key=lambda item: natural_key(item.route_dir)):
            lines.append(f"          - {yaml_quote(note.title)}: {yaml_quote(note.route_dir.as_posix() + '/index.md')}")
    return "\n".join(lines) + "\n"


def print_warning_report(warnings: list[WarningEvent], *, verbose: bool) -> None:
    if not warnings:
        return
    labels = {
        "missing_asset": "Missing assets",
        "image_compression_failed": "Image compression fallbacks",
        "tikz_failed": "TikZ diagrams kept as source",
        "tikz_skipped": "TikZ diagrams skipped",
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


def prepare_output(output: Path) -> tuple[Path, Path]:
    docs_dir = output / "docs"
    cache_dir = output / ".cache" / "tikz"
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)
    mkdocs_yml = output / "mkdocs.yml"
    if mkdocs_yml.exists():
        mkdocs_yml.unlink()
    return docs_dir, cache_dir


def build_site(
    root: Path,
    output: Path,
    *,
    strict: bool,
    fail_on_tikz_warnings: bool,
    render_tikz: bool,
    verbose_warnings: bool,
    compress_images: bool,
    image_max_width: int,
    jpeg_quality: int,
) -> int:
    root = root.resolve()
    output = output.resolve()
    docs_dir, cache_dir = prepare_output(output)
    ctx = BuildContext(
        root=root,
        output=output,
        docs_dir=docs_dir,
        cache_dir=cache_dir,
        render_tikz=render_tikz,
        compress_images=compress_images,
        image_max_width=image_max_width,
        jpeg_quality=jpeg_quality,
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
        title = course_title(course_dir, entries_by_path)
        topic = topic_for_course(course_dir, entries_by_path)
        write_text(docs_dir / course_dir / "index.md", course_page_markdown(course_dir, course_notes, title, topic))
    write_text(docs_dir / "index.md", home_markdown(notes, courses, catalog_entries, entries_by_path))
    write_text(docs_dir / "assets" / "stylesheets" / "ai-notes.css", css_content())
    write_text(docs_dir / "assets" / "javascripts" / "mathjax.js", mathjax_config())
    write_text(output / "mkdocs.yml", generate_mkdocs_yml(courses, entries_by_path))
    print(f"Generated {len(notes)} note pages across {len(courses)} course pages in {output}")
    print_warning_report(ctx.warnings, verbose=verbose_warnings)
    if strict and not notes:
        return 1
    if fail_on_tikz_warnings and any(warning.kind in {"tikz_failed", "tikz_skipped"} for warning in ctx.warnings):
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root")
    parser.add_argument("--output", type=Path, default=Path(".web-build"), help="Generated MkDocs workspace")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if no notes can be generated")
    parser.add_argument("--skip-tikz", action="store_true", help="Keep TikZ source blocks instead of rendering SVG")
    parser.add_argument("--fail-on-tikz-warnings", action="store_true", help="Return non-zero if TikZ diagrams fall back to source blocks")
    parser.add_argument("--verbose-warnings", action="store_true", help="Print detailed warning messages")
    parser.add_argument("--no-compress-images", action="store_true", help="Copy JPG/PNG assets without resizing or recompressing")
    parser.add_argument("--image-max-width", type=int, default=1600, help="Maximum width for copied JPG/PNG assets")
    parser.add_argument("--jpeg-quality", type=int, default=82, help="JPEG quality for copied JPG assets")
    args = parser.parse_args()
    return build_site(
        args.root,
        args.output,
        strict=args.strict,
        fail_on_tikz_warnings=args.fail_on_tikz_warnings,
        render_tikz=not args.skip_tikz,
        verbose_warnings=args.verbose_warnings,
        compress_images=not args.no_compress_images,
        image_max_width=args.image_max_width,
        jpeg_quality=args.jpeg_quality,
    )


if __name__ == "__main__":
    raise SystemExit(main())

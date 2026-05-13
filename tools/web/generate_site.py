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
from typing import Callable
from urllib.parse import quote

from PIL import Image, ImageOps


SITE_URL = "https://hqhq1025.github.io/ai-course-notes/"
REPO_URL = "https://github.com/hqhq1025/ai-course-notes"
RAW_BASE_URL = f"{REPO_URL}/raw/main"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
PDF_EXTENSIONS = {".pdf"}
TIKZ_RENDERER_VERSION = "pdf-v2"
IMAGE_CACHE_VERSION = "image-v1"
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
            convert_latex_fragment(strip_document_shell(read_text(note.tex_path)), ctx)
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
        "20vc": "20VC with Harry Stebbings",
        "aitime": "AITIME 论道",
        "alibaba-cloud": "阿里云",
        "cs146s": "CS146S",
        "cs153": "CS153",
        "cs224n": "CS224N",
        "cs224r": "CS224R",
        "cs231n": "CS231N",
        "cs25": "CS25",
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
  --ai-notes-page-gutter: clamp(0.8rem, 2vw, 2rem);
  --ai-notes-rule-color: color-mix(in srgb, var(--md-default-fg-color), transparent 86%);
  --ai-notes-sidebar-toggle-size: 1.55rem;
}

@media screen and (min-width: 76.25em) {
  .md-grid {
    max-width: min(96rem, calc(100vw - 2 * var(--ai-notes-page-gutter)));
  }

  .md-main__inner {
    width: 100%;
  }

  .ai-notes-sidebar-toggle {
    align-items: center;
    background: color-mix(in srgb, var(--md-default-bg-color), var(--md-primary-fg-color) 6%);
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 999px;
    color: var(--md-default-fg-color--light);
    cursor: pointer;
    display: flex;
    height: var(--ai-notes-sidebar-toggle-size);
    justify-content: center;
    position: sticky;
    top: 3.4rem;
    transition: background-color 140ms ease, color 140ms ease, transform 140ms ease;
    width: var(--ai-notes-sidebar-toggle-size);
    z-index: 3;
  }

  .ai-notes-sidebar-toggle:hover {
    background: var(--md-accent-fg-color--transparent);
    color: var(--md-accent-fg-color);
  }

  .ai-notes-sidebar-toggle svg {
    height: 0.95rem;
    width: 0.95rem;
  }

  .ai-notes-sidebar-toggle--primary {
    float: right;
    margin: 0.15rem 0.2rem 0.45rem 0;
  }

  .ai-notes-sidebar-toggle--secondary {
    float: left;
    margin: 0.15rem 0 0.45rem 0.2rem;
  }

  body.ai-notes-nav-collapsed .md-sidebar--primary {
    display: none;
  }

  body.ai-notes-toc-collapsed .md-sidebar--secondary {
    display: none;
  }

  .ai-notes-sidebar-restore {
    background: var(--md-default-bg-color);
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 999px;
    box-shadow: var(--md-shadow-z1);
    color: var(--md-default-fg-color--light);
    cursor: pointer;
    display: none;
    height: 1.8rem;
    justify-content: center;
    position: fixed;
    top: 4.4rem;
    width: 1.8rem;
    z-index: 5;
  }

  .ai-notes-sidebar-restore:hover {
    color: var(--md-accent-fg-color);
  }

  .ai-notes-sidebar-restore svg {
    height: 1rem;
    width: 1rem;
  }

  .ai-notes-sidebar-restore--primary {
    left: max(0.55rem, var(--ai-notes-page-gutter));
  }

  .ai-notes-sidebar-restore--secondary {
    right: max(0.55rem, var(--ai-notes-page-gutter));
  }

  body.ai-notes-nav-collapsed .ai-notes-sidebar-restore--primary,
  body.ai-notes-toc-collapsed .ai-notes-sidebar-restore--secondary {
    display: flex;
  }
}

@media screen and (max-width: 76.234em) {
  .ai-notes-sidebar-toggle,
  .ai-notes-sidebar-restore {
    display: none;
  }
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

.md-typeset .admonition {
  border-radius: 0.45rem;
  box-shadow: none;
  margin: 1rem 0 1.3rem;
}

.md-typeset .admonition-title {
  font-weight: 700;
  letter-spacing: 0;
}

.md-typeset table:not([class]) {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.38rem;
  display: table;
  font-size: 0.88rem;
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

.md-typeset .ai-notes-table-caption {
  margin: -0.55rem 0 1.25rem;
  color: var(--md-default-fg-color--light);
  font-size: 0.78rem;
  line-height: 1.55;
  text-align: center;
}
""".strip()


def sidebar_script() -> str:
    return """
(function () {
  var sidebarConfigs = [
    {
      selector: ".md-sidebar--primary",
      collapsedClass: "ai-notes-nav-collapsed",
      storageKey: "ai-notes-sidebar-nav-collapsed",
      buttonClass: "ai-notes-sidebar-toggle--primary",
      restoreClass: "ai-notes-sidebar-restore--primary",
      collapseLabel: "折叠左侧导航",
      restoreLabel: "展开左侧导航",
      collapseIcon: "M15 6 9 12l6 6",
      restoreIcon: "M9 6l6 6-6 6"
    },
    {
      selector: ".md-sidebar--secondary",
      collapsedClass: "ai-notes-toc-collapsed",
      storageKey: "ai-notes-sidebar-toc-collapsed",
      buttonClass: "ai-notes-sidebar-toggle--secondary",
      restoreClass: "ai-notes-sidebar-restore--secondary",
      collapseLabel: "折叠右侧目录",
      restoreLabel: "展开右侧目录",
      collapseIcon: "M9 6l6 6-6 6",
      restoreIcon: "M15 6 9 12l6 6"
    }
  ];

  function icon(path) {
    return '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="' + path + '"></path></svg>';
  }

  function setCollapsed(config, collapsed) {
    document.body.classList.toggle(config.collapsedClass, collapsed);
    try {
      localStorage.setItem(config.storageKey, collapsed ? "1" : "0");
    } catch (_error) {
      return;
    }
  }

  function storedCollapsed(config) {
    try {
      return localStorage.getItem(config.storageKey) === "1";
    } catch (_error) {
      return false;
    }
  }

  function createButton(className, label, path) {
    var button = document.createElement("button");
    button.type = "button";
    button.className = className;
    button.setAttribute("aria-label", label);
    button.title = label;
    button.innerHTML = icon(path);
    return button;
  }

  function installToggle(config) {
    var sidebar = document.querySelector(config.selector);
    if (!sidebar) {
      return;
    }
    var scrollwrap = sidebar.querySelector(".md-sidebar__scrollwrap") || sidebar;
    var collapseButton = createButton(
      "ai-notes-sidebar-toggle " + config.buttonClass,
      config.collapseLabel,
      config.collapseIcon
    );
    var restoreButton = createButton(
      "ai-notes-sidebar-restore " + config.restoreClass,
      config.restoreLabel,
      config.restoreIcon
    );

    collapseButton.addEventListener("click", function () {
      setCollapsed(config, true);
    });
    restoreButton.addEventListener("click", function () {
      setCollapsed(config, false);
    });

    scrollwrap.prepend(collapseButton);
    document.body.appendChild(restoreButton);
    setCollapsed(config, storedCollapsed(config));
  }

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

  document.addEventListener("DOMContentLoaded", function () {
    sidebarConfigs.forEach(installToggle);
    installScrollMemory();
  });
})();
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
        "repo_name: hqhq1025/ai-course-notes",
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
        "  - assets/javascripts/ai-notes.js",
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
    return docs_dir, cache_dir, image_cache_dir


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
    write_text(docs_dir / "assets" / "javascripts" / "ai-notes.js", sidebar_script())
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
    parser.add_argument("--cache-dir", type=Path, default=None, help="Persistent cache root for generated TikZ SVGs and compressed images")
    parser.add_argument("--check-tikz-cache", action="store_true", help="Return zero when every TikZ diagram already has a cached SVG")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if no notes can be generated")
    parser.add_argument("--skip-tikz", action="store_true", help="Keep TikZ source blocks instead of rendering SVG")
    parser.add_argument("--fail-on-tikz-warnings", action="store_true", help="Return non-zero if TikZ diagrams fall back to source blocks")
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
        render_tikz=not args.skip_tikz,
        verbose_warnings=args.verbose_warnings,
        compress_images=not args.no_compress_images,
        image_max_width=args.image_max_width,
        jpeg_quality=args.jpeg_quality,
        cache_root=args.cache_dir,
    )


if __name__ == "__main__":
    raise SystemExit(main())

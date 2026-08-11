#!/usr/bin/env python3
"""Build a source manifest for one lecture directory.

The manifest is intentionally simple Markdown so agents can read it before
writing notes. It supports PDF decks, executable slide sources, local images,
and existing notes.
"""

from __future__ import annotations

import argparse
import ast
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


@dataclass
class SourceNode:
    node_id: str
    kind: str
    title: str
    source: str
    required: bool = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a lecture source manifest.")
    parser.add_argument("lecture_dir", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def pdf_pages(pdf: Path) -> int:
    try:
        out = subprocess.check_output(["pdfinfo", str(pdf)], text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return 0
    match = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(match.group(1)) if match else 0


def constant_text(call: ast.Call) -> str:
    if call.args and isinstance(call.args[0], ast.Constant):
        return str(call.args[0].value)
    return ""


def nodes_from_python(py: Path) -> list[SourceNode]:
    tree = ast.parse(py.read_text(encoding="utf-8", errors="ignore"))
    nodes: list[SourceNode] = []
    current_section = "opening"
    counter = 0
    for fn in [n for n in tree.body if isinstance(n, ast.FunctionDef)]:
        fn_calls = []
        for node in ast.walk(fn):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in {"text", "image"}:
                    fn_calls.append((getattr(node, "lineno", 0), node.func.id, constant_text(node)))
        for _lineno, kind, text in sorted(fn_calls):
            if kind == "text" and text.startswith("##"):
                current_section = text.lstrip("#").strip() or current_section
                counter += 1
                nodes.append(SourceNode(f"py-{counter:03d}", "section", current_section, f"{py.name}:{fn.name}"))
            elif kind == "text" and text.startswith("###"):
                counter += 1
                nodes.append(SourceNode(f"py-{counter:03d}", "subsection", text.lstrip("#").strip(), f"{py.name}:{fn.name}"))
            elif kind == "image":
                counter += 1
                title = text
                nodes.append(SourceNode(f"py-{counter:03d}", "figure", title, f"{py.name}:{fn.name}"))
            elif kind == "text" and text.strip():
                snippet = re.sub(r"\s+", " ", text.strip())
                if len(snippet) > 96:
                    snippet = snippet[:93] + "..."
                counter += 1
                nodes.append(SourceNode(f"py-{counter:03d}", "text", snippet, f"{py.name}:{fn.name}", required=False))
    return nodes


def nodes_from_pdf(pdf: Path) -> list[SourceNode]:
    slides_dir = pdf.parent / "slides-images"
    if slides_dir.exists():
        slide_images = sorted(
            path
            for path in slides_dir.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTS and path.stem.startswith("slide-")
        )
        if slide_images:
            return [
                SourceNode(
                    image.stem,
                    "slide",
                    str(image.relative_to(pdf.parent)),
                    pdf.name,
                )
                for image in slide_images
            ]

    pages = pdf_pages(pdf)
    return [
        SourceNode(f"slide-{i:03d}", "slide", f"Slide {i}", pdf.name)
        for i in range(1, pages + 1)
    ]


def local_images(lecture_dir: Path) -> list[Path]:
    images: list[Path] = []
    for dirname in ["slides-images", "images", "official-images", "figures", "frames"]:
        d = lecture_dir / dirname
        if d.exists():
            images.extend(sorted(p for p in d.iterdir() if p.suffix.lower() in IMAGE_EXTS))
    return images


def python_slide_sources(lecture_dir: Path) -> list[Path]:
    canonical = sorted(lecture_dir.glob("*slides*.py"))
    if canonical:
        return canonical
    return sorted(lecture_dir.glob("lecture_*.py"))


def supplementary_sources(lecture_dir: Path) -> list[Path]:
    sources: list[Path] = []
    for dirname in ["source-materials", "sources"]:
        directory = lecture_dir / dirname
        if directory.exists():
            sources.extend(
                sorted(path for path in directory.rglob("*") if path.is_file() and not path.name.startswith("."))
            )
    return sources


def write_manifest(lecture_dir: Path, output: Path) -> None:
    nodes: list[SourceNode] = []
    for pdf in sorted(lecture_dir.glob("*slides*.pdf")):
        nodes.extend(nodes_from_pdf(pdf))
    for py in python_slide_sources(lecture_dir):
        nodes.extend(nodes_from_python(py))

    images = local_images(lecture_dir)
    note = next(iter(sorted(lecture_dir.glob("*-notes.tex"))), None)
    lines = [
        f"# Source Manifest: `{lecture_dir}`",
        "",
        "## Files",
        "",
    ]
    for p in sorted(lecture_dir.iterdir()):
        if p.is_file() and p.suffix.lower() not in {".aux", ".log", ".out", ".toc"}:
            lines.append(f"- `{p.name}`")
    lines += [
        "",
        "## Supplementary Source Materials",
        "",
    ]
    sources = supplementary_sources(lecture_dir)
    if sources:
        for source in sources:
            lines.append(f"- `{source.relative_to(lecture_dir)}`")
    else:
        lines.append("- none found")

    lines += [
        "",
        "## Local Visual Assets",
        "",
    ]
    if images:
        for img in images:
            lines.append(f"- `{img.relative_to(lecture_dir)}`")
    else:
        lines.append("- none found")

    lines += [
        "",
        "## Coverage Nodes",
        "",
        "| ID | Type | Required | Source | Title / Snippet |",
        "|---|---|---|---|---|",
    ]
    for node in nodes:
        title = node.title.replace("|", "\\|")
        lines.append(f"| {node.node_id} | {node.kind} | {'yes' if node.required else 'optional'} | `{node.source}` | {title} |")

    lines += [
        "",
        "## Existing Note",
        "",
        f"- `{note.name}`" if note else "- none",
        "",
        "## Generation Contract",
        "",
        "- Review every slide and figure node; teaching-bearing nodes are required by default.",
        "- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.",
        "- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.",
        "- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.",
        "- Every important figure needs a nearby `读图` explanation.",
        "- Dense terminology clusters need a table or concept box.",
        "- Foundational concepts need diagram/table/formula scaffolding.",
        "- Final PDF must pass visual QA via rendered pages/contact sheet.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    lecture_dir = args.lecture_dir.resolve()
    output = args.output or (lecture_dir / "lecture-manifest.md")
    write_manifest(lecture_dir, output)
    print(output)


if __name__ == "__main__":
    main()

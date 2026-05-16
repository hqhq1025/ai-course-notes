#!/usr/bin/env python3
"""Render PDF pages and create a contact sheet for visual QA."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render PDF pages for visual QA.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--dpi", type=int, default=120)
    parser.add_argument("--thumb", default="240x340")
    parser.add_argument("--tile", default="4x")
    return parser.parse_args()


def run(cmd: list[str], log: Path | None = None) -> None:
    if log is None:
        subprocess.check_call(cmd)
        return
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(proc.stdout, encoding="utf-8", errors="ignore")
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, cmd, output=proc.stdout)


def nonwhite_ratio(path: Path) -> float:
    im = Image.open(path).convert("RGB")
    small = im.resize((max(1, im.width // 16), max(1, im.height // 16)))
    pixels = small.getdata()
    total = len(pixels)
    nonwhite = sum(1 for r, g, b in pixels if min(r, g, b) < 245)
    return nonwhite / total if total else 0.0


def rendered_pages(out_dir: Path) -> list[Path]:
    return sorted(out_dir.glob("page*.png"))


def clear_pages(out_dir: Path) -> None:
    for page in rendered_pages(out_dir):
        page.unlink()


def render_with_pdftoppm(pdf: Path, out_dir: Path, dpi: int) -> tuple[list[Path], Path]:
    log = out_dir / "pdftoppm.log"
    run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(out_dir / "page")], log)
    return rendered_pages(out_dir), log


def render_with_mutool(pdf: Path, out_dir: Path, dpi: int) -> tuple[list[Path], Path]:
    log = out_dir / "mutool.log"
    run(["mutool", "draw", "-r", str(dpi), "-o", str(out_dir / "page-%03d.png"), str(pdf)], log)
    return rendered_pages(out_dir), log


def main() -> None:
    args = parse_args()
    pdf = args.pdf.resolve()
    out_dir = args.out_dir or (pdf.parent / "qa" / pdf.stem)
    out_dir.mkdir(parents=True, exist_ok=True)
    clear_pages(out_dir)
    for stale in (out_dir / "contact.png", out_dir / "qa-report.md"):
        stale.unlink(missing_ok=True)

    renderer = ""
    render_log: Path | None = None
    if shutil.which("pdftoppm"):
        pages, render_log = render_with_pdftoppm(pdf, out_dir, args.dpi)
        renderer = "pdftoppm"
        blank_pages = [page for page in pages if nonwhite_ratio(page) < 0.005]
        if blank_pages and shutil.which("mutool"):
            clear_pages(out_dir)
            pages, render_log = render_with_mutool(pdf, out_dir, args.dpi)
            renderer = "mutool (fallback after blank-page detection)"
    elif shutil.which("mutool"):
        pages, render_log = render_with_mutool(pdf, out_dir, args.dpi)
        renderer = "mutool"
    else:
        raise SystemExit("Need pdftoppm or mutool for PDF rendering")

    if not pages:
        raise SystemExit("No rendered pages produced")
    blank_pages = [page.name for page in pages if nonwhite_ratio(page) < 0.005]

    contact = out_dir / "contact.png"
    if shutil.which("montage"):
        run(["montage", *map(str, pages), "-thumbnail", args.thumb, "-tile", args.tile, "-geometry", "+8+8", str(contact)])
    elif shutil.which("magick"):
        run(["magick", "montage", *map(str, pages), "-thumbnail", args.thumb, "-tile", args.tile, "-geometry", "+8+8", str(contact)])
    else:
        raise SystemExit("Need montage or magick for contact sheet")

    report = out_dir / "qa-report.md"
    report.write_text(
        "\n".join(
            [
                f"# PDF Visual QA: `{pdf.name}`",
                "",
                f"- PDF: `{pdf}`",
                f"- Rendered pages: `{out_dir}`",
                f"- Contact sheet: `{contact}`",
                f"- Page count rendered: {len(pages)}",
                f"- Renderer: {renderer}",
                f"- Renderer log: `{render_log}`" if render_log else "- Renderer log: none",
                f"- Near-blank rendered pages: {', '.join(blank_pages) if blank_pages else 'none'}",
                "",
                "## Manual Checklist",
                "",
                "- [ ] Figures render and are readable.",
                "- [ ] Tables/formulas/code do not spill outside margins.",
                "- [ ] Important figures have nearby explanations.",
                "- [ ] No orphan captions, stranded headings, or mostly blank pages.",
                "- [ ] Box titles and long URLs look sane.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(contact)
    print(report)


if __name__ == "__main__":
    main()

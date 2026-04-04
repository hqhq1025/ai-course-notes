#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]

COURSE_ROOTS = {
    "6s191",
    "agentic-rl",
    "cs25",
    "cs146s",
    "cs224n",
    "cs224r",
    "cs231n",
    "cs336",
    "kaist-cs492d",
    "llm-architect",
    "modern-agent",
}

COURSE_PREFIXES = {
    "talks/berkeley-llm-agents",
}

EXPLICIT_MIN_PAGES = {
    "talks/deepseek-china-ai": 30,
    "talks/state-of-ai-2026": 25,
    "talks/jensen-huang-nvidia": 15,
    "talks/jensen-huang-vision": 15,
    "talks/openclaw-agent": 25,
    "talks/qingke-agentic": 8,
    "talks/qingke-infra": 8,
}

SEMINAR_SERIES_PREFIXES = (
    "cs25/",
    "talks/berkeley-llm-agents/",
)


@dataclass
class AuditRow:
    tex: str
    pdf: str
    rel_dir: str
    note_type: str
    duration_text: str
    duration_minutes: int | None
    pages: int | None
    min_pages: int
    gap_pages: int
    boxes: int
    min_boxes: int
    gap_boxes: int
    has_importantbox: bool
    has_knowledgebox: bool
    has_warningbox: bool
    has_final_summary: bool
    summary_count: int
    notedate: str
    noteauthors: str
    videourl: str
    structural_failures: str
    pass_pages: bool
    pass_boxes: bool
    pass_structure: bool
    pass_all: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Full-repo note quality audit.")
    parser.add_argument(
        "--format",
        choices=["table", "json", "csv"],
        default="table",
        help="Output format.",
    )
    parser.add_argument(
        "--only-failures",
        action="store_true",
        help="Show only failing notes.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional file to write the report to.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def pdf_pages(pdf: Path) -> int | None:
    try:
        output = subprocess.check_output(
            ["pdfinfo", str(pdf)],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except Exception:
        return None
    match = re.search(r"^Pages:\s+(\d+)", output, flags=re.M)
    return int(match.group(1)) if match else None


def metadata_value(text: str, key: str) -> str:
    patterns = [
        rf"\\newcommand\{{\\{key}\}}\{{([^}}]*)\}}",
        rf"\\{key}\{{([^}}]*)\}}",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return ""


def parse_duration_minutes(raw: str) -> int | None:
    if not raw:
        return None

    text = raw.strip()
    normalized = (
        text.replace("约", "")
        .replace("分鐘", "分钟")
        .replace("小時", "小时")
        .replace("個", "")
        .replace("~", "")
        .replace("∼", "")
        .replace("$\\sim$", "")
    )

    if re.search(r"lecture|导论|视频时长|X Article|Article|阅读时长|阅读", normalized, re.I):
        return None

    match = re.search(r"(\d+)\s*:\s*(\d{2})(?::(\d{2}))?", normalized)
    if match:
        h_or_m = int(match.group(1))
        mm = int(match.group(2))
        ss = int(match.group(3) or 0)
        if h_or_m >= 1 and mm < 60:
            return h_or_m * 60 + mm + (1 if ss >= 30 else 0)

    total = 0
    found = False

    for pattern in [r"(\d+(?:\.\d+)?)\s*小时", r"(\d+(?:\.\d+)?)\s*h"]:
        match = re.search(pattern, normalized, re.I)
        if match:
            total += int(round(float(match.group(1)) * 60))
            found = True

    for pattern in [r"(\d+)\s*分钟", r"(\d+)\s*min", r"(\d+)\s*m(?![a-z])"]:
        match = re.search(pattern, normalized, re.I)
        if match:
            total += int(match.group(1))
            found = True

    return total if found else None


def note_type_for(rel_dir: str, duration_minutes: int | None, title: str, channel: str) -> str:
    if rel_dir.startswith("articles/"):
        return "article"
    if rel_dir.startswith("interviews/"):
        return "interview"
    if rel_dir.split("/", 1)[0] in COURSE_ROOTS:
        return "course"
    if any(rel_dir.startswith(prefix) for prefix in COURSE_PREFIXES):
        return "course"

    interview_like = False
    if rel_dir.startswith("talks/"):
        interview_like = (
            "访谈" in title
            or "podcast" in channel.lower()
            or duration_minutes is not None and duration_minutes >= 180
        )
    return "interview_like_talk" if interview_like else "talk"


def min_pages_for(rel_dir: str, note_type: str, duration_minutes: int | None) -> int:
    if rel_dir in EXPLICIT_MIN_PAGES:
        return EXPLICIT_MIN_PAGES[rel_dir]

    if any(rel_dir.startswith(prefix) for prefix in SEMINAR_SERIES_PREFIXES):
        if duration_minutes is not None and duration_minutes >= 90:
            return 8
        if duration_minutes is not None and duration_minutes >= 30:
            return 6
        return 5

    if note_type == "article":
        return 8
    if note_type in {"interview", "interview_like_talk"}:
        if duration_minutes is None:
            return 15
        if duration_minutes >= 300:
            return 30
        if duration_minutes >= 180:
            return 25
        if duration_minutes >= 60:
            return 15
        if duration_minutes >= 30:
            return 8
        return 5

    if note_type == "course":
        if duration_minutes is not None:
            if duration_minutes >= 90:
                return 10
            if duration_minutes >= 30:
                return 8
            return 5
        return 8

    if duration_minutes is not None and duration_minutes < 30:
        return 5
    return 8


def min_boxes_for(min_pages: int) -> int:
    if min_pages >= 30:
        return 20
    if min_pages >= 25:
        return 15
    if min_pages >= 20:
        return 10
    if min_pages >= 15:
        return 8
    if min_pages >= 8:
        return 5
    return 3


def structural_failures(text: str, notedate: str, authors: str, videourl: str) -> list[str]:
    failures: list[str] = []
    if r"\section{总结与延伸}" not in text:
        failures.append("missing-final-summary")
    if "本章小结" not in text:
        failures.append("missing-section-summary")
    if not notedate or notedate == r"\today" or notedate == "[在此填写日期]":
        failures.append("bad-notedate")
    bad_authors = {
        "五道口纳什 & Codex",
        r"五道口纳什 \& Codex",
        "五道口纳什 & AI",
        r"五道口纳什 \& AI",
        "五道口纳什 & Claude",
        r"五道口纳什 \& Claude",
    }
    if authors in bad_authors:
        failures.append("bad-author")
    if "视频链接：未填写" in text or "文章链接：未填写" in text:
        failures.append("visible-missing-link")
    return failures


def iter_rows() -> Iterable[AuditRow]:
    for tex in sorted(ROOT.rglob("*-notes.tex")):
        if ".git" in tex.parts or "tools/templates" in str(tex):
            continue
        # Parallel workers may briefly replace files during rewrites; skip paths
        # that disappear between globbing and read time instead of aborting audit.
        if not tex.exists():
            continue
        rel_tex = tex.relative_to(ROOT)
        pdf = tex.with_suffix(".pdf")
        rel_dir = str(rel_tex.parent).replace("\\", "/")
        try:
            text = read_text(tex)
        except FileNotFoundError:
            continue
        duration_text = metadata_value(text, "videoduration")
        duration_minutes = parse_duration_minutes(duration_text)
        title = metadata_value(text, "notetitle")
        channel = metadata_value(text, "videochannel")
        notedate = metadata_value(text, "notedate")
        authors = metadata_value(text, "noteauthors")
        videourl = metadata_value(text, "videourl")
        note_type = note_type_for(rel_dir, duration_minutes, title, channel)
        min_pages = min_pages_for(rel_dir, note_type, duration_minutes)
        min_boxes = min_boxes_for(min_pages)
        pages = pdf_pages(pdf) if pdf.exists() else None
        boxes = len(re.findall(r"importantbox|knowledgebox|warningbox", text))
        summary_count = len(re.findall(r"本章小结|总结与延伸", text))
        failures = structural_failures(text, notedate, authors, videourl)
        gap_pages = max(0, min_pages - (pages or 0))
        gap_boxes = max(0, min_boxes - boxes)
        pass_pages = pages is not None and pages >= min_pages
        pass_boxes = (
            boxes >= min_boxes
            and "importantbox" in text
            and "knowledgebox" in text
            and "warningbox" in text
        )
        pass_structure = not failures
        yield AuditRow(
            tex=str(rel_tex),
            pdf=str(pdf.relative_to(ROOT)),
            rel_dir=rel_dir,
            note_type=note_type,
            duration_text=duration_text,
            duration_minutes=duration_minutes,
            pages=pages,
            min_pages=min_pages,
            gap_pages=gap_pages,
            boxes=boxes,
            min_boxes=min_boxes,
            gap_boxes=gap_boxes,
            has_importantbox="importantbox" in text,
            has_knowledgebox="knowledgebox" in text,
            has_warningbox="warningbox" in text,
            has_final_summary=r"\section{总结与延伸}" in text,
            summary_count=summary_count,
            notedate=notedate,
            noteauthors=authors,
            videourl=videourl,
            structural_failures=",".join(failures),
            pass_pages=pass_pages,
            pass_boxes=pass_boxes,
            pass_structure=pass_structure,
            pass_all=pass_pages and pass_boxes and pass_structure,
        )


def render_table(rows: list[AuditRow]) -> str:
    lines = []
    header = [
        "status",
        "pages",
        "min",
        "gap",
        "boxes",
        "minb",
        "type",
        "duration",
        "dir",
        "structural_failures",
    ]
    lines.append("\t".join(header))
    for row in rows:
        lines.append(
            "\t".join(
                [
                    "PASS" if row.pass_all else "FAIL",
                    str(row.pages or 0),
                    str(row.min_pages),
                    str(row.gap_pages),
                    str(row.boxes),
                    str(row.min_boxes),
                    row.note_type,
                    row.duration_text,
                    row.rel_dir,
                    row.structural_failures,
                ]
            )
        )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    rows = sorted(
        iter_rows(),
        key=lambda row: (
            row.pass_all,
            -row.gap_pages,
            -row.gap_boxes,
            row.rel_dir,
        ),
    )
    if args.only_failures:
        rows = [row for row in rows if not row.pass_all]

    if args.format == "json":
        output = json.dumps([asdict(row) for row in rows], ensure_ascii=False, indent=2)
    elif args.format == "csv":
        if rows:
            fields = list(asdict(rows[0]).keys())
        else:
            fields = list(AuditRow.__annotations__.keys())
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))
        output = buffer.getvalue()
    else:
        output = render_table(rows)

    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()

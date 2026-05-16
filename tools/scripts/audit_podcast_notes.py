#!/usr/bin/env python3
"""Audit podcast/interview style notes and queue files.

This is intentionally heuristic. It is meant to catch systemic workflow issues:
thin notes, missing source manifests, missing PDF visual QA, figures without
read-the-figure treatment, and duplicate-prone queue entries.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


DEFAULT_ROOTS = ("modern-agent", "agentic-rl", "llm-architect", "youtube")


def pdf_pages(pdf: Path) -> int:
    if not pdf.exists():
        return 0
    try:
        out = subprocess.check_output(
            ["pdfinfo", str(pdf)],
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except Exception:
        return 0
    match = re.search(r"^Pages:\s+(\d+)", out, re.MULTILINE)
    return int(match.group(1)) if match else 0


def audit_notes(roots: list[Path]) -> list[dict]:
    rows: list[dict] = []
    for root in roots:
        if not root.exists():
            continue
        for tex in sorted(root.glob("**/*-notes.tex")):
            if ".web-build" in tex.parts or "site" in tex.parts:
                continue
            text = tex.read_text(errors="replace")
            rows.append({
                "tex": str(tex),
                "pages": pdf_pages(tex.with_suffix(".pdf")),
                "pdf": tex.with_suffix(".pdf").exists(),
                "sections": text.count("\\section{"),
                "boxes": len(re.findall(r"\\begin\{(?:importantbox|knowledgebox|warningbox)\}", text)),
                "figs": text.count("\\includegraphics"),
                "readfig": text.count("读图"),
                "summaries": text.count("本章小结") + text.count("总结与延伸"),
                "manifest": (tex.parent / "lecture-manifest.md").exists(),
                "qa": any(tex.parent.glob("qa/**/qa-report.md")),
            })
    return rows


def audit_queue(queue_path: Path) -> dict | None:
    if not queue_path.exists():
        return None
    data = json.loads(queue_path.read_text())
    items = data.get("items") or []
    markers = ["含字幕", "视频", "纯享版", "投屏版", "英文", "加更英文原声版", "音频版", "串台"]
    marker_hits = {
        marker: [item for item in items if marker in (item.get("title") or "")]
        for marker in markers
    }
    return {
        "path": str(queue_path),
        "items": len(items),
        "kind_counts": Counter(item.get("kind", "unknown") for item in items),
        "status_counts": Counter(item.get("status", "unknown") for item in items),
        "missing_episode": [item for item in items if not item.get("episode")],
        "marker_hits": marker_hits,
        "english_video_series": len(data.get("english_video_series") or []),
    }


def print_markdown(rows: list[dict], queues: list[dict]) -> None:
    print("# Podcast Notes Audit\n")
    print("## Notes\n")
    print("| file | pages | boxes | figs | readfig | summaries | manifest | qa | flags |")
    print("|---|---:|---:|---:|---:|---:|---|---|---|")
    for row in rows:
        flags = []
        if row["pages"] < 8:
            flags.append("thin")
        if row["figs"] < 3:
            flags.append("few-figures")
        if row["figs"] and row["readfig"] == 0:
            flags.append("no-readfig")
        if not row["manifest"]:
            flags.append("no-manifest")
        if not row["qa"]:
            flags.append("no-visual-qa")
        print(
            f"| {row['tex']} | {row['pages']} | {row['boxes']} | {row['figs']} | "
            f"{row['readfig']} | {row['summaries']} | {row['manifest']} | {row['qa']} | "
            f"{', '.join(flags)} |"
        )

    print("\n## Summary\n")
    print(f"- Notes audited: {len(rows)}")
    print(f"- Thin notes pages<8: {sum(row['pages'] < 8 for row in rows)}")
    print(f"- Notes with figs<3: {sum(row['figs'] < 3 for row in rows)}")
    print(f"- Notes with figures but no `读图`: {sum(row['figs'] > 0 and row['readfig'] == 0 for row in rows)}")
    print(f"- Notes missing manifest: {sum(not row['manifest'] for row in rows)}")
    print(f"- Notes missing visual QA: {sum(not row['qa'] for row in rows)}")

    if queues:
        print("\n## Queues\n")
        for queue in queues:
            print(f"### `{queue['path']}`\n")
            print(f"- Items: {queue['items']}")
            print(f"- English/video-series supplements: {queue['english_video_series']}")
            print(f"- Kind counts: {dict(queue['kind_counts'])}")
            print(f"- Status counts: {dict(queue['status_counts'])}")
            print(f"- Missing episode number: {len(queue['missing_episode'])}")
            for marker, hits in queue["marker_hits"].items():
                if hits:
                    print(f"- Title marker `{marker}`: {len(hits)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("roots", nargs="*", default=list(DEFAULT_ROOTS))
    parser.add_argument("--queue", action="append", default=["youtube/zhangxiaojun/queue.json"])
    args = parser.parse_args()

    rows = audit_notes([Path(root) for root in args.roots])
    queues = [q for q in (audit_queue(Path(path)) for path in args.queue) if q]
    print_markdown(rows, queues)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def format_time(seconds: int) -> str:
    return f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build five-minute teacher-voice blocks for a panel discussion.")
    parser.add_argument("lecture_dir", type=Path)
    parser.add_argument("--window", type=int, default=300)
    args = parser.parse_args()

    segments = json.loads((args.lecture_dir / "subs.json").read_text())["segments"]
    duration = int(max(segment["end"] for segment in segments))
    lines = [
        "# Teacher Voice Ledger",
        "",
        "| Time window | Discussion points | Why it matters | Where it appears in note |",
        "|---|---|---|---|",
    ]
    for start in range(0, duration + 1, args.window):
        end = start + args.window
        spoken = "".join(
            segment["text"] for segment in segments
            if segment["end"] >= start and segment["start"] < end
        ).replace("|", "\\|")
        lines.append(
            f"| {format_time(start)}--{format_time(min(end, duration))} | {spoken} | Preserve positions, disagreements, examples, and caveats | synthesized in panel chapter |"
        )
    (args.lecture_dir / "teacher-voice-ledger.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

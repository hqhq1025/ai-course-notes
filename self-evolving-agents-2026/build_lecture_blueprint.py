#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def format_time(seconds: float) -> str:
    value = int(seconds)
    return f"{value // 3600:02d}:{value % 3600 // 60:02d}:{value % 60:02d}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Align selected slides with Whisper segments.")
    parser.add_argument("lecture_dir", type=Path)
    args = parser.parse_args()

    slides = json.loads((args.lecture_dir / "slide-selection.json").read_text())
    transcript = json.loads((args.lecture_dir / "subs.json").read_text())["segments"]
    rows = []
    for index, slide in enumerate(slides):
        start = slide["timestamp_seconds"]
        end = slides[index + 1]["timestamp_seconds"] if index + 1 < len(slides) else float("inf")
        spoken = "".join(
            segment["text"]
            for segment in transcript
            if segment["end"] >= start and segment["start"] < end
        )
        rows.append({**slide, "end_seconds": None if end == float("inf") else end, "spoken": spoken})

    manifest_lines = [
        "# Lecture Source Manifest",
        "",
        "## Local Sources",
        "",
        "- `video.mp4`: merged public Bilibili video stream.",
        "- `audio.wav`: 16 kHz mono transcription input.",
        "- `subs.srt` / `subs.txt` / `subs.json`: local Whisper transcript.",
        "- `frame-candidates/`: 15-second visual sampling.",
        "- `slides-images/`: cropped, perceptually deduplicated slide candidates.",
        "",
        "## Coverage Matrix",
        "",
        "| # | Time | Slide | Spoken explanation | Planned treatment | Status |",
        "|---:|---|---|---|---|---|",
    ]
    for index, row in enumerate(rows, 1):
        excerpt = row["spoken"].replace("|", "\\|")[:180]
        manifest_lines.append(
            f"| {index} | {format_time(row['timestamp_seconds'])} | `{row['file']}` | {excerpt} | Identify claim, visual reading, limits, and connection | pending |"
        )
    (args.lecture_dir / "lecture-manifest.md").write_text("\n".join(manifest_lines) + "\n")

    ledger_lines = [
        "# Teacher Voice Ledger",
        "",
        "| Time / source node | Spoken point | Why it matters | Where it appears in note |",
        "|---|---|---|---|",
    ]
    for row in rows:
        spoken = row["spoken"].replace("|", "\\|")
        ledger_lines.append(
            f"| {format_time(row['timestamp_seconds'])} | {spoken} | Preserve motivation, caveat, example, or transition | pending |"
        )
    (args.lecture_dir / "teacher-voice-ledger.md").write_text("\n".join(ledger_lines) + "\n")
    print(f"slides={len(rows)} transcript_segments={len(transcript)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Convert SRT captions into readable timestamped text and fixed-time chunks."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


TIMESTAMP_RE = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2},\d{3})\s+-->\s+(?P<end>\d{2}:\d{2}:\d{2},\d{3})"
)


@dataclass(frozen=True)
class Caption:
    start_ms: int
    end_ms: int
    text: str


def timestamp_to_ms(value: str) -> int:
    hours, minutes, rest = value.split(":")
    seconds, millis = rest.split(",")
    return (
        int(hours) * 3_600_000
        + int(minutes) * 60_000
        + int(seconds) * 1_000
        + int(millis)
    )


def format_time(milliseconds: int) -> str:
    total_seconds = milliseconds // 1_000
    hours, remainder = divmod(total_seconds, 3_600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def parse_srt(path: Path) -> list[Caption]:
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig").strip())
    captions: list[Caption] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        timestamp_index = next(
            (index for index, line in enumerate(lines) if TIMESTAMP_RE.fullmatch(line)),
            None,
        )
        if timestamp_index is None:
            continue
        match = TIMESTAMP_RE.fullmatch(lines[timestamp_index])
        assert match is not None
        text = " ".join(lines[timestamp_index + 1 :])
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        captions.append(
            Caption(
                start_ms=timestamp_to_ms(match.group("start")),
                end_ms=timestamp_to_ms(match.group("end")),
                text=text,
            )
        )
    return captions


def render_timed(captions: list[Caption]) -> str:
    return "\n".join(
        f"[{format_time(caption.start_ms)}--{format_time(caption.end_ms)}] {caption.text}"
        for caption in captions
    ) + "\n"


def render_chunks(captions: list[Caption], chunk_minutes: int) -> str:
    chunk_ms = chunk_minutes * 60_000
    sections: list[str] = []
    current_chunk = -1
    current_text: list[str] = []
    current_start = 0
    current_end = 0

    def flush() -> None:
        if not current_text:
            return
        paragraph = re.sub(r"\s+", " ", " ".join(current_text)).strip()
        sections.append(
            f"## {format_time(current_start)}--{format_time(current_end)}\n\n{paragraph}\n"
        )

    for caption in captions:
        chunk_index = caption.start_ms // chunk_ms
        if chunk_index != current_chunk:
            flush()
            current_chunk = chunk_index
            current_start = chunk_index * chunk_ms
            current_text = []
        current_end = caption.end_ms
        current_text.append(caption.text)
    flush()
    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("srt", type=Path)
    parser.add_argument("--timed-output", type=Path, required=True)
    parser.add_argument("--chunked-output", type=Path, required=True)
    parser.add_argument("--chunk-minutes", type=int, default=5)
    args = parser.parse_args()

    captions = parse_srt(args.srt)
    args.timed_output.write_text(render_timed(captions), encoding="utf-8")
    args.chunked_output.write_text(
        render_chunks(captions, args.chunk_minutes), encoding="utf-8"
    )
    print(f"{args.srt}: {len(captions)} captions")


if __name__ == "__main__":
    main()

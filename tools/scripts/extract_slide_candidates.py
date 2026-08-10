#!/usr/bin/env python3
"""Extract stable, full-screen slide candidates from lecture recordings."""

from __future__ import annotations

import argparse
import csv
import math
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


@dataclass
class Sample:
    timestamp: float
    path: Path
    gray: np.ndarray
    bright_ratio: float
    diff: float = 0.0


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def format_time(seconds: float) -> str:
    rounded = int(round(seconds))
    hours, remainder = divmod(rounded, 3_600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def image_features(path: Path) -> tuple[np.ndarray, float]:
    image = Image.open(path).convert("RGB").resize((64, 36))
    rgb = np.asarray(image, dtype=np.float32)
    gray = rgb.mean(axis=2)
    return gray, float((gray > 180).mean())


def cluster_samples(
    samples: list[Sample], bright_threshold: float, diff_threshold: float
) -> list[Sample]:
    slide_samples = [sample for sample in samples if sample.bright_ratio >= bright_threshold]
    if not slide_samples:
        return []

    clusters: list[Sample] = []
    current = slide_samples[0]
    for sample in slide_samples[1:]:
        difference = float(np.abs(sample.gray - current.gray).mean())
        sample.diff = difference
        if difference <= diff_threshold:
            current = sample
        else:
            clusters.append(current)
            current = sample
    clusters.append(current)
    return clusters


def extract_full_resolution(video: Path, timestamp: float, output: Path, crop: str) -> None:
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{timestamp:.3f}",
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-vf",
            f"crop={crop}",
            "-q:v",
            "2",
            "-y",
            str(output),
        ]
    )


def ocr_title(path: Path) -> str:
    if shutil.which("tesseract") is None:
        return ""
    result = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "6"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    lines = [" ".join(line.split()) for line in result.stdout.splitlines() if line.strip()]
    return " | ".join(lines[:3])[:500]


def build_contact_sheets(candidates: list[tuple[Sample, Path, str]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    columns = 4
    rows = 4
    cell_width = 400
    image_height = 225
    label_height = 42
    cell_height = image_height + label_height
    font = ImageFont.load_default(size=16)

    for sheet_index in range(math.ceil(len(candidates) / (columns * rows))):
        subset = candidates[sheet_index * columns * rows : (sheet_index + 1) * columns * rows]
        sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), "white")
        draw = ImageDraw.Draw(sheet)
        for index, (sample, image_path, title) in enumerate(subset):
            x = (index % columns) * cell_width
            y = (index // columns) * cell_height
            image = Image.open(image_path).convert("RGB")
            image.thumbnail((cell_width, image_height))
            paste_x = x + (cell_width - image.width) // 2
            paste_y = y + (image_height - image.height) // 2
            sheet.paste(image, (paste_x, paste_y))
            label = f"{sheet_index * columns * rows + index + 1:03d}  {format_time(sample.timestamp)}"
            draw.rectangle((x, y + image_height, x + cell_width, y + cell_height), fill="#111111")
            draw.text((x + 8, y + image_height + 4), label, fill="white", font=font)
            if title:
                draw.text(
                    (x + 8, y + image_height + 22),
                    title[:48],
                    fill="#dddddd",
                    font=ImageFont.load_default(),
                )
        sheet.save(output_dir / f"contact-{sheet_index + 1:02d}.jpg", quality=92)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--interval", type=float, default=8.0)
    parser.add_argument("--crop", default="1766:992:78:88")
    parser.add_argument("--bright-threshold", type=float, default=0.75)
    parser.add_argument("--diff-threshold", type=float, default=3.0)
    parser.add_argument("--skip-ocr", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    candidate_dir = args.output_dir / "candidates"
    contact_dir = args.output_dir / "contact-sheets"
    candidate_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="slide-samples-") as temporary:
        sample_dir = Path(temporary)
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(args.video),
                "-vf",
                f"fps=1/{args.interval},crop={args.crop},scale=640:-1",
                "-q:v",
                "5",
                str(sample_dir / "sample-%05d.jpg"),
            ]
        )

        samples: list[Sample] = []
        for index, sample_path in enumerate(sorted(sample_dir.glob("sample-*.jpg"))):
            gray, bright_ratio = image_features(sample_path)
            samples.append(
                Sample(
                    timestamp=index * args.interval,
                    path=sample_path,
                    gray=gray,
                    bright_ratio=bright_ratio,
                )
            )
        selected = cluster_samples(samples, args.bright_threshold, args.diff_threshold)

    extracted: list[tuple[Sample, Path, str]] = []
    for index, sample in enumerate(selected, start=1):
        timestamp_label = format_time(sample.timestamp).replace(":", "-")
        output = candidate_dir / f"slide-{index:03d}-{timestamp_label}.jpg"
        extract_full_resolution(args.video, sample.timestamp, output, args.crop)
        title = "" if args.skip_ocr else ocr_title(output)
        extracted.append((sample, output, title))

    with (args.output_dir / "index.tsv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["candidate", "timestamp", "bright_ratio", "diff", "file", "ocr"])
        for index, (sample, output, title) in enumerate(extracted, start=1):
            writer.writerow(
                [
                    index,
                    format_time(sample.timestamp),
                    f"{sample.bright_ratio:.4f}",
                    f"{sample.diff:.4f}",
                    output.relative_to(args.output_dir),
                    title,
                ]
            )

    build_contact_sheets(extracted, contact_dir)
    print(
        f"{args.video}: {len(samples)} samples, "
        f"{sum(sample.bright_ratio >= args.bright_threshold for sample in samples)} slide frames, "
        f"{len(extracted)} candidates"
    )


if __name__ == "__main__":
    main()

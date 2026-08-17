#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


def visual_distance(left: Image.Image, right: Image.Image) -> float:
    left_gray = left.convert("L").resize((128, 72))
    right_gray = right.convert("L").resize((128, 72))
    difference = ImageChops.difference(left_gray, right_gray)
    return ImageStat.Stat(difference).mean[0]


def main() -> None:
    parser = argparse.ArgumentParser(description="Crop and deduplicate slide frames from the NICE event layout.")
    parser.add_argument("lecture_dir", type=Path)
    parser.add_argument("--interval", type=int, default=15, help="Seconds between source frame candidates")
    parser.add_argument("--threshold", type=float, default=1.8, help="Minimum mean pixel difference for a new slide")
    args = parser.parse_args()

    candidates = sorted((args.lecture_dir / "frame-candidates").glob("frame-*.jpg"))
    output_dir = args.lecture_dir / "slides-images"
    output_dir.mkdir(parents=True, exist_ok=True)

    selected = []
    previous_slide = None
    for old_slide in output_dir.glob("slide-*.jpg"):
        old_slide.unlink()
    for candidate in candidates:
        frame_number = int(candidate.stem.split("-")[-1])
        timestamp = (frame_number - 1) * args.interval
        with Image.open(candidate) as image:
            width, height = image.size
            slide = image.crop((int(width * 0.075), int(height * 0.115), int(width * 0.835), int(height * 0.89)))
            distance = None if previous_slide is None else visual_distance(slide, previous_slide)
            if previous_slide is not None and distance < args.threshold:
                continue
            filename = f"slide-{len(selected) + 1:03d}-{timestamp:05d}s.jpg"
            slide.save(output_dir / filename, quality=92, subsampling=0)
            selected.append({
                "file": f"slides-images/{filename}",
                "source_frame": candidate.name,
                "timestamp_seconds": timestamp,
                "hash_distance": distance,
            })
            previous_slide = slide.copy()

    (args.lecture_dir / "slide-selection.json").write_text(
        json.dumps(selected, ensure_ascii=False, indent=2) + "\n"
    )
    print(f"selected={len(selected)} candidates={len(candidates)}")


if __name__ == "__main__":
    main()

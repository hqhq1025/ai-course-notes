#!/usr/bin/env python3
"""Prepare official CS336 Spring 2026 source packs without downloading videos."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COURSE_DIR = ROOT / "cs336-2026"
RAW_BASE = "https://raw.githubusercontent.com/stanford-cs336/lectures/main"
WDKNS_COMMIT = "39f1a04c46e1d0d70f6b71a8fcf079b305a632b9"
LECTURES_COMMIT = "8b59b50730766695c2ffedd1a79c50cd09b9eb91"


@dataclass(frozen=True)
class Lecture:
    number: int
    video_id: str
    topic: str
    date: str
    speaker: str
    source: str | None

    @property
    def slug(self) -> str:
        return f"lecture{self.number:02d}"

    @property
    def url(self) -> str:
        return f"https://www.youtube.com/watch?v={self.video_id}"


LECTURES = [
    Lecture(1, "JuoVZkPBiKk", "Overview, Tokenization", "2026-03-30", "Percy Liang", "lecture_01.py"),
    Lecture(2, "kuYAsz7zspQ", "PyTorch, einops, Resource Accounting", "2026-04-01", "Percy Liang", "lecture_02.py"),
    Lecture(3, "lVynu4bo1rY", "Architectures, Hyperparameters", "2026-04-06", "Tatsunori Hashimoto", "lecture_03.pdf"),
    Lecture(4, "cKSwj_qZ8Jg", "Attention Alternatives and Mixture of Experts", "2026-04-08", "Tatsunori Hashimoto", "lecture_04.pdf"),
    Lecture(5, "izZba4UA7iY", "GPUs, TPUs", "2026-04-13", "Tatsunori Hashimoto", "lecture_05.pdf"),
    Lecture(6, "xnDHaNUvHBg", "Kernels, Triton, XLA", "2026-04-15", "Percy Liang", "lecture_06.py"),
    Lecture(7, "SzpOcwdIL0Y", "Parallelism I", "2026-04-20", "Percy Liang", "lecture_07.py"),
    Lecture(8, "6-cXp-aOmdg", "Parallelism II", "2026-04-22", "Tatsunori Hashimoto", "lecture_08.pdf"),
    Lecture(9, "Q15rhEWZPQ4", "Scaling Laws I", "2026-04-27", "Tatsunori Hashimoto", "lecture_09.pdf"),
    Lecture(10, "EfM546A79aM", "Inference", "2026-04-29", "Percy Liang", "lecture_10.py"),
    Lecture(11, "vTfEyOyzV9E", "Scaling Laws II", "2026-05-04", "Tatsunori Hashimoto", "lecture_11.pdf"),
    Lecture(12, "JpAxdTWQJxM", "Evaluation", "2026-05-06", "Percy Liang", "lecture_12.py"),
    Lecture(13, "-qm0ln33G24", "Data: Sources and Datasets", "2026-05-11", "Percy Liang", "lecture_13.py"),
    Lecture(14, "5sxHosTLPF8", "Data: Filtering, Deduplication, Mixing, Synthetic Data", "2026-05-13", "Percy Liang", "lecture_14.py"),
    Lecture(15, "2oH6PWPrYFo", "Mid/Post-Training: SFT and RLHF", "2026-05-18", "Tatsunori Hashimoto", "lecture_15.pdf"),
    Lecture(16, "dIFAi87Ws4E", "Post-Training: RLVR", "2026-05-20", "Tatsunori Hashimoto", "lecture_16.pdf"),
    Lecture(17, "26FtD08ZpOU", "Alignment and Multimodality", "2026-05-27", "Percy Liang", "lecture_17.py"),
    Lecture(18, "9EEm4iMAF5s", "Guest Lecture: Dan Fu", "2026-06-03", "Dan Fu", None),
]


def run(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": "ai-course-notes/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        destination.write_bytes(response.read())


def timestamp_to_seconds(value: str) -> float:
    hours, minutes, seconds = value.replace(",", ".").split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def seconds_to_timestamp(value: float) -> str:
    total = max(0, int(value))
    return f"{total // 3600:02d}:{(total % 3600) // 60:02d}:{total % 60:02d}"


def clean_srt(srt_path: Path, timed_path: Path, clean_path: Path) -> None:
    blocks = re.split(r"\n\s*\n", srt_path.read_text(encoding="utf-8", errors="ignore").strip())
    cues: list[tuple[float, float, str]] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        time_index = next((i for i, line in enumerate(lines) if " --> " in line), None)
        if time_index is None:
            continue
        start, end = lines[time_index].split(" --> ", 1)
        text = " ".join(lines[time_index + 1 :])
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            continue
        cues.append((timestamp_to_seconds(start), timestamp_to_seconds(end), text))

    def normalized_token(token: str) -> str:
        return re.sub(r"(^\W+|\W+$)", "", token).lower()

    def novel_suffix(previous: str, current: str) -> str:
        previous_tokens = previous.split()
        current_tokens = current.split()
        previous_normalized = [normalized_token(token) for token in previous_tokens]
        current_normalized = [normalized_token(token) for token in current_tokens]
        max_overlap = min(len(previous_tokens), len(current_tokens), 40)
        overlap = 0
        for size in range(max_overlap, 0, -1):
            if previous_normalized[-size:] == current_normalized[:size]:
                overlap = size
                break
        if overlap == len(current_tokens):
            return ""
        return " ".join(current_tokens[overlap:]).strip()

    novel_cues: list[tuple[float, float, str]] = []
    previous_full_text = ""
    for start, end, text in cues:
        novel = novel_suffix(previous_full_text, text) if previous_full_text else text
        previous_full_text = text
        if novel:
            novel_cues.append((start, end, novel))

    deduped: list[tuple[float, float, str]] = []
    for start, end, text in novel_cues:
        if deduped:
            prev_start, prev_end, prev_text = deduped[-1]
            word_count = len(prev_text.split())
            sentence_complete = bool(re.search(r"[.!?][\"']?$", prev_text))
            if start - prev_end <= 2.5 and word_count < 34 and not sentence_complete:
                deduped[-1] = (prev_start, end, f"{prev_text} {text}".strip())
                continue
        deduped.append((start, end, text))

    timed_path.write_text(
        "\n".join(
            f"[{seconds_to_timestamp(start)}--{seconds_to_timestamp(end)}] {text}"
            for start, end, text in deduped
        )
        + "\n",
        encoding="utf-8",
    )
    clean_path.write_text("\n".join(text for _, _, text in deduped) + "\n", encoding="utf-8")


def prepare_video_assets(lecture: Lecture, directory: Path) -> dict:
    output = directory / lecture.slug
    run(
        [
            "yt-dlp",
            "--skip-download",
            "--write-info-json",
            "--write-thumbnail",
            "--convert-thumbnails",
            "jpg",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en,en-orig",
            "--convert-subs",
            "srt",
            "-o",
            str(output) + ".%(ext)s",
            lecture.url,
        ]
    )

    info_path = directory / f"{lecture.slug}.info.json"
    info = json.loads(info_path.read_text(encoding="utf-8"))
    metadata = {
        **asdict(lecture),
        "url": lecture.url,
        "title": info.get("title"),
        "upload_date": info.get("upload_date"),
        "duration": info.get("duration"),
        "duration_string": info.get("duration_string"),
        "channel": info.get("channel"),
        "playlist_id": "PLoROMvodv4rMqXOcazWaTUHhq-yembLCV",
        "wdkns_skills_commit": WDKNS_COMMIT,
        "official_lectures_commit": LECTURES_COMMIT,
    }
    (directory / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    thumbnails = sorted(directory.glob(f"{lecture.slug}*.jpg"))
    if thumbnails:
        shutil.copyfile(thumbnails[0], directory / "cover.jpg")

    subtitles = sorted(directory.glob(f"{lecture.slug}*.srt"))
    if subtitles:
        preferred = next((path for path in subtitles if ".en." in path.name), subtitles[0])
        canonical_subtitle = directory / f"{lecture.slug}.en.srt"
        if preferred != canonical_subtitle:
            shutil.copyfile(preferred, canonical_subtitle)
        clean_srt(
            canonical_subtitle,
            directory / "transcript_timed.txt",
            directory / "transcript_clean.txt",
        )
    return metadata


def prepare_official_source(lecture: Lecture, directory: Path) -> None:
    if lecture.source is None:
        return
    suffix = Path(lecture.source).suffix
    source_path = directory / f"{lecture.slug}-slides{suffix}"
    download(f"{RAW_BASE}/{lecture.source}", source_path)
    if lecture.source.endswith(".pdf"):
        slides_dir = directory / "slides-images"
        slides_dir.mkdir(exist_ok=True)
        run(
            [
                "pdftoppm",
                "-jpeg",
                "-r",
                "144",
                str(source_path),
                str(slides_dir / "slide"),
            ]
        )
        return

    source = source_path.read_text(encoding="utf-8")
    local_images = sorted(set(re.findall(r'["\'](images/[^"\']+)["\']', source)))
    for relative in local_images:
        download(f"{RAW_BASE}/{relative}", directory / "images" / Path(relative).name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lecture", type=int, action="append", help="Prepare only selected lecture numbers")
    parser.add_argument("--skip-video-assets", action="store_true")
    parser.add_argument("--skip-official-source", action="store_true")
    parser.add_argument("--reclean-only", action="store_true")
    args = parser.parse_args()

    selected = set(args.lecture or [lecture.number for lecture in LECTURES])
    manifest = []
    for lecture in LECTURES:
        manifest.append(asdict(lecture) | {"slug": lecture.slug, "url": lecture.url})
        if lecture.number not in selected:
            continue
        directory = COURSE_DIR / lecture.slug
        directory.mkdir(parents=True, exist_ok=True)
        if args.reclean_only:
            subtitle = directory / f"{lecture.slug}.en.srt"
            if not subtitle.exists():
                raise FileNotFoundError(subtitle)
            clean_srt(subtitle, directory / "transcript_timed.txt", directory / "transcript_clean.txt")
            print(f"refined {lecture.slug}: {lecture.topic}")
            continue
        if not args.skip_video_assets:
            prepare_video_assets(lecture, directory)
        if not args.skip_official_source:
            prepare_official_source(lecture, directory)
        print(f"prepared {lecture.slug}: {lecture.topic}")

    (COURSE_DIR / "course-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

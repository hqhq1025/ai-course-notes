#!/usr/bin/env python3
import argparse
import json
import time
from pathlib import Path

from faster_whisper import WhisperModel


def fmt_srt(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe audio/video with faster-whisper and write SRT/TXT/JSON.")
    parser.add_argument("input", help="Audio or video file")
    parser.add_argument("--out-prefix", required=True, help="Output prefix without extension")
    parser.add_argument("--model", default="large-v3")
    parser.add_argument("--language", default="zh")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--device-index", type=int, default=0)
    parser.add_argument("--compute-type", default="float16")
    parser.add_argument("--beam-size", type=int, default=5)
    parser.add_argument("--vad-filter", action="store_true", default=True)
    parser.add_argument("--no-vad-filter", dest="vad_filter", action="store_false")
    args = parser.parse_args()

    out_prefix = Path(args.out_prefix)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)
    srt_path = Path(f"{out_prefix}.srt")
    txt_path = Path(f"{out_prefix}.txt")
    json_path = Path(f"{out_prefix}.json")

    started = time.time()
    model = WhisperModel(
        args.model,
        device=args.device,
        device_index=args.device_index,
        compute_type=args.compute_type,
    )
    segments_iter, info = model.transcribe(
        args.input,
        language=args.language,
        task="transcribe",
        vad_filter=args.vad_filter,
        beam_size=args.beam_size,
        word_timestamps=False,
    )

    segments = []
    with srt_path.open("w") as srt, txt_path.open("w") as txt:
        for i, seg in enumerate(segments_iter, 1):
            text = seg.text.strip()
            segments.append({"start": seg.start, "end": seg.end, "text": text})
            srt.write(f"{i}\n{fmt_srt(seg.start)} --> {fmt_srt(seg.end)}\n{text}\n\n")
            txt.write(f"[{fmt_srt(seg.start)[:-4]}--{fmt_srt(seg.end)[:-4]}] {text}\n")
            if i % 100 == 0:
                elapsed = time.time() - started
                print(f"segments={i} elapsed={elapsed:.1f}s", flush=True)

    json_path.write_text(json.dumps({
        "language": info.language,
        "language_probability": info.language_probability,
        "duration": info.duration,
        "model": args.model,
        "device": args.device,
        "compute_type": args.compute_type,
        "segments": segments,
        "elapsed_seconds": time.time() - started,
    }, ensure_ascii=False, indent=2))
    print(f"done segments={len(segments)} elapsed={time.time() - started:.1f}s language={info.language}")


if __name__ == "__main__":
    main()

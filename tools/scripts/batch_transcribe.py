#!/usr/bin/env python3
"""
Batch Whisper transcription for downloaded audio files.
Supports multi-GPU parallel execution.

Usage:
    # Single GPU (default model: large-v3, needs ~10GB VRAM)
    python3 batch_transcribe.py /path/to/dirs/*/

    # Use a smaller model if GPU memory is limited
    WHISPER_MODEL=medium python3 batch_transcribe.py /path/to/dirs/*/

    # English courses
    WHISPER_LANG=en python3 batch_transcribe.py /path/to/dirs/*/

    # Multi-GPU (run multiple instances)
    CUDA_VISIBLE_DEVICES=0 python3 batch_transcribe.py dir1/ dir2/ dir3/ &
    CUDA_VISIBLE_DEVICES=1 python3 batch_transcribe.py dir4/ dir5/ dir6/ &
"""
import whisper, os, sys, glob

def transcribe_dir(model, d):
    name = os.path.basename(d.rstrip('/'))
    audio = None
    for ext in ['m4a', 'wav', 'mp4', 'webm']:
        candidates = glob.glob(f"{d}/audio.{ext}")
        if candidates:
            audio = candidates[0]
            break
    if not audio:
        print(f"SKIP {name}: no audio")
        return
    srt_path = os.path.join(d, f"{name}.srt")
    if os.path.exists(srt_path) and os.path.getsize(srt_path) > 100:
        print(f"SKIP {name}: SRT exists")
        return
    print(f"TRANSCRIBING {name}...")
    lang = os.environ.get("WHISPER_LANG", "zh")
    result = model.transcribe(audio, language=lang, verbose=False)
    segments = result.get("segments", [])
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            start, end = seg["start"], seg["end"]
            sh, sm, ss = int(start//3600), int((start%3600)//60), start%60
            eh, em, es = int(end//3600), int((end%3600)//60), end%60
            f.write(f"{i}\n{sh:02d}:{sm:02d}:{ss:06.3f} --> "
                    f"{eh:02d}:{em:02d}:{es:06.3f}\n{seg['text'].strip()}\n\n")
    print(f"DONE {name}: {len(segments)} segments")

if __name__ == "__main__":
    dirs = sys.argv[1:] if len(sys.argv) > 1 else sorted(glob.glob("*/"))
    model_name = os.environ.get("WHISPER_MODEL", "large-v3")
    device = "cuda" if os.environ.get("CUDA_VISIBLE_DEVICES") is not None or __import__('torch').cuda.is_available() else "cpu"
    print(f"Loading Whisper {model_name} on {device}...")
    model = whisper.load_model(model_name, device=device)
    print(f"Processing {len(dirs)} directories")
    for d in dirs:
        try:
            transcribe_dir(model, d)
        except Exception as e:
            print(f"ERROR {d}: {e}")
    print("=== All done ===")

#!/usr/bin/env python3
"""
Batch Whisper transcription for downloaded audio files.
Supports multi-GPU parallel execution.

Usage:
    # Single GPU
    python3.11 batch_transcribe.py /path/to/dirs/*/
    
    # Multi-GPU (run multiple instances)
    CUDA_VISIBLE_DEVICES=0 python3.11 batch_transcribe.py dir1/ dir2/ dir3/ &
    CUDA_VISIBLE_DEVICES=1 python3.11 batch_transcribe.py dir4/ dir5/ dir6/ &
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
    result = model.transcribe(audio, language="zh", verbose=False)
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
    print("Loading Whisper large-v3...")
    model = whisper.load_model("large-v3", device="cuda")
    print(f"Processing {len(dirs)} directories")
    for d in dirs:
        try:
            transcribe_dir(model, d)
        except Exception as e:
            print(f"ERROR {d}: {e}")
    print("=== All done ===")

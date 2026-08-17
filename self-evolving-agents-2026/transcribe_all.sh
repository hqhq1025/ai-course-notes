#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${FW_PYTHON:-/home/v-haoqiwang/dwbench/.venv/bin/python}"
MODEL="${WHISPER_MODEL:-mobiuslabsgmbh/faster-whisper-large-v3-turbo}"
CPU_THREADS="${WHISPER_CPU_THREADS:-48}"

if [[ ! -x "$PYTHON" ]]; then
  echo "Set FW_PYTHON to a Python environment containing faster-whisper." >&2
  exit 1
fi

for lecture in "$ROOT"/lecture??; do
  [[ -f "$lecture/audio.wav" ]] || continue
  [[ -f "$lecture/subs.json" ]] && continue
  echo "Transcribing $(basename "$lecture")"
  "$PYTHON" "$ROOT/../tools/scripts/transcribe_faster_whisper.py" \
    "$lecture/audio.wav" \
    --out-prefix "$lecture/subs" \
    --model "$MODEL" \
    --language zh \
    --device cpu \
    --compute-type int8 \
    --cpu-threads "$CPU_THREADS" \
    --beam-size 5
done

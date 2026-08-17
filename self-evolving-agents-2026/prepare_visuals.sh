#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for lecture in "$ROOT"/lecture??; do
  [[ -f "$lecture/video.mp4" ]] || continue
  mkdir -p "$lecture/frame-candidates" "$lecture/qa"
  if ! compgen -G "$lecture/frame-candidates/*.jpg" >/dev/null; then
    ffmpeg -hide_banner -loglevel error -i "$lecture/video.mp4" \
      -vf "fps=1/15,scale=1280:-2" -q:v 2 \
      "$lecture/frame-candidates/frame-%05d.jpg"
  fi
  lecture_name="$(basename "$lecture")"
  if [[ "$lecture_name" != "lecture05" && "$lecture_name" != "lecture09" && ! -f "$lecture/slide-selection.json" ]]; then
    python3 "$ROOT/select_slides.py" "$lecture"
  fi
  python3 "$ROOT/../tools/scripts/build_lecture_manifest.py" "$lecture"
  if [[ -f "$lecture/subs.json" && "$lecture_name" != "lecture05" && "$lecture_name" != "lecture09" ]]; then
    python3 "$ROOT/build_lecture_blueprint.py" "$lecture"
  elif [[ -f "$lecture/subs.json" ]]; then
    python3 "$ROOT/build_panel_ledger.py" "$lecture"
  fi
done

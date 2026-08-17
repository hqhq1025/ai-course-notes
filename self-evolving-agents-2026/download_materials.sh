#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BVID="BV1P4LX68EcS"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/136 Safari/537.36"
REFERER="https://www.bilibili.com/video/${BVID}"

fetch_json() {
  local url="$1"
  local output="$2"
  local referer="$3"
  local temporary="${output}.part"

  for attempt in {1..10}; do
    if curl -fsSL --retry 3 -A "$UA" -e "$referer" "$url" -o "$temporary" \
      && jq -e '.code == 0' "$temporary" >/dev/null 2>&1; then
      mv "$temporary" "$output"
      return 0
    fi
    sleep "$attempt"
  done
  echo "Unable to fetch valid JSON from $url" >&2
  return 1
}

fetch_json \
  "https://api.bilibili.com/x/web-interface/view?bvid=${BVID}" \
  "$ROOT/metadata.full.json" \
  "https://www.bilibili.com/"

if [[ ! -s "$ROOT/cover.jpg" ]]; then
  curl -fsSL --retry 3 -A "$UA" -e "$REFERER" \
    "$(jq -r '.cover_url' "$ROOT/metadata.json")" \
    -o "$ROOT/cover.jpg"
fi

jq -c '.parts[] | select(.lecture != null)' "$ROOT/metadata.json" | while read -r part; do
  page="$(jq -r '.page' <<<"$part")"
  cid="$(jq -r '.cid' <<<"$part")"
  lecture="$(jq -r '.lecture' <<<"$part")"
  target="$ROOT/$lecture"
  mkdir -p "$target/raw"

  if [[ -s "$target/video.mp4" && -s "$target/audio.wav" ]]; then
    echo "Skipping completed $lecture"
    continue
  fi

  playurl="$target/raw/playurl.json"
  fetch_json \
    "https://api.bilibili.com/x/player/playurl?bvid=${BVID}&cid=${cid}&qn=64&fnval=16" \
    "$playurl" \
    "$REFERER?p=$page"

  jq -e '.data.dash.video | length > 0' "$playurl" >/dev/null
  jq -e '.data.dash.audio | length > 0' "$playurl" >/dev/null

  video_url="$(jq -r '.data.dash.video | sort_by([.height, .bandwidth]) | last | .baseUrl' "$playurl")"
  audio_url="$(jq -r '.data.dash.audio | sort_by(.bandwidth) | last | .baseUrl' "$playurl")"

  curl -fsSL --retry 5 -A "$UA" -e "$REFERER?p=$page" "$video_url" -o "$target/raw/video.m4s.part"
  mv "$target/raw/video.m4s.part" "$target/raw/video.m4s"
  curl -fsSL --retry 5 -A "$UA" -e "$REFERER?p=$page" "$audio_url" -o "$target/raw/audio.m4s.part"
  mv "$target/raw/audio.m4s.part" "$target/raw/audio.m4s"
  ffmpeg -nostdin -y -loglevel error -i "$target/raw/video.m4s" -i "$target/raw/audio.m4s" \
    -c copy "$target/video.mp4"
  ffmpeg -nostdin -y -loglevel error -i "$target/raw/audio.m4s" -ac 1 -ar 16000 "$target/audio.wav"
done

echo "Downloaded nine teaching units under $ROOT"

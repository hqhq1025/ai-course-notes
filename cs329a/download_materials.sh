#!/usr/bin/env bash
set -euo pipefail

mode="${1:-metadata}"
root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

videos=(
  "01|6YnLB0XbTnI|course-overview"
  "02|-Ggc37xLj_Y|test-time-compute-scaling"
  "03|p7TdPUcPoik|robust-verification"
  "04|Lxh9RF5S-K0|learning-from-feedback-with-tools-code"
  "05|Ml_fp9XkB8Y|planning-and-multi-step-reasoning"
  "06|yVnmHSAy3ck|train-time-scaling-and-scaling-rl"
  "07|Uni9dqyuuDM|self-improvement-and-deep-research-agents"
  "08|8JAqLnTaZu4|agentic-evaluations-and-long-horizon-tasks"
  "09|AyO6wyu4DEg|future-research-areas"
)

download_metadata() {
  local index="$1"
  local video_id="$2"
  local lecture_dir="$root_dir/lecture${index}"
  local url="https://www.youtube.com/watch?v=${video_id}"
  local full_metadata="$lecture_dir/metadata.full.json"
  local public_metadata="$lecture_dir/metadata.json"

  mkdir -p "$lecture_dir"
  yt-dlp --no-warnings --dump-single-json --skip-download "$url" > "$full_metadata"

  local subtitle_lang
  subtitle_lang="$(jq -r '(.subtitles // {}) | keys | .[0] // empty' "$full_metadata")"
  if [[ -z "$subtitle_lang" ]]; then
    subtitle_lang="$(jq -r 'if (.automatic_captions // {} | has("en-orig")) then "en-orig" elif (.automatic_captions // {} | has("en")) then "en" else empty end' "$full_metadata")"
  fi

  jq '{
    schema_version: 1,
    id,
    title,
    description,
    duration,
    duration_string,
    upload_date,
    timestamp,
    release_timestamp,
    release_year,
    channel,
    channel_id,
    channel_url,
    channel_follower_count,
    uploader,
    uploader_id,
    uploader_url,
    webpage_url,
    original_url,
    playlist,
    playlist_index,
    thumbnail,
    tags,
    categories,
    chapters,
    view_count,
    like_count,
    comment_count,
    language,
    availability,
    age_limit,
    live_status,
    was_live,
    media_type,
    extractor,
    extractor_key
  } | with_entries(select(.value != null))' "$full_metadata" > "$public_metadata"

  yt-dlp --no-warnings --skip-download \
    --write-thumbnail --convert-thumbnails jpg \
    -o "$lecture_dir/source.%(ext)s" "$url"
  if [[ -f "$lecture_dir/source.jpg" ]]; then
    mv "$lecture_dir/source.jpg" "$lecture_dir/cover.jpg"
  fi

  if [[ -n "$subtitle_lang" ]]; then
    yt-dlp --no-warnings --skip-download \
      --write-subs --write-auto-subs --sub-langs "$subtitle_lang" \
      --sub-format vtt --convert-subs srt \
      -o "$lecture_dir/source.%(ext)s" "$url"
    local subtitle_file
    subtitle_file="$(find "$lecture_dir" -maxdepth 1 -type f -name 'source.*.srt' | head -n 1 || true)"
    if [[ -n "$subtitle_file" ]]; then
      mv "$subtitle_file" "$lecture_dir/lecture${index}.srt"
    fi
  fi
}

download_video() {
  local index="$1"
  local video_id="$2"
  local lecture_dir="$root_dir/lecture${index}"
  local url="https://www.youtube.com/watch?v=${video_id}"

  mkdir -p "$lecture_dir"
  yt-dlp --no-warnings \
    -f 'bv*[height<=1080]+ba/b[height<=1080]/best' \
    --merge-output-format mp4 \
    -o "$lecture_dir/lecture${index}.%(ext)s" "$url"
}

for entry in "${videos[@]}"; do
  IFS='|' read -r index video_id slug <<< "$entry"
  printf '== lecture%s: %s ==\n' "$index" "$slug"
  case "$mode" in
    metadata) download_metadata "$index" "$video_id" ;;
    video) download_video "$index" "$video_id" ;;
    all)
      download_metadata "$index" "$video_id"
      download_video "$index" "$video_id"
      ;;
    *)
      printf 'Usage: %s [metadata|video|all]\n' "$0" >&2
      exit 2
      ;;
  esac
done

#!/bin/bash
# Batch download audio + covers from Bilibili
# Usage: ./batch_download.sh <cookies_file> <output_dir> <BV1> <BV2> ...
#
# Example:
#   ./batch_download.sh bilibili_cookies.txt modern-agent/lecture01 BV1wjY5zyEki

COOKIES=$1
DIR=$2
shift 2

for bv in "$@"; do
    url="https://www.bilibili.com/video/${bv}"
    echo "=== Downloading ${bv} to ${DIR} ==="
    mkdir -p "$DIR"
    
    # Cover
    thumb=$(yt-dlp --cookies "$COOKIES" --dump-json "$url" 2>/dev/null | \
        python3 -c "import sys,json; print(json.load(sys.stdin).get('thumbnail',''))" 2>/dev/null)
    [ -n "$thumb" ] && curl -sL "$thumb" -o "$DIR/cover.jpg"
    
    # Audio
    yt-dlp --cookies "$COOKIES" -x -o "$DIR/audio.%(ext)s" "$url" 2>/dev/null
done
echo "=== Done ==="

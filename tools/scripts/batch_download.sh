#!/bin/bash
# Batch download audio + covers from YouTube or Bilibili
#
# Usage:
#   # YouTube (no cookies needed)
#   ./batch_download.sh lecture01 https://youtube.com/watch?v=xxx
#   ./batch_download.sh lecture01 https://youtube.com/watch?v=xxx lecture02 https://youtube.com/watch?v=yyy
#
#   # Bilibili (cookies required for full audio)
#   ./batch_download.sh --cookies bilibili_cookies.txt lecture01 https://bilibili.com/video/BV1xxx
#
# Each pair of arguments is: <output_dir> <url>

COOKIES=""
if [ "$1" = "--cookies" ]; then
    COOKIES="--cookies $2"
    shift 2
fi

if [ $(($# % 2)) -ne 0 ]; then
    echo "Error: arguments must be pairs of <output_dir> <url>"
    echo "Usage: $0 [--cookies file] dir1 url1 dir2 url2 ..."
    exit 1
fi

while [ $# -ge 2 ]; do
    DIR=$1
    URL=$2
    shift 2

    echo "=== Downloading to ${DIR} ==="
    mkdir -p "$DIR"

    # Cover
    thumb=$(yt-dlp $COOKIES --dump-json "$URL" 2>/dev/null | \
        python3 -c "import sys,json; print(json.load(sys.stdin).get('thumbnail',''))" 2>/dev/null)
    [ -n "$thumb" ] && curl -sL "$thumb" -o "$DIR/cover.jpg"

    # Audio
    yt-dlp $COOKIES -x -o "$DIR/audio.%(ext)s" "$URL" 2>/dev/null

    echo "  Done: $DIR"
done
echo "=== All done ==="

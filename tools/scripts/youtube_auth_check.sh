#!/usr/bin/env bash
set -euo pipefail

URL="${1:-https://www.youtube.com/watch?v=ttkd0t5qTD4}"
COOKIES_FILE="${YOUTUBE_COOKIES_FILE:-youtube_cookies.txt}"
BGUTIL_IMAGE="${BGUTIL_IMAGE:-brainicism/bgutil-ytdlp-pot-provider:1.3.1}"
BGUTIL_NAME="${BGUTIL_NAME:-bgutil-provider}"

if ! command -v yt-dlp >/dev/null 2>&1; then
  echo "ERROR: yt-dlp is not installed or not on PATH." >&2
  exit 2
fi

if ! python3 - <<'PY' >/dev/null 2>&1
import curl_cffi
ver = tuple(int(x) for x in curl_cffi.__version__.split('.')[:2])
raise SystemExit(0 if (ver == (0, 5) or (0, 10) <= ver < (0, 15)) else 1)
PY
then
  echo "ERROR: yt-dlp requires curl_cffi 0.5.10 or 0.10.x through 0.14.x for impersonation." >&2
  echo "Fix: python3 -m pip install 'curl_cffi>=0.14,<0.15' --force-reinstall" >&2
  exit 2
fi

if ! python3 - <<'PY' >/dev/null 2>&1
import importlib.util
raise SystemExit(0 if importlib.util.find_spec('yt_dlp_plugins.extractor.getpot_bgutil') else 1)
PY
then
  echo "ERROR: bgutil-ytdlp-pot-provider plugin is not installed." >&2
  echo "Fix: python3 -m pip install -U bgutil-ytdlp-pot-provider" >&2
  exit 2
fi

if command -v docker >/dev/null 2>&1; then
  if ! python3 - <<'PY' >/dev/null 2>&1
import urllib.request
urllib.request.urlopen('http://127.0.0.1:4416/ping', timeout=2).read()
PY
  then
    docker rm -f "$BGUTIL_NAME" >/dev/null 2>&1 || true
    docker run --name "$BGUTIL_NAME" -d -p 4416:4416 --init "$BGUTIL_IMAGE" >/dev/null
    sleep 1
  fi
fi

if [ ! -s "$COOKIES_FILE" ]; then
  cat >&2 <<EOF
ERROR: $COOKIES_FILE not found.

YouTube is requiring real account cookies for this host. Export Netscape-format
cookies from a browser where YouTube is logged in, save them as:

  $(pwd)/$COOKIES_FILE

Then re-run:

  YOUTUBE_COOKIES_FILE=$COOKIES_FILE $0 "$URL"

The file is ignored by git. Do not commit it.
EOF
  exit 3
fi

yt-dlp \
  --cookies "$COOKIES_FILE" \
  --impersonate chrome \
  --remote-components ejs:github \
  --extractor-args 'youtube:player_client=mweb;formats=missing_pot' \
  --list-formats \
  "$URL"

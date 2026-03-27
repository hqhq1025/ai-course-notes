#!/bin/bash
# Batch download subtitles and covers for all lectures
set -e

download_lecture() {
    local course="$1"
    local num="$2"
    local url="$3"
    local dir="/home/v-haoqiwang/ai-course-notes/${course}/lecture${num}"

    echo "[${course}/lecture${num}] Downloading subtitles and cover..."

    # Download cover
    if [ ! -f "${dir}/cover.jpg" ]; then
        yt-dlp --write-thumbnail --skip-download --convert-thumbnails jpg \
            -o "${dir}/cover" "$url" 2>/dev/null || true
        # yt-dlp may save as cover.jpg or cover.webp.jpg etc
        for f in "${dir}"/cover.*; do
            if [ -f "$f" ] && [ "$f" != "${dir}/cover.jpg" ]; then
                mv "$f" "${dir}/cover.jpg" 2>/dev/null || true
            fi
        done
    fi

    # Download subtitles
    if [ ! -f "${dir}/"*.srt ] 2>/dev/null; then
        # Try manual English subtitles first, then auto-generated
        yt-dlp --write-sub --write-auto-sub --sub-lang en --sub-format srt \
            --skip-download --convert-subs srt \
            -o "${dir}/lecture${num}" "$url" 2>/dev/null || true
    fi

    echo "[${course}/lecture${num}] Done"
}

# ============ CS336 ============
download_lecture cs336 01 "https://www.youtube.com/watch?v=SQ3fZ1sAqXI" &
download_lecture cs336 02 "https://www.youtube.com/watch?v=msHyYioAyNE" &
download_lecture cs336 03 "https://www.youtube.com/watch?v=ptFiH_bHnJw" &
download_lecture cs336 04 "https://www.youtube.com/watch?v=LPv1KfUXLCo" &
download_lecture cs336 06 "https://www.youtube.com/watch?v=E8Mju53VB00" &
download_lecture cs336 07 "https://www.youtube.com/watch?v=l1RJcDjzK8M" &
download_lecture cs336 08 "https://www.youtube.com/watch?v=LHpr5ytssLo" &
download_lecture cs336 09 "https://www.youtube.com/watch?v=6Q-ESEmDf4Q" &
download_lecture cs336 10 "https://www.youtube.com/watch?v=fcgPYo3OtV0" &
download_lecture cs336 11 "https://www.youtube.com/watch?v=OSYuUqGBQxw" &
download_lecture cs336 12 "https://www.youtube.com/watch?v=x-R5l2HsXqM" &
download_lecture cs336 13 "https://www.youtube.com/watch?v=WePxmeXU1xg" &
download_lecture cs336 14 "https://www.youtube.com/watch?v=9Cd0THLS1t0" &
download_lecture cs336 15 "https://www.youtube.com/watch?v=Dfu7vC9jo4w" &
download_lecture cs336 16 "https://www.youtube.com/watch?v=46f2QTDB08Q" &
download_lecture cs336 17 "https://www.youtube.com/watch?v=JdGFdViaOJk" &

wait
echo "=== CS336 subtitles done ==="

# ============ CS224N ============
download_lecture cs224n 01 "https://www.youtube.com/watch?v=DzpHeXVSC5I" &
download_lecture cs224n 02 "https://www.youtube.com/watch?v=nBor4jfWetQ" &
download_lecture cs224n 03 "https://www.youtube.com/watch?v=HnliVHU2g9U" &
download_lecture cs224n 04 "https://www.youtube.com/watch?v=KVKvde-_MYc" &
download_lecture cs224n 05 "https://www.youtube.com/watch?v=fyc0Jzr74y4" &
download_lecture cs224n 06 "https://www.youtube.com/watch?v=Ba6Fn1-Jsfw" &
download_lecture cs224n 07 "https://www.youtube.com/watch?v=J7ruSOIzhrE" &
download_lecture cs224n 08 "https://www.youtube.com/watch?v=LWMzyfvuehA" &
download_lecture cs224n 09 "https://www.youtube.com/watch?v=DGfCRXuNA2w" &
download_lecture cs224n 10 "https://www.youtube.com/watch?v=35X6zlhoCy4" &
download_lecture cs224n 11 "https://www.youtube.com/watch?v=TO0CqzqiArM" &
download_lecture cs224n 12 "https://www.youtube.com/watch?v=UVX7SYGCKkA" &
download_lecture cs224n 13 "https://www.youtube.com/watch?v=tfVgHsKpRC8" &
download_lecture cs224n 14 "https://www.youtube.com/watch?v=I0tj4Y7xaOQ" &
download_lecture cs224n 15 "https://www.youtube.com/watch?v=dnF463_Ar9I" &
download_lecture cs224n 16 "https://www.youtube.com/watch?v=S8d-7v3f5MQ" &
download_lecture cs224n 18 "https://www.youtube.com/watch?v=NxH0Y78xcF4" &

wait
echo "=== CS224N subtitles done ==="

# ============ CS231N ============
download_lecture cs231n 01 "https://www.youtube.com/watch?v=2fq9wYslV0A" &
download_lecture cs231n 02 "https://www.youtube.com/watch?v=pdqofxJeBN8" &
download_lecture cs231n 03 "https://www.youtube.com/watch?v=dyNGd06MWn4" &
download_lecture cs231n 04 "https://www.youtube.com/watch?v=25zD5qJHYsk" &
download_lecture cs231n 05 "https://www.youtube.com/watch?v=f3g1zGdxptI" &
download_lecture cs231n 06 "https://www.youtube.com/watch?v=aVJy4O5TOk8" &
download_lecture cs231n 07 "https://www.youtube.com/watch?v=kG2lAPBF7zA" &
download_lecture cs231n 08 "https://www.youtube.com/watch?v=RQowiOF_FvQ" &
download_lecture cs231n 09 "https://www.youtube.com/watch?v=PTypu6GqEd4" &
download_lecture cs231n 10 "https://www.youtube.com/watch?v=wElqklprhPE" &
download_lecture cs231n 11 "https://www.youtube.com/watch?v=9MvD-XsowsE" &
download_lecture cs231n 12 "https://www.youtube.com/watch?v=4howBU7THbM" &
download_lecture cs231n 13 "https://www.youtube.com/watch?v=zbHXQRUNlH0" &
download_lecture cs231n 14 "https://www.youtube.com/watch?v=Edr4uZFh4EE" &
download_lecture cs231n 15 "https://www.youtube.com/watch?v=7lxrKDKtykM" &
download_lecture cs231n 16 "https://www.youtube.com/watch?v=mQOK0Mfyrkk" &
download_lecture cs231n 17 "https://www.youtube.com/watch?v=XSfmOH_xVSU" &
download_lecture cs231n 18 "https://www.youtube.com/watch?v=g8UaBfj6Sh8" &

wait
echo "=== CS231N subtitles done ==="
echo "=== ALL DOWNLOADS COMPLETE ==="

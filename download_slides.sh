#!/bin/bash
# Download slides for all courses
set -e
BASE="/home/v-haoqiwang/ai-course-notes"

download_slides() {
    local dir="$1"
    local url="$2"
    local filename="$3"
    if [ ! -f "${dir}/${filename}" ]; then
        echo "Downloading ${dir}/${filename}..."
        curl -sL -o "${dir}/${filename}" "$url" || echo "FAILED: ${url}"
    fi
}

extract_slides() {
    local dir="$1"
    local pdf="$2"
    if [ -f "${dir}/${pdf}" ] && [ ! -f "${dir}/slides-images/slide-000.jpg" ]; then
        echo "Extracting ${dir}/${pdf}..."
        convert -density 200 "${dir}/${pdf}" "${dir}/slides-images/slide-%03d.jpg" 2>/dev/null || true
    fi
}

# ============ CS336 slides (from GitHub) ============
CS336_SLIDES_BASE="https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/nonexecutable"

# Tatsu's PDF slides
download_slides "${BASE}/cs336/lecture03" "${CS336_SLIDES_BASE}/2025%20Lecture%203%20-%20architecture.pdf" "lecture03-slides.pdf" &
download_slides "${BASE}/cs336/lecture04" "${CS336_SLIDES_BASE}/2025%20Lecture%204%20-%20MoEs.pdf" "lecture04-slides.pdf" &
download_slides "${BASE}/cs336/lecture07" "${CS336_SLIDES_BASE}/2025%20Lecture%207%20-%20Parallelism%20basics.pdf" "lecture07-slides.pdf" &
download_slides "${BASE}/cs336/lecture09" "${CS336_SLIDES_BASE}/2025%20Lecture%209%20-%20Scaling%20laws%20basics.pdf" "lecture09-slides.pdf" &
download_slides "${BASE}/cs336/lecture11" "${CS336_SLIDES_BASE}/2025%20Lecture%2011%20-%20Scaling%20details.pdf" "lecture11-slides.pdf" &
download_slides "${BASE}/cs336/lecture15" "${CS336_SLIDES_BASE}/2025%20Lecture%2015%20-%20RLHF%20Alignment.pdf" "lecture15-slides.pdf" &
download_slides "${BASE}/cs336/lecture16" "${CS336_SLIDES_BASE}/2025%20Lecture%2016%20-%20RLVR.pdf" "lecture16-slides.pdf" &

# Percy's .py slides
PY_BASE="https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main"
download_slides "${BASE}/cs336/lecture01" "${PY_BASE}/lecture_01.py" "lecture01-slides.py" &
download_slides "${BASE}/cs336/lecture02" "${PY_BASE}/lecture_02.py" "lecture02-slides.py" &
download_slides "${BASE}/cs336/lecture06" "${PY_BASE}/lecture_06.py" "lecture06-slides.py" &
download_slides "${BASE}/cs336/lecture08" "${PY_BASE}/lecture_08.py" "lecture08-slides.py" &
download_slides "${BASE}/cs336/lecture10" "${PY_BASE}/lecture_10.py" "lecture10-slides.py" &
download_slides "${BASE}/cs336/lecture12" "${PY_BASE}/lecture_12.py" "lecture12-slides.py" &
download_slides "${BASE}/cs336/lecture13" "${PY_BASE}/lecture_13.py" "lecture13-slides.py" &
download_slides "${BASE}/cs336/lecture14" "${PY_BASE}/lecture_14.py" "lecture14-slides.py" &
download_slides "${BASE}/cs336/lecture17" "${PY_BASE}/lecture_17.py" "lecture17-slides.py" &

wait
echo "=== CS336 slides downloaded ==="

# ============ CS224N slides ============
CS224N_BASE="https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides"

download_slides "${BASE}/cs224n/lecture01" "${CS224N_BASE}/cs224n-spr2024-lecture01-wordvecs1.pdf" "lecture01-slides.pdf" &
download_slides "${BASE}/cs224n/lecture02" "${CS224N_BASE}/cs224n-spr2024-lecture02-wordvecs2.pdf" "lecture02-slides.pdf" &
download_slides "${BASE}/cs224n/lecture03" "${CS224N_BASE}/cs224n-spr2024-lecture03-neuralnets.pdf" "lecture03-slides.pdf" &
download_slides "${BASE}/cs224n/lecture04" "${CS224N_BASE}/cs224n-spr2024-lecture04-dep-parsing.pdf" "lecture04-slides.pdf" &
download_slides "${BASE}/cs224n/lecture05" "${CS224N_BASE}/cs224n-spr2024-lecture05-rnnlm.pdf" "lecture05-slides.pdf" &
download_slides "${BASE}/cs224n/lecture06" "${CS224N_BASE}/cs224n-spr2024-lecture06-fancy-rnn.pdf" "lecture06-slides.pdf" &
download_slides "${BASE}/cs224n/lecture07" "${CS224N_BASE}/cs224n-spr2024-lecture07-final-project.pdf" "lecture07-slides.pdf" &
download_slides "${BASE}/cs224n/lecture08" "${CS224N_BASE}/cs224n-spr2024-lecture08-transformers.pdf" "lecture08-slides.pdf" &
download_slides "${BASE}/cs224n/lecture09" "${CS224N_BASE}/cs224n-spr2024-lecture09-pretraining-updated.pdf" "lecture09-slides.pdf" &
download_slides "${BASE}/cs224n/lecture10" "${CS224N_BASE}/cs224n-spr2024-lecture10-prompting-rlhf.pdf" "lecture10-slides.pdf" &
download_slides "${BASE}/cs224n/lecture11" "${CS224N_BASE}/cs224n-spr2024-lecture11-evaluation-yann.pdf" "lecture11-slides.pdf" &
download_slides "${BASE}/cs224n/lecture12" "${CS224N_BASE}/cs224n-spr2024-lecture12-training-shikhar.pdf" "lecture12-slides.pdf" &
download_slides "${BASE}/cs224n/lecture13" "${CS224N_BASE}/cs224n-spr2024-lecture13-speech-bci.pdf" "lecture13-slides.pdf" &
download_slides "${BASE}/cs224n/lecture14" "${CS224N_BASE}/cs224n-spr2024-lecture14-agents-shikhar-updated.pdf" "lecture14-slides.pdf" &
download_slides "${BASE}/cs224n/lecture15" "${CS224N_BASE}/cs224n-spr2024-lecture15-life-after-dpo-lambert.pdf" "lecture15-slides.pdf" &
download_slides "${BASE}/cs224n/lecture16" "${CS224N_BASE}/cs224n-spr2024-lecture16-CNN-TreeRNN.pdf" "lecture16-slides.pdf" &
download_slides "${BASE}/cs224n/lecture18" "${CS224N_BASE}/cs224n-spr2024-lecture18-nlp-linguistics-philosophy.pdf" "lecture18-slides.pdf" &

wait
echo "=== CS224N slides downloaded ==="

# ============ CS231N slides ============
CS231N_BASE="https://cs231n.stanford.edu/slides/2025"

download_slides "${BASE}/cs231n/lecture01" "${CS231N_BASE}/lecture_1_part_1.pdf" "lecture01-slides-part1.pdf" &
download_slides "${BASE}/cs231n/lecture01" "${CS231N_BASE}/lecture_1_part_2.pdf" "lecture01-slides-part2.pdf" &
download_slides "${BASE}/cs231n/lecture02" "${CS231N_BASE}/lecture_2.pdf" "lecture02-slides.pdf" &
download_slides "${BASE}/cs231n/lecture03" "${CS231N_BASE}/lecture_3.pdf" "lecture03-slides.pdf" &
download_slides "${BASE}/cs231n/lecture04" "${CS231N_BASE}/lecture_4.pdf" "lecture04-slides.pdf" &
download_slides "${BASE}/cs231n/lecture05" "${CS231N_BASE}/lecture_5.pdf" "lecture05-slides.pdf" &
download_slides "${BASE}/cs231n/lecture06" "${CS231N_BASE}/lecture_6.pdf" "lecture06-slides.pdf" &
download_slides "${BASE}/cs231n/lecture07" "${CS231N_BASE}/lecture_7.pdf" "lecture07-slides.pdf" &
download_slides "${BASE}/cs231n/lecture08" "${CS231N_BASE}/lecture_8.pdf" "lecture08-slides.pdf" &
download_slides "${BASE}/cs231n/lecture09" "${CS231N_BASE}/lecture_9.pdf" "lecture09-slides.pdf" &
download_slides "${BASE}/cs231n/lecture10" "${CS231N_BASE}/lecture_10.pdf" "lecture10-slides.pdf" &
download_slides "${BASE}/cs231n/lecture11" "${CS231N_BASE}/lecture_11.pdf" "lecture11-slides.pdf" &
download_slides "${BASE}/cs231n/lecture12" "${CS231N_BASE}/lecture_12.pdf" "lecture12-slides.pdf" &
download_slides "${BASE}/cs231n/lecture13" "${CS231N_BASE}/lecture_13.pdf" "lecture13-slides.pdf" &
download_slides "${BASE}/cs231n/lecture14" "${CS231N_BASE}/lecture_14.pdf" "lecture14-slides.pdf" &
download_slides "${BASE}/cs231n/lecture15" "${CS231N_BASE}/lecture_15.pdf" "lecture15-slides.pdf" &
download_slides "${BASE}/cs231n/lecture16" "${CS231N_BASE}/lecture_16.pdf" "lecture16-slides.pdf" &
download_slides "${BASE}/cs231n/lecture17" "${CS231N_BASE}/lecture_17.pdf" "lecture17-slides.pdf" &
# Lecture 18 slides not yet posted

wait
echo "=== CS231N slides downloaded ==="

# ============ Extract slide images from PDFs ============
echo "=== Extracting slide images ==="

for pdf in $(find "${BASE}" -name "*-slides.pdf" -o -name "*-slides-part*.pdf" | sort); do
    dir=$(dirname "$pdf")
    extract_slides "$dir" "$(basename "$pdf")" &
done

wait
echo "=== ALL SLIDES PROCESSING COMPLETE ==="

#!/bin/bash
# Quality check for lecture notes
# Usage: bash check_quality.sh <tex-file-or-directory>
#
# Examples:
#   bash check_quality.sh cs336/lecture05/lecture05-notes.tex
#   bash check_quality.sh cs336/          # check all in a series
#   bash check_quality.sh .               # check everything

set -euo pipefail

pdf_pages() {
    local pdf="$1"
    local pages=""

    [ -f "$pdf" ] || {
        echo 0
        return
    }

    if command -v pdfinfo >/dev/null 2>&1; then
        pages=$(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages:/ {print $2; exit}' || true)
        if [[ "$pages" =~ ^[0-9]+$ ]]; then
            echo "$pages"
            return
        fi
    fi

    if command -v mutool >/dev/null 2>&1; then
        pages=$(mutool show "$pdf" trailer/Root/Pages/Count 2>/dev/null | awk '/^[0-9]+$/ {print $1; exit}' || true)
        if [[ "$pages" =~ ^[0-9]+$ ]]; then
            echo "$pages"
            return
        fi

        pages=$(mutool info "$pdf" 2>/dev/null | awk '/^Pages:/ {print $2; exit}' || true)
        if [[ "$pages" =~ ^[0-9]+$ ]]; then
            echo "$pages"
            return
        fi
    fi

    echo 0
}

check_one() {
    local f="$1"
    local pdf="${f%.tex}.pdf"
    local name=$(echo "$f" | sed 's|^\./||')

    local pages=0 secs=0 subs=0 boxes=0 figs=0 summary=0
    local readfig=0 prose_chars=0 prose_per_fig=0
    pages=$(pdf_pages "$pdf")
    secs=$(grep -c '\\section{' "$f" 2>/dev/null || true)
    subs=$(grep -c '\\subsection{' "$f" 2>/dev/null || true)
    boxes=$(grep -Ec '\\begin\{importantbox\}|\\begin\{knowledgebox\}|\\begin\{warningbox\}' "$f" 2>/dev/null || true)
    figs=$(grep -c '\\includegraphics' "$f" 2>/dev/null || true)
    summary=$(grep -c '本章小结\|总结与延伸' "$f" 2>/dev/null || true)
    readfig=$(grep -c '读图' "$f" 2>/dev/null || true)
    prose_chars=$(python3 - "$f" <<'PY'
from pathlib import Path
import re, sys
text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="ignore")
chars = 0
for raw in text.splitlines():
    line = raw.strip()
    if not line or line.startswith("%"):
        continue
    if "\\includegraphics" in line or "\\caption" in line or "\\figsource" in line:
        continue
    if any(cmd in line for cmd in ["\\toprule", "\\midrule", "\\bottomrule", "\\endhead"]):
        continue
    if "&" in line and "\\\\" in line:
        continue
    line = re.sub(r"%.*$", "", line)
    line = re.sub(r"\\(?:section|subsection|caption|figsource|label)\*?(?:\[[^\]]*\])?\{[^}]*\}", " ", line)
    line = re.sub(r"\\(?:begin|end)\{[^}]*\}", " ", line)
    line = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", line)
    line = re.sub(r"[{}$^_]", " ", line)
    chars += len(re.findall(r"[\u4e00-\u9fffA-Za-z0-9]", line))
print(chars)
PY
)
    if [ "$figs" -gt 0 ]; then
        prose_per_fig=$((prose_chars / figs))
    fi

    local issues=""
    [ "$pages" -lt 8 ] && issues="${issues} pages<8"
    [ "$boxes" -lt 5 ] && issues="${issues} boxes<5"
    [ "$figs" -lt 3 ] && issues="${issues} figs<3"
    [ "$summary" -lt 2 ] && issues="${issues} no-summary"
    [ "$figs" -ge 12 ] && [ "$prose_per_fig" -lt 260 ] && issues="${issues} prose/fig<260"

    local grade="⭐⭐⭐"
    [ -n "$issues" ] && grade="⭐"
    [ "$pages" -ge 8 ] && [ "$boxes" -ge 5 ] && [ "$figs" -ge 3 ] && [ "$summary" -ge 2 ] && grade="⭐⭐"
    [ "$pages" -ge 20 ] && [ "$boxes" -ge 10 ] && [ "$figs" -ge 8 ] && { [ "$figs" -lt 12 ] || [ "$prose_per_fig" -ge 260 ]; } && grade="⭐⭐⭐"

    # Long-form podcast/interview notes often have no slides or demos. In that
    # case, do not require repeated speaker frames just to satisfy a figure
    # quota; 5+ substantive figures/diagrams plus read-the-figure treatment is
    # enough for ⭐⭐⭐.
    if [[ "$f" == youtube/* || "$f" == modern-agent/* || "$f" == agentic-rl/* || "$f" == llm-architect/* || "$f" == *"/youtube/"* || "$f" == *"/modern-agent/"* || "$f" == *"/agentic-rl/"* || "$f" == *"/llm-architect/"* ]]; then
        [ "$pages" -ge 20 ] && [ "$boxes" -ge 10 ] && [ "$figs" -ge 5 ] && [ "$readfig" -ge 3 ] && grade="⭐⭐⭐"
    fi

    if [ -n "${VERBOSE:-}" ] || [ -n "$issues" ]; then
        printf "%-55s %3dp %2ds %2db %2df %4dc/f  %s %s\n" "$name" "$pages" "$secs" "$boxes" "$figs" "$prose_per_fig" "$grade" "$issues"
    else
        printf "%-55s %3dp %2ds %2db %2df %4dc/f  %s\n" "$name" "$pages" "$secs" "$boxes" "$figs" "$prose_per_fig" "$grade"
    fi
}

target="${1:-.}"

if [ -f "$target" ]; then
    echo "=== Quality Check ==="
    echo ""
    check_one "$target"
else
    files=$(
        find "$target" \( -name '*-notes.tex' -o -name 'notes.tex' \) \
            -not -path '*/templates/*' \
            -not -path '*/.web-build/*' \
            -not -path '*/site/*' \
            -not -path './.web-build/*' \
            -not -path './site/*' \
            | sort
    )
    total=$(echo "$files" | wc -l)
    star3=0; star2=0; star1=0

    echo "=== Quality Report: $target ($total files) ==="
    echo "File                                                    Pages Secs Boxes Figs Prose/Fig Grade"
    echo "---------------------------------------------------------------------------------------------------------------"

    while IFS= read -r f; do
        check_one "$f"
    done <<< "$files"

    echo ""
    echo "Legend: p=pages s=sections b=boxes f=figures c/f=prose characters per figure"
    echo "⭐⭐⭐=优秀 ⭐⭐=达标 ⭐=需改进"
fi

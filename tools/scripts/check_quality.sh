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
    pages=$(pdf_pages "$pdf")
    secs=$(grep -c '\\section{' "$f" 2>/dev/null || true)
    subs=$(grep -c '\\subsection{' "$f" 2>/dev/null || true)
    boxes=$(grep -Ec '\\begin\{importantbox\}|\\begin\{knowledgebox\}|\\begin\{warningbox\}' "$f" 2>/dev/null || true)
    figs=$(grep -c '\\includegraphics' "$f" 2>/dev/null || true)
    summary=$(grep -c '本章小结\|总结与延伸' "$f" 2>/dev/null || true)

    local issues=""
    [ "$pages" -lt 8 ] && issues="${issues} pages<8"
    [ "$boxes" -lt 5 ] && issues="${issues} boxes<5"
    [ "$figs" -lt 3 ] && issues="${issues} figs<3"
    [ "$summary" -lt 2 ] && issues="${issues} no-summary"

    local grade="⭐⭐⭐"
    [ -n "$issues" ] && grade="⭐"
    [ "$pages" -ge 8 ] && [ "$boxes" -ge 5 ] && [ "$figs" -ge 3 ] && [ "$summary" -ge 2 ] && grade="⭐⭐"
    [ "$pages" -ge 20 ] && [ "$boxes" -ge 10 ] && [ "$figs" -ge 8 ] && grade="⭐⭐⭐"

    if [ -n "${VERBOSE:-}" ] || [ -n "$issues" ]; then
        printf "%-55s %3dp %2ds %2db %2df  %s %s\n" "$name" "$pages" "$secs" "$boxes" "$figs" "$grade" "$issues"
    else
        printf "%-55s %3dp  %s\n" "$name" "$pages" "$grade"
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
    echo "File                                                    Pages Secs Boxes Figs Grade"
    echo "---------------------------------------------------------------------------------------------------------------"

    while IFS= read -r f; do
        check_one "$f"
    done <<< "$files"

    echo ""
    echo "Legend: p=pages s=sections b=boxes f=figures"
    echo "⭐⭐⭐=优秀 ⭐⭐=达标 ⭐=需改进"
fi

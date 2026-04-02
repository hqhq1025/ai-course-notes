#!/bin/bash
# Setup script: install skills into Claude Code
# Run this after cloning the repo

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"

echo "Installing AI Course Notes skills into Claude Code..."

for skill_dir in "$SCRIPT_DIR/skills"/*/; do
    skill_name=$(basename "$skill_dir")
    target="$SKILLS_DIR/$skill_name"
    
    if [ -d "$target" ]; then
        echo "  ⚠️  $skill_name already exists, skipping (backup manually if needed)"
    else
        mkdir -p "$target"
        cp -r "$skill_dir"* "$target/"
        # Copy shared template into skill assets
        mkdir -p "$target/assets"
        cp "$SCRIPT_DIR/templates/notes-template.tex" "$target/assets/"
        echo "  ✅ Installed $skill_name"
    fi
done

echo ""
echo "Done! Skills installed to $SKILLS_DIR"
echo ""
echo "Dependencies you'll need:"
echo "  pip install openai-whisper yt-dlp"
echo "  # XeLaTeX: apt install texlive-xetex texlive-lang-chinese"
echo "  # ffmpeg: apt install ffmpeg (or download static binary)"

#!/usr/bin/env python3
"""
Batch-patch all .tex files to add repo footer and standardize author line.

Changes:
1. Add \repourl command (if missing)
2. Add fancyhdr page footer with "AI Course Notes" (if missing)
3. Add "项目主页" line in cover info box (if missing)
4. Standardize \noteauthors — remove "五道口纳什 & Codex/AI/Claude", keep descriptive ones
"""
import glob, re, sys, os

REPO_URL = "https://github.com/hqhq1025/ai-course-notes"

# Patterns to replace in noteauthors
AUTHOR_REPLACEMENTS = {
    r"五道口纳什 \\& Codex": "基于公开课程资料整理",
    r"五道口纳什 \\& AI": "基于公开课程资料整理",
    r"五道口纳什 \\& Claude": "基于公开课程资料整理",
    r"五道口纳什": "基于公开课程资料整理",
    r"青稞社区 \\& AI": "基于公开课程资料整理",
    r"张小珺商业访谈录 \\& AI": "基于公开课程资料整理",
}

FANCYHDR_BLOCK = r"""
% Footer with repo info
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\fancyfoot[R]{\footnotesize\color{gray}\href{\repourl}{AI Course Notes}}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
"""

def patch_file(path, dry_run=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Standardize noteauthors
    for pattern, replacement in AUTHOR_REPLACEMENTS.items():
        old = f"\\newcommand{{\\noteauthors}}{{{pattern}}}"
        new = f"\\newcommand{{\\noteauthors}}{{{replacement}}}"
        if old in content:
            content = content.replace(old, new)
            changes.append(f"  author: {pattern} → {replacement}")

    # 2. Add \repourl if missing
    if '\\repourl' not in content:
        # Insert after \videocoverpath line
        match = re.search(r'(\\newcommand\{\\videocoverpath\}\{[^}]*\})', content)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + f"\n\\newcommand{{\\repourl}}{{{REPO_URL}}}" + content[insert_pos:]
            changes.append("  added \\repourl")

    # 3. Add fancyhdr if missing
    if '\\usepackage{fancyhdr}' not in content:
        # Insert before \begin{document}
        match = re.search(r'\\begin\{document\}', content)
        if match:
            content = content[:match.start()] + FANCYHDR_BLOCK + "\n" + content[match.start():]
            changes.append("  added fancyhdr footer")

    # 4. Add 项目主页 in info box if missing
    if '项目主页' not in content:
        # Try specific pattern first: \href{\videourl}{\nolinkurl{\videourl}} ... }
        match = re.search(r'(\\href\{\\videourl\}\{\\nolinkurl\{\\videourl\}\}\s*\n\})', content)
        if match:
            insert_after = match.end()
            repo_line = "\n\\par\n\\textbf{项目主页}：\\href{\\repourl}{\\nolinkurl{\\repourl}}"
            content = content[:insert_after] + repo_line + content[insert_after:]
            changes.append("  added 项目主页 in info box")
        else:
            # Fallback: insert before the first \end{tcolorbox} in titlepage
            tp_match = re.search(r'\\begin\{titlepage\}', content)
            if tp_match:
                # Find first \end{tcolorbox} after \begin{titlepage}
                tc_match = re.search(r'\\end\{tcolorbox\}', content[tp_match.start():])
                if tc_match:
                    abs_pos = tp_match.start() + tc_match.start()
                    repo_line = "\\textbf{项目主页}：\\href{\\repourl}{\\nolinkurl{\\repourl}}\\par\n"
                    content = content[:abs_pos] + repo_line + content[abs_pos:]
                    changes.append("  added 项目主页 in info box (fallback)")

    if content != original:
        if not dry_run:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes
    return []

def main():
    dry_run = '--dry-run' in sys.argv
    tex_files = sorted(glob.glob('**/*-notes.tex', recursive=True) +
                       glob.glob('**/notes.tex', recursive=True))

    # Exclude template
    tex_files = [f for f in tex_files if 'templates/' not in f]

    total_changed = 0
    for f in tex_files:
        changes = patch_file(f, dry_run=dry_run)
        if changes:
            total_changed += 1
            print(f"{f}:")
            for c in changes:
                print(c)

    mode = "DRY RUN" if dry_run else "PATCHED"
    print(f"\n=== {mode}: {total_changed}/{len(tex_files)} files changed ===")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Fix all .tex files:
1. Replace 五道口纳什 & XXX in noteauthors
2. Fix "视频链接未填写" — hide the line when videourl is empty
3. Ensure 项目主页 has \par before it (newline)
4. Ensure 项目主页 has \par after it
"""
import glob, re, sys

def fix_file(path, dry_run=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    changes = []

    # 1. Fix noteauthors
    for old_author in [
        '五道口纳什 \\& Codex',
        '五道口纳什 \\& AI',
        '五道口纳什 \\& Claude',
        '五道口纳什',
        '青稞社区 \\& AI',
        '张小珺商业访谈录 \\& AI',
    ]:
        old = f'\\newcommand{{\\noteauthors}}{{{old_author}}}'
        new = '\\newcommand{\\noteauthors}{基于公开课程资料整理}'
        if old in content:
            content = content.replace(old, new)
            changes.append(f'  author: {old_author}')

    # 2. Fix "未填写" — replace ifdefempty block to hide when empty
    # Old pattern:
    #   \textbf{视频链接}：
    #   \ifdefempty{\videourl}{
    #   未填写
    #   }{
    #   \href{\videourl}{\nolinkurl{\videourl}}
    #   }
    old_pattern = (
        '\\textbf{视频链接}：\n'
        '\\ifdefempty{\\videourl}{\n'
        '未填写\n'
        '}{\n'
        '\\href{\\videourl}{\\nolinkurl{\\videourl}}\n'
        '}'
    )
    new_pattern = (
        '\\ifdefempty{\\videourl}{}{\n'
        '\\textbf{视频链接}：\\href{\\videourl}{\\nolinkurl{\\videourl}}\\par\n'
        '}'
    )
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        changes.append('  fixed 视频链接未填写')

    # Also handle article variant
    old_article = (
        '\\textbf{文章链接}：\n'
        '\\ifdefempty{\\videourl}{\n'
        '未填写\n'
        '}{\n'
        '\\href{\\videourl}{\\nolinkurl{\\videourl}}\n'
        '}'
    )
    new_article = (
        '\\ifdefempty{\\videourl}{}{\n'
        '\\textbf{文章链接}：\\href{\\videourl}{\\nolinkurl{\\videourl}}\\par\n'
        '}'
    )
    if old_article in content:
        content = content.replace(old_article, new_article)
        changes.append('  fixed 文章链接未填写')

    # 3. Fix 项目主页 missing \par before it
    # Pattern: something without \par right before \textbf{项目主页}
    # Need \par\n before \textbf{项目主页} if not already there
    content = re.sub(
        r'([^\n])\n(\\textbf\{项目主页\})',
        r'\1\\par\n\2',
        content
    )
    # But don't double up \par\par
    content = content.replace('\\par\\par\n\\textbf{项目主页}', '\\par\n\\textbf{项目主页}')

    # Ensure \par after 项目主页 line before \end{tcolorbox}
    content = re.sub(
        r'(\\textbf\{项目主页\}：\\href\{\\repourl\}\{\\nolinkurl\{\\repourl\}\})\s*\n(\\end\{tcolorbox\})',
        r'\1\\par\n\2',
        content
    )
    # Don't double \par
    content = content.replace('\\par\\par\n\\end{tcolorbox}', '\\par\n\\end{tcolorbox}')

    # 5. Fix \notedate{\today} — replace with \videopublishdate value
    today_match = re.search(r'\\newcommand\{\\notedate\}\{\\today\}', content)
    if today_match:
        # Extract videopublishdate value
        vd_match = re.search(r'\\newcommand\{\\videopublishdate\}\{(.+?)\}', content)
        if vd_match:
            publish_date = vd_match.group(1)
            content = content.replace(
                '\\newcommand{\\notedate}{\\today}',
                f'\\newcommand{{\\notedate}}{{{publish_date}}}'
            )
            changes.append(f'  notedate: \\today → {publish_date}')

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
    tex_files = [f for f in tex_files if 'templates/' not in f]

    total = 0
    for f in tex_files:
        changes = fix_file(f, dry_run=dry_run)
        if changes:
            total += 1
            if '--verbose' in sys.argv:
                print(f'{f}: {", ".join(changes)}')

    mode = "DRY RUN" if dry_run else "FIXED"
    print(f"=== {mode}: {total}/{len(tex_files)} files ===")

if __name__ == '__main__':
    main()

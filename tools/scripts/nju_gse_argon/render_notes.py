"""Render Argon's structured prose as editable TeX and Markdown."""
import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3] / 'nju-generative-software-engineering-2026/argon-rewrite'
REPO = ROOT.parents[1]


def esc(s):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
                    '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
                    '^': r'\textasciicircum{}'}
    replacements.update({'≈':r'\ensuremath{\approx}', '≠':r'\ensuremath{\ne}',
        '≤':r'\ensuremath{\le}', '≥':r'\ensuremath{\ge}', '→':r'\ensuremath{\rightarrow}',
        '⇒':r'\ensuremath{\Rightarrow}', '×':r'\ensuremath{\times}', '∈':r'\ensuremath{\in}',
        '∀':r'\ensuremath{\forall}', '∃':r'\ensuremath{\exists}', '∧':r'\ensuremath{\land}',
        '∨':r'\ensuremath{\lor}', '⊨':r'\ensuremath{\models}',
        '∪':r'\ensuremath{\cup}', '∩':r'\ensuremath{\cap}',
        '′':r'\ensuremath{\prime}', '働':r'{\cjkfallback 働}'})
    s = str(s).replace('**', '').replace('並', '并').replace('僅', '仅').replace('強', '强')
    parts = re.split(r'(\$(?!\{)[^$\n\u4e00-\u9fff]+\$|\\\([^\n]*?\\\)|\\Delta(?:_\{[^}]+\}|_[A-Za-z0-9])?)', s)
    output = []
    for part in parts:
        if part.startswith('$') and part.endswith('$'):
            output.append(r'\('+part[1:-1]+r'\)')
        elif part.startswith(r'\(') and part.endswith(r'\)'):
            output.append(part)
        elif part.startswith(r'\Delta'):
            output.append(r'\('+part+r'\)')
        else:
            output.append(''.join(replacements.get(c,c) for c in part).replace('`', ''))
    return ''.join(output)


PREAMBLE = r'''\documentclass[UTF8,a4paper,11pt,fontset=fandol]{ctexart}
\IfFontExistsTF{Droid Sans Fallback}
  {\newCJKfontfamily\cjkfallback{Droid Sans Fallback}}
  {\IfFontExistsTF{Noto Sans CJK SC}
    {\newCJKfontfamily\cjkfallback{Noto Sans CJK SC}}
    {\newcommand{\cjkfallback}{\CJKfamily{song}}}}
\usepackage[margin=22mm,headheight=15pt]{geometry}
\usepackage{graphicx,float,xcolor,amsmath,amssymb,booktabs,longtable,array,tabularx}
\usepackage[most]{tcolorbox}
\usepackage{listings,needspace,fancyhdr}
\usepackage[unicode,colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black,breaklinks=true]{hyperref}
\usepackage{xurl}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.65em}
\setlength{\emergencystretch}{3em}
\linespread{1.14}
\raggedbottom
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{南京大学 · 生成式软件工程 2026}\fancyfoot[C]{\thepage}
\newtcolorbox{importantbox}[1]{enhanced,breakable,colback=blue!3,colframe=blue!45!black,title={#1},fonttitle=\bfseries}
\newtcolorbox{knowledgebox}[1]{enhanced,breakable,colback=teal!3,colframe=teal!50!black,title={#1},fonttitle=\bfseries}
\newtcolorbox{warningbox}[1]{enhanced,breakable,colback=orange!4,colframe=orange!60!black,title={#1},fonttitle=\bfseries}
\lstset{basicstyle=\ttfamily\small,breaklines=true,columns=fullflexible,keepspaces=true,showstringspaces=false,frame=single,captionpos=b}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\begin{document}
'''


def render(i):
    d = ROOT/f'lecture{i:02d}'
    obj = json.loads((d/'generation/prose.json').read_text())
    plan = json.loads((d/'generation/plan.json').read_text())
    slides = json.loads((d/'sources/slides.json').read_text())
    used = [u['slide_id'] for s in obj['sections'] for u in s['units']]
    assert sorted(used) == sorted(x['id'] for x in slides)
    for ident in used: assert (d/f'slides-images/{ident}.png').exists(), ident
    subprocess.run(['python3', str(REPO/'tools/scripts/build_lecture_manifest.py'), str(d)], check=True, capture_output=True)
    manifest = d/'lecture-manifest.md'
    text = manifest.read_text()
    marker = '|---|---|---|---|---|'
    rows = [f'| {s["id"]} | slide | yes | `sources/official-slides.html` | slides-images/{s["id"]}.png |' for s in slides]
    text = text.replace(marker, marker+'\n'+'\n'.join(rows))
    manifest.write_text(text)
    matrix = ['# 覆盖矩阵与蓝图','', '| 来源页 | 章节 | 处理 |', '|---|---|---|']
    for s in plan['sections']:
        for ident in s['slide_ids']: matrix.append(f'| {ident} | {s["title"]} | 原图与正文解释 |')
    matrix += ['', '## 教师讲解摘要', '', '| 来源 | 要点 | 去处 |','|---|---|---|']
    for v in plan['teacher_voice']:
        matrix.append('| '+' | '.join(str(v.get(k,'' )).replace('|','／').replace('\n',' ') for k in ['source','point','placement'])+' |')
    (d/'coverage-matrix.md').write_text('\n'.join(matrix)+'\n')
    title = f'第 {i} 讲：' + re.sub(r'^第[一二三四五六七八\d\s]+讲[：:、\s]*', '', obj['title'])
    source_note = ('据蒋炎岩课程讲义、课件与课堂字幕整理。'
                   '正文：Gemini Argon；配图与编校：Codex。'
                   '原课程采用 CC BY-NC 4.0 许可。')
    tex = [PREAMBLE, r'\begin{titlepage}\centering\vspace*{25mm}',
           r'{\Large 南京大学 · 生成式软件工程 2026\par}\vspace{12mm}',
           r'{\Huge\bfseries '+esc(title)+r'\par}\vspace{10mm}',
           r'{\Large Argon 完整重写版\par}\vspace{10mm}',
           r'主讲与原始讲义作者：蒋炎岩\par',
           r'资料快照：2026-10-20\par\vfill', esc(source_note),
           r'\vspace{8mm}\url{https://jyywiki.cn/GSE/2026/}',r'\end{titlepage}',
           r'\tableofcontents\clearpage',r'\section*{导读}\addcontentsline{toc}{section}{导读}',esc(obj['lead'])]
    md = [f'# {title}', '', source_note, '', obj['lead'], '']
    diagram = json.loads((d/'assets/mechanism.json').read_text())
    tex += [r'\paragraph{机制总览}',esc(diagram['before']),
            r'\begin{figure}[H]\centering\includegraphics[width=\linewidth]{assets/mechanism.pdf}',
            r'\caption{'+esc(diagram['title'])+'（据本讲绘制）}',r'\end{figure}',
            r'\begin{knowledgebox}{读图：机制与适用边界}',esc(diagram['reading']),esc(diagram['after']),r'\end{knowledgebox}']
    md += ['### 机制总览','',diagram['before'],'','![机制总览](assets/mechanism.svg)','',
           '读图：'+diagram['reading'],'',diagram['after'],'']
    for sec in obj['sections']:
        tex += [r'\needspace{8\baselineskip}\section{'+esc(sec['title'])+'}',esc(sec['intro'])]
        md += ['## '+sec['title'],'',sec['intro'],'']
        for u in sec['units']:
            sid = u['slide_id']; page = int(sid.split('-')[1])
            tex += [r'\subsection{'+esc(u['title'])+'}',esc(u['before']),
                    r'\begin{figure}[H]\centering',
                    r'\includegraphics[width=\linewidth]{slides-images/'+sid+'.png}',
                    r'\caption{'+esc(u['title'])+f'（官方课件第 {page} 页）'+'}',
                    r'\end{figure}',
                    esc(u['reading']),
                    esc(u['after'])]
            md += ['### '+u['title'],'',u['before'],'',f'![官方课件第 {page} 页](slides-images/{sid}.png)','',
                   u['reading'],'',u['after'],'']
            if i == 5 and page == 7:
                frames = [f'images/official-slide007-video-t{t:03d}.png' for t in [5,25,45]]
                if all((d/f).exists() for f in frames):
                    tex += [r'\begin{figure}[H]\centering']
                    tex += [r'\includegraphics[width=.32\linewidth]{'+f+'}' for f in frames]
                    tex += [r'\caption{Office Assistant 演示，课件内嵌视频第 5、25、45 秒。}',r'\end{figure}']
                    md += ['原课件内嵌视频补充帧（片内 5、25、45 秒）：','']
                    md += [f'![课件内嵌视频补充帧]({f})' for f in frames]+['']
        for b in sec['boxes']:
            assert b['kind'] in ['importantbox','knowledgebox','warningbox']
            tex += ['\\begin{'+b['kind']+'}{'+esc(b['title'])+'}',esc(b['text']),'\\end{'+b['kind']+'}']
            md += ['> '+b['title'],'>','> '+b['text'].replace('\n','\n> '),'']
        table = sec.get('table')
        if table:
            cols = len(table['headers']); assert all(len(r)==cols for r in table['rows'])
            tex += [r'\par\needspace{5\baselineskip}\textbf{术语消化：'+esc(table['caption'])+'}',
                    r'\begin{center}\small\begin{tabularx}{\linewidth}{'+'Y'*cols+'}',r'\toprule',
                    ' & '.join(esc(h) for h in table['headers'])+r'\\\midrule']
            for row in table['rows']:tex.append(' & '.join(esc(c) for c in row)+r'\\[3pt]')
            tex += [r'\bottomrule\end{tabularx}\end{center}']
            md += ['术语消化：'+table['caption'],'','| '+' | '.join(table['headers'])+' |','|'+'---|'*cols]
            md += ['| '+' | '.join(str(c).replace('|','／') for c in row)+' |' for row in table['rows']]+['']
        code = sec.get('code')
        if code:
            tex += [r'\begin{lstlisting}[basicstyle={\ttfamily\small\linespread{1}\selectfont},captionpos=t,caption={'+esc(code['caption'])+'}]\n'+code['source'].strip('\n')+'\n'+r'\end{lstlisting}',esc(code['explanation'])]
            md += ['```'+code.get('language','text'),code['source'],'```','',code['explanation'],'']
        eq = sec.get('equation')
        if eq:
            tex += [r'\['+'\n'+eq['latex']+'\n'+r'\]',esc(eq['explanation'])]
            md += ['$$',eq['latex'],'$$','',eq['explanation'],'']
        tex += [r'\needspace{7\baselineskip}\subsection{本章小结}',esc(sec['summary'])]
        md += ['### 本章小结','',sec['summary'],'']
    tex += [r'\needspace{8\baselineskip}\section{总结与延伸}',esc(obj['conclusion']),r'\subsection{学习练习}',
            '用下面的延伸练习检查自己能否应用本讲方法。']
    md += ['## 总结与延伸','',obj['conclusion'],'','### 学习练习','',
           '用下面的延伸练习检查自己能否应用本讲方法。','']
    for n, exercise in enumerate(obj['practice'],1):
        tex += [r'\paragraph{练习 '+str(n)+'}',esc(exercise['task']),r'\par 验收标准：'+esc(exercise['acceptance'])]
        md += [f'{n}. {exercise["task"]}','',f'   验收标准：{exercise["acceptance"]}','']
    tex += [r'\subsection{拓展阅读}',
            '下面列出本讲的原始讲义、课件和相关项目，便于回看案例、查阅代码并继续实践。',
            r'\begin{itemize}']
    refs = [{'title':'官方讲义','url':f'https://jyywiki.cn/GSE/2026/lect{i}.md'},
            {'title':'官方课件','url':f'https://jyywiki.cn/GSE/2026/slides{i}.html'},
            {'title':'社区字幕校订稿（固定版本）','url':'https://github.com/NinZeige/NJU-2026-GSE-Captions/tree/0456f3a46fd5fa2f2a86123e02b7ed48696adacb'},
            {'title':'原课程许可 CC BY-NC 4.0','url':'https://creativecommons.org/licenses/by-nc/4.0/'}] + obj['references']
    md += ['### 拓展阅读','']
    seen = set()
    for ref in refs:
        if ref['url'] in seen:continue
        seen.add(ref['url'])
        tex += [r'\item '+esc(ref['title'])+r'：\url{'+ref['url']+'}']
        md += [f'- [{ref["title"]}]({ref["url"]})']
    tex += [r'\end{itemize}',r'\end{document}']
    (d/f'lecture{i:02d}-notes.tex').write_text('\n\n'.join(tex)+'\n')
    (d/f'lecture{i:02d}-notes.md').write_text('\n'.join(md)+'\n')
    print(i, 'rendered', len(used), 'slides', flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('lectures', nargs='+', type=int)
    for i in ap.parse_args().lectures: render(i)

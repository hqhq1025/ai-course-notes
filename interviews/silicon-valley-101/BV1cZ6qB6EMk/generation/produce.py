"""One-episode Argon request receipts and editable note rendering."""
import argparse
import importlib.util
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

EPISODE = Path(__file__).resolve().parent.parent
REPO = EPISODE.parents[2]
STEM = 'BV1cZ6qB6EMk-notes'
SOURCE_URL = 'https://www.bilibili.com/video/BV1cZ6qB6EMk/'
_spec = importlib.util.spec_from_file_location('course_render', REPO / 'tools/scripts/nju_gse_argon/render_notes.py')
_renderer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_renderer)
esc = _renderer.esc
_writer_spec = importlib.util.spec_from_file_location('argon_write', REPO / 'tools/scripts/argon_write.py')
_writer = importlib.util.module_from_spec(_writer_spec)
_writer_spec.loader.exec_module(_writer)


def request(prompt_file, prefix):
    """Send the prepared prompt through the shared writer."""
    return _writer.request(prompt_file, prefix)


def prose(text):
    """Reuse course typography and keep explicit display formulas intact."""
    parts = re.split(r'(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\])', str(text))
    return '\n'.join(
        '\\[\n' + p[2:-2].strip() + '\n\\]' if p.startswith(('$$', r'\['))
        else _renderer.prose(p) for p in parts if p)


def validate(book):
    for key in ['title', 'lead', 'conclusion']:
        if not isinstance(book.get(key), str) or not book[key].strip():
            raise ValueError(f'Missing text: {key}')
    if not book.get('sections'):
        raise ValueError('No sections')
    for number, section in enumerate(book['sections'], 1):
        for key in ['title', 'intro', 'summary']:
            if not isinstance(section.get(key), str) or not section[key].strip():
                raise ValueError(f'Section {number}: missing {key}')
        for unit in section['units']:
            if not unit.get('title') or not unit.get('paragraphs') or not all(isinstance(p, str) and p.strip() for p in unit['paragraphs']):
                raise ValueError(f'Section {number}: incomplete unit')
        for box in section.get('boxes', []):
            if box['kind'] not in {'importantbox', 'knowledgebox', 'warningbox'}:
                raise ValueError(f'Unknown box kind: {box["kind"]}')
        table = section.get('table')
        if table and (not table['headers'] or any(len(row) != len(table['headers']) for row in table['rows'])):
            raise ValueError(f'Section {number}: uneven table')
        figure = section.get('figure')
        if figure:
            for key in ['path', 'caption', 'before', 'reading', 'after']:
                if not figure.get(key):
                    raise ValueError(f'Section {number}: missing figure {key}')
            image = (EPISODE / figure['path']).resolve()
            if not image.is_relative_to(EPISODE) or not image.is_file():
                raise ValueError(f'Missing/local-only figure: {image}')
            if re.search(r'[^A-Za-z0-9_./-]', figure['path']):
                raise ValueError('Figure path must use portable ASCII filename characters')
    for reference in book.get('references', []):
        if not re.match(r'^https?://[^\s{}\\]+$', reference['url']):
            raise ValueError(f'Invalid reference URL: {reference["url"]}')


def render(book_path):
    book = json.loads(book_path.read_text(encoding='utf-8'))
    validate(book)
    info = json.loads((EPISODE / 'sources/source.info.json').read_text(encoding='utf-8'))
    public_date = datetime.fromtimestamp(info['pubdate'], ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d')
    guest_lines = re.search(r'【嘉宾】\s*([\s\S]*?)(?=\n【|\Z)', info['desc']).group(1).strip().splitlines()
    guests = [re.sub(r'（X:.*?）', '', line).strip() for line in guest_lines if line.strip()]
    preamble = _renderer.PREAMBLE.replace('南京大学 · 生成式软件工程 2026', '硅谷101 · 访谈学习笔记')
    preamble = preamble.replace(r'\begin{document}',
        r'\newcommand{\notetitle}{' + esc(book['title']) + '}\n' +
        r'\newcommand{\videocoverpath}{cover.jpg}' + '\n' +
        r'\newcommand{\videourl}{' + SOURCE_URL + '}\n' +
        r'\newcommand{\videochannel}{硅谷101播客}' + '\n' +
        r'\newcommand{\videopublishdate}{' + public_date + '}\n' +
        r'\newcommand{\noteauthors}{泓君、徐栋、亓鲁、吕瀛杰}' + '\n' +
        r'\newcommand{\sourceurl}{' + SOURCE_URL + '}\n' + r'\begin{document}')
    tex = [preamble, r'\begin{titlepage}\centering\vspace*{4mm}',
           r'{\Large 硅谷101 · 访谈学习笔记\par}\vspace{8mm}',
           r'{\LARGE\bfseries \notetitle\par}\vspace{7mm}',
           r'\includegraphics[width=.86\linewidth,height=.27\textheight,keepaspectratio]{cover.jpg}',
           r'\par\vspace{6mm}{\small 原节目：' + esc(info['title']) + r'\par}',
           r'\vspace{4mm}主播：泓君\par', *[r'{\small ' + esc(g) + r'\par}' for g in guests],
           r'\vfill 发布：' + public_date + r'\par',
           r'整理：2026-10-20\quad 正文：Gemini Argon\quad 配图与编校：Codex\par',
           r'\vspace{4mm}\url{' + SOURCE_URL + '}', r'\end{titlepage}',
           r'\begingroup\small\setlength{\parskip}{0pt}\tableofcontents\endgroup\clearpage', r'\section*{导读}\addcontentsline{toc}{section}{导读}', prose(book['lead'])]
    md = ['# ' + book['title'], '', '原节目：' + info['title'], '',
          '主播：泓君。嘉宾：' + '；'.join(guests) + '。', '',
          f'发布：{public_date}。整理：2026-10-20。', '',
          f'[观看原节目]({SOURCE_URL})', '', '## 导读', '', book['lead'], '']
    for section in book['sections']:
        tex += [r'\needspace{8\baselineskip}\section{' + esc(section['title']) + '}', prose(section['intro'])]
        md += ['## ' + section['title'], '', section['intro'], '']
        for unit in section['units']:
            tex += [r'\needspace{6\baselineskip}\subsection{' + esc(unit['title']) + '}']
            md += ['### ' + unit['title'], '']
            for paragraph in unit['paragraphs']:
                tex += [prose(paragraph), '']
                md += [paragraph, '']
        for box in section.get('boxes', []):
            tex += [r'\begin{' + box['kind'] + '}{' + esc(box['title']) + '}', prose(box['text']), r'\end{' + box['kind'] + '}']
            md += ['> **' + box['title'] + '**', '>', '> ' + box['text'].replace('\n', '\n> '), '']
        table = section.get('table')
        if table:
            columns = len(table['headers'])
            width = f'\\dimexpr(\\linewidth-{2 * columns}\\tabcolsep)/{columns}\\relax'
            spec = ('>{\\raggedright\\arraybackslash}p{' + width + '}') * columns
            header = ' & '.join(esc(h) for h in table['headers']) + r'\\\midrule'
            tex += [r'\begin{table}[H]\centering\small',
                    r'\caption{' + esc(table['caption']) + '}',
                    r'\begin{tabular}{' + spec + '}', r'\toprule', header]
            tex += [' & '.join(esc(cell) for cell in row) + r'\\[4pt]' for row in table['rows']]
            tex += [r'\bottomrule\end{tabular}\end{table}']
            cell = lambda value: str(value).replace('|', '\\|').replace('\n', '<br>')
            md += [table['caption'], '', '| ' + ' | '.join(map(cell, table['headers'])) + ' |', '|' + '---|' * columns]
            md += ['| ' + ' | '.join(map(cell, row)) + ' |' for row in table['rows']] + ['']
        figure = section.get('figure')
        if figure:
            tex += [prose(figure['before']), r'\begin{figure}[H]\centering',
                    r'\includegraphics[width=\linewidth,height=.68\textheight,keepaspectratio]{' + figure['path'] + '}',
                    r'\caption{' + esc(figure['caption']) + '}', r'\end{figure}',
                    r'\begin{knowledgebox}{读图：' + esc(section['title']) + '}',
                    prose(figure['reading']), r'\end{knowledgebox}', prose(figure['after'])]
            web_image = figure['path']
            if Path(web_image).suffix == '.pdf' and (EPISODE / Path(web_image).with_suffix('.png')).exists():
                web_image = str(Path(web_image).with_suffix('.png'))
            md += [figure['before'], '', '![' + figure['caption'] + '](' + web_image + ')', '', figure['reading'], '', figure['after'], '']
        tex += [r'\needspace{6\baselineskip}\subsection{本章小结}', prose(section['summary'])]
        md += ['### 本章小结', '', section['summary'], '']
    tex += [r'\needspace{8\baselineskip}\section{总结与延伸}', prose(book['conclusion'])]
    md += ['## 总结与延伸', '', book['conclusion'], '']
    if book.get('references'):
        tex += [r'\subsection{拓展阅读}', '以下资料供回看节目、查阅术语与继续学习。', r'\begin{itemize}']
        md += ['### 拓展阅读', '']
        for reference in book['references']:
            tex += [r'\item ' + esc(reference['title']) + r'：\url{' + reference['url'] + '}']
            md += ['- [' + reference['title'] + '](' + reference['url'] + ')']
        tex += [r'\end{itemize}']
    tex += [r'\end{document}']
    for suffix, lines in [('.tex', tex), ('.md', md)]:
        target = EPISODE / (STEM + suffix)
        target.write_text('\n'.join(line.rstrip() for line in '\n'.join(lines).splitlines()) + '\n', encoding='utf-8')
        print(target)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    request_parser = commands.add_parser('request')
    request_parser.add_argument('prompt_file', type=Path)
    request_parser.add_argument('outprefix', type=Path)
    render_parser = commands.add_parser('render')
    render_parser.add_argument('book', type=Path, nargs='?', default=EPISODE / 'generation/book.json')
    args = parser.parse_args()
    if args.command == 'request':
        request(args.prompt_file, args.outprefix)
    else:
        render(args.book)

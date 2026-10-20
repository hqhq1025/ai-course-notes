"""Group every ASR segment into readable timestamped source paragraphs."""
import json
from pathlib import Path

episode = Path(__file__).resolve().parent.parent
raw = json.loads((episode / 'sources/transcript.raw.json').read_text())


def stamp(seconds):
    seconds = int(seconds)
    return f'{seconds // 3600:02d}:{seconds // 60 % 60:02d}:{seconds % 60:02d}'


lines = ['# 完整口述阅读稿', '', '按约 30 秒分组，保留全部 ASR 文字和原始段落编号。未逐字校订；术语核对见 terminology-check.md。', '']
group = []
for index, segment in enumerate(raw['segments'], 1):
    if group and segment['start'] - group[0][1]['start'] >= 30:
        lines += [f"[{stamp(group[0][1]['start'])}–{stamp(group[-1][1]['end'])}；S{group[0][0]}–S{group[-1][0]}] " + ' '.join(s['text'] for _, s in group), '']
        group = []
    group.append((index, segment))
if group:
    lines += [f"[{stamp(group[0][1]['start'])}–{stamp(group[-1][1]['end'])}；S{group[0][0]}–S{group[-1][0]}] " + ' '.join(s['text'] for _, s in group), '']
(episode / 'sources/transcript-reading.md').write_text('\n'.join(lines))
print(f"Grouped {len(raw['segments'])} segments without omissions")

blueprint_path = episode / 'generation/accepted-blueprint.json'
if blueprint_path.exists():
    blueprint = json.loads(blueprint_path.read_text())
    matrix = ['# 口述覆盖矩阵', '', '按核定蓝图规划；成稿覆盖另行对照正文验收。', '',
              '| 节点 | 来源时间 | 正文位置 | 需要保留的讲解 | 配图 |',
              '|---|---|---|---|---|']
    for section in blueprint['sections']:
        matrix.append('| voice-%02d | %s | %s | %s | assets/%s.pdf |' % (
            section['id'], '；'.join(section['ranges']), section['title'],
            '；'.join(section['points']), section['figure']))
    matrix += ['', '## 连续时间覆盖', '',
               '2740 条 ASR 均保留在 transcript-reading.md，编号沿用原始段序。正文覆盖 00:01:11 到 01:19:33 的实质讨论；开场预告合并入各主题，推广与结束语省略。', '',
               '讲者要点分别见 sources/digest-00-35.md 与 sources/digest-35-80.md，覆盖85条带时间的口述记录。', '',
               '## 省略与合并', '']
    matrix += ['- '+row['range']+'：'+row['reason'] for row in blueprint['omissions']]
    (episode / 'coverage-matrix.md').write_text('\n'.join(matrix)+'\n')
    manifest = episode / 'lecture-manifest.md'
    if manifest.exists():
        text = manifest.read_text()
        start = text.index('| ID | Type | Required | Source | Title / Snippet |')
        end = text.index('\n## Existing Note', start)
        table = '| ID | Type | Required | Source | Title / Snippet |\n|---|---|---|---|---|\n'
        for section in blueprint['sections']:
            table += '| voice-%02d | section | yes | `%s` | %s |\n' % (
                section['id'], '；'.join(section['ranges']), section['title'])
        text = text[:start]+table+'\n'+text[end:]
        figures_path = episode / 'assets/figures.json'
        if figures_path.exists():
            figures = json.loads(figures_path.read_text())
            start = text.index('## Local Visual Assets')
            end = text.index('## Coverage Nodes', start)
            assets = '## Local Visual Assets\n\n'
            assets += '\n'.join('- `%s` — %s（%s）' % (f['path'], f['title'], f['source']) for f in figures)
            text = text[:start] + assets + '\n\n' + text[end:]
        manifest.write_text(text)

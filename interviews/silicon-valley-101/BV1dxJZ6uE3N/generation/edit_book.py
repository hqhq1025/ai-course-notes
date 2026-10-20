"""Assemble chapters, request Argon's complete-document edit, and apply exact edits."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

from write_chapters import blueprint, episode, source_names, source_text, writer


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['request', 'apply'])
    parser.add_argument('--attempt', default='resume1')
    parser.add_argument('--edit', default='editorial-01')
    parser.add_argument('--sections', nargs='+', type=int, default=list(range(1, 8)))
    parser.add_argument('--edits', nargs='+')
    args = parser.parse_args()
    folder = episode / 'generation'
    prefix = folder / args.edit
    if args.action == 'request':
        sections = [json.loads((folder / f'chapter-{i:02d}-{args.attempt}.json').read_text()) for i in range(1, 8)]
        book = {'title': blueprint['title'], 'sections': sections}
        save(folder / 'book-draft.json', book)
        figures = json.loads((episode / 'assets/figures.json').read_text())
        findings = folder / 'review-findings.md'
        prompt = '''你是这份访谈学习笔记的作者及最终主编。通读下面完整初稿、完整转录、核定蓝图和配图语义，完成整篇编辑。
保留人物视角、真实例子和推理，明确观点与事实归属，改善章节衔接、重复定义和机械措辞。条件写进解释；删除反复出现的泛化免责声明，不让“不是A而是B”句式占满正文。正文是教学文章，不能变成审计报告。保留蓝图全部实质内容，尤其插花纠正动作、二十个Agent与平台利益、沙箱总账单、机器人快慢控制、厨房资源比喻、实验周期、工业酶应用、人的学习和主持人的结尾总结。数字必须带任务条件，预测保持预测语气。对缺漏例子可扩写相应完整段落。
请写导读（约300字）、总结与延伸（约400字），并为七张图写与章节论证相连的before、reading、after，不重复刚讲过的定义。图是依据节目绘制的机制示意；用图的箭头、行列和颜色讲清比较方法与因果关系，必要范围写进解释，不要每图都附“不能证明”。figure.caption用提供的图标题、来源时间及“依据节目口述整理”。首次出现英文术语需定义，密集术语放进现有表格；适当用短列表和关键短语强调。
返回完整JSON对象：
{"lead":"导读","conclusion":"总结与延伸","figures":[{"id":"提供的图ID","path":"提供的PDF路径","caption":"图标题与来源","before":"论证如何引出图，80到120字","reading":"读图讲解，120到180字","after":"接续下一步，60到100字"}],"edits":[{"path":"/sections/0/units/0/paragraphs/0","old":"该字符串字段中逐字存在且唯一的原文","new":"替换文字"}],"editor_note":"实际改进"}
edits只修改字符串叶节点；path使用从0开始的列表索引；old必须精确匹配一次。可替换整段，不改JSON结构、章节标题或图ID。优先完整修复独立审阅要求，可返回60到80处必要修改；问题少时不凑数量。同一问题在正文、表格、小结重复出现时全部同步修正。不要输出未修改段落，不编造引用和新事实。
'''
        prompt += '\n【全文初稿】\n' + json.dumps(book, ensure_ascii=False)
        prompt += '\n【配图】\n' + json.dumps(figures, ensure_ascii=False)
        prompt += '\n【核定蓝图】\n' + json.dumps(blueprint, ensure_ascii=False)
        if findings.exists():
            prompt += '\n【独立审阅】\n' + findings.read_text()
        prompt += '\n【完整来源及核对】\n' + source_text
        prompt += '\n【本批返回范围与精简格式，覆盖上方返回格式】\n'
        prompt += f'本次仍通读全文，但只返回章节 {args.sections} 的文字修改及这些章节的配图。章节编号从1开始，JSON路径sections从0开始。'
        prompt += 'edits每项仅含path和new，不重复old原文。new是该字符串字段的完整替换值。脚本用本次请求中的全文初稿哈希绑定版本，再逐字段替换。请完整落实这些章的审查意见，不输出其他章节的改动。'
        prompt += '仅当包含第1章时返回lead和conclusion，否则省略这两个字段。figures只含本批章节，editor_note照常返回。修改正确清楚的段落无须返回。'
        path = Path(str(prefix) + '-input.txt')
        path.write_text(prompt)
        writer.request(path, prefix, sources=[folder / 'book-draft.json', *[episode / 'sources' / name for name in source_names]])
        return
    original = folder / 'book-draft.json'
    book = copy.deepcopy(json.loads(original.read_text()))
    responses = []
    for name in args.edits or [args.edit]:
        receipt = json.loads((folder / (name + '-receipt.json')).read_text())
        digest = hashlib.sha256(original.read_bytes()).hexdigest()
        if not any(entry['sha256'] == digest and Path(entry['path']).name == original.name for entry in receipt['source_snapshot']):
            raise ValueError('Draft differs from the version used for editing')
        responses.append(json.loads((folder / (name + '.json')).read_text()))
    response = {'edits': [e for r in responses for e in r['edits']],
                'figures': [f for r in responses for f in r['figures']],
                'lead': next(r['lead'] for r in responses if 'lead' in r),
                'conclusion': next(r['conclusion'] for r in responses if 'conclusion' in r),
                'editor_note': '\n'.join(r['editor_note'] for r in responses)}
    seen = set()
    for edit in response['edits']:
        if edit['path'] in seen:
            raise ValueError('Duplicate edited path: ' + edit['path'])
        seen.add(edit['path'])
        parts = edit['path'].strip('/').split('/')
        node = book
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        key = int(parts[-1]) if isinstance(node, list) else parts[-1]
        if not isinstance(node[key], str) or not isinstance(edit['new'], str):
            raise ValueError('Edit must replace an existing string: ' + edit['path'])
        node[key] = edit['new']
    book['lead'], book['conclusion'] = response['lead'], response['conclusion']
    figures = {figure['id']: figure for figure in response['figures']}
    for section, plan in zip(book['sections'], blueprint['sections']):
        section['figure'] = figures[plan['figure']]
    book['references'] = [
        {'title': '硅谷101：本期完整节目', 'url': 'https://www.bilibili.com/video/BV1dxJZ6uE3N/'},
        {'title': 'AlphaFold 3 官方说明：代码、模型参数与数据条款', 'url': 'https://github.com/google-deepmind/alphafold3/blob/131ab9e7420066523c62546199243f7a9b3e3e78/README.md'}]
    corrections_path = folder / 'factual-corrections.json'
    corrections = json.loads(corrections_path.read_text()) if corrections_path.exists() else []
    for correction in corrections:
        parts = correction['path'].strip('/').split('/')
        node = book
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        key = int(parts[-1]) if isinstance(node, list) else parts[-1]
        if node[key].count(correction['old']) != 1:
            raise ValueError('Factual correction does not match: ' + correction['path'])
        node[key] = node[key].replace(correction['old'], correction['new'], 1)
    save(folder / 'book.json', book)
    save(folder / 'editorial-applied.json', {
        'model': writer.MODEL, 'edits': len(response['edits']),
        'codex_verified_factual_corrections': len(corrections),
        'draft_sha256': hashlib.sha256(original.read_bytes()).hexdigest(),
        'final_sha256': hashlib.sha256((folder / 'book.json').read_bytes()).hexdigest(),
        'editor_note': response['editor_note']})
    print('Applied', len(response['edits']), 'exact edits')


if __name__ == '__main__':
    main()

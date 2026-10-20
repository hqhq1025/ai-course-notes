"""Argon edits each complete lecture; exact-span patches keep requests bounded."""
import argparse
import concurrent.futures
import copy
import hashlib
import json
from pathlib import Path

from argon_writer import CAUTIONS, ROOT, request, sources


def leaves(value, path=''):
    if isinstance(value, dict):
        for key, child in value.items():
            if key not in ('slide_id', 'url', 'kind', 'language'):
                yield from leaves(child, path+'/'+key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from leaves(child, path+'/'+str(index))
    elif isinstance(value, str):
        yield {'path': path, 'text': value}


def apply_edits(draft, edits):
    result = copy.deepcopy(draft)
    editable = {leaf['path'] for leaf in leaves(draft)}
    for edit in edits:
        if edit['path'] not in editable:
            raise ValueError(f'Not an editable text field: {edit["path"]}')
        parts = edit['path'].strip('/').split('/')
        node = result
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        key = int(parts[-1]) if isinstance(node, list) else parts[-1]
        old = edit['old']
        if not isinstance(node[key], str) or not old or node[key].count(old) != 1:
            raise ValueError(f'Edit does not match exactly once: {edit["path"]}: {old[:100]}')
        node[key] = node[key].replace(old, edit['new'], 1)
    original_ids = [u['slide_id'] for s in draft['sections'] for u in s['units']]
    final_ids = [u['slide_id'] for s in result['sections'] for u in s['units']]
    assert original_ids == final_ids
    return result


def edit_lecture(i):
    folder = ROOT/f'lecture{i:02d}'/'generation'
    draft_path = folder/'prose-draft.json'
    if not draft_path.exists():
        draft_path.write_bytes((folder/'prose.json').read_bytes())
    draft = json.loads(draft_path.read_text())
    findings_path = folder/'review-findings.md'
    findings = findings_path.read_text() if findings_path.exists() else ''
    prompt = '''你是本讲教材的最终主编。请通读下面完整初稿和官方资料，在全讲上下文中编辑，使读者能顺着问题、例子、推导和检验学懂课程。正文是你此前写的，现在需要统一改稿。

优先完成全部独立审阅意见中的事实、代码、数学和因果修正，并检查同一错误的其他出现位置。然后编辑每章引导和跨节连接，统一术语，合并重复定义。逐页套话（“本页展示”“阅读本页时”“这张图告诉我们”）应改成具体内容。保持完整教学内容与全部课件页；删除冗余句，不能把正文压缩成摘要。

写作要求：用自然、直接、清楚的中文，有问题、输入、过程、结果。别把说明写成口号或劝告。“唯有/彻底/瞬间/必然/无人能敌/残酷真相”若缺少事实依据，改成具体作用。减少“不是A而是B”句式。不要添加免责声明，不要每页再总结“不能证明/不代表/仅供参考”。把真实前提放在机制本身，例如限定输入容量、标明测试检查的行为、说明锁由谁持有。课堂假说只需第一次明确“老师推测”，后续解释假说内容，不反复声明未证实。保留课堂例子和讲者思路，避免生硬译词、外语杂字和过密的抽象名词。段落之间应有所推进，不重复刚讲过的结论。所有程序和公式保持正确。

返回合法 JSON，只有需要修改的文字片段，不要重复整讲。格式：
{"edits":[{"path":"/sections/0/units/0/before","old":"该字段中逐字存在且唯一的原文片段","new":"修改后的片段"}],"editor_note":"简短说明全讲主线和实际完成的改进"}

每个路径指向下面列表中一个字符串叶节点。old 必须是该字段的原文且只匹配一次。替换可覆盖完整段落、代码或公式，也可以仅一个句子。允许同一字段多处互不重叠的替换。保留原字段结构和 slide_id。不输出未修改的字段。代码中的反斜杠必须满足JSON转义。优先修完所有事实问题，此外检查全篇衔接、重复和绝对化措辞，输出约60到110处高价值编辑即可，不需改动本来清楚正确的段落。
'''
    prompt += '\n【技术核查】\n'+CAUTIONS[i]+'\n【独立审阅发现】\n'+findings
    prompt += '\n【全讲初稿，按可编辑路径列出】\n'+json.dumps(list(leaves(draft)), ensure_ascii=False)
    prompt += '\n【来源材料，用于事实校核】\n'+sources(i)
    response = request(i, 'editorial', prompt)
    matching_path = folder/'editorial-matching.json'
    if matching_path.exists():
        response = copy.deepcopy(response)
        for correction in json.loads(matching_path.read_text()):
            response['edits'][correction['index']]['old'] = correction['old']
    final = apply_edits(draft, response['edits'])
    final_text = json.dumps(final, ensure_ascii=False, indent=2)+'\n'
    (folder/'prose.json').write_text(final_text)
    report = {'model':'gemini-4-argon', 'edits':len(response['edits']),
              'draft_sha256':hashlib.sha256(draft_path.read_bytes()).hexdigest(),
              'final_sha256':hashlib.sha256(final_text.encode()).hexdigest(),
              'editor_note':response.get('editor_note','')}
    (folder/'editorial-applied.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'L{i:02d} edited: {len(response["edits"])} exact replacements', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lectures', nargs='+', type=int)
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(edit_lecture, args.lectures))

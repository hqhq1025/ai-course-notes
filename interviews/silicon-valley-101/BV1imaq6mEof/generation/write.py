"""Write chapters and edit the assembled note with the shared Argon client."""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / 'generation'
spec = importlib.util.spec_from_file_location('writer', ROOT.parents[2] / 'tools/scripts/argon_write.py')
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def request(name, prompt):
    result = GEN / (name + '.json')
    if result.exists():
        return json.loads(result.read_text())
    source = GEN / (name + '-input.txt')
    source.write_text(prompt)
    return writer.request(source, GEN / name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['chapters', 'edit', 'figures'])
    parser.add_argument('--attempt', default='01')
    args = parser.parse_args()
    blueprint = json.loads((GEN / 'blueprint.json').read_text())
    names = ['transcript.raw.txt', 'source-notes.md', 'source.info.json', 'terminal-bench.md', 'hle.md']
    sources = '\n\n'.join('【' + name + '】\n' + (ROOT / 'sources' / name).read_text() for name in names)
    if args.action == 'figures':
        book = json.loads((GEN / 'book.json').read_text())
        drawings = '\n'.join(path.read_text() for path in sorted((ROOT / 'assets').glob('*.svg')))
        prompt = '''核对下面实际SVG和完整书稿，修正六张图的before/reading/after，并改写导读。上轮读图出现不存在的左右支路，必须按SVG坐标和实际节点说明。
第三图实际为上排3类任务汇到下方总分，再用底部一行文字提示跨任务表现与真实体验，没有左右支路。第四图从上排左到右，再下到下排右向左，任务设计在上排最后。第五图从上方任务向下分为左侧SFT和右侧RL，底部是说明文字而非框。第六图下方实际只写隔离测试内容/复核标准与解法/核对过程与结果，不要称图中有未绘出的多模型或流程录屏节点。更具体的方法可以作为正文联系。
图都在该章小节正文之后、章末小结之前，因此after不要称接下来才讲已经讲过的本章内容。自然引向下一章，第六章则收束并转总结。六图reading各100到150汉字，before和after各60到80汉字。导读约220字，直接用可理解的问题讲清读者会学到什么，不堆缩写，不自夸系统拆解深度对谈。
返回JSON：{"lead":"导读","figures":[{"id":"图ID","before":"...","reading":"...","after":"..."}]}。保留事实、不要新增数据。
'''
        prompt += '\n【实际SVG】\n' + drawings + '\n【完整成稿】\n' + json.dumps(book, ensure_ascii=False) + '\n' + sources
        result = request('figure-edit-' + args.attempt, prompt)
        book['lead'] = result['lead']
        figures = {f['id']: f for f in result['figures']}
        for chapter in book['sections']:
            f = figures[chapter['figure']['id']]
            chapter['figure'].update({key:f[key] for key in ['before','reading','after']})
        save(GEN / 'book.json', book)
        print('Figure explanations corrected', flush=True)
        return
    if args.action == 'chapters':
        for chapter in blueprint['sections']:
            prompt = '''依据完整节目转录和蓝图，写一章可独立学习的中文访谈讲义。只写指定章。用流畅的正常段落解释问题、机制、例子和下一步，不写审计报告，不把口述压成PPT字幕。
保留说话人观点和分歧。自然使用“嘉宾提醒”“实践经验”等，具体案例带1到3处分钟时间。ASR姓名和术语按来源说明纠正。影响结论的条件写入原句；不反复附加“不能证明/不代表/仅供参考”的泛化免责声明。节目估计不能变统计，预测不能变现状，补充README不能变节目原话。
按指定章节小节展开，每章约1600到2200汉字，随内容调整。每小节2到4段，要有前因、具体做法、结果和解释。重要术语首次解释，比较用表格，并列观点/步骤可用真正换行的列表与少量**重点短语**；连续推理用段落。不要编造公式、引语、数字或新链接。
输出完整JSON：{"title":"蓝图标题","intro":"约100字承接","units":[{"title":"蓝图小节标题","paragraphs":["段落","段落"]}],"boxes":[{"kind":"importantbox或knowledgebox或warningbox","title":"内容明确的短标题","text":"80到120字的具体解释"}],"table":{"caption":"比较主题","headers":["术语或场景","解决的问题","机制或取舍"],"rows":[["简短","简短","简短"]]},"figure":null,"summary":"约120字本章小结"}。
每章两个有具体教学内容的框、一个3到5行表格。避免表格重复段落。图随后插入。
'''
            prompt += '\n【完整蓝图】\n' + json.dumps(blueprint, ensure_ascii=False)
            prompt += '\n【只写本章】\n' + json.dumps(chapter, ensure_ascii=False) + '\n' + sources
            request(f"chapter-{chapter['id']:02d}-{args.attempt}", prompt)
            print('Completed chapter', chapter['id'], flush=True)
        return
    chapters = [json.loads((GEN / f"chapter-{c['id']:02d}-{args.attempt}.json").read_text()) for c in blueprint['sections']]
    book = {'title': blueprint['title'], 'sections': chapters}
    save(GEN / 'book-draft.json', book)
    figures = json.loads((ROOT / 'assets/figures.json').read_text())
    prompt = '''你是这份讲义的作者，通读完整初稿及节目来源，做一次整篇编辑：统一术语，消除重复和机械措辞，补齐关键案例，连接各章。保留嘉宾分歧、条件和具体内容，不添泛化免责声明。正文不是制作日志。
返回完整JSON：{"lead":"300字导读","conclusion":"400字总结与延伸，包含嘉宾结尾的激励及持续研发讨论","edits":[{"path":"/sections/0/units/0/paragraphs/0","new":"该字符串字段完整替换值"}],"figures":[{"id":"提供的图ID","path":"提供的path","caption":"图标题；依据节目口述整理；时间","before":"80字解释本图回答什么并承接正文","reading":"140字沿实际箭头/行列讲清含义和关系","after":"60字联系下一步"}],"editor_note":"简述修改"}。
edits只替换现有字符串叶节点，不改数组结构；索引从0开始，同一路径只改一次。改动少则不凑数量。六张图按章节顺序全部返回；严格依据图说明和实际节点，不猜数值。定义易懂，段落连贯，适量列表和强调，保留读者理解所需细节。'''
    prompt += '\n【初稿】\n' + json.dumps(book, ensure_ascii=False)
    prompt += '\n【配图】\n' + json.dumps(figures, ensure_ascii=False)
    prompt += '\n【具体复核意见，请逐处落实】\n' + (GEN / 'review-notes.md').read_text()
    prompt += '\n【蓝图】\n' + json.dumps(blueprint, ensure_ascii=False) + '\n' + sources
    result = request('editorial-' + args.attempt, prompt)
    seen = set()
    for edit in result['edits']:
        if edit['path'] in seen:
            raise ValueError('Duplicate edit path: ' + edit['path'])
        seen.add(edit['path'])
        parts = edit['path'].strip('/').split('/')
        node = book
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        key = int(parts[-1]) if isinstance(node, list) else parts[-1]
        if not isinstance(node[key], str) or not isinstance(edit['new'], str):
            raise ValueError('Expected a string edit')
        node[key] = edit['new']
    book.update(lead=result['lead'], conclusion=result['conclusion'])
    # The editorial pass rewrites the final comparison into three columns.
    table = book['sections'][-1]['table']
    table['headers'] = table['headers'][:3]
    table['rows'] = [row[:3] for row in table['rows']]
    by_id = {f['id']: f for f in result['figures']}
    for chapter, figure in zip(book['sections'], figures):
        chapter['figure'] = by_id[figure['id']]
    book['references'] = [
        {'title':'硅谷101：原节目','url':'https://www.bilibili.com/video/BV1imaq6mEof/'},
        {'title':"Humanity's Last Exam 官方仓库",'url':'https://github.com/centerforaisafety/hle'},
        {'title':'Terminal-Bench 官方仓库','url':'https://github.com/laude-institute/terminal-bench'}]
    save(GEN / 'book.json', book)
    print('Whole-document edit complete:', len(result['edits']), 'changes', flush=True)


if __name__ == '__main__':
    main()

"""Build source-complete chapter prompts and call the shared Argon writer."""
import concurrent.futures
import argparse
import importlib.util
import json
from pathlib import Path

episode = Path(__file__).resolve().parent.parent
repo = episode.parents[2]
spec = importlib.util.spec_from_file_location('argon_write', repo / 'tools/scripts/argon_write.py')
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
blueprint = json.loads((episode / 'generation/accepted-blueprint.json').read_text())
source_names = ['transcript-reading.md', 'editorial-checks.md', 'terminology-check.md', 'digest-00-35.md', 'digest-35-80.md']
source_text = '\n\n'.join('【'+name+'】\n'+(episode/'sources'/name).read_text() for name in source_names)

instruction = '''你正在写一份可独立学习的中文访谈笔记。这次只写指定一章。正文由你撰写；Codex已精读资料并给出核定蓝图。按蓝图标题和小节组织，原始plan.json不作为输入。
以真实口述中的问题、尝试、例子、纠正和观点联系为主线。写自然、清楚的教学文章，不写逐页PPT解说，不写审计报告。先明确人物归属，随后流畅解释。人物意见不能变成普遍事实，模型内部机制不能由访谈猜测变成确定陈述。不要用“颠覆、绝对、必然、终局、暴涨、完美、彻底解决”等夸大词替代实际机制。
不要反复写“这不代表/不能证明/仅供参考/必须谨慎”等防御性套话。将影响结论的条件直接写到例子或定义中，不要每段末尾加免责声明。每个重要案例讲清前因、操作或尝试、观察结果、为什么改变下一步。不要把抽象总结当作案例解释。
整章约1800到2400中文字符的教学内容，不包含JSON键，随材料密度调整，不为字数重复。每个小节有2到4个正常段落，首段先接上前文并提出问题。首次使用缩写或术语就定义。定义、并列观点、步骤可用短列表与**重点短语**，但连续推理保持段落。列表单独占一个paragraph字符串，用真实换行。数字保留单位、对象、时间/场景，避免将预测写成现状。不同观察范围的金额不拼算。
输出一个完整JSON对象：
{"title":"核定章节标题","intro":"100到160字承上启下","units":[{"title":"核定小节标题","paragraphs":["段落","段落"]}],"boxes":[{"kind":"importantbox或knowledgebox或warningbox","title":"具体教学标题","text":"80到150字机制解释，可有列表"}],"table":{"caption":"术语/机制对照","headers":["术语或场景","解决什么问题","理解要点"],"rows":[["短语","具体问题","简洁机制"]]},"figure":null,"summary":"100到160字，3条分点或自然总结"}
每章2个有实际内容的框，定义和直觉优先，warningbox只有具体常见混淆时使用。表格3到5行，单元格不堆长段。不要编造参考链接、实验、代码、公式和直接引语。图由Codex另绘，figure设null，后续整体编辑时配读图说明。
读者关心内容，正文不夹入“本次来源核对/ASR/写作流程”等制作说明。在具体案例处自然标1到3个来源时间范围，精确到分钟和秒。长标题可读，不在标题堆5个名词。
'''


def chapter(section, attempt):
    prefix = episode/'generation'/f"chapter-{section['id']:02d}-{attempt}"
    if prefix.with_suffix('.json').exists():
        return str(prefix)+': already complete'
    prompt = instruction+'\n【整篇核定蓝图】\n'+json.dumps(blueprint,ensure_ascii=False)+'\n【本次章节】\n'+json.dumps(section,ensure_ascii=False)+'\n'+source_text
    input_path = Path(str(prefix)+'-input.txt')
    input_path.write_text(prompt)
    return writer.request(input_path, prefix, sources=[episode/'sources'/name for name in source_names])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--attempt', required=True)
    parser.add_argument('--chapters', nargs='+', type=int, default=list(range(1, 8)))
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(chapter, section, args.attempt): section['id'] for section in blueprint['sections'] if section['id'] in args.chapters}
        for future in concurrent.futures.as_completed(jobs):
            future.result()
            print('Completed chapter', jobs[future], flush=True)

"""Provide complete transcript and a teaching blueprint to Argon."""
import argparse
import importlib.util
import json
from pathlib import Path

episode=Path(__file__).resolve().parent.parent
repo=episode.parents[2]
spec=importlib.util.spec_from_file_location('argon_write',repo/'tools/scripts/argon_write.py')
writer=importlib.util.module_from_spec(spec);spec.loader.exec_module(writer)
blueprint=json.loads((episode/'generation/blueprint.json').read_text())
source_text='\n\n'.join('【'+name+'】\n'+(episode/'sources'/name).read_text() for name in ['transcript-reading.md','source-guide.md','autoresearch.md','opro.md'])

instruction='''你是这份中文访谈学习讲义的作者 Argon。根据完整转录与蓝图，写本次指定章节。讲清真实问题、例子、因果关系、技术条件，读者不看视频也能学懂。每章约1800–2300中文字符（可按密度调整），3小节各2–4段，首段承接前节并引出本节问题。不要重复预告片；跳过问候广告。自然段讲推理，比较放表格，并列要点可分点与**重点短语**，不机械把每段都写成列表。
人名术语按source-guide修正；职位按简介。预测与企业自述保留归属，日期2026-07-06；半年仅跑通后训练单环，不能变成已实现持续RSI。少用“不是A而是B”，不要防御性套话或审计口吻。先把改变理解的条件说清就够。官方README是延伸材料，不要冒充现场原话。不要把抽象理论当成节目做过的实验。不编造引语、公式、数据、来源或具体案例结果。术语首次定义，密集术语表消化。可用“实践经验”“讲者强调”标明具体口述经验，每章至少一个真实案例深入解释并在相关处标时间范围。
输出严格JSON对象：{"title":"蓝图章标题","intro":"80–140字","units":[{"title":"蓝图小节标题","paragraphs":["完整段落","完整段落"]}],"boxes":[{"kind":"importantbox或knowledgebox或warningbox","title":"具体机制","text":"80–140字"}],"table":{"caption":"具体比较主题","headers":["术语或对象","作用","如何理解"],"rows":[["短语","具体作用","机制解释"]]},"figure":null,"summary":"100字左右总结"}。
每章两个有内容的框，定义与背景优先，warningbox只用于具体误区。表格3–5行短句，不堆长段。图后续由Codex绘制与Argon编辑配文。'''

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--attempt',default='01');p.add_argument('--chapters',nargs='+',type=int,default=list(range(1,8)));a=p.parse_args()
    for section in blueprint['sections']:
        if section['id'] not in a.chapters:continue
        prefix=episode/'generation'/f"chapter-{section['id']:02d}-{a.attempt}"
        if prefix.with_suffix('.json').exists():continue
        path=Path(str(prefix)+'-input.txt')
        path.write_text(instruction+'\n【整篇蓝图】\n'+json.dumps(blueprint,ensure_ascii=False)+'\n【本次章节】\n'+json.dumps(section,ensure_ascii=False)+'\n'+source_text)
        writer.request(path,prefix)
        print('Completed chapter',section['id'],flush=True)

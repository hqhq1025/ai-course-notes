"""Ask the author to align figure prose with the actual rendered SVG nodes."""
import json
import sys
from pathlib import Path
from write_chapters import episode, writer, source_text

folder=episode/'generation'
if sys.argv[1]=='request':
    book=json.loads((folder/'book.json').read_text())
    prompt='''请对已完成全文编辑的学习笔记做一次局部准确性修正。必须看实际SVG的文字和坐标，不能根据主题想象不存在的分支。七图全部只有横向四个方框：learning-loop和reverse-learning有从最右回到最左的底部虚线；university-value与ability-check四栏并列无箭头；其余三图横向单链，无上下分支。原来的读图描述错误地增添了分支、记忆栏、上下对比，并把一些节点顺序调错。
请按实际标签写七图reading，必要时一起修正before和after。图旁说明可以连接源案例，但只有SVG出现的文字和关系才能说“图中/上方/下方/第几栏”。大学价值顺序是学科基础、同辈与导师、自我认识、学历信号。能力自查顺序是能解释、能判断、能迁移、能接续。工具图是表达意图、探索问题、执行任务、检查交付。整项任务图为准备与检索、生成与实现、验证与返工、最终交付。保持自然教学口吻，不写审计报告，不补泛化免责声明。
同时返回两处事实修订的作者文字：第5章第1框，原稿把进度文档说成无缝24小时接力，还编造每次子功能结束自动更新等步骤；实际口述只是Alfred持续维护task/progress.md，当Claude Code挂了或配额用完交给Codex继续。按此写约100字，不增加未说过的步骤或保证。第7章第2框，官方METR摘要说16位有多年经验的开发者、熟悉自身仓库、246任务；不保留“所有人至少5年”的未核实阈值，保留19%实际慢与20%主观快，无新手对照组。
输出完整JSON：{"figures":[{"id":"实际ID","before":"承接正文","reading":"120到170字实际读图","after":"连接下一段"}],"boxes":[{"section":5,"index":0,"title":"...","text":"..."},{"section":7,"index":1,"title":"...","text":"..."}]}。section从1开始，index从0开始。只处理这些局部，不修改其余章节。不需要重复图路径和图注。
'''
    prompt+='\n【当前完整讲义】\n'+json.dumps(book,ensure_ascii=False)
    for p in sorted((episode/'assets').glob('*.svg')):prompt+='\n【实际图 '+p.name+'】\n'+p.read_text()
    prompt+='\n【完整来源】\n'+source_text
    inp=folder/'editorial-figure-fix-input.txt';inp.write_text(prompt)
    writer.request(inp,folder/'editorial-figure-fix')
else:
    book=json.loads((folder/'book.json').read_text());fix=json.loads((folder/'editorial-figure-fix.json').read_text())
    byid={f['id']:f for f in fix['figures']}
    for section in book['sections']:
        f=section['figure'];e=byid[f['id']]
        for k in ['before','reading','after']:f[k]=e[k]
    for box in fix['boxes']:
        target=book['sections'][box['section']-1]['boxes'][box['index']]
        for k in ['title','text']:target[k]=box[k]
    (folder/'book.json').write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n')
    print('Applied figure-aligned explanations and two source corrections')

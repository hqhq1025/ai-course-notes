"""Assemble chapter drafts and request a source-informed whole-document edit."""
import argparse
import json
from pathlib import Path

from write_chapters import blueprint, episode, source_text, writer


def save(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['request','apply'])
    parser.add_argument('--edit',default='editorial-v1')
    args=parser.parse_args()
    folder=episode/'generation'
    if args.action=='request':
        book={'title':blueprint['title'],'sections':[json.loads((folder/f'chapter-{i:02d}-v1.json').read_text()) for i in range(1,8)]}
        save(folder/'book-draft.json',book)
        prompt='''你是这份学习笔记的作者和最终主编。请通读完整七章初稿及完整转录，完成全文润色与必要纠错。保留三位嘉宾各自的经历、主张和分歧，不把圆桌变成一个人的观点。清理重复定义、泛化防御句、频繁“不是A而是B”句式，连接七章推理，维持以自然段讲解、列表和表格帮助比较的节奏。
请务必落实来源与蓝图中的编校要点：99%是Jack对个人作业AI参与的估计，非全代写；录制2026年2月、发布2026年5月15日；模拟专家团不是真专家发言；METR未测新手对照组、不从19%和20%算精确40%差距；术语中文首用解释；产品评价只保留当时任务与个人体验，不给当前排名及优惠保证；模型用户记忆不是训练权重变化。依恋类型影响AI关系是Kolento的研究问题，不是已有证实结果。正文保留泓君对深度理解的异议、Alfred公开课+项目复盘+法律手写考试、Kolento反向学习两路验证、Jack有无AI仍能写代码的经历、记者转录同步思考、主持人末尾高中生后记。
为全篇写约300字导读、约400字总结与延伸。为七图分别写before 80到120字、reading 120到170字、after 50到90字，讲清箭头或并列关系，嵌入论证，不重复前面定义。图注带提供的时间范围与“依据节目口述整理”；自我检查四问题是整理而非实验量表。无需虚构公式、数据、引语和新网址。
输出单个完整JSON：{"lead":"...","conclusion":"...","edits":[{"path":"/sections/0/units/0/paragraphs/0","new":"该字符串字段的完整替换文本"}],"figures":[{"id":"图ID","path":"assets/图ID.pdf","caption":"图标题、时间、来源","before":"...","reading":"...","after":"..."}],"editor_note":"完成了哪些实质改进"}。
只修改确有问题的字符串叶节点；不改变章节标题、JSON结构和图ID。edits可以替换整段、表格单元格、小结；不要为凑数量重写正确文本。figures必须包含七图，正文应通读完整七章。不要返回其他字段或markdown围栏。
'''
        prompt+='\n【全篇初稿】\n'+json.dumps(book,ensure_ascii=False)
        prompt+='\n【配图】\n'+(episode/'assets/figures.json').read_text()
        prompt+='\n【核定蓝图】\n'+json.dumps(blueprint,ensure_ascii=False)
        prompt+='\n【初稿复核】\n'+(folder/'review-findings.md').read_text()
        prompt+='\n【完整来源】\n'+source_text
        prompt+='\n【METR官方补充原文】\n'+(episode/'sources/metr-study.txt').read_text()
        path=folder/(args.edit+'-input.txt');path.write_text(prompt)
        writer.request(path,folder/args.edit)
        return
    book=json.loads((folder/'book-draft.json').read_text())
    result=json.loads((folder/(args.edit+'.json')).read_text())
    seen=set()
    for edit in result['edits']:
        if edit['path'] in seen:raise ValueError('Duplicate path '+edit['path'])
        seen.add(edit['path']);parts=edit['path'].strip('/').split('/');node=book
        for part in parts[:-1]:node=node[int(part)] if isinstance(node,list) else node[part]
        key=int(parts[-1]) if isinstance(node,list) else parts[-1]
        if not isinstance(node[key],str):raise ValueError('Expected text field')
        node[key]=edit['new']
    book['lead']=result['lead'];book['conclusion']=result['conclusion']
    figures={f['id']:f for f in result['figures']}
    for section,plan in zip(book['sections'],blueprint['sections']):section['figure']=figures[plan['figure']]
    book['references']=[{'title':'硅谷101：完整节目','url':'https://www.bilibili.com/video/BV1zD5a6bEoY/'},
      {'title':'METR：2025年早期AI对资深开源开发者生产率的研究','url':'https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/'}]
    save(folder/'book.json',book)
    save(folder/'editorial-applied.json',{'model':writer.MODEL,'edits':len(seen),'editor_note':result['editor_note']})
    print('Applied',len(seen),'edits and seven figure explanations')


if __name__=='__main__':main()

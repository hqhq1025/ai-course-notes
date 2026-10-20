"""Ask Argon to edit the complete draft, then apply its string replacements."""
import argparse
import copy
import json
from pathlib import Path
from write_chapters import blueprint,episode,source_text,writer

folder=episode/'generation'
def save(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['request','apply']);p.add_argument('--attempt',default='01');a=p.parse_args()
    prefix=folder/('editorial-'+a.attempt)
    if a.action=='request':
        book={'title':blueprint['title'],'sections':[json.loads((folder/f'chapter-{i:02d}-01.json').read_text()) for i in range(1,8)]}
        save(folder/'book-draft.json',book)
        figures=json.loads((episode/'assets/figures.json').read_text())
        prompt='''你是这份讲义的作者及主编 Argon。通读完整初稿、完整转录、蓝图和配图说明，完成全文语言编辑与内容核对。正文要连贯、自然、易学，删掉章节间机械重复定义，保留具体节目例子和论证。不用重复免责声明，少用不是A而是B。半年的预测必须归属李辈滨、2026-07-06节目中的后训练单环；持续递归仍需处理漂移。数字归属、代码/模型训练/脚手架不同改进对象、科学发现与验证均应清楚。纠正无依据的细节或引语。不要在成稿写ASR、核对、编写流程等制作说明。注意整篇不能省略节目的结尾价值观追问。
输出JSON：{"lead":"250–350字导读","conclusion":"350–500字总结与延伸，保留少数科学家塑造AI与大众价值观的问题","edits":[{"path":"/sections/0/units/0/paragraphs/0","new":"完整替换字符串"}],"figures":[{"id":"配图id","path":"配图path","caption":"标题＋来源时间＋依据口述整理","before":"80–100字从本章引出图的问题","reading":"120–160字读图，解释箭头或并列关系及教学含义","after":"60–90字连接后续讨论"}],"editor_note":"简述实际编辑"}。edits只修改已有字符串叶节点，列表下标从0开始，只给需要改的字符串，不改结构；修复所有相关重复出现处。七张图每张一个对象，图不是实验数据。保持图中实际箭头与文字一致。无需凑编辑数。'''
        prompt+='\n【完整初稿】\n'+json.dumps(book,ensure_ascii=False)+'\n【蓝图】\n'+json.dumps(blueprint,ensure_ascii=False)+'\n【图】\n'+json.dumps(figures,ensure_ascii=False)+'\n【完整来源】\n'+source_text
        review=folder/'review-notes.md'
        if review.exists():prompt+='\n【需修正】\n'+review.read_text()
        path=Path(str(prefix)+'-input.txt');path.write_text(prompt);writer.request(path,prefix)
    else:
        book=copy.deepcopy(json.loads((folder/'book-draft.json').read_text()));response=json.loads(prefix.with_suffix('.json').read_text());seen=set()
        for edit in response['edits']:
            assert edit['path'] not in seen;seen.add(edit['path']);parts=edit['path'].strip('/').split('/');node=book
            for part in parts[:-1]:node=node[int(part)] if isinstance(node,list) else node[part]
            key=int(parts[-1]) if isinstance(node,list) else parts[-1]
            assert isinstance(node[key],str) and isinstance(edit['new'],str);node[key]=edit['new']
        book['lead']=response['lead'];book['conclusion']=response['conclusion']
        figures={f['id']:f for f in response['figures']}
        for section,plan in zip(book['sections'],blueprint['sections']):section['figure']=figures[plan['figure']]
        book['references']=[{'title':'硅谷101：本期完整节目','url':'https://www.bilibili.com/video/BV1sAT16WEYg/'},{'title':'Karpathy autoresearch：训练实验的自动迭代','url':'https://github.com/karpathy/autoresearch'},{'title':'Google DeepMind OPRO：语言模型作为优化器','url':'https://github.com/google-deepmind/opro'}]
        save(folder/'book.json',book);print('Applied',len(seen),'editorial changes')

"""Align the final explanations with the diagrams actually drawn."""
import json
from write_chapters import episode,source_text,writer

folder=episode/'generation'
book=json.loads((folder/'book.json').read_text())
diagrams='\n'.join(p.read_text() for p in sorted((episode/'assets').glob('*.svg')))
prompt='''请对这份你刚刚编辑的学习讲义做最后一轮具体修改，返回JSON {"edits":[{"path":"/sections/0/figure/reading","new":"完整替换字符串"}]}，只改现有字符串叶节点，不改结构，不返回全文。修改任务如下：
1. 最重要：逐张阅读提供的实际SVG。之前你写的图说明虚构了没有画出的结构，例如第3图“通过并采纳”、第4图左右脚双向箭头/两侧虚线、第6图并列A/B问题，都是错的。所有figure.reading必须严格对应SVG里的实际标签、箭头和布局，不描述不存在的节点。第1图现在明确是诊断薄弱能力→构造训练任务→执行训练→验证效果→回流。第3图回流到候选解法。第4图就是4节点顺序循环，不是两脚结构图。图说明只解释实际画面再联系正文。
2. 每张图位于本章小结前，after应衔接下一章，不要说接下来讨论本章已经讨论过的事。末章figure.after移向总结和研究判断，删除英文examine。
3. 精确改掉第6章boxes/0/text中“模型宪法（Constitutional AI）”为“模型宪法（Constitution）”，避免成文原则与训练方法名混淆。
4. 第7章units/2/paragraphs/0删除“当早期GPT-3相关技术被放进GitHub Copilot时”技术平台猜测，只说他2021年体验早期GitHub Copilot。第7章units/1/paragraphs/1成本后不写未核实疏水性，只写其它材料性能。
5. 第2章units/0/paragraphs/1明说扩窗条件是讲义的技术解释，后面才归属嘉宾百万例子，别把位置编码硬件补充冒充原话。第2章units/1/paragraphs/1重要复杂度放展示公式，并紧接解释n是词元数，计算范围标准稠密全序列注意力；避免推理每一步皆二次的误会。
6. 总结conclusion里“任何一侧微调都要求另一侧同步适应”过强，改为模型行为改变后应重新检查脚手架匹配；开放问题可以采用分工验证，不一概必须所有工具都用。不要写泛化免责声明。
只返回本轮必要的完整字符串替换；不改其它正确内容。'''
prompt+='\n【当前全文】\n'+json.dumps(book,ensure_ascii=False)+'\n【实际SVG】\n'+diagrams+'\n【完整来源】\n'+source_text
path=folder/'figure-edit-01-input.txt';path.write_text(prompt)
r=writer.request(path,folder/'figure-edit-01')
for edit in r['edits']:
    parts=edit['path'].strip('/').split('/');node=book
    for part in parts[:-1]:node=node[int(part)] if isinstance(node,list) else node[part]
    key=int(parts[-1]) if isinstance(node,list) else parts[-1]
    assert isinstance(node[key],str) and isinstance(edit['new'],str);node[key]=edit['new']
(folder/'book.json').write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n')
print('Applied',len(r['edits']),'diagram and factual corrections')

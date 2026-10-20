"""Ask Argon to edit the complete book, then render its saved string edits."""
import argparse
import json
from pathlib import Path
from write_chapters import episode, blueprint, source_text, writer

folder = episode / 'generation'

def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['request', 'apply'])
    parser.add_argument('--prefix', default='editorial-01')
    args = parser.parse_args()
    prefix = folder / args.prefix
    if args.action == 'request':
        sections = [json.loads((folder / f'chapter-{i:02d}-01.json').read_text()) for i in range(1, 8)]
        book = {'title': blueprint['title'], 'sections': sections}
        save(folder / 'book-draft.json', book)
        figures = json.loads((episode / 'assets/figures.json').read_text())
        prompt = '''你是本书作者，现在通读整篇初稿、完整转录和配图，完成全文编辑。统一术语、改善衔接、删除重复定义与防御性套话，保留真实案例和发言归属。读者学习的是机制和具体业务选择。
输出JSON：{"lead":"约250字导读","conclusion":"约400字总结与延伸","figures":[{"id":"配图id","path":"配图path","caption":"图标题，依据节目口述整理，时间范围","before":"80字左右，从本章论证引出图","reading":"120字左右，按图中箭头、行列和颜色讲解机制","after":"60字左右接下一个问题"}],"edits":[{"path":"/sections/0/units/0/paragraphs/0","new":"完整替换字符串"}],"editor_note":"实际完成的改进"}。
为全部七张图提供解释。edits只修改初稿中已有的字符串叶节点，路径中的列表从0开始；可以完整替换段落、表格单元格、小结，不能新建路径或更改结构。返回必要修改即可，不凑数。必须整篇阅读后纠正跨章重复和矛盾。
复核重点：APP点咖啡为节目体验，眼镜为讨论情景；两周自主Agent为期待。Qwen3-Next-80B-A3B的80B总参数与3B激活分开。MTP是多token预测，不与MoE混同；TTFT首包时延、生成TPS、总吞吐不混同。360度理解和剪辑不自动等于世界模型。RAG需读者能理解，企业清洗、规则、复审都不可省。高端家电是2024开始、合作约一年半后销量涨23%、客单价涨6点几%，为嘉宾客户观察，不写成单独归因AI实验；语义识别不是语音识别。行业中间层有垂直模型、业务知识与落地经验，不只是API转售。尾声license加用量包、企业决策和竞争力必须保留。
具体初稿复核：第1章“高维度身份特征向量、强约束注入扩散过程”属于原节目未提供的内部机制猜测，必须改为输入参考视频帮助后续角色外貌和声音保持一致，不能假装知道实现。全篇避免“终结抽卡”“问题得到解决”“完美”“质变”“工业级跃迁”等绝对化表述；用可控性提高及实际筛选修改流程解释。短剧成本2万元口径源文再核对；背景比例、体型比例、光影控制等若原文未陈述就删除多余精确细节。第1章小结不可写成有统一盈利保证。
第2章必须修正：不要说推理模型“不再依赖概率接龙”，推理增强并不改变生成模型的概率基础；不要贬称工作流死板、僵化，其确定性业务节点仍有价值。o1首次发布是2024年9月，写“2024年下半年”即可。端侧模型名称、4B具体参数、100B比较在转录不清楚，全部从正文、表格、小结删掉这些精确型号数字，改为轻量化端侧模型及嘉宾认为能力提高。原文不能支持特定Qwen-Omni 4B型号。去掉“毫秒级响应”等未给定性能指标。Memory只是偏好记忆功能，不写成已验证内部实现；Skills与MCP不能混成同一个接口规范，前者组织任务知识/流程，后者约定工具与数据接入。长上下文容量不保证精准召回，代码能力不等于模型自行拥有执行权限。七成比例放在归属明确的嘉宾判断，勿在表格和小结重复成事实指标。
第3章必须修正：删掉 Qwen3-Next 的“2025年底发布”具体日期，讲型号即可。MoE 总参数增加模型容量但不保证知识或理解上限，少激活参数减少计算但不等于同激活参数稠密小模型的全部内存和服务成本，路由、通信、权重驻留仍有开销；表格和框中的“保障/保证”一并修正。MTP可以用于推测解码候选预测，需要验证接受，不能写成单次前向直接保证多token输出或TPS成倍。首包缩短、TPS提升是嘉宾对改进趋势的举例，不当实测保证。谷歌成本十分之一是主持人口述比较、没有同任务条件，删数值只讲软硬协同路径。利用率30%到50%是低利用率举例，不是调度前后实测；小结不可说实际从30%提升。影石十几元具体组成未公开，删除“包含多模态理解与管线综合开销”等推定，只保留该任务的口述成本量级。两个成本警告框重复太多，请把第3章那个已有框改写为一个具体小模型选型机制框（kind仍保留原枚举若不改结构）。
第4章必须修正：32B单卡部署取决于显存、权重精度、上下文与并发，不能说“恰好单张主流显卡完整跑起来”。可在该knowledgebox明确32B FP16权重约64GB（32e9乘2字节，只是权重），量化会降低权重空间，KV缓存等仍需显存；这是教学算例不是节目测试。正文、表格、小结里单卡措辞同时加条件或删重复。开源不等于任意用途无限制，按具体许可证；这里无需展开法律说明。API是交付方式，不必然闭源，可以托管开源模型；MaaS并不保证最新或高并发，要看实际服务。Qwen3-Max参数规模不能从节目推断已公开，只说当时旗舰模型和部署成本判断。研发投入与DeepSeek生态效应保留徐栋观点，不变成所有公司的统计。
第5章修正：第一小节“前端千问直接提取高光”与第二小节的自研全景理解分工矛盾，统一为自研模型负责全景理解/高光、通用模型处理平面内容编排、万相用于特效。世界模型一词可给学习用定义为环境随状态和动作变化的模型，不写成只要理解3D就是世界模型。全景等距柱状投影、FOV视窗属于背景说明，勿断言影石产品具体算法；仅凭单视点全景不能平移到新相机位置，“模拟平移、推进”改为“选择视角和调整视场”。“无需构图”改为“可在后期选择取景方向”。成本口述非综合开销证明，删括号式免责声明但在该段自然说明环节未细分。输入压缩“严格保证不丢失”“极高”“大幅”改成保留关键事件作为优化条件，说明筛减后还要看高光召回和成片，不编保证。
第6章修正：人口标签与购买兴趣“没有直接关联”太绝对，改成不能单独回答具体产品使用需求。不到70%的案例原因原文没有拆解，不得编成“缺乏微调/未清洗/未拆流程导致”，在框中仅说这是所接触客户直接调用案例，后续需要本行业评测定位错例。RAG不是微调训练，知识库清洗有助于检索但不保证准确或必须依赖大模型，清洗与模型训练区别讲清。删“必然漏洞百出”“才能保证”“实际准确率显著提升”等无数据保证。小结不能说只要组合这些措施“才能超越人工”，保留吕瀛杰对单点问答的经验判断。退货六到一归属案例，人工复审不是无误保证。全书每章框都大段“切勿/需严格区分”很机械，请将框标题改为具体教学问题或机制，正文把条件融入自然解释，保留少数实际误区即可。
第7章修正：六到一是该流程所需人数变化，不能推定实际裁撤编制。销量23%与客单价6点几%为嘉宾合作后客户观察，不能写成AI单独拉动的因果证据；“逆势”没有市场对照依据。语忆100%增长是公司自报，不能据此证明特定计费模式导致增长。License原文按SaaS版本，未说按账号，不要补计价细则。“只有增长才值得投AI”太绝对，降本项目也能有价值，讲两种评价尺度即可。订阅/用量包是该公司选择，不写所有应用商不能按token收费。请全篇消除“只要...保证”“必然”“证明商业闭环”等因果跃迁，条件直接放在相关句子，勿新加免责声明段。
不要在正文出现来源审计、写作流程等制作术语；ASR若用于解释语音模型功能可以正常定义。不要禁止视频生成中的提示词这一业务术语。不编新数据或直接引语。自然使用必要列表、重点与表格。
'''
        prompt += '\n【完整初稿】\n' + json.dumps(book, ensure_ascii=False)
        prompt += '\n【全部配图】\n' + json.dumps(figures, ensure_ascii=False)
        prompt += '\n【蓝图】\n' + json.dumps(blueprint, ensure_ascii=False)
        prompt += '\n【完整转录与来源】\n' + source_text
        path = Path(str(prefix) + '-input.txt')
        path.write_text(prompt)
        writer.request(path, prefix)
    else:
        book = json.loads((folder / 'book-draft.json').read_text())
        response = json.loads(prefix.with_suffix('.json').read_text())
        seen = set()
        for edit in response['edits']:
            if edit['path'] in seen:
                raise ValueError('Duplicate edit path')
            seen.add(edit['path'])
            node = book
            parts = edit['path'].strip('/').split('/')
            for part in parts[:-1]:
                node = node[int(part)] if isinstance(node, list) else node[part]
            key = int(parts[-1]) if isinstance(node, list) else parts[-1]
            if not isinstance(node[key], str) or not isinstance(edit['new'], str):
                raise ValueError('Expected existing text field')
            node[key] = edit['new']
        book['lead'], book['conclusion'] = response['lead'], response['conclusion']
        figures = {f['id']: f for f in response['figures']}
        for section, plan in zip(book['sections'], blueprint['sections']):
            section['figure'] = figures[plan['figure']]
        book['references'] = [
            {'title': '硅谷101：本期完整节目', 'url': 'https://www.bilibili.com/video/BV1cZ6qB6EMk/'},
            {'title': 'Qwen3 官方模型说明与开源资源', 'url': 'https://github.com/QwenLM/Qwen3'}]
        save(folder / 'book.json', book)
        print('Applied', len(seen), 'whole-document edits')

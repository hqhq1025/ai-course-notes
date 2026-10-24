"""Render source-grounded KV-cache and research mechanisms."""
import json
from diagram_base import Diagram, FIGURES, ROOT, convert

def chain(d,labels,y=110):
    nodes=[d.box(35+i*240,y,210,lines,['blue','purple','orange','green'][i]) for i,lines in enumerate(labels)]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    return nodes

def diagrams():
    d=Diagram('question-discovery','寻找问题：历史线索与一线观察',445,'00:54:35–01:02:16','两种输入进入同一个判断过程：历史告诉我们哪些约束曾重要，一线观察告诉我们哪些约束正在变化；小规模探索检验问题是否成立。')
    d.box(60,95,380,['技术史与经典论文','当时约束／解决方式'],'blue');d.box(560,95,380,['真实系统与工程工作','现在瓶颈／需求变化'],'green')
    d.path('M250,207 L250,252 L490,252');d.path('M750,207 L750,252 L510,252')
    d.box(205,280,590,['提出问题 → 小规模探索 → 修正判断'],'purple');d.text(500,422,'导师提供方向和反馈，学生保留探索与解决问题的空间',21);d.save()

    d=Diagram('streaming-observation','视频体验是整条传输链的结果',460,'00:26:18–00:39:54；00:47:13–00:53:56','上行展示服务到用户的传输路径。播放器上报的体验指标汇集成大规模观测，帮助分析网络和服务质量，观测相关性不自动定位唯一故障。')
    chain(d,[['内容服务与编码','准备视频片段'],['CDN 节点','靠近用户缓存'],['网络传输','带宽与拥塞'],['用户播放器','缓冲／解码／显示']])
    d.box(185,315,630,['播放观测汇总：清晰度／卡顿／起播等待'],'purple')
    d.path('M865,225 L865,350 L828,350');d.path('M175,350 L140,350 L140,225')
    d.text(500,438,'把体验数据用于发现共同问题和选择优化位置',22);d.save()

    d=Diagram('prefill-reuse','相同上下文：重算还是加载已有 KV',485,'01:24:37–01:29:42；01:31:52–01:34:24','上行首次读取长文档，prefill生成KV缓存；下行后续请求在兼容同前缀时加载缓存，再处理新增问题并解码。缓存减少部分重算，加载和存储仍占用资源。')
    chain(d,[['首次：文档＋问题','输入 token'],['Prefill','计算 K、V 张量'],['Decode','逐步生成回答'],['保存可复用 KV','准备后续加载']],100)
    chain(d,[['后续：同文档','新的问题'],['加载前缀 KV','兼容模型与位置'],['处理新增 token','继续生成'],['本次回答','任务结果']],300)
    d.path('M865,215 L865,257 L380,257 L380,288');d.text(500,466,'示意比较不表示固定的节省比例',21);d.save()

    d=Diagram('cache-layer','LMCache 连接推理引擎与存储层',485,'01:15:59–01:21:03；01:37:28–01:40:55','上方不同推理引擎经过连接器进入缓存管理层，再接下方不同存储介质。旁注压缩与片段复用是不同能力；共享接口不消除模型兼容要求。')
    d.box(65,90,370,['推理引擎 A','加载／保存 KV'],'blue');d.box(565,90,370,['推理引擎 B','加载／保存 KV'],'blue')
    d.path('M250,203 L250,228');d.path('M750,203 L750,228')
    d.box(95,245,810,['LMCache：缓存管理、传输与连接器'],'purple')
    for x,lines in [(40,['CPU 内存']),(365,['本地 SSD']),(690,['远程存储'])]:
        d.path(f'M{x+135},324 L{x+135},353');d.box(x,370,270,lines,'green',h=64)
    d.text(500,470,'CacheGen：压缩传输；CacheBlend：选择性重算后的片段复用',20);d.save()

    d=Diagram('memory-paths','改进模型行为的三条互补路径',445,'01:41:55–01:49:22','三列分别改变权重、上下文和推理中间状态。缓存管理能节约重算；更深的内部状态优化需结合任务质量检验，不等于永久训练。')
    for x,title,lines,c in [(40,'训练模型',['改变模型权重','训练数据与优化'],'blue'),(365,'组织上下文',['选择输入内容','检索／提示／历史'],'purple'),(690,'管理内部状态',['保存与复用 KV','研究选择和优化'],'green')]:
        d.text(x+135,110,title,26);d.box(x,142,270,lines,c,h=118);d.path(f'M{x+135},268 L{x+135},312')
    d.box(150,325,700,['共同目标：任务效果、效率与适合当前问题的行为'],'orange');d.save()

    d=Diagram('team-decisions','从研究协作到平等的公司决策',440,'01:50:54–02:04:35','左侧提出机会和方向，右侧提供实现约束，中间通过信任形成阶段行动。底部用客户反馈与进展代替等待论文截止日。')
    d.box(45,95,350,['方向与需求判断','为什么值得做'],'blue');d.box(605,95,350,['技术与执行判断','现在能做到哪一步'],'green')
    d.path('M405,148 L488,148');d.path('M595,180 L512,180');d.text(500,137,'共同',23);d.text(500,169,'决策',23)
    d.box(135,285,730,['阶段交付 → 用户反馈 → 调整优先级 → 下一次交付'],'purple')
    d.path('M220,215 L220,274');d.path('M780,215 L780,274');d.text(500,418,'既有师生合作带来信任；联创之间平等讨论技术反对意见',20);d.save()

    d=Diagram('stable-interface','稳定接口连接多样化的上下层',490,'02:04:35–02:12:16','上方是应用和Agent，中间是相对稳定的请求响应接口，下方有不同模型与推理后端。这个细腰是网络历史的类比，缓存数据层仍需建立自己的兼容约定。')
    for x,lines in [(45,['应用']),(365,['Agent']),(685,['开发工具'])]:d.box(x,90,270,lines,'blue',h=65);d.path(f'M{x+135},162 L{x+135},195 L500,195 L500,218')
    d.box(235,230,530,['兼容的请求与响应格式'],'purple',h=80)
    for x,lines,c in [(45,['模型与服务 A'],'green'),(365,['推理引擎 B'],'green'),(685,['硬件与平台 C'],'green')]:
        d.path(f'M500,317 L500,345 L{x+135},345 L{x+135},366');d.box(x,380,270,lines,c,h=65)
    d.text(500,474,'模块可替换仍需承担传输、调度和兼容成本',21);d.save()

if __name__=='__main__':
    import xml.etree.ElementTree as ET
    diagrams()
    for f in FIGURES:
        p=ROOT/(f['id']+'.svg');convert(p,int(ET.parse(p).getroot().get('height')))
    (ROOT/'figures.json').write_text(json.dumps(FIGURES,ensure_ascii=False,indent=2)+'\n')
    print('Rendered',len(FIGURES),'mechanism diagrams')

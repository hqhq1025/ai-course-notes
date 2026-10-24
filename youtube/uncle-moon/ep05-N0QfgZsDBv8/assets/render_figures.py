"""Editable mechanism diagrams for the two Uncle Moon interviews."""
import argparse
import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
spec=importlib.util.spec_from_file_location('diagram',REPO/'interviews/silicon-valley-101/BV1cZ6qB6EMk/assets/render_figures.py')
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)

def diagram(i,title,source,desc,height=480):
    return lib.Diagram(f'figure-{i:02d}',title,height,source,desc)

def row(d,labels,y=115):
    nodes=[d.box(35+i*245,y,210,label,['blue','purple','orange','green'][i],h=110) for i,label in enumerate(labels)]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    return nodes

def ep5():
    d=diagram(1,'潜伏的配置错误怎样在故障时暴露','00:10:26–00:19:38','上方为正常运行路径，下方为恢复路径；配置只在恢复时读取，因此故障注入和提前检查能够发现平时没有触发的错误。',500)
    d.box(45,115,240,['正常请求','未触发恢复路径'],'blue');d.box(380,115,240,['系统表面正常','错误配置潜伏'],'green');d.path('M290,170 L365,170')
    nodes=[d.box(45,300,240,['外部故障发生'],'orange'),d.box(380,300,240,['启动恢复','读取错误配置'],'purple'),d.box(715,300,240,['恢复失败','暴露配置问题'],'orange')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.path('M500,228 L500,288',True);d.text(500,464,'研究方向：在真正故障到来前，检查这些潜伏路径',23);d.save()
    d=diagram(2,'从具体故障挖到基础研究问题','00:36:09–00:53:09','上方是具体问题到基础机制的深入过程，下方是导师和同伴的反馈。图示不表示所有研究都沿同一条路线。')
    row(d,[['真实使用现场','故障／需求'],['复现与观察','理解失败条件'],['抽象机制','并发／异步'],['方案与实验','检验解释']])
    d.path('M867,232 L867,278 L140,278 L140,236');d.box(145,325,710,['导师与同伴：选问题 → 提供反馈 → 继续深入'],'green');d.save()
    d=diagram(3,'AI 运维需要完成一个恢复闭环','00:58:38–01:09:14','顺序为观察、诊断、执行和验证；底部故障环境产生重复评估任务，验证服务恢复而非只读一段诊断文字。')
    row(d,[['观察系统','告警／日志'],['形成假设','定位故障'],['执行修复','调用工具'],['验证结果','服务恢复']])
    d.path('M867,232 L867,280 L140,280 L140,236');d.box(140,325,720,['SREGym：部署系统 → 注入故障 → 评估实际恢复'],'blue');d.save()
    d=diagram(4,'形式化建模与模型检查各做什么','01:09:14–01:23:05','从程序和需求构建抽象模型与性质，再由模型检查寻找反例。结果反馈给规格和实现；安全性与活性是不同性质。',555)
    row(d,[['需求与程序','明确预期'],['抽象状态模型','定义行为'],['检查性质','探索状态'],['发现反例','修改模型／代码']],105)
    d.path('M867,224 L867,278 L380,278 L380,224');d.box(60,335,410,['Safety 安全性','坏事不发生'],'blue');d.box(530,335,410,['Liveness 活性','条件成立时最终有进展'],'green');d.text(500,522,'AI 协助建模；检查结论依赖模型、性质与假设',23);d.save()
    d=diagram(5,'把 Agent 错误转成可检测、可恢复的过程','00:19:38–00:24:12；01:23:05–01:33:00','执行前明确权限，执行中观察结果，失败时依据可恢复边界处理；Undo与Microreboot是不同粒度的恢复方式。',515)
    row(d,[['操作请求','身份与权限'],['执行动作','记录可观察结果'],['发现失败','定位影响范围'],['恢复与再验证','继续任务']],100)
    d.box(70,305,400,['Undo','回退可撤销操作'],'purple');d.box(530,305,400,['Microreboot','局部重启故障组件'],'orange');d.text(500,475,'外部副作用与依赖决定恢复边界',23);d.save()
    d=diagram(6,'生产经验怎样变成研究问题','01:33:00–01:47:21','工作现场提供具体问题，工程实现提供约束，反思把经验提炼为问题，研究再返回实践。',460)
    row(d,[['进入生产团队','询问真实困难'],['参与实际交付','理解系统约束'],['反思方案','代价与替代路径'],['形成研究问题','可验证的假设']])
    d.path('M867,232 L867,280 L140,280 L140,236');d.text(500,367,'职业选择同时看：学习内容、合作的人、生活条件',24);d.save()
    d=diagram(7,'问题、方法与技能在实践中相互校正','01:47:21–01:57:31','问题决定方法和技能需求；实践反馈既可以修正方法，也可以促使问题重述，导师和工具提供支持。',495)
    d.box(45,120,260,['找到愿意长期投入','而且有意义的问题'],'blue');d.box(370,120,260,['选择能检验想法','的研究方法'],'purple');d.box(695,120,260,['补齐实际需要','的技能与知识'],'orange')
    d.path('M310,175 L354,175');d.path('M635,175 L679,175');d.box(240,315,520,['实际尝试、反馈、修正'],'green');d.path('M825,236 L825,368 L772,368');d.path('M227,368 L175,368 L175,236');d.save()

def ep6():
    d=diagram(1,'有效算力由整条执行链决定','00:01:10–00:13:10','应用需求经模型和运行时转成芯片上的工作；下方指出优化要回到实际任务的结果与成本。',455)
    row(d,[['应用需求','回答／服务目标'],['模型与算法','运算与数据'],['软件运行时','映射与调度'],['芯片与系统','计算／存储／互联']])
    d.box(140,320,720,['优化目标：满足效果与时延要求的有效任务成本'],'green');d.save()
    d=diagram(2,'芯片从设计到量产的主要环节','00:13:10–00:25:50','两行分别是设计与制造，箭头从需求经过逻辑验证和物理设计进入流片，再经过封装测试到系统。',545)
    nodes=row(d,[['需求与架构','功能／功耗目标'],['RTL 设计','描述数字逻辑'],['功能验证','检查设计行为'],['物理设计','布局与布线']],100)
    nodes=row(d,[['系统使用','软件与应用'],['封装和测试','成品筛选'],['晶圆制造','多道工艺加工'],['流片','提交制造设计']],330)
    d.path('M867,224 L867,318');
    # The manufacturing row runs right to left.
    d.parts=[p for p in d.parts if not ('<path' in p and 'M250,385' in p) and not ('<path' in p and 'M495,385' in p) and not ('<path' in p and 'M740,385' in p)]
    for x in [770,525,280]:d.path(f'M{x-5},385 L{x-18},385')
    d.text(500,508,'AI 可协助局部设计和检查；最终仍要通过工程验证',23);d.save()
    d=diagram(3,'指令集、实现与制造属于不同层次','00:25:50–00:40:55','三层依次说明软件约定、具体微架构和制造；开放指令集只开放其中一层，制程节点不能直接解释全部性能。',560)
    for y,title,detail,col in [(105,'指令集 ISA','软件可见的指令与行为约定；如 RISC-V','blue'),(240,'微架构与芯片设计','具体流水线、缓存、互联与实现取舍','purple'),(375,'制造、封装与系统','晶圆工艺、良率、封装、供电和散热','orange')]:
        d.box(110,y,780,[title,detail],col,h=100)
    d.path('M500,211 L500,229');d.path('M500,346 L500,364');d.text(500,529,'节点名不是所有尺寸；能效、密度、成本需要一起看',22);d.save()
    d=diagram(4,'预填充与解码使用同一模型的不同方式','00:40:55–00:50:57','上行一次处理已知输入，生成键值缓存；下行反复生成新token并更新缓存，数据搬运与计算共同影响时延。',560)
    d.box(35,110,235,['输入 token 序列','已知上下文'],'blue');d.box(370,110,260,['Prefill 预填充','处理完整输入'],'purple');d.box(730,110,235,['KV 缓存','保留键和值'],'green');d.path('M276,165 L354,165');d.path('M636,165 L714,165')
    d.box(35,340,235,['已生成 token','逐步扩展序列'],'blue');d.box(370,340,260,['Decode 解码','预测下一个 token'],'orange');d.box(730,340,235,['读取并更新','KV 缓存'],'green');d.path('M276,395 L354,395');d.path('M636,395 L714,395');d.path('M849,228 L849,327');d.path('M500,450 L500,495 L153,495 L153,453');d.save()
    d=diagram(5,'AI 加速器在不同位置改变系统','00:50:57–01:09:54','四行是节目讨论的架构取向，不是性能排名；每种路线都要适配模型、编译器、容量与系统规模。',595)
    rows=[('NVIDIA GPU','通用并行计算、软件生态与系统集成','blue'),('Groq','确定性调度与片上存储取向','purple'),('Cerebras','晶圆级集成，减少部分跨芯片搬运','orange'),('SambaNova','可重构数据流与模型映射','green')]
    for j,(label,body,col) in enumerate(rows):
        d.box(40,100+j*105,235,[label],col,h=75);d.box(300,100+j*105,660,[body],col,h=75)
    d.text(500,563,'比较条件：模型、精度、输入长度、批大小、服务目标',22);d.save()
    d=diagram(6,'架构选择要同时面对技术与生态','01:09:54–01:29:21','中间是具体产品决策，周边分别提供性能、兼容、组织和长期维护约束；职业选择应看实际工作内容。',545)
    d.box(345,225,310,['具体产品与团队','作出技术取舍'],'purple',h=100)
    d.box(40,100,260,['性能与功耗','工作负载目标'],'blue');d.box(700,100,260,['软件兼容','迁移与开发成本'],'green');d.box(40,355,260,['组织执行','资源／协作／节奏'],'orange');d.box(700,355,260,['生态与维护','工具／伙伴／长期投入'],'blue')
    d.path('M305,180 L331,243');d.path('M695,180 L669,243');d.path('M305,393 L331,305');d.path('M695,393 L669,305');d.save()
    d=diagram(7,'虚拟仿真需要接回实机反馈','01:29:21–01:50:46','观测实际负载后建模，在虚拟环境试验候选方案，再在真实系统验证，误差反馈到模型。',505)
    row(d,[['真实负载观测','任务与硬件信息'],['建立系统模型','表示运行过程'],['虚拟试验','比较候选配置'],['实机验证','收益与误差']])
    d.path('M867,235 L867,285 L385,285 L385,235');d.text(620,315,'校准模型',22)
    d.box(100,360,800,['客户价值：减少试错成本，找到可落地的优化方案'],'green');d.save()
    d=diagram(8,'AI 工具把工程师的学习反馈缩短','01:50:46–01:56:44','从基础知识形成问题，借助AI实现候选，再以真实反馈检验；判断能力来自持续修正。',470)
    row(d,[['理解计算机基础','知道数据怎样流动'],['定义实际问题','明确交付目标'],['用 AI 辅助实现','生成与试验'],['读懂结果','修正下一次判断']])
    d.path('M867,233 L867,283 L140,283 L140,233');d.text(500,374,'学习成果体现在解释、验证与交付能力中',24);d.save()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('episode',type=int,choices=[5,6]);args=parser.parse_args()
    name={5:'ep05-N0QfgZsDBv8',6:'ep06-gxeP0tAm8mc'}[args.episode]
    lib.ROOT=REPO/'youtube/uncle-moon'/name/'assets';lib.ROOT.mkdir(exist_ok=True);lib.FIGURES=[]
    ep5() if args.episode==5 else ep6()
    import xml.etree.ElementTree as ET
    for f in lib.FIGURES:
        svg=lib.ROOT/(f['id']+'.svg');lib.convert(svg,int(ET.parse(svg).getroot().get('height')))
    (lib.ROOT/'figures.json').write_text(json.dumps(lib.FIGURES,ensure_ascii=False,indent=2)+'\n')
    print('Rendered',len(lib.FIGURES),'figures for',name)

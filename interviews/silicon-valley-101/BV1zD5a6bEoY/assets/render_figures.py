"""Render seven learning diagrams with the series SVG/Cairo renderer."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('series_figures', ROOT.parents[1]/'BV1dxJZ6uE3N/assets/render_figures.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
renderer.ROOT = ROOT

PLANS = [
 ('learning-loop','把知识变成能解释、能使用的能力',
  [['课程基础','概念与语言'],['多轮追问','补足不懂处'],['项目实践','暴露真实问题'],['复盘重述','解释自己的选择']],
  '06:38–12:11','顺箭头读四环节，虚线表示项目复盘反过来决定补什么基础。法律复习与代码项目都依靠自己的解释和实际任务反馈。','反馈决定下一轮要补什么知识',True,False),
 ('university-value','大学提供的四种资源',
  [['学科基础','理解专业语言'],['同辈与导师','交流并建立信任'],['自我认识','辨明兴趣和价值'],['学历信号','获得社会认可']],
  '14:43–31:07','四栏并列，分别表示知识、关系、自我探索和社会信号。Alfred 与 Kolento 给这些资源不同权重。','每个人要为不同资源分配时间',False,True),
 ('reverse-learning','从目标作品反推学习路径',
  [['观察好作品','建立质量标准'],['找关键差异','明确自己不懂处'],['追问并补基础','定义与具体例子'],['查源与真人反馈','再做自己的作品']],
  '36:26–39:19','先看作品和解释，再找关键区分点，补解决当前问题所需知识；最后借出处和真人检查，模型模拟的专家不是真实专家发言。','验证后的作品成为下一轮比较对象',True,False),
 ('assignment-flow','让自己的判断贯穿作业过程',
  [['读课程要求','定义交付目标'],['拆解任务','列出步骤和限制'],['比较候选产出','用课程知识检查'],['解释与交付','为最终结果负责']],
  '40:51–46:38','AI 可参与各环节，人确定要求和评价。标准题检查答案及推导；开放作品检查论证、用途和取舍。','AI 参与比例与个人理解程度是两个问题',False,False),
 ('tool-workflow','按任务分工组织 AI 工具',
  [['表达意图','语音与文字输入'],['探索问题','脑暴与检索'],['执行任务','编程与设计'],['检查交付','运行、阅读、比较']],
  '46:38–59:46','图展示任务角色。记忆有助于表达个人偏好，执行阶段则需重新说明事实、目标和约束。','用任务、效果和成本决定是否增加调度层',False,False),
 ('ability-check','用四个问题检查自己的学习',
  [['能解释吗','说清核心原理'],['能判断吗','发现错误与取舍'],['能迁移吗','换一个任务应用'],['能接续吗','工具受限时推进']],
  '59:46–01:12:12','四栏是依据访谈整理的自我检查问题。用真实课程或项目回答，可以把工具熟练度和个人能力分别看清。','检查真实任务，避免只凭顺畅感判断',False,True),
 ('whole-task','把完整任务时间纳入效率判断',
  [['准备与检索','形成问题和资料'],['生成与实现','产出初稿或代码'],['验证与返工','发现并修复问题'],['最终交付','可用且可解释']],
  '01:12:12–01:15:21','沿完整任务链记录时间。METR 和泓君的转录经历提示，某一步加速可能把工作转移到检查阶段。','同时记录完成时间、质量和学到的内容',False,False)
]

if __name__ == '__main__':
    for name,title,labels,source,reading,footer,loop,parallel in PLANS:
        d=renderer.Diagram(name,title,350,source,reading)
        nodes=[d.box(32+i*247,100,195,label,['blue','purple','orange','green'][i],h=112) for i,label in enumerate(labels)]
        if not parallel:
            for a,b in zip(nodes,nodes[1:]): d.right(a,b)
        if loop:d.path('M870,218 V260 H130 V219',True)
        d.text(500,316,footer,22,color='#64748b');d.save()
        renderer.convert(ROOT/(name+'.svg'),350)
    (ROOT/'figures.json').write_text(json.dumps(renderer.FIGURES,ensure_ascii=False,indent=2)+'\n')
    print('Rendered',len(renderer.FIGURES),'figures')

"""Render editable teaching diagrams with librsvg and Cairo."""
import ctypes as C
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COLORS = [('#dbeafe','#3b82f6'),('#f3e8ff','#a855f7'),('#fef3c7','#f59e0b'),('#d1fae5','#22c55e')]
FIGURES = [
 ('improvement-loop','一次改进的闭环',['诊断薄弱能力','构造训练任务','执行训练','验证效果'],'03:29–10:58；22:22–23:32','每轮验证改变下一轮诊断','箭头表示依次执行，底部回流表示下一轮重新诊断。上下文里修改答案和改变训练后的模型能力是两个层次。'),
 ('long-task','长任务系统的三层支撑',['模型能力','记忆与任务分工','工具和环境反馈'],'10:58–13:21；29:48–31:42','上下文容量、有效利用和持续任务分别检查','三个并列模块共同支撑长任务：模型理解当前信息，记忆与分工选择上下文，工具反馈提供任务进度。图中不把百万上下文当成任务成功保证。'),
 ('verification','求解与验证使用不同的工作上下文',['任务与条件','候选解法','独立验证步骤','汇总与修订'],'14:57–20:02','代码看测试；数学看证明；开放问题看证据','从任务条件读到候选，再按任务选择测试、证明检查或证据审查。验证反馈回到候选修改。分开的工作上下文能减少自我重复，但仍需关注共同错误。'),
 ('training-harness','模型与脚手架交替改进',['观察任务失败','更新数据与训练','调整脚手架','检查整体效果'],'20:02–28:48；01:07:01–01:08:51','案例：先分解问题，再按需要搜索','左脚右脚比喻对应模型训练和脚手架调整。成功要检查整体任务；仅增加搜索数据可能让模型一开始就搜索，偏离先分析再行动的目标。'),
 ('discovery','科学发现的两个问题：新不新，真不真',['检索已有知识','提出新假设','设计验证办法','实验与新证据'],'34:47–40:26；52:02–57:53','模型、模拟器、真实实验各有自己的作用','先确定已有知识，再提出假设，选择证明、代码实验、模拟或真实实验。返回的证据可以否定假设，下一轮据此改变问题。新颖性和可验证性要分别判断。'),
 ('research-taste','把研究判断变成模型可学习的信号',['候选研究问题','专家比较与理由','偏好或示范训练','新的选题与检验'],'40:26–52:02；01:05:04–01:06:47','追求有价值的问题，同时给出可行的检验路径','专家在两个问题之间解释价值差异，把判断转为示范或偏好数据。模型再提出问题，检验训练是否改变了行为。学术品味不等于话术风格，也不是一个通用分数。'),
 ('progress-stages','单环、多轮递归与持续可靠',['跑通一次改进','多轮重复提升','维持目标与约束'],'57:53–01:05:04','“最快半年”是李辈滨在 2026-07-06 节目中的单环预测','从左到右是不同要求：单次诊断训练有效；多轮有继续改进能力；长时间运行仍能控制漂移、成本和目标。这里是概念阶段，没有实验时间轴或实测百分比。')
]

def svg(name,title,labels,source,footer,reading):
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="340" viewBox="0 0 1000 340"><title>{escape(title)}</title><desc>{escape(reading)}</desc>',
      '<style>text{font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;fill:#1e293b}</style>',
      '<defs><marker id="a" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L8,4 L0,8 L2,4 z" fill="#64748b"/></marker></defs><rect width="1000" height="340" fill="white"/>']
    def text(x,y,t,size=23):parts.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle">{escape(t)}</text>')
    def arrow(d):parts.append(f'<path d="{d}" fill="none" stroke="#64748b" stroke-width="1.5" marker-end="url(#a)"/>')
    text(500,48,title,30)
    n=len(labels); w=(920-40*(n-1))/n
    for i,label in enumerate(labels):
        x=40+i*(w+40);fill,stroke=COLORS[i]
        parts.append(f'<rect x="{x}" y="108" width="{w}" height="86" rx="10" fill="{fill}" stroke="{stroke}"/>');text(x+w/2,159,label)
        if i<n-1 and name!='long-task':arrow(f'M{x+w+5},151 L{x+w+29},151')
    if name not in ('long-task','progress-stages'):
        left=40+w/2+(w+40 if name=='verification' else 0);right=960-w/2
        arrow(f'M{right},199 C{right},274 {left},274 {left},205')
        text(500,245,'根据反馈调整下一轮',20)
    elif name=='long-task':
        for i in range(n):
            x=40+i*(w+40)+w/2;arrow(f'M{x},199 C{x},220 500,220 500,245')
        text(500,274,'持续完成可检查的任务',22)
    text(500,321,footer,19)
    parts.append('</svg>');(ROOT/(name+'.svg')).write_text('\n'.join(parts)+'\n')

def convert(path):
    rsvg=C.CDLL('librsvg-2.so.2');cairo=C.CDLL('libcairo.so.2');obj=C.CDLL('libgobject-2.0.so.0')
    for lib,name,args,result in [(rsvg,'rsvg_handle_new_from_file',[C.c_char_p,C.c_void_p],C.c_void_p),(rsvg,'rsvg_handle_render_cairo',[C.c_void_p,C.c_void_p],C.c_int),(cairo,'cairo_pdf_surface_create',[C.c_char_p,C.c_double,C.c_double],C.c_void_p),(cairo,'cairo_image_surface_create',[C.c_int,C.c_int,C.c_int],C.c_void_p),(cairo,'cairo_create',[C.c_void_p],C.c_void_p),(cairo,'cairo_scale',[C.c_void_p,C.c_double,C.c_double],None),(cairo,'cairo_surface_write_to_png',[C.c_void_p,C.c_char_p],C.c_int),(cairo,'cairo_destroy',[C.c_void_p],None),(cairo,'cairo_surface_destroy',[C.c_void_p],None),(obj,'g_object_unref',[C.c_void_p],None)]:
        f=getattr(lib,name);f.argtypes=args;f.restype=result
    handle=rsvg.rsvg_handle_new_from_file(str(path).encode(),None)
    assert handle
    for kind in ['pdf','png']:
        out=path.with_suffix('.'+kind)
        surface=cairo.cairo_pdf_surface_create(str(out).encode(),1000,340) if kind=='pdf' else cairo.cairo_image_surface_create(0,2000,680)
        ctx=cairo.cairo_create(surface)
        if kind=='png':cairo.cairo_scale(ctx,2,2)
        assert rsvg.rsvg_handle_render_cairo(handle,ctx)
        if kind=='png':assert cairo.cairo_surface_write_to_png(surface,str(out).encode())==0
        cairo.cairo_destroy(ctx);cairo.cairo_surface_destroy(surface)
    obj.g_object_unref(handle)

if __name__=='__main__':
    result=[]
    for row in FIGURES:
        svg(*row);convert(ROOT/(row[0]+'.svg'))
        result.append(dict(id=row[0],title=row[1],path='assets/'+row[0]+'.pdf',source=row[3],reading=row[5]))
    (ROOT/'figures.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('Rendered',len(result),'diagrams')

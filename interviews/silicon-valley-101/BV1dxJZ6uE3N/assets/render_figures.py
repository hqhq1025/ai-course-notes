#!/usr/bin/env python3
"""Rebuild the seven editable teaching diagrams using system librsvg/Cairo."""
import ctypes as C
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COLORS = {'blue': ('#dbeafe', '#3b82f6'), 'green': ('#d1fae5', '#22c55e'),
          'orange': ('#fef3c7', '#f59e0b'), 'purple': ('#f3e8ff', '#a855f7')}
FIGURES = []


class Diagram:
    def __init__(self, name, title, height, source, explanation):
        self.name, self.height = name, height
        self.parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}">
<title>{escape(title)}</title><desc>{escape(explanation)}</desc>
<style>text {{ font-family: 'PingFang SC', 'Microsoft YaHei', 'Noto Sans CJK SC', 'Droid Sans Fallback', system-ui, sans-serif; fill:#1e293b; }}</style>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L8,4 L0,8 L2,4 z" fill="#64748b"/></marker></defs>
<rect width="1000" height="{height}" fill="white"/>''']
        self.text(500, 49, title, 30)
        self.meta = {'id': name, 'title': title, 'path': f'assets/{name}.pdf',
                     'svg': f'assets/{name}.svg', 'png': f'assets/{name}.png',
                     'source': source, 'provenance': '依据节目口述整理的机制示意图',
                     'reading': explanation}

    def text(self, x, y, value, size=23, anchor='middle', color='#1e293b'):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" style="fill:{color}">{escape(value)}</text>')

    def box(self, x, y, w, lines, color='blue', h=None):
        h = h or 72 + 34 * (len(lines) - 1)
        fill, stroke = COLORS[color]
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        for i, line in enumerate(lines):
            self.text(x + w / 2, y + h / 2 + 8 - 17 * (len(lines) - 1) + i * 34, line)
        return x, y, w, h

    def path(self, d, dashed=False):
        dash = ' stroke-dasharray="6,4"' if dashed else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"{dash}/>')

    def right(self, a, b):
        x, y, w, h = a
        self.path(f'M{x+w+5},{y+h/2} L{b[0]-11},{y+h/2}')

    def save(self):
        (ROOT / f'{self.name}.svg').write_text('\n'.join(self.parts) + '\n</svg>\n')
        FIGURES.append(self.meta)


def diagrams():
    d = Diagram('task-experience', '同一模型，三种任务体验', 445, '06:10–06:52；07:35–09:36；09:36–13:48',
                '从左到右读每一行。机器人行保留分叉花茎造成失败及捏窄后成功的动作变化；编程行描述更长任务中的稳定性；科研行描述借助 GUI 学习旧软件流程。三行是不同任务的经验，不是同一指标下的模型比分。')
    rows = [('机器人', ['插花遇阻'], ['捏窄分叉花茎'], ['成功插入']),
            ('编程', ['任务持续更久'], ['记住上下文'], ['检查长期稳定性']),
            ('科研', ['旧软件难接入'], ['操作图形界面'], ['学习工作流程'])]
    for i, (label, a, b, c) in enumerate(rows):
        y = 88 + i * 104
        d.text(91, y + 43, label)
        nodes = [d.box(180, y, 230, a), d.box(455, y, 230, b, 'orange'), d.box(730, y, 230, c, 'green')]
        d.right(nodes[0], nodes[1]); d.right(nodes[1], nodes[2])
    d.text(500, 416, '比较任务变化，不合成统一得分', 21, color='#64748b'); d.save()

    d = Diagram('agent-constraints', '个人 Agent 落地的三个条件', 392, '13:48–25:22',
                '三个并列条件共同影响任务能否完成。访问权关乎平台和网络能否进入；代理身份关乎是否获用户授权及网站是否认可代理关系；成本包括模型 token 和沙箱计算。个人设备可能改变部分条件，但没有自动满足其余条件。')
    for x, lines, color in [(40,['访问权','平台与网络可进入'],'blue'), (365,['代理身份','授权及代理关系'],'purple'), (690,['可承受成本','token ＋ 沙箱'],'orange')]:
        d.box(x, 91, 270, lines, color, h=110)
    for x in (175,500,825):
        d.path(f'M{x},206 C{x},232 500,227 500,247')
    d.box(290,258,420,['完成个人 Agent 任务'],'green')
    d.text(500, 365, '本地设备只改变部分条件，三项需分别检验', 21, color='#64748b'); d.save()

    d = Diagram('evaluation-gap', '基准解题与真实研究的任务差别', 383, '29:06–30:44；01:01:25–01:05:18',
                '两列分别展示已定义任务和开放研究的条件。左侧给定输入、目标和测试；右侧还要界定问题、等待实验反馈并分配资源。水平并列表示任务差别，不表示基准没有价值，也不是能力优劣排名。')
    d.box(50,90,425,['固定输入','明确目标','已知测试'],'blue',h=150)
    d.box(525,90,425,['未知目标','实验反馈','资源约束'],'orange',h=150)
    d.path('M262.5,245 L262.5,264'); d.path('M737.5,245 L737.5,264')
    d.box(50,275,425,['基准解题'],'green');d.box(525,275,425,['真实研究'],'purple');d.save()

    d = Diagram('robot-control', '按任务条件划分规划与控制', 523, '31:30–38:20；45:05–46:59',
                '主链从慢速规划到可执行子目标、本地快速控制及物理环境。两条回流分别将执行反馈用于调整规划和快速控制。下方两栏区分几何外观与动力学：重建形状不能自动补齐接触、摩擦或流体的即时反馈。图不指定固定频率或已实现的统一架构。')
    labels=[['慢速规划'],['可执行子目标'],['本地快速控制'],['物理环境']]
    nodes=[d.box(35+i*245,120,195,l, ['purple','blue','orange','green'][i]) for i,l in enumerate(labels)]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.path('M867.5,115 C867.5,76 132.5,76 132.5,109',True)
    d.path('M867.5,197 C867.5,280 622.5,280 622.5,203',True)
    d.text(500, 267, '执行反馈同时用于规划和控制', 21, color='#64748b')
    d.box(70,329,410,['几何外观','形状、位置、空间关系'],'blue',h=110)
    d.box(520,329,410,['动力学','接触、摩擦、运动响应'],'orange',h=110)
    d.text(500,491,'分层边界随任务变化；几何重建不等于动力学准确',21,color='#64748b');d.save()

    d=Diagram('wetlab-loop','把候选假设接到实验反馈',397,'47:41–01:00:26；01:16:10–01:18:20',
              '沿箭头读四个环节。模型提出候选假设后，实验方案必须匹配实验室预算、设备和时间，再由实验人员或设备执行湿实验。结果回流用于修订假设。本图展示协作关系，不提供生物实验操作配方。')
    labels=[['候选假设'],['资源匹配的','实验方案'],['湿实验执行'],['结果回流']]
    nodes=[d.box(35+i*245,111,195,l,['purple','blue','orange','green'][i],h=106) for i,l in enumerate(labels)]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.path('M867.5,222 C867.5,298 132.5,298 132.5,228',True)
    d.text(500,260,'用实验结果修订假设',21,color='#64748b')
    d.box(240,309,520,['共同约束：预算 · 设备 · 时间'],'orange',h=62);d.save()

    d=Diagram('science-data','围绕持续问题积累实验数据',391,'52:06–58:14；01:04:13–01:08:15',
              '从持续问题出发选择实验，验证结果产生新的数据，再改进下一轮。数据不是脱离问题堆积；选择什么实验决定得到哪种反馈。底部注明工业酶与药物研发的验证周期不同，不用虚构数值或曲线代表两类任务。')
    labels=[['持续问题'],['选择实验'],['验证结果'],['积累数据'],['改进下一轮']]
    nodes=[d.box(35+i*195,101,150,l,['purple','blue','orange','green','purple'][i]) for i,l in enumerate(labels)]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.path('M890,178 C890,266 110,266 110,184',True)
    d.text(500,218,'新数据改变下一轮的问题与实验选择',21,color='#64748b')
    d.box(160,283,680,['工业酶应用与药物研发：反馈周期不同'],'orange')
    d.save()

    d=Diagram('human-learning','人和模型怎样互相提供学习材料',397,'01:08:16–01:12:09',
              '上方箭头表示人提供日常示范、新问题与评价；下方反向箭头表示模型帮助人学习知识和工具。研究目标单独列出，提醒读者跨场景熟练不等于已实现自主学习。这里的学习包括人的学习和提供训练/反馈材料，不主张每次交流都会更新模型权重。')
    d.box(70,131,220,['人'],'blue',h=102);d.box(710,131,220,['模型'],'purple',h=102)
    d.path('M295,151 L699,151');d.text(500,125,'日常示范 · 新问题 · 评价',21)
    d.path('M705,218 L301,218');d.text(500,256,'帮助人学习知识与工具',21)
    d.box(130,300,740,['研究目标：学会如何学习'],'orange');d.save()


def convert(svg, height):
    rsvg=C.CDLL('librsvg-2.so.2');cairo=C.CDLL('libcairo.so.2');gobject=C.CDLL('libgobject-2.0.so.0')
    for lib,name,args,result in [(rsvg,'rsvg_handle_new_from_file',[C.c_char_p,C.c_void_p],C.c_void_p),
        (rsvg,'rsvg_handle_render_cairo',[C.c_void_p,C.c_void_p],C.c_int),
        (cairo,'cairo_pdf_surface_create',[C.c_char_p,C.c_double,C.c_double],C.c_void_p),
        (cairo,'cairo_image_surface_create',[C.c_int,C.c_int,C.c_int],C.c_void_p),
        (cairo,'cairo_create',[C.c_void_p],C.c_void_p),(cairo,'cairo_scale',[C.c_void_p,C.c_double,C.c_double],None),
        (cairo,'cairo_surface_write_to_png',[C.c_void_p,C.c_char_p],C.c_int),
        (cairo,'cairo_destroy',[C.c_void_p],None),(cairo,'cairo_surface_destroy',[C.c_void_p],None),
        (gobject,'g_object_unref',[C.c_void_p],None)]:
        f=getattr(lib,name);f.argtypes=args;f.restype=result
    handle=rsvg.rsvg_handle_new_from_file(str(svg).encode(),None)
    assert handle
    for kind in ['pdf','png']:
        path=svg.with_suffix('.'+kind)
        surface=(cairo.cairo_pdf_surface_create(str(path).encode(),1000,height) if kind=='pdf'
                 else cairo.cairo_image_surface_create(0,2000,2*height))
        ctx=cairo.cairo_create(surface)
        if kind=='png':cairo.cairo_scale(ctx,2,2)
        assert rsvg.rsvg_handle_render_cairo(handle,ctx)
        if kind=='png':assert cairo.cairo_surface_write_to_png(surface,str(path).encode())==0
        cairo.cairo_destroy(ctx);cairo.cairo_surface_destroy(surface)
    gobject.g_object_unref(handle)


if __name__=='__main__':
    import xml.etree.ElementTree as ET
    diagrams()
    for item in FIGURES:
        svg=ROOT/(item['id']+'.svg');tree=ET.parse(svg)
        convert(svg,int(tree.getroot().get('height')))
    (ROOT/'figures.json').write_text(json.dumps(FIGURES,ensure_ascii=False,indent=2)+'\n')
    print('Rendered',len(FIGURES),'figures as SVG, PDF and PNG')

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
    d = Diagram('data-supply', '数据供给的四种能力来源', 372, '05:24–08:02',
                '四栏表示招聘网络、众包组织、内部培养、工程合成的不同能力来源，不代表公司互斥分类。蓝色是找到人，绿色是组织交付，橙色是培养质量，紫色是工程加工；底部说明它们都要形成可用训练信号。')
    nodes = [['招聘网络','找到领域专家'],['众包组织','灵活调配产能'],['内部培养','积累质量经验'],['工程合成','搭建任务环境']]
    for i, lines in enumerate(nodes):
        box = d.box(35+i*245,100,195,lines,['blue','green','orange','purple'][i],h=110)
        d.path(f'M{132.5+i*245},215 C{132.5+i*245},240 500,240 500,263')
    d.box(250,274,500,['交付可用的训练信号'],'green')
    d.save()

    d = Diagram('task-feedback', '任务环境与评分细则如何配合', 397, '09:22–20:20',
                '从任务进入智能体，智能体在工具和沙箱中执行，产出交给验证器。验证器同时接收程序检查、专家评分细则和偏好判断；虚线把反馈送回智能体。评分细则是验证方式之一，并不与整个环境互相替代。')
    nodes=[d.box(35+i*245,108,195,lines,['blue','purple','orange','green'][i],h=100)
           for i,lines in enumerate([['任务目标'],['智能体','工具与沙箱'],['执行结果'],['验证器']])]
    for a,b in zip(nodes,nodes[1:]): d.right(a,b)
    d.path('M867.5,103 C867.5,75 377.5,75 377.5,97',True)
    d.box(185,280,630,['程序检查 ＋ 专家评分细则 ＋ 偏好判断'],'orange')
    d.path('M820,316 C950,316 940,250 867.5,219')
    d.save()

    d = Diagram('evaluation-distribution', '从多项评测到真实任务体验', 388, '20:20–33:35',
                '三个评测维度对应不同任务，各自成绩经过任务分布和权重形成总分。总分与真实任务体验并列对照而非等同；两条支路提醒分别观察跨任务能力和具体产品体验。图没有给出经验权重。')
    for i,lines in enumerate([['代码任务'],['行业任务'],['长程工作流']]):
        d.box(45+i*325,100,260,lines,['blue','orange','purple'][i])
        d.path(f'M{175+i*325},177 C{175+i*325},198 500,198 500,218')
    d.box(250,229,500,['任务分布与权重 → 综合得分'],'green')
    d.text(500,338,'同时对照：跨任务表现 · 真实用户体验',23)
    d.save()

    d = Diagram('procurement-processing', '先采购原材料，再加工训练环境', 424, '33:35–44:18',
                '上行是原材料与权利的获取，下行是把材料组织成可运行任务。箭头连接专业知识和项目材料、使用许可、任务设计、工具沙箱、验证与交付；采购能力和工程加工都影响最终质量。')
    a=d.box(45,100,270,['专业知识','项目材料'],'blue',h=104)
    b=d.box(365,100,270,['获取资料','明确使用许可'],'orange',h=104)
    c=d.box(685,100,270,['设计真实任务'],'purple',h=104)
    d.right(a,b);d.right(b,c)
    e=d.box(685,275,270,['工具与沙箱'],'purple')
    f=d.box(365,275,270,['验证任务结果'],'green')
    g=d.box(45,275,270,['交付训练环境'],'green')
    d.path('M820,209 L820,264')
    d.path('M680,311 L646,311');d.path('M360,311 L326,311')
    d.text(500,392,'原材料的获取能力与加工能力共同决定交付',22)
    d.save()

    d = Diagram('training-recipe', '把任务变成适合模型的学习信号', 410, '44:18–48:45',
                '相同任务可以进入两种训练方式：答案和轨迹用于监督微调，执行反馈用于强化学习。底部共同条件包含难度匹配、资源预算和捷径检查；评测只看最终成功时，仍不能直接替代训练配方。')
    d.box(310,93,380,['任务与环境'],'blue')
    d.path('M395,170 C395,192 250,185 250,217')
    d.path('M605,170 C605,192 750,185 750,217')
    d.box(45,228,410,['答案与轨迹 → 监督微调'],'purple')
    d.box(545,228,410,['执行反馈 → 强化学习'],'green')
    d.text(500,362,'共同条件：难度匹配 · 资源预算 · 捷径检查',23)
    d.save()

    d = Diagram('expert-quality', '专家数据需要同时解决三类质量问题', 384, '48:45–57:44',
                '三列区分测试内容进入训练集、评分或答案错误、提交者伪造材料。下行是各类问题的对应处理。底部强调专家激励贯穿数据提交和复核过程；流程记录和第二专家复核存在成本，不能天然消除作弊。')
    rows=[(['数据污染'],['隔离测试内容']),(['测试或答案错误'],['复核标准与解法']),(['伪造任务材料'],['核对过程与结果'])]
    for i,(problem,action) in enumerate(rows):
        a=d.box(45+i*325,96,260,problem,['blue','orange','purple'][i])
        b=d.box(45+i*325,226,260,action,'green')
        d.path(f'M{175+i*325},173 L{175+i*325},215')
    d.text(500,344,'贯穿全程：让提交者与复核者的激励对齐',23)
    d.save()


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

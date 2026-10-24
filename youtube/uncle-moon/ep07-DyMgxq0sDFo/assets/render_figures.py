#!/usr/bin/env python3
"""Render the seven mechanism diagrams for the Chen Ran interview."""
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
    d=Diagram('learning-to-value','从学习问题到可观察的结果',380,'00:01:15–00:22:24',
              '从理解评价规则到补足能力，再到真实任务与结果。箭头代表学习和实践的次序；商业反馈帮助选择下一步，不表示所有技术工作都必须立即赚钱。')
    nodes=[d.box(35,115,210,['明确问题','评价规则']),d.box(275,115,210,['补足能力','课程／项目'],'purple'),d.box(515,115,210,['进入真实任务','用户／业务'],'orange'),d.box(755,115,210,['观察结果','调整方向'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.text(500,295,'从考试、CMU 项目到机器学习应用：先问要解决什么',22);d.save()

    d=Diagram('delivery-loop','技术落地需要组织配合',450,'00:22:24–00:38:26',
              '上方是管理者搭建的支持条件，下方才是团队执行和实验的闭环。上下两层配合，算法才有进入产品和收到反馈的机会。')
    d.box(70,85,860,['管理支持：统一优先级 · 数据与实验基础 · 跨团队清障'],'purple')
    d.path('M500,167 L500,215')
    nodes=[d.box(35,230,210,['业务问题','团队提出方案']),d.box(275,230,210,['数据与原型','检验可行性'],'orange'),d.box(515,230,210,['上线实验','观察影响'],'green'),d.box(755,230,210,['复盘与迭代','下一步责任'],'blue')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.text(500,418,'自主提出方案，也要对交付与结果负责',22);d.save()

    d=Diagram('shared-risk','不同资产可能暴露于同一种风险',465,'00:51:48–01:01:40',
              '上方同一个科技行业变化可以同时影响工资、雇主股票与当地住房需求。三条路径指向家庭现金流，说明资产名称不同不等于风险来源不同。')
    d.box(290,75,420,['科技行业与雇主状况'],'purple')
    for x,title,sub,col in [(40,'工资与职业','未来收入','blue'),(365,'雇主股票','持仓市值','orange'),(690,'当地房产','需求与房贷','green')]:
        d.box(x,225,270,[title,sub],col)
        d.path(f'M500,155 C500,185 {x+135},185 {x+135},215')
    d.text(500,415,'规划先看家庭现金流、消费底线与集中暴露',22);d.save()

    d=Diagram('small-business','从真实需求到能持续经营的小项目',420,'01:04:46–01:20:21',
              '四个阶段依次是需求证据、产品提供、成本收入和迭代。需求既可来自本人长期遇到的问题，也可来自关键词等外部线索，但仍要看用户是否使用。')
    nodes=[d.box(35,105,210,['找到真实需求','亲历／搜索']),d.box(275,105,210,['做出可用产品','备考资料'],'purple'),d.box(515,105,210,['算清每笔账','收入／成本'],'orange'),d.box(755,105,210,['观察用户反馈','继续／调整'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.box(130,285,740,['“零人”仍需要选题、查看运行与经营决策'],'blue');d.save()

    d=Diagram('company-workflow','AI 重构交付后，瓶颈向获客移动',445,'01:20:21–01:31:11',
              '系统删减、知识沉淀、专业人员和AI配合形成交付流程。交付能力提高以后，新的约束转向客户增长；监管决定仍不由生成文档代替。')
    nodes=[d.box(35,100,210,['客户真正需求','删减功能']),d.box(275,100,210,['系统＋知识库','沉淀经验'],'purple'),d.box(515,100,210,['专家＋AI工具','完成服务交付'],'orange'),d.box(755,100,210,['更多交付能力','需要更多客户'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.box(100,275,365,['Pure Global','医疗器械注册服务'],'blue')
    d.box(535,275,365,['VayoMed','生命科学客户增长'],'green');d.save()

    d=Diagram('bottleneck-and-incentive','局部提速与整体收益之间还有哪些环节',465,'01:31:11–01:40:51；01:45:25–01:49:04',
              '上方是20%工作环节提速5倍的假设算例，其余80%不变时，总耗时降到84%。下方说明任务效率还要经过交付和获客，才能形成可分配收益。')
    d.box(40,85,425,['原总耗时：100%','待提速环节 20% ＋ 其余 80%'],'blue')
    d.box(535,85,425,['新总耗时：84%','20% ÷ 5 ＋ 80%'],'purple')
    d.path('M475,140 L523,140')
    nodes=[d.box(40,285,270,['任务提速','完成有效工作']),d.box(365,285,270,['交付与获客','形成业务结果'],'orange'),d.box(690,285,270,['收益与分配','调整参与激励'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.text(500,440,'教学算例：整体速度约为原来的 1.19 倍',22);d.save()

    d=Diagram('next-step','从自己的约束出发做一次小规模实践',415,'01:40:51–01:45:25；01:49:04–01:56:14',
              '四个步骤将家庭财务约束、既有经验、一手信息和小规模产品尝试连接起来。结果帮助下一次选择；人物的具体职业和消费安排无需照搬。')
    nodes=[d.box(35,105,210,['梳理生活目标','时间／现金流']),d.box(275,105,210,['盘点行业经验','能解决的问题'],'purple'),d.box(515,105,210,['接触一手实践','客户／做事者'],'orange'),d.box(755,105,210,['试做一个产品','观察使用反馈'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.box(130,280,740,['用实际结果更新判断，再决定下一步投入'],'blue');d.save()


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

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
    d = Diagram('video-production', '可控的视频如何进入广告生产', 450, '04:28–10:57',
                '从产品素材和参考视频进入生成、筛选与交付。上方呈现生产链，下方区分生成成本与销售收入；成本和售价来自嘉宾接触案例，差额还需要支付筛选、修改、人员和销售成本。')
    nodes = [d.box(35,100,210,['素材与参考','角色／声音']), d.box(275,100,210,['多镜头生成','可控性提升'],'purple'), d.box(515,100,210,['筛选与修改','检查可交付性'],'orange'), d.box(755,100,210,['投放交付','广告主／代理'],'green')]
    for a,b in zip(nodes,nodes[1:]): d.right(a,b)
    d.box(60,270,395,['15 秒生成成本：15 元以下'],'blue')
    d.box(545,270,395,['合格广告售价：25—50 元'],'green')
    d.text(500,409,'口述案例量级；收入减生成成本还不是净利润',22);d.save()

    d = Diagram('agent-device', '自然语言如何接到实际服务', 440, '14:13–24:37',
                '上方显示点咖啡任务经过理解、选择与交易服务的执行链。下方端侧和云端不是两种独立产品，而是围绕延时、隐私、复杂度与负载协作；眼镜属于节目讨论的硬件入口。')
    nodes=[d.box(35,90,210,['用户需求','语音／视觉']),d.box(275,90,210,['理解意图','偏好与上下文'],'purple'),d.box(515,90,210,['选择并调用工具','菜单／口味／订单'],'orange'),d.box(755,90,210,['服务返回','确认交易结果'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.box(70,270,390,['端侧','及时交互／本地信息'],'blue')
    d.box(540,270,390,['云端','复杂任务／服务接入'],'purple')
    d.path('M466,308 L528,308');d.path('M534,335 L472,335');d.text(500,415,'任务分配随设备能力和业务条件变化',22);d.save()

    d=Diagram('cost-stack','成本下降发生在三个层次',430,'24:37–30:18',
              '三列分别指向模型计算、软硬配合与云端利用率。三条路径一起影响单位有效任务成本；底部提醒首包时延、生成速度与并发仍需按具体工作负载考察。')
    for x,title,lines,col in [(40,'模型结构',['小模型／稀疏激活','混合精度／MTP'],'blue'),(365,'软硬配合',['芯片与模型协同','适合任务的执行'],'purple'),(690,'资源调度',['不同时段与任务','空闲资源用于跑批'],'orange')]:
        d.text(x+135,105,title,26);d.box(x,130,270,lines,col,h=105);d.path(f'M{x+135},242 L{x+135},279')
    d.box(150,290,700,['单位有效任务成本下降'],'green')
    d.text(500,405,'同时考察：回答效果 · 首包时延 · 生成速度 · 并发',22);d.save()

    d=Diagram('business-layers','从模型权重到完整任务结果',445,'30:18–39:20',
              '从左到右增加服务商承担的工作。开源用户仍需部署运维；模型API交付推理能力；Agent服务把模型、工具、流程组合成任务结果。下方反馈环路说明社区与商业服务可以相互促进。')
    nodes=[d.box(35,105,275,['开源模型权重','用户部署与运维'],'blue',h=130),d.box(362,105,275,['模型 API（MaaS）','托管推理与并发'],'purple',h=130),d.box(689,105,275,['Agent 服务','工具＋流程＋结果'],'green',h=130)]
    d.right(nodes[0],nodes[1]);d.right(nodes[1],nodes[2])
    d.box(120,305,760,['社区反馈 → 模型改进 → 易用服务 → 更多应用'],'orange')
    d.text(500,420,'token 反映使用量；收入还取决于模型、任务和定价',22);d.save()

    d=Diagram('panorama-editing','先拍后剪：全景专用能力接通用模型',465,'39:20–49:02',
              '上方保留用户想讲的故事，下方才是素材处理链。全景模型先从360度素材选视角和高光，通用模型组织平面内容，最后结合节奏与特效交付。压缩目标是减少冗余输入同时保留任务需要的事件。')
    d.box(185,85,630,['用户意图：纪实故事／高光片段／氛围表达'],'purple')
    d.path('M500,161 L500,207')
    nodes=[d.box(30,220,210,['360° 素材','保留完整现场']),d.box(275,220,210,['专用全景理解','选择视角与事件'],'orange'),d.box(520,220,210,['通用模型编排','连成故事'],'purple'),d.box(765,220,210,['剪辑与生成特效','形成可分享视频'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.text(500,410,'降低输入冗余，而非只按固定间隔丢弃画面',23);d.save()

    d=Diagram('customer-knowledge','客服资料怎样变成可执行的知识',450,'49:02–57:17',
              '左侧的文档、图片和对话先被清洗成知识库。用户意图决定检索和流程，复杂优惠需要继续核对规则，退货归因保留人工复审。底部是从业务相关标签回到产品和服务的反馈。')
    nodes=[d.box(35,100,210,['文档／详情页','客服对话']),d.box(275,100,210,['清洗与结构化','建立知识库'],'purple'),d.box(515,100,210,['意图识别＋RAG','检索业务知识'],'orange'),d.box(755,100,210,['规则与工作流','回答／处理／复审'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.box(95,290,810,['业务标签：肤质与反馈 · 产品／物流意见 · 退货归因'],'blue')
    d.text(500,418,'RAG：检索相关资料，再让模型结合资料生成回答',22);d.save()

    d=Diagram('value-loop','AI 的处理结果怎样成为业务价值',455,'57:17–66:43',
              '数据加工生成标签和报告，经营者选择产品与服务动作，再根据市场反馈调整。下方区分服务成本和客户理解的收费单位，说明token成本不必原样成为客户账单。')
    nodes=[d.box(35,95,210,['消费者数据','对话／反馈']),d.box(275,95,210,['AI 加工','标签／分析报告'],'purple'),d.box(515,95,210,['人的决策','产品／营销／服务'],'orange'),d.box(755,95,210,['业务反馈','转化／使用体验'],'green')]
    for a,b in zip(nodes,nodes[1:]):d.right(a,b)
    d.path('M860,208 L860,255 L140,255 L140,215')
    d.box(80,310,385,['供应商成本','模型与数据处理'],'blue')
    d.box(535,310,385,['客户账单','SaaS 许可＋数据用量包'],'green');d.save()


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

#!/usr/bin/env python3
"""Render clean concept figures for Zhang Xiaojun podcast notes.

The generated podcast notes intentionally avoid repeated fixed-camera speaker
frames. These compact teaching diagrams are the visual spine for episodes with
no slides or screen-share content.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]

FONT_CANDIDATES = [
    Path("/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf"),
    Path("/usr/share/fonts/truetype/arphic/uming.ttc"),
    Path("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"),
]

FONT_PATH = next((p for p in FONT_CANDIDATES if p.exists()), FONT_CANDIDATES[-1])

W, H = 1600, 960

COLORS = {
    "bg": "#FAFAF7",
    "ink": "#1D2430",
    "muted": "#6A7280",
    "line": "#D7DDE5",
    "card": "#FFFFFF",
    "shadow": "#E8ECEF",
    "blue": "#2D6CDF",
    "green": "#17895A",
    "amber": "#C77914",
    "red": "#B5453F",
    "purple": "#6D5BAA",
    "teal": "#087D86",
    "slate": "#465568",
}

PALETTE = [
    COLORS["blue"],
    COLORS["green"],
    COLORS["amber"],
    COLORS["purple"],
    COLORS["teal"],
    COLORS["red"],
    COLORS["slate"],
]


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size)


def text_width(text: str, fnt: ImageFont.FreeTypeFont) -> float:
    return fnt.getlength(text)


def wrap_text(text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words: list[str] = []
    buf = ""
    for ch in text:
        if ch.isspace():
            if buf:
                words.append(buf)
                buf = ""
            continue
        if "\u4e00" <= ch <= "\u9fff":
            if buf:
                words.append(buf)
                buf = ""
            words.append(ch)
        else:
            buf += ch
    if buf:
        words.append(buf)

    lines: list[str] = []
    cur = ""
    for token in words:
        trial = cur + token
        if cur and text_width(trial, fnt) > max_width:
            lines.append(cur)
            cur = token
        else:
            cur = trial
    if cur:
        lines.append(cur)

    compact: list[str] = []
    for line in lines:
        if compact and len(line) == 1 and text_width(compact[-1] + line, fnt) <= max_width:
            compact[-1] += line
        else:
            compact.append(line)
    return compact


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 8,
) -> int:
    x, y = xy
    for line in wrap_text(text, fnt, max_width):
        draw.text((x, y), line, fill=fill, font=fnt)
        y += fnt.size + line_gap
    return y


def canvas(title: str, subtitle: str = "") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (W, H), COLORS["bg"])
    draw = ImageDraw.Draw(image)
    draw.text((78, 48), title, fill=COLORS["ink"], font=font(42))
    if subtitle:
        draw.text((80, 108), subtitle, fill=COLORS["muted"], font=font(23))
    draw.line((76, 150, W - 76, 150), fill=COLORS["line"], width=2)
    return image, draw


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str | None = None) -> None:
    color = color or COLORS["muted"]
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=4)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 17
    p1 = (x2 + size * math.cos(angle + math.pi * 0.84), y2 + size * math.sin(angle + math.pi * 0.84))
    p2 = (x2 + size * math.cos(angle - math.pi * 0.84), y2 + size * math.sin(angle - math.pi * 0.84))
    draw.polygon([end, p1, p2], fill=color)


def card(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    body: str,
    color: str,
    title_size: int = 25,
    body_size: int = 20,
) -> None:
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle((x1 + 5, y1 + 7, x2 + 5, y2 + 7), radius=18, fill=COLORS["shadow"])
    draw.rounded_rectangle(xy, radius=18, fill=COLORS["card"], outline=color, width=3)
    draw.rounded_rectangle((x1, y1, x1 + 12, y2), radius=6, fill=color)
    draw.text((x1 + 30, y1 + 24), title, fill=color, font=font(title_size))
    draw_text(draw, (x1 + 30, y1 + 68), body, font(body_size), COLORS["ink"], x2 - x1 - 56, 7)


def save(image: Image.Image, rel: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, quality=95)


def draw_flow(rel: str, title: str, subtitle: str, nodes: list[tuple[str, str]], colors: list[str] | None = None) -> None:
    image, draw = canvas(title, subtitle)
    count = len(nodes)
    card_w = 250 if count >= 5 else 300
    gap = (W - 160 - card_w * count) // max(1, count - 1)
    y = 360
    for i, (node_title, body) in enumerate(nodes):
        x = 80 + i * (card_w + gap)
        color = (colors or PALETTE)[i % len(colors or PALETTE)]
        card(draw, (x, y, x + card_w, y + 160), node_title, body, color, 23, 18)
        if i < count - 1:
            arrow(draw, (x + card_w + 5, y + 80), (x + card_w + gap - 8, y + 80))
    draw.text((135, 760), "读图：从左到右看依赖关系；正文负责展开细节，图只保留骨架。", fill=COLORS["muted"], font=font(26))
    save(image, rel)


def draw_split(rel: str, title: str, subtitle: str, left: tuple[str, str], right: tuple[str, str]) -> None:
    image, draw = canvas(title, subtitle)
    card(draw, (95, 250, 720, 700), left[0], left[1], COLORS["blue"], 28, 22)
    card(draw, (880, 250, 1505, 700), right[0], right[1], COLORS["green"], 28, 22)
    arrow(draw, (735, 475), (865, 475))
    save(image, rel)


def draw_grid(rel: str, title: str, subtitle: str, nodes: list[tuple[str, str]]) -> None:
    image, draw = canvas(title, subtitle)
    cols = 3
    card_w, card_h = 430, 150
    x0, y0 = 95, 235
    for i, (node_title, body) in enumerate(nodes):
        row, col = divmod(i, cols)
        x = x0 + col * 505
        y = y0 + row * 205
        card(draw, (x, y, x + card_w, y + card_h), node_title, body, PALETTE[i % len(PALETTE)], 23, 18)
    save(image, rel)


def draw_radial(rel: str, title: str, subtitle: str, center_title: str, nodes: list[tuple[str, str]]) -> None:
    image, draw = canvas(title, subtitle)
    cx, cy = 800, 500
    draw.ellipse((660, 360, 940, 640), fill=COLORS["card"], outline=COLORS["ink"], width=3)
    draw_text(draw, (710, 450), center_title, font(34), COLORS["ink"], 190, 8)
    positions = [
        (105, 235, 430, 370),
        (575, 205, 900, 340),
        (1070, 235, 1395, 370),
        (1070, 635, 1395, 770),
        (575, 670, 900, 805),
        (105, 635, 430, 770),
    ]
    for i, (node_title, body) in enumerate(nodes[:6]):
        xy = positions[i]
        color = PALETTE[i % len(PALETTE)]
        card(draw, xy, node_title, body, color, 22, 17)
        arrow(draw, ((xy[0] + xy[2]) // 2, (xy[1] + xy[3]) // 2), (cx, cy), color)
    save(image, rel)


def draw_stack(rel: str, title: str, subtitle: str, nodes: list[tuple[str, str]]) -> None:
    image, draw = canvas(title, subtitle)
    x1, x2 = 360, 1240
    y = 220
    for i, (node_title, body) in enumerate(nodes):
        color = PALETTE[i % len(PALETTE)]
        card(draw, (x1, y, x2, y + 110), node_title, body, color, 24, 18)
        if i < len(nodes) - 1:
            arrow(draw, ((x1 + x2) // 2, y + 116), ((x1 + x2) // 2, y + 155))
        y += 145
    save(image, rel)


SPECS: list[tuple[str, str, str, str, object]] = [
    # EP104 Rokid / Zhu Mingming
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/rokid-founder-timeline.png", "flow", "Rokid 创业时间线", "从阿里收购、M Lab 到 AI/AR 硬件十一年", [("First Startup", "阿里收购"), ("Alibaba", "M Lab"), ("Rokid", "AI 硬件"), ("2019", "切换 AR"), ("Glasses", "智能眼镜")]),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/ai-to-hardware-spillover.png", "flow", "AI 软件能力外溢到硬件", "从云端模型到随身智能和具身智能", [("AI Model", "软件能力"), ("Device", "入口硬件"), ("Wearable", "随身智能"), ("Embodied", "具身智能"), ("Ecosystem", "应用生态")]),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/ar-pivot-decision.png", "split", "2019：从 AI 音箱转向 AR", "一周内切换赛道，代价是组织重构", (("AI 音箱", "语音入口竞争激烈，巨头资源强。"), ("AR 眼镜", "新入口未定型，硬件和场景都有机会。"))),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/hardware-black-forest.png", "radial", "硬件创业黑森林", "供应链、现金流、库存、渠道和巨头竞争同时存在", "Hardware", [("供应链", "交付"), ("现金流", "生死线"), ("库存", "风险"), ("渠道", "触达"), ("巨头", "竞争"), ("PMF", "验证")]),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/smart-glasses-stage.png", "flow", "智能眼镜阶段判断", "从黑莓到 iPhone 1 之间，入口正在形成", [("Feature", "单点功能"), ("BlackBerry", "早期形态"), ("iPhone 1", "入口确立"), ("Platform", "生态"), ("Mass Market", "规模化")]),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/china-us-glasses-definition.png", "split", "中美定义智能眼镜的差异", "产品定义、渠道和用户场景不同", (("中国", "硬件供应链、价格带、线下渠道和快速迭代。"), ("美国", "平台生态、开发者、隐私监管和品牌入口。"))),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/startup-vs-giants-four-no.png", "grid", "创业公司对巨头的四个不", "马云提醒：创业公司要找巨头不愿、不敢、不能、不屑做的机会", [("不愿", "小市场"), ("不敢", "高风险"), ("不能", "组织限制"), ("不屑", "低端/长尾"), ("速度", "小团队"), ("专注", "单点突破")]),
    ("youtube/zhangxiaojun/ep104-qW-kgogQwJc/figures/playfulness-culture.png", "radial", "玩心文化", "硬件创业需要 trouble maker 式的问题意识", "Play", [("好奇", "发现问题"), ("动手", "做样机"), ("冒险", "试错"), ("审美", "体验"), ("团队", "价值观")]),
    # Nuclear fusion special pVuE4J5cn98
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/fusion-energy-chain.png", "flow", "可控核聚变能量链", "从燃料、等离子体到电网输出的核心路径", [("Fuel", "氘/氚"), ("Plasma", "高温等离子体"), ("Confinement", "磁约束"), ("Heat", "能量交换"), ("Grid", "发电并网")]),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/tokamak-stack.png", "stack", "托卡马克系统栈", "磁体、真空室、等离子体控制和能量转换层层耦合", [("超导磁体", "产生约束磁场"), ("真空室", "承载等离子体"), ("加热系统", "达到反应温度"), ("控制系统", "稳定运行"), ("热工系统", "取热发电")]),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/fusion-bottlenecks.png", "grid", "核聚变关键瓶颈", "科学、工程、材料、资金和监管同时过线", [("等离子体", "稳定约束"), ("材料", "中子辐照"), ("磁体", "高场超导"), ("热工", "取热转换"), ("资金", "长周期消耗"), ("监管", "安全许可")]),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/energy-ai-loop.png", "flow", "AI 与能源约束", "AGI 不一定怕人类，但一定怕断电", [("AI", "算力需求"), ("Data Center", "电力负载"), ("Energy", "稳定供给"), ("Fusion", "长期解法"), ("Civilization", "上限提升")]),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/fusion-startup-roadmap.png", "flow", "核聚变创业路线图", "从物理验证到示范电厂，再到商业电站", [("Physics", "物理增益"), ("Device", "实验装置"), ("Pilot", "示范电厂"), ("Grid", "并网验证"), ("Commercial", "商业复制")]),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/public-private-fusion.png", "split", "公共大科学 vs 私营创业", "核聚变从国家工程走向创业公司竞速", (("公共大科学", "长期投入、国际协作、基础验证。"), ("私营创业", "工程压缩、资本下注、目标电厂。"))),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/holy-grail-tradeoff.png", "radial", "能源圣杯的代价", "无限能源愿景背后是极端工程复杂度", "Fusion", [("高温", "上亿度"), ("约束", "磁场"), ("材料", "寿命"), ("资金", "消耗"), ("时间", "不确定")]),
    ("youtube/zhangxiaojun/special-pVuE4J5cn98/figures/fusion-investment-logic.png", "flow", "聚变投资逻辑", "巨额资本赌的是文明能源上限，而非短期现金流", [("Capital", "长期资金"), ("Milestone", "技术节点"), ("Risk", "物理/工程"), ("Option Value", "能源上限"), ("Return", "产业重构")]),
    # EP106 / subtitle edition Puptr04av5g
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/language-intelligence-jump.png", "split", "语言不是智能本质", "语言是人类智能的一次跃变，而不是智能的唯一入口", (("Intelligence", "视情况对环境做出反应，包含感知、行动和反馈。"), ("Language", "压缩经验、传播知识，让智能发生一次跃变。"))),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/embodied-ai-origin.png", "flow", "具身智能学术边缘史", "从导航、视觉和感知-动作循环走向主流", [("Vision", "视觉流派"), ("Navigation", "早期任务"), ("Perception", "感知"), ("Action", "动作"), ("Embodied AI", "主流渗透")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/perception-action-loop.png", "flow", "Perception-Action Loop", "具身智能的核心叙事是感知、行动和反馈闭环", [("Observe", "看见环境"), ("Infer", "理解状态"), ("Act", "执行动作"), ("Feedback", "获得结果"), ("Adapt", "调整策略")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/academic-path.png", "flow", "王鹤学术路径", "从人类视频、世界模型到家庭机器人研究目标", [("Tsinghua", "本科"), ("Stanford", "博士转向"), ("Video", "人与物交互"), ("Synthetic", "位姿/合成数据"), ("Home Robot", "家庭机器人")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/software-hardware-spiral.png", "flow", "软硬件螺旋上升", "硬件过激会拖累智能，智能成熟又反推硬件", [("Hardware", "本体约束"), ("Data", "动作采集"), ("Model", "智能能力"), ("Scenario", "场景落地"), ("Next Hardware", "反推迭代")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/vlm-vs-llm-data.png", "split", "VLM 为什么弱于 LLM", "视觉覆盖与动作数据远少于文本覆盖", (("LLM", "互联网文字接近人类说过的话，数据覆盖高。"), ("VLM/VLA", "视觉和 action 数据更稀缺，近两年才开始系统采集。"))),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/data-recipe-robotics.png", "stack", "具身数据 Recipe", "真实 1%、合成管线、出货回流和数据飞轮", [("互联网/视觉", "常识预训练"), ("合成数据", "场景和长尾扩增"), ("真实数据", "1% 高价值校准"), ("出货回流", "真实失败反馈"), ("飞轮", "生产力提升")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/two-traps.png", "split", "两个泥潭", "长期漂浮与算不过账都会限制公司天花板", (("长期漂浮", "只有叙事和 demo，迟迟不进入真实场景。"), ("算不过账", "边际成本不降，越交付越重，生产力难成立。"))),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/productivity-as-product.png", "flow", "生产力即产品", "大模型卖智能，具身智能必须卖可衡量生产力", [("Task", "场景任务"), ("Robot", "执行"), ("Cost", "边际成本"), ("Output", "生产力"), ("Revenue", "客户付费")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/capital-chaos-reward.png", "radial", "资本轰炸后的乱象", "谁创造生产力，谁只是在讲故事", "Reward", [("融资", "估值"), ("Demo", "展示"), ("遥操作", "伪装"), ("真实展示", "信任"), ("万台应用", "行业验证")]),
    ("youtube/zhangxiaojun/ep106-Puptr04av5g/figures/robotics-validation-clock.png", "flow", "五年验证时钟", "五年内需要万台以上应用，否则领域叙事会被证伪", [("2025", "资本涌入"), ("场景", "找 PMF"), ("出货", "规模应用"), ("数据", "真实回流"), ("验证", "万台级")]),
    # EP109
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/sim2real-loop.png", "flow", "Sim2Real 闭环", "从仿真生成数据，到现实部署，再用真实反馈修正仿真", [("Simulation", "仿真场景"), ("Synthetic Data", "合成数据"), ("Training", "训练模型"), ("Real World", "现实部署"), ("Feedback", "修正仿真")]),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/real2sim-workflow.png", "flow", "Real2Sim 工作流", "从真实世界采集、重建、校准到可复现仿真", [("Real Data", "采集"), ("Reconstruction", "重建"), ("Calibration", "校准"), ("Simulation", "复现"), ("Evaluation", "评估")]),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/av-vs-embodied-data.png", "split", "智能驾驶 vs 具身智能", "智能驾驶偏视觉游戏，具身智能更依赖物理交互", (("Autonomous Driving", "场景更结构化，视觉和规则强，车辆与地面交互相对稳定。"), ("Embodied AI", "本体多样、接触丰富、物理交互和动作反馈更关键。"))),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/physical-interaction-bottleneck.png", "flow", "物理交互瓶颈", "抓取、接触、力反馈和材料差异让数据特别贵", [("Contact", "接触"), ("Force", "力反馈"), ("Material", "材质"), ("Action", "动作"), ("Failure", "失败回流")]),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/meta-scale-data.png", "split", "Meta 收购 Scale AI 的信号", "未来十万亿公司需要掌握 AI 数据能力", (("Scale AI", "数据生产、标注、流程和人类示范。"), ("Meta", "模型、产品、算力和下一代 AI 数据入口。"))),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/embodied-supply-chain-map.png", "grid", "全球具身智能产业链", "硬件、基座模型、垂直落地和仿真公司分工", [("硬件", "宇树"), ("基座模型", "π/Skild/英伟达/DeepMind"), ("软硬结合", "Figure/Tesla"), ("仿真落地", "光轮"), ("大脑", "字节/小米/理想"), ("数据", "仿真/合成")]),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/china-us-embodied-opportunity.png", "split", "中美具身机会差异", "美国更有模型层机会，中国更适合大脑+本体+场景整合", (("美国", "模型层、frontier lab、资本和通用智能信仰。"), ("中国", "硬件供应链、主机厂、制造和场景落地。"))),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/nvidia-simulation-company.png", "flow", "NVIDIA is a simulation company", "算力、物理引擎、仿真环境和机器人训练连成闭环", [("GPU", "算力"), ("Physics", "物理仿真"), ("Synthetic Data", "合成数据"), ("Robotics", "训练"), ("Deployment", "现实反馈")]),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/cross-universe-model.png", "radial", "跨宇宙、跨世界、跨本体", "终局模型要提升跨环境泛化能力", "Generalize", [("Universe", "仿真世界"), ("World", "任务环境"), ("Embodiment", "不同本体"), ("Data", "多源数据"), ("Policy", "泛化策略")]),
    ("youtube/zhangxiaojun/ep109-pWY0HVUH8GA/figures/embodied-gpt1-stage.png", "flow", "具身智能仍在 GPT-1 阶段", "还没找到稳定 scaling law，数据 recipe 仍在探索", [("Data", "稀缺"), ("Simulation", "未成熟"), ("Recipe", "未知"), ("Scaling Law", "未找到"), ("GPT-1", "早期阶段")]),
    # Lovart special biptonYq-ys
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/lovart-positioning.png", "split", "Lovart：垂直 Agent", "Manus 是通用 Agent，Lovart 面向设计师和创意工作流", (("General Agent", "覆盖多种任务，价值在通用执行和工具编排。"), ("Vertical Agent", "深扎设计场景，价值在专业工作流和审美产出。"))),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/design-agent-workflow.png", "flow", "设计 Agent 工作流", "从 brief 到素材、方案、迭代和交付", [("Brief", "需求"), ("Assets", "素材"), ("Concept", "方案"), ("Iteration", "修改"), ("Delivery", "交付")]),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/startup-survival-path.png", "flow", "应用创业生存线", "补贴战、下架、现金见底、融资困难之后仍然活下来", [("补贴战", "消耗"), ("下架", "打击"), ("4000块现金", "绝境"), ("融不到资", "压力"), ("爆发", "Lovart出圈")]),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/fighting-ceo.png", "radial", "战斗型 CEO", "产品、融资、增长、交付和情绪能量同时拉满", "Fighting\\nCEO", [("产品", "体验"), ("融资", "生存"), ("增长", "传播"), ("团队", "执行"), ("情绪", "能量")]),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/pmf-emotion-loop.png", "flow", "PMF 与情绪回路", "用户认可、产品爆发和创始人快乐互相放大", [("用户惊叹", "反馈"), ("产品传播", "增长"), ("现金缓解", "生存"), ("创始人快乐", "能量"), ("继续迭代", "复利")]),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/agent-app-vs-model.png", "split", "应用 Agent vs 模型能力", "应用创业要在模型红利窗口内沉淀工作流和心智", (("模型红利", "底座变强，能力窗口打开，但会快速同质化。"), ("应用壁垒", "工作流、用户心智、数据回流和垂直体验。"))),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/designers-ai-native.png", "grid", "设计师 AI Native 需求", "专业设计场景需要审美、上下文、版本和交付", [("审美", "taste"), ("上下文", "brand"), ("版本", "iteration"), ("素材", "assets"), ("协作", "team"), ("交付", "files")]),
    ("youtube/zhangxiaojun/special-biptonYq-ys/figures/magic-moment-to-business.png", "flow", "从好爽到生意", "情绪爆点必须转成留存、付费和工作流", [("好爽", "情绪"), ("传播", "流量"), ("留存", "频次"), ("付费", "收入"), ("工作流", "壁垒")]),
    # EP110
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/agent-definition-loop.png", "flow", "Agent 最小定义", "感知环境、决策、行动，再读取反馈", [("Perception", "观察环境"), ("Decision", "选择策略"), ("Action", "执行动作"), ("Feedback", "读取结果"), ("Goal", "推进任务")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/agent-types-map.png", "grid", "Agent 类型地图", "Coding、Search、Tool-use、Computer-use 对应不同环境", [("Coding", "代码环境"), ("Search", "信息检索"), ("Tool-use", "函数/工具"), ("Computer-use", "GUI/浏览器"), ("Language Agent", "语言接口"), ("Family", "多 Agent")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/agent-training-routes.png", "split", "Agent 两条训练路线", "In-context 灵活，End-to-end 稳定但成本高", (("In-Context", "靠强预训练模型、prompt、工具协议和上下文工程，迭代快。"), ("End-to-End", "把行为写进权重，推理稳定，但环境和训练成本更高。"))),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/training-ingredients.png", "flow", "Agent Training 三件套", "合成轨迹、强化学习和安全约束共同构成训练管线", [("Data Synthesis", "轨迹"), ("RL", "可验证奖励"), ("Safety", "沙盒/约束"), ("Evaluation", "任务评测"), ("Deployment", "真实使用")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/kimi-k2-agentic-pipeline.png", "flow", "Kimi K2 Agentic Pipeline", "MuonClip、15.5T tokens、agentic data synthesis 与 joint RL", [("MoE", "1T/32B active"), ("MuonClip", "稳定训练"), ("15.5T tokens", "预训练"), ("Agentic data", "合成轨迹"), ("Joint RL", "环境交互")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/chatgpt-agent-unified-system.png", "flow", "ChatGPT Agent 统一系统", "Operator + Deep Research + ChatGPT + 工具计算机", [("Operator", "网页操作"), ("Deep Research", "信息综合"), ("ChatGPT", "对话/推理"), ("Virtual Computer", "工具执行"), ("User Control", "确认/接管")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/qwen3-coder-stack.png", "flow", "Qwen3-Coder Stack", "480B MoE、256K/1M context、Code RL 与 Long-horizon RL", [("480B MoE", "35B active"), ("7.5T tokens", "70% code"), ("256K/1M ctx", "长上下文"), ("Code RL", "可验证代码"), ("Long RL", "多轮工具")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/manus-context-engineering.png", "grid", "Manus Context Engineering", "KV cache、工具遮蔽、文件系统、todo、错误保留和多样性", [("KV Cache", "稳定前缀"), ("Mask tools", "遮蔽而非移除"), ("Filesystem", "外部记忆"), ("Todo", "操控注意力"), ("Keep errors", "保留失败"), ("Diversity", "避免少样本陷阱")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/report-comparison.png", "grid", "四份报告对照", "Kimi、ChatGPT Agent、Qwen3-Coder、Manus 分别强调不同层", [("Kimi K2", "开放模型"), ("ChatGPT Agent", "统一产品系统"), ("Qwen3-Coder", "代码/RL/工具"), ("Manus", "上下文工程"), ("Training", "轨迹/RL"), ("Deployment", "工具/安全")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/new-agent-paradigm.png", "flow", "Agent 新范式", "数据核心从 input-output 转向 environment + task-reward", [("Old data", "input-output"), ("Environment", "可交互世界"), ("Task", "目标"), ("Reward/Rubric", "可验证反馈"), ("Self-improve", "经验复用")]),
    ("youtube/zhangxiaojun/ep110-8dKBH4x0D9o/figures/family-of-agents.png", "radial", "Family of Agents", "Agent 像拓展的大脑，背后是一支军团", "Agent\\nFamily", [("Coding", "写代码"), ("Search", "查资料"), ("Browser", "操作网页"), ("Memory", "长期状态"), ("Safety", "约束")]),
    # EP111
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/lidar-active-eye.png", "split", "激光雷达：主动的眼睛", "摄像头被动看世界，激光雷达主动发光并测距", (("Camera", "被动接收光线，距离需要从图像中估计。"), ("LiDAR", "主动发射激光，通过飞行时间直接测距。"))),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/cost-down-stack.png", "flow", "99.5% 降本路径", "从实验室原型到车规量产，需要设计、芯片、供应链和制造共同压价", [("原型", "高成本"), ("设计降本", "重构方案"), ("芯片自研", "核心部件"), ("供应链", "规模采购"), ("量产", "车规成本")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/hesai-timeline.png", "flow", "禾赛 11 年创业路线", "从实验室技术、第一笔大单，到进入汽车大本营", [("实验室技术", "传感器"), ("创业", "三人平分"), ("大单", "2000万"), ("倒戈", "客户转向"), ("汽车大本营", "主机厂")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/three-founder-equity.png", "split", "三人平分股份", "罕见股权结构背后是信任、能力互补和长期绑定", (("常见结构", "一号位控股，其他创始人按贡献分配。"), ("三人平分", "强化共同体，但也要求高度信任和治理能力。"))),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/financing-cashflow.png", "flow", "融资与现金流", "硬件创业不能只讲故事，必须跨过样机、订单和现金流", [("技术故事", "能融钱"), ("样机", "能展示"), ("订单", "能验证"), ("回款", "能活着"), ("量产", "能扩张")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/first-big-order.png", "flow", "第一笔 2000 万大单", "大单让技术团队第一次被市场验证，也把交付压力放大", [("客户需求", "真实场景"), ("报价", "商业判断"), ("签单", "2000万"), ("交付", "组织压力"), ("信用", "下一阶段")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/pricing-logic.png", "grid", "硬件定价心思", "定价不是成本加成，而是客户价值、风险和市场位置", [("成本", "BOM/制造"), ("价值", "安全/性能"), ("竞品", "替代价格"), ("客户", "预算/风险"), ("规模", "降本预期"), ("战略", "进入主机厂")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/customer-defection.png", "flow", "客户开始倒戈", "硬件供应链的突破时刻，是客户愿意从旧方案转向新方案", [("旧供应商", "稳定但贵"), ("新产品", "更低成本"), ("验证", "性能可信"), ("倒戈", "客户转向"), ("行业信号", "拐点")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/auto-maincamp.png", "flow", "进入汽车大本营", "从技术样机到车规供应商，要进入主机厂体系", [("样机", "可用"), ("车规", "可靠性"), ("主机厂", "认证"), ("量产", "交付"), ("产业链", "长期位置")]),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/new-money-old-money.png", "split", "新钱与老钱", "全球化沟通里，不同资本和产业文化有不同信任语言", (("老钱", "重视秩序、历史、稳健和体面。"), ("新钱", "重视速度、增长、技术和重新定义规则。"))),
    ("youtube/zhangxiaojun/ep111-JxEetUlV9RA/figures/national-industrial-opportunity.png", "radial", "国家、民族与产业机会", "硬科技创业常常来自时代、产业链和国家能力的叠加", "Opportunity", [("国家", "产业政策"), ("民族", "长期实力"), ("产业链", "供应能力"), ("技术", "硬科技"), ("市场", "新能源车"), ("企业家", "执行")]),
    # EP112
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/model-company-divergence.png", "grid", "模型公司开始分化", "Gemini/OpenAI 通用，Anthropic Coding+Agentic，Thinking Machines 多模态交互", [("Gemini/OpenAI", "通用模型"), ("Anthropic", "Coding+Agentic"), ("Thinking Machines", "多模态/交互"), ("Grok", "生态定位"), ("Meta", "原创基因弱"), ("F1", "顶级竞赛")]),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/horizontal-vs-vertical.png", "split", "横向全家桶 vs 纵向垂直整合", "ChatGPT 横向套件，Gemini 纵向超级集成", (("横向全家桶", "Chat、搜索、Coding、Agent、Workspace 逐步纳入一个入口。"), ("纵向垂直整合", "TPU、模型、应用、文档、浏览器、OS、视频生态联动。"))),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/intelligence-product-balance.png", "flow", "智能和产品都重要", "智能上限探索必须转成流量、品牌和用户心智", [("智能上限", "模型能力"), ("产品体验", "可用入口"), ("流量", "用户增长"), ("品牌心智", "默认选择"), ("商业化", "收入闭环")]),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/ai-product-mining-window.png", "flow", "AI 产品像挖矿", "Magic Moment 的保鲜窗口正在缩短", [("新能力", "矿脉"), ("首个体验", "挖矿"), ("Magic", "惊叹"), ("窗口缩短", "竞争复制"), ("品牌收益", "营销红利")]),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/l4-experience-map.png", "split", "L4 体验地图", "Deep Research 和 Claude Code 分别代表搜索和软件开发", (("Deep Research", "信息搜索、资料综合、报告生成，接近 L4 研究助理。"), ("Claude Code", "代码理解、修改、测试和长程开发，接近 L4 软件助理。"))),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/google-revaluation.png", "flow", "重新评价 Google", "广告、搜索、Gemini、TPU 和全家桶逻辑会重新汇合", [("Ads", "商业化"), ("Search", "入口"), ("Gemini", "模型"), ("TPU/Cloud", "算力"), ("Ecosystem", "全家桶")]),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/model-vs-product-moat.png", "split", "模型壁垒 vs 产品壁垒", "技术壁垒会被追赶，产品壁垒包含流量、品牌和默认入口", (("模型壁垒", "benchmark、coding、agentic、上下文和推理能力。"), ("产品壁垒", "用户习惯、品牌、入口、数据回流和商业化。"))),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/startup-between-giants.png", "flow", "创业者夹在巨头之间", "技术每月进步，但模型公司也不断吃掉机会", [("技术进步", "兴奋"), ("巨头下场", "绝望"), ("Magic Window", "短窗口"), ("垂直场景", "避开正面"), ("速度", "抢先体验")]),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/agi-bubble-dashboard.png", "grid", "AGI Bubble 仪表盘", "泡沫是否破裂取决于收入、模型进步、CapEx 和产品兑现", [("收入", "真实付费"), ("模型", "持续进步"), ("CapEx", "投资强度"), ("产品", "L4体验"), ("竞争", "巨头压力"), ("预期", "估值泡沫")]),
    ("youtube/zhangxiaojun/ep112-6yExfoTuSWw/figures/chinese-agi-global.png", "split", "华人的 AGI", "全球 AGI 竞赛中，华人团队的技术、产品和商业能力被重新定价", (("优势", "工程速度、产品直觉、全球人才和高强度创业。"), ("挑战", "全球化品牌、资本市场、算力供应和企业销售。"))),
    # EP113
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/infinite-mountain-map.png", "radial", "一座无限的山", "问题不可避免，但问题可以解决；模型进步不断打开新问题", "Infinity", [("雪山", "没有尽头"), ("问题", "不可避免"), ("解决", "可以推进"), ("K2", "新高度"), ("创业", "继续攀登")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/brain-in-vat-to-agent.png", "flow", "从缸中之脑到 Agent", "编程能力和工具使用让模型开始操控数字世界", [("缸中之脑", "只会思考"), ("Code", "长出手"), ("Tools", "多轮使用"), ("World", "外部反馈"), ("Agentic LLM", "闭环行动")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/test-time-scaling-map.png", "flow", "Test-time Scaling", "长思考 RL 和 Agent RL 都在扩展推理时计算", [("Prompt", "任务输入"), ("Reasoning", "长思考"), ("Tool Use", "外部调用"), ("Verification", "验证反馈"), ("More compute", "测试时扩展")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/l1-l5-agent-ladder.png", "flow", "L1 到 L5 不一定串行", "Reasoning 与 Agent 可以并行押注，Claude 是典型例子", [("L1", "聊天"), ("L2", "推理"), ("L3", "工具"), ("L4", "参与创新"), ("L5", "自主系统")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/k2-design-goals.png", "grid", "Kimi K2 设计目标", "基础模型、token efficiency、Agentic 能力和开源同时成立", [("Base Model", "强底座"), ("Token Efficiency", "同数据更聪明"), ("Agentic", "多轮工具"), ("Open Source", "生态扩散"), ("Muon", "优化器"), ("Rephrase", "数据改写")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/token-efficiency-loop.png", "flow", "Token Efficiency 闭环", "数据改写、优化器和训练策略提高每个 token 的收益", [("Raw Data", "原始数据"), ("Rephrase", "改写增强"), ("Muon", "优化器"), ("Training", "更高效率"), ("Capability", "脑子长更多")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/agentic-generalization.png", "split", "Agentic 模型的泛化挑战", "会用工具不等于能泛化到新任务", (("训练内工具", "模型熟悉流程，容易表现很好。"), ("新环境任务", "工具、反馈和目标变化，泛化才是真挑战。"))),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/open-source-strategy.png", "split", "从闭源到开源", "模型与产品完成度、生态传播和商业路径共同影响开源选择", (("闭源", "控制产品体验、商业化和迭代节奏。"), ("开源", "扩大开发者生态、验证基础模型能力、提升信任。"))),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/scaling-data-wall.png", "flow", "Scaling 与数据墙", "数据墙之后，FLOPs、RL、反馈和架构效率重新平衡", [("Data Wall", "高质数据变少"), ("FLOPs", "继续扩算"), ("RL", "测试/交互"), ("Feedback", "外部环境"), ("Architecture", "效率取舍")]),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/linear-attention-iq-risk.png", "split", "Long Context 架构与智商风险", "Linear Attention 降成本，但 bias 可能影响模型能力", (("效率收益", "降低长上下文成本，提升吞吐和部署空间。"), ("能力风险", "架构 bias 可能影响推理、记忆和智商。"))),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/agent-product-boundary.png", "split", "基座模型公司 vs Agent 应用公司", "长期边界取决于模型、数据、工具和用户入口", (("基座模型公司", "模型能力、训练数据、API、平台和生态。"), ("Agent 应用公司", "任务场景、工作流、用户入口和反馈数据。"))),
    ("youtube/zhangxiaojun/ep113-ouG6jrkECrc/figures/rl-management-sft-risk.png", "flow", "用 RL 管理，而不是只用 SFT", "目标、反馈和奖励会塑造团队，但也容易被 hack", [("目标", "定义方向"), ("Reward", "反馈信号"), ("探索", "团队试错"), ("Hack", "钻指标"), ("校正", "回到使命")]),
    # EP102 Zhang Xiangyu multimodal history
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/cv-to-nlp-learning-history.png", "flow", "CV 向 NLP 学习的历史", "从 ImageNet/ResNet 到 ViT、iGPT、MIM 与多模态大模型", [("ImageNet", "数据规模"), ("ResNet", "模型 scaling"), ("ViT", "Transformer 迁移"), ("iGPT/MIM", "NLP范式试验"), ("VLM", "视觉语言对齐")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/static-image-three-way-split.png", "radial", "静态图像的三重割裂", "生成、理解和人类对齐在静态图像中天然分离", "Image", [("生成", "像素分布"), ("理解", "人类语义"), ("对齐", "语言标注"), ("自然", "图像在那里"), ("任务", "后天定义")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/generation-understanding-gap.png", "split", "生成与理解未融合", "两个分支都变强，但放在一起没有 1+1>2", (("理解模型", "看图、视频、语言对齐越来越强。"), ("生成模型", "能生成图像/视频，但可控性和物理约束仍弱。"))),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/next-token-compression-defect.png", "flow", "Next Token Prediction 的缺陷", "压缩分布不等于计算精度，越大会越倾向跳步", [("Data Distribution", "人类语料"), ("Compression", "预测下个token"), ("Shortcut", "跳步"), ("Math", "一步错全错"), ("RL", "目标校正")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/feature-collapse.png", "split", "特征坍缩现象", "生成模型会保留高概率特征，却丢失计算和约束精度", (("分布接近", "像训练语料，压缩率更高。"), ("精度不足", "数学、几何和物理约束不能只靠分布相似。"))),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/rl-cot-pattern.png", "flow", "RL 与 CoT Pattern", "RL 不只是算法名，关键是激发可搜索的思考模式", [("Pretrain", "已有模式"), ("RL", "目标反馈"), ("CoT", "展开步骤"), ("Reflection", "反思"), ("Critical Decision", "关键分支")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/meta-cot-critical-decision.png", "flow", "Meta-CoT 与 Critical Decision", "当一个 token 解决不了分支选择，就需要反思和元思维链", [("State", "当前推理"), ("Branch", "左右分支"), ("One token?", "复杂度不足"), ("Reflect", "扩展动作空间"), ("Meta-CoT", "CoT的CoT")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/visual-long-cot.png", "flow", "视觉空间 Long CoT", "在视觉空间慢思考，把反思模式迁移到多模态推理", [("Image/Video", "视觉输入"), ("Visual Actions", "局部观察/标注"), ("Reason", "空间推理"), ("Reflect", "纠错"), ("Answer", "多模态输出")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/two-leg-roadmap.png", "split", "多模态后续两条腿", "扩充预训练语料，同时扩展动作空间", (("Pretraining Data", "更多视觉、视频、图文、交互和生成过程数据。"), ("Action Space", "反思、局部观察、生成、工具调用和多模型协作。"))),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/long-context-multi-model.png", "flow", "Long Context 与多模型协作", "不用把整本书塞进一个上下文，而是全局规划+局部执行", [("Global Planner", "整体印象"), ("Retrieve/Turn page", "翻书"), ("Local Worker", "局部推理"), ("Feedback", "回传结果"), ("Context Shift", "切换情景")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/online-learning-agent.png", "flow", "在线学习与自主学习", "下一个 GPT-4 时刻可能来自环境反馈和持续自我改进", [("Environment", "外部世界"), ("Agent", "行动"), ("Feedback", "结果"), ("RL/IRL", "目标优化"), ("Online Learning", "持续更新")]),
    ("youtube/zhangxiaojun/ep102-vWrYHvSRz0s/figures/world-model-robotics-gap.png", "split", "世界模型与机器人抢跑", "人没有生成器官，但有世界模型；机器人不能跳过视觉理解", (("World Model", "用于空间推理、物理常识和未来预测。"), ("Robotics", "需要视觉、动作、反馈和本体共同过线。"))),
    # EP97 / Q1 2025 large-model quarterly review
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/q1-model-map.png", "radial", "2025 Q1 大模型季报地图", "Pre-training、Coding、Agent、Online Learning 与全球格局共同构成主线", "Q1\\n2025", [("Pre-training", "上限"), ("Coding", "模型的手"), ("Agent", "新物种"), ("Online", "新范式"), ("产品", "容器和壁垒"), ("格局", "中美/公司")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/pretrain-posttrain-split.png", "split", "Pre-training 与 Post-training", "预训练决定内在上限，后训练和 RL 更像能力塑形", (("Pre-training", "用大规模数据压缩世界，决定模型的知识、表征和潜在能力上限。"), ("Post-training/RL", "把能力对齐到任务、偏好、工具和安全边界，增强可用性。"))),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/coding-as-cyber-environment.png", "flow", "Coding 是赛博世界环境", "代码不是单一技能，而是模型行动、验证和改造数字世界的入口", [("Code", "可读写世界"), ("Tools", "调用系统"), ("Tests", "可验证反馈"), ("Agent", "长程执行"), ("AGI Path", "通用能力")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/openai-anthropic-strategy.png", "split", "OpenAI vs Anthropic", "战略差异是组织能力、价值观和产品路径的表达", (("OpenAI", "模型、消费入口、o 系列和平台野心并行，风险是过早消费互联网化。"), ("Anthropic", "更聚焦安全、企业、Coding 和 Agentic 工作流，组织气质更收敛。"))),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/agi-roadmap-mountain.png", "flow", "AGI 路线山脊", "ChatGPT 只是山脚，后续主峰依次进入更强行动环境", [("ChatGPT", "山脚"), ("Coding", "数字行动"), ("Coding Agent", "长程任务"), ("General Agent", "跨工具"), ("AI4Science", "科学发现"), ("Robotics", "物理世界")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/intelligence-measurement.png", "grid", "智能进步如何衡量", "从生存、探索、自动化，到 token 消耗和任务闭环", [("生存", "适应环境"), ("探索", "发现新策略"), ("自动化", "减少人工"), ("Token", "思考成本"), ("任务", "完成闭环"), ("反馈", "持续改进")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/agent-three-capabilities.png", "grid", "Agent 三个关键能力", "Long context reasoning、Tool use、Instruction following 共同支撑新物种", [("Long Context", "长期任务状态"), ("Tool Use", "改变外部世界"), ("Instruction", "服从复杂目标"), ("Memory", "替代纯长上下文"), ("Feedback", "结果回流"), ("Autonomy", "主动探索")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/online-learning-loop.png", "flow", "Online Learning 闭环", "未来范式级路线：模型在环境里自主探索、获得反馈、更新能力", [("Environment", "环境"), ("Action", "行动"), ("Reward", "反馈"), ("Update", "学习"), ("Memory/Weights", "沉淀经验")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/model-product-moat.png", "split", "模型与产品的壁垒", "裸模型发布时代弱化，Cloud/OS/生态成为防线", (("Model", "能力上限和成本效率很重要，但会被追赶和开源冲击。"), ("Product/OS", "入口、工作流、生态、计费和数据回流形成复合壁垒。"))),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/fire-thieves.png", "grid", "模型盗火者", "Perplexity、Cursor、Manus 把前沿模型能力搬进具体工作流", [("Perplexity", "搜索/研究"), ("Cursor", "编程环境"), ("Manus", "通用执行"), ("容器", "承接智能"), ("成本", "token 经济"), ("壁垒", "工作流沉淀")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/model-company-portfolio.png", "grid", "全球模型公司格局", "不同公司押注模型、产品、生态、开源和资本结构", [("Anthropic", "企业/Coding"), ("OpenAI", "模型+产品"), ("ByteDance", "产品/流量"), ("DeepSeek", "开源效率"), ("SSI/Mira", "研究信仰"), ("Cursor/Manus", "应用执行")]),
    ("youtube/zhangxiaojun/ep97-YshXmh_q_Q4/figures/china-us-geofence.png", "split", "中美 AI 格局", "地缘封锁下，技术创造力比混圈更重要", (("美国", "算力、frontier lab、资本和全球产品入口强。"), ("中国", "工程速度、应用场景、开源效率和产业链执行力强。"))),
    # EP96 / Lang Xianpeng autonomous driving
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/av-ten-year-map.png", "flow", "自动驾驶十年路线图", "从高精地图和激光雷达，到 BEV/Transformer、端到端和世界模型", [("HD Map", "有轨电车"), ("LiDAR Stack", "昂贵传感"), ("BEV", "统一空间"), ("End-to-End", "数据驱动"), ("World Model", "预测未来")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/tesla-updimension.png", "flow", "Tesla 的升维解法", "用车队数据、视觉、芯片和规模化训练解决系统问题", [("Fleet Data", "海量车队"), ("Vision", "低成本感知"), ("Chip", "自研算力"), ("Training", "大规模训练"), ("FSD", "持续迭代")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/hdmap-lidar-vs-vision.png", "split", "高精地图+激光雷达 vs 视觉路线", "一条依赖外部确定性，一条依赖数据和模型泛化", (("HD Map + LiDAR", "用高精地图、主动测距和规则系统降低感知不确定性，但成本高、维护重。"), ("Vision + Model", "用摄像头、车队数据和模型学习解决长尾，成本低但训练难。"))),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/sensor-cost-stack.png", "stack", "自动驾驶成本栈", "早期方案被传感器、计算平台和工程车成本拖住", [("多颗 LiDAR", "50-60万/台"), ("传感器套件", "摄像头/雷达/定位"), ("计算平台", "GPU/车规芯片"), ("工程车", "改装和维护"), ("量产约束", "成本必须下降")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/camera-lidar-tradeoff.png", "split", "Camera 与 LiDAR 的取舍", "LiDAR 直接给距离，Camera 给语义和低成本规模", (("LiDAR", "主动测距，几何直接，夜间稳定；但成本、外观和量产规模有压力。"), ("Camera", "便宜、信息密度高、可规模部署；但需要模型从图像中学深度和语义。"))),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/e2e-stack.png", "flow", "端到端自动驾驶栈", "从传感器输入到轨迹输出，中间层逐步被学习系统压缩", [("Sensors", "图像/雷达"), ("BEV", "空间表征"), ("Planning", "规划意图"), ("Trajectory", "轨迹"), ("Control", "执行")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/l3-l4-ladder.png", "split", "L3 不是 L2 的延长", "郎咸朋强调 L3 更像 L4 的先导，而不是辅助驾驶线性升级", (("L2", "人负责，系统辅助；失败时驾驶员随时接管。"), ("L3/L4", "系统承担责任，需要设计运行域、接管边界和安全冗余。"))),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/e2e-rl-worldmodel.png", "flow", "端到端 + VLM + 世界模型", "从模仿轨迹走向强化学习和未来状态预测", [("Data", "驾驶轨迹"), ("E2E", "端到端策略"), ("VLM", "语义理解"), ("World Model", "预测后果"), ("RL", "闭环优化")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/ideal-av-data-loop.png", "flow", "理想智驾数据闭环", "量产车队、长尾 case、训练和上线反馈形成飞轮", [("Fleet", "量产车队"), ("Cases", "长尾问题"), ("Label/Train", "标注训练"), ("Deploy", "OTA上线"), ("Feedback", "真实反馈")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/weicheng-project.png", "radial", "卫城项目压力场", "技术路线、供应商、组织尊严和量产节点同时挤压", "Project\\nWeicheng", [("技术", "端到端"), ("供应商", "博弈"), ("组织", "站着死"), ("量产", "节点"), ("领导", "高压"), ("团队", "韧性")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/av-org-leadership.png", "flow", "自动驾驶组织闭环", "技术判断、老板压力、团队执行和安全责任必须同时成立", [("判断", "技术路线"), ("压力", "高层要求"), ("执行", "工程团队"), ("验证", "安全评测"), ("信任", "用户体验")]),
    ("youtube/zhangxiaojun/ep96-qtugoE1xQZk/figures/av-terms-map.png", "grid", "自动驾驶关键术语地图", "BEV、Transformer、E2E、VLM、World Model 和 RL 的关系", [("BEV", "鸟瞰空间"), ("Transformer", "统一建模"), ("E2E", "输入到轨迹"), ("VLM", "语义理解"), ("World Model", "预测未来"), ("RL", "闭环优化")]),
    # EP95 / Manus founder Xiao Hong
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/xiaohong-relay-interview.png", "flow", "肖弘接力式访谈地图", "两次访谈记录 AI 应用创业者在不稳定环境中的连续思考", [("2024 秋", "融资后"), ("第一段创业", "连续创业"), ("Monica", "浏览器插件"), ("2025 春节", "DeepSeek冲击"), ("Manus", "Agent第一枪")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/founder-cycle.png", "radial", "连续创业者循环", "技能、资本、市场、产品和心态不断出现新维度", "Founder", [("技能点", "产品/工程"), ("资本", "融资/稀释"), ("市场", "泡沫/窗口"), ("产品", "等待模型"), ("心态", "昂贵生活"), ("博弈", "成为变量")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/vc-expensive-capital.png", "split", "VC 是昂贵的集资手段", "贵不在困难时，而在公司变好时", (("困难时", "钱救命，稀释看起来可接受。"), ("变好时", "高速增长和大机会出现后，早期稀释成本被放大。"))),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/predict-giants.png", "flow", "预判大厂的预判", "等待、诱惑和大空头式反共识共同构成关键转折", [("观察", "大厂动作"), ("预判", "大厂预判"), ("等待", "不乱动"), ("诱惑", "资本/市场"), ("转折", "反共识时刻")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/monica-product-evolution.png", "flow", "Monica 产品演进", "从浏览器插件、ChatGPT for Google 到 AI 应用平台", [("Plugin", "浏览器插件"), ("ChatGPT for Google", "搜索补充"), ("Monica.im", "多场景入口"), ("用户反馈", "高频使用"), ("Agent", "下一阶段")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/ai-app-taxonomy.png", "grid", "AI 应用分类方法", "主场景补充、模型能力变化、特定领域外溢", [("主场景补充", "增强已有工作流"), ("能力变化", "新模型打开新功能"), ("领域外溢", "能力迁移到垂直场景"), ("入口", "用户高频位置"), ("时机", "等模型成熟"), ("壁垒", "数据/流程")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/wait-for-model-capability.png", "flow", "先做好应用，等模型能力到来", "预判下一个模型能力，提前站到产品位置上", [("Forecast", "预判能力"), ("Build shell", "先做容器"), ("Wait", "等待模型"), ("Magic moment", "能力到来"), ("Scale", "放大增长")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/model-company-vs-app-company.png", "split", "大模型原厂 vs 应用公司", "原厂做通用能力，应用公司做场景、容器和反馈", (("模型原厂", "训练底座、API、通用产品和平台生态。"), ("应用公司", "找主场景、做工作流、拿用户反馈、沉淀垂直壁垒。"))),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/deepseek-product-lesson.png", "split", "DeepSeek 产品启发", "最佛的团队取得最好结果，给应用创业者精神鼓励", (("DeepSeek", "用能力、开源和低姿态重写预期。"), ("应用创业", "少一点表演，多一点产品真实价值。"))),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/manus-agent-thesis.png", "flow", "Manus：国内 Agent 第一枪", "从任务、工具、环境、记忆到可交付结果", [("Task", "用户目标"), ("Tools", "浏览器/文件/API"), ("Environment", "可操作世界"), ("Memory", "任务状态"), ("Deliverable", "结果交付")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/aha-lifeform.png", "radial", "A-ha Moment：制造生命感", "Agent 产品从工具感走向会行动的生命感", "A-ha", [("目标", "自主拆解"), ("行动", "调用工具"), ("反馈", "自我修正"), ("状态", "长期任务"), ("惊讶", "超预期"), ("信任", "可控交付")]),
    ("youtube/zhangxiaojun/ep95-VdWEE6vOYRw/figures/founder-game-thinking.png", "split", "Founder 的博弈思维", "不是线性外推，而是让自己成为重要变量", (("逻辑推理", "在既有条件下推演最优解，容易被线性外推限制。"), ("博弈思维", "改变条件、影响对手预期，让自己成为局面里的变量。"))),
    # EP101 YouWare / Ming Chaoping
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/product-manager-three-stations.png", "flow", "产品经理三站", "OnePlus、ByteDance、Moonshot 形成产品判断底盘", [("OnePlus", "体验"), ("ByteDance", "数据/增长"), ("Moonshot", "模型/AI"), ("YouWare", "Agent应用"), ("CEO", "第一次创业")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/experience-not-data.png", "split", "体验不是数据", "续航数据和续航体验不划等号", (("Data", "平均续航、转化、留存、点击等可量化指标。"), ("Experience", "焦虑、敏感点、临界状态和用户主观感受。"))),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/bitter-lesson-pivot.png", "flow", "Bitter Lesson 转向", "想雕花和加脚手架，可能背离时代最大变量", [("Scaffold", "雕花"), ("Launch?", "未上线"), ("Wrong variable", "背离模型"), ("Stop", "叫停"), ("Rethink", "重新定义")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/token-consumption-speed.png", "flow", "Token 消耗速度", "AI 时代产品指标从点击/时长转向更高效消耗智能", [("User intent", "需求"), ("Container", "容器/环境"), ("Agent action", "执行"), ("Tokens", "智能消耗"), ("Value", "per token valuation")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/container-environment.png", "split", "壳、容器与环境", "只给 Chatbot 输入框不够，环境是人的反应器", (("Shell", "表层入口，只承接输入输出。"), ("Environment", "承载上下文、行动、反馈和人的反应。"))),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/vibe-coder-new-crowd.png", "flow", "Vibe Coder 新人群", "Coding 像 Camera，工具变化会创造新创作者人群", [("Camera", "单反用户"), ("Phone", "手机摄影师"), ("Coding", "工程师"), ("AI Coding", "Vibe Coder"), ("New apps", "新生态")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/agent-ecosystem-two-models.png", "split", "Agent 两种生态", "新加坡式小而强 vs 美国式大而全", (("Singapore-like", "小而强、开放连接、依赖外部生态。"), ("US-like", "大而全、自给自足、平台能力完整。"))),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/page-rank-to-agent-rank.png", "flow", "PageRank 到 AgentRank", "网页被链接排序，Agent 可能被调用和信任排序", [("Page", "网页"), ("Links", "链接"), ("PageRank", "排序"), ("Agent", "能力节点"), ("AgentRank", "调用/信任")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/agent-network-effect.png", "radial", "Agent 网络效应", "Agent 之间的调用、身份、信任和工具会形成生态", "Agent\\nNetwork", [("Identity", "身份"), ("Trust", "信任"), ("Tools", "工具"), ("Users", "用户"), ("Calls", "调用"), ("Rank", "排序")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/os-agent-living-system.png", "flow", "OS Agent：它是活的", "基础模型造更聪明的人，应用公司提供环境和经验", [("Model", "变聪明"), ("Environment", "使用环境"), ("Experience", "经验适配"), ("OS Agent", "活系统"), ("Feedback", "持续反馈")]),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/ape-with-fire-stick.png", "split", "今天的 Agent 阶段", "像大猩猩刚拿起烧火棍，能力粗糙但方向危险且巨大", (("Primitive", "能力粗糙、试错多、砸东西。"), ("Potential", "工具一旦变好，生产方式会重排。"))),
    ("youtube/zhangxiaojun/ep101-a04POJEknCY/figures/ego-countermeasure.png", "flow", "对抗 Ego", "第一次做 CEO，要用第三方视角、情绪价值和棋手心态约束自我", [("Third view", "第三方视角"), ("Emotion", "情绪价值"), ("Thin ice", "如履薄冰"), ("Anti-ego", "对抗自我"), ("Player", "棋手")]),
    # EP100 Mercedes-Benz / Ola Kallenius
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/mercedes-transition-map.png", "radial", "139 岁奔驰的转型地图", "中国速度、电动化、AI 和豪华品牌同时重构", "Mercedes", [("China", "速度/创新"), ("EV", "零排放"), ("AI", "智能汽车"), ("Luxury", "品牌体验"), ("CEO", "监护人"), ("R&D", "全球网络")]),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/china-market-flywheel.png", "flow", "中国市场飞轮", "中国速度、中国研发、中国成果反哺全球", [("China speed", "快节奏"), ("Local R&D", "北京/上海"), ("Tech partners", "腾讯/高德"), ("Product fit", "中国体验"), ("Global reuse", "为世界服务")]),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/luxury-vs-electrification.png", "split", "豪华战略 vs 电动化战略", "康林松强调两者不是二选一", (("Luxury Strategy", "品牌、体验、保值、高端利润和现金流。"), ("Electrification", "全产品组合推进，按市场节奏提供选择。"))),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/mbos-architect-chef.png", "flow", "MBOS：架构师与厨师", "核心架构自控，同时整合伙伴技术", [("MBOS", "操作系统"), ("In-house code", "核心控制"), ("Partners", "高通/腾讯/高德"), ("Integration", "整合体验"), ("Luxury control", "奔驰质感")]),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/ai-car-stack.png", "flow", "AI 汽车技术栈", "芯片、传感器、云、生成式 AI 和虚拟助手共同构成体验", [("Sensors", "感知"), ("Compute", "车载算力"), ("Cloud", "连接"), ("GenAI", "智能助手"), ("Safety", "零事故愿景")]),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/technology-democratization-luxury.png", "split", "技术民主化与豪华车", "技术不再稀缺时，豪华要靠综合体验继续成立", (("Tech democratization", "AI、电动化和智能座舱逐渐普及。"), ("Luxury", "安全、质量、设计、体验、品牌和长期价值。"))),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/transformation-ceo-loop.png", "flow", "转型期 CEO 决策闭环", "51/49 决策、持续学习、必要时修正", [("Uncertainty", "不确定"), ("Decision", "51/49"), ("Observe", "收集信息"), ("Correct", "不怕改"), ("Guardian", "品牌监护人")]),
    ("youtube/zhangxiaojun/ep100-9Yjws_rt378/figures/guardian-of-brand.png", "split", "品牌监护人", "成功不是单一技术指标，而是交接时品牌更强", (("短期指标", "市场份额、利润率、技术领先、销量。"), ("监护人目标", "品牌、客户体验、财务实力和创新实力共同提升。"))),
    # EP115
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/second-half-map.png", "radial", "AI 下半场地图", "从模型能力走向 Agent、系统、交互和人类全局", "Second\\nHalf", [("人", "语言/非共识"), ("系统", "任务/环境"), ("奖励", "自我探索"), ("边界", "interface"), ("全局", "单极/多元")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/language-generalization.png", "split", "语言是泛化工具", "人类用语言压缩经验，Agent 用语言连接任务和世界", (("人类语言", "把经验、规则、目标和抽象关系压缩成可传播工具。"), ("语言 Agent", "用自然语言表示任务、规划、工具调用和反馈。"))),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/agent-two-core-questions.png", "flow", "Agent 研究的两个核心", "有价值的任务/环境 + 简单通用的方法", [("任务", "现实相关"), ("环境", "可交互"), ("方法", "简单通用"), ("泛化", "跨环境"), ("系统", "可扩展")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/agent-history-waves.png", "flow", "Agent 三波兴衰", "方法线和任务线相辅相成，不能只看算法", [("古典 Agent", "决策/环境"), ("RL Agent", "奖励探索"), ("LLM Agent", "语言工具"), ("任务线", "环境定义"), ("方法线", "通用算法")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/reward-multi-agent.png", "split", "Agent 两个关键方向", "拥有自己的 reward，与多智能体形成组织结构", (("Reward", "让 Agent 自己探索、试错和优化，而不是只模仿。"), ("Multi-Agent", "让多个 Agent 协作、分工、竞争并形成组织。"))),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/code-affordance.png", "flow", "Code 是关键 Affordance", "代码让 AI 从语言进入数字世界行动", [("语言", "表达意图"), ("Code", "可执行动作"), ("API", "连接工具"), ("数字世界", "可操作环境"), ("Agent", "闭环执行")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/reward-definition-problem.png", "flow", "奖励定义问题", "现实任务的 reward 难在长期、稀疏和不可完全观测", [("目标", "想要什么"), ("反馈", "怎么判断"), ("探索", "如何试错"), ("泛化", "跨任务"), ("安全", "别钻空子")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/interface-superapp.png", "grid", "吞噬边界：Interface 决定机会", "不同交互方式可能产生不同 Super App", [("Chatbot", "人形对话"), ("Assistant", "个人助理"), ("Her", "情感接口"), ("Non-human UI", "非人交互"), ("Super App", "入口聚合"), ("Startup", "新界面机会")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/chatbot-to-agent.png", "flow", "Chatbot 到 Agent", "模型公司的聊天系统会自然演化成 Agent 系统", [("Chatbot", "对话入口"), ("Memory", "长期状态"), ("Tools", "调用能力"), ("Tasks", "执行任务"), ("Agent", "系统闭环")]),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/single-pole-vs-plural.png", "split", "既单极又多元", "重要模型公司会成为关键一环，但世界不必被单极垄断", (("单极趋势", "模型、算力、数据和 Super App 会集中。"), ("多元机会", "不同 interface、任务、生态和组织会产生新入口。"))),
    ("youtube/zhangxiaojun/ep115-gQgKkUsx5q0/figures/different-bet.png", "flow", "Different Bet", "超越霸主需要不同下注，而不是复制已有主线", [("霸主路径", "已有优势"), ("复制", "很难超越"), ("Different Bet", "新界面/任务"), ("新上限", "更高机会")]),
    # EP116
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/company-history-map.png", "flow", "明略 19 年公司史", "第一段创业、第二段创业、痛苦急转和企业级 AI 重新连成一条线", [("第一段", "秒针/推荐系统"), ("合并", "明略/Edmaster"), ("第二段", "Palantir/ToB"), ("急转", "现金流/聚焦"), ("AI时代", "Agentic Model")]),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/palantir-to-b-logic.png", "split", "Palantir 与中国 ToB", "不是照搬 ToG，而是寻找数据、场景和交付闭环", (("Palantir", "政府/企业数据整合，强工程交付和分析平台。"), ("明略路径", "从 ToG/ToB 经验转向企业私有数据和行业场景。"))),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/conversational-data-acquisition.png", "flow", "Conversational Data 线索", "并购不是只买应用，而是买数据入口和 AI 场景", [("企业微信", "安装基础"), ("微伴/CRM", "销售客服对话"), ("Conversational AI", "理解对话"), ("并购", "拿到入口"), ("AI产品", "从数据出发")]),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/two-b-company-turnaround.png", "flow", "ToB 公司痛苦急转", "战场过宽、现金流压力和经营能力迫使公司重新聚焦", [("战场过宽", "多业务线"), ("成本压力", "月烧钱"), ("痛苦年份", "2022"), ("聚焦", "收缩战线"), ("造血", "经营能力")]),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/private-data-value.png", "split", "私有 Data 的差异化价值", "公开数据卖 token 会卷，私有数据能形成行业价值", (("公开数据", "基础模型同质化，token 价格趋向电费化。"), ("私有数据", "流程、客户、交易、对话和行业知识形成差异化。"))),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/enterprise-agentic-model.png", "flow", "企业级 Agentic Model", "从私有数据到工具调用，再到企业工作流执行", [("私有数据", "企业上下文"), ("模型", "理解/推理"), ("Tool Use", "调用系统"), ("Agent", "执行任务"), ("工作流", "可审计交付")]),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/deepminer-product-loop.png", "flow", "DeepMiner 产品闭环", "用 AI 挖掘企业数据中的规则、风险和行动线索", [("数据接入", "多系统"), ("挖掘", "DeepMiner"), ("洞察", "数值游戏"), ("行动", "Agent/工具"), ("反馈", "业务结果")]),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/supply-demand-relation.png", "split", "供给侧能力 vs 链接网络", "只做连接但不掌握供给侧能力的网络会变危险", (("链接网络", "撮合、分发、关系链，价值依赖网络位置。"), ("供给侧能力", "真正提供产品、数据、工具、模型和交付能力。"))),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/new-production-relation.png", "radial", "AI 带来的新生产关系", "模型、工具、Agent、私有数据和人类合伙人重新分工", "Production\\nRelation", [("模型", "认知能力"), ("工具", "执行接口"), ("数据", "企业资产"), ("Agent", "自动协作"), ("人", "老板/合伙人")]),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/boss-partner-org.png", "split", "老板与合伙人组织", "企业可能从雇员组织转向少数老板和大量 AI 合伙人", (("传统组织", "老板、管理层、员工，靠人力流程交付。"), ("AI组织", "老板定义目标，合伙人和 Agent 共同承担结果。"))),
    ("youtube/zhangxiaojun/ep116-khrOsS7YQn4/figures/happy-founder-mission.png", "flow", "幸福 Founder 的使命对齐", "个人使命、家庭使命和公司使命高度相关", [("个人使命", "长期问题"), ("家庭使命", "稳定能量"), ("公司使命", "客户价值"), ("延迟满足", "扛题能力"), ("幸福", "持续投入")]),
    # EP117
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/paper-reading-loop.png", "flow", "用 AI 学 AI 的论文阅读闭环", "翻译、提问、路书、复盘和分享让论文不再只是 PDF", [("选题", "找到问题"), ("翻译", "跨过语言"), ("追问", "用 AI 辅助"), ("路书", "连成地图"), ("复盘", "开源分享")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/four-part-history-map.png", "radial", "36 篇论文的四条主线", "模型范式、Infra/数据、语言模型和多模态共同构成 AI 变迁史", "AI\\nHistory", [("模型范式", "架构/训练"), ("Infra", "并行/集群"), ("数据", "规模/质量"), ("语言模型", "预训练/后训练"), ("多模态", "视觉/生成"), ("硬件", "算力边界")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/model-paradigm-timeline.png", "flow", "模型范式时间线", "GPU、CNN、Attention、Transformer、MoE 与 Agent 逐步接力", [("GPU", "Brook/CUDA"), ("CNN", "AlexNet/ResNet"), ("Attention", "seq2seq"), ("Transformer", "通用架构"), ("Agent", "CoT/ReAct")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/hardware-lottery.png", "split", "硬件彩票", "能抱住主流硬件的架构会获得长期复利", (("抽中硬件", "卷积、矩阵乘、Transformer 都能吃到 GPU/TPU 的规模红利。"), ("没抽中硬件", "思想可能正确，但并行性、内存访问或生态不适配。"))),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/transformer-origin-ladder.png", "flow", "从序列建模到 Transformer", "seq2seq、Attention、残差与并行计算共同铺路", [("RNN/seq2seq", "压缩上下文"), ("Attention", "直接对齐"), ("Residual", "更深网络"), ("Self-Attention", "并行建模"), ("Transformer", "时代入口")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/adaptation-agent-stack.png", "flow", "从能力到行动的栈", "蒸馏、LoRA、CoT 和 ReAct 把模型推向可用系统", [("Distillation", "能力迁移"), ("LoRA", "低成本适配"), ("CoT", "显式推理"), ("ReAct", "推理+行动"), ("Agent", "工具闭环")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/infra-data-stack.png", "stack", "Infra 与数据栈", "ZeRO、Scaling Law、开源数据和万卡集群共同放大模型", [("ZeRO", "状态分片"), ("Scaling Law", "规模规律"), ("Chinchilla", "数据/参数配比"), ("LAION/RefinedWeb", "开源数据"), ("MegaScale", "万卡训练")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/language-model-lineage.png", "flow", "语言模型谱系", "从词向量到预训练，再到指令对齐与开源后训练", [("Word2Vec", "词向量"), ("NMT", "线上神经翻译"), ("GPT/BERT", "预训练范式"), ("GPT-3", "规模涌现"), ("Instruct/Tulu", "后训练")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/multimodal-lineage.png", "flow", "多模态模型谱系", "视频、GAN、Diffusion、ViT、CLIP、Stable Diffusion 与 DiT 汇合", [("Video", "DeepVideo/双流"), ("GAN", "生成序章"), ("Diffusion", "重回中央"), ("ViT/CLIP", "视觉语言"), ("DiT", "融合未来")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/bitter-lesson-map.png", "split", "Bitter Lesson", "长期看，通用计算与规模化学习会反复压过手工结构", (("手工特征", "短期有效，依赖人类设计和领域知识。"), ("规模化学习", "算力增长后，用通用方法从数据中学习规律。"))),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/open-source-learning-map.png", "grid", "开源学习地图", "论文、代码、数据、模型、PPT 和社区形成学习基础设施", [("论文", "问题原型"), ("代码", "可复现"), ("数据", "训练来源"), ("模型", "能力载体"), ("PPT/路书", "学习路径"), ("社区", "反馈扩散")]),
    ("youtube/zhangxiaojun/ep117-zrvnoYYPaWQ/figures/two-reader-advice.png", "split", "两类读者建议", "门外张望者先建立地图，体系内工作者要追问边界", (("门外张望者", "用 AI 翻译、先读综述和路书，抓住三到五年不变的知识。"), ("体系内工作者", "回到论文和问题源头，理解边界、硬件和数据约束。"))),
    # EP118
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/ceo-moe-interview-map.png", "radial", "CEO 大模型访谈地图", "把李想当作 MoE 架构：技术、战略、组织与人共同被调用", "CEO\\nMoE", [("Context", "长文本提问"), ("技术专家", "VLA/世界模型"), ("战略专家", "产品与产业"), ("组织专家", "团队和方法论"), ("人", "能量/关系"), ("智慧", "万物关系")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/human-ai-context-window.png", "split", "人类上下文 vs AI 上下文", "人更适合做减法，AI 更适合处理大规模信息", (("人类 CEO", "生理注意力有限，需要抽象、减法和关键判断。"), ("AI/大模型", "可吞吐大量 token，但必须接入行动和反馈才产生价值。"))),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/deepseek-best-practice.png", "flow", "从 DeepSeek 学到的最佳实践", "极简地使用人类最佳实践，再把组织和工程压实", [("MoE", "专家分工"), ("极简", "少而强"), ("开源", "生态扩散"), ("团队", "高密度人才"), ("实践", "快速验证")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/vla-driver-os-stack.png", "stack", "VLA 司机操作系统", "Vision、Language、Action 组合成物理世界的驾驶大模型", [("Vision", "看见道路和环境"), ("Language", "理解规则和意图"), ("Action", "控制车辆动作"), ("World Model", "预测交通演化"), ("Driver OS", "服务车与机器人")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/action-agent-alignment.png", "flow", "从回答到行动", "AI 进入资产、工具和车辆时，对齐要求会变高", [("回答", "信息检索"), ("研究", "寻找源头"), ("计划", "拆任务"), ("行动", "调用工具/资产"), ("责任", "对齐与权限")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/world-model-loop.png", "flow", "交通世界模型闭环", "真实驾驶数据、仿真生成和 VLA 训练互相推动", [("真实车队", "道路数据"), ("世界模型", "生成交通场景"), ("训练", "VLA/端到端"), ("评测", "安全与体验"), ("部署", "回到车辆")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/agi-era-apple-route.png", "flow", "AGI 时代的苹果路线", "车、机器人、操作系统和模型能力共同构成入口", [("车", "物理入口"), ("VLA", "司机模型"), ("机器人", "家庭/工厂"), ("操作系统", "生态接口"), ("AGI Apple", "下一代平台")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/org-as-moe.png", "radial", "组织也像 MoE", "CEO 调度专家、方法论、年轻人才和反馈回路", "Org\\nMoE", [("技术", "模型/硬件"), ("产品", "体验定义"), ("战略", "长期取舍"), ("校招", "高密度成长"), ("方法论", "统一语言"), ("反馈", "真实结果")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/energy-relationship-loop.png", "flow", "能量与亲密关系", "关系不是消耗项，而是让人变得更好的反馈系统", [("需求", "大胆表达"), ("连接", "亲密关系"), ("反馈", "互相照见"), ("能量", "持续存在"), ("成长", "变得更好")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/wisdom-relation-map.png", "radial", "智慧是关系", "智慧来自与人、物、组织、技术和世界持续接触", "Wisdom", [("人", "亲密与协作"), ("物", "产品与车辆"), ("组织", "共同大脑"), ("技术", "AI 和模型"), ("世界", "真实反馈")]),
    ("youtube/zhangxiaojun/ep118-RxXVq7-sJzM/figures/shell-vs-model-ability.png", "split", "套壳与模型能力", "应用创新要走向 action，最终仍要补基础能力", (("套壳/工具", "可快速验证入口、流程和用户需求。"), ("基础能力", "模型、记忆、工具调用和行动可靠性必须真正训练。"))),
    # EP119
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/attention-problem-map.png", "flow", "Attention 问题地图", "长上下文推理把 KV cache、decoding 和全局注意力推到瓶颈", [("长 CoT", "几万 token"), ("Full Attention", "O(L^2)"), ("KV Cache", "显存压力"), ("Decoding", "逐 token 成本"), ("新 Attention", "降成本")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/linear-attention-intuition.png", "split", "Linear Attention 直觉", "平方矩阵改写成线性 recurrence", (("Softmax Attention", "QK 得到 LxL 注意力矩阵，复杂度随序列平方增长。"), ("Linear Attention", "去掉/改写 Softmax，用 recurrence 让总复杂度近似线性。"))),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/kimi-linear-kda.png", "flow", "Kimi Linear / KDA", "Kimi Delta Attention 用更细粒度 decay 改善记忆利用", [("Gated DeltaNet", "基础模块"), ("粗粒度 decay", "head 共享"), ("细粒度 decay", "维度独立"), ("KDA", "记忆更新"), ("Hybrid", "3:1 全局层")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/scaling-ladder.png", "flow", "Scaling Ladder", "小规模通关后再上更大规模，与 Full Attention 对比", [("小规模", "快速筛选"), ("指标达标", "过关"), ("更大规模", "继续 scale"), ("Full Attention", "基线对比"), ("上线候选", "成本/性能")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/linear-vs-sparse-vs-full.png", "grid", "三条 Attention 路线", "Kimi、DeepSeek、MiniMax 的不同押注", [("Linear/Hybrid", "省 KV cache"), ("Sparse", "少算 Top-K"), ("Full", "表达力强"), ("Kimi", "混合线性"), ("DeepSeek", "动态稀疏"), ("MiniMax M2", "回到 Full")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/moe-to-attention.png", "flow", "从 MoE 到 Attention", "FFN 已经被雕成 MoE，Attention 成为下一块可雕区域", [("Transformer", "Attention+FFN"), ("FFN", "变成 MoE"), ("Attention", "仍是瓶颈"), ("Linear/Sparse", "架构创新"), ("长上下文", "目标场景")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/algorithm-archaeology.png", "flow", "算法考古路线", "旧论文、旧机制和新硬件重新组合", [("Transformer", "2017"), ("Sparse", "早期变种"), ("DeltaNet", "2021"), ("Gated Linear", "改进"), ("KDA", "重组发光")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/hardware-friendly-algorithm.png", "flow", "硬件亲和算法", "数学 make sense，还要能并行、能矩阵乘、能 scale", [("数学合理", "principled"), ("并行算法", "chunkwise"), ("矩阵乘", "硬件友好"), ("Kernel", "Triton/优化"), ("Scale", "大模型可用")]),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/deepseek-hardware-codesign.png", "split", "DeepSeek 的硬件协同", "稀疏选择、FP8 和矩阵乘共同服务效率", (("算法侧", "Sparse Attention / Indexer / Top-K 选择，减少 token 计算。"), ("硬件侧", "FP8、矩阵乘、去掉昂贵 softmax/exp，贴近硬件原则。"))),
    ("youtube/zhangxiaojun/ep119-858HR43pegk/figures/young-researcher-advice.png", "flow", "进入架构研究的路径", "考古、算力、frontier lab 和硬件意识缺一不可", [("读旧论文", "建立地图"), ("找问题", "有用方向"), ("算力", "验证 scale"), ("实习", "接近 frontier"), ("开源", "让技术流传")]),
    # EP120
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/liuxianming-trajectory.png", "flow", "刘先明的 Physical AI 路径", "从 CV、卫星图像、Robotaxi 到小鹏自动驾驶", [("CV/ML", "学术训练"), ("Facebook", "卫星图像"), ("Cruise", "Robotaxi"), ("小鹏", "车端数据"), ("Physical AI", "量产闭环")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/autonomous-stack-evolution.png", "flow", "自动驾驶软件栈演化", "从规则、半模型、端到端，到更大模型和云端工厂", [("Software 1.0", "规则/优化"), ("Software 1.5", "模型+规则"), ("Software 2.0", "端到端"), ("Software 3.0", "VLA/VLM"), ("云端工厂", "训练/蒸馏/部署")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/remove-language-bottleneck.png", "split", "拆掉 Language Bottleneck", "中间语言 token 会限制数据 scaling", (("保留 Language", "传感器信号翻译成语言，再解码轨迹；引入人工监督瓶颈。"), ("拆掉 L", "Vision+Language 直接输入，Action 直接输出，减少中间压缩。"))),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/cloud-model-factory.png", "flow", "云端模型工厂", "大模型在云端训练，再蒸馏量化剪枝到车端", [("云端大模型", "大参数/大数据"), ("训练", "Scaling"), ("蒸馏", "能力压缩"), ("量化剪枝", "适配车端"), ("部署", "多硬件模型")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/data-infra-loop-xpeng.png", "flow", "数据与 Infra 闭环", "主机厂优势在可控数据链路和量产反馈", [("车队", "真实行驶"), ("数据回流", "corner case"), ("Infra", "训练/分析"), ("模型更新", "端到端/VLA"), ("上线", "量产验证")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/physical-ai-strategy.png", "radial", "小鹏 Physical AI 转型", "从自动驾驶能力走向物理世界智能", "Physical\\nAI", [("车", "最大本体"), ("数据", "可控链路"), ("模型", "VLA/VLM"), ("Robotaxi", "广州目标"), ("组织", "扁平快速")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/simple-is-beautiful.png", "flow", "简单即美", "不断拆掉浓郁中间层，让数据直接训练能力", [("激光雷达依赖", "拆"), ("规控规则", "拆"), ("端到端中间层", "拆"), ("Language 瓶颈", "拆"), ("更简单系统", "保留必要")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/org-flat-engineering.png", "flow", "扁平工程组织", "前沿 AI 与量产结合，需要一线问题快速决策", [("一线工程师", "代码/实验"), ("负责人", "直接看问题"), ("Deep Dive", "复盘实验"), ("资源整合", "减少重复"), ("快速切换", "模型超越规则")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/leader-mission-stages.png", "flow", "小鹏智驾负责人使命", "不同阶段对应不同技术路线和组织任务", [("谷俊丽", "早期探索"), ("吴新宙", "规则/量产"), ("李力耘", "端到端转型"), ("刘先明", "Physical AI"), ("下一阶段", "生活一部分")]),
    ("youtube/zhangxiaojun/ep120-40qPt8R2uys/figures/ai-transition-risk-balance.png", "split", "切换时机：机会 vs 风险", "车企不能只因技术酷就上线，必须等模型超过规则", (("机会", "模型性能涌现，规则上限显现，体验明显提升。"), ("风险", "安全责任、量产质量、成本和用户信任。"))),
    # EP121
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/graphics-to-robotics.png", "flow", "从图形学到机器人", "在仿真里做机器人，再迁移到真实世界", [("图形学", "仿真角色"), ("物理动画", "运动控制"), ("RL", "学习步态"), ("Sim2Real", "迁移真实"), ("机器人", "真实执行")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/brain-cerebellum-robot.png", "split", "大脑与小脑", "多模态模型负责认知，强化学习负责执行", (("大脑", "语言理解、常识、计划和任务拆解。"), ("小脑", "步态、平衡、抓取和底层控制。"))),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/vla-action-gap.png", "flow", "VLA 补上 Action 输出", "多模态模型要控制机器人，必须学会输出动作", [("Vision", "看见环境"), ("Language", "理解指令"), ("VLM", "文本/计划"), ("Action Data", "机器人轨迹"), ("VLA", "输出动作")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/robotics-data-bottleneck.png", "grid", "机器人数据瓶颈", "非结构环境、长尾失败和动作反馈让数据特别贵", [("真实环境", "不可控"), ("动作轨迹", "采集昂贵"), ("长尾失败", "难覆盖"), ("跨本体", "硬件差异"), ("精细操作", "成功率低"), ("高质量数据", "核心瓶颈")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/gemini-robotics-15-loop.png", "flow", "Gemini Robotics 1.5 闭环", "从视觉语言到动作，再用 motion transfer 泛化到新本体", [("指令", "自然语言"), ("感知", "图像/状态"), ("计划", "Gemini"), ("Motion Transfer", "跨本体迁移"), ("执行", "机器人动作")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/synthetic-data-loop.png", "flow", "Synthetic Data 闭环", "真实数据不足时，用仿真生成大量可控训练样本", [("真实任务", "定义目标"), ("仿真环境", "生成场景"), ("合成轨迹", "大量样本"), ("训练", "模型更新"), ("真实评测", "回流差距")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/world-model-vlv.png", "flow", "世界模型 V-L-V", "Vision + Language 输入，预测下一帧视觉状态", [("Vision", "当前画面"), ("Language", "目标/动作"), ("World Model", "预测后果"), ("Vision", "下一帧"), ("Policy", "选择动作")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/tactile-dexterous-hand.png", "split", "触觉与灵巧手", "硬件越灵巧，触觉越重要", (("普通夹爪", "视觉和粗动作已经能完成不少任务。"), ("灵巧手", "接触力、滑动、材质和抓取稳定性都需要触觉。"))),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/robot-generalist-stages.png", "flow", "通用机器人阶段", "从固定自动化到超人能力的长期路线", [("Automation", "固定规则"), ("Teleoperation", "遥操作"), ("Narrow Generalist", "窄域泛化"), ("Home Generalist", "家庭通用"), ("Superhuman", "超人能力")]),
    ("youtube/zhangxiaojun/ep121-2o281Zy5aZE/figures/china-us-robotics-split.png", "split", "中美机器人分工", "美国更强智能范式，中国更强硬件与供应链", (("美国/硅谷", "长期投入、模型大脑、研究信仰和算力。"), ("中国", "硬件、本体、供应链、制造和快速迭代。"))),
    # EP123
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/product-manager-trajectory.png", "flow", "王冠的 AI 产品路径", "从结构化数据到非结构化生成，再到模型产品", [("大数据", "用户画像"), ("CV/深度学习", "算法平台"), ("预训练", "模型商业化"), ("Moonshot", "模型即产品"), ("ONE2X", "生成系统")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/compression-intelligence.png", "flow", "压缩即智能", "压缩把离散任务连接成可泛化能力", [("数据", "离散样本"), ("压缩", "形成连续"), ("语言", "表达世界"), ("泛化", "未见任务"), ("智能", "对外表现")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/data-three-stages.png", "flow", "数据三阶段", "公域数据、领域数据、产品内生数据对应不同玩家", [("公域数据", "基座模型"), ("领域数据", "大厂/行业"), ("产品内生数据", "应用创业"), ("飞轮", "使用中生成"), ("边界", "决定智能")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/video-generation-bet.png", "grid", "为什么选择视频生成", "高价值模态、未成熟窗口和可变现产品同时出现", [("高价值", "视频比图文更重"), ("未成熟", "窗口更早"), ("产品空间", "处理不只是生成"), ("收入验证", "创作者愿付费"), ("供给变化", "内容生产扩张"), ("平台重排", "分发权变化")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/generation-system-stack.png", "stack", "生成系统栈", "DSL、Context、Agent/Workflow 和 System1 协同", [("System1", "模型底座"), ("DSL", "表达问题"), ("Context", "有效 token"), ("Agent/Workflow", "生产流程"), ("评测", "智慧程度")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/app-model-boundary.png", "split", "应用公司与模型公司边界", "边界会变模糊，但数据飞轮不同", (("模型公司", "拥有基座模型、算力、通用能力和 API 分发。"), ("应用公司", "拥有场景、产品内生数据、工作流和用户价值。"))),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/power-shift-to-consumer.png", "flow", "权力向消费者端渗透", "信息商品链条从平台分配走向用户意图驱动", [("生产者", "生产内容"), ("平台", "分发匹配"), ("消费者", "被动消费"), ("生成系统", "按意图生产"), ("权力迁移", "用户定义需求")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/recommendation-vs-generation.png", "split", "推荐系统 vs 生成系统", "库存分配与按需生产的根本差异", (("推荐系统", "从已有库存中匹配内容，平台掌握分配权。"), ("生成系统", "按用户需求即时生产，分配内化到生产。"))),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/ai-product-north-star.png", "flow", "AI 产品北极星", "商业价值之上，用系统智慧程度衡量产品", [("商业价值", "能赚钱"), ("能力设计", "用户可感知"), ("Context", "释放模型"), ("自动生产", "系统会做事"), ("智慧程度", "北极星")]),
    ("youtube/zhangxiaojun/ep123-qZbzFZ2R_Nw/figures/distribution-to-production.png", "flow", "从分销平台到产销平台", "单点内容、Recipe、IP 与信任货币", [("分销平台", "注意力货币"), ("单点内容", "进入流量池"), ("Recipe", "生产方法"), ("连续 IP", "稳定供给"), ("信任", "新货币")]),
    # EP125
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/us-tech-three-lines.png", "flow", "美股科技三条主线", "AI、再工业化和金融数字化彼此咬合", [("AI", "芯片/云/模型"), ("再工业化", "能源/数据中心"), ("金融数字化", "稳定币/支付"), ("政策", "关税和选举"), ("资本", "重仓主线")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/openai-negative-flywheel.png", "flow", "OpenAI 负向滚雪球", "收入追赶上一代训练，下一代训练继续放大支出", [("上一代训练", "成本=1"), ("次年收入", "回收=2"), ("新训练", "成本=10"), ("现金流", "2-10=-8"), ("拐点", "训练增速放缓")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/openai-four-pillars.png", "grid", "OpenAI 四个收入支柱", "ChatGPT、API、Agent 与新产品共同构成收入栈", [("ChatGPT", "个人+企业订阅"), ("API", "开发者和企业调用"), ("Agent", "任务执行与合作"), ("广告", "免费用户变现"), ("企业入口", "办公系统协同"), ("新产品", "搜索/电商/硬件")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/openai-vs-anthropic.png", "split", "OpenAI vs Anthropic", "2C 产品公司与 2B/Coding 公司", (("OpenAI", "ChatGPT 心智强，个人和企业并行，入口想象更大。"), ("Anthropic", "2B 占比高，Coding/Finance/Agent 模型更清晰。"))),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/robinhood-alpha-loop.png", "flow", "Robinhood Alpha 路径", "从一手烂牌到一站式金融应用", [("周期业务", "交易额波动"), ("多元化", "11条收入线"), ("份额", "年轻用户账户"), ("定价权", "加密和新业务"), ("成本控制", "经营杠杆")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/founder-archetypes.png", "grid", "硅谷创始人画像", "乖小孩、坏小孩、刺猬和哪吒代表不同 taste", [("乖小孩", "合规稳健"), ("坏小孩", "打破常规"), ("刺猬型", "单点极深"), ("反叛者", "挑战旧秩序"), ("哪吒型", "不按牌理"), ("Founder-led", "一号位驱动")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/ai-sector-map-2025.png", "grid", "2025 AI 赛道地图", "Coding、视频、Agentic Commerce 与垂直应用", [("Coding", "50亿+ ARR"), ("视频", "可优化对象"), ("Agentic Commerce", "购买入口重写"), ("金融/法律", "垂直场景"), ("医疗/客服", "明确ROI"), ("AI 应用", "估值新口径")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/electronic-revenue-vs-labor.png", "split", "电子收入 vs 劳动力池", "互联网存量不够大，真正大数在劳动和生产力", (("电子收入", "广告、电商佣金、订阅，约4000亿级存量池。"), ("劳动力池", "美国劳动力成本约15万亿，Agent/AI for Science 打开增量。"))),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/ai-bubble-dashboard.png", "flow", "判断 AI Bubble 的仪表盘", "不问情绪，先看模型进步和收入兑现", [("用户", "渗透速度"), ("收入", "OpenAI/Anthropic"), ("ROIC", "大厂回报"), ("模型", "是否继续scale"), ("估值", "是否透支")]),
    ("youtube/zhangxiaojun/ep125-k82iFzvKFCQ/figures/ai-market-2026-watchlist.png", "grid", "2026 市场观察清单", "从投入叙事转向收入和应用兑现", [("Google", "广告竞争"), ("Meta", "模型进展"), ("Tesla", "FSD/Robotaxi"), ("Cloud", "利润率竞争"), ("Nvidia/ASIC", "芯片交付"), ("传统行业", "AI提效数据")]),
    # EP127
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/ai-war-alliances.png", "grid", "AI War 的两条主线", "硬件生态、模型公司和反制联盟同时形成", [("Nvidia GPU", "开放生态与供给瓶颈"), ("Google TPU", "模型-芯片-云-产品闭环"), ("OpenAI", "C端产品与下一范式"), ("Anthropic", "Coding 与企业场景"), ("反Google联盟", "避免单一平台独大"), ("反OpenAI联盟", "平衡入口和模型权力")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/openai-revenue-stack.png", "stack", "OpenAI 收入栈", "从看得见的收入，走向替代劳动和高价值增量", [("订阅", "用户付费与企业席位"), ("广告电商", "大流量平台变现"), ("API", "模型云与开发者生态"), ("Agent 劳动", "吃工资预算"), ("AI 科学家", "做人做不了的事")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/top-model-rotation.png", "flow", "三大模型交替领先", "GPT、Claude、Gemini 在同一范式内你追我赶", [("GPT", "C端与品牌"), ("Claude", "Coding与企业"), ("Gemini", "多模态和生态"), ("交替领先", "Benchmark不等于终局"), ("新范式", "拉开差距的变量")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/foundation-model-as-ecommerce.png", "split", "基础模型 = 综合电商", "Scale SKU 类比 Scale Data", (("综合电商", "从图书扩到全品类，仓配、支付、流量和供应链复用。"), ("基础模型", "从聊天、Coding、Office 到垂直行业，数据管线可复用。"))),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/search-agent-disruption.png", "flow", "Search 与 Agent 的流量重分配", "Agent 成为入口后，传统平台的抽成逻辑被重新定价", [("用户目标", "我要完成任务"), ("Agent入口", "理解和拆解"), ("工具执行", "搜索/订票/支付"), ("平台绕行", "中介价值下降"), ("新分配权", "谁控制入口")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/scaling-paradigm-shift.png", "flow", "三种学习范式", "预训练、强化学习和 Online Learning 的接力", [("Pre-training", "大规模压缩"), ("RL/Post-train", "专家反馈塑形"), ("Memory", "长期上下文"), ("Online Learning", "边交互边学习"), ("主动Agent", "越用越懂你")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/energy-metaphor.png", "grid", "能源隐喻", "石油、新能源和核聚变对应三类数据与学习方式", [("石油", "预训练数据量大但有限"), ("新能源", "专家数据有用但总量少"), ("核聚变", "Online Learning 尚未突破"), ("算力供给", "研究员获得更多实验机会"), ("基础设施", "长上下文、Memory、LoRA"), ("硅基时代", "突破后的想象空间")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/model-data-product-loop.png", "flow", "模型即产品，数据即模型", "产品体验最终回到数据分布和反馈闭环", [("用户任务", "真实工作流"), ("交互数据", "偏好和失败点"), ("专家蒸馏", "金牌级过程"), ("模型升级", "能力边界外扩"), ("产品体验", "更可靠更主动")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/neo-labs-map.png", "radial", "Neo Labs 分布", "下一范式、材料、多Agent、世界模型和开源都在冒头", "新实验室", [("SSI", "自主学习"), ("Thinking Machines", "Post-train与下一范式"), ("Periodic", "材料模型"), ("Aethera", "Multi-agent环境"), ("General Intuition", "世界模型数据"), ("Reflection", "美国开源模型")]),
    ("youtube/zhangxiaojun/ep127-SG90aehV3vU/figures/china-founder-operating-model.png", "flow", "华人 AI 创业模型", "全球市场、人才工程红利和产品说话", [("全球市场", "高付费地区"), ("中国人才", "工程师红利"), ("风险资本", "支持0到1"), ("产品说话", "淡化身份标签"), ("长期目标", "十个字节")]),
    # EP128
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/manus-journey.png", "flow", "Manus 奇幻漂流路线", "从个人开发者、NLP、Agent，到最后一次访谈", [("App Store", "出海+变现"), ("NLP", "需求牵引学习"), ("Open IE", "结构化知识"), ("Manus", "Agent 产品化"), ("Meta 收购", "阶段终点")]),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/appstore-to-ai-platform.png", "split", "App Store 蛮荒期 vs AI 时代", "新平台出现时，个人开发者和巨头的起跑线不同", (("App Store 蛮荒期", "硬件媒介变化带来分发红利，个人开发者也能全球变现。"), ("AI 时代", "技术突破很大，但没有同等新平台，巨头和创业公司反应都很快。"))),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/nlp-lineage.png", "flow", "从浏览器预加载到 NLP", "具体需求牵引学习路径，而不是先选宏大赛道", [("浏览器", "弱网和下一页"), ("预测点击", "preloading"), ("NLP", "语义理解"), ("Word2Vec", "稠密向量"), ("知识图谱", "结构化答案")]),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/manus-arr-flywheel.png", "flow", "Manus 从 0 到 1 亿 ARR", "产品、用户、收入和反馈形成增长飞轮", [("产品", "Agent 可用性"), ("用户", "真实工作流"), ("收入", "ARR 增长"), ("反馈", "错误和需求"), ("迭代", "能力升级")]),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/ai-like-manufacturing.png", "flow", "AI 更像制造业", "不是只做模型，而是把质量、成本、供应链和交付压实", [("模型", "能力底座"), ("算力", "成本和产能"), ("数据", "原料和工艺"), ("交付", "客户现场"), ("质量", "稳定可复现")]),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/complexity-risk.png", "flow", "复杂性风险", "每增加一个功能，都在稀释其他东西", [("增长", "想做更多"), ("功能", "复杂度上升"), ("稀释", "特色变弱"), ("克制", "保持核心"), ("飞轮", "不牺牲增长")]),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/agent-market-map.png", "grid", "Agent 市场地图", "垂直、Coding、C 端和基础设施同时推进", [("Coding", "Replit / Lovable / Claude Code"), ("垂直 Agent", "Sierra / 行业任务"), ("C 端 Agent", "提效与个人工作流"), ("支付/权限", "Stripe / Cloudflare 等生态"), ("模型公司", "OpenAI / Anthropic / Google")]),
    ("youtube/zhangxiaojun/ep128-MW-ezf2RhVg/figures/stay-simple-principle.png", "flow", "保持简单的产品原则", "Manus 最怕失去特色，内部最怕变得复杂", [("核心价值", "主力生产力工具"), ("克制", "少加无关功能"), ("特色", "用户记得住"), ("增长", "进入更多人群"), ("长期", "复杂中保持简单")]),
    # EP129
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/zhipu-ai-roadmap.png", "flow", "智谱六年路线", "从认知智能到上市节点，再回到 AGI 目标", [("认知智能", "感知智能下一步"), ("P2P 转化", "paper 到 product"), ("GPT 冲击", "范式重估"), ("DeepSeek", "开源和效率冲击"), ("IPO", "公司治理新阶段")]),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/paper-to-product-loop.png", "flow", "P2P：Paper to Product", "研究、工程、客户和商业反馈共同演进", [("Paper", "研究成果"), ("Prototype", "原型代码"), ("System", "生产系统"), ("Product", "客户可用"), ("Feedback", "反哺研究")]),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/cognitive-intelligence-ladder.png", "flow", "从感知智能到认知智能", "认知智能被视为迈向 AGI 的下一层台阶", [("感知智能", "CV/NLP 早期突破"), ("认知智能", "理解和推理"), ("大模型", "通用能力底座"), ("Agent", "连接应用场景"), ("AGI", "长期目标")]),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/model-shockwaves.png", "flow", "三次模型冲击", "GPT-3、ChatGPT、DeepSeek 改变团队判断和行业节奏", [("GPT-3", "规模范式出现"), ("ChatGPT", "用户心智爆发"), ("2024", "多主角分化"), ("DeepSeek", "开源效率冲击"), ("2025+", "Agent 与 RL")]),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/scaling-law-evolution.png", "flow", "Scaling Law 范式演变", "从预训练规模律走向多数据、RL 和 Agent 闭环", [("规模", "参数/数据/算力"), ("多模态", "数据融合"), ("Post-train", "偏好和任务反馈"), ("RL", "新计算方式"), ("Agent", "落地路径")]),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/open-vs-closed.png", "split", "开源 vs 闭源", "模型公司要在生态影响和商业控制之间取舍", (("开源", "扩大生态、建立信任、获得开发者反馈。"), ("闭源", "保留商业控制、服务企业客户和安全边界。"))),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/company-stage-thresholds.png", "flow", "创业公司阶段门槛", "50人、200人、500人和上市对应不同管理问题", [("50人", "先活下来"), ("200人", "分工与协调"), ("500人", "层级与制度"), ("上市", "合规与治理")]),
    ("youtube/zhangxiaojun/ep129-9zSMTUUEfmU/figures/idealism-commercialization.png", "flow", "理想主义与商业化", "智谱的平衡：追求 AGI，也要客户价值和收入", [("技术理想", "让机器像人思考"), ("工程文化", "模型能力持续上拱"), ("商业化", "客户现场创造价值"), ("治理", "上市公司纪律"), ("先行者", "AGI 开路")]),
    # EP130
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/flow-to-context-design.png", "flow", "从流程设计到上下文设计", "AI Native 的核心变化：从穷举路径到组织上下文", [("流程", "按钮、路径、输入输出"), ("上下文", "材料、工具、约束"), ("模型", "开放生成与执行"), ("反馈", "用户修正再进入循环")]),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/miaoya-not-ai-native.png", "flow", "妙鸭为什么不是 AI Native", "它是 AI 能力很强的互联网产品", [("输入固定", "约20张照片"), ("链路固定", "模板与工艺链"), ("输出固定", "写真结果"), ("优势", "真、像、美")]),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/one-way-door-product.png", "flow", "One Way Door 产品", "用户用了新解法，就不愿回到旧方法", [("旧解法", "慢、贵、能力窄"), ("新解法", "全方位更优"), ("心智迁移", "默认行为改变"), ("长期复利", "份额随时间上涨")]),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/ai-product-org-two-stage.png", "flow", "AI 产品组织的两段式", "先验证模型能力，再封装产品体验", [("探索", "context 与 prompt"), ("验证", "输出质量与评测"), ("封装", "流程、UI、商业模式"), ("上线", "用户心智与反馈")]),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/ai-population-will-skill.png", "flow", "AI 人口：Will 与 Skill", "人负责目标，AI 负责执行", [("Will", "目标、选择、品味"), ("Skill", "生成、执行、工具"), ("AI 个体", "可协作对象"), ("人类网络", "进入工作和关系")]),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/xingmian-dokie-two-bets.png", "split", "星眠与 Dokie 两条线", "一个验证陪伴内容，一个押注能力边界", (("星眠", "AI 乙女游戏，验证角色、陪伴、内容频次和女性向交互。"), ("Dokie", "创作表达 Agent，从 PPT 切入，目标是突破用户能力边界。"))),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/agent-short-loop.png", "flow", "Agent 短程高频反馈", "先做可控闭环，再挑战长程任务", [("意图", "自然语言目标"), ("LM 内核", "拆解并调用工具"), ("产物", "PPT/文档/内容"), ("反馈", "低延迟修正")]),
    ("youtube/zhangxiaojun/ep130-ruVJ_5dObxs/figures/platform-tool-agent-positioning.png", "flow", "工具、平台与 Agent 入口", "边界不是越宽越好，而是要有用户心智", [("工具", "解决单任务"), ("平台", "关系和生态"), ("Agent", "会做事的入口"), ("心智", "高频且清晰")]),
    # EP132
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/trajectory-industrial-training.png", "flow", "高继扬的产业训练路径", "从算法直觉到工程系统，再到客户交付", [("归纳", "竞赛和论文方法"), ("AI 入门", "从数据学规律"), ("Waymo", "系统工程"), ("Momenta", "量产交付"), ("星海图", "整机+模型+数据")]),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/waymo-momenta-contrast.png", "split", "Waymo 与 Momenta", "工程天堂与量产战场的互补训练", (("Waymo", "完整系统、好 infra、长期执行；但离客户和经营较远。"), ("Momenta", "量产、客户、结果导向；组织压力更大，也更接近商业闭环。"))),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/autonomous-driving-business-models.png", "grid", "自动驾驶商业模式", "谁拥有车、客户、数据和利润池", [("Robotaxi", "自营车队服务"), ("车企订阅", "卖车+软件"), ("供应商", "NRE+license"), ("整车平台", "品牌+渠道+智驾")]),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/embodied-ai-value-chain.png", "flow", "具身智能价值链", "短期算法可复制，长周期资产形成壁垒", [("整机", "12-18个月"), ("客户", "渠道与信任"), ("数据", "6-12个月"), ("Infra", "训练与部署"), ("算法", "传播最快")]),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/robot-data-recipe-flywheel.png", "radial", "机器人 Data Recipe", "数据不是库存，而是产品闭环", "Recipe", [("整机", "真实入口"), ("采集", "轨迹和失败"), ("训练", "VLA/模型"), ("价值", "客户付费"), ("回流", "错误修正"), ("共享", "生态验证")]),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/robot-brain-dual-system.png", "flow", "机器人大脑双系统", "VLM 拆解任务，VLA 产生动作", [("指令", "模糊目标"), ("VLM", "拆解与规划"), ("VLA", "vision+language->action"), ("本体", "执行并反馈")]),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/go-to-soil-robotics.png", "split", "到土里去", "机器人创业必须进入真实摩擦", (("软件/模型", "可专注模型、增长和体验，迭代更轻。"), ("机器人", "整机、供应链、现场、维护、数据和责任同时存在。"))),
    ("youtube/zhangxiaojun/ep132-n4_c_HsodPg/figures/three-product-combo.png", "flow", "星海图三件套", "像培训员工一样培训机器人", [("整机", "硬件和数据入口"), ("基础模型", "VLA/VLM 底座"), ("后训练工具", "示范与自我演练"), ("生产力场景", "稳定交付")]),
    # EP133
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/world-model-stack.png", "flow", "世界模型最小闭环", "预测要进入行动，而不是停在生成", [("感知", "多模态输入"), ("状态", "任务相关表征"), ("预测", "s,a -> next state"), ("规划", "选择动作"), ("反馈", "误差回流")]),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/llm-vs-world-model.png", "split", "LLM 与世界模型", "数字空间和物理世界的能力边界", (("LLM", "擅长 token、文本、代码、知识和数字任务。"), ("World Model", "面向连续信号、物理预测、规划和安全控制。"))),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/representation-ladder.png", "flow", "从视觉任务到世界模型", "能力阶梯越高，越依赖抽象表征", [("识别", "分类/检测"), ("看图问答", "语言接口"), ("事件流", "连续视频"), ("空间认知", "对象关系"), ("预测", "action 后果")]),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/research-taste-map.png", "radial", "Research Taste", "问题、审美、证据和时机共同构成判断系统", "Taste", [("问题", "值得长期做"), ("审美", "反口号"), ("证据", "实验和失败"), ("时机", "资源窗口"), ("长期", "时间积分")]),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/ami-labs-thesis.png", "flow", "AMI Labs 组织命题", "在研究自由、资源和真实世界之间找平衡", [("世界模型", "predictive brain"), ("研究氧气", "探索空间"), ("伙伴网络", "world needs world"), ("商业闭环", "价值反哺数据"), ("学术连接", "开放讨论")]),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/download-internet-to-world.png", "split", "下载互联网 vs 下载世界", "从静态语料转向动态环境", (("Internet -> GPT", "下载网页、书籍和代码，训练语言模型。"), ("World -> Model", "伙伴、工厂、医院、机器人和传感器共同产生数据。"))),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/intelligence-spectrum.png", "flow", "智能不是语言分数线", "真实智能要回到感知、行动和反馈", [("文本", "token 推理"), ("视觉", "空间对象"), ("行动", "控制决策"), ("身体", "环境约束"), ("社会", "目标协作")]),
    ("youtube/zhangxiaojun/ep133-iiBY0fqpThI/figures/trajectory-timeline.png", "flow", "谢赛宁研究轨迹", "每次选择都围绕问题、共事者和资源", [("SJTU", "通识和兴趣"), ("UCSD", "Vision"), ("FAIR", "表征学习"), ("NYU", "世界模型"), ("AMI", "组织资源")]),
    # EP134
    ("youtube/zhangxiaojun/ep134-owjTOT14bG0/figures/data-pyramid.png", "stack", "机器人数据金字塔", "越真实越稀缺，越大规模越弱接地", [("真实端侧", "部署和失败反馈"), ("遥操作/仿真", "可控长尾场景"), ("互联网/人类", "大规模常识"), ("Recipe", "配比、评测、回流")]),
    ("youtube/zhangxiaojun/ep134-owjTOT14bG0/figures/data-engine-loop.png", "flow", "Data Engine 闭环", "数据不是一次购买，而是持续运行", [("部署", "进入场景"), ("采集", "成功/失败"), ("挖掘", "长尾 case"), ("训练", "更新能力"), ("评测", "判断进步")]),
    ("youtube/zhangxiaojun/ep134-owjTOT14bG0/figures/data-taxonomy.png", "grid", "数据类型版图", "不同模型需要不同数据", [("文本/代码", "LLM"), ("多模态", "视觉/音频"), ("轨迹", "动作和反馈"), ("仿真", "可控环境"), ("失败对", "恢复能力"), ("人类反馈", "偏好和纠错")]),
    ("youtube/zhangxiaojun/ep134-owjTOT14bG0/figures/data-pricing.png", "radial", "数据定价", "按边际能力提升，而不是按 GB", "Value", [("真实", "贴近部署"), ("稀缺", "长尾失败"), ("可验证", "能判对错"), ("可复用", "跨任务"), ("边际收益", "新增贡献")]),
    ("youtube/zhangxiaojun/ep134-owjTOT14bG0/figures/data-recipe.png", "flow", "Data Recipe", "数据到能力的转换器", [("来源", "多种数据"), ("过滤", "去噪去重"), ("配比", "混合比例"), ("课程", "训练顺序"), ("反馈", "评测回流")]),
    ("youtube/zhangxiaojun/ep134-owjTOT14bG0/figures/data-industry-landscape.png", "radial", "数据产业共生网络", "模型、本体、仿真和客户共同形成闭环", "Data\\nNetwork", [("大模型", "基座能力"), ("世界模型", "物理预测"), ("VLA", "语言到动作"), ("本体", "端侧数据"), ("仿真", "长尾环境"), ("客户", "真实任务")]),
    # EP135
    ("youtube/zhangxiaojun/ep135-x8qdqWIVVTA/figures/context-flow.png", "flow", "Context 流动闭环", "获取、组织、行动和反馈构成 AI 社交资产", [("获取", "聊天/文件/行为"), ("组织", "记忆和画像"), ("行动", "代表用户"), ("反馈", "纠错和更新")]),
    ("youtube/zhangxiaojun/ep135-x8qdqWIVVTA/figures/subjectivity-stack.png", "stack", "主体性上下文栈", "AI 要代表你行动，需要多层边界", [("身份", "我是谁"), ("偏好", "我如何选择"), ("记忆", "我经历过什么"), ("权限", "AI 能做什么"), ("目标", "此刻要什么")]),
    ("youtube/zhangxiaojun/ep135-x8qdqWIVVTA/figures/context-privacy-tradeoff.png", "split", "Context 与隐私交换", "能力越强，边界越要清楚", (("少交 Context", "隐私风险低，但能力通用、主体性弱。"), ("多交 Context", "能力更强，但带来泄露、锁定和误用风险。"))),
    ("youtube/zhangxiaojun/ep135-x8qdqWIVVTA/figures/ai-social-vs-internet-social.png", "split", "互联网社交 vs AI 社交", "关系链之外，AI 社交还要管理上下文资产", (("互联网社交", "关注、内容分发、点赞评论和关系链。"), ("AI 社交", "长期 context、代理行动、分身和协作。"))),
    ("youtube/zhangxiaojun/ep135-x8qdqWIVVTA/figures/context-competition.png", "radial", "AI 社交竞争变量", "模型、关系链、Context 和信任共同构成壁垒", "Competition", [("模型", "理解生成"), ("关系链", "用户图谱"), ("Context", "长期记忆"), ("主体性", "代表行动"), ("隐私", "信任边界")]),
    ("youtube/zhangxiaojun/ep135-x8qdqWIVVTA/figures/proactive-product-shift.png", "flow", "从 Reactive 到 Proactive", "AI 产品从被动响应走向主动行动", [("Reactive", "用户问"), ("Assistive", "AI 帮做"), ("Proactive", "主动建议"), ("Guardrails", "权限审计")]),
    # EP136
    ("youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/figures/coding-second-act.png", "flow", "Coding 是 AGI 第二幕", "从聊天到干活，再到模型 OS", [("Chat", "回答问题"), ("Coding", "读写代码"), ("Agent", "跨工具执行"), ("OS", "工作入口")]),
    ("youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/figures/frontier-lab-map.png", "grid", "硅谷模型公司位置图", "不同公司在模型、产品、infra 和生态上分化", [("OpenAI", "产品+模型"), ("Anthropic", "安全+企业"), ("Google", "模型+云"), ("Meta", "开源+社交"), ("xAI", "速度+平台")]),
    ("youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/figures/harness-engineering.png", "flow", "Harness Engineering", "模型到真实工作流之间需要脚手架", [("模型", "基础能力"), ("工具", "API/浏览器"), ("记忆", "状态上下文"), ("评测", "任务成功"), ("产品", "稳定流程")]),
    ("youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/figures/model-as-os.png", "radial", "模型作为新一代 OS", "意图理解、工具调度、状态记忆和权限控制", "Model\\nOS", [("意图", "理解目标"), ("调度", "选择工具"), ("状态", "上下文"), ("权限", "安全边界"), ("生态", "插件应用")]),
    ("youtube/zhangxiaojun/ep136-u1Lzp-7Ybn8/figures/social-impact-chain.png", "flow", "Coding 加速器的社会传导", "生产力提升会影响组织和岗位结构", [("效率", "个人产出"), ("组织", "团队重组"), ("成本", "交付下降"), ("岗位", "再分配压力")]),
    # EP137
    ("youtube/zhangxiaojun/ep137-bv8ghyTFF9w/figures/math-created-discovered.png", "split", "数学：被发现还是被创造", "客观结构和人类语言共同塑造数学", (("被发现", "结构和关系似乎独立存在，等待揭示。"), ("被创造", "符号、定义、证明风格由人类共同塑造。"))),
    ("youtube/zhangxiaojun/ep137-bv8ghyTFF9w/figures/bounded-free-attention.png", "split", "两种数学注意力", "严谨边界和自由联想共同产生创造", (("Bounded", "在定义、条件和证明目标内保持严谨。"), ("Free", "跨领域联想，寻找新表征和新问题。"))),
    ("youtube/zhangxiaojun/ep137-bv8ghyTFF9w/figures/ai-for-math-stack.png", "flow", "AI for Math 技术栈", "从问题到验证，再回到数学家反馈", [("问题", "自然语言"), ("形式化", "Lean"), ("搜索", "证明步骤"), ("验证", "机器检查"), ("反馈", "数学价值")]),
    ("youtube/zhangxiaojun/ep137-bv8ghyTFF9w/figures/lean-proof-loop.png", "flow", "Lean 证明闭环", "自然语言证明转为机器可验证对象", [("陈述", "定理条件"), ("翻译", "Lean 代码"), ("证明", "策略/lemma"), ("验证", "编译反馈"), ("修正", "人机循环")]),
    ("youtube/zhangxiaojun/ep137-bv8ghyTFF9w/figures/ai-for-math-roadmap.png", "flow", "AI for Math 路线图", "从做题走向研究协作", [("竞赛题", "短程可验证"), ("形式化库", "可复用知识"), ("研究辅助", "猜想证明反例"), ("协作", "人机共研")]),
    ("youtube/zhangxiaojun/ep137-bv8ghyTFF9w/figures/ai-math-neolab.png", "radial", "AI for Math Neo Lab", "数学家、形式化系统、模型和资源形成闭环", "Math\\nLab", [("数学家", "问题品味"), ("Lean", "验证基础"), ("模型", "证明生成"), ("算力", "训练资源"), ("产品", "研究服务")]),
    # EP138
    ("youtube/zhangxiaojun/ep138-vG1RBqn1sG4/figures/chat-to-agent-paradigm.png", "flow", "从 Chat 到 Agent", "重心从预训练聊天转向后训练和环境反馈", [("Chat", "问答"), ("Tool Use", "调用工具"), ("Agent", "观察计划执行"), ("Post-train", "任务反馈")]),
    ("youtube/zhangxiaojun/ep138-vG1RBqn1sG4/figures/agent-rl-infra-loop.png", "flow", "Agent RL Infra 闭环", "环境、rollout、reward 和训练系统构成新基础设施", [("环境", "网页/代码/工具"), ("Rollout", "多步执行"), ("Reward", "成功/偏好"), ("训练", "RL/SFT"), ("评测", "真实任务")]),
    ("youtube/zhangxiaojun/ep138-vG1RBqn1sG4/figures/mimo-orchestration.png", "radial", "MiMo 多模型编排", "Agent 任务需要多个模型和工具协同", "MiMo", [("Planner", "拆任务"), ("Coder", "写代码"), ("Verifier", "测试"), ("Retriever", "检索"), ("UI Agent", "操作界面")]),
    ("youtube/zhangxiaojun/ep138-vG1RBqn1sG4/figures/compute-allocation.png", "split", "算力分配趋势", "Chat 阶段和 Agent 阶段资源重点不同", (("Chat 阶段", "更多资源投向预训练、通用模型和对话能力。"), ("Agent 阶段", "更多资源投向后训练、环境、rollout 和评测。"))),
    ("youtube/zhangxiaojun/ep138-vG1RBqn1sG4/figures/org-equality.png", "radial", "Agent 研究中的组织平权", "研究、产品、工程、评测和 infra 进入同一闭环", "Org", [("研究", "模型算法"), ("工程", "工具系统"), ("产品", "用户价值"), ("评测", "定义成功"), ("Infra", "训练管线")]),
    ("youtube/zhangxiaojun/ep138-vG1RBqn1sG4/figures/model-evolution-timeline.png", "flow", "模型进化时间线", "从 ChatGPT 到 Agent 后训练", [("2022", "ChatGPT"), ("2023", "Tool Use"), ("2024", "Reasoning"), ("2025", "Agent")]),
    # EP139
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/agent-loop.png", "flow", "Agent 最小循环", "环境、观察、推理、动作和记忆不断迭代", [("环境", "工具/文件"), ("观察", "读取状态"), ("推理", "计划下一步"), ("动作", "修改世界"), ("记忆", "保留经验")]),
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/agent-history-timeline.png", "flow", "Agent 技术谱系", "从符号逻辑到 OpenClaw Moment", [("符号 AI", "规则规划"), ("RL Agent", "环境交互"), ("LLM Agent", "语言工具"), ("OpenClaw", "通用数字行动")]),
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/language-agent-stack.png", "flow", "Language Agent 栈", "从用户目标到工具、环境反馈和记忆", [("目标", "用户意图"), ("LLM", "理解规划"), ("工具", "API/浏览器"), ("反馈", "结果错误"), ("记忆", "长期上下文")]),
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/agent-productization-funnel.png", "flow", "Agent 产品化漏斗", "从 Moment 到生产系统需要层层压实", [("Moment", "惊艳演示"), ("Repeat", "可复现"), ("Reliable", "稳定可靠"), ("Workflow", "嵌入流程"), ("Business", "商业闭环")]),
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/boundary-convergence.png", "radial", "边界的消弭", "多种数字环境入口正在收敛到 universal digital agent", "Boundary", [("浏览器", "网页任务"), ("IDE", "代码任务"), ("Office", "文档表格"), ("OS", "文件应用"), ("Chat", "语言入口")]),
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/continual-learning-map.png", "radial", "Continual Learning 地图", "Agent 从经验中学习，逐步形成可迁移能力", "Learning", [("经验", "任务轨迹"), ("记忆", "长期状态"), ("World Model", "预测环境"), ("Expert Agent", "领域技能"), ("评测", "能力增长")]),
    ("youtube/zhangxiaojun/ep139-Xxz5uh0L1mE/figures/agent-evaluation-matrix.png", "grid", "Agent 评测矩阵", "成功率、效率、鲁棒性、可控性和用户价值共同决定质量", [("成功率", "任务完成"), ("效率", "时间成本"), ("鲁棒性", "异常处理"), ("可控性", "权限安全"), ("用户价值", "真实收益")]),
]


def render(spec: tuple[object, ...]) -> None:
    rel = str(spec[0])
    kind = str(spec[1])
    title = str(spec[2])
    subtitle = str(spec[3])
    if kind == "flow":
        payload = spec[4]
        draw_flow(rel, title, subtitle, payload)  # type: ignore[arg-type]
    elif kind == "split":
        payload = spec[4]
        left, right = payload  # type: ignore[misc]
        draw_split(rel, title, subtitle, left, right)
    elif kind == "grid":
        payload = spec[4]
        draw_grid(rel, title, subtitle, payload)  # type: ignore[arg-type]
    elif kind == "radial":
        center, nodes = str(spec[4]), spec[5]
        draw_radial(rel, title, subtitle, center, nodes)
    elif kind == "stack":
        payload = spec[4]
        draw_stack(rel, title, subtitle, payload)  # type: ignore[arg-type]
    else:
        raise ValueError(f"unknown figure kind: {kind}")


def main() -> None:
    for spec in SPECS:
        render(spec)
    print(f"Rendered {len(SPECS)} Zhang Xiaojun concept figures with {FONT_PATH}")


if __name__ == "__main__":
    main()

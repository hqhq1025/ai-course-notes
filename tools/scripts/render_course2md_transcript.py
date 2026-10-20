#!/usr/bin/env python3
"""Render a course2md timeline using pause-aware, source-faithful transcript text."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path


CORRECTIONS = {
    "NeoWim": "Neovim",
    "Compure Science": "Computer Science",
    "PCGR8800": "Altair 8800",
    "AIware": "AI 味",
    "ChatGPD": "ChatGPT",
    "ChatGPG": "ChatGPT",
    "GPG": "GPT",
    "webcoding": "vibe coding",
    "操系统": "操作系统",
    "保验": "保研",
    "深圳式转件工程": "生成式软件工程",
    "InlaAssembly": "inline assembly",
    "Anthropodic": "Anthropic",
    "幻冻片": "幻灯片",
    "非慢学习法": "费曼学习法",
    "非凡学习法": "费曼学习法",
    "Github": "GitHub",
    "base64": "Base64",
    "agents.md": "AGENTS.md",
    "agency.md": "AGENTS.md",
    "codecode": "Claude Code",
    "open cloud": "OpenClaw",
    "Open cloud": "OpenClaw",
    "openclaw": "OpenClaw",
    "open claw": "OpenClaw",
    "Ermas": "Hermes",
    "ermis": "Hermes",
    "telegram": "Telegram",
    "markdown": "Markdown",
    "python": "Python",
    "deepstick": "DeepSeek",
    "Deepseek": "DeepSeek",
    "turing": "Turing",
    "GPT5.6sol": "GPT-5.6 slow",
    "GPT5.6SOL": "GPT-5.6 slow",
    "GPT5.6Soul": "GPT-5.6 slow",
    "GPT5.6": "GPT-5.6",
    "GP5.6": "GPT-5.6",
    "GP14": "GPT-4",
    "GP4": "GPT-4",
    "大圆模型": "大语言模型",
    "生存式软件工程": "生成式软件工程",
    "生成式载件工程": "生成式软件工程",
    "EGA": "eza",
    "makefire": "Makefile",
    "conversion": "conversation",
    "workbody": "WorkBuddy",
    "AI slug normal": "AI slop novel",
    "把一个很长的上文采短": "把一个很长的上下文改短",
    "教训辅助Agen": "教学辅助 Agent",
    "这门客": "这门课",
    "装机先人": "装机仙人",
    "mirrors.ngu.edu.cnn": "mirrors.nju.edu.cn",
    "得办13": "Debian 13",
    "模拟期": "模拟器",
    "Qemail": "QEMU",
    "自然源": "自然语言",
    "ZHRC": ".zshrc",
    "小红树": "小红书",
    "已图的状态": "已读的状态",
    "日常的事物": "日常的事务",
    "AI梗同学": "AI Council",
    "AI耿同学": "AI Council",
    "Ai肯同学": "AI Council",
    "The Philosopher of Software Design": "A Philosophy of Software Design",
    "Mythical Man-Mouth": "Mythical Man-Month",
    "Mystical Man-Mouth": "Mythical Man-Month",
    "Lessence": "lessons",
    "Compher Science": "Computer Science",
    "神贵": "神棍",
    "上个老，下个小": "上有老，下有小",
    "HTP": "HTTP",
    "Cure": "curl",
    "CodeLink": "Kotlin",
    "Boundbox": "bounding box",
    "暴动隐私": "暴露隐私",
    "教学周围": "教学任务",
    "Links": "Linux",
    "ripple": "repo",
    "lectronose": "lecture notes",
    "AIS-Law": "AI slop",
    "走通过": "走通",
    "Archive": "arXiv",
    "Emily": "Hermes",
    "prong": "prompt",
    "操线用作业": "操作系统作业",
    "歪不扣": "vibe coding",
    "签问": "千问",
    "卷则": "卷子",
    "圈面": "卷面",
    "欧拉玛": "Ollama",
    "千万3.8": "Qwen3.8",
    "考进去": "拷进去",
    "考到外面考出来": "拷到外面、拷出来",
    "敲敲射评": "敲敲键盘",
    "三级打印机": "3D 打印机",
    "QR阵点Excel": "qrgen Excel",
    "QR件": "qrgen",
    "QR键": "qrgen",
    "QRGEN": "qrgen",
    "XL2019": "Excel 2019",
    "解断了": "截断了",
    "智朴": "智谱",
    "chain of software": "chain of thought",
    "维护的Nita": "维护的泥潭",
    "复兴界": "编程语言",
    "tire long": "IR",
    "静暗容性": "向后兼容性",
    "AI slope": "AI slop",
    "硬研码": "硬编码",
    "bibration": "verification",
    "生成是软件工程": "生成式软件工程",
    "The Mexican Mammoth": "The Mythical Man-Month",
    "交游坑": "焦油坑",
    "冰死的动物": "濒死的动物",
    "或者信仰": "或者性能",
    "Cloud Fable": "Claude",
    "DeepSync": "DeepSeek",
    "AI for AC，SC for AR": "AI for SE、SE for AI",
    "分钟级能点别的": "分钟级能解决的",
    "弊补": "弥补",
    "补权": "补全",
    "low horizon": "short horizon",
    "cloud opus": "Claude Opus",
    "上下文一初": "上下文溢出",
    "一两个其实词": "一两个提示词",
    "绘画的历史": "对话的历史",
    "yolo模": "YOLO 模式",
    "ls-l": "ls -l",
    "include pass": "include path",
    "杀箱": "沙箱",
    "paster": "parser",
    "DPC v4 flash": "DeepSeek V4 Flash",
    "老大男的问题": "老大难的问题",
    "很大的票意": "很大的漂移",
    "huggingface": "Hugging Face",
    "仙灵校区": "仙林校区",
    "self-compagnate": "self-contained",
    "roll sum": "rule of thumb",
    "PG Student": "PhD student",
    "exterminate.js": "xterm.js",
    "打材的": "打出来的",
    "Aerware": "AI 味",
    "不常规的建具": "不常规的间距",
    "个人主业": "个人主页",
    "前代能力": "前端能力",
    "技术选行": "技术选型",
    "TileScript": "TypeScript",
    "churchTuring thesis": "Church-Turing thesis",
    "技术器": "计数器",
    "曼尼尔·布朗姆": "Manuel Blum",
    "Chat of Sol": "Chain of Thought",
    "test time skilling": "test-time scaling",
    "运脚": "韵脚",
    "核四共振": "核磁共振",
    "片方": "偏旁",
    "Chair of Thoughts": "Chain of Thought",
    "test to speech": "text-to-speech",
    "往身里面": "往深里面",
    "chain of salt": "chain of thought",
    "chill of salt": "chain of thought",
    "作题家": "做题家",
    "一个注视": "一个注释",
    "零食目": "临时目录",
    "AI slot": "AI slop",
    "车谷的话": "车轱辘话",
    "强头草": "墙头草",
    "实验座的": "实验做得",
    "HCMD": "AGENTS.md",
    "boots卖的太大": "步子迈得太大",
    "Commerce Science": "Computer Science",
    "夹谱树": "家谱树",
    "单遗产": "单遗传",
    "给剑出来": "给建出来",
    "真正这种，long horizon的认为": "真正这种 long horizon 的任务",
    "上下文版了": "上下文满了",
    "急品飞车": "极品飞车",
    "机品飞车": "极品飞车",
    "人乐成化": "《人月神话》",
    "原代码": "源代码",
    "文林斯内核": "Linux 内核",
    "特别删掉": "特别擅长",
    "Proven Engineering": "Prompt Engineering",
    "Suffer Tension": "self-attention",
    "松柔和": "松耦合",
    "操机系统": "操作系统",
    "操细系统": "操作系统",
    "互联网黑化": "互联网黑话",
    "指令上海文": "指令上下文",
    "宝贵的那些经历": "宝贵的那些精力",
    "Chelpsot": "ChatGPT",
    "perlumnal hierarchy": "polynomial hierarchy",
    "HamiltonPath": "Hamiltonian path",
    "试镜里的词": "《诗经》里的词",
    "destroint": "disjoint",
    "short token": "烧 token",
    "气堵墙": "筑一堵墙",
    "训练预料": "训练语料",
    "哪片我": "哪怕我",
    "好 今天": "好，今天",
    "生存式转件工程": "生成式软件工程",
    "DeepSeek vcflash": "DeepSeek V4 Flash",
    "deep seek vcflash": "DeepSeek V4 Flash",
    "DVCV4Flash": "DeepSeek V4 Flash",
    "pcglisflash": "DeepSeek V4 Flash",
    "cloudfable": "Claude",
    "AI耿，耿同学": "AI Council",
    "Authers": "authors",
    "gpt5.6": "GPT-5.6",
    "我没有prompt": "我们有prompt",
    "文字的代码图片": "文字、代码、图片",
    "py下的agent": "Pi下的agent",
    "内轮加载完了": "任务加载完了",
    "deepseek，chat": "DeepSeek Chat",
    "Pi更清凉": "Pi更轻量",
    "有些-IR这样的选项": "有些-I这样的选项",
    "抢头草": "墙头草",
    "前端能力": "前端能力",
    "偏方或者部首": "偏旁或者部首",
    "Chain of Thoughts": "Chain of Thought",
    "long horizon的认为": "long horizon的任务",
    "一个影看": "一个影子",
    "原汤化原始": "原汤化原食",
    "审考人": "审稿人",
    "你宝贵的那些经历": "你宝贵的那些精力",
    "起了同校的名字": "起了同样的名字",
    "无限的，计算资源": "无限的计算资源",
    "网年试卷": "往年试卷",
    "很听老实话": "很听老师话",
    "开选考试": "开卷考试",
    "隐私都引掉了": "隐私都隐掉了",
    "一大堆赛头": "一大堆title",
    "简历显": "简历亮点",
    "都有支付宝和微信量。二维码": "都有支付宝和微信，二维码",
    "在头就等于不存在": "在投就等于不存在",
    "课程显": "课程里",
    "隔离的上下文明": "隔离的上下文里面",
    "玩F5": "按F5",
    "阔写": "扩写",
    "导流乱器": "浏览器",
    "练乎了吗": "颠覆了吗",
    "专业选求课": "专业选修课",
    "形式与政策": "形势与政策",
    "尝试webcode": "尝试vibe coding",
    "大圆模型的支持": "大语言模型的知识",
    "Bronchia Lab": "frontier lab",
    "GCLVM": "GLM",
    "retracing": "ray tracing",
    "Communer Science": "Computer Science",
    "派，你只要": "Pi，你只要",
    "派里面": "Pi里面",
    "这个仓库，AGENTS.md": "这个仓库的AGENTS.md",
    "教室里面大概": "教室里面大概",
    "dc个充100块": "DeepSeek充100块",
    "两门谷的时间": "流量低谷的时间",
    "学习曲线态度": "学习曲线太陡",
    "不想用的评定": "不想用的壁垒",
    "非常的通过": "非常地痛苦",
    "我可以干净什么事": "我可以干一件什么事",
    "表面关要好": "表面上要好",
    "生存100年": "生存100年",
    "Slies": "slides",
    "审搞": "审稿",
    "滑翔买瓜": "滑翔伞买瓜",
    "神棍": "神棍",
    "USB的摄像头卡": "USB的视频采集卡",
    "只能做的，就是在，到处可以敲敲键盘": "唯一能做的，就是到处敲敲键盘",
    "外扣定出来": "vibe coding出来",
    "Word，可以": "World，可以",
    "HelloWord": "Hello World",
    "射屏": "摄屏",
    "电脏机网络": "计算机网络",
    "二维码偷出数据": "用二维码偷出数据",
    "一号.n9.16.16的思法": "一个典型的死法",
    "后续脸线人，5.3": "GLM-5.3",
    "顺激的GPT5.3": "新出的GLM-5.3",
    "AIGP5.3": "GLM-5.3",
    "GM5.3": "GLM-5.3",
    "你的bibration": "它的verification",
    "我做了一个中间语言": "我做了一个中间语言",
    "挣一个意": "挣一个亿",
    "强法呀": "想法呀",
    "规格空间": "规格空间",
    "奖励，他如果任务": "奖励，它如果任务",
    "功能，他不断地": "功能，它不断地",
    "测试用力": "测试用例",
    "信仰": "性能",
    "做其家": "做题家",
    "最确实品位": "最缺失品位",
    "主导QRG开发": "指导qrgen开发",
    "在投": "在投",
    "把自己蒸馏成一个skill": "把自己的经验蒸馏成一个skill",
    "指令上下文的增长": "指令上下文的增长",
    "经历，都是有限的": "精力，都是有限的",
    "人力是有": "人力是有限的",
    "这个时间是不能生的": "这个时间是不能省的",
    "怎么阻止指导qrgen开发": "怎么指导qrgen开发",
    "怎么设计一号的研究": "怎么设计一个好的研究",
    "Cloud Max": "Claude Max",
    "能直在解决的问题，把位置拆成便宜的实验": "能找到值得解决的问题，把未知拆成便宜的实验",
    "AI现在最缺失品位": "AI现在最缺失的是品位",
    "比如GM，或者DeepSeek": "比如GLM，或者DeepSeek",
    "你喜欢试镜": "你喜欢《诗经》",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("structured_json", type=Path)
    parser.add_argument("raw_srt", type=Path)
    parser.add_argument("frames_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--uploader", default="蒋炎岩")
    parser.add_argument("--course", default="2026 南京大学《生成式软件工程》")
    return parser.parse_args()


def parse_timestamp(value: str) -> float:
    hours, minutes, rest = value.split(":")
    seconds, millis = rest.split(",")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(millis) / 1000


def parse_srt(path: Path) -> list[dict]:
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8").strip())
    segments = []
    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3 or " --> " not in lines[1]:
            continue
        start, end = lines[1].split(" --> ")
        segments.append(
            {
                "start": parse_timestamp(start),
                "end": parse_timestamp(end),
                "text": " ".join(lines[2:]).strip(),
            }
        )
    return segments


def correct_terms(text: str) -> str:
    for source, target in CORRECTIONS.items():
        text = text.replace(source, target)
    text = re.sub(r"\bAI\s*的\s*agent\b", "AI Agent", text, flags=re.IGNORECASE)
    text = re.sub(r"\bagent\b", "Agent", text, flags=re.IGNORECASE)
    text = re.sub(r"\bcodex\b", "Codex", text, flags=re.IGNORECASE)
    text = re.sub(r"\bdeepseek\b", "DeepSeek", text, flags=re.IGNORECASE)
    text = re.sub(r"\bpre-LM\b", "pre-LLM", text, flags=re.IGNORECASE)
    text = re.sub(r"\bprompt\b", "prompt", text, flags=re.IGNORECASE)
    text = re.sub(r"\btoken\b", "token", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def remove_repeated_prefix(previous: str, current: str) -> str:
    max_overlap = min(len(previous), len(current))
    for size in range(max_overlap, 7, -1):
        if previous[-size:] == current[:size]:
            return current[size:].lstrip("，。！？； ")
    return current


def punctuation_for(text: str, gap: float, sentence_chars: int) -> str:
    question_markers = (
        "吗",
        "呢",
        "什么",
        "为什么",
        "怎么",
        "怎么样",
        "是不是",
        "对不对",
        "有没有",
        "哪里",
        "多少",
    )
    if text.endswith(question_markers):
        return "？"
    if gap >= 0.65 or sentence_chars >= 72:
        return "。"
    if text.endswith(("对吧", "是吧", "好", "OK", "Anyway", "没关系", "就结束了")):
        return "。"
    return "，"


def rebuild_text(
    segments: list[dict], start: float, end: float, used_segments: set[int]
) -> str:
    selected = [
        segment
        for segment in segments
        if segment["index"] not in used_segments
        and segment["end"] > start - 0.05
        and segment["start"] < end + 0.05
    ]
    if not selected:
        return ""
    parts = []
    sentence_chars = 0
    for index, segment in enumerate(selected):
        used_segments.add(segment["index"])
        text = correct_terms(segment["text"]).strip("，。！？； ")
        if not text:
            continue
        next_start = selected[index + 1]["start"] if index + 1 < len(selected) else end
        gap = max(0.0, next_start - segment["end"])
        sentence_chars += len(text)
        punctuation = punctuation_for(text, gap, sentence_chars)
        parts.append(text + punctuation)
        if punctuation in "。！？":
            sentence_chars = 0
    result = "".join(parts)
    result = result.rstrip("，") + ("。" if result.endswith("，") else "")
    return correct_terms(result)


def format_time(seconds: float) -> str:
    total = round(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}" if hours else f"{minutes:02d}:{secs:02d}"


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def source_at(url: str, seconds: float) -> str:
    return f"{url}{'&' if '?' in url else '?'}t={round(seconds)}"


def render_markdown(data: dict, args: argparse.Namespace) -> str:
    lines = [
        f"# {args.title}",
        "",
        f"- 课程：{args.course}",
        f"- 主讲：{args.uploader}",
        f"- 时长：{format_time(data['meta']['duration'])}",
        f"- 来源：[Bilibili 原视频]({args.source_url})",
        f"- 形式：课堂时间线图文实录（{len(data['sections'])} 张课堂截图）",
        "",
        "> 依照课堂原始顺序整理。正文只校正自动转写中的标点、断句和明确识别错误，不另作总结或改写。",
        "",
        "---",
        "",
    ]
    for section in data["sections"]:
        stamp = format_time(section["t"])
        lines.extend(
            [
                f"## [{stamp}]({source_at(args.source_url, section['t'])})",
                "",
                f"![{stamp}]({section['image']})",
                "",
            ]
        )
        for speech in section["speech"]:
            lines.extend([speech["text"], ""])
    return "\n".join(lines).rstrip() + "\n"


def render_html(data: dict, args: argparse.Namespace) -> str:
    sections = []
    for section in data["sections"]:
        stamp = format_time(section["t"])
        paragraphs = "\n".join(
            f"<p>{html.escape(speech['text'])}</p>" for speech in section["speech"]
        )
        sections.append(
            f"""<section>
<h2><a href="{html.escape(source_at(args.source_url, section['t']))}">{stamp}</a></h2>
<a href="{html.escape(section['image'])}"><img src="{html.escape(section['image'])}" alt="{stamp} 课堂画面" loading="lazy"></a>
{paragraphs}
</section>"""
        )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(args.title)}</title>
<style>
:root {{ color-scheme:light; --ink:#202124; --muted:#666; --line:#ddd; --link:#075985; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); background:#fff; font:17px/1.85 system-ui,-apple-system,"Segoe UI","Noto Sans CJK SC",sans-serif; }}
main {{ width:min(920px,calc(100% - 32px)); margin:48px auto 80px; }}
h1 {{ margin:0 0 16px; font-size:clamp(28px,5vw,42px); line-height:1.25; letter-spacing:0; }}
h2 {{ margin:52px 0 14px; padding-top:20px; border-top:1px solid var(--line); font-size:20px; letter-spacing:0; }}
a {{ color:var(--link); }}
.meta {{ color:var(--muted); }}
.notice {{ margin:24px 0 36px; padding:12px 16px; border-left:3px solid #0f766e; background:#f5faf9; }}
img {{ display:block; width:100%; height:auto; border:1px solid var(--line); }}
p {{ margin:16px 0; text-align:justify; }}
@media (max-width:600px) {{ main {{ width:min(100% - 20px,920px); margin-top:24px; }} body {{ font-size:16px; }} h2 {{ margin-top:36px; }} }}
</style>
</head>
<body>
<main>
<h1>{html.escape(args.title)}</h1>
<div class="meta">
<div>课程：{html.escape(args.course)}</div>
<div>主讲：{html.escape(args.uploader)}</div>
<div>时长：{format_time(data['meta']['duration'])}</div>
<div>来源：<a href="{html.escape(args.source_url)}">Bilibili 原视频</a></div>
<div>形式：课堂时间线图文实录（{len(data['sections'])} 张课堂截图）</div>
</div>
<p class="notice">依照课堂原始顺序整理。正文只校正自动转写中的标点、断句和明确识别错误，不另作总结或改写。</p>
{''.join(sections)}
</main>
</body>
</html>
"""


def render_srt(data: dict) -> str:
    blocks = []
    index = 1
    for section in data["sections"]:
        for speech in section["speech"]:
            blocks.append(
                f"{index}\n{srt_time(speech['start'])} --> {srt_time(speech['end'])}\n"
                f"{speech['text']}\n"
            )
            index += 1
    return "\n".join(blocks)


def main() -> None:
    args = parse_args()
    data = json.loads(args.structured_json.read_text(encoding="utf-8"))
    segments = parse_srt(args.raw_srt)
    for index, segment in enumerate(segments):
        segment["index"] = index
    used_segments: set[int] = set()
    previous = ""
    for section in data["sections"]:
        retained = []
        for speech in section["speech"]:
            speech["raw_text"] = speech["text"]
            rebuilt = rebuild_text(
                segments, speech["start"], speech["end"], used_segments
            )
            speech["text"] = remove_repeated_prefix(
                previous, rebuilt or correct_terms(speech["text"])
            )
            if not speech["text"]:
                continue
            retained.append(speech)
            previous = speech["text"]
        section["speech"] = retained

    data["meta"].update(
        {
            "title": args.title,
            "uploader": args.uploader,
            "webpage_url": args.source_url,
            "course": args.course,
        }
    )
    data["editing"] = {
        "policy": "pause-aware punctuation and manually reviewed evident ASR corrections; no summarization"
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "structured.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "course.md").write_text(
        render_markdown(data, args), encoding="utf-8"
    )
    (args.output_dir / "course.html").write_text(
        render_html(data, args), encoding="utf-8"
    )
    (args.output_dir / "transcript.cleaned.srt").write_text(
        render_srt(data), encoding="utf-8"
    )
    shutil.copy2(args.raw_srt, args.output_dir / "transcript.raw.srt")
    destination = args.output_dir / "frames"
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(args.frames_dir, destination)
    print(f"wrote {args.output_dir}")


if __name__ == "__main__":
    main()

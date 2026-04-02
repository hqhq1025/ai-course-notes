# AI Course Notes — 项目指南

## 项目概述

本仓库存放 CS/AI/LLM 相关公开课的中文讲义 PDF，基于视频字幕 + 官方 Slides 整理生成。

## 目录结构

```
ai-course-notes/
├── CLAUDE.md              # 本文件
├── README.md              # 课程索引
├── cs336/                 # Stanford CS336
│   ├── lecture05/
│   │   ├── lecture05-notes.pdf
│   │   ├── lecture05-notes.tex
│   │   ├── lecture05-slides.pdf   # 官方 slides
│   │   ├── lecture05.srt          # 字幕
│   │   ├── cover.jpg
│   │   └── slides-images/        # slides 逐页提取的图片
│   ├── lecture06/
│   └── ...
├── cs231n/                # 其他课程以此类推
└── ...
```

每节课一个子目录，包含：tex 源文件、编译后 PDF、字幕、slides（如有）、图片素材。

## 讲义生成流程

生成一节课的讲义分为 5 步：

### Step 1: 素材搜集（Supplementary Material Discovery）

**在下载视频之前**，先搜索该课程的官方补充材料：

1. 从视频标题提取课程代码、讲者、学校、年份
2. 按以下顺序搜索：
   - 视频描述中的直链
   - 课程官网（如 `stanford-cs336.github.io`）
   - GitHub 课程组织（如 `github.com/stanford-cs336`）
   - 讲者个人/实验室主页
   - 网络搜索 `"<course> slides pdf"`
3. 如果找到 slides PDF，用 `magick -density 200 slides.pdf slides-images/slide-%03d.jpg` 提取每页为高清图片
4. **有 slides 时优先用 slide 图片做插图**，视频帧仅作补充（白板、demo 等 slides 中没有的内容）
5. 找不到 slides 则回退到视频帧提取模式

### Step 2: 视频素材获取

1. 用 `yt-dlp --dump-json` 检查元数据（标题、章节、时长、字幕）
2. 下载封面图（最高分辨率 thumbnail）
3. 获取字幕（**哪里方便就从哪里拿**，不限定平台）：
   - 同一讲座若多平台有源，优先从有现成字幕的平台获取
   - YouTube：优先手动字幕，fallback 到 `youtube-transcript-api`
   - Bilibili：CC 字幕 → Whisper ASR → 纯视觉模式
   - 允许混合：视频从 A 平台下载，字幕从 B 平台获取
4. 下载视频（720p 通常够用于帧提取）

### Step 3: 通读字幕，梳理课程结构

- 合并字幕文本，提取教学结构（大纲、章节、知识点）
- 跳过非教学内容（问候、闲聊、赞助商、频道推广）
- 保留讲者总结性发言（有教学价值的结尾）

### Step 4: 撰写 LaTeX 讲义

基于 `assets/notes-template.tex` 模板，规则如下：

**语言**：中文（除非用户指定其他语言）

**结构**：
- 用 `\section{}` / `\subsection{}` 组织，重新梳理教学逻辑（不照搬字幕顺序）
- 每个大节结尾加 `\subsection{本章小结}`
- 有外链时加 `\subsection{拓展阅读}`
- 文档末尾必须有 `\section{总结与延伸}`

**三种高亮盒子**：
- `importantbox`（黄色）：核心概念、定义、定理、关键机制摘要
- `knowledgebox`（蓝色）：背景知识、前置提醒、历史脉络、设计权衡、类比
- `warningbox`（红色）：常见误解、隐含假设、容易犯的错误、因果混淆

盒子使用规则：
- **图片不得放在盒子内部**
- 每节无数量限制，以教学信号为准
- 每个盒子应携带具体的教学信息，不做装饰性使用

**图片**：
- 尽可能多地包含有教学价值的图（slides 页、关键帧、自绘 TikZ 图）
- 每张来自视频/slides 的图必须加脚注标注来源（slides 页码或视频时间区间）
- 使用 `[H]` 定位防止浮动

**公式**：用 `$$...$$` 展示，后紧跟符号逐项说明列表

**代码**：用 `lstlisting` 环境包裹，必须附 caption

### Step 5: 编译 PDF

```bash
cd <lecture-dir>
xelatex -interaction=nonstopmode <file>.tex  # 第一次（生成引用）
xelatex -interaction=nonstopmode <file>.tex  # 第二次（解析引用）
```

## LaTeX 模板

模板位于 `~/.claude/skills/youtube-render-pdf/assets/notes-template.tex`，主要特性：
- `ctex` + fandol 字体（无需额外安装）
- `tcolorbox` 三种高亮盒子
- `lstlisting` 代码块（默认 Python）
- `tikz` + `pgfplots` 绘图
- 封面自动展示视频封面图 + 元数据信息框

## CS336 特定信息

- 课程官网：https://stanford-cs336.github.io/
- YouTube 播放列表：https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_
- Spring 2025 Slides 仓库：https://github.com/stanford-cs336/spring2025-lectures
  - Tatsu 讲授的课（PDF）在 `nonexecutable/` 目录下
  - Percy 讲授的课以 `.py` 文件形式发布
- Spring 2024 Slides：https://github.com/stanford-cs336/spring2024-lectures

## 文章整理流程

除视频外，本仓库也整理技术博客、X/Twitter 文章等内容为 LaTeX PDF。

### 内容获取
- **博客/网页**：用 `fetch_content` 或 `WebFetch` 抓取全文
- **X/Twitter**：用 `api.fxtwitter.com/{user}/status/{id}` 获取 JSON，Article 内容在 `tweet.article.content.blocks` 中
- **YouTube**：沿用现有 youtube-render-pdf skill

### 译文处理规则（重要）
当文章为译文时（标题含【译】、正文标注"原文链接"、作者为已知翻译账号如 @dotey 等）：
1. **必须找到并获取原文**，基于原文内容整理笔记
2. 在笔记首页和元数据中标注原文作者、原文链接
3. 译文仅作参考，帮助理解术语翻译，不作为主要内容来源
4. 原文为英文时，笔记仍用中文撰写，但技术术语保留英文原文

### 目录结构
```
articles/
├── anthropic-harness-design/    # 按主题命名
│   ├── harness-design-notes.tex
│   ├── harness-design-notes.pdf
│   └── cover.jpg (如有)
├── karpathy-agentic-thinking/
└── ...
```

### LaTeX 适配
文章笔记复用视频讲义的 LaTeX 模板，但元数据区适配为：
- 首页标题改为"文章笔记"
- `\videochannel` → 文章作者/来源
- `\videopublishdate` → 发布日期
- `\videoduration` → 阅读时长（估算）
- 不需要视频时间戳脚注

## 环境注意事项

- **TikZ 编译极慢**：避免使用 TikZ 图，改用表格和文字描述
- **xeCJK `[` bug**：表格单元格以 `[` 开头会导致编译死循环，用 `{[}...{]}` 转义
- **Whisper 需要 python3.11**：系统默认 python3 是 3.12，torch 2.11 不支持 V100 (CC 7.0)，必须用 `python3.11` + torch 2.4.x
- **ffmpeg**：静态二进制在 `~/.local/bin/ffmpeg`
- **双 V100 GPU**：每张 32GB，Whisper large-v3 每实例 ~10GB，单卡可跑 3 实例，双卡最多 6 路并行
- 用 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 控制进程分配到哪张卡

## Bilibili 下载

- 未登录只能下载前 2-3 分钟音频，**必须使用 cookies**
- Cookies 文件：`bilibili_cookies.txt`（已在 .gitignore 中）
- 下载命令：`yt-dlp --cookies bilibili_cookies.txt -x -o "dir/audio.%(ext)s" URL`
- 音频格式通常是 m4a，Whisper 可直接读取（需要 ffmpeg）
- 封面下载：从 `--dump-json` 的 `thumbnail` 字段用 curl 下载

## 批量处理策略

处理大量视频时采用三阶段流水线，各阶段尽量并行：
1. **下载**：批量下载音频+封面（顺序即可，每个几秒）
2. **转录**：Whisper large-v3 多路并行（双卡 5-6 进程，用独立 Python 脚本 + `CUDA_VISIBLE_DEVICES`）
3. **讲义生成**：派多个 agent 并行生成 LaTeX（不同目录互不冲突）

已转录的可以先开始生成讲义，不必等全部转录完。每批 agent 控制在 8-16 讲以内防止超时。

## 完整目录结构

```
ai-course-notes/
├── cs336/                 # Stanford CS336 (17讲)
├── cs224n/                # Stanford CS224N (17讲)
├── cs231n/                # Stanford CS231N (18讲)
├── cs224r/                # Stanford CS224R Deep RL (19讲, 含 slides PDF)
├── cs146s/                # Stanford CS146S Modern SWE (10周, 基于 slides)
├── cs25/                  # Stanford CS25 Transformers United (40讲, V1-V5)
├── modern-agent/          # 五道口纳什 Modern Agent (16讲)
├── llm-architect/         # 五道口纳什 LLM Architect (10讲)
├── agentic-rl/            # 五道口纳什 Agentic RL + veRL (20讲)
├── interviews/            # 访谈 (杨植麟/季逸超/谢赛宁)
├── talks/
│   ├── berkeley-llm-agents/  # Berkeley CS294 LLM Agents (35讲, f24/sp25/f25)
│   ├── qingke-*/           # 青稞 AI 嘉年华 (4场圆桌)
│   ├── zhang-bo-agi/       # AGI 峰会演讲
│   └── ...
├── articles/              # 技术文章笔记
└── bilibili_cookies.txt   # (gitignored)
```

## 注意事项

- `yt-dlp` 版本需保持最新（`pip install --upgrade yt-dlp`），YouTube 经常更新反爬策略
- 字幕下载失败时用 `youtube-transcript-api` 作为 fallback
- slides 图片比视频帧质量高得多，优先使用
- 矩阵维度、公式细节以 slides 为准（字幕可能有听写错误）
- 编译 PDF 需要运行两次 xelatex 才能正确生成目录和引用
- X/Twitter 内容获取使用 `api.fxtwitter.com`（无需 API key，零依赖）
- YouTube 英文视频也用中文写讲义，技术术语保留英文
- Seminar 类课程（CS25, Berkeley LLM Agents）每讲是独立 talk，标题格式 `[系列名] 主题 — 嘉宾`

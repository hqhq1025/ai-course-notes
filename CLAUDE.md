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
3. 获取字幕：
   - YouTube：优先手动字幕，fallback 到 `youtube-transcript-api`
   - Bilibili：CC 字幕 → Whisper ASR → 纯视觉模式
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

## 注意事项

- `yt-dlp` 版本需保持最新（`pip install --upgrade yt-dlp`），YouTube 经常更新反爬策略
- 字幕下载失败时用 `youtube-transcript-api` 作为 fallback
- slides 图片比视频帧质量高得多，优先使用
- 矩阵维度、公式细节以 slides 为准（字幕可能有听写错误）
- 编译 PDF 需要运行两次 xelatex 才能正确生成目录和引用

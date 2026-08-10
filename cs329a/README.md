# Stanford CS329A: Self-Improving AI Agents

本目录对应 Stanford CS329A（Autumn 2025）的 9-Part 官方公开视频课程。课程主页列出的完整学期还包括 guest lectures、期中展示与项目环节；这里的讲义范围以 Stanford Online 发布的官方 9-Part 播放列表为准。

## 课程来源

- 课程主页：<https://cs329a.stanford.edu/>
- 官方播放列表：<https://www.youtube.com/playlist?list=PLangBM27OtEA>
- 在线阅读：<https://hqhq1025.github.io/ai-course-notes/cs329a/>
- 授课教师：Aakanksha Chowdhery、Azalia Mirhoseini
- 讲义生成规范：`wdkns/wdkns-skills` 的 `youtube-render-pdf`，固定到 commit `39f1a04c46e1d0d70f6b71a8fcf079b305a632b9`（2026-08-09），并叠加本仓库 `CLAUDE.md`、`QUALITY.md` 与 `CONTRIBUTING.md` 的结构和质量要求。

## 讲义目录

9 讲均已完成中文 LaTeX 讲义、原始课件关键帧与同页视频时间脚注；本地最终 PDF 共 215 页，均经 XeLaTeX 双遍编译并通过仓库课程级结构审计。按照仓库当前发布策略，生成的 `*-notes.pdf` 保留在本地但不提交，GitHub Pages 直接从 LaTeX 源码生成在线讲义。

| Part | 主题 | 本地 PDF 页数 | 中文讲义源码 | 视频 |
|---:|---|---:|---|---|
| 1 | Course Overview | 21 | [LaTeX](lecture01/lecture01-notes.tex) | [YouTube](https://www.youtube.com/watch?v=6YnLB0XbTnI) |
| 2 | Test-Time Compute Scaling | 23 | [LaTeX](lecture02/lecture02-notes.tex) | [YouTube](https://www.youtube.com/watch?v=-Ggc37xLj_Y) |
| 3 | Robust Verification | 22 | [LaTeX](lecture03/lecture03-notes.tex) | [YouTube](https://www.youtube.com/watch?v=p7TdPUcPoik) |
| 4 | Learning from Feedback with Tools/Code | 20 | [LaTeX](lecture04/lecture04-notes.tex) | [YouTube](https://www.youtube.com/watch?v=Lxh9RF5S-K0) |
| 5 | Planning and Multi-Step Reasoning | 23 | [LaTeX](lecture05/lecture05-notes.tex) | [YouTube](https://www.youtube.com/watch?v=Ml_fp9XkB8Y) |
| 6 | Train-Time Scaling / Scaling RL | 23 | [LaTeX](lecture06/lecture06-notes.tex) | [YouTube](https://www.youtube.com/watch?v=yVnmHSAy3ck) |
| 7 | Self-Improvement and Deep Research Agents | 26 | [LaTeX](lecture07/lecture07-notes.tex) | [YouTube](https://www.youtube.com/watch?v=Uni9dqyuuDM) |
| 8 | Agentic Evaluations and Long-Horizon Tasks | 27 | [LaTeX](lecture08/lecture08-notes.tex) | [YouTube](https://www.youtube.com/watch?v=8JAqLnTaZu4) |
| 9 | Future Research Areas | 30 | [LaTeX](lecture09/lecture09-notes.tex) | [YouTube](https://www.youtube.com/watch?v=AyO6wyu4DEg) |

## 内容与图源规范

- 每讲按教学逻辑重构，不是字幕逐句翻译；技术术语保留英文。
- 所有正文插图均来自对应视频实际画面，语义化文件名位于 `figures/`。
- `figure-manifest.tsv` 记录每张图的精确视频帧时间和讲解区间。
- 公式后解释符号，高信号内容使用核心概念、背景知识与常见误解盒子。
- 每讲包含章节小结、拓展阅读以及课程级总结与开放问题。

## 可复现素材下载

```bash
bash cs329a/download_materials.sh metadata
bash cs329a/download_materials.sh video
```

每讲目录保留公开稳定字段组成的 `metadata.json`、人工字幕、原始封面、视频、教学关键帧、LaTeX 源文件和编译后的 PDF。完整 yt-dlp dump 写入本地忽略的 `metadata.full.json`，避免把临时签名媒体 URL 和请求头提交到公开仓库。视频与候选帧用于本地复现；最终提交内容以讲义、封面、`figures/` 和 `figure-manifest.tsv` 为主。

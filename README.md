<div align="center">

# 📚 AI Course Notes

**368 份 AI / LLM 中文讲义，支持在线阅读、LaTeX 源码查看与本地 PDF 编译**

基于公开课视频字幕、课程 slides、访谈、技术文章与公开资料整理，使用 LaTeX 生成 PDF，并自动发布为可搜索的网页阅读站。

[![Online Reading](https://img.shields.io/badge/在线阅读-GitHub%20Pages-00A884?style=for-the-badge)](https://hqhq1025.github.io/ai-course-notes/)
[![Total Notes](https://img.shields.io/badge/讲义总数-368份-blue?style=for-the-badge)](.)
[![Collections](https://img.shields.io/badge/内容系列-17个-green?style=for-the-badge)](.)
[![Format](https://img.shields.io/badge/格式-Web%20%7C%20LaTeX%20%7C%20Local%20PDF-red?style=for-the-badge)](.)

[🌐 在线阅读](https://hqhq1025.github.io/ai-course-notes/) · [📄 浏览目录](#-课程一览) · [🤝 参与贡献](CONTRIBUTING.md)

</div>

---

## ✨ 这是什么

- **在线阅读优先**：网页站点支持目录导航、全文搜索和公式渲染；正文默认加载优化后的图片，点击即可查看仓库原图。
- **中文讲义**：英文课程、访谈和文章统一整理为中文，关键技术术语保留英文。
- **覆盖面广**：从 Transformer、LLM pretraining、RLHF，到 Agent、Diffusion、Infra、模型架构和 AI 工程实践。
- **LaTeX 为源文稿**：仓库保留 `*-notes.tex` 和配套图片，网页由 `.tex` 自动生成；讲义 PDF 可在本地编译，不重复存入 Git。
- **持续更新**：新课程、演讲、访谈和技术文章会继续补充。

## 🌐 在线阅读

在线站点：**[https://hqhq1025.github.io/ai-course-notes/](https://hqhq1025.github.io/ai-course-notes/)**

站点由 [tools/web/generate_site.py](tools/web/generate_site.py) 从仓库中的 LaTeX 讲义自动生成 MkDocs 项目，并通过 [.github/workflows/pages.yml](.github/workflows/pages.yml) 在 `main` 分支更新后部署到 GitHub Pages。

> 大多数用户**不需要 clone** —— 直接访问在线站即可阅读、搜索全部 368 份讲义。

## 📥 克隆指南

仓库历史中累积了大量 PDF、图片和字幕，完整克隆体积较大（数 GB）。请按需选择克隆方式：

| 方式 | 命令 | 适用场景 | 体积量级 |
|------|------|----------|----------|
| **浅克隆** | `git clone --depth=1 https://github.com/hqhq1025/ai-course-notes.git` | 只想读最新版本（推荐） | 几百 MB |
| **无 blob 克隆** | `git clone --filter=blob:none https://github.com/hqhq1025/ai-course-notes.git` | 想保留完整历史，但按需下载文件内容 | ~2 GB |
| **稀疏 checkout** | 见下方 | 只关心某一门课（例如 cs336） | 几十 MB |
| **完整克隆** | `git clone https://github.com/hqhq1025/ai-course-notes.git` | 想拿到所有历史与文件 | 数 GB |

只克隆某门课（以 cs336 为例）：

```bash
git clone --filter=blob:none --no-checkout https://github.com/hqhq1025/ai-course-notes.git
cd ai-course-notes
git sparse-checkout init --cone
git sparse-checkout set cs336
git checkout main
```

## 📄 PDF 与 LaTeX

- **直接阅读**：推荐使用[在线阅读站](https://hqhq1025.github.io/ai-course-notes/)，无需下载 PDF；网页图片使用优化副本，点击图片可打开原图。
- **LaTeX 源码**：每篇在线讲义顶部都有“LaTeX 源码”入口，也可以 clone 仓库后直接查看对应的 `*-notes.tex`。
- **自行生成 PDF**：仓库不再提交可由源码重复生成的 `*-notes.pdf`。下载对应课程目录后，使用 XeLaTeX 连续编译两遍即可生成目录和交叉引用完整的 PDF。
- **官方课件**：课程方发布的 `*-slides.pdf` 无法由讲义源码重建，因此仍会保留。

```bash
git clone --depth=1 https://github.com/hqhq1025/ai-course-notes.git
cd ai-course-notes/<course>/<lecture>
xelatex -interaction=nonstopmode -halt-on-error <lecture>-notes.tex
xelatex -interaction=nonstopmode -halt-on-error <lecture>-notes.tex
```

例如编译 CS329A 第一讲：

```bash
cd ai-course-notes/cs329a/lecture01
xelatex -interaction=nonstopmode -halt-on-error lecture01-notes.tex
xelatex -interaction=nonstopmode -halt-on-error lecture01-notes.tex
```

## 📊 内容规模

| 分类 | 数量 | 说明 |
|------|------|------|
| Stanford 课程 | 169 | CS329A、CS336、CS224R、CS25、CS153、CS146S、CS224N、CS231N |
| MIT 课程 | 10 | MIT 6.S191 Introduction to Deep Learning |
| KAIST 课程 | 15 | CS492D Diffusion Models and Flow Models |
| Berkeley 课程 | 35 | CS294 LLM Agents / Advanced LLM Agents / Agentic AI |
| B 站系列课程 | 48 | Modern Agent、LLM Architect、Agentic RL、Self-Evolving Agents 2026 |
| 演讲与访谈 | 67 | Lex Fridman、Dwarkesh Patel、青稞、WhynotTV、张小珺等 |
| 技术文章笔记 | 25 | Agent Harness、Claude Code、Codex、Agentic Memory 等 |
| **合计** | **369** | 统计口径：仓库内 `*-notes.tex` 讲义源文件 |

---

## 📋 课程一览

### 🏫 Stanford 课程 (169 份)

| 课程 | 主题 | 讲数 | 讲者 |
|------|------|------|------|
| [**CS329A**](cs329a/) | Self-Improving AI Agents | 9 | Aakanksha Chowdhery, Azalia Mirhoseini |
| [**CS336**](cs336/) / [**CS336 2026**](cs336-2026/) | Language Modeling from Scratch | 17 + 18 | Percy Liang, Tatsu Hashimoto |
| [**CS224R**](cs224r/) | Deep Reinforcement Learning | 19 | Chelsea Finn |
| [**CS25**](cs25/) / [**CS25 V6**](cs25-v6/) | Transformers United (V1-V6) | 41 + 9 | Hinton, Karpathy, Vaswani, Noam Brown... |
| [**CS153**](cs153/) | Infra @ Scale / Frontier Systems | 11 | Anjney Midha + 业界领袖 |
| [**CS146S**](cs146s/) | The Modern Software Developer | 10 | Mihail Eric + 业界嘉宾 |
| [**CS224N**](cs224n/) | NLP with Deep Learning | 17 | Chris Manning |
| [**CS231N**](cs231n/) | Deep Learning for Computer Vision | 18 | — |

> **CS336 Spring 2026 第二轮重写已完成（2026-08-11）**：18/18 讲共 607 页、561 张图、824 个教学盒；全部通过 strict source coverage、`⭐⭐⭐` 质量检查、双遍 XeLaTeX 与人工 PDF 视觉 QA。有 transcript 或 executable narration 的讲次均附 teacher-voice ledger。

> **CS25 V1--V5 全量重写已完成（2026-08-12）**：41/41 讲共 2,021 页、2,051 张图、1,598 个教学盒，均按 source-first 工作流重建并通过 strict coverage、`⭐⭐⭐`、双遍 XeLaTeX 与人工 PDF 视觉 QA；官方 slides、录像恢复 teaching states、teacher-voice ledger、coverage matrix 与 QA 报告均随讲次保存。

> **CS25 V6 全量生成已完成（2026-08-13）**：9/9 讲共 472 页、474 张教学图、393 个教学盒，全部按 source-first / teacher-voice / slide-complete 流程制作，并通过 strict coverage、`⭐⭐⭐`、稳定双遍 XeLaTeX 与人工 PDF 视觉 QA。Lecture 09 `Serving Transformers: Lessons from the Trenches of Production Inference` 为 59 页，覆盖 57 张 required 官方 deck pages + 1 张 live token-timing demo，包含 71 个教学盒、12 个公式块与 7 个代码 listing；完整审计 82:31 录像的 990 个五秒采样和 17 张 contact sheets，未把录像未讲的 CI/CL appendix 与招聘页补造成课堂内容。课程范围与官方链接记录在 [`cs25-v6/COURSE_SCOPE.md`](cs25-v6/COURSE_SCOPE.md)。

### 🏛 MIT 课程 (10 份)

| 课程 | 主题 | 讲数 | 讲者 |
|------|------|------|------|
| [**6.S191**](6s191/) | Introduction to Deep Learning | 10 | Alexander Amini + 业界嘉宾 |

### 🇰🇷 KAIST 课程 (15 份)

| 课程 | 主题 | 讲数 | 讲者 |
|------|------|------|------|
| [**CS492D**](kaist-cs492d/) | Diffusion Models and Flow Models | 15 | Minhyuk Sung |

### 🐻 Berkeley 课程 (35 份)

| 课程 | 主题 | 讲数 | 亮点嘉宾 |
|------|------|------|----------|
| [**CS294 F24**](talks/berkeley-llm-agents/f24/) | LLM Agents | 12 | Denny Zhou, 姚顺雨, Jim Fan, Percy Liang |
| [**CS294 SP25**](talks/berkeley-llm-agents/sp25/) | Advanced LLM Agents | 12 | Jason Weston, AlphaProof, Salakhutdinov |
| [**CS294 F25**](talks/berkeley-llm-agents/f25/) | Agentic AI | 11 | Noam Brown, Oriol Vinyals, James Zou |

### 🇨🇳 B 站系列课程 (48 份)

| 系列 | 主题 | 讲数 | UP 主 |
|------|------|------|------|
| [**Modern Agent**](modern-agent/) | LLM Agent 实战 (ReAct, RAG, Codex) | 17 | 五道口纳什 |
| [**LLM Architect**](llm-architect/) | 模型架构 (MoE, RoPE, VLM, K2.5) | 10 | 五道口纳什 |
| [**Agentic RL**](agentic-rl/) | RL for LLM (PPO→GRPO→DPO, veRL) | 20 | 五道口纳什 |
| [**Self-Evolving Agents 2026**](self-evolving-agents-2026/) | 因果世界模型、Agentic RL、经验智能、能力外部化与 Agent 理论 | 1 册 / 9 单元 | NICE 学术 |

### 🎤 演讲与访谈 (29 份)

| 来源 / 频道 | 主题 | 数量 | 目录 |
|-------------|------|------|------|
| [**Lex Fridman Podcast**](talks/lex-fridman/) | Dario Amodei、Jensen Huang、State of AI、DeepSeek、中国 AI、OpenClaw | 5 | talks |
| [**AITIME 论道**](talks/aitime/) | 张钹、林俊旸、姚顺雨、杨植麟 | 4 | talks |
| [**青稞社区**](talks/qingke/) | LLM、Agentic、RL、Infra 圆桌 | 4 | talks |
| [**WhynotTV**](interviews/whynot-tv/) | 陈天奇、翁嘉颐、胡渊鸣、杨硕 | 4 | interviews |
| [**张小珺商业访谈录**](interviews/zhang-xiaojun/) | 季逸超、谢赛宁、杨植麟 | 3 | interviews |
| [**Ungrounded 不着边际**](interviews/ungrounded/) | GUI Agent、SGLang | 2 | interviews |
| [**Dwarkesh Patel Podcast**](talks/dwarkesh-patel/) | Ilya Sutskever: From Scaling to Research | 1 | talks |
| [**No Priors Podcast**](talks/no-priors/) | Andrej Karpathy: Code Agents & AutoResearch | 1 | talks |
| [**20VC with Harry Stebbings**](talks/20vc/) | Demis Hassabis: AGI, Scaling Laws & DeepMind | 1 | talks |
| [**Cleo Abram**](talks/cleo-abram/) | Jensen Huang: NVIDIA Vision | 1 | talks |
| [**Greg Isenberg**](talks/greg-isenberg/) | Claude Cowork & Code | 1 | talks |
| [**NVIDIA GTC**](talks/nvidia-gtc/) | 杨植麟 K2.5 | 1 | talks |
| [**阿里云**](talks/alibaba-cloud/) | AGI 圆桌 | 1 | talks |

### 📝 技术文章笔记 (25 篇)

<details>
<summary><b>点击展开文章列表</b></summary>

| 文章 | 来源 |
|------|------|
| **Agent Harness Engineering 专题** | |
| [Harness Engineering](articles/openai-harness-engineering/) | OpenAI |
| [Building Effective Agents](articles/anthropic-building-agents/) | Anthropic |
| [Writing Effective Tools](articles/anthropic-writing-tools/) | Anthropic |
| [Effective Harnesses for Long-Running Agents](articles/anthropic-effective-harnesses/) | Anthropic |
| [Harness Design for Long-Running Apps](articles/anthropic-harness-long-running/) | Anthropic |
| [Improving Deep Agents with Harness Engineering](articles/langchain-improving-deep-agents/) | LangChain |
| [Evaluating Deep Agents](articles/langchain-evaluating-deep-agents/) | LangChain |
| [Agent Needs a Harness, Not a Framework](articles/inngest-agent-harness/) | Inngest |
| [Skill Issue: Harness Engineering](articles/humanlayer-skill-issue/) | HumanLayer |
| [Harness Engineering](articles/fowler-harness-engineering/) | Martin Fowler |
| **其他** | |
| [Anthropic Harness Design](articles/anthropic-harness-design/) | Anthropic Blog |
| [Karpathy: Vibe Coding](articles/dotey-karpathy-translation/) | @kabornethy (宝玉译) |
| [Claude Code Skills 指南](articles/dotey-claude-code-skills-translation/) | @dotey (宝玉译) |
| [Google Agent Skill Patterns](articles/google-agent-skill-patterns/) | Google Blog |
| [OpenAI Codex Best Practices](articles/openai-codex-best-practices/) | OpenAI |
| [OpenAI Codex Datasets](articles/openai-codex-datasets/) | OpenAI |
| [Claude vs Codex](articles/hesamation-claude-vs-codex/) | @hesamation |
| [Claude Architect 模式](articles/hooeem-claude-architect/) | @hooeem |
| [Agentic Memory](articles/ram-agentic-memory/) | @ramfromindia |
| [林俊旸: Agentic Thinking](articles/junyang-lin-agentic-thinking/) | @junyang_lin |
| [10x Skills 指南](articles/minli-10x-skills-translation/) | @MinLiBuilds (实践哥译) |
| [50 Claude Tips](articles/vishwas-50-claude-tips/) | @vishwas_ai |
| [Claude Code Best Practices](articles/panda-claude-code-best-practices/) | @panda_quant |
| [Cowork Starter](articles/corey-cowork-starter/) | @corey_latislaw |
| [Notes from inside China's AI labs](articles/interconnects-china-ai-labs/) | Interconnects AI |

</details>

---

## 🔥 推荐阅读路线

```text
入门 LLM
CS336 → CS224R L09 (RLHF) → CS25 V2 Karpathy (Transformer 入门)

深入 Agent
Berkeley F24 姚顺雨 Agent 概述 → CS329A → Modern Agent 全系列 → Agentic RL 全系列

模型架构
LLM Architect 全系列 → CS25 V4 Mixtral → CS336 L04 MoE

前沿洞察
Ilya Sutskever → Dario Amodei → Lex Fridman State of AI 2026
```

## 📁 目录结构

```text
ai-course-notes/
├── cs329a/                   # Stanford CS329A Self-Improving AI Agents (9 讲)
├── cs336/                    # Stanford CS336 (17 讲)
├── cs336-2026/               # Stanford CS336 Spring 2026 (18 讲, 完整)
├── cs153/                    # Stanford CS153 Infra @ Scale (11 讲)
├── cs224n/                   # Stanford CS224N (17 讲)
├── cs231n/                   # Stanford CS231N (18 讲)
├── cs224r/                   # Stanford CS224R (19 讲, 含 slides)
├── cs146s/                   # Stanford CS146S (10 周, 基于 slides)
├── cs25/                     # CS25 Transformers United (41 讲)
├── cs25-v6/                  # CS25 Transformers United V6 (9 讲, 完整)
├── 6s191/                    # MIT 6.S191 (10 讲)
├── kaist-cs492d/             # KAIST CS492D (15 讲)
├── modern-agent/             # 五道口纳什 Modern Agent (17 讲)
├── llm-architect/            # 五道口纳什 LLM Architect (10 讲)
├── agentic-rl/               # 五道口纳什 Agentic RL + veRL (20 讲)
├── interviews/               # 深度访谈，按频道/来源分组
├── talks/                    # 演讲与公开课，按频道/来源分组
├── articles/                 # 技术文章笔记
├── tools/web/                # 在线阅读站生成器
└── .github/workflows/        # GitHub Pages 自动部署
```

## ⚙️ 生成方式

```mermaid
graph LR
    A[YouTube/Bilibili 视频] --> B[yt-dlp 下载]
    B --> C{有字幕?}
    C -->|是| D[下载 SRT]
    C -->|否| E[Whisper large-v3]
    E --> D
    D --> F[Claude 智能整理]
    G[官方 Slides / 公开资料] --> F
    F --> H[LaTeX 源文件]
    H --> I[XeLaTeX 编译]
    I --> J[PDF 讲义]
    H --> K[网页阅读站]
```

### 本地预览在线阅读站

```bash
python -m pip install -r requirements-web.txt
python tools/web/generate_site.py --strict --skip-tikz
mkdocs serve -f .web-build/mkdocs.yml
```

完整构建与 GitHub Pages 工作流一致：

```bash
python tools/web/generate_site.py --strict --verbose-warnings --fail-on-tikz-warnings
mkdocs build -f .web-build/mkdocs.yml --strict
```

## 🔗 项目链接

| 项目 | 地址 |
|------|------|
| GitHub 仓库 | [github.com/hqhq1025/ai-course-notes](https://github.com/hqhq1025/ai-course-notes) |
| 在线阅读站 | [hqhq1025.github.io/ai-course-notes](https://hqhq1025.github.io/ai-course-notes/) |
| GitHub Pages 工作流 | [.github/workflows/pages.yml](.github/workflows/pages.yml) |
| 站点生成器 | [tools/web/generate_site.py](tools/web/generate_site.py) |
| 贡献指南 | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 质量标准 | [QUALITY.md](QUALITY.md) |

## 🔗 课程资源链接

| 课程 | 官网 | YouTube | Slides |
|------|------|---------|--------|
| CS329A | [cs329a.stanford.edu](https://cs329a.stanford.edu/) | [9-Part 播放列表](https://www.youtube.com/playlist?list=PLangBM27OtEA) | 视频内课件 |
| CS336 | [cs336.stanford.edu](https://cs336.stanford.edu/) | [Spring 2025 播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) | [Spring 2026 GitHub](https://github.com/stanford-cs336/lectures) |
| CS153 | [cs153.stanford.edu](https://cs153.stanford.edu/) | [W25](https://www.youtube.com/playlist?list=PL2aDf5-VARtCwgVceDClce1OcnUk1vIvR) · [S26](https://www.youtube.com/playlist?list=PL2aDf5-VARtBwz1kz5FsuSZXOig2U6aJI) | — |
| CS224R | [cs224r.stanford.edu](https://cs224r.stanford.edu/) | [播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL) | [官网](https://cs224r.stanford.edu/spring_2025/slides/) |
| CS25 | [web.stanford.edu/class/cs25](https://web.stanford.edu/class/cs25/) | [播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) | — |
| CS146S | [themodernsoftware.dev](https://themodernsoftware.dev) | — | Google Slides |
| CS224N | [官网](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/) | [播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) | [官网](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/) |
| CS231N | [cs231n.stanford.edu](https://cs231n.stanford.edu/) | [播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb) | [官网](https://cs231n.stanford.edu/slides/2025) |
| KAIST CS492D | [course page](https://mhsung.github.io/kaist-cs492d-fall-2024/) | [播放列表](https://www.youtube.com/playlist?list=PLQ28Nx3M4JrhkqBVIXg-i5_CVVoS1UzAv) | — |
| Berkeley LLM Agents | [rdi.berkeley.edu](https://rdi.berkeley.edu/llm-agents/f24) | [F24](https://www.youtube.com/playlist?list=PLS01nW3RtgopsNLeM936V4TNSsvvVglLc) · [SP25](https://www.youtube.com/playlist?list=PLS01nW3RtgorL3AW8REU9nGkzhvtn6Egn) · [F25](https://www.youtube.com/playlist?list=PLS01nW3RtgoqGkm4UeqNeZLccW-OGc1fJ) | [rdi.berkeley.edu](https://rdi.berkeley.edu/llm-agents/assets/) |

---

## 🤝 贡献

欢迎提 Issue 或 PR：

- 发现讲义内容错误
- 推荐新课程、演讲、访谈或技术文章
- 改进现有讲义质量
- 优化在线阅读站生成效果

更多说明见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [QUALITY.md](QUALITY.md)。

## 🙏 致谢

讲义生成工具链基于 [wdkns-skills](https://github.com/wdkns/wdkns-skills)（五道口纳什）改进，在此基础上增加了模块化重构、批量处理脚本、文章整理 skill 和在线阅读站生成器等扩展。

## 📜 License

本仓库的讲义、工具和脚本采用 [CC BY-NC-SA 4.0](LICENSE) 许可证。

本项目仅供学习和研究用途。仓库中引用的课程 slides、视频截图等素材的版权归原作者和所属机构所有。如果您是相关内容的版权持有者，认为本项目侵犯了您的权益，请通过 [Issues](../../issues) 联系我们，我们会在确认后第一时间移除相关内容。

<div align="center">

**⭐ 如果觉得有用，请给个 Star！**

</div>

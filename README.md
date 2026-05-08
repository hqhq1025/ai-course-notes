<div align="center">

# 📚 AI Course Notes

**301 份 AI / LLM 公开课中文讲义 PDF**

基于视频字幕（Whisper large-v3）、课程 Slides 和公开资料，自动生成的高质量 LaTeX 讲义

[![Total Notes](https://img.shields.io/badge/讲义总数-301份-blue?style=for-the-badge)](.)
[![Courses](https://img.shields.io/badge/课程系列-15个-green?style=for-the-badge)](.)
[![PDF](https://img.shields.io/badge/格式-LaTeX%20PDF-red?style=for-the-badge)](.)

</div>

---

## ✨ 亮点

- 🎯 **覆盖广泛**：从 Transformer 原理到 LLM Agent 实战，从强化学习到模型架构设计
- 📖 **中文讲义**：英文课程也全部整理为中文，技术术语保留英文
- 🎨 **排版精美**：LaTeX 专业排版，三种高亮盒子（核心概念/背景知识/常见误解）
- 🤖 **自动化生成**：Whisper 语音转录 + Claude 智能整理 + XeLaTeX 编译
- 🔄 **持续更新**：新课程和演讲持续收录中

---

## 📋 课程一览

### 🏫 Stanford 课程 (142 份)

| 课程 | 主题 | 讲数 | 讲者 |
|------|------|------|------|
| [**CS336**](cs336/) / [**2026**](cs336-2026/) | Language Modeling from Scratch | 17 + 10 | Percy Liang, Tatsu Hashimoto |
| [**CS224R**](cs224r/) | Deep Reinforcement Learning | 19 | Chelsea Finn |
| [**CS25**](cs25/) | Transformers United (V1-V5) | 40 | Hinton, Karpathy, Vaswani, Noam Brown... |
| [**CS153**](cs153/) | Infra @ Scale / Frontier Systems | 11 | Anjney Midha + 业界领袖 |
| [**CS146S**](cs146s/) | The Modern Software Developer | 10 | Mihail Eric + 业界嘉宾 |
| [**CS224N**](cs224n/) | NLP with Deep Learning | 17 | Chris Manning |
| [**CS231N**](cs231n/) | Deep Learning for Computer Vision | 18 | — |

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

### 🇨🇳 B站系列课程 (47 份)

| 系列 | 主题 | 讲数 | UP主 |
|------|------|------|------|
| [**Modern Agent**](modern-agent/) | LLM Agent 实战 (ReAct, RAG, Codex) | 17 | 五道口纳什 |
| [**LLM Architect**](llm-architect/) | 模型架构 (MoE, RoPE, VLM, K2.5) | 10 | 五道口纳什 |
| [**Agentic RL**](agentic-rl/) | RL for LLM (PPO→GRPO→DPO, veRL) | 20 | 五道口纳什 |

### 🎤 演讲与访谈 (28 份)

<details>
<summary><b>点击展开完整列表</b></summary>

| 嘉宾 | 主题 | 来源 |
|------|------|------|
| **Ilya Sutskever** | From Scaling to Research | Dwarkesh Patel |
| **Dario Amodei** | Claude, AGI & Humanity | Lex Fridman |
| **Andrej Karpathy** | Code Agents & AutoResearch | No Priors |
| **Jensen Huang** ×2 | NVIDIA Vision / $4T AI Revolution | Cleo Abram / Lex |
| **杨植麟** ×3 | K2 对话 / Scaling Law / GTC K2.5 | 张小珺 / AITIME / GTC |
| **季逸超** | Manus 最后的访谈 | 张小珺 |
| **谢赛宁** | 7h 马拉松访谈 | AMI |
| **Lex Fridman** ×2 | State of AI 2026 / DeepSeek & China | Lex Fridman |
| **Peter Steinberg** | OpenClaw Agent | Lex Fridman |
| **青稞嘉年华** ×4 | LLM / Agentic / RL / Infra 圆桌 | 青稞社区 |
| **AGI 峰会** ×4 | 张钹 / 林俊旸 / 姚顺雨 / 阿里圆桌 | AITIME / 阿里云 |
| **Greg Isenberg** | Claude Cowork & Code | YouTube |
| **Demis Hassabis** | AGI, Scaling Laws & DeepMind 战略 | 20VC Podcast |

### 📝 技术文章笔记 (24 篇)

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

</details>

---

## 🔥 推荐阅读路线

### 入门 LLM
```
CS336 (从零训LLM) → CS224R L09 (RLHF) → CS25 V2 Karpathy (Transformer入门)
```

### 深入 Agent
```
Berkeley F24 姚顺雨 (Agent概述) → Modern Agent 全系列 → Agentic RL 全系列
```

### 模型架构
```
LLM Architect 全系列 → CS25 V4 Mixtral → CS336 L04 (MoE)
```

### 前沿洞察
```
Ilya (Research时代) → Dario (AGI路线) → Lex (State of AI 2026)
```

---

## 📁 目录结构

```
ai-course-notes/
├── cs336/                    # Stanford CS336 (17讲)
├── cs336-2026/               # Stanford CS336 Spring 2026 (进行中)
├── cs153/                    # Stanford CS153 Infra@Scale (11讲)
├── cs224n/                   # Stanford CS224N (17讲)
├── cs231n/                   # Stanford CS231N (18讲)
├── cs224r/                   # Stanford CS224R (19讲, 含 slides)
├── cs146s/                   # Stanford CS146S (10周, 基于 slides)
├── cs25/                     # CS25 Transformers United (40讲)
├── kaist-cs492d/             # KAIST CS492D (15讲)
├── modern-agent/             # 五道口纳什 Modern Agent (17讲)
├── llm-architect/            # 五道口纳什 LLM Architect (10讲)
├── agentic-rl/               # 五道口纳什 Agentic RL + veRL (20讲)
├── interviews/               # 深度访谈（按频道/来源分组）
│   ├── whynot-tv/            # WhynotTV
│   ├── zhang-xiaojun/        # 张小珺商业访谈录
│   └── ungrounded/           # Ungrounded 不着边际
├── talks/                    # 演讲与访谈（按频道/来源分组）
│   ├── berkeley-llm-agents/  # Berkeley CS294 (35讲)
│   ├── lex-fridman/          # Lex Fridman Podcast
│   ├── aitime/               # AITIME 论道
│   ├── qingke/               # 青稞嘉年华
│   └── ...                   # 更多来源
└── articles/                 # 技术文章笔记
```

---

## ⚙️ 生成方式

```mermaid
graph LR
    A[YouTube/Bilibili 视频] --> B[yt-dlp 下载]
    B --> C{有字幕?}
    C -->|是| D[下载 SRT]
    C -->|否| E[Whisper large-v3]
    E --> D
    D --> F[Claude 智能整理]
    G[官方 Slides PDF] --> F
    F --> H[LaTeX 源文件]
    H --> I[XeLaTeX 编译]
    I --> J[📄 中文讲义 PDF]
```

---

## 🔗 课程资源链接

| 课程 | 官网 | YouTube | Slides |
|------|------|---------|--------|
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
- 🐛 发现讲义内容错误
- 💡 推荐新课程或演讲
- 📝 改进现有讲义质量

---

## 🙏 致谢

讲义生成工具链基于 [wdkns-skills](https://github.com/wdkns/wdkns-skills)（五道口纳什）改进，在此基础上增加了模块化重构、批量处理脚本、文章整理 skill 等扩展。

## 📜 License

本仓库的讲义、工具和脚本采用 [CC BY-NC-SA 4.0](LICENSE) 许可证。

本项目仅供学习和研究用途。仓库中引用的课程 slides、视频截图等素材的版权归原作者和所属机构所有。如果您是相关内容的版权持有者，认为本项目侵犯了您的权益，请通过 [Issues](../../issues) 联系我们，我们会在确认后第一时间移除相关内容。

<div align="center">

**⭐ 如果觉得有用，请给个 Star！**

</div>

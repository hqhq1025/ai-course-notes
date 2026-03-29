# AI Course Notes

CS / AI / LLM 相关公开课、演讲和访谈的中文讲义，基于视频字幕（Whisper large-v3 转录 / YouTube 自动字幕）、课程 slides 和公开资料整理生成。

**收录统计：220 份可编译 PDF 讲义**

| 类别 | 来源 | 数量 |
|------|------|------|
| Stanford 课程 | CS336 / CS224N / CS231N / CS224R / CS146S / CS25 | 121 |
| Berkeley 课程 | CS294 LLM Agents (F24/SP25/F25) | 35 |
| B站系列 | Modern Agent / LLM Architect / Agentic RL | 46 |
| 演讲与访谈 | AGI 峰会 / 青稞嘉年华 / 访谈 | 13 |
| 文章笔记 | 技术博客整理 | 5 |

---

## Stanford 课程

### CS336: Language Modeling from Scratch (Spring 2025)

从零构建语言模型：Tokenizer → Transformer → 训练 → 推理 → 评估 → 数据 → 对齐。17 讲。

📎 [课程官网](https://stanford-cs336.github.io/) · [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) · [Slides](https://github.com/stanford-cs336/spring2025-lectures) · 详见 [cs336/](cs336/)

### CS224R: Deep Reinforcement Learning (Spring 2025)

Chelsea Finn 主讲。Imitation Learning → Policy Gradient → Actor-Critic → RLHF → Meta-RL → 机器人。19 讲，每讲配官方 slides。

📎 [课程官网](https://cs224r.stanford.edu/) · [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL) · 详见 [cs224r/](cs224r/)

### CS25: Transformers United (V1–V5, 40讲)

Stanford 最受欢迎的 Seminar。嘉宾包括 **Geoffrey Hinton**、**Andrej Karpathy**、**Ashish Vaswani**（Attention 原作者）、**Noam Brown**、**Chris Olah**、**Jim Fan** 等。

📎 [课程官网](https://web.stanford.edu/class/cs25/) · [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) · 详见 [cs25/](cs25/)

### CS146S: The Modern Software Developer (Fall 2025)

AI 时代的软件开发方法论。10 周，每周邀请业界嘉宾（Claude Code 创作者、Warp CEO、Semgrep CEO 等）。基于 slides 生成。

📎 [课程官网](https://themodernsoftware.dev) · 详见 [cs146s/](cs146s/)

### CS224N: NLP with Deep Learning (Spring 2024)

17 讲，Chris Manning 主讲。

📎 [课程官网](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/) · [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) · 详见 [cs224n/](cs224n/)

### CS231N: Deep Learning for Computer Vision (Spring 2025)

18 讲。

📎 [课程官网](https://cs231n.stanford.edu/) · [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb) · 详见 [cs231n/](cs231n/)

---

## Berkeley 课程

### CS294/194-196: Large Language Model Agents (35讲)

Dawn Song 组织的 LLM Agents Seminar Series。三个学期，每讲邀请一位顶级嘉宾。

- **Fall 2024** (12讲): Denny Zhou, 姚顺雨, Percy Liang, Jim Fan, Ben Mann (Anthropic), Omar Khattab (DSPy)
- **Spring 2025 Advanced** (12讲): Jason Weston, Thomas Hubert (AlphaProof), Ruslan Salakhutdinov
- **Fall 2025 Agentic AI** (11讲): Noam Brown, Oriol Vinyals, James Zou, Yangqing Jia

📎 [课程官网](https://rdi.berkeley.edu/llm-agents/f24) · [YouTube F24](https://www.youtube.com/playlist?list=PLS01nW3RtgopsNLeM936V4TNSsvvVglLc) · [YouTube SP25](https://www.youtube.com/playlist?list=PLS01nW3RtgorL3AW8REU9nGkzhvtn6Egn) · [YouTube F25](https://www.youtube.com/playlist?list=PLS01nW3RtgoqGkm4UeqNeZLccW-OGc1fJ) · 详见 [talks/berkeley-llm-agents/](talks/berkeley-llm-agents/)

---

## B站系列课程（五道口纳什）

### Modern Agent (16讲)

LLM Agent 实战：ReAct、LangGraph、RAG、Visual Prompting、Codex 内部机制、Skills 系统、Subagents。

详见 [modern-agent/](modern-agent/)

### LLM Architect (10讲)

模型架构深度解析：MoE 参数量计算、RoPE 几何推导、Attention Head 模式、VLM 多模态设计、K2.5 论文串讲、KV-Cache 与推理优化。

详见 [llm-architect/](llm-architect/)

### Agentic RL (20讲)

强化学习 for LLM：PG → PPO → GRPO → DPO 完整链路，veRL 框架实现，AgentLoop 代码串讲，Multi-Turn Tool Use 训练。

详见 [agentic-rl/](agentic-rl/)

---

## 演讲与访谈

### 青稞 AI 嘉年华 (4场圆桌)

LLM/MLLM、Agentic、RL、Infra 四个专题的专家圆桌讨论。详见 [talks/qingke-*/](talks/)

### 访谈

| 嘉宾 | 主题 | PDF |
|------|------|-----|
| 杨植麟 | K2、Agentic LLM、艰难的泛化 | [PDF](interviews/yang-zhilin-k2/yang-zhilin-k2-notes.pdf) |
| 季逸超 | Manus 决定出售前最后的访谈 | [PDF](interviews/ji-yichao-manus/ji-yichao-manus-notes.pdf) |
| 谢赛宁 | 7 小时马拉松访谈 | [PDF](interviews/xie-saining-ami/xie-saining-ami-notes.pdf) |

### AGI 峰会演讲

张钹院士、杨植麟、林俊旸 (Qwen)、姚顺雨、阿里云圆桌、Greg Isenberg (Claude Code)。详见 [talks/](talks/)

---

## 生成方式

1. **素材获取**：YouTube/Bilibili 视频下载 + 官方 slides 搜集
2. **字幕转录**：Whisper large-v3（双 V100 GPU 多路并行）或 YouTube 自动字幕
3. **讲义生成**：基于字幕 + slides 生成 LaTeX 中文讲义，ctex + tcolorbox 模板
4. **编译**：XeLaTeX 两次编译生成 PDF

详细流程见 [CLAUDE.md](CLAUDE.md)。

# Lecture 07 Blueprint

## Lecture Identity

- Course: Agentic AI MOOC, Fall 2025
- Date: 2025-10-27
- Speaker: Sida Wang
- Topic: Predictable Noise and Patterns from Millions of Questions
- Video: `HV8pugcFVO0`
- Official deck: `slides/PredEval.pdf` (42 pages)

## Teaching Arc

1. 用 ImageNet 与小型生成式 benchmark 的样本量差异提出测量危机。
2. 检验“一个极难问题就足够有信息量”的反方直觉。
3. 读取逐题、逐模型 pass probability 热图，解释模型能力的不一致性。
4. 建立 super-population、paired comparison、total variance 和 standard error。
5. 用 bootstrap、sign test 与 Eval-Arena 把统计量转为可复用工具。
6. 解释 predictable noise、accuracy dependence、Beta probability pattern。
7. 说明过滤与重加权为何没有显著提高 signal，并给出更可靠的数据策略。
8. 用 signal-to-noise 和 SWE-bench 事故把统计问题连接到 agent evaluation 治理。

## Writing Decisions

- 42 页官方 slide 全部保留；空文字页 10--11 是热图证据，不是空白页。
- 官方 slide 是视觉主线，旧视频帧不再入文，避免重复同一课堂画面。
- 统计公式逐一定义符号，并把 paired 与 unpaired 的差异落到同题比较。
- “模型可独立重复采样”与“题目采样”分开讨论，防止把 seed variance 当成全部噪声。
- 课堂主张与讲义延伸分开：Sida 的失败结论保留为课堂证据，发布门禁和治理流程标为工程化推导。

## Acceptance Targets

- 42/42 official slides referenced.
- Strict coverage has no warnings.
- At least 260 prose characters per figure.
- Teacher-voice points appear in normal prose and marked boxes.
- Two XeLaTeX passes, `⭐⭐⭐`, clean hard-error log, signed visual QA.

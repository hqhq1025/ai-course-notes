# CS153 Lecture 06 Blueprint

Status: complete and accepted on 2026-08-11.

## Goal

把 Abdullah Alswaha 的访谈重写成一份关于“国家如何把 AI 基础设施投资转化为应用扩散、生产率与公共服务”的系统讲义。课堂跨度很大，必须用统一的因果链组织：硬件效率决定 token economics，token economics 影响应用扩散，数据、治理与 human-in-the-loop 决定 agent 是否能跨越 task-level demo，国家级平台最终要同时管理主权、韧性、公平性和长期技术债。

## Teaching Thesis

本讲不是一份沙特项目清单，而是三层系统设计课：

1. `device / memory / interconnect / cooling → useful compute per watt`；
2. `compute capacity → affordable inference → vertical applications → productivity`；
3. `data + workflow + governance + human accountability → deployable public-service agents`。

## Section Plan

1. 来源审计与 technocrat 视角：从互联网基础设施浪潮读取 AI signal。
2. 从硬件热潮到应用扩散：基础设施只有进入行业 workflow 才产生生产率。
3. 能效问题栈：semiconductor、memory wall、interconnect、cooling。
4. 数据中心 power budget 与 PUE：facility power 不等于 accelerator power。
5. 规划时钟冲突：电力/土地、facility、accelerator 与模型周期不一致。
6. 三类 AI frontier：generative、agentic、physical。
7. 医疗案例：drug formulation、clinical governance 与 robotic surgery。
8. 能源案例：pipeline/drilling agents、传感器数据与 human operator。
9. Model agnostic：开放/封闭、小/大模型由任务、证据与约束选择。
10. 基础设施的 no-regret 逻辑：training、inference、利用率与普惠 access。
11. 数字主权与 data embassy：位置、控制、管辖、恢复必须分开设计。
12. AI × space：communication、Earth observation、water 与 harsh environment。
13. In-memory / near-memory / photonics：减少 data movement，而非只追 FLOPS。
14. Robotics：healthcare、robotaxi、lunar rover 与经济结构变化。
15. Government agent：task、workflow、multi-agent、data layer、business model 与 human-in-the-loop。
16. 总结、国家级 AI infrastructure design exercise 与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有问题设置、读图说明和证据边界。
- 首次解释 technocrat、signal-to-noise ratio、von Neumann bottleneck、compound semiconductor、SRAM、DRAM、HBM、interconnect、PUE、model agnostic、training、inference、data sovereignty、data embassy、in-memory computing、near-memory computing、workflow-level agent 和 human-in-the-loop。
- 把现场数量写成“讲者估计/课堂口径”，不把计划值或比喻改写成审计事实。
- 明确“生成配方缩短”不等于临床审批消失，“全机器人手术”不等于 autonomous surgery。
- 区分课堂时点的 Groq/Aramco Digital 与之后的扩展公告，不倒写后续容量。
- 对数字主权、数据本地化和 data embassy 只讲架构维度，不从访谈推导具体法律结论。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

## Acceptance

- Final note: 27 pages, 16 figures, 43 teaching boxes, 7 teacher-voice markers.
- Strict coverage: zero errors and zero warnings.
- Quality: `⭐⭐⭐`, 1005 prose characters per figure.
- XeLaTeX: two clean passes with no overfull, underfull, undefined-reference, or LaTeX warnings.
- Canonical PDF QA: contact sheet and representative full-size pages reviewed; report signed.

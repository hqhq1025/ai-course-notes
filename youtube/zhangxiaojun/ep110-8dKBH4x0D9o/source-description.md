# Source Description

我们又来读论文啦！！！


今天我们要读的论文是最近几个星期内最值得品读的几篇技术报告，分别是：Kimi K2、ChatGPT Agent、Qwen3-Coder的技术报告，以及Manus的一篇技术博文。他们的相关性是，这几篇内容都和Agent有关系。


今天的嘉宾是俄亥俄州立大学（The Ohio State University）的在读博士郑博元，他的研究方向是Language Agent，他会带我们一起读上述技术报告和博文。


这是《商业访谈录》的“技术之美”系列，期待和你一起读论文，领略科技平权，感受技术之美——做你的赛博组会：）


00:02:00 给Agent下定义和分类


00:14:50 Kimi K2、ChatGPT Agent、Qwen3-Coder、Manus的技术路线对比


00:28:29 Agent Training 的关键环节：合成数据、强化学习、安全


00:30:57 第一篇技术报告：Kimi K2: Open Agentic Intelligence


github.com (https://github.com/MoonshotAI/Kimi-K2/blob/main/tech_report.pdf)


00:43:50 第二篇技术报告和访谈：Introducing ChatGPT agent: bridging research and action


openai.com (https://openai.com/zh-Hans-CN/index/introducing-chatgpt-agent/)


红杉访谈OpenAI：OpenAI Just Released ChatGPT Agent, Its Most Powerful Agent Yet


www.sequoiacap.com (https://www.sequoiacap.com/podcast/training-data-chatgpt-agent/)


01:53:38 第三篇技术报告：Qwen3-Coder: Agentic Coding in the World


qwenlm.github.io (https://qwenlm.github.io/blog/qwen3-coder/)


01:59:04 第四篇技术博文：AI代理的上下文工程：构建Manus的经验教训（作者：Yichao 'Peak' Ji）


manus.im (https://manus.im/zh-cn/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)


02:06:06 展望：也许会有一个新的范式


02:15:20 我感觉Agent是“我拓展的大脑”，我背后有一个“军团”（Family of Agents）


02:16:41 不同Bot的语言风格：DeepSeek嘴臭，元宝舔狗


智能体定义


Agent是一种能够与环境进行交互（interaction）的智能系统。


它具备两个基本能力：


感知能力（Perception）
能够观察环境的状态，包括获取外部信息、读取反馈信号、解析上下文等。


行动能力（Action）
能够在环境中执行动作，例如调用工具、生成输出、控制界面、修改变量等。


简言之，Agent = 感知 + 行动
在一个循环中不断执行“观察 → 决策 → 行动”的流程，以达成任务目标。


Agent 的定义与分类


1. Coding Agent（代码智能体）
代表产品：Cursor、Windsurf
特点：代码生成与编辑能力强，用户体验优秀
应用场景：代码补全、代码重构、多人协作编程


2. Search Agent（搜索型智能体）
特点：结合搜索引擎，自动完成信息检索和汇总
应用场景：市场调研、报告生成、竞争对手分析等
潜力：在企业级场景中有很强的应用价值


3. Tool-Use Agent（工具使用型智能体）
特点：能够调用多种外部工具完成复杂任务
应用重点：是目前 Agent 研究和落地的主要方向
举例：ReAct（推理 + 行动）类 Agent，通过 tool calling 执行任务


4. Computer Use Agent（电脑操作型智能体）
代表产品：OpenAI Operator、Claude 的 Computer Use
特点：模拟人类使用电脑，完成跨应用的复杂操作
应用场景：执行流程自动化、远程助理、办公代理


Agent 的技术路线对比


1. In-Context Learning（上下文学习）
特点：依赖强大的预训练模型，通过提示构造实现任务规划与执行
优势：无需微调，灵活性高
局限：泛化能力弱，rollout 长度有限，容易失控


2. End-to-End Training（端到端训练）
特点：将 Agent 的全部行为编码进模型权重
优势：推理稳定，可控性强
局限：训练成本高，环境构建复杂


Agent Training 的关键环节


1. Data Synthesis（数据合成）
方法：生成大量高质量的 trajectory（行动轨迹）
用途：训练 Agent 在任务中如何决策、调用工具、管理 memory（记忆）


2. Reinforcement Learning（强化学习）
条件：需要定义清晰的 task（任务）与 verifiable reward（可验证奖励）
挑战：任务难度与环境反馈设计直接影响 Agent 的行为质量


3. Safety（安全性）问题
风险：Agent 具备自主决策能力，容易误用工具、走偏轨迹
对策：加入 sandbox（沙盒）限制、行为约束机制、Human-in-the-loop（人类监控）


展望：也许会有一个新的范式


生成数据的核心会从 input-output 式的数据标注，转向构建 environment（环境）以及对应的 task-reward（任务-奖励）。比如 Scale AI 提出的 rubrics as reward（用评分标准作为奖励机制）


Agent 能不能实现自我提升（self-improve）？一方面，Agent 在和环境交互的过程中会不断获得新数据；那它能不能自己找到或构造 verifiable reward（可验证的奖励）？交互中积累的 experience（经验），能不能被更有效地利用起来？
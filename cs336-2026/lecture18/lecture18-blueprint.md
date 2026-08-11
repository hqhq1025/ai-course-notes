# Lecture 18 Blueprint — Dan Fu Guest Lecture

Narrative question: 当语言模型已经训练完成，怎样从真实 workload 与 SLA 出发，把“模型权重”变成低延迟、高吞吐、可持续演进的推理服务；又怎样反过来让系统约束启发 kernel 与模型架构创新？

1. **建立全栈地图**：从 request、scheduler、KV cache、prefill/decode、parallelism 到 token output，说明推理引擎不是一次 forward，而是持续运行的资源调度循环。
2. **从 workload 推导 SLA**：区分 TTFT、TBT/TPOT 与 throughput，解释 coding agent、batch processing、multi-turn chat 对系统的不同压力。
3. **调度与缓存是系统主线**：用 continuous batching、Radix Tree prefix sharing、prefill/decode disaggregation 和 GPU→CPU DRAM→SSD 层级说明“省计算”与“搬状态”的权衡。
4. **系统级优化与生产边界**：讨论 fault tolerance、million-token context、cache-aware prefill-decode disaggregation，以及 observability 为什么能发现单元测试漏掉的 kernel bug。
5. **Megakernel 把 GPU 当分布式系统**：从 launch bubble、tail effect 与 load latency 出发，解释 whole-model megakernel、fine-grained overlap、ThunderKittens abstraction 与性能收益。
6. **Parcae：从系统约束回到架构**：解释 looped model 的参数复用、训练不稳定、residual dynamical system、spectral radius、稳定参数化与 scaling laws。
7. **高价值问答与设计原则**：保留 megakernel 人力成本、hardware/model co-design、loop vs parameters、agentic workload、multi-GPU communication 等问答，并归纳可操作的设计检查表。

Teacher voice: 从 `transcript_timed.txt` 建立 `lecture18-teacher-voice-ledger.md`，把 workload、生产事故、megakernel、Parcae 与 Q&A 中的口头动机和 caveat 织入正文；讲义推导与课堂原话明确区分。

Transition out: 本讲作为课程收束，把训练、推理、kernel、硬件与架构统一到一个原则——优化对象必须是端到端 workload，而不是孤立的模型 FLOPs。

# Lecture 18 Teacher-Voice Ledger

Primary source: `transcript_timed.txt`. The lecture combines Dan Fu's systems talk, Parcae material, and an extended Q&A; rows preserve spoken motivations, production stories, caveats, and design heuristics rather than merely restating slide labels.

| Time interval | Spoken point | Why it matters | Where it appears in the note |
|---|---|---|---|
| `00:07:34--00:09:38` | A token request passes through scheduling, optional prefill/decode disaggregation, prefix/KV lookup, model execution, and detokenization; the AI-generated slides are only high-level accurate. | Establishes the full-stack map and the source-trust caveat. | Opening overview, `怎样阅读本讲的图`, and the inference-engine figure. |
| `00:10:15--00:13:10` | Serving goals depend on workload shape; TTFT, TBT/TPOT, and throughput answer different questions. | Prevents one aggregate tokens/s number from standing in for user experience and capacity. | `Workload 与 SLA`, `课堂提示：先画 workload histogram`. |
| `00:14:12--00:21:10` | Prefill and decode have different resource profiles; continuous batching, prefix reuse, and disaggregation respond to queue and state heterogeneity. | Connects request shape to scheduler and pool design. | `一次请求怎样变成连续输出的 token` and its four figures. |
| `00:22:03--00:25:33` | Rare NaNs, broken tool-call termination, and an off-by-one read of uninitialized memory become visible at enormous serving scale; output anomalies expose systems bugs. | Shows why observability must include token repetition, completion length, language distribution, and replayable requests. | `Production bug 为什么需要 observability`, `课堂提示：万亿 token 规模...`. |
| `00:25:33--00:29:54` | KV cache behaves like a memory hierarchy across GPU, CPU DRAM, and SSD; eviction and prefetch depend on future session reuse and recomputation cost. | Recasts inference state management as an operating-systems problem with expensive misses. | `KV cache：推理系统里的“内存层级”`, `课堂提示：最优淘汰需要知道未来`. |
| `00:35:03--00:41:32` | Independent kernels leave launch, load, dependency, and tail bubbles; a persistent whole-model megakernel schedules finer instructions and overlaps preparation with computation. | Explains that the optimization target is the full decode timeline, not one GEMM. | `Megakernel`, `课堂提示：Megakernel 的目标不是...`, performance caveat. |
| `00:42:45--00:54:13` | Recurrence decouples FLOPs from parameter count, but naive looping is unstable; residual dynamics and spectral radius motivate Parcae's constrained parameterization. | Separates the architectural knob from the stability mechanism that makes it trainable. | `Parcae`, `课堂提示：Looping 提供的是独立缩放旋钮`. |
| `00:54:13--00:59:30` | Recurrence enters compute-optimal scaling: the best loop count changes with data and FLOP budget, and fixed depth is not always optimal in the shown regime. | Turns “loop or not” into a budgeted scaling decision rather than a universal claim. | `Recurrence scaling laws` and the loop-vs-fixed-depth figures. |
| `01:00:46--01:03:25` | Post-hoc looping of pretrained layers has suggestive but unexplained results; fewer parameters can cross memory/communication thresholds and yield nonlinear inference benefits. | Preserves the Q&A's caution and capacity-threshold intuition. | First two dialogue boxes in `问答中的系统设计原则`. |
| `01:04:47--01:06:14` | Hardware/model co-design starts from memory capacity and KV headroom, then considers native quantization formats and software support. | Gives a concrete order for architecture decisions under a known deployment target. | `Hardware/model co-design 从 memory 开始`, its dialogue and `课堂提示`. |
| `01:07:56--01:09:59` | Agentic workloads should keep KV cache hot; one-pass batch processing values different attention and cache choices. | Demonstrates that workload can change the optimal model architecture, not just serving parameters. | `Agentic workload 把 hot KV 变成核心资产`, its dialogue and `课堂提示`. |
| `01:10:27--01:11:28` | Communication calls can be fused into a megakernel, but fusion does not remove collective latency; specialized layer/block kernels may be the practical path. | Sets a realistic boundary on whole-model megakernel claims. | `Megakernel 能否融合多 GPU 通信`, its dialogue and `课堂提示`. |

## Attribution Rule

- `课堂提示` marks points directly grounded in the timed transcript.
- Equations, external numeric verification, and engineering checklists remain note synthesis unless the ledger identifies a matching spoken source.

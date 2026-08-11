# Lecture 10 Teacher-Voice Ledger

Status: executable-source narration mapped on 2026-08-11.

Lecture 10 has no separate subtitle file. The official executable source contains extensive `text(...)` narration; the note attributes only directly supported motivations, caveats, transitions, observations, and recipes to the instructor.

| Source node | Spoken point | Why it matters | Where it appears in note |
|---|---|---|---|
| `landscape():64–97` | Training is a one-time cost, inference repeats; agents can generate unbounded internal tokens; tokens generated equal compute spent. | Establishes inference as a long-term systems budget. | `推理为什么重要` box `课堂提示：训练付一次，推理会重复付费` |
| `arithmetic_intensity_of_inference():178–218` | MLP intensity scales with `B*T`; prefill can make it large, while generation has `T=1` and unpredictable concurrency. | Explains why the same weights behave differently across stages. | MLP box `课堂提示：prefill 与 generation 的 MLP 只差 shape，不差权重` |
| `reduce_kv_cache_size():372–404` | GQA reduces KV cache by `N/K`; memory reduction produces speedup, but accuracy must be checked. | Connects structural change, bandwidth, capacity, and quality. | GQA box `课堂提示：GQA 的速度来自 N/K 倍 KV 缩减` |
| `quantization():480–486` | Large activation channels make the weights they touch more important; keep only 0.1–1% in higher precision. | Preserves the operational AWQ intuition. | AWQ box `课堂提示：AWQ 让 activation 决定哪些权重值得精度` |
| `main():32–41` + `model_pruning():491–499` | Define a faster architecture, remove expensive parts, then repair via distillation; “rip out” and “fix it up.” | Distinguishes architecture design from post-change quality repair. | Pruning box `老师强调：先 rip out，再 fix it up` |
| `speculative_sampling():508–550` | Checking candidate tokens is more parallel than generating them; modified rejection sampling gives exact target samples. | Separates lossless systems acceleration from approximation. | Speculative box `课堂提示：checking 比 generation 更容易并行` |
| `continuous_batching():556–573` | Inference requests form a ragged array; use iteration-level scheduling and selective batching for attention vs non-attention operators. | Explains the serving scheduler’s core decomposition. | Continuous batching box `课堂提示：动态流量先变成 ragged array，再拆算子 batching` |
| `paged_attention():579–607` | Preallocation causes internal/external fragmentation; paging, prefix sharing, copy-on-write, and fused block reads solve dynamic KV management. | Connects LLM serving to operating-system memory ideas. | PagedAttention box `课堂提示：PagedAttention 直接借用操作系统 paging` |

Editorial attribution rule:

- `课堂提示` / `老师强调` is reserved for the ledger rows above.
- `讲义提醒` marks extra workload-reporting, quality-frontier, and tail-latency guidance added by the note author.

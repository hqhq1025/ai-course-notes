# Lecture 06 Teacher-Voice Ledger

Status: executable-source narration mapped on 2026-08-11.

Lecture 06 has no separate subtitle file. Teacher voice comes from explanatory `text(...)` nodes in `lecture06-slides.py`; only directly supported motivations, caveats, heuristics, transitions, and observations are attributed to the instructor.

| Source node | Spoken point | Why it matters | Where it appears in note |
|---|---|---|---|
| `main():14–36` | Programming models provide correctness, hardware knowledge provides performance, benchmarking shows scaling, profiling shows what runs, and Triton encourages block-level thinking. | Establishes the full optimization loop. | `本讲主线` box `课堂提示：正确性与性能需要两套模型` |
| `review_of_gpus():58–78` | Threads are natural for elementwise work; softmax and matmul require communication, so a block shares memory and is scheduled on one SM. | Explains why the programming hierarchy exists. | `Programming model` box `老师强调：为什么非逐元素算子需要 thread block` |
| `review_of_gpus():92–137` | Register pressure lowers warp occupancy but low occupancy is not always bad; block waves can leave SMs idle when the tail is small. | Prevents optimizing one occupancy number blindly. | `Interaction...` box `课堂提示：occupancy 不是越高越好，tail 也要单独看` |
| `benchmarking_and_profiling():145–176` | Benchmark/profile, make changes, then measure again; benchmarking gives wall-clock and scaling, not attribution. | Turns optimization into an evidence loop. | `Benchmarking 与 Profiling` box `老师强调：成功 recipe 是测量闭环` |
| `profiling():206–234` | Small shapes can show nearly constant time before cubic scaling; dimensions select different kernels, and kernel names expose library, architecture, dtype, and tile shape. | Connects performance curves to concrete implementation choices. | `Profiler case matrix` box `课堂提示：先看 scaling，再读 kernel 名` |
| `naive_vs_builtin_vs_compiled_gelu():263–302` | Builtin and compiled GeLU are faster because they use one fused kernel instead of many HBM round trips; the compiled kernel is Triton. | Demonstrates evidence-first fusion analysis. | GeLU box `老师强调：快的是执行图，不是 Python 写法更短` |
| `triton_introduction():308–314` | CUDA specifies per-thread work; Triton specifies per-block work as load, operate, and write back. | Provides the core Triton mental model. | `Triton mental model` box `课堂提示：Triton 把思考单位从 thread 提升到 block` |
| `triton_row_sum_example():488–497` | If a row does not fit in one block, split it into tiles, accumulate partial sums, then reduce accumulators. | Shows how a capacity constraint changes the algorithm. | `Triton row sum` box `课堂提示：先问一行能否放进一个 block` |
| `triton_matmul_relu_example():539–587` | Naive matmul rereads values; tiling reuses A/B chunks in shared memory, and fusion applies activation before writing output to HBM. | Unifies tiling and fusion as data-movement reductions. | `Triton matmul + ReLU` box `课堂提示：fusion 的收益要用省掉的 HBM traffic 解释` |

Editorial attribution rule:

- `课堂提示` / `老师强调` is reserved for the rows above.
- `讲义提醒` marks additional invariants and tuning advice that are useful but not directly stated in executable narration.

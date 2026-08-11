# Lecture 18 Coverage Matrix

| Source cluster | Treatment | Status |
|---|---|---|
| video/transcript `00:07:34--00:09:38` | inference engine 全栈地图；明确 AI-generated slides 只作高层示意 | covered |
| `00-11-40-workload-sla.jpg` + transcript | workload shape、TTFT、TBT/TPOT、QPS/GPU 与 SLA 联动 | covered |
| `00-16-00-request-to-token.jpg` / `00-16-40-continuous-batching.jpg` | prefill/decode 资源属性与 continuous batching 调度 | covered |
| `00-18-30-radix-prefix-cache.jpg` / `00-20-30-prefill-decode-disaggregation.jpg` | prefix reuse、KV cache 与 prefill/decode 分离 | covered |
| `00-26-30-kv-cache-hierarchy.jpg` | GPU→CPU DRAM→SSD 的 offload/prefetch/eviction 机制 | covered |
| production bug stories | NaN、tool-call length shift、off-by-one Chinese-token bug 与 observability | covered |
| `00-31-20-context-parallelism.jpg` / `00-32-30-cache-aware-pd.jpg` | long-context、fault tolerance、CPD warm/cold routing | covered |
| `00-36-45-kernel-bubbles.jpg` / `00-38-20-megakernel-solution.jpg` | kernel launch、stragglers、whole-model fusion | covered |
| `00-39-40-fine-grained-overlap.jpg` / `00-40-45-thunderkittens.jpg` / `00-41-10-decoding-payoff.jpg` | instruction abstraction、shared-memory orchestration、fine-grained overlap、性能证据 | covered |
| `00-42-45-parcae-overview.jpg` / `00-44-30-why-loop.jpg` | looped model 动机、参数复用与 FLOPs/parameter 解耦 | covered |
| `00-46-00-loop-instability.jpg` / `00-48-00-residual-dynamics.jpg` | learning-rate sensitivity、loss spike 与 residual dynamical system | covered |
| `00-50-30-spectral-radius.jpg` / `00-51-45-parcae-constraints.jpg` / `00-52-15-stable-loss.jpg` | closed form、spectral radius、negative diagonal parameterization、稳定训练 | covered |
| `00-54-00-quality-table.jpg` / `00-55-00-classic-scaling.jpg` / `00-58-30-recurrence-scaling.jpg` / `00-59-00-loop-vs-fixed-depth.jpg` | 质量结果与 recurrence/data/parameter scaling laws | covered |
| Parcae paper / CPD official post / HazyResearch megakernel sources | 术语、公式、数字和工程背景交叉核验 | covered |
| Q&A `01:00:46--01:11:28` | pretrained looping、memory benefits、megakernel labor cost、hardware co-design、agentic workload、NCCL fusion | covered |
| final synthesis | full-stack innovation 的统一视角与工程检查表 | covered |

## Acceptance

- Teacher voice is traceable through `lecture18-teacher-voice-ledger.md`, with timestamped production stories, caveats, transition logic, and Q\&A design heuristics woven into the note as `课堂提示`.
- Strict coverage reports no warning; the quality script reports `⭐⭐⭐`.
- The note compiles cleanly in two XeLaTeX passes to a 30-page PDF.
- Canonical visual QA is signed after inspection of the full contact sheet and representative dense/end pages; no crop, overflow, orphan caption, malformed box title, or near-blank page was found.

# Lecture 09 Writing Blueprint

## Teaching thesis

The lecture is organized around one claim: production inference is a constrained control system, not a pile of isolated GPU tricks. Application semantics define workload and correctness; workload defines latency, throughput, model, engine, and hardware choices; observability and evals make optimization safe; only then should an engineer descend from architectural changes to host work and finally kernels.

## Planned structure

| Section | Question answered | Required evidence | Planned teaching treatment |
|---|---|---|---|
| 1. Why inference | Why is serving a first-class engineering discipline? | slides 002--004; captions 00:00:56--00:07:35 | Lifecycle/economics argument, cross-stack map, source boundary. |
| 2. Applications become workloads | How do product archetypes become measurable constraints? | slides 007, 009--012; captions 00:08:13--00:20:02 | Archetype table, SLO contract, QPS/TPQ/prefix/latency glossary, per-user objective table. |
| 3. Benchmark one replica | How do we measure the feasible latency-throughput region? | slides 013--015; live frame 00:22:07; captions 00:20:02--00:22:55 | Serial/burst/sweep algorithm, queueing formulas, tail-latency demo and warning. |
| 4. Choose model and engine | How do quality constraints and runtime architecture change deployment? | slides 017--020, 022--025; captions 00:23:00--00:39:45 | Efficiency/capability regimes, orchestrator hierarchy, inference-engine process graph, engine tradeoff table. |
| 5. Map workload to hardware | Why are prefill and decode different systems problems? | slides 027--031; captions 00:39:55--00:48:55 | Arithmetic intensity, roofline, HBM/SRAM/SM/Tensor-Core glossary, alternative-hardware caveats. |
| 6. Deploy under scarcity and failure | How do we keep bursty GPU services fast and reliable? | slides 033--040, 043--046; captions 00:49:05--00:56:55 | Network/utilization definitions, reliability table, allocation-control sequence, Cloud Buffer, container cache, checkpoint/restore. |
| 7. Debug with observability and evals | How can correctness and performance failures be reconstructed? | slides 048--052; captions 00:57:08--01:05:45 | Three-layer bug taxonomy, token-ID logging, eval lifecycle, minimum metrics and queue diagnosis. |
| 8. Optimize in the right order | Which changes dominate and why? | slides 054--067; captions 01:06:45--01:19:49 | Optimization funnel, speculative decoding math, quantization ladder, CUDA Graph, host profiling, kernel decision gate. |
| 9. Future inference engineering | What changes when correctness is application-specific and agents write systems code? | slides 069, 071; captions 01:19:56--01:22:19; VibeServe arXiv 2605.06068 | Lossy optimization warning, heterogeneous accelerators, agent correctness system, bespoke-engine thesis. |
| 10. Summary and extension | What reusable workflow should the reader carry into practice? | all sections | Ten-step deployment checklist, failure modes, lecture-date source snapshot, primary readings. |

## Formula and code plan

1. Workload tuple and offered load: `W=(QPS,L_in,L_out,r_prefix,SLO)` and Little's-law intuition.
2. TTFT/TPOT/TTLT decomposition with tool-call extension.
3. Per-replica capacity and replica-count sizing.
4. Latency-throughput endpoints and sweep pseudocode.
5. Tail-amplification probability across many emitted tokens.
6. Arithmetic intensity and roofline performance bound.
7. Transformer decode byte/FLOP intuition and KV-cache memory.
8. Availability/failure probability caveat for fleets.
9. Cold-start critical-path decomposition.
10. Speculative decoding acceptance and expected speedup model.
11. Quantized-weight byte and bandwidth model.
12. CUDA Graph launch-overhead model.
13. Optimization decision pseudocode and structured logging examples.

## Dense terminology blocks

- SLO/SLA, QPS/RPS, TPQ, TTFT, TPOT/ITL, TTLT, prefix reuse.
- Replica, scheduler, tokenizer/detokenizer, continuous batching, PagedAttention/RadixAttention.
- DRAM, SRAM/shared memory, HBM, SM, Tensor Core, NVLink, InfiniBand, arithmetic intensity, roofline.
- Allocation utilization, kernel utilization, SM utilization, bandwidth/FLOP utilization.
- Speculative decoding, N-gram, MTP, EAGLE, DFlash, drafter, verifier, acceptance rate.
- BF16, FP8, FP4, weight quantization, activation quantization, KV-cache quantization.
- CUDA Graph, CUPTI, Nsight Systems, Nsight Compute, py-spy, PTX, SASS.

## Evidence boundaries

- Provider prices and intelligence indices are market snapshots, not controlled scientific comparisons.
- The H100 failure-rate slide summarizes one production context; it is not a universal hardware warranty statistic.
- Claimed speedups are workload-, model-, hardware-, batch-, and implementation-dependent.
- Quantization and lossy optimization require application evals; no numeric format is universally safe.
- Deck page 072 is not treated as classroom content because the recording ends after page 071.
- Future hardware and agentic-engine claims are forecasts, not deployed guarantees.

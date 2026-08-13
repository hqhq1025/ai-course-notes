# Lecture 09 Coverage Matrix

| Source node | Evidence | Required treatment |
|---|---|---|
| Inference motivation | slides 002--004; captions 00:00:56--00:07:35 | Lifecycle economics, post-training inference, cross-stack scope, experience boundary. |
| Application archetypes | slide 007; captions 00:08:13--00:11:12 | Chatbot+, background agent, data processor; consumer, burstiness, latency, and objective. |
| Workload/SLO contract | slides 009--010; captions 00:11:17--00:13:15 | Stakeholder handoff, workload tuple, concrete discovery checklist. |
| Metric glossary | slide 011; captions 00:13:20--00:19:10 | First-use definitions for QPS, TPQ, prefix reuse, TTFT, TPOT/ITL, TTLT, replica. |
| Figures of merit | slide 012; captions 00:19:10--00:20:02 | Tokens/s/user, TTLT, megatokens per dollar and why objectives differ. |
| Replica benchmark | slides 013--014; captions 00:20:02--00:21:30 | Serial minimum-latency test, all-at-once maximum-throughput test, rate sweep. |
| Tail-latency intuition | slide 015; live frame 00:22:07; captions 00:21:30--00:22:55 | p50/p95/p99, token-level stutter, compounding probability, non-universal demo warning. |
| Model regimes | slides 017--020; captions 00:23:00--00:33:12 | Efficiency-bound/capability-bound comparison, open/proprietary choices, orchestrator/subagent hierarchy, cost-capability plot caveat. |
| Engine architecture | slide 022; captions 00:33:20--00:35:10 | RPC, tokenizer, detokenizer, scheduler, model workers, CPU/GPU boundary. |
| Engine landscape | slides 023--025; captions 00:35:10--00:39:45 | TRT-LLM, vLLM, SGLang tradeoffs; simple implementations and source-study method. |
| Prefill/decode split | slide 027; captions 00:39:55--00:42:45 | Compute-heavy versus bandwidth-heavy intuition and continuous batching relationship. |
| Arithmetic intensity | slide 028 | Formula, roofline, axes, ridge point, limitations. |
| GPU hierarchy | slides 029--030; captions 00:42:45--00:45:25 | HBM/SRAM/shared memory/SM/Tensor Core/interconnect first-use glossary. |
| Alternative hardware | slide 031; captions 00:45:25--00:48:55 | CPU/TPU/ASIC tradeoffs and software ecosystem constraint. |
| Deployment constraints | slide 033; captions 00:49:05--00:50:40 | Scarcity, network latency, local versus served inference, four utilization layers. |
| Reliability | slides 034--035; captions 00:50:40--00:51:55 | Failure table reading guide, fleet-health monitoring, inference versus training fault model. |
| Bursty allocation | slides 036--040; captions 00:51:55--00:54:00 | Demand trace, fixed/slow/fast allocation, startup-latency decomposition. |
| Cloud Buffer | slides 043--044; captions 00:54:00--00:55:00 | Warm-capacity pool, control loop, queueing and allocation boundary. |
| Container cache | slide 045; captions 00:55:00--00:55:55 | Lazy/eager/content-addressed layers and repeated-start benefit. |
| Checkpoint/restore | slide 046; captions 00:55:55--00:56:55 | Process-as-data intuition, CRIU/CUDA state, socket caveat. |
| Bug taxonomy | slide 048; captions 00:57:08--00:59:24 | Application/model/performance bugs; train-serve skew; tokenizer/chat-template failures. |
| Observability | slide 049; captions 00:59:24--01:01:27 | Logs, token IDs, traces, user feedback, metric supersets. |
| Evals | slide 050; captions 01:01:27--01:02:55 | Evals as tests/observability, model-agnostic assets, notebook-first start. |
| Metrics dashboard | slides 051--052; captions 01:02:55--01:05:45 | RPS/QPS, queueing, prefill/decode, per-replica percentiles, hardware telemetry. |
| Optimization hierarchy | slide 054; captions 01:06:45--01:07:45 | Big architectural changes before host work before kernels. |
| Speculation mechanism | slides 055--056; captions 01:07:45--01:10:50 | Draft/verify/reject loop, lossless condition, acceptance and batch pressure. |
| Speculation taxonomy | slide 057; captions 01:10:50--01:13:20 | N-gram, MTP, EAGLE, DFlash comparison and source snapshot. |
| Quantization | slide 058; captions 01:13:20--01:16:10 | Byte/FLOP effects, BF16/FP8/FP4, long-context and KV-cache caveats, eval gate. |
| Host overhead | slides 059--064; captions 01:16:10--01:18:42 | GPU starvation, CUDA Graph, system timeline, temperature, py-spy case study. |
| Kernel optimization | slides 065--067; captions 01:18:42--01:19:49 | Library reuse, Nsight Compute counters, PTX/SASS mapping, whiteboard-first reasoning. |
| Future systems | slide 069; captions 01:19:56--01:20:44 | Lossy optimization, megakernels, heterogeneous prefill/decode hardware, forecast boundary. |
| Agentic engineering | slide 071; captions 01:20:50--01:22:19; arXiv 2605.06068 | Correctness system, permissions/tools/metrics, VibeServe bespoke-engine hypothesis. |
| Optional visuals | slides 001, 005--006, 008, 016, 021, 026, 032, 041--042, 047, 053, 068, 070, 072--073 | Explicit omission reasons retained in selection table. |
| Full recording audit | 990 five-second frames; 17 contact sheets | Record one deck-external teaching demo and no missing whiteboard/live-coding visual. |

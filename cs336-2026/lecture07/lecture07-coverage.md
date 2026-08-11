# Lecture 07 Coverage Matrix

Status: complete after source-first rewrite and executable-narration verification on 2026-08-11.

Source: `lecture07-slides.py`, checked against the official Stanford CS336 raw source; only whitespace differs. The note treats the executable source clusters as the coverage spine rather than patching the old outline.

Verification evidence:

- `tools/scripts/check_quality.sh cs336-2026/lecture07/lecture07-notes.tex` reports `29p 12s 52b 15f 1160c/f ⭐⭐⭐`.
- Strict coverage reports `figs=15 readfig=19 boxes=52 term_digest=8 teacher_voice=11 formulas=7 code=7 summaries=11 prose_chars=17413` with no errors or warnings.
- Double-pass XeLaTeX succeeds; the log has no layout overflow, missing-character, undefined-control-sequence, or rerun warnings.
- Visual PDF QA was rendered and checked in `qa/lecture07-notes/`.
- `lecture07-teacher-voice-ledger.md` traces 12 executable narration clusters to the note; source-backed `课堂提示` and editorial `讲义提醒` are explicitly separated.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| Part 1 distributed communication | source cluster | yes | 分布式通信基本语言 | ranks/world size + collectives table + diagrams | complete |
| Collective operations | source cluster | yes | Collectives | broadcast/scatter/gather/reduce/all-gather/reduce-scatter/all-reduce/all-to-all | complete |
| Hardware and NCCL | source cluster | yes | Hardware/NCCL | topology, RDMA, InfiniBand/RoCE, NCCL explanation | complete |
| torch.distributed | source cluster | yes | PyTorch distributed | init/process group/rank semantics | complete |
| Benchmarking | source cluster | yes | Communication benchmark | bandwidth/latency methodology | complete |
| Data parallelism | figure | yes | Distributed training | figure + explanation + gradient sync | complete |
| Tensor parallelism | figure | yes | Distributed training | figure + row/column split explanation | complete |
| Pipeline parallelism | figure | yes | Distributed training | figure + bubble/microbatch explanation | complete |
| PDF visual QA | QA | yes | qa/lecture07-notes | rendered pages + contact sheet | complete |

## Acceptance

- Executable source coverage remains complete; no manifest item is satisfied only by an invisible comment marker.
- Teacher voice preserves locality motivation, collective use cases, topology reasoning, benchmark protocol, the data-parallel invariant, TP/PP boundaries, JAX/PyTorch scope, and the recompute-memory-communication tradeoff.
- Strict coverage has no warning, the quality grade is `⭐⭐⭐`, and the 29-page PDF compiles cleanly in two XeLaTeX passes.
- Canonical QA is signed after the sparse final page was replaced with a substantive next-lecture ledger and self-test.

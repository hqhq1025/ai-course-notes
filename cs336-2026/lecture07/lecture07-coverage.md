# Lecture 07 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source: `lecture07-slides.py`, checked against the official Stanford CS336 raw source; only whitespace differs. The note treats the executable source clusters as the coverage spine rather than patching the old outline.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture07-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture07/lecture07-notes.tex` reports `26p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture07/lecture07-notes.tex --manifest cs336-2026/lecture07/lecture07-manifest.md` reports `figs=15 readfig=18 boxes=42 term_digest=8 formulas=7 code=7 summaries=11` with no hard errors.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture07-notes/`.

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

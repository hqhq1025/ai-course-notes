# Lecture 08 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source deck: `lecture08-slides.pdf`, 73 pages. The rewritten note includes every source slide image `slide-001.jpg` through `slide-073.jpg`, plus the cover reuse, for 74 `\includegraphics` calls total.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture08-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture08/lecture08-notes.tex` reports `53p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture08/lecture08-notes.tex --manifest cs336-2026/lecture08/lecture08-manifest.md` reports `figs=74 readfig=59 boxes=76 term_digest=4 formulas=3 code=0 summaries=2` with no hard errors.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture08-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| slides 001-003 | title/goals/organization | yes | 本讲主线 | slide-complete figures, teaching-goal explanation, terms map | complete |
| slides 004-013 | networking basics | yes | Part 1 | compute/memory limits, collectives, topology, Part 1 recap | complete |
| slides 014-031 | data parallel and ZeRO/FSDP | yes | Part 2 | DDP, memory ledger, ZeRO 1/2/3, FSDP lifecycle | complete |
| slides 032-038 | pipeline parallel | yes | Part 2 | layer-wise, bubbles, microbatches, zero-bubble scheduling | complete |
| slides 039-049 | tensor and sequence parallel | yes | Part 2 | width sharding, row/column TP, activation memory, SP | complete |
| slides 050-056 | expert/context parallel and summary table | yes | Part 2 | EP, CP, recap table, model-vs-tensor perspective | complete |
| slides 057-073 | 3D/4D parallelism and recent models | yes | Part 3 | rules of thumb, Megatron/Narayanan, model case studies, final recap | complete |
| PDF visual QA | QA | yes | `qa/lecture08-notes/` | rendered pages + contact sheet + checked report | complete |

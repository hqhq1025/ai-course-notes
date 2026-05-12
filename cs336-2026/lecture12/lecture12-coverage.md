# Lecture 12 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source: `lecture12-slides.py`, official executable lecture source. The rewritten note follows source clusters and localizes all image assets.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture12-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture12/lecture12-notes.tex` reports `29p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture12/lecture12-notes.tex --manifest cs336-2026/lecture12/lecture12-manifest.md` reports `figs=44 readfig=25 boxes=40 term_digest=4 formulas=2 code=0 summaries=6` with no hard errors or warnings.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture12-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| main and what-is-good | source cluster | yes | Lecture 12 / What is good | construct-to-metric framing, leaderboards/cost/preference/usage | complete |
| perplexity | source cluster | yes | Perplexity | formula, GPT-2 OOD, LAMBADA, HellaSwag, zero-shot clarification | complete |
| exam benchmarks | source cluster | yes | Exam benchmarks | MMLU, MMLU-Pro, GPQA, HLE examples/pipeline/results | complete |
| chat benchmarks | source cluster | yes | Chat benchmarks | Arena, ELO, AlpacaEval, WildBench, judge-bias caveats | complete |
| agentic benchmarks | source cluster | yes | Agentic benchmarks | SWE-Bench, TerminalBench, CyBench, MLE-Bench, scaffolds | complete |
| pure reasoning | source cluster | yes | Pure reasoning benchmarks | ARC-AGI 1/2/3 and reasoning model discussion | complete |
| safety benchmarks | source cluster | yes | Safety benchmarks | crash-test analogy, AIR-Bench, GCG, contextual safety | complete |
| realism/validity | source cluster | yes | Realism / Validity | GDPVal, MedHELM, Clio, contamination, dataset quality | complete |
| how to think | source cluster | yes | How to think about evaluation | methods/models/agents distinction and rules | complete |
| PDF visual QA | QA | yes | `qa/lecture12-notes/` | rendered pages + contact sheet + checked report | complete |

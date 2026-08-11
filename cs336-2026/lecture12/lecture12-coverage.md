# Lecture 12 Coverage Matrix

Status: second-round executable-source and teacher-voice verification completed on 2026-08-11.

Source: `lecture12-slides.py`, official executable lecture source. The note follows source clusters, localizes all image assets, and maps directly supported narration in `lecture12-teacher-voice-ledger.md`. Additional benchmark-audit synthesis is labeled `讲义提醒`.

Verification evidence:

- Strict coverage reports `figs=44 readfig=27 boxes=46 term_digest=4 teacher_voice=14 formulas=2 code=0 summaries=7 prose_chars=11784`, with no warnings or hard errors.
- Quality check reports 32 pages, 11 sections, 46 teaching boxes, 44 source figures, `⭐⭐⭐`.
- Double-pass XeLaTeX succeeds; final logs have no overfull boxes, LaTeX errors, undefined control sequences, missing characters, emergency stops, or fatal errors.
- Visual QA inspected the complete 32-page contact sheet and full-size pages 30--32; all dense leaderboards, benchmark examples, validity figures, and the new purpose/object subsections are readable and uncropped.

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
| teacher voice | spoken/source text | yes | throughout | `课堂提示` / `老师强调` / `讲义提醒` / `实践经验` markers integrated into prose | complete |
| PDF visual QA | QA | yes | `qa/lecture12-notes/` | rendered pages + contact sheet + checked report | complete |

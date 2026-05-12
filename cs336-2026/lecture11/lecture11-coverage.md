# Lecture 11 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source deck: `lecture11-slides.pdf`, 58 pages. The rewritten note includes every source slide image `slide-001.jpg` through `slide-058.jpg`, plus the cover reuse, for 59 `\includegraphics` calls total.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture11-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture11/lecture11-notes.tex` reports `43p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture11/lecture11-notes.tex --manifest cs336-2026/lecture11/lecture11-manifest.md` reports `figs=59 readfig=53 boxes=60 term_digest=5 formulas=1 code=0 summaries=4` with no hard errors.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture11-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| slides 001-005 | motivation and setup | yes | 本讲主线 | slide-complete figures, real-scaling framing | complete |
| slides 006-018 | MiniCPM | yes | MiniCPM | muP, LR/batch scaling, WSD, Chinchilla methods | complete |
| slides 019-030 | DeepSeek and recent models | yes | DeepSeek 与近期 recipes | LR/batch scaling, IsoFLOP, Qwen/Kimi/Hunyuan/LLaMA/MiniMax | complete |
| slides 031-043 | optimizer scaling and Muon | yes | Optimizer scaling | StepFun, LR/batch variables, robustness, Muon | complete |
| slides 044-057 | muP in depth | yes | muP in depth | A1/A2 derivations, modern LM caveats, failures | complete |
| slide 058 | recap | yes | 总结与延伸 | final synthesis and takeaways | complete |
| PDF visual QA | QA | yes | `qa/lecture11-notes/` | rendered pages + contact sheet + checked report | complete |

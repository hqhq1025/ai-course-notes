# Lecture 04 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source deck: `lecture04-slides.pdf`, 60 pages. The rewritten note includes every source slide image `slide-000.jpg` through `slide-059.jpg`, plus the course cover, for 61 figures total.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture04-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture04/lecture04-notes.tex` reports `41p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture04/lecture04-notes.tex --manifest cs336-2026/lecture04/lecture04-manifest.md` reports `figs=61 readfig=105 boxes=42 term_digest=3 formulas=2 code=0 summaries=10` with no hard errors.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture04-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| slides 001-013 | attention alternatives | yes | Attention alternatives | slide-complete figures, linear attention formulas, DSA/GDN glossary | complete |
| slides 014-024 | MoE motivation | yes | Why MoE | slide-complete figures, MoE definition, FLOPs vs params explanation | complete |
| slides 025-035 | routing variants | yes | Routing | top-k routing formula, token-choice/expert-choice glossary, evidence slides interpreted | complete |
| slides 036-043 | MoE training and balancing | yes | Training MoEs | load balancing losses, stochastic approximations, DeepSeek bias, z-loss explanation | complete |
| slides 044-047 | MoE systems side | yes | Systems side | expert parallelism, all-to-all, communication compression, stochasticity | complete |
| slides 048-053 | stability, fine-tuning, upcycling | yes | Stability and adaptation | router z-loss, fine-tuning caveats, upcycling glossary | complete |
| slides 054-059 | DeepSeek MoE v1-v3, MLA, MTP | yes | DeepSeek MoE case study | slide-complete, MLA/MTP first-use glossary, architecture timeline | complete |
| slide 060 | recap | yes | Summary | final synthesis | complete |
| PDF visual QA | QA | yes | `qa/lecture04-notes/` | rendered pages + contact sheet + report | complete |

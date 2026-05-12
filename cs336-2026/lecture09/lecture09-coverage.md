# Lecture 09 Coverage Matrix

Status: complete after source-first rewrite and verification on 2026-05-12.

Source deck: `lecture09-slides.pdf`, 57 pages. The rewritten note includes every source slide image `slide-001.jpg` through `slide-057.jpg`, plus the cover reuse, for 58 `\includegraphics` calls total.

Verification evidence:

- `xelatex -interaction=nonstopmode -halt-on-error lecture09-notes.tex` run twice successfully.
- `tools/scripts/check_quality.sh cs336-2026/lecture09/lecture09-notes.tex` reports `42p  ⭐⭐⭐`.
- `python3 tools/scripts/check_note_coverage.py cs336-2026/lecture09/lecture09-notes.tex --manifest cs336-2026/lecture09/lecture09-manifest.md` reports `figs=58 readfig=53 boxes=59 term_digest=3 formulas=5 code=3 summaries=5` with no hard errors.
- LaTeX log scan reports no `LaTeX Error`, `Undefined control sequence`, rerun warning, `Overfull`, or `Missing character`.
- Visual PDF QA was rendered and checked in `qa/lecture09-notes/`.

| Source node | Type | Required? | Note section | Treatment | Status |
|---|---|---|---|---|---|
| slides 001-004 | opening and motivation | yes | 本讲问题 | slide-complete figures, scenario interpretation, scaling-law definition | complete |
| slides 005-011 | history and background | yes | Part 1 | sample complexity, early data scaling, Hestness work | complete |
| slides 012-027 | data scaling behaviors | yes | Part 2 | power law formulas, mean estimation, intrinsic dimension, composition/repetition | complete |
| slides 028-042 | model engineering scaling | yes | Scaling laws for model engineering | architecture, optimizer, depth/width, batch, muP, downstream caveats | complete |
| slides 043-057 | joint scaling and compute allocation | yes | Joint data-model scaling | Kaplan/Chinchilla, IsoFLOPS, joint fits, overtraining, final recap | complete |
| PDF visual QA | QA | yes | `qa/lecture09-notes/` | rendered pages + contact sheet + checked report | complete |

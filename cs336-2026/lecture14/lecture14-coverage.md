# Lecture 14 Coverage Matrix

Status: complete after second-round source-complete rewrite and verification on 2026-08-11.

Verification evidence:

- Strict coverage reports `figs=18 readfig=13 boxes=33 term_digest=1 teacher_voice=6 formulas=8 code=1 summaries=7 prose_chars=13479` with no errors or warnings.
- `tools/scripts/check_quality.sh cs336-2026/lecture14/lecture14-notes.tex` reports `25p 8s 33b 18f 748c/f ⭐⭐⭐`.
- `lecture14-teacher-voice-ledger.md` records eleven timestamped/source-aligned teaching points and separates source-backed `课堂提示` from note-authored `讲义提醒`.
- Double-pass XeLaTeX succeeds with no layout overflow, missing-character, undefined-control-sequence, or rerun warnings.
- Canonical visual QA was rendered to `qa/lecture14-notes/`; the contact sheet and enlarged pages 6, 11--16, and 25 were manually inspected.

| Source cluster | Treatment | Status |
|---|---|---|
| transformation / `dclm-wet.png` / `finepdfs-pdf-structure.png` | HTML/PDF/code 转换的损失、PDF object-to-layout 关系与质量边界 | covered |
| filtering / `raw-target-schema.png` | target-vs-raw 框架、score、threshold、sampling | covered |
| language/quality/toxicity cases | fastText、KenLM、GPT-3/LLaMA、phi-1、Dolma | covered |
| `data-filtering-scale.png` | 过滤器规模、推理成本与收益的权衡 | covered |
| exact/fuzzy dedup / `near-duplicate-examples.png` | hash、真实 near-duplicate、Jaccard、复杂度 | covered |
| LSH / `lsh-collision-probability.png` / `lsh-band-thresholds.png` | MinHash、banding、S 曲线、候选预算与阈值校准 | covered |
| data mixing / `marin-token-viewer.png` / `the-pile.png` | unique tokens、weights、epochs、effective size | covered |
| mixing methods / `data-mixing-methods.png` / `regmix.png` | proxy runs、回归优化、epoching 与外推风险 | covered |
| post-training synthetic data | OpenThoughts、SWE-smith、SWE-rebench、SWE-zero | covered |
| transcript teaching voice | timestamped transformation、dedup、epoching、teacher selection、execution caveats | covered |
| final audit loop | 可复现数据卡与 provenance checklist | covered |

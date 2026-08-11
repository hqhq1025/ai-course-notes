# Lecture 05 Coverage Matrix

Status: second-round slide-complete rewrite completed and visually verified on 2026-08-11.

Source deck: `lecture05-slides.pdf`, 55 pages. All 55 pages now appear in source order; the first slide is reused as the note cover and the remaining 54 appear in the body.

Verification evidence:

- Strict coverage: `figs=55 readfig=67 boxes=52 term_digest=2 teacher_voice=0 formulas=2 code=0 summaries=7 prose_chars=15636`, with no warnings or hard errors.
- Quality check: 40 pages, 55 figures, 284 prose characters per figure, `⭐⭐⭐`.
- Double-pass XeLaTeX succeeds with no overfull box, missing character, LaTeX error, fatal error, or undefined control sequence.
- Visual QA: full contact sheet and representative full-size pages reviewed; checklist signed.

| Source cluster | Required? | Note section | Treatment | Status |
|---|---|---|---|---|
| slides 001--004 | yes | 本讲问题 / GPU 主线 | Title/cover, goals, source provenance and three-part lecture organization retained and explained. | complete |
| slides 005--019 | yes | GPU 为什么适合深度学习 | Every screenshot included; compute scaling, GPU hierarchy, SIMT, tensor cores and memory-wall recap explained. | complete |
| slides 020--029 | yes | Roofline 与低精度 | Every screenshot included; matmul irregularity, roofline, optimization map, FP8/MXFP8/MXFP4 and numerical tradeoffs explained. | complete |
| slides 030--035 | yes | Operator fusion 与 recomputation | Every screenshot included; factory/memory analogy, fusion and compute-memory tradeoffs explained. | complete |
| slides 036--048 | yes | Coalescing、tiling 与矩阵性能异常 | Every screenshot included; burst/coalesced access, shared-memory tiling, alignment and wave quantization explained. | complete |
| slides 049--054 | yes | FlashAttention | Every screenshot included; optimization recap, IO-aware premise, KQV tiling, online softmax and forward pass explained. | complete |
| slide 055 | yes | 总结 | Final recap screenshot included and connected to a reproducible performance protocol. | complete |
| teacher voice | not available | whole note | No transcript, subtitles, speaker notes or executable narration nodes exist in the lecture directory; no classroom voice is fabricated. | not applicable |
| PDF visual QA | yes | `qa/lecture05-notes/` | 40-page contact sheet and representative full-size pages inspected; checklist signed. | complete |

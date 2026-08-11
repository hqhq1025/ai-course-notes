# Lecture 04 Coverage Matrix

Status: second-round slide-complete rewrite completed and visually verified on 2026-08-11.

Source deck: `lecture04-slides.pdf`, 60 pages. The note includes all 59 teaching-bearing pages in source order. `slide-000.jpg` is a pure title page duplicated by the note cover and is the only intentional omission.

Verification evidence:

- Strict coverage: `figs=60 readfig=97 boxes=49 term_digest=3 teacher_voice=0 formulas=2 code=0 summaries=10 prose_chars=15691`, with no warnings or hard errors.
- Quality check: 43 pages, 60 figures, 261 prose characters per figure, `⭐⭐⭐`.
- Double-pass XeLaTeX succeeds with no overfull box, LaTeX error, fatal error, or undefined control sequence.
- Visual QA: full contact sheet plus representative full-size pages reviewed; the initially sparse final page was replaced with an annotated reading table and counterfactual exercise, then the checklist was signed.

| Source cluster | Required? | Note section | Treatment | Status |
|---|---|---|---|---|
| slide 000 | no | note cover | Pure title page duplicated by the note cover; intentionally omitted. | optional |
| slides 001--013 | yes | 本讲主线 / Attention alternatives | Every screenshot included; cost motivation, linear/recurrent/hybrid attention and DSA explained. | complete |
| slides 014--023 | yes | MoE 为什么流行 | Every screenshot included; active-vs-total parameters, training/quality evidence and four-account resource ledger explained. | complete |
| slides 024--034 | yes | Routing | Every screenshot included; token/expert choice, classic top-k, recent routing variants and ablations explained. | complete |
| slides 035--042 | yes | Training MoEs | Every screenshot included; sparsity, REINFORCE/stochastic approximation, load balancing and auxiliary-free methods explained. | complete |
| slides 043--046 | yes | MoE systems side | Every screenshot included; expert parallelism, all-to-all pipeline, communication compression and routing stochasticity explained. | complete |
| slides 047--052 | yes | 稳定性、fine-tuning 与 upcycling | Every screenshot included; z-loss, fine-tuning behavior and dense-to-MoE cases explained. | complete |
| slides 053--058 | yes | DeepSeek MoE case study | Every screenshot included; v2/v3, MLA latent reconstruction and MTP combination logic explained. | complete |
| slide 059 | yes | 总结 | Final summary screenshot included and connected to a resource acceptance table. | complete |
| teacher voice | not available | whole note | No transcript, subtitles, speaker notes or executable narration nodes exist in the lecture directory; no classroom voice is fabricated. | not applicable |
| PDF visual QA | yes | `qa/lecture04-notes/` | 43-page contact sheet and representative full-size pages inspected; final page expanded and checklist signed. | complete |

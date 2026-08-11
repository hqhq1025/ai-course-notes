# Lecture 03 Coverage Matrix

Status: second-round slide-complete rewrite completed and visually verified on 2026-08-11.

Source deck: `lecture03-slides.pdf`, 67 pages. The note includes all 66 teaching-bearing pages in source order. `slide-000.jpg` is a pure title page duplicated by the note cover and is the only intentional omission.

Verification evidence:

- Strict coverage: `figs=67 readfig=28 boxes=51 term_digest=5 teacher_voice=0 formulas=5 summaries=10 prose_chars=17440`, with no warnings or hard errors.
- Quality check: 48 pages, 67 figures, 260 prose characters per figure, `⭐⭐⭐`.
- Double-pass XeLaTeX succeeds with no overfull box, LaTeX error, fatal error, or undefined control sequence.
- Visual QA: `qa/lecture03-notes/contact.png` plus representative full-size pages reviewed; checklist signed.

| Source cluster | Required? | Note section | Treatment | Status |
|---|---|---|---|---|
| slide 000 | no | note cover | Pure course title duplicated by the note cover; intentionally omitted. | optional |
| slides 001--008 | yes | 本讲目标 | Every screenshot included; original/modern baselines, release survey and coverage map explained. | complete |
| slides 009--018 | yes | Norm 与 residual stream | Every screenshot included; pre/post norm mechanisms, non-residual norm, RMSNorm runtime and no-bias evidence explained. | complete |
| slides 019--028 | yes | Activations、FFN 与 parallel blocks | Every screenshot included; activation taxonomy, gated FFN formulas, corroborating evidence and systems motivation explained. | complete |
| slides 029--034 | yes | Position embeddings 与 RoPE | Every screenshot included; relative-position geometry, rotations, formulas, implementation and extrapolation limits explained. | complete |
| slides 035--050 | yes | Hyperparameter defaults | Every screenshot included; FFN ratios, GLU budget, T5 exception, head/aspect ratios, vocabulary and regularization evidence explained. | complete |
| slides 051--055 | yes | Stability tricks | Every screenshot included; failure signals, softmax instability, z-loss, QK norm and soft-capping explained. | complete |
| slides 056--065 | yes | Attention variants and inference pressure | Every screenshot included; arithmetic intensity, KV-cache accounting, MQA/GQA quality tradeoffs and hybrid attention explained. | complete |
| slide 066 | yes | 本章小结：Recap | Final recap screenshot included and connected to an evidence-aware recipe checklist. | complete |
| teacher voice | not available | whole note | No transcript, subtitles, speaker notes or executable narration nodes exist in the lecture directory; no classroom voice is fabricated. | not applicable |
| PDF visual QA | yes | `qa/lecture03-notes/` | Full contact sheet and representative full-size pages inspected; checklist signed. | complete |

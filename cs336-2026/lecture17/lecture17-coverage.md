# Lecture 17 Coverage Matrix

Status: complete after second-round source-complete rewrite and verification on 2026-08-11.

Verification evidence:

- Strict coverage reports `figs=31 readfig=21 boxes=32 term_digest=1 teacher_voice=6 formulas=6 code=0 summaries=7 prose_chars=10129` with no errors or warnings.
- `tools/scripts/check_quality.sh cs336-2026/lecture17/lecture17-notes.tex` reports `27p 8s 32b 31f 326c/f ⭐⭐⭐`.
- `lecture17-teacher-voice-ledger.md` records thirteen transcript/source-aligned teaching points across omni-model framing, CLIP/SigLIP, LLaVA/OneVision, Qwen-VL, and Chameleon.
- Double-pass XeLaTeX succeeds with no layout overflow, missing-character, undefined-control-sequence, or rerun warnings.
- Canonical visual QA was rendered to `qa/lecture17-notes/`; the contact sheet and enlarged pages 5, 7, 11, 12, 14, 16--18, 20--22, and 27 were manually inspected.

| Source cluster | Teaching unit | Status |
|---|---|---|
| multimodality / ViT | modality-to-token framing | covered |
| CLIP / SigLIP / code figures | contrastive and sigmoid objectives, batch coupling, parallelism | covered |
| LLaVA | encoder-projector-LM architecture and generation boundary | covered |
| LLaVA-OneVision / all source figures | modality token budgets, data filtering, curriculum, three transfer cases | covered |
| Qwen-VL family / all source figures | staged training, examples, dynamic resolution, capability map, MRoPE, DeepStack, results | covered |
| Chameleon / VQ-VAE | discrete image tokens and unified generation | covered |
| transcript + executable narration | token budget, data quality, batch systems caveat, training stability, comprehension-vs-generation | covered |

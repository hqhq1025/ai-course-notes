# CS25 V6 Lecture 08 — Source Manifest

## Canonical course sources

- Stanford CS25 V6 course page: `https://web.stanford.edu/class/cs25/`
- Official Stanford Online recording: `https://www.youtube.com/watch?v=NDdc39KYqDU`
- Classroom date: 2026-05-21.
- Stanford Online upload date: 2026-06-04.
- Speaker: Victoria Lin, Thinking Machines; previously Meta AI and Salesforce AI Research.
- Recording runtime: 01:04:39. The prepared talk ends at 00:41:39; the remainder is substantive Q&A.
- Official deck: Google Drive file `10Doblrt3Le_FpbVQoMP0DbuCIO3rtWPW`, downloaded as `lecture08-slides.pdf` with 56 pages.
- Source disclaimer: the speaker states that the talk uses public material and reflects her own opinions rather than her employer's views.

## Lecture-snapshot primary papers

- Chameleon Team, `Chameleon: Mixed-Modal Early-Fusion Foundation Models`, arXiv `2405.09818v2`, revised 2025-03-21: `https://arxiv.org/abs/2405.09818v2`.
- Razavi, van den Oord, and Vinyals, `Generating Diverse High-Fidelity Images with VQ-VAE-2`, arXiv `1906.00446v1`, submitted 2019-06-02: `https://arxiv.org/abs/1906.00446v1`.
- Zhou et al., `Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model`, arXiv `2408.11039v1`, submitted 2024-08-20: `https://arxiv.org/abs/2408.11039v1`.
- Liang et al., `Mind the Gap: Understanding the Modality Gap in Multi-modal Contrastive Representation Learning`, arXiv `2203.02053v2`, revised 2022-10-19: `https://arxiv.org/abs/2203.02053v2`.
- Liang et al., `Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models`, arXiv `2411.04996v2`, revised 2025-05-08: `https://arxiv.org/abs/2411.04996v2`.
- Shi et al., `LMFusion: Adapting Pretrained Language Models for Multimodal Generation`, arXiv `2412.15188v4`, revised 2025-02-05: `https://arxiv.org/abs/2412.15188v4`.
- Deng et al., `Emerging Properties in Unified Multimodal Pretraining`, arXiv `2505.14683v3`, revised 2025-07-27: `https://arxiv.org/abs/2505.14683v3`.
- Physical Intelligence et al., `π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities`, arXiv `2604.15483v2`, revised 2026-04-24: `https://arxiv.org/abs/2604.15483v2`.

All versions above were public before the 2026-05-21 classroom date. The note uses them to clarify mechanisms and evidence boundaries, not to replace the lecture's own sequence.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata, source hashes, paper versions, and visual-audit counts.
- `lecture08.en.srt` preserves the official English manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture08-selection.tsv` freezes all 56 official pages: 37 required teaching pages and 19 optional title/build/recording-skipped pages.
- `lecture08-teacher-voice-ledger.md` maps spoken motivations, caveats, practical heuristics, and Q&A into the note.
- `slides-images/` contains all 56 official deck pages rendered as 1440×810 JPEG images.

## Visual audit

- The complete 01:04:39 recording was sampled every five seconds, producing 776 frames and 13 contact sheets.
- All 13 contact sheets were reviewed against the official deck.
- The recording uses clean full-screen deck pages during the prepared talk and a camera view over the conclusion slide during Q&A.
- No deck-external whiteboard, live demo, question card, or independent teaching diagram appears.
- Pages 053--055 are present in the downloadable deck but the recording jumps directly from page 052 to page 056. They are documented as optional deck-only appendix pages and are not reconstructed as taught content.

## Evidence boundaries

- `Token` is used as a sequence interface, not necessarily a discrete symbol. Continuous image patches and audio frames can be token-like model inputs.
- Text-only multimodal models and omni models are different regimes: accepting an image does not imply the model can generate images or audio.
- Chameleon's early-fusion result shows that discrete mixed-modal token sequences can work; it does not show that VQ image tokens are optimal for fine-grained understanding or scalable generation.
- Transfusion unifies a backbone while retaining different losses for text and images. A shared transformer does not require one universal target distribution.
- The modality-gap plots motivate specialization but do not prove that representation separation causes better downstream performance.
- MoT uses deterministic routing by known modality, unlike learned MoE gating. Its reported gains must be interpreted with active-parameter and compute accounting, not raw total-parameter counts alone.
- The speaker explicitly states that MoT-style separation helped image generation but did not improve image understanding in the discussed experiments.
- BAGEL and π0.7 are examples of modality-aware systems, not evidence that digital omni models have solved physical-world intelligence.
- Qualitative generations are evidence of capability but are not substitutes for controlled human evaluation, likelihood calibration, safety testing, or real-world task success.
- Language is currently an effective reasoning scaffold, but the Q&A does not establish that all future reasoning must pass through text.
- Pages 053--055 must not be treated as classroom content because they were not shown or discussed in the actual recording.

# CS25 V6 Lecture 05 — Source Manifest

## Canonical course sources

- Stanford CS25 V6 course page: `https://web.stanford.edu/class/cs25/`
- Official Stanford Online recording: `https://www.youtube.com/watch?v=e_H_tkpCAK4`
- Classroom date: 2026-04-30
- Stanford Online upload date: 2026-05-11
- Speaker: Shrimai Prabhumoye, Mistral AI and Boston University; the lecture primarily presents work completed at NVIDIA.
- Recording runtime: 00:57:56; the prepared talk ends at approximately 00:49:30 and the remaining recording is Q&A.

The course row publishes a `Link to slides`, but on 2026-08-12 that link resolves to Google Drive file `1dxdC76Rk_o6UEd5AqhHjp0rapsxYOR6j`, the 106-page `The Ultra-Scale Talk` deck already used by Lecture 04. It is not a Lecture 05 deck. The speaker's public research page lists the talk but does not expose an independent slide download. This lecture therefore uses the official recording as the canonical visual spine and does not copy the incorrect Drive file.

## Lecture-snapshot primary papers

- Feng et al., `Maximize Your Data's Potential: Enhancing LLM Accuracy with Two-Phase Pretraining`, arXiv `2412.15285v1`, submitted 2024-12-18: `https://arxiv.org/abs/2412.15285v1`.
- Akter et al., `Front-Loading Reasoning: The Synergy between Pretraining and Post-Training Data`, arXiv `2510.03264v1`, submitted 2025-09-26: `https://arxiv.org/abs/2510.03264v1`.
- Hatamizadeh et al., `RLP: Reinforcement as a Pretraining Objective`, arXiv `2510.01265v2`, revised 2026-03-01 and published at ICLR 2026: `https://arxiv.org/abs/2510.01265v2`. Version 2 is the latest version available before the 2026-04-30 lecture.

## Early-reasoning comparison sources

- Zelikman et al., `Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking`, arXiv `2403.09629`: `https://arxiv.org/abs/2403.09629`.
- Dong et al., `Reinforcement Pre-Training`, arXiv `2506.08007`: `https://arxiv.org/abs/2506.08007`.
- Liu et al., `Reinforcement Learning on Pre-Training Data`, arXiv `2509.19249`: `https://arxiv.org/abs/2509.19249`.

## Supporting primary resources

- Epoch AI, `Will we run out of data? Limits of LLM scaling based on human-generated data`: `https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data`.
- Hugging Face, FineWeb-Edu dataset card and educational-quality classifier description: `https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu`.
- NVIDIA, Nemotron pretraining and post-training data collections: `https://huggingface.co/collections/nvidia/nemotron-pre-training-datasets` and `https://huggingface.co/collections/nvidia/nemotron-post-training-datasets`.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata, source hashes, paper-version boundaries, and visual-audit counts.
- `lecture05.en.srt` preserves the official English manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture05-selection.tsv` freezes 44 recording-derived slide states: 41 required teaching visuals and three optional title cards.
- `lecture05-teacher-voice-ledger.md` maps spoken motivation, caveats, examples, mid-talk questions, and final Q&A into the note.
- `slides-images/` contains 44 clean 1920x1080 frames extracted from the official recording.

## Visual audit

- The full 00:57:56 recording was sampled every five seconds, producing 695 frames and 12 timeline contact sheets.
- All 12 contact sheets were reviewed. The prepared talk contains direct-feed slides through approximately 00:49:30; the remaining segment is speaker-only Q&A except for no new independent teaching visual.
- A frame-difference pass found 69 bright slide runs. Progressive builds, repeated title cards, and camera interruptions were then reconciled manually.
- Final independent states: 41 required teaching visuals plus three optional title/divider cards.
- Every selected frame is a clean direct-feed 1920x1080 recording frame; no projector crop or camera-dominant substitute is required.

## Evidence boundaries

- `Quality` is an operational label produced by a rubric, classifier, filtering pipeline, domain prior, and downstream ablation. It is not an intrinsic scalar property of a document.
- The two-phase results show that diversity-first and quality-later ordering worked in the reported settings. They do not prove one universal curriculum for every corpus, token budget, architecture, or objective.
- The front-loading results compare carefully constructed reasoning-data conditions. They do not imply that arbitrary chain-of-thought text is always beneficial or that post-training becomes unnecessary.
- `Reasoning data` in the experiments largely means question, long reasoning trace, and final-solution records from community datasets, with a STEM-heavy composition. The lecture explicitly warns that the definition is not domain universal.
- RLP's reward is dense and verifier-free relative to RLVR-style external verification, but it still depends on the observed next token, a learned thought policy, a no-think baseline, rollout sampling, and optimization choices.
- A positive token-level information-gain reward means the sampled thought increased probability on the observed next token relative to the baseline. It does not by itself prove truth, causal understanding, or human-interpretable reasoning.
- Reported relative gains are tied to the shown benchmarks, baselines, token budgets, and FLOP accounting. They are not interchangeable with absolute percentage-point improvements.
- The lecture presents RLP experiments on language-model pretraining. Vision-language alignment is explicitly left untested in Q&A.
- RLHF, hallucination mitigation, and alignment classifiers are discussed in Q&A as adjacent open work, not as results of the three featured papers.

## Private temporary inputs

- The 1920x1080 source recording, raw `yt-dlp` metadata, five-second audit frames, contact sheets, OCR scratch output, and downloaded paper PDFs remain under `/tmp/cs25-v6-lecture05-work/` and must not be committed.

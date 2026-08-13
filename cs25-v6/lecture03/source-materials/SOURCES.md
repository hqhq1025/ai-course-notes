# CS25 V6 Lecture 03 — Source Manifest

## Canonical course sources

- Stanford CS25 V6 course page: `https://web.stanford.edu/class/cs25/`
- Official recording: `https://www.youtube.com/watch?v=OyimE74UMF8`
- Classroom date: 2026-04-16
- Stanford Online upload date: 2026-04-27
- Speaker: Albert Gu, Carnegie Mellon University and Cartesia AI
- Recording runtime: 01:17:07; the Albert Gu lecture and Q&A end at approximately 01:06:35. The remaining MongoDB presentation is sponsor content and is not part of this lecture note.

The official course row does not publish a slide link for this lecture. The visual spine is therefore reconstructed from the official recording rather than from an independently downloadable deck.

## Speaker-authored conceptual source

- Albert Gu, `On the Tradeoffs of SSMs and Transformers`, Goomba Lab, published 2025-07-08: `https://goombalab.github.io/blog/2025/tradeoffs/`

The speaker explicitly recommends this article as a supplement in the opening minute. It supplies the longer written version of the state-size/state-expressivity/training-efficiency decomposition, the database/brain analogy, the token-resolution thesis, and the final FLOPs-to-capabilities framing. The classroom recording remains canonical for what was actually said on 2026-04-16.

## Lecture-snapshot primary papers

- Gu and Dao, `Mamba: Linear-Time Sequence Modeling with Selective State Spaces`, `https://arxiv.org/abs/2312.00752`.
- Dao and Gu, `Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality`, `https://arxiv.org/abs/2405.21060`.
- Lahoti et al., `Mamba-3: Improved Sequence Modeling using State Space Principles`, `https://arxiv.org/abs/2603.15569v1`, submitted 2026-03-16. Version 1 is the only version available before the lecture.
- Hwang, Wang, and Gu, `Dynamic Chunking for End-to-End Hierarchical Sequence Modeling`, `https://arxiv.org/abs/2507.07955v2`, revised 2025-07-15. Version 2 is the lecture-snapshot H-Net paper.
- Wang et al., `MambaByte: Token-free Selective State Space Model`, `https://arxiv.org/abs/2401.13660`.
- Shah et al., `dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning`, `https://arxiv.org/abs/2602.10603v3`, revised 2026-04-09. Version 3 is the latest revision available before the 2026-04-16 lecture; later revisions must not be projected backward into the classroom claims.
- Goldman et al., `The Benefits of Learning to Route`, H3 / Hungry Hungry Hippos, `https://arxiv.org/abs/2212.14052`.
- Lieber et al., `Jamba: A Hybrid Transformer-Mamba Language Model`, `https://arxiv.org/abs/2403.19887`.
- Glorioso et al., `Zamba: A Compact 7B SSM Hybrid Model`, `https://arxiv.org/abs/2405.16712`.
- Ren et al., `Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling`, `https://arxiv.org/abs/2406.07522`.
- Yang et al., `Parallelizing Linear Transformers with the Delta Rule over Sequence Length`, `https://arxiv.org/abs/2406.06484`.
- Schmidt et al., `Tokenization Is More Than Compression`, `https://arxiv.org/abs/2402.18376`.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata, content hashes, source counts, paper-version boundaries, and visual-audit results.
- `lecture03.en.srt` preserves the English original automatic captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture03-visual-audit.md` records the complete two-second recording audit and every required/optional visual decision.
- `lecture03-selection.tsv` freezes 33 recording-derived slide states: 32 required teaching visuals and one optional title card.
- `lecture03-teacher-voice-ledger.md` maps spoken motivation, caveats, examples, and Q&A into the note.
- `slides-images/` contains the 33 high-resolution recording-derived slide states. Camera-dominant pages are cropped from the projector region and remain identifiable as recording captures.

## Visual audit

- The Albert Gu segment was sampled every two seconds, producing 1,999 frames.
- The high-recall pass classified 1,053 clean direct-feed slide frames, 830 projector-region frames, and 116 camera/fallback frames.
- A complete 10-second timeline contact-sheet review covered the whole lecture and Q&A; denser two-second candidates were inspected around transitions and camera-only gaps.
- Final independent states: 32 required teaching visuals plus one optional title card.
- No deck-external question card, whiteboard derivation, or independent demonstration was found. The Q&A is visually speaker-only except for one duplicate H-Net architecture flash.
- The sponsor segment beginning at approximately 01:06:30 is intentionally excluded.

## Evidence boundaries

- `Linear-time` and `constant-memory` describe the recurrent inference state under the model abstraction; wall-clock throughput still depends on kernels, batch size, hardware, and implementation.
- The database/brain analogy is explicitly coarse. It is an intuition about memory interfaces, not a neuroscience claim.
- The commonly reported hybrid ratios are empirical and task/model dependent. The speaker says older perplexity studies often found roughly 10:1 SSM-to-attention layers, while newer systems often use at least 3:1 or 4:1; neither is a universal optimum.
- Byte-level and DNA curves support an architecture-by-resolution interaction in the shown settings. They do not prove that SSMs dominate Transformers on every raw modality or downstream task.
- H-Net is presented as an early end-to-end dynamic-chunking architecture. The speaker explicitly says it is not the end state and had not yet been validated at the largest scales.
- The claim that compression can improve modeling is an inductive-bias hypothesis supported by H-Net ablations, not proof that every finite recurrent state is inherently more intelligent.
- Small-model behavior, biological plausibility, and long-context hierarchical memory are discussed in Q&A as open questions or research directions, not established results.

## Private temporary inputs

- The 1920x1080 source recording, raw `yt-dlp` metadata, dense video-audit samples, OCR scratch output, and downloaded web/paper copies remain under `/tmp/cs25-v6-lecture03.*` and must not be committed.

# Lecture 39 Source Audit

## Canonical public sources

- Course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Official recording: `https://www.youtube.com/watch?v=8kXIaUM3h1E`
- Official title: `Stanford CS25: V5 I Multimodal World Models for Drug Discovery, Eshed Margalit of Noetik.ai`
- Classroom date: May 20, 2025.
- Stanford Online upload date: June 13, 2025.
- Runtime and resolution: 1:11:02, 1920x1080.
- Speaker: Eshed Margalit, Noetik.ai.
- The course row and video description expose no standalone public slide deck.

## Captions and transcript

- YouTube exposes a manual `en-US` subtitle track with 1,643 SRT cues.
- After normalization and removal of empty rolling-caption fragments, 1,622 timed transcript segments remain.
- `lecture39.en.srt` preserves the refreshed manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are derived from that track.
- The speaker-only Q&A from approximately 00:58:43 through 01:10:07 is required teacher voice. It adds evidence boundaries about sample size, causal validation, missing healthy controls, experimental prioritization, and the realistic role of scientific agents.

## Visual-source audit

- No standalone public deck was found on the CS25 V5 schedule or in the official recording description.
- The complete 4,262-second recording was scanned once per second with no brightness gate and a low visual-difference threshold.
- The high-recall scan produced 441 candidates. All were OCRed and reviewed through 28 contact sheets plus four batch overviews.
- `lecture39-selection.tsv` marks 60 independent teaching states as required and 381 bumper, speaker-only, transition, repeated, progressive, or embedded-video micro-states as optional.
- The official recording is therefore the canonical visual spine. The late Q&A contains no independent teaching slide after the closing frame, so its content is preserved through the teacher-voice ledger and prose rather than speaker screenshots.

## Reproducibility and retention

- The temporary 1080p source recording is stored outside the repository at `/tmp/cs25-lecture39-audit/lecture39-source.mp4` and must not be committed.
- The raw `yt-dlp` metadata dump is stored outside the repository at `/tmp/cs25-lecture39-audit/metadata.full.json` and must not be committed.
- The one-second scan, OCR index, and contact sheets remain temporary audit inputs under `/tmp/cs25-lecture39-audit/slide-scan/`.
- Public `metadata.json` contains only stable fields and SHA-256 hashes.
- SHA-256 values:
  - source video: `cb26fbe1b3d4209fddc4d21f6c3f9fad4e9586f48cb34cadcef9e2b92d41f637`
  - manual captions: `db7a7224926946145bd99fcd88be64ad652169735d0d2a855bcad27b1ea1c77e`
  - cover: `b5898d6a549f4cf49955d4bf6885f54c358361164783432bd93b61a8f1233e2b`

## Evidence boundary

- The talk reports a rapidly growing Noetik research dataset and several in-progress systems. Dataset counts, model status, and product interfaces are evidence from the May 20, 2025 lecture, not claims about Noetik's current 2026 production state.
- Predicted gene expression and virtual-cell counterfactuals are model outputs. They are useful for hypothesis ranking, but they do not by themselves establish a causal drug mechanism or clinical efficacy.
- The presented cohort is built from clinically obtained tumor material. Missing healthy controls and sampling bias constrain what the learned patient distribution can support.
- A simulator does not choose valuable experiments on its own. Domain experts or well-evaluated agents still need to define interventions, rank hypotheses, and close the loop with wet-lab and clinical validation.

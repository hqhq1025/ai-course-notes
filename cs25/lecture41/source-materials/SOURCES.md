# Lecture 41 Source Audit

## Canonical sources

- Official Stanford recording: `https://www.youtube.com/watch?v=YGHF8_tf--g`
- CS25 V5 course page: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Movie Gen primary paper: `https://ai.meta.com/static-resource/movie-gen-research-paper/`

The course page identifies the June 3, 2025 class session and Andrew Brown of Meta. The official recording was uploaded July 3, 2025, runs 1:13:35, and is available at 1920x1080. Neither the course row, video description, nor the speaker's public announcement links a standalone slide deck, so the official recording is the canonical visual source.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata and SHA-256 hashes.
- `lecture41.en.srt` preserves the refreshed manual `en-US` captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are derived from 1,438 non-empty timed segments.
- `lecture41-teacher-voice-ledger.md` maps spoken explanations and Q\&A boundaries into the note.
- `lecture41-selection.tsv` records all 780 required/optional decisions from the full visual audit.
- `slides-images/` contains only the 32 retained full-resolution teaching states.

## Visual audit

- The full 4,415-second recording was sampled once per second with no brightness gate.
- Perceptual transition clustering produced 780 high-recall candidates.
- All candidates were OCRed and reviewed through 49 contact sheets and 13 batch overviews.
- Thirty-two independent slide or capability/evidence states are required; 748 bumper, speaker-only, transition, progressive, repeated, loading, embedded-video micro-state, or Q\&A projector states are optional.
- The 00:54:10--01:13:20 Q\&A introduces almost no new visual material, but all substantive answers remain required teacher voice.

## Evidence boundaries

- Generated clips demonstrate capability, not distribution-wide reliability or causal physical understanding.
- Human pairwise evaluation is more informative than weak automatic video metrics, but it remains prompt-set- and protocol-dependent.
- The scaling-law overlay supports a useful empirical analogy to Llama 3; it does not prove modality-independent scaling in all regimes.
- Movie Gen is a model family. Video generation, editing, personalization, and synchronized audio use related but distinct training paths or models.
- Public training-infrastructure details come from the paper; serving architecture was not disclosed in the talk and must not be invented.

## Private temporary inputs

- `/tmp/cs25-lecture41-audit/lecture41-source.mp4`
- `/tmp/cs25-lecture41-audit/lecture41.info.json`
- `/tmp/cs25-lecture41-audit/movie-gen-paper.pdf`
- `/tmp/cs25-lecture41-audit/slide-preview/`

These audit inputs must not be committed. Raw `yt-dlp` metadata and the source video remain outside the repository.

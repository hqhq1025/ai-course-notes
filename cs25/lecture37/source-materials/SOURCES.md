# Lecture 37 Source Audit

## Canonical public sources

- Course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Official recording: `https://www.youtube.com/watch?v=ebnX5Ur1hBk`
- Official title: `Stanford CS25: V5 I Large Language Model Reasoning, Denny Zhou of Google Deepmind`
- Classroom date: April 29, 2025.
- Stanford Online upload date: May 21, 2025.
- Runtime and resolution: 1:06:07, 1920x1080.
- Speaker: Denny Zhou, Google DeepMind.
- Official speaker deck: `https://dennyzhou.github.io/LLM-Reasoning-Stanford-CS-25.pdf`
- The deck is 49 pages and identifies itself as the Stanford CS25 V5 talk from April 29, 2025.

## Captions and transcript

- YouTube exposes a manual `en-US` subtitle track with 1,089 SRT cues.
- All 1,089 cues parse into non-empty timed transcript segments.
- `lecture37.en.srt` preserves the official manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are derived from that track.
- The Q\&A from approximately 00:57:30 through 01:06:04 is part of the required teacher voice even though it introduces no new slide pages.

## Visual-source audit

- All 49 official deck pages were rendered at 180 dpi into `slides-images/`.
- Pages 1--48 contain independent teaching content. Page 49 is the closing card and is optional.
- The full 1:06:07 recording was sampled every 30 seconds, producing 132 review frames.
- That audit found only the official deck, the speaker, and ordinary transitions; no deck-external live demo, whiteboard, code screen, or independent teaching visual needs a separate frame.
- The official deck is therefore the canonical visual spine, while the recording supplies motivation, caveats, examples, transitions, and Q\&A.

## Reproducibility and retention

- The temporary 1080p source recording is stored outside the repository at `/tmp/cs25-lecture37-audit/lecture37-source.mp4` and must not be committed.
- The raw `yt-dlp` metadata dump is stored outside the repository at `/tmp/cs25-lecture37-audit/metadata.full.json` and must not be committed.
- Public `metadata.json` contains only stable fields and SHA-256 hashes.
- SHA-256 values:
  - source video: `bcb0804d8e890a18b2a3e8c3effbd1d6bac98accdf5f3bc916d3301005f52f52`
  - official slides: `6e5b54fd31b385d0d8f9aa7de5cb3f4accb74e477a3d7c3558d59c52d879fcfc`
  - manual captions: `a08715f44c45ac0c971b6e72ae7b0b81360ff42c5b1e52813d2e4081b3496524`
  - cover: `04c5dcc85533977bf3336894e471f76643eb381671cc572ce8b2b924a4fe7b2b`

## Evidence boundary

- The lecture defines reasoning operationally as intermediate generated tokens between input and final answer; it does not claim that those tokens reproduce human cognition.
- Claims about Gemini 2.0 thinking mode, benchmark results, confidence, and deep-research systems are April 2025 classroom evidence, not 2026 product specifications.
- The speaker's comparisons such as “RL finetuning > SFT” and “retrieval + reasoning > reasoning only” are a compact lecture synthesis whose scope and verifier assumptions must be explained in the note.

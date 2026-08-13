# Lecture 40 Source Audit

## Canonical public sources

- Course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Official recording: `https://www.youtube.com/watch?v=vXtapCFctTI`
- Official title: `Stanford CS25: V5 I Transformers in Diffusion Models for Image Generation and Beyond`
- Classroom date: May 27, 2025.
- Stanford Online upload date: June 24, 2025.
- Runtime and resolution: 1:14:32, 1920x1080.
- Speaker: Sayak Paul, Hugging Face.
- Speaker research page: `https://sayak.dev/pages/research.html`
- Official slide short link: `http://bit.ly/dit-cs25`
- Resolved official deck: `https://docs.google.com/presentation/d/1dGA1Jpppv9BciOOrc95ZYRinsj_ZYrI-IQOIifHGIZw/edit?usp=sharing`
- The exported official deck contains 66 pages and is stored as `lecture40-slides.pdf`.

## Captions and transcript

- YouTube exposes a manual `en-US` subtitle track with 1,528 raw SRT cues.
- The repository parser normalizes these into 1,489 non-empty timed transcript segments.
- The fresh manual captions replace the legacy 3,523-cue rolling-caption artifact.
- `lecture40.en.srt`, `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` preserve the spoken lecture and Q\&A.

## Visual-source audit

- All 66 official pages were exported to PDF and rendered at high resolution into `slides-images/`.
- Pages 04--65 are independent teaching pages and are required in the note.
- Page 01 is the title, page 02 is a scope disclaimer, page 03 is the administrative overview, and page 66 is the closing link/QR page; their useful information is preserved in metadata and prose.
- A full-recording audit sampled 149 frames at 30-second intervals across all 4,472 seconds. The samples contain official slides or speaker-only footage; no deck-external live demo, whiteboard, code screen, or independent teaching visual was found.
- The official deck is therefore the canonical visual spine, while the recording supplies teacher voice, transitions, practical heuristics, and Q\&A.

## Reproducibility and retention

- The temporary 1080p source recording remains outside the repository at `/tmp/cs25-lecture40-audit/lecture40-source.mp4` and must not be committed.
- The raw `yt-dlp` metadata dump remains outside the repository at `/tmp/cs25-lecture40-audit/metadata.full.json` and must not be committed.
- The rendered deck PDF is public source material and is retained as `lecture40-slides.pdf`; generated page images are retained under `slides-images/` for source-complete note generation.
- SHA-256 values are recorded in `metadata.json` for the source video, manual captions, cover, official deck, course-page snapshot, and speaker source-page snapshot.

## Evidence boundary

- Model names, efficiency numbers, quality claims, and architecture status reflect the May 27, 2025 lecture and its cited papers. They are not automatically current product claims in August 2026.
- Qualitative image grids do not establish prompt fidelity, diversity, fairness, or human preference. Benchmark plots must be read with their compute, resolution, dataset, and evaluation setup.
- Architectural simplicity does not imply training simplicity. The speaker explicitly separates backbone design from data, optimization, post-training, preference alignment, and evaluation.
- Parameter sharing, linear attention, MMDiT, and structural-control designs trade quality, memory, latency, and implementation complexity; no single architecture dominates every deployment regime.

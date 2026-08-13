# Lecture 01 Source Audit

## Canonical classroom sources

- Official Stanford recording: `https://www.youtube.com/watch?v=bHSDPgZYie0`
  - Title: `Stanford CS25: Transformers United V6 I Overview of Transformers`
  - Classroom date: 2026-04-02
  - Upload date: 2026-04-22
  - Runtime: 1:16:46 (`4606` seconds)
  - Resolution: 1920x1080 at 30 fps
- Live V6 course page: `https://web.stanford.edu/class/cs25/`
- Official Google Drive deck: document `153Gu4BIfpnn6jj6WmXlsyD7kv702zcrB`
  - Local canonical export: `slides.pdf`
  - Pages: 156
  - SHA-256: `049ad3c219fa60aa7465dd32a51a4090aa1bff5bb9d73f46ecd40d2283c40a70`
- Official manual YouTube captions: `en-US`
  - Raw cues: 1,558
  - Parsed non-empty segments: 1,558
  - SHA-256: `5523b5b18aac2bee3427a35d3cdce2ba2515a919091439406fe6cea4cd248306`

The recording and deck identify Steven Feng and Karan Singh as the classroom presenters. The video description also lists Michael C. Frank and Christopher Manning among the course instructors, but they do not present this recorded overview lecture.

## Primary papers linked from the official course row

- Feng, Tan, and Frank, `Baby Scale: Investigating Models Trained on Individual Children's Language Input`, `https://arxiv.org/abs/2603.29522`.
- Zeng, Feng, and Frank, `Bringing Up a Bilingual BabyLM: Investigating Multilingual Language Acquisition Using Small-Scale Models`, `https://arxiv.org/abs/2603.29552`.
- Singh et al., `To Memorize or to Retrieve: Scaling the Interaction Between Pretraining and Retrieval`, `https://arxiv.org/abs/2604.00715`.
- Singh, Band, and Adeli, `Curriculum-Guided Layer Scaling for Language Model Pretraining`, `https://arxiv.org/abs/2506.11389`.
- Singh et al., `Interpretable Cross-Network Attention for Resting-State fMRI Representation Learning`, `https://arxiv.org/abs/2603.00786`.
- Liu et al., `A Unified Definition of Hallucination: It's The World Model, Stupid!`, `https://arxiv.org/abs/2512.21577`.

## Local reproducible artifacts

- `metadata.json` contains sanitized stable metadata and content hashes.
- `lecture01.en.srt` preserves the refreshed manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are deterministic caption derivatives.
- `lecture01-selection.tsv` records all 156 required/optional slide decisions.
- `lecture01-teacher-voice-ledger.md` maps spoken motivation, caveats, examples, and transitions into the note.
- `slides-images/` contains all 156 official deck renders, including optional pages for reproducibility.

## Visual audit

- All 156 deck pages were rendered at the original 16:9 slide aspect ratio and reviewed through ten contact sheets.
- Required teaching pages: 116.
- Optional pages: 40, limited to cover/biography/logistics, pure section dividers, paper-title or QR/contact pages without independent mechanisms, repeated research-question cards, progressive states superseded by a complete page, and the closing card.
- The complete recording was sampled every five seconds. Of 921 samples, 882 were slide-like; transition clustering retained 194 stable high-recall candidates.
- Review of all candidates found no independent deck-external teaching visual. Speaker-only states and progressive builds are therefore optional; the official deck remains the visual spine.

## Evidence boundaries

- The overview combines tutorial material, the instructors' own recent papers, broad field maps, and forward-looking opinions. These evidence types must remain visibly distinct.
- BabyLM, bilingual exposure, RAG scaling, curriculum-guided growth, fMRI representation learning, and hallucination results are study-specific. They do not establish universal laws for all model sizes, languages, domains, or deployment settings.
- The April 2026 lecture snapshot includes claims and papers published close to the classroom date. Later developments must not be projected backward into the lecture.
- “World model,” “true continual learning,” “alignment,” and “hallucination” are used with explicit definitions and assumptions rather than as interchangeable slogans.

## Private temporary inputs

- `/tmp/cs25-v6-lecture01.7ohKd8/source.mp4`
- `/tmp/cs25-v6-lecture01.7ohKd8/source.info.json`
- `/tmp/cs25-v6-lecture01.7ohKd8/video-audit/`
- `/tmp/cs25-v6-lecture01.7ohKd8/contact-sheets/`

The source video and raw `yt-dlp` metadata remain outside the repository and must not be committed.

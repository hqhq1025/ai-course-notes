# Lecture 35 Source Audit

## Canonical public sources

- Course schedule: `https://web.stanford.edu/class/cs25/past/cs25-v5/`
- Official recording: `https://www.youtube.com/watch?v=gLwiPrwUDJ8`
- Official title: `Stanford CS25: V5 I RL as a Co-Design of Product and Research, Karina Nguyen`
- Classroom date: April 8, 2025.
- Stanford Online upload date: April 29, 2025.
- Runtime and resolution: 1:12:10, 1920x1080.
- Speaker: Karina Nguyen, OpenAI; the classroom introduction also notes her previous work at Anthropic.
- The course page and video description do not link a standalone slide deck. The official recording is therefore the canonical visual source.

## Captions and transcript

- YouTube exposes a manual `en-US` subtitle track with 1,325 SRT cues.
- Empty cues were omitted when building the readable transcript, leaving 1,288 timed text segments.
- The previous local subtitle file contained 3,135 rolling/repeated cues. It was replaced by the fresh manual track rather than used as the writing source.
- `lecture35.en.srt` preserves the official manual captions with LF line endings.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` are derived from that manual track.

## Visual recovery method

- The full 4,330-second official recording was sampled once per second at the native 1920x1080 frame.
- Bright-frame filtering retained 2,540 slide-like samples.
- Visual-change clustering produced 208 high-recall candidates.
- Every candidate was reviewed through 13 contact sheets and OCR-assisted indexing.
- Sixty independent teaching states were retained. The remaining 148 states are opening/closing bumpers, speaker-only frames, black transitions, repeated frames, or superseded progressive builds from embedded product demos.
- `lecture35-selection.tsv` records the required/optional decision for all 208 candidates.
- Required states are copied into `slides-images/` with semantic filenames. The downloaded source video remains a temporary audit artifact and is not committed.

## Legacy-note defects

- The old note had no canonical video URL and only generic Spring 2025 metadata.
- It had zero figures, zero teacher-voice markers, zero displayed formula blocks, and zero captioned listings.
- It compressed the talk into roughly 10 KB and omitted the full visual evidence chain: Canvas demos, fashion search, 100K context, adaptive interfaces, Claude in Slack, collaborator training, refusal taxonomy, eval construction, dataset-level debugging, XSTest, RL-environment design, reward hacking, and the future vignettes.
- It treated the lecture as a generic RL overview instead of the speaker's actual thesis: product behavior, evaluation, environment, reward, and interface must be co-designed.
- The replacement note must preserve the long Q&A because it contains important spoken clarifications on subjective tasks, preference diversity, RLAIF, qualitative diagnosis, synthetic-data verification, cost, robotics, social intelligence, and research-driven product development.

## Integrity hashes

- Source video SHA-256: `6748478a190a759596e13b8f0e4fca8740b234438689820e68feacac21228d78`
- Manual-caption SHA-256: `873707553b4528e6aa112089f035f03f92565386196a38580d7c2d0c46410a16`
- Cover SHA-256: `84fdd9ea778b867d9c85ac311703518ee6750ebadf5aa3fe76620158043071a2`

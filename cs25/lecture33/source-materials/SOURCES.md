# Lecture 33 Source Audit

## Canonical standalone source

- Official video: Stanford Online, `Stanford CS25: V4 I Hyung Won Chung of OpenAI`.
  - Video ID: `orDKvo8h71o`
  - Talk title in the official description: `Shaping the Future of AI from the History of Transformer`
  - Classroom date: 2024-04-11
  - Upload date: 2024-06-11
  - Runtime: 36:30 (`2190` seconds)
  - Resolution: 1920x1080
  - Official playlist position: 33
- Official V4 archive: `https://web.stanford.edu/class/cs25/past/cs25-v4/`.
- Official speaker deck: Google Slides document `1u05yQQaw4QXLVYGLI6o3YoFHv6eC3YN8GvWD8JMumpE`.
  - Local canonical export: `lecture33-slides.pdf`
  - Pages: 67
  - SHA-256: `24114d8f2d108454eb730efc9d2e8e4de42ddb5f10d6331e9eacb089c8e6fa36`
- Official manual subtitle track: YouTube `en-US`.
  - Parsed caption segments: 376
  - Derivatives: `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md`
  - SHA-256: `55420fd72d86e96b5aebeb893d1c2af384e599242e1a421d0eb996ec57e2fd3c`

## Relationship to Lecture 27

- The official playlist also contains `3gb-ZkVRemQ`, a combined 1:17:07 classroom upload with Jason Wei followed by Hyung Won Chung.
- Lecture 33 is the official standalone edit of the Hyung Won Chung talk from that classroom session, not a different lecture topic.
- The standalone deck export is byte-identical to `cs25/lecture27/hyung-slides.pdf`; the two files share the SHA-256 above.
- Lecture 33 remains a separate deliverable because it is an independent official playlist item with its own video ID, metadata, cover, captions, timestamps, and audience reading path.
- The standalone edit ends with the prepared talk and does not include the later joint Q\&A retained in Lecture 27. The Lecture 33 note therefore excludes Q\&A-only claims about MLE, RLHF, architecture bottlenecks, Moore's law, and energy limits.

## Visual policy

- All 67 official pages are rendered as `slides-images/hyung-slide-001.jpg` through `hyung-slide-067.jpg`.
- Required teaching pages: 47.
- Optional pages: 20, limited to progressive duplicates, an empty comparison scaffold, a pure section divider, and an intermediate multi-turn-attention build.
- The final complete state of each progressive sequence is retained whenever it carries the same teaching claim as the omitted builds.
- Because the official deck is complete, ordinary teaching figures use slide renders rather than video-frame reconstruction.

## Legacy-note audit

The legacy note was an 11 KB prose summary with no official deck coverage, no canonical standalone metadata, no teacher-voice ledger, and no visual evidence beyond the cover. It compressed the talk into broad claims such as “decoder-only won” while omitting the 67-page derivation, the four-step architecture transformation, the historical task assumptions, and the speaker's evidence-level caveats.

The replacement note must preserve the actual prepared-talk boundary. It should explain exponentially cheaper compute as a proposed dominant force rather than a universal law; distinguish short-run efficiency from long-run scalability; derive the encoder-decoder to decoder-only transformation one assumption at a time; and retain the speaker's explicit labels such as anecdotal evidence, hypothesis, and extrapolation.

## Historical-claim policy

- Product, architecture, hardware, and scaling claims are presented as April 2024 classroom material.
- The speaker's compute extrapolation and architecture predictions are labeled as hypotheses or research heuristics, not settled laws.
- The note distinguishes empirical evidence from illustrative examples, especially for FLAN, bidirectionality, layer depth, and cache reuse.
- The note does not import the combined video's later Q\&A into the standalone lecture.

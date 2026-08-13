# Lecture 40 Coverage Matrix

## Coverage policy

- Canonical visual source: Sayak Paul's official 66-page Google Slides deck.
- Required nodes: pages 04--65, for 62 independent teaching pages.
- Optional nodes: pages 01--03 and 66, covering title, scope/overview administration, and closing contact information.
- Every required slide image must occur exactly once in `lecture40-notes.tex`.
- The full 1:14:32 recording supplies required teacher voice, including the approximately 00:57:31--01:08:43 architecture and evaluation Q\&A.

## Section mapping

| Note section | Required deck pages | Teacher voice |
|---|---|---|
| Diffusion/flow-matching mental model and system components | 04--14 | 00:02:48--00:14:44 |
| Giant UNet, UViT, and motivation for DiT | 15--21 | 00:14:44--00:21:54 |
| Original DiT: patching, conditioning, adaLN-Zero, initialization, scaling | 22--34 | 00:21:54--00:32:56 |
| PixArt-α and text-conditioned DiT | 35--40 | 00:32:56--00:40:45 |
| Quadratic attention and SANA efficiency | 41--44 | 00:40:45--00:49:49 |
| MMDiT/SD3, modality-specific projections, and variants | 45--54 | 00:49:49--00:57:31 plus Q\&A 01:03:04--01:04:45 |
| Parameter sharing and DiT-Air | 55--58 | 01:05:00--01:08:43 |
| Structural controls and video generation | 59--61 | 01:08:47--01:11:44 |
| In-context generation, implementations, MoE, and open directions | 62--65 | 01:11:44--01:14:23 |

## Intentional omissions

| Deck pages / recording states | Reason |
|---|---|
| 01 | Title page; note cover and metadata preserve title, speaker, venue, and date. |
| 02 | Scope disclaimer; its substantive limits are required in prose and the teacher-voice ledger, but it adds no architecture mechanism. |
| 03 | Administrative overview; the note's section plan preserves the sequence. |
| 66 | Closing slide with short URL, QR code, and sample image; source links are preserved in source audit and further reading. |
| Speaker-only frames throughout the recording | No independent visual evidence; spoken explanations and Q\&A are retained in the ledger and note. |

## Status

- [x] Official video, classroom date, upload date, speaker, runtime, resolution, cover, and manual captions verified.
- [x] Speaker source page and official Google Slides deck verified; 66-page PDF exported and hashed.
- [x] All 66 deck pages rendered and reviewed; 62 required/4 optional decisions completed.
- [x] Full-recording 30-second audit found no deck-external teaching visual.
- [x] Fresh manual captions and derived transcript artifacts completed.
- [x] Legacy thin-note, missing URL, one-figure coverage, and rolling-subtitle defects documented.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: all 62 required deck pages appear once.
- [x] Strict coverage passed with no warnings.
- [x] Stabilized double XeLaTeX passed and canonical PDF regenerated at 49 pages.
- [x] PDF visual QA signed after complete contact-sheet review and full-size inspection of pages 48 and 49.

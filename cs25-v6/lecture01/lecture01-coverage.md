# Lecture 01 Coverage Matrix

## Coverage policy

- Canonical visual source: the official 156-page Stanford CS25 V6 deck.
- Required nodes: 116 independent teaching pages.
- Optional nodes: 40 cover, biography, sponsor/logistics, section-divider, paper-title/QR, repeated, progressive, or closing pages.
- Every required slide image must occur exactly once in `lecture01-notes.tex`.
- The full 1:16:46 recording supplies required teacher voice; the five-second high-recall audit found no independent deck-external teaching visual.

## Section mapping

| Note section | Required deck pages | Teacher voice |
|---|---|---|
| Learning paradigms and representation | 11, 13--18, 20--22 | 00:06:12--00:10:14 |
| Embeddings, RNNs, and Transformer mechanics | 23--33 | 00:10:14--00:16:20 |
| Pretraining data and strategy map | 35--37 | 00:16:20--00:20:23 |
| Baby Scale | 39--41, 43--50 | 00:20:23--00:25:25 |
| Bilingual BabyLM | 52--53, 55--57, 59--60, 62--66 | 00:25:25--00:29:01 |
| RAG and curriculum-guided scaling | 68, 70--72, 75--81, 84--86 | 00:29:01--00:36:33 |
| Reasoning and preference optimization | 88--94, 96--100 | 00:36:33--00:43:12 |
| Self-improving agents | 102--107 | 00:43:12--00:45:43 |
| Vision and neuroscience applications | 109, 111--112, 114--115, 117--118 | 00:45:43--00:52:47 |
| Future limits and hallucination | 121--125, 127--128, 130--137 | 00:52:47--01:03:52 |
| Memory, continual learning, interpretability, and alignment | 139--143, 145--149 | 01:03:52--01:13:02 |
| JEPA/world models and SSMs | 151--155 | 01:13:02--01:16:20 |

## Intentional omissions

| Slides | Reason |
|---|---|
| 1--10 | Cover, instructor biographies, sponsor acknowledgement, club promotion, course website, logistics, and audit rules. |
| 12, 34, 38, 67, 74, 83, 87, 95, 101, 108, 110, 113, 120, 126, 129, 138, 144, 150 | Pure section dividers represented by prose transitions. |
| 42, 51 | Paper title/author pages; provenance is preserved in the source audit and surrounding prose. |
| 73, 82, 119 | QR/contact pages without independent teaching claims. |
| 19, 54, 58, 61, 69, 116 | Repeated or progressive states superseded by the retained complete page. |
| 156 | Closing card without teaching content. |

## Status

- [x] Live V6 course row, video metadata, classroom/upload dates, speakers, runtime, resolution, cover, and manual captions verified.
- [x] Official 156-page deck downloaded, hashed, rendered, and reviewed page by page.
- [x] All 156 required/optional decisions completed: 116 required and 40 optional.
- [x] Complete five-second recording audit reviewed; no independent deck-external teaching visual found.
- [x] Fresh manual captions and deterministic transcript derivatives completed.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: all 116 required deck pages appear once.
- [x] Strict coverage passed with no warnings.
- [x] Stabilized double XeLaTeX passed and canonical PDF regenerated at 90 pages.
- [x] PDF visual QA signed after complete 90-page review in six enlarged contact-sheet segments and full-size inspection of dense preference/alignment tables and the final synthesis/reading pages.

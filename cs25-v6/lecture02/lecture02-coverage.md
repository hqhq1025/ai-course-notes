# Lecture 02 Coverage Matrix

## Coverage policy

- Canonical visual source: the official 55-page Stanford CS25 V6 deck.
- Required deck nodes: 47 independent teaching pages.
- Optional deck nodes: 8 cover, agenda, title/credit, divider, or closing pages.
- Required recording node: `images/frame-00-31-25.jpg`, the deck-external question card on object-representation fidelity and causal-graph recovery.
- Every required image must occur exactly once in `lecture02-notes.tex`.
- The complete 1:11:03 recording supplies required teacher voice and Q&A boundaries.

## Section mapping

| Note section | Required visual nodes | Teacher voice |
|---|---|---|
| World-model contract and JEPA | slides 3--9 | 00:01:52--00:10:17 |
| From patches to object-centric states | slides 12--18 | 00:10:17--00:16:30 |
| Causal-JEPA masking and action interface | slides 19--27 | 00:16:30--00:22:38 |
| Causal-JEPA evidence | slides 28--32 | 00:22:38--00:28:45 |
| Causal meaning and limits | slides 33--35; frame 00:31:25 | 00:28:45--00:34:51 |
| LeWorldModel and SIGReg | slides 37--43 | 00:34:51--00:42:59 |
| Latent control and systems evidence | slides 45--47 | 00:42:59--00:49:08 |
| Physics probes and latent geometry | slides 49--52 | 00:49:08--00:55:14 |
| Limitations, tooling, and Q&A | slides 53--54 | 00:55:14--01:10:59 |

## Intentional omissions

| Slides | Reason |
|---|---|
| 1 | Cover page; source metadata is preserved on the note cover and in the source audit. |
| 2 | Pure agenda represented by the note's teaching structure. |
| 10, 36 | Paper or speaker title cards without independent mechanisms. |
| 11 | Collaborator credits preserved in the source audit and prose. |
| 44, 48 | Pure section dividers represented by prose transitions. |
| 55 | Closing card without teaching content. |

## Status

- [x] Live V6 course row, video metadata, classroom/upload dates, speakers, runtime, resolution, cover, and manual captions verified.
- [x] Official 55-page deck downloaded, hashed, rendered, and reviewed page by page.
- [x] All 55 required/optional decisions completed: 47 required and 8 optional.
- [x] Complete five-second recording audit reviewed: 853 samples, 198 candidates, and one required deck-external teaching visual.
- [x] Lecture-snapshot Causal-JEPA v1 and LeWorldModel v1 verified against post-lecture revisions.
- [x] Fresh manual captions and deterministic transcript derivatives completed.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: 47 required deck pages and the 00:31:25 recording frame each appear once.
- [x] Strict coverage passed with no warnings.
- [x] Stabilized double XeLaTeX passed and canonical PDF regenerated at 51 pages with no overfull or underfull boxes.
- [x] PDF visual QA signed after complete 51-page review, five enlarged contact-sheet segments, and full-size inspection of dense result, table, Q\&A, and closing pages.

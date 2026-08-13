# Lecture 41 Coverage Matrix

## Coverage policy

- Canonical visual source: the complete 1:13:35 official Stanford Online recording, because the CS25 V5 page, video description, and speaker announcement do not link a standalone public deck.
- Candidate universe: 780 high-recall states from a full one-second scan of all 4,415 seconds with no brightness gate.
- Required nodes: 32 independent teaching slides or representative capability/evidence states.
- Optional nodes: 748 bumper, title, speaker-only, transition, loading, progressive, repeated, embedded-video micro-state, or Q\&A projector states.
- Every required image must occur exactly once in `lecture41-notes.tex`.
- The complete 00:54:10--01:13:20 Q\&A is required teacher voice even though it contributes almost no new independent visual state.

## Section mapping

| Note section | Required states | Teacher voice |
|---|---|---|
| Capability frontier and 2022--2024 transition | 064, 091, 112, 150, 155, 174, 175 | 00:01:13--00:11:19 |
| Representation and temporal compression | 177, 178, 181, 182, 185 | 00:11:19--00:19:45 |
| Flow Matching training and inference | 187, 188, 189 | 00:19:45--00:24:50 |
| Llama-style Transformer and Movie Gen architecture | 193, 194, 195, 196, 244 | 00:25:12--00:35:12 |
| Data curation and progressive training | 247, 250 | 00:35:20--00:41:11 |
| Learned visual world, editing, personalization, and audio | 257, 305, 337, 374, 388, 419 | 00:41:11--00:45:13 |
| Human evaluation and scaling evidence | 433, 434 | 00:45:13--00:49:20 |
| Failure boundary and future directions | 460, 464 | 00:49:20--00:54:04 |
| Q\&A engineering and evidence boundaries | no new visual | 00:54:10--01:13:20 |

## Intentional omissions

| Candidate states | Reason |
|---|---|
| 001--047 | Stanford bumper, repeated title, host introduction, and speaker-only opening; note metadata and teacher voice preserve the useful context. |
| 048--144 except 064, 091, 112 | Progressive frames inside three opening demos; the retained states preserve generation quality, difficult reflection, and instruction-based editing without dumping every video frame. |
| 145--169 except 150, 155 | Progressive comparison playback, loading states, transitions, and speaker-only interlude. |
| 170--252 except listed required states | Personal biography, repeated agenda cards, incremental builds, duplicate architecture states, and speaker-only frames; final complete teaching states are retained. |
| 253--432 except listed required states | Hundreds of micro-states inside six embedded videos; representative states preserve physical interaction, editing, personalization, and audio evidence. |
| 433--466 except 433, 434, 460, 464 | Progressive result/failure playback, acknowledgement slide, and repeated future-direction state. |
| 467--780 | Q\&A is visually speaker-only or revisits earlier slides; every substantive answer is retained in the teacher-voice ledger and prose. |

## Status

- [x] Official course row, lecture date, upload date, speaker, runtime, resolution, cover, and manual captions verified.
- [x] Course page, video description, and speaker announcement checked; no standalone public deck is linked.
- [x] Movie Gen primary paper downloaded and hash recorded for formula and system-detail verification.
- [x] Full one-second audit and all 780 required/optional decisions completed.
- [x] Fresh manual captions and derived transcript artifacts completed.
- [x] Legacy thin-note, missing canonical URL, one-figure coverage, and rolling-caption defects documented.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: all 32 required states appear once.
- [x] Strict coverage passed with no warnings.
- [x] Stabilized double XeLaTeX passed and canonical PDF regenerated at 37 pages.
- [x] PDF visual QA signed after complete contact-sheet review, three enlarged contact-sheet segments, and full-size inspection of the editing, personalization/audio, terminology, and closing pages.

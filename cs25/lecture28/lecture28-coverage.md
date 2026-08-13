# Lecture 28 Coverage Matrix

## Coverage policy

- Required nodes: 67 official teaching pages from the 77-page deck.
- Optional nodes: 10 pages limited to pure dividers, empty/superseded builds, a QR-only atlas state, and the closing contact card.
- Every required image must occur exactly once in `lecture28-notes.tex`.

## Section mapping

| Note section | Official nodes | Teacher voice |
|---|---|---|
| Historical spine and RLHF motivation | 001, 003, 005--012, 014--015 | 00:00:34--00:08:59 |
| Atlas, base/aligned models, definitions | 017, 019--027 | 00:09:20--00:12:30 |
| First open instruct models | 029--040 | 00:13:42--00:24:47 |
| QLoRA and accessibility | 041--043, 045 | 00:24:56--00:28:45 |
| Safety and transition ecosystem | 046--048 | 00:28:55--00:32:14 |
| Evaluation infrastructure | 049--057 | 00:32:14--00:39:45 |
| RLHF, reward modeling, and DPO | 059--066 | 00:40:00--00:46:20 |
| Preference-optimization model releases | 067--069 | 00:46:33--00:49:35 |
| Modern ecosystem and directions | 071--076 | 00:50:00--01:03:48 |
| Q&A extension | no independent slide | 01:04:49--01:15:29 |

## Intentional omissions

| Node | Reason |
|---|---|
| 002 | Pure history section divider. |
| 004 | Empty timeline build superseded by later milestone pages. |
| 013 | Progressive RLHF-adoption build superseded by pages 14 and 15. |
| 016 | QR-only atlas build superseded by page 17. |
| 018 | Empty chapter-atlas build superseded by pages 19--23. |
| 028, 044, 058, 070 | Pure chapter dividers; surrounding prose and atlas pages preserve transitions. |
| 077 | Closing thanks/contact card without independent teaching content. |

## Status

- [x] Canonical video, manual subtitles, official deck, and companion collection verified.
- [x] Incorrect Lecture 27 deck contamination removed.
- [x] Required/optional page selection completed.
- [x] Teacher-voice ledger completed.
- [x] Required figures inserted exactly once: 67/67, no duplicates, no optional-page leakage.
- [x] Strict coverage passed with zero warnings.
- [x] Double XeLaTeX passed; no overfull, reference, rerun, or hyperref warnings remain. Only repository-standard Fandol notices and one harmless underfull table cell remain.
- [x] PDF visual QA signed after contact-sheet review and full-size spot checks.

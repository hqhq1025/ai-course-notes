# Lecture 31 Coverage Matrix

## Coverage policy

- Required nodes: 31 independent teaching states recovered from the official 1920x1080 recording.
- Optional nodes: opening/ending Stanford bumpers, three pure chapter dividers, and the closing thanks/contact card.
- Repeated one-second candidates, transition blends, and changing frames inside the embedded video demo are one visual state unless they teach a distinct step.
- Q&A introduces no new slide state; its spoken clarifications remain required teacher voice.
- Every required image must occur exactly once in `lecture31-notes.tex`.

## Section mapping

| Note section | Required states | Teacher voice |
|---|---|---|
| Source boundary and roadmap | 002--003 | 00:02:31--00:04:35 |
| Three LLM moments | 004--006 | 00:05:00--00:13:18 |
| Architecture and systems | 008--011 | 00:13:18--00:24:27; Q&A 01:08:10--01:10:30 |
| Alignment and the data thesis | 012--014 | 00:25:00--00:34:20; Q&A 01:10:30--01:12:30 |
| VLM architectures | 016--024 | 00:35:00--00:44:19; Q&A 01:15:00--01:16:15 |
| Image generation objectives | 026--032 | 00:45:00--00:57:54; Q&A 01:12:30--01:15:00 |
| Video and research agenda | 033--035 | 00:57:54--01:08:10; Q&A 01:16:15--01:19:59 |

## Intentional omissions

| State | Reason |
|---|---|
| 001, 037 | Stanford Engineering bumpers without teaching content. |
| 007, 015, 025 | Pure section-divider slides; their chapter transitions are represented in prose. |
| 036 | Closing thanks/contact card; stable source links are retained in source materials. |
| Duplicate candidates | Repeated shares, transition blends, and changing embedded-video frames do not add independent teaching content. |

## Status

- [x] Canonical course page, official recording, manual captions, and 1080p source verified.
- [x] Legacy 2026 date and unsupported engineering-governance framing identified.
- [x] One-second high-recall slide audit and required/optional selection completed.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: 31 required assets, 31 figure uses, 31 unique paths.
- [x] Strict coverage passed with zero warnings.
- [x] Double XeLaTeX passed; only standard Fandol font notices remain.
- [x] PDF visual QA signed after full contact-sheet review and enlarged inspection of systems tables, preference formulas, VLM comparisons, GUI trace, diffusion pages, research matrix, self-test, and final references.

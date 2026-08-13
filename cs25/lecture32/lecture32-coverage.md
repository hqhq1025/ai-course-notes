# Lecture 32 Coverage Matrix

## Coverage policy

- Canonical visual source: 71-page official speaker deck exported from the Google Slides link on Loubna Ben Allal's official site.
- Required nodes: 58 teaching pages.
- Optional nodes: pure question/section dividers, intermediate animation builds, one exact FineWeb duplicate, completion checkmarks, and the closing thank-you slide.
- All 71 pages are rendered and retained under `slides-images/`; every required page must occur exactly once in `lecture32-notes.tex`.
- Teacher voice from the official manual captions remains required even when the deck is complete.

## Section mapping

| Note section | Required slides | Teacher voice |
|---|---|---|
| Open models and transparency | 1--7, 11 | 00:00:50--00:06:20 |
| Scaling laws and lifecycle cost | 13--23 | 00:06:20--00:13:20 |
| Data sources | 26--27, 29--36 | 00:13:20--00:24:20 |
| General filtering experiments | 39--40, 42--43 | 00:24:20--00:30:00 |
| The Stack/StarCoder pipeline | 44--52 | 00:30:00--00:40:00 |
| Code-model ecosystem | 55--60 | 00:38:30--00:43:10 |
| Responsible release | 61--63 | 00:43:10--00:45:10 |
| Evaluation and tooling | 64--70 | 00:44:20--00:52:40 |
| Q&A extensions | no independent slides | 00:52:40--01:01:30 |

## Intentional omissions

| Slides | Reason |
|---|---|
| 8, 12, 25, 38, 54 | Pure question/section dividers represented by prose transitions. |
| 9--10 | Intermediate builds; slide 11 is the complete state. |
| 24, 37, 53 | Completion checkmarks without new teaching content. |
| 28 | FineWeb branding/title card without independent mechanism. |
| 41 | Exact teaching duplicate of slide 29. |
| 71 | Closing thank-you slide. |

## Status

- [x] Official course page, recording, speaker page, manual captions, and 71-page deck verified.
- [x] Legacy missing video/source attribution and thumbnail-only coverage identified.
- [x] All deck pages rendered; required/optional selection completed.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: 58 required slide assets, 58 figure uses, 58 unique paths.
- [x] Strict coverage passed with zero warnings.
- [x] Double XeLaTeX passed; only standard Fandol font notices remain.
- [x] PDF visual QA signed after full contact-sheet review and enlarged inspection of scaling-law curves, FineWeb filtering results, The Stack pipelines, near-deduplication evidence, responsible-release material, benchmark pages, self-test, and final references.

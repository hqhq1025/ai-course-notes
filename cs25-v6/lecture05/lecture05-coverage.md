# Lecture 05 Coverage Matrix

## Coverage policy

- Canonical visual source: 44 states reconstructed from the official Stanford Online recording because the course-page slide link incorrectly points to Lecture 04.
- Required visual nodes: 41 independent teaching states.
- Optional visual nodes: slides 1, 13, and 22, which are title/divider cards represented by the cover and prose transitions.
- Every required slide must occur exactly once in `lecture05-notes.tex`.
- Prepared talk: approximately 00:00:48--00:49:30. Final Q&A: approximately 00:49:30--00:57:50.
- Primary-paper language is frozen to the 2026-04-30 lecture snapshot: two-phase v1, front-loading v1, and RLP v2.

## Section mapping

| Note section | Required visual nodes | Teacher voice |
|---|---|---|
| Learning recipe and comparison lens | slides 2--5 | 00:00:48--00:06:27 |
| Data frontier and optimal blends | slides 6--9 | 00:06:40--00:09:29 |
| Two-phase curriculum | slides 10--12 | 00:09:29--00:12:32 |
| Front-loading setup and evaluation design | slides 14--16 | 00:12:39--00:15:48 |
| Five front-loading lessons | slides 17--21 | 00:15:48--00:21:48 |
| Mid-talk data and curriculum Q&A | no new required visual | 00:22:00--00:27:58 |
| RLP motivation and standard-pretraining gap | slides 23--25 | 00:28:14--00:32:34 |
| RLP mechanism | slides 26--32 | 00:32:34--00:36:31 |
| Qwen and Nemotron evaluation | slides 33--37 | 00:36:31--00:42:20 |
| Early-reasoning literature and RPT comparison | slides 38--40 | 00:42:20--00:45:56 |
| Ablations and integrated recipe | slides 41--44 | 00:45:56--00:49:30 |
| Final Q&A and limitations | no new required visual | 00:49:30--00:57:50 |

## Intentional omissions

| Slide | Reason |
|---|---|
| 1 | Talk title card; title, speaker, date, course, recording URL, and visual-source mode are preserved on the cover and in the source manifest. |
| 13 | `Front-Loading Reasoning` divider; the section transition and first mechanism figure preserve its teaching role. |
| 22 | `RLP` divider; the section transition and Tale of Two Learners figure preserve its teaching role. |

## Status

- [x] Live Stanford course row, official recording, classroom/upload dates, speaker, runtime, resolution, and manual captions verified.
- [x] Confirmed that the Lecture 05 course-page slide URL duplicates the Lecture 04 Ultra-Scale deck and must not be used.
- [x] English manual captions refreshed and deterministic transcript derivatives generated.
- [x] Complete five-second recording audit and 12-sheet timeline review completed.
- [x] All 44 required/optional visual decisions frozen: 41 required and three optional.
- [x] Two-phase v1, front-loading v1, RLP v2, Quiet-STaR, RPT, and RLPT verified against the lecture date.
- [x] Teacher-voice ledger completed with prepared-talk, mid-talk Q&A, and final Q&A rows.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once.
- [x] Strict coverage passes with no hard errors or warnings.
- [x] Quality script reports `⭐⭐⭐`.
- [x] Stable double XeLaTeX passes with no overfull or underfull boxes.
- [x] Full PDF visual QA is signed.

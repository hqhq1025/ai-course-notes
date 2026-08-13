# Lecture 38 Coverage Matrix

## Coverage policy

- Canonical visual source: the complete 1:12:32 official Stanford Online recording because no standalone public deck is linked.
- Candidate universe: 357 high-recall states from a full one-second scan of all 4,352 seconds.
- Required nodes: 62 independent teaching states.
- Optional nodes: 295 opening bumper, speaker-only, transition, repeated, progressive, or live-browser micro-states.
- Every required image must occur exactly once in `lecture38-notes.tex`.
- The 01:08:27--01:12:26 discussion remains required teacher voice even though it introduces no independent visual state after the further-reading slide.

## Section mapping

| Note section | Required figures | Teacher voice |
|---|---|---|
| Biology analogy and behavioral paradoxes | 01--04 | 00:01:41--00:08:19 |
| One-token computation and “grown, not built” | 05--09 | 00:08:22--00:10:20 |
| Features, CLTs, attribution graphs, and interventions | 10--24 | 00:11:38--00:30:52 |
| Medical and multilingual abstract representations | 25--31 | 00:31:52--00:47:26 |
| Parallel addition and metacognitive mismatch | 32--43 | 00:49:58--00:58:54 |
| Hallucinations and jailbreak competition | 44--52 | 00:58:54--01:04:45 |
| Poetry planning and chain-of-thought unfaithfulness | 53--61 | 01:04:48--01:09:54 |
| Method limits, mitigation tradeoffs, and open questions | 62 | 01:09:54--01:12:26 |

## Intentional omissions

| Candidate states | Reason |
|---|---|
| 001--036 and non-teaching intro frames | Stanford bumper, host logistics, speaker-only footage, and title builds; the complete title state is retained once. |
| 084, 086, 094--095, 101--104, and 107 | Duplicate or progressive builds; the final readable state preserves the independent teaching point. |
| 109--126, 145--163, 174--233, 305--353, and 356--357 | Speaker-only, transitions, cursor motion, or Q&A footage without independent visual content. Spoken teaching is retained in the ledger and prose. |
| 130, 132, 135--144 except 138 | Repeated attribution-graph exploration states; overview, a representative routed path, and the prose workflow preserve the distinct mechanism. |
| 234--247 | Live scrolling through the interactive article. Method details are retained through the canonical article source and selected readable lecture states rather than every browser viewport. |
| 249, 253, 257--258, 261--263, 265--266, and 269 | Duplicates, article scroll increments, or lower-information builds around the retained addition states. |
| 271, 274, 277--279, 281, 284, 286, 292, 295, 297, and 299 | Repeated section cards or progressive builds; the complete comparison/intervention state is retained. |
| 301--304 and 354--355 | Q&A returns to already-retained chain-of-thought and further-reading slides; no new visual evidence. |

## Status

- [x] Official video, classroom date, upload date, speaker, runtime, resolution, cover, and manual captions verified.
- [x] Course page and linked materials checked; no standalone public deck is linked.
- [x] Exhaustive one-second audit and all 357 required/optional decisions completed.
- [x] Fresh manual captions and derived transcript artifacts completed.
- [x] Legacy thin-note and rolling-subtitle defects documented.
- [x] Teacher-voice ledger completed.
- [x] Coverage blueprint completed before prose writing.
- [x] Required figures inserted exactly once: all 62 required teaching states appear once.
- [x] Strict coverage passed with no warnings.
- [x] Double XeLaTeX passed and canonical PDF regenerated at 48 pages.
- [x] PDF visual QA signed after full contact-sheet review and full-size inspection of pages 7, 16, 31, 43, and 48.

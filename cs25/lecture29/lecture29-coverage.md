# Lecture 29 Coverage Matrix

## Coverage policy

- Required nodes: 26 independent teaching states recovered from the official 1920x1080 recording.
- Optional nodes: 17 states limited to the Stanford bumper, pure dividers, the closing card, and superseded progressive builds.
- Q&A screen-sharing after the main talk repeats existing slides and adds no independent visual state; its spoken content remains required teacher voice.
- Every required image must occur exactly once in `lecture29-notes.tex`.

## Section mapping

| Note section | Required states | Teacher voice |
|---|---|---|
| Source framing and dense baseline | 003, 007--009 | 00:01:04--00:07:01 |
| MoE lineage and routing mechanism | 010, 012--014 | 00:07:01--00:09:38 |
| Mixtral overview and performance | 015, 018--020 | 00:09:38--00:12:38 |
| Architecture and systems myths | 021--025, 028 | 00:12:38--00:19:15 |
| Routing interpretation | 030, 032--034, 037, 040--042 | 00:19:15--00:29:47 |
| Q&A engineering synthesis | no independent visual state | 00:31:45--01:04:14 |

## Intentional omissions

| State | Reason |
|---|---|
| 001 | Stanford Engineering bumper without teaching content. |
| 002 | Partial content build superseded by state 003. |
| 004 | Pure architecture divider. |
| 005--006 | GQA/SWA progressive builds superseded by state 007. |
| 011 | Blank MoE-layer divider. |
| 016--017 | MLP-hypothesis progressive builds superseded by state 018. |
| 026--027 | Compression progressive builds superseded by state 028. |
| 029 | Pure interpretation divider. |
| 031 | Domain-experiment setup superseded by state 032. |
| 035--036 | Myth-4 progressive builds superseded by state 037. |
| 038--039 | Treasure-hunt progressive builds superseded by state 040. |
| 043 | Closing thanks card without independent teaching content. |

## Status

- [x] Canonical course page, official recording, automatic subtitles, and 1080p source verified.
- [x] Incorrect Lecture 28 deck contamination removed.
- [x] One-second high-recall slide audit and required/optional selection completed.
- [x] Teacher-voice ledger completed.
- [x] Required figures inserted exactly once: 26/26, no duplicates and no optional-state leakage.
- [x] Strict coverage passed with zero warnings.
- [x] Double XeLaTeX passed; no overfull, reference, rerun, or hyperref warnings remain. Only repository-standard Fandol notices remain.
- [x] PDF visual QA signed after complete contact-sheet review and enlarged critical-page inspection.

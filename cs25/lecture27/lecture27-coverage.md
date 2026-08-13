# Lecture 27 Coverage Matrix

## Coverage policy

- Required nodes: 66 official teaching pages from the two decks.
- Optional nodes: 21 pages limited to the closing card, pure divider, empty scaffold, or redundant progressive builds.
- Every required image must occur exactly once in `lecture27-notes.tex`.

## Section mapping

| Note section | Official nodes | Teacher voice |
|---|---|---|
| Source framing and shared method | J001--J003, H001--H004, H006 | 00:00:55--00:02:32; 00:32:29--00:36:21 |
| Massive multi-task learning | J004--J007 | 00:02:38--00:08:51 |
| Scaling and emergence | J008--J015 | 00:08:58--00:19:24; 00:28:29--00:30:21 |
| Inverse scaling and research curves | J016--J019 | 00:19:34--00:25:51 |
| Compute and the Bitter Lesson | H007--H016 | 00:37:29--00:44:59 |
| Architecture foundations | H017--H028, H032, H037 | 00:45:42--00:54:03 |
| Four-step transformation | H040--H051 | 00:54:03--00:57:32 |
| Inductive-bias case studies | H052--H067 | 00:57:32--01:06:42 |
| Q&A extension | no independent slide | 01:12:39--01:16:54 |

## Intentional omissions

| Node | Reason |
|---|---|
| J020 | Closing contact card without independent teaching content. |
| H005 | Progressive duplicate; H006 is the final complete prediction-difficulty plot. |
| H011--H012 | Progressive builds; H013 preserves the complete compute-regime comparison. |
| H019--H020 | Tokenization/embedding builds; H021 preserves the complete sequence-model pipeline. |
| H024, H026 | Incremental encoder-decoder builds whose claims are retained by H022, H023, H025, H027, and H028. |
| H029--H031 | Encoder-only progressive builds; H032 is the complete annotated state. |
| H033--H036 | Decoder-only progressive builds; H037 is the complete annotated state. |
| H038 | Pure section divider. |
| H039 | Empty comparison table populated in H042, H045, H048, and H051. |
| H043, H046, H049 | Repeated architecture states between transformation steps. |
| H065 | First half of the chat-attention build; H066 contains the complete bidirectional/unidirectional comparison. |

## Status

- [x] Canonical video and speaker boundary verified.
- [x] Two official decks verified and rendered.
- [x] Manual subtitles normalized.
- [x] Required/optional visual selection completed.
- [x] Teacher-voice ledger completed.
- [x] Required figures inserted exactly once: 66/66, no duplicates, no optional-page leakage.
- [x] Strict coverage passed with zero warnings.
- [x] Double XeLaTeX passed; only repository-standard Fandol font notices remain.
- [x] PDF visual QA signed after contact-sheet review and full-size spot checks.

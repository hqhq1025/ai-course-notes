# Source Manifest: `cs25/lecture12`

## Files

- `cover.jpg`
- `lecture12.en.srt`
- `lecture12-notes.tex`
- `metadata.json`
- `transcript_clean.txt`
- `transcript_timed.txt`

## Supplementary Source Materials

- `source-materials/SOURCES.md`
- `lecture12-teacher-voice-ledger.md`
- `lecture12-blueprint.md`
- `lecture12-coverage.md`

## Local Visual Assets

- 17 manually reviewed teaching states in `slides-images/`, recovered from the official 1080p recording because no standalone slide PDF was exposed by the official description or course archive.
- The slide talk ends near 00:30:54. The remaining classroom Q&A is represented by text nodes because the recording continues to display the same final slide.

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | slide | yes | `official video 00:00:23--00:00:49` | `slides-images/slide-01-title.jpg` |
| V002 | slide | yes | `official video 00:00:49--00:03:18` | `slides-images/slide-02-team-ai-strong-players.jpg` |
| V003 | slide | yes | `official video 00:03:18--00:04:16` | `slides-images/slide-03-two-objectives.jpg` |
| V004 | slide | yes | `official video 00:04:16--00:05:31` | `slides-images/slide-04-follow-human-intent.jpg` |
| V005 | slide | yes | `official video 00:05:31--00:06:35` | `slides-images/slide-05-explicit-implicit-intent.jpg` |
| V006 | slide | yes | `official video 00:06:35--00:07:55` | `slides-images/slide-06-rlhf-reward-model.jpg` |
| V007 | slide | yes | `official video 00:07:55--00:09:24` | `slides-images/slide-07-rlhf-full-loop.jpg` |
| V008 | slide | yes | `official video 00:09:24--00:15:18` | `slides-images/slide-08-instructgpt-preferences.jpg` |
| V009 | slide | yes | `official video 00:15:18--00:19:05` | `slides-images/slide-09-instructgpt-training-costs.jpg` |
| V010 | slide | yes | `official video 00:19:05--00:20:19` | `slides-images/slide-10-chatgpt-lessons.jpg` |
| V011 | slide | yes | `official video 00:20:19--00:20:32` | `slides-images/slide-11-evaluation-title.jpg` |
| V012 | slide | yes | `official video 00:20:32--00:22:25` | `slides-images/slide-12-evaluation-easier-examples.jpg` |
| V013 | slide | yes | `official video 00:22:25--00:25:30` | `slides-images/slide-13-scaling-human-supervision.jpg` |
| V014 | slide | yes | `official video 00:25:30--00:26:38` | `slides-images/slide-14-critiques-and-dialog.jpg` |
| V015 | slide | yes | `official video 00:26:38--00:28:57` | `slides-images/slide-15-measuring-progress.jpg` |
| V016 | slide | yes | `official video 00:28:57--00:29:45` | `slides-images/slide-16-summarization-critiques-results.jpg` |
| V017 | slide | yes | `official video 00:29:45--00:30:54` | `slides-images/slide-17-machines-vs-humans.jpg` |
| T001 | text | optional | `transcript_timed.txt` | Team AI gets stronger players while humans still choose which systems join. |
| T002 | text | optional | `transcript_timed.txt` | Alignment recruits AI to Team Human; governance writes the game rules. |
| T003 | text | optional | `transcript_timed.txt` | The lecture covers alignment rather than governance. |
| T004 | text | optional | `transcript_timed.txt` | Current-model alignment and future scalable alignment are separate buckets. |
| T005 | text | optional | `transcript_timed.txt` | Explicit intent is only a subset of what users actually mean. |
| T006 | text | optional | `transcript_timed.txt` | The slide omits SFT for simplicity. |
| T007 | text | optional | `transcript_timed.txt` | Labelers disagree and the reward model aggregates preferences. |
| T008 | text | optional | `transcript_timed.txt` | Reward models amortize the cost of human comparisons. |
| T009 | text | optional | `transcript_timed.txt` | A 100x-smaller aligned model can win human preference on the paper distribution. |
| T010 | text | optional | `transcript_timed.txt` | PPO-ptx mitigates regressions by mixing pretraining data. |
| T011 | text | optional | `transcript_timed.txt` | PPO was familiar and worked reasonably well, not proven optimal. |
| T012 | text | optional | `transcript_timed.txt` | Human comparisons commonly rank a small response set. |
| T013 | text | optional | `transcript_timed.txt` | Fine-tuning compute is tiny relative to pretraining; feedback labor is not. |
| T014 | text | optional | `transcript_timed.txt` | Behavioral cloning can imitate the wrong human limitations. |
| T015 | text | optional | `transcript_timed.txt` | January 2023 ChatGPT still hallucinates and is prompt-sensitive. |
| T016 | text | optional | `transcript_timed.txt` | Evaluation can be easier than generation. |
| T017 | text | optional | `transcript_timed.txt` | Human evaluation capability does not automatically scale with model capability. |
| T018 | text | optional | `transcript_timed.txt` | Optimizing against weak feedback can reward persuasion or deception. |
| T019 | text | optional | `transcript_timed.txt` | AI can transform a global audit into checking a concrete alleged flaw. |
| T020 | text | optional | `transcript_timed.txt` | Critiques, dialogue, explanations, fact checks, and quotes are assistance modes. |
| T021 | text | optional | `transcript_timed.txt` | Hard real tasks usually lack ground truth. |
| T022 | text | optional | `transcript_timed.txt` | Targeted perturbations create a known good/bad pair. |
| T023 | text | optional | `transcript_timed.txt` | Critique assistance finds roughly 50 percent more flaws in the experiment. |
| T024 | text | optional | `transcript_timed.txt` | Many critiques are garbage or nitpicking and summarization is comparatively easy. |
| T025 | text | optional | `transcript_timed.txt` | Discriminator--critique gap measures knowledge not surfaced as critique. |
| T026 | text | optional | `transcript_timed.txt` | Machines do cognitive labor; humans communicate preferences. |
| T027 | text | optional | `transcript_timed.txt` | Uncertainty calibration remains immature. |
| T028 | text | optional | `transcript_timed.txt` | Do not train naively on arbitrary public interface feedback. |
| T029 | text | optional | `transcript_timed.txt` | Labeler pools poorly represent diverse human preferences. |
| T030 | text | optional | `transcript_timed.txt` | Preference drift and model updates create prompt-compatibility costs. |
| T031 | text | optional | `transcript_timed.txt` | Browsing and APIs improve verification while expanding the safety boundary. |
| T032 | text | optional | `transcript_timed.txt` | Exact ChatGPT training quantities were not public. |
| T033 | text | optional | `transcript_timed.txt` | Trusted outer signals may reduce some inner alignment concerns to distribution shift. |
| T034 | text | optional | `transcript_timed.txt` | Self-critique still needs a trusted ground-truth signal. |
| T035 | text | optional | `transcript_timed.txt` | Interpretability may be neither sufficient nor necessary and can induce selection effects. |

## Existing Note

- `lecture12-notes.tex` is a legacy 195-line draft that imports post-lecture Superalignment and generic deployment material. It must be fully replaced rather than patched.

## Generation Contract

- Review every visual and teacher-voice node; all 17 teaching slides are required exactly once.
- Preserve the 2023-01-17 evidence boundary and distinguish slide claims, spoken judgments, and primary-paper clarification.
- Every non-summary section/subsection starts with a prose bridge before figures, tables, formulas, or code.
- Dense figures receive setup, reading guidance, evidence interpretation, and a statement of what they do not prove.
- Final PDF must pass strict coverage, `⭐⭐⭐` quality, stable two-pass XeLaTeX, and visual QA.

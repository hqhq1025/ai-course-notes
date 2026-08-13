# Source Manifest: CS25 Lecture 04

Access date: 2026-08-11.

## Files

- `cover.jpg`: Stanford Online official thumbnail.
- `metadata.json`: sanitized stable video metadata.
- `lecture04.en.srt`: official manual English (`en-US`) captions, 1,516 parsed cues.
- `transcript_timed.txt`: timestamp-preserving transcript.
- `transcript_clean.txt`: five-minute transcript digest for source review.
- `lecture04.mp4`: local ignored 1080p official recording used for slide recovery.
- `slides-images/`: 24 reviewed teaching slides or final progressive-build states.

## Supplementary Source Materials

- `source-materials/SOURCES.md`: official course/video sources, primary papers, code, and source-boundary notes.
- `lecture04-teacher-voice-ledger.md`: motivations, warnings, Q&A clarifications, and their planned placement.
- `lecture04-blueprint.md`: teaching thesis and section plan.
- `lecture04-coverage.md`: source-node treatment matrix.

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| V001 | figure | yes | official video 00:06 | `slides-images/slide-01-title.jpg` |
| V002 | figure | yes | official video 01:40 | `slides-images/slide-02-transformers-for-sequential-data.jpg` |
| V003 | figure | yes | official video 02:20 | `slides-images/slide-03-scalable-models-stable-training.jpg` |
| V004 | figure | yes | official video 03:10 | `slides-images/slide-04-sequential-data-to-sequential-decision.jpg` |
| V005 | figure | yes | official video 04:00 | `slides-images/slide-05-background-reinforcement-learning.jpg` |
| V006 | figure | yes | official video 05:20 | `slides-images/slide-06-background-offline-rl.jpg` |
| V007 | figure | yes | official video 07:00 | `slides-images/slide-07-motivating-challenge-rl-does-not-scale.jpg` |
| V008 | figure | yes | official video 12:56 | `slides-images/slide-08-decision-transformer-architecture.jpg` |
| V009 | figure | yes | official video 14:56 | `slides-images/slide-09-forward-pass.jpg` |
| V010 | figure | yes | official video 17:24 | `slides-images/slide-10-forward-pass-code.jpg` |
| V011 | figure | yes | official video 23:40 | `slides-images/slide-11-loss-function.jpg` |
| V012 | figure | yes | official video 24:58 | `slides-images/slide-12-rollouts.jpg` |
| V013 | figure | yes | official video 30:00 | `slides-images/slide-13-rl-as-probabilistic-inference.jpg` |
| V014 | figure | yes | official video 32:24 | `slides-images/slide-14-experiments-divider.jpg` |
| V015 | figure | yes | official video 33:24 | `slides-images/slide-15-offline-rl-summary-results.jpg` |
| V016 | figure | yes | official video 38:12 | `slides-images/slide-16-evaluating-return-conditioning.jpg` |
| V017 | figure | yes | official video 47:34 | `slides-images/slide-17-comparison-with-behavior-cloning.jpg` |
| V018 | figure | yes | official video 53:06 | `slides-images/slide-18-effect-of-context-length.jpg` |
| V019 | figure | yes | official video 55:12 | `slides-images/slide-19-sparse-reward-environments.jpg` |
| V020 | figure | yes | official video 1:00:04 | `slides-images/slide-20-long-term-credit-assignment.jpg` |
| V021 | figure | yes | official video 1:03:02 | `slides-images/slide-21-decision-transformers-as-critics.jpg` |
| V022 | figure | yes | official video 1:08:56 | `slides-images/slide-22-summary.jpg` |
| V023 | figure | yes | official video 1:10:46 | `slides-images/slide-23-future-work.jpg` |
| V024 | figure | yes | official video 1:11:30 | `slides-images/slide-24-useful-links.jpg` |
| O001 | figure | no | official video 00:00--00:05 | Stanford Engineering bumper and repeated title transitions. |
| O002 | figure | no | official video 00:38--01:40 | Progressive builds of the same sequential-data slide; final complete state retained as V002. |
| O003 | figure | no | official video 05:40--07:00 | Progressive motivation bullets; final complete state retained as V007. |
| O004 | figure | no | official video 11:18--13:22 | Repeated animation cycle of the Decision Transformer diagram; final complete state retained as V008. |
| O005 | figure | no | official video 14:40--30:00 | Intermediate bullet builds and repeated code toggles; final teaching states retained as V009--V012. |
| O006 | figure | no | official video 32:32--49:56 | Repeated experiment slides during Q&A; final versions retained as V015--V017. |
| O007 | figure | no | official video 1:11:42 | Administrative “Questions?” page. |
| O008 | figure | no | official video 1:12:18--1:20:37 | Q&A navigation back to already retained slides plus end bumper. |
| T001 | text | no | transcript 00:35--03:13 | Stable scaling in perception motivates a unified model that also makes decisions. |
| T002 | text | no | transcript 03:13--07:00 | Offline RL removes trial-and-error interaction but exposes a scale and stability gap. |
| T003 | text | no | transcript 07:00--13:22 | Return-to-go is the control token; reward, state, and action form one causal sequence. |
| T004 | text | no | transcript 14:40--20:00 | Addition versus concatenation, timestep embeddings, and deliberately non-Markov conditioning. |
| T005 | text | no | transcript 20:00--24:16 | Partial observability and data-collection policy determine what the offline learner can infer. |
| T006 | text | no | transcript 23:34--30:02 | Supervised MSE/CE objectives replace Bellman-style dynamic programming; rollout decrements target return. |
| T007 | text | no | transcript 30:00--38:12 | RL-as-inference explains optimality variables and the difference between requested and realized return. |
| T008 | text | no | transcript 38:12--45:00 | Return conditioning can select behaviors, but extreme targets saturate and “multitask” needs qualification. |
| T009 | text | no | transcript 45:03--50:00 | Percent behavior cloning is a strong baseline; Decision Transformer separates most clearly in low-data regimes. |
| T010 | text | no | transcript 50:00--55:12 | Context length ablation tests whether history, rather than only current state, drives performance. |
| T011 | text | no | transcript 55:12--1:00:04 | Sparse reward removes dense feedback; return-to-go exposes future success but does not solve exploration. |
| T012 | text | no | transcript 1:00:04--1:05:03 | The same causal model can act as a critic by predicting return probability through Key-to-Door phases. |
| T013 | text | no | transcript 1:05:03--1:11:30 | Closing synthesis emphasizes simplicity, stability, multimodality, multitask and multi-agent extensions. |
| T014 | text | no | transcript 1:11:42--1:16:36 | Online RL is not obtained by naively adding epsilon-greedy or Boltzmann sampling. |
| T015 | text | no | transcript 1:16:36--1:18:22 | Discounting remains compatible; finite context may still be insufficient for long-horizon credit. |
| T016 | text | no | transcript 1:18:22--1:20:37 | CQL-style pessimism or Q-learning losses may be useful, but the original work intentionally tests conceptual simplicity. |
| P001 | reference | no | Chen et al. 2021 | Decision Transformer: Reinforcement Learning via Sequence Modeling. |
| P002 | reference | no | Janner et al. 2021 | Offline Reinforcement Learning as One Big Sequence Modeling Problem. |
| P003 | reference | no | Kumar et al. 2020 | Conservative Q-Learning for Offline Reinforcement Learning. |
| P004 | reference | no | Fu et al. 2020 | D4RL: Datasets for Deep Data-Driven Reinforcement Learning. |
| P005 | reference | no | Levine 2018 | Reinforcement Learning and Control as Probabilistic Inference. |
| P006 | reference | no | official project/code | Decision Transformer project page and GitHub implementation. |

## Existing Note

- `lecture04-notes.tex` is a thin legacy note and will be replaced wholesale.

## Generation Contract

- Review every required visual node and place it where its idea is taught.
- Use the final complete state for progressive builds and retain intermediate states only when they teach a distinct operation.
- Preserve teacher voice in normal prose and explicit `课堂提示` / `老师强调` / `讲义提醒` / `实践经验` blocks.
- Explain requested return versus realized environmental return, dataset support, extrapolation saturation, and the online-RL limitation.
- Every important figure needs setup, a `读图` treatment, and a follow-up connection.
- Final PDF must pass strict coverage, `⭐⭐⭐` quality, two-pass XeLaTeX, and manual visual QA.

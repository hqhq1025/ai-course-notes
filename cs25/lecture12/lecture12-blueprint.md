# CS25 Lecture 12 Blueprint

## Teaching thesis

The lecture is not a survey of every alignment proposal. It builds one argument: RLHF can turn implicit human preferences into a useful training signal for current language models, but the method stops scaling when unaided humans can no longer reliably evaluate model behavior. The proposed next step is to use AI systems to amplify human evaluation while keeping humans responsible for preference judgments.

## Planned structure

| Section | Core question | Required visual nodes | Teacher-voice nodes | Formal treatment |
|---|---|---|---|---|
| 1. Source boundary and Team AI | Why is alignment framed as recruiting capable systems, and what is outside the lecture? | V001--V003 | T001--T003 | Alignment/governance distinction table. |
| 2. Human intent | Why are explicit instructions insufficient? | V004--V005 | T004--T005 | Explicit/implicit objective decomposition. |
| 3. RLHF mechanism | How do comparisons become a policy update? | V006--V007 | T006--T013 | SFT--RM--RL pipeline, Bradley--Terry loss, KL-regularized objective, pseudocode. |
| 4. InstructGPT and ChatGPT | What did alignment buy, what did it cost, and what remained broken? | V008--V010 | T014--T018 | Preference probability, cost accounting, SFT/RL comparison. |
| 5. Evaluation asymmetry | Why can evaluation supervise capabilities beyond direct human generation? | V011--V012 | T019 | Verification/generation distinction and limits. |
| 6. Scalable oversight | Where does ordinary RLHF fail, and how can AI assistance move the ceiling? | V013--V014 | T020--T021 | Capability/evaluation curves and assisted-evaluation decomposition. |
| 7. Measuring progress | How can oversight be tested when real hard tasks lack ground truth? | V015--V016 | T022--T025 | Targeted perturbations, assisted accuracy, discriminator--critique gap. |
| 8. Human--machine division of labor | Which cognitive work should machines do, and what remains human? | V017 | T026--T035 | Responsibility table plus Q&A synthesis. |
| 9. Summary and extension | What is established, what is promising, and what remains unknown? | all | all | Evidence ladder and open questions. |

## Acceptance targets

- All 17 teaching slides appear exactly once and are explained locally.
- At least 20 pages, 10 teaching boxes, 3 teacher-voice markers, 3 formula groups, and 2 captioned code blocks.
- At least 260 prose characters per figure on average and roughly 220 nearby prose characters for dense slides.
- Every non-summary section/subsection opens with a prose bridge.
- Strict coverage has zero warnings; quality is `⭐⭐⭐`; two-pass XeLaTeX is stable; visual QA is signed.

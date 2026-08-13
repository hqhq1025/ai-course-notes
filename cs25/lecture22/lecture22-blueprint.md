# Lecture 22 Blueprint

## Teaching Thesis

The lecture is not a universal list of alignment hyperparameters. It is a case study in how an open research team turns a vague goal such as “helpful chatbot” into four coupled engineering objects: a distribution of demonstrations, a distribution of preferences, a training recipe, and an evaluation protocol. The central lesson is that changing the evaluator can reverse the apparent conclusion of a data experiment.

## Section Plan

1. **Source audit and evidence boundary**
   - Official course/date/video/deck metadata.
   - Repair the legacy note's blank URL, unsupported hyperparameters, and collapsed evidence categories.
   - Slides 1--3.
2. **What “training a chatbot” decomposes into**
   - SFT, reward modeling, RLHF, helpfulness versus harmlessness.
   - Formalize the SFT loss and pairwise reward-model loss.
   - Slides 4--5; teacher voice T001.
3. **Instruction-data landscape: who writes what**
   - Human-written versus model-generated prompts/completions.
   - Self-Instruct, UltraChat, CAMEL, OpenAssistant, Dolly, LIMA, and Surge as mechanisms rather than brand names.
   - Slides 7--13; T002--T004.
4. **SFT dataset design and Surge collection**
   - Task distribution, prompt/response length, quantity, human provenance, examples, demographics.
   - Explain why dataset size alone is not a meaningful independent variable.
   - Slides 14--22; T005--T006.
5. **Preference data as a separate measurement system**
   - 20K dialogues / 80K prompts, multi-turn context, 2,048-token cap, four-turn average, helpfulness priority, rating margins.
   - Bradley--Terry intuition, chosen/rejected pairs, weekly endpoint iteration.
   - Slides 23--29; T007--T010.
6. **Recipe 2: alignment distillation and Zephyr**
   - dSFT, AI feedback, dDPO, UltraChat, UltraFeedback, Mistral-7B.
   - DPO objective and why SFT remains necessary.
   - Slides 30--31 and 56--58; T011 and T014.
7. **Training and evaluation are different graphs**
   - Pretraining, in-context learning, SFT, RLHF.
   - Instruction following, human Elo, AlpacaEval, LMSYS Arena, MT-Bench, reward-model benchmarks, red teaming.
   - Slides 33--47; T012.
8. **Human-curated SFT results: metrics disagree**
   - Open LLM Leaderboard versus MT-Bench.
   - Prompt length, response length, dataset-size ablations, diminishing returns.
   - Separate correlation from causation and lecture-time leaderboard snapshots from durable conclusions.
   - Slides 49--55; T013.
9. **LLM-as-a-judge failure modes**
   - Positional bias, overcorrection, scoring versus ranking, training-evaluation doping, verbosity/diversity bias, task-dependent human correlation.
   - Pair-order randomization code and an evaluation audit table.
   - Slides 60--65; T015--T017 and T019.
10. **Cost, scale, and Q&A boundaries**
    - Vendor cost estimate, unstudied causes of bias, reward-model sequence score, approximate 10K/100K scale contrast.
    - T018--T020.
11. **Summary and extensions**
    - Slides 66--70.
    - Distill the recipe into data, objective, evaluator, and audit dimensions.
    - Recommend primary papers without importing post-2023 results as classroom facts.

## Mandatory Teaching Devices

- Definitions and formulas for SFT, reward modeling, RLHF, DPO, Elo, and pairwise preference.
- A terminology table for Self-Instruct, UltraChat, CAMEL, LIMA, OpenAssistant, Dolly, Surge-Instruct, UltraFeedback, AlpacaEval, MT-Bench, and Chatbot Arena.
- A comparison table separating human evaluation, automatic task metrics, LLM judges, reward-model benchmarks, and red teaming.
- A warning box on metric reversal and a warning box on judge/data contamination.
- Three captioned listings: task-distribution sampler, DPO batch schema, and pair-order-balanced LLM-judge evaluation.
- At least 20 teacher-voice markers woven into normal prose.
- Every required slide image referenced exactly once, with dense plots/tables receiving local `读图` explanations.

## Acceptance Targets

- 66 required teaching figures, all referenced exactly once.
- At least 20 pages, 10 teaching boxes, 3 formulas, 3 captioned listings, and 20 teacher-voice markers.
- At least 260 prose characters per figure on average; dense result/evaluator figures receive roughly 220 local prose characters.
- Strict coverage zero warning, `⭐⭐⭐`, stabilized two-pass XeLaTeX, and signed visual QA.

# Lecture 28 Writing Blueprint

## Teaching thesis

Open alignment progressed through a coupled system, not a single algorithm: strong base models, accessible instruction data, realistic chat distributions, memory-efficient fine-tuning, usable evaluations, preference data, reward modeling, and optimization recipes. Each wave changed what open builders could measure and reproduce. The lecture's strongest conclusion is that data and evaluation infrastructure often mattered as much as the named optimizer.

## Planned sections

1. Source correction, lecture scope, and the historical spine from Shannon to ChatGPT.
2. Base versus aligned models; definitions of IFT, SFT, RLHF, DPO, and alignment.
3. The first open instruct wave: Alpaca, self-instruct, Vicuna, ShareGPT, weight differences, OpenAssistant, and StableVicuna.
4. QLoRA/Guanaco and the accessibility of fine-tuning; why LoRA methods did not automatically solve RLHF.
5. Safety backlash, “uncensored” models, and the transition ecosystem.
6. Evaluation infrastructure: ChatBotArena, AlpacaEval, MT-Bench, Open LLM Leaderboard, bias, latency, and gaming.
7. RLHF objective, KL regularization, pairwise reward modeling, and the path to DPO.
8. DPO versus PPO through Zephyr, Tulu 2, SteerLM, and Starling.
9. Modern ecosystem, Llama 3, open/closed gap, data bottlenecks, synthetic data, and future directions.
10. Final synthesis, research checklist, self-test, and reading.

## Formal scaffolding

- Autoregressive next-token objective and the shift to instruction-response training.
- Low-rank update `Delta W = BA` and memory accounting for full fine-tuning versus LoRA/QLoRA.
- Bradley--Terry pairwise preference model.
- RLHF objective with reward and KL penalty.
- DPO loss and the role of policy/reference log-ratios.
- Evaluation decomposition into prompt distribution, candidate model, judge, baseline, and aggregation.
- Confidence intervals and pairwise Elo intuition for human preference evaluation.

## Terminology obligations

Define near first use: base model, instruction fine-tuning, supervised fine-tuning, alignment, RLHF, PPO, DPO, reward model, preference data, self-instruct, synthetic data, chat template, system prompt, LoRA, QLoRA, quantization, weight difference, LLM-as-a-judge, ChatBotArena, AlpacaEval, MT-Bench, Elo, KL divergence, policy, reference model, rejection sampling, and benchmark contamination.

## Figure treatment

- Insert every required official slide exactly once.
- Treat timeline builds as a prose-led history, not a screenshot album.
- Explain every evaluation table by prompt source, judge, baseline, aggregation, latency, and failure modes.
- Explain every RLHF/DPO formula symbol immediately and distinguish mathematical equivalence claims from optimizer behavior.
- Label model scores and ecosystem comparisons as April 2024 snapshots.

## Acceptance targets

- 67 official teaching figures, each exactly once.
- At least 22 teacher-voice markers.
- At least 30 teaching boxes and 14 displayed formulas.
- At least three captioned `lstlisting` blocks.
- At least 260 prose characters per figure on average.
- Strict coverage with zero warnings, double XeLaTeX, `⭐⭐⭐`, rendered PDF QA, and a signed QA report.

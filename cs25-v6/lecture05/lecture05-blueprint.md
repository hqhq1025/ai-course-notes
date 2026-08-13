# Lecture 05 Coverage Blueprint

## Teaching thesis

The lecture argues that the next scaling axis is not only more tokens or a larger model, but a better learning process. Data weighting, temporal ordering, early reasoning exposure, and exploratory thought rewards modify what the model can extract from the same nominal corpus. The note must keep three claims separate: two-phase pretraining optimizes curriculum over data mixtures; front-loading reasoning changes when reasoning data enters the pipeline; RLP changes the objective by rewarding thoughts for predictive information gain.

## Planned teaching flow

1. Establish the four-component SOTA recipe and the Pascal/Volta/Ampere/Hopper controlled analogy.
2. Explain the human-data frontier and distinguish blend weights from curriculum order.
3. Derive quality estimation, epoch estimation, and the two-phase diversity-to-quality schedule.
4. Interpret natural-distribution, random-optimal-blend, and two-phase baselines.
5. Define front-loading reasoning, reason-base/no-reason-base conditions, and the diversity/quality/quantity axes.
6. Read the five evaluation lessons without mixing base-model and post-trained metrics.
7. Motivate RLP through learning by doing and contrast vanilla next-token prediction with thought-conditioned prediction.
8. Derive the thought policy, no-think baseline, information-gain reward, dense advantages, and EMA update.
9. Separate token-matched, FLOP-matched, checkpoint-matched, architecture-scale, and post-training comparisons.
10. Compare NTP, Quiet-STaR, RPT, RLPT, and RLP by reward source, granularity, and reasoning emergence.
11. Preserve mid-talk and final Q&A on quality labels, recipe automation, phase reversal, GRPO, modalities, RLHF boundaries, token selection, and earlier checkpoints.
12. End with an engineering decision framework and open research questions rather than treating the reported recipes as universal laws.

## Formula scaffolding

- Autoregressive next-token loss and the distinction between observing a token and exploring a latent thought.
- Data-mixture weights under a fixed token budget, including domain-level epoch/repeat estimates.
- Two-phase schedule as a piecewise sampling distribution over training progress.
- Reasoning-data allocation under fixed pretraining and SFT budgets.
- Thought-conditioned predictor `p_theta(x_t | x_{<t}, c_t)` and no-think baseline `p_phi(x_t | x_{<t})`.
- Information-gain reward `r_t = log p_theta - log p_phi`, with positive, zero, and negative cases.
- Group-relative advantage and clipped policy surrogate at a conceptual level.
- EMA baseline update `phi <- tau phi + (1-tau) theta` and stability interpretation.
- Token-matched versus FLOP-matched accounting for rollout cost.
- Relative improvement versus absolute percentage-point improvement.

## Code scaffolding

- Captioned pseudocode for quality and repeat-count ablation when creating an optimal blend.
- Captioned pseudocode for a two-phase sampler with a phase boundary.
- Captioned pseudocode for the RLP training step, including random token selection, thought rollouts, dense rewards, group-relative advantages, NTP update, and EMA refresh.
- Captioned evaluation harness distinguishing base, continued-pretraining, post-trained, token-matched, and FLOP-matched baselines.

## Terminology digestion

- `data blend`, `curriculum`, `epoch estimation`, `quality estimation`, `phase 1`, `phase 2`.
- `reason base`, `no-reason base`, `SHQ`, `LDQ`, `LMQ`, `SFT`, `RLVR`.
- `thought policy`, `rollout`, `no-think baseline`, `information gain`, `dense reward`, `EMA`, `reward hacking`.
- `NTP`, `CPT`, `Quiet-STaR`, `RPT`, `RLPT`, `RLP`, `GRPO`.
- `token-matched`, `FLOP-matched`, `relative gain`, `absolute gain`, and `checkpoint matched`.

## Figure treatment

- All 41 required recording-derived slide states appear exactly once.
- Three title/divider states are optional because the cover and prose transitions preserve their metadata and role.
- Every result chart receives axes/baseline/metric interpretation and a statement of what the plot does not prove.
- Progressive builds are represented by the final fully revealed state; intermediate states are omitted unless they teach a different mechanism.
- Every recording frame carries a same-page timestamp provenance footnote.
- The introductory recipe and closing recipe are both retained because the second functions as synthesis after the mechanisms are known.

## Quality risks

- Do not equate more repetitions with more unique data.
- Do not treat classifier-assigned quality as objective truth.
- Do not infer that diversity-first ordering is universal outside the reported data and model regimes.
- Do not compare percentages across different benchmark suites as if they shared one denominator.
- Do not conflate `reasoning data` with all high-quality data or with all domains.
- Do not claim that front-loading eliminates SFT or RLVR; the reported gains often compound after them.
- Do not call RLP verifier-free without explaining that the observed next token supplies self-supervision.
- Do not interpret information gain as factual correctness or faithful human-readable reasoning.
- Do not compare token counts without accounting for rollout FLOPs.
- Do not project the language-only result to vision-language models; the speaker explicitly says this is untested.
- Do not convert Q&A opinions about RLHF and alignment into findings of the three papers.
- Do not copy the Lecture 04 Ultra-Scale deck through the erroneous Lecture 05 course-page link.

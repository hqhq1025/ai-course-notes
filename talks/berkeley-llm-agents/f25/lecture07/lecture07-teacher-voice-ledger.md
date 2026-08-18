# Lecture 07 Teacher Voice Ledger

| Time | Spoken point | Why it matters | Note location |
|---|---|---|---|
| 00:03--00:07 | Modern generative and agent benchmarks are far smaller than MNIST/ImageNet, but each item may contain a long answer. | Frames the central tension rather than assuming sample size alone decides quality. | Official evidence, small-benchmark motivation |
| 00:10--00:15 | A weak model sometimes solves a hard item and a strong model misses an easy one; the first nonzero success probability is more informative than moving from 1% to 99%. | Separates qualitative capability discovery from stable comparative measurement. | Heatmap and probability interpretation |
| 00:15:15 | The kettle assistant calls a kettle a robotic vacuum; later correct-looking advice should no longer receive full trust. | Makes multi-step inconsistency concrete for agent tasks. | Kettle example and warning box |
| 00:20--00:25 | Models can be sampled repeatedly in a way humans usually cannot; this inference randomness is not the only noise and may be the more important one. | Prevents seed variance from being confused with dataset uncertainty. | Two-level sampling model |
| 00:28:21 | Bootstrap is valid, but simple array formulas can expose what is being estimated and reduce implementation mistakes. | Keeps statistical tooling interpretable. | Bootstrap/sign-test section |
| 00:31--00:37 | Noise is predictable from dataset size and accuracy range, while filtering/reweighting questions did not improve signal much. | Moves effort from clever reweighting toward more data and richer labels. | Predictable-noise and failed-signal sections |
| 00:38:12 | Multiple seeds and training-curve variance are useful but usually underestimate the full evaluation uncertainty. | Clarifies the evidence boundary of common practice. | Measurement recommendations |
| 00:42--00:44 | Signal-to-noise is necessary to interpret gains; complex long-context evaluations can hide serious benchmark defects when nobody inspects details. | Connects statistics to benchmark governance. | Final signal-to-noise and audit sections |

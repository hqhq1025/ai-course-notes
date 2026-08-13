# Lecture 22 Coverage Matrix

| Source nodes | Teaching treatment | Evidence boundary | Planned section |
|---|---|---|---|
| Slides 1--5 | H4 scope, open alignment recipe, SFT/reward-model/RLHF pipeline, helpfulness versus harmlessness. | The lecture mainly studies helpfulness/SFT; it is not a complete harmlessness recipe. | Scope and pipeline |
| Slides 7--13 | Demonstration schema and the synthetic-to-human continuum; Self-Instruct, UltraChat, CAMEL, OpenAssistant, Dolly, LIMA, Surge. | Dataset names are explained through authorship, generation, filtering, and provenance. | Data landscape |
| Slides 14--22 | Prior diminishing-return evidence, SFT desiderata, task and length distributions, Surge examples and annotator context. | Observed dataset correlations do not by themselves prove causal effects. | SFT design |
| Slides 23--29 | Preference interfaces, desiderata, pilot, 20K/80K allocation, context/turn constraints, rating scale, chosen/rejected examples. | Collection choices are H4 design decisions under 2023 model/context limits. | Preference data |
| Slides 30--31 | Synthetic alignment distillation and Zephyr's dSFT--AI feedback--dDPO pipeline. | Zephyr claims are tied to displayed 2023 protocols and do not imply universal superiority. | Distillation mechanism |
| Slides 33--47 | Training stages and evaluation layers: instruction following, Elo, AlpacaEval, Arena, MT-Bench, reward models, red teaming. | Each evaluation protocol measures a different operational question. | Evaluation stack |
| Slides 49--55 | Open LLM and MT-Bench results, response/prompt length, and dataset-size ablations. | Metric disagreement is itself a result; no single plot identifies a universally best dataset. | Human-curated results |
| Slides 56--58 | Distillation results and Zephyr ablations. | DPO-only failure, strong SFT contribution, and smaller DPO gain are lecture-time ablations. | Distillation results |
| Slides 60--65 | Position bias, prompted overcorrection, scoring/ranking, data doping, length/diversity bias, task-dependent correlation. | Judge behavior is protocol- and task-dependent; causal explanations remain partly open. | LLM-as-judge audit |
| Slides 66--70 | Takeaways, public labor context, UN advisory context, official H4 resources, and team attribution. | Closing institutional slides provide provenance, not technical performance evidence. | Final synthesis |
| T001--T010 | H4 scope, data authorship, synthetic mechanisms, human-quality tradeoff, SFT desiderata, Surge context, preference design, task entropy, iterative collection, rating scale. | Spoken points are paraphrased with timestamps and kept within the lecture boundary. | Sections 1--5 |
| T011--T017 | Zephyr mechanism, evaluation stack, metric conflicts, ablations, positional bias, data/style bias, task-dependent correlation. | Claims remain tied to the shown experiments and protocols. | Sections 6--9 |
| T018--T020 | Vendor cost, incomplete bias-cause study, balanced pair ordering, reward-model intuition, approximate 10K/100K scale contrast. | Q&A numbers are attributed estimates, not general laws. | Cost and Q&A |

## Intentional Omissions

| Slide | Reason |
|---|---|
| 6 | Pure `Dataset` divider; its transition is preserved in prose. |
| 32 | Pure `Experiments & Evaluation` divider; its transition is preserved in prose. |
| 48 | Pure `SFT Results` divider; its transition is preserved in prose. |
| 59 | Pure `Quirks of using GPT4 as Evaluator` divider; its transition is preserved in prose. |
| 71 | Closing `Thanks for listening` slide with no substantive teaching content. |

## Acceptance Evidence

- The final note is 60 pages and references all 66 required slide nodes exactly once; the five optional divider/closing pages remain intentionally omitted. It contains 72 teaching boxes, 23 in-note teacher-voice markers, 6 displayed formula blocks, 3 captioned listings, and 22,805 prose characters, averaging 345 prose characters per figure.
- `check_note_coverage.py --strict` reports 66 figures, 51 local read-figure treatments, 12 section summaries, and zero warnings or missing required nodes.
- `check_quality.sh` reports `⭐⭐⭐`; the stabilized final two-pass XeLaTeX log has no overfull/underfull boxes, undefined references, rerun requests, or hyperref warnings beyond the repository-standard Fandol font notices.
- Canonical PDF visual QA is signed in `qa/lecture22-notes/qa-report.md` after reviewing the complete 60-page contact sheet and enlarged source-audit, data, formula, table, code, result, evaluator-bias, synthesis, and reference pages.

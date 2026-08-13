# CS153 Lecture 04 Coverage Matrix

Status: complete on 2026-08-11; strict coverage and visual QA accepted.

| Source node | Type | Required? | Planned note section | Treatment | Status |
|---|---|---|---|---|---|
| V001 | diagram | yes | 研究轨迹 | translation → theorem proving → LLaMA → Mistral; research questions become infrastructure requirements | complete |
| V002 | diagram | yes | 无监督翻译 | embedding spaces, alignment transform, dictionary bootstrap and back-translation loop | complete |
| V003 | diagram | yes | 形式化证明 | proof state, tactic, multiple subgoals and hyper-tree structure | complete |
| V004 | diagram | yes | Informal-to-formal | informal proof proposal guides formal search; verifier remains authoritative | complete |
| V005 | diagram | yes | Chinchilla | fixed-compute objective versus lifetime inference objective | complete |
| V006 | diagram | yes | 训练故障 | small-run pass, large-run FP16 drift, loss increase and diagnosis loop | complete |
| V007 | diagram | yes | R&D iceberg | final training run versus failed experiments, tooling and debugging | complete |
| V008 | diagram | yes | Mistral 7B | data-heavy team allocation and data-quality iteration | complete |
| V009 | diagram | yes | checkpoint-to-solution | weights → runtime → endpoint → application → operations | complete |
| V010 | diagram | yes | 部署模式 | external API, private cloud, on-prem and edge constraints | complete |
| V011 | diagram | yes | 定制闭环 | use case → data → synthetic generation → fine-tuning → eval → deploy | complete |
| V012 | diagram | yes | 产品反馈 | tool-using product, user feedback, failure taxonomy and training priorities | complete |
| V013 | diagram | yes | reasoning | task/environment/verifier/reward/training loop and early-stage uncertainty | complete |
| V014 | diagram | yes | post-training | data/eval/tool/serving/safety pipeline as an operating system | complete |
| V015 | diagram | yes | privacy/reliability | control, residency and reliability requirements select deployment architecture | complete |
| V016 | diagram | yes | open ecosystem | reuse open assets, add customization and product-specific systems | complete |
| P001 | paper | yes | 无监督翻译 | distinguish geometric intuition from the full adversarial/back-translation method | complete |
| P002 | paper | yes | 形式化证明 | HTPS online learning, proof verification and hypergraph semantics | complete |
| P003 | paper | yes | Chinchilla | 70B / 1.4T compute-optimal result and its objective boundary | complete |
| P004 | paper | yes | LLaMA | small models trained on large token horizons and inference-efficiency motivation | complete |
| P005 | paper | yes | Mistral 7B | GQA, SWA, Apache 2.0 and efficient deployment claims | complete |
| W001 | official web | yes | Mistral 7B | official release/deployment paths and fine-tuning positioning | complete |
| W002 | official web | yes | EU AI Act | current GPAI obligations and timeline, clearly separated from lecture-time uncertainty | complete |
| T001--T016 | teacher voice | yes | whole note | motivations, caveats, informal definitions and engineering judgments from ledger | complete |
| PDF visual QA | QA | yes | `qa/lecture04-notes/` | inspect contact sheet, dense diagrams, wide tables, URLs and final page | complete |

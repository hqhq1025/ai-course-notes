# Lecture 23 Coverage Matrix

| Node | Required source | Planned treatment | Note section | Status |
|---|---|---|---|---|
| slide-01-title | `slides-images/slide-01-title.jpg` | Title, project scope, and sociotechnical thesis | Opening | covered |
| slide-02-written-languages | `slides-images/slide-02-written-languages.jpg` | Global written-language gap and personal motivation | Coverage | covered |
| slide-03-product-coverage | `slides-images/slide-03-product-coverage.jpg` | Lecture-time product counts with timestamp caveat | Coverage | covered |
| slide-04-double-coverage-safely | `slides-images/slide-04-double-coverage-safely.jpg` | Double coverage while preserving quality and safety | Coverage | covered |
| slide-05-current-progress | `slides-images/slide-05-current-progress.jpg` | High-resource versus low-resource progress | Coverage | covered |
| slide-06-real-problem | `slides-images/slide-06-real-problem.jpg` | Research question before model construction | Human-centered method | covered |
| slide-07-speaker-interviews | `slides-images/slide-07-speaker-interviews.jpg` | Interview cohort and method | Human-centered method | covered |
| slide-08-interview-findings | `slides-images/slide-08-interview-findings.jpg` | Decline, inclusion, and useful-imperfect translation | Human-centered method | covered |
| slide-09-evaluation-datasets | `slides-images/slide-09-evaluation-datasets.jpg` | Evaluation-first transition | FLORES | covered |
| slide-10-flores-101 | `slides-images/slide-10-flores-101.jpg` | FLORES benchmark lineage | FLORES | covered |
| slide-11-flores-properties | `slides-images/slide-11-flores-properties.jpg` | Low-resource, many-to-many, diverse, document-level properties | FLORES | covered |
| slide-12-flores-collection-pipeline | `slides-images/slide-12-flores-collection-pipeline.jpg` | Standard alignment, translation, review, and QC | FLORES | covered |
| slide-13-flores-collection-challenges | `slides-images/slide-13-flores-collection-challenges.jpg` | Recruitment, standards, scripts, variants | FLORES | covered |
| slide-14-seed-data-why | `slides-images/slide-14-seed-data-why.jpg` | Bootstrapping dependencies | Data mining | covered |
| slide-15-nllb-seed | `slides-images/slide-15-nllb-seed.jpg` | Seed size, languages, and uses | Data mining | covered |
| slide-16-wikimatrix | `slides-images/slide-16-wikimatrix.jpg` | Large-scale mining precedent | Data mining | covered |
| slide-17-sentence-alignment | `slides-images/slide-17-sentence-alignment.jpg` | Content matching, extraction, and sentence scoring | Data mining | covered |
| slide-18-encoder-training | `slides-images/slide-18-encoder-training.jpg` | MLM and multilingual distillation | Data mining | covered |
| slide-19-laser3-encoder-quality | `slides-images/slide-19-laser3-encoder-quality.jpg` | Cross-language encoder quality comparison | Data mining | covered |
| slide-20-data-pipeline | `slides-images/slide-20-data-pipeline.jpg` | Full iterative LID/mining/filtering/validation loop | Data mining | covered |
| slide-21-stopes-open-source | `slides-images/slide-21-stopes-open-source.jpg` | Released pipeline and reproducibility | Data mining | covered |
| slide-22-very-low-resource-challenges | `slides-images/slide-22-very-low-resource-challenges.jpg` | Monolingual bottleneck, scripts, narrow domains | Data mining | covered |
| slide-23-model-challenges | `slides-images/slide-23-model-challenges.jpg` | Augmentation, interference, and scale | Data recipe | covered |
| slide-24-transformer-preliminaries | `slides-images/slide-24-transformer-preliminaries.jpg` | Encoder-decoder translation path | Data recipe | covered |
| slide-25-data-source-comparison | `slides-images/slide-25-data-source-comparison.jpg` | Provenance/noise/size/model-dependence taxonomy | Data recipe | covered |
| slide-26-public-seed-data | `slides-images/slide-26-public-seed-data.jpg` | Initial long-tail imbalance | Data recipe | covered |
| slide-27-mining-backtranslation | `slides-images/slide-27-mining-backtranslation.jpg` | Expanded data distribution and residual imbalance | Data recipe | covered |
| slide-28-moe-architecture | `slides-images/slide-28-moe-architecture.jpg` | Conditional capacity and routing tradeoffs | MoE | covered |
| slide-29-dropout-eom-results | `slides-images/slide-29-dropout-eom-results.jpg` | Dense/MoE regularization ablations | MoE | covered |
| slide-30-curriculum-learning | `slides-images/slide-30-curriculum-learning.jpg` | Overfitting buckets and schedule | MoE | covered |
| slide-31-flores101-comparison | `slides-images/slide-31-flores101-comparison.jpg` | Prior-system comparison | Evaluation | covered |
| slide-32-flores200-results | `slides-images/slide-32-flores200-results.jpg` | Direction/resource-level results | Evaluation | covered |
| slide-33-external-system-comparison | `slides-images/slide-33-external-system-comparison.jpg` | Commercial-system calibration | Evaluation | covered |
| slide-34-human-evaluation | `slides-images/slide-34-human-evaluation.jpg` | Automatic versus human roles | Evaluation | covered |
| slide-35-human-evaluation-paper | `slides-images/slide-35-human-evaluation-paper.jpg` | Consistent protocol across language pairs | Evaluation | covered |
| slide-36-human-evaluation-results | `slides-images/slide-36-human-evaluation-results.jpg` | Into/out-of/non-English human results | Evaluation | covered |
| slide-37-toxicity-error-severity | `slides-images/slide-37-toxicity-error-severity.jpg` | Unequal error severity and COVID example | Safety | covered |
| slide-38-toxicity-lists | `slides-images/slide-38-toxicity-lists.jpg` | 200-language culturally specific lists | Safety | covered |
| slide-39-future-directions | `slides-images/slide-39-future-directions.jpg` | Explicit multilinguality, support, ease of use | Future/Q&A | covered |
| teacher-voice-01 | `lecture23-teacher-voice-ledger.md` | Personal motivation and safe usable translation | Opening | covered |
| teacher-voice-02 | `lecture23-teacher-voice-ledger.md` | Interview-first method and community findings | Human-centered method | covered |
| teacher-voice-03 | `lecture23-teacher-voice-ledger.md` | Evaluation before training | FLORES | covered |
| teacher-voice-04 | `lecture23-teacher-voice-ledger.md` | Iterative data pipeline and hard data floor | Data mining | covered |
| teacher-voice-05 | `lecture23-teacher-voice-ledger.md` | MoE capacity versus overfitting | MoE | covered |
| teacher-voice-06 | `lecture23-teacher-voice-ledger.md` | Automatic metric versus real usability | Evaluation | covered |
| teacher-voice-07 | `lecture23-teacher-voice-ledger.md` | Toxicity example and cultural specificity | Safety | covered |
| teacher-voice-08 | `lecture23-teacher-voice-ledger.md` | Native-speaker participation through the lifecycle | Future/Q&A | covered |
| teacher-voice-09 | `lecture23-teacher-voice-ledger.md` | Data/model work split and Common Crawl caveat | Future/Q&A | covered |
| teacher-voice-10 | `lecture23-teacher-voice-ledger.md` | Zero-shot boundary, SeamlessM4T, foundation-model shift | Future/Q&A | covered |

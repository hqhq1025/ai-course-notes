# Lecture 23 Rewrite Blueprint

## Teaching Thesis

NLLB is not simply a larger multilingual Transformer. The lecture's actual thesis is that breaking the 200-language barrier requires a coupled sociotechnical system: community consultation, benchmark construction, seed and mined data, multilingual representation learning, conditional model capacity, regularization, human evaluation, toxicity analysis, and open release.

## Evidence Order

1. Stanford recording and manual subtitles define classroom scope and teacher voice.
2. Recovered classroom frames define the visual spine.
3. The NLLB paper and official repositories clarify mechanisms and metric notation.
4. The team seminar is verification-only and cannot substitute for classroom evidence.

## Planned Sections

### 1. 从语言覆盖率到真实可用性

- Slides 01--05.
- Define written-language coverage, high/low-resource, and safe usable translation.
- Preserve Fan's personal motivation and warning that product counts were already time-sensitive.
- Teaching devices: resource glossary, coverage-vs-quality warning, central objective box.

### 2. 先问人，再定义任务

- Slides 06--08.
- Reconstruct the interview-first method and findings about decline, inclusion, and sufficiency.
- Separate community consultation from post hoc user testing.
- Teaching devices: human-centered loop diagram/table, teacher-voice markers, participation warning.

### 3. FLORES-200：先把评估基础设施建起来

- Slides 09--13.
- Explain benchmark lineage, many-to-many directions, domain/document diversity, language-standard alignment, translator review, and collection challenges.
- Add formulas for translation-direction count and metric aggregation limits.
- Teaching devices: benchmark property table, collection pipeline reading guide, standardization warning.

### 4. 从 Seed 到可挖掘的多语语料

- Slides 14--22.
- Explain NLLB-Seed, WikiMatrix, sentence alignment, multilingual distillation, LASER3, LID, filtering, bilingual validation, and Stopes.
- Emphasize that the pipeline is iterative and cannot create monolingual evidence that the web does not contain.
- Teaching devices: seed dependency box, mining score formula, pipeline stage table, low-resource failure warning.

### 5. 数据配方与长尾不平衡

- Slides 23--27.
- Introduce encoder-decoder Transformer only to the depth needed for translation.
- Compare human-aligned, public, mined, multilingual-BT, and bilingual-BT data by provenance, noise, scale, and model dependence.
- Explain backtranslation and why expanded volume does not imply balanced quality.
- Teaching devices: first-use glossary, data taxonomy table, backtranslation pseudocode listing.

### 6. MoE、过拟合与课程学习

- Slides 28--30.
- Define token-level Mixture of Experts, routing, conditional capacity, language interference, dropout, expert-output masking, and overfitting-based curriculum scheduling.
- Explain the ablation plots without claiming causality beyond the displayed comparisons.
- Teaching devices: MoE formula and symbol list, dense-vs-MoE table, overfitting warning, curriculum pseudocode.

### 7. 自动指标、人工评估与安全

- Slides 31--38.
- Read FLORES-101/FLORES-200 results by direction and resource group.
- Define BLEU/chrF++ at an intuitive level and clarify relative 44% BLEU.
- Explain human evaluation consistency and added-toxicity as a separate safety axis.
- Teaching devices: metric glossary, results reading boxes, relative-improvement formula, toxicity failure case.

### 8. 开源、未来方向与课堂问答

- Slide 39 plus Q&A transcript.
- Cover explicit multilinguality, spoken-language limits, full-development native-speaker participation, data/model work allocation, Common Crawl limits, zero-shot boundary, SeamlessM4T, and the move toward stronger foundation models.
- Teaching devices: evidence-boundary warning, open artifact table, future research questions.

## Quantitative Targets

- 39/39 selected teaching states included.
- At least 20 pages, with a practical target of 40+ pages.
- At least 24 teaching boxes and 12 teacher-voice markers.
- At least 6 displayed formulas with immediate symbol explanations.
- At least 2 captioned code listings.
- At least 260 prose characters per figure on average and no cluster of thin local explanations.
- Strict coverage with zero warnings, `⭐⭐⭐`, clean double-pass XeLaTeX, and signed visual QA.

## Prohibited Legacy Claims

- No Padlet poll, GitHub localization map, invented priority formula, weekly BigQuery dashboard, internal staff dashboard, agentic deployment, steering-meeting cadence, fixed governance thresholds, or unsupported routing/cache operations.
- No claim that a single automatic metric proves usability or safety.
- No claim that NLLB trained directly on every one of the 200x200 directions.

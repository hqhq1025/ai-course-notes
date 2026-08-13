# Lecture 13 Writing Blueprint

## Teaching Thesis

The lecture is not a slogan that "bigger is always better." It teaches how to reason about regime changes: distinguish smooth loss scaling from thresholded task metrics, treat scale as one of several coupled variables, preserve causal uncertainty, and understand chain-of-thought plus self-consistency as scale-dependent inference interventions.

## Source Boundary

- Required visual spine: official deck slides 1--36.
- Intentionally omitted slide: slide 37, pure thanks/contact page.
- Required live evidence: no-CoT and CoT Playground math states at 00:39:54 and 00:40:17.
- Teacher voice: all high-value ledger rows should be synthesized; at least six explicit `课堂提示` markers.
- Historical cutoff: 2023-01-24. Later emergence-metric debates belong only in clearly labeled post-lecture reading, if mentioned at all.

## Section Plan

1. **来源审计与阅读地图**
   - Classroom/upload dates, official deck, subtitle quality, exclusion of later debates.
   - Slides 1--2.
2. **平滑 scaling laws 与 emergent abilities**
   - Slides 3--6.
   - Define loss scaling, emergence, three scale axes, and operational task presence.
   - Formula chain for cross-entropy/perplexity and approximate training compute.
3. **Few-shot 阈值、inverse scaling 与 U-shape**
   - Slides 7--12.
   - Read axes/baselines, MMLU/IPA examples, inverse scaling, emergent prompting techniques.
4. **阈值为什么会移动：数据、后训练与度量轴**
   - Slides 13--18.
   - Better data, controlled verb-frequency ablation, fine-tuning desired behavior, parameters/FLOPs/perplexity, surprising fine-tuning crossover.
   - Distinguish ability discovery from capability transfer.
5. **Emergence 的证据边界与工程含义**
   - Slide 19.
   - General-purpose scaling versus known production tasks, costly ablations, prediction difficulty, benchmark lifecycle.
6. **Chain-of-thought：把答案 token 变成推理轨迹**
   - Slides 20--23 plus two live-demo figures.
   - Standard versus CoT prompts, GSM8K/StrategyQA, explicit worked example, two captioned Python listings.
7. **BIG-Bench Hard：从平均分到任务级异质性**
   - Slides 24--27.
   - Benchmark construction, navigation/word sorting, average versus human-threshold metrics, scale threshold.
8. **跨语言组合性与 scaling 的错误修复**
   - Slides 28--30.
   - MGSM, underrepresented languages, error categories, task-spectrum diagram.
9. **Self-consistency：用采样预算换可靠性**
   - Slides 31--33.
   - Temperature sampling, answer marginalization, majority vote, cost/accuracy tradeoff, emergence.
10. **讨论、结论与研究议程**
    - Slides 34--36.
    - Prompt engineering durability, few-shot generalization, open causal questions, better benchmarks, compute-efficient access.

## Planned Formal Elements

- Approximate training compute: `C \propto ND` with a warning that constants and architecture matter.
- Cross-entropy and perplexity: `PPL = exp(H)` with an "effective choices" intuition and limitations.
- Chance-normalized task gain to separate random baseline from raw accuracy.
- CoT autoregressive factorization over intermediate tokens.
- Temperature sampling distribution.
- Self-consistency answer vote / marginalization approximation.

## Planned Code Listings

1. Standard prompting versus few-shot CoT prompt construction.
2. Self-consistency sampling and majority vote with explicit answer extraction.

## Figure Treatment Rules

- Every slide filename must appear exactly once in the TeX.
- Closely related incremental slides may share a subsection, but each receives nearby prose that identifies axes, baselines, comparisons, and limitations.
- Target at least 11,000 prose characters for 38 required visual states; target 300+ characters per figure overall.
- Use `读图` boxes for slides 4, 8, 11, 12, 13, 14, 15, 16, 17, 18, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, and 33.

## Acceptance Targets

- 30+ PDF pages.
- 38 required figures, 10+ teaching boxes, 3+ formulas, 2 captioned listings.
- Strict coverage with zero warnings.
- `check_quality.sh` grade `⭐⭐⭐`.
- Two-pass XeLaTeX without unresolved references or layout warnings.
- Canonical visual QA contact sheet reviewed and report signed.

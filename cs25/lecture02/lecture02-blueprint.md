# CS25 Lecture 02 Blueprint

Status: complete and accepted on 2026-08-11 after strict coverage, two-pass XeLaTeX, `⭐⭐⭐` quality audit, and canonical PDF visual QA.

## Goal

把 Mark Chen 的 GPT/Codex 讲座重写成一份“generative pretraining 如何跨越文本、图像和代码”的系统讲义。正文以 45 张原始 teaching slides 为视觉骨架，围绕三个问题展开：为什么生成建模可作为无监督学习接口；为什么 scale 与 prompting 产生 zero/few-shot behavior；为什么 code 需要 functional correctness、pass@k 和 sampling-aware evaluation。

## Teaching Thesis

本讲可以压缩为三个闭环：

1. `model distribution → sample → human/task evaluation → scale/recipe change`；
2. `unlabeled data → autoregressive objective → representation/behavior → downstream transfer`；
3. `problem prompt → sampled programs → unit tests → pass@k → temperature/model decision`。

## Section Plan

1. 来源审计与 2021 时间边界。
2. 3-gram、RNN、LSTM、Transformer 与 GPT-2/3 的语言建模演进。
3. Human detection experiment：质量、distribution 与评估边界。
4. 为什么无监督学习：标注瓶颈与互联网规模数据。
5. Analysis by synthesis、autoregressive likelihood 与 sentiment neuron。
6. GPT-1/2：pretrain-finetune、zero-shot reading/summarization/translation。
7. GPT-3：language-model meta-learning、few-shot arithmetic、unscrambling 与 general curves。
8. iGPT：像素序列生成、completion 与 feature learning。
9. DALL-E：text-to-image、zero-shot image-to-image 与 representation interface。
10. Code as modality：HumanEval、functional correctness 与 benchmark construction。
11. Pass@k 推导、sampling temperature 与 oracle approximation。
12. Codex training、Codex-S、main figure、limitations 与安全边界。
13. 总结、评估作业与拓展阅读。

## Required Treatment

- 45 张 teaching slides 全部进入正文；3 张纯章节分隔页、Stanford bumper、重复结束页和 acknowledgments 作为明确 optional nodes。
- 首次解释 n-gram、perplexity、RNN/LSTM、autoregressive model、unsupervised learning、analysis by synthesis、zero-shot、few-shot、in-context learning、meta-learning、representation learning、functional correctness、unit test、pass@k、sampling temperature、oracle、fine-tuning。
- 推导 autoregressive likelihood、perplexity 与 unbiased pass@k estimator；解释每个符号。
- 每个 dense plot/code slide 有读图说明，特别区分 benchmark improvement、sample diversity 与 deployed correctness。
- 最终执行 strict coverage、双遍 XeLaTeX、`⭐⭐⭐`、canonical PDF QA 与人工签署。

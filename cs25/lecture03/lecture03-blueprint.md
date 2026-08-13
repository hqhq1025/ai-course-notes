# CS25 Lecture 03 Blueprint

Status: complete and accepted on 2026-08-11 after strict coverage, two-pass XeLaTeX, `⭐⭐⭐` quality audit, and canonical PDF visual QA.

## Goal

把 Lucas Beyer 的 Vision Transformers 讲座重写成一份“如何测量、训练与扩展通用视觉表示”的系统讲义。正文以 36 张原始 teaching slides 为视觉骨架，不把 ViT 简化成 patchify 加 Transformer，而是把 VTAB、BiT、数据泄漏、归纳偏置、位置编码、compute scaling、模型形状、训练日程和 MLP-Mixer 串成完整证据链。

## Teaching Thesis

本讲围绕四个闭环展开：

1. `general representation → few-shot adaptation → VTAB measurement`；
2. `data scale + model capacity + training recipe → transferable representation`；
3. `image patches → token sequence → Transformer encoder → downstream adaptation`；
4. `compute budget → model shape / schedule / regularization → sample efficiency and scaling laws`。

## Section Plan

1. 来源审计、2021 时间边界与 general visual representation 的目标。
2. 人类 few-shot 视觉归纳与 VTAB 的 upstream/downstream protocol。
3. self-supervised、semi-supervised 与 Big Transfer 的路线比较。
4. BiT 的数据规模、训练耐心、鲁棒性与 deduplication。
5. ViT 架构：patch、linear projection、class token、position embedding 与 encoder。
6. 数据规模、正则化和 compute 对 ViT/ResNet 的影响。
7. position embedding、model shape、inference speed 与 effective receptive field。
8. Scaling ViT：深度/宽度、无限日程、head weight decay、sample efficiency 与 scaling laws。
9. MLP-Mixer：当 data 足够大时，哪些视觉归纳偏置可以被削弱。
10. Q&A 中关于参数量、FLOPs、视觉研究资源和模型容量的口头判断。
11. 总结、评估练习与拓展阅读。

## Required Treatment

- 36 张 teaching slides 全部进入正文；纯 bumper、纯章节过渡、重复回看和冗余 animation build 必须在 coverage 中说明。
- 首次解释 visual representation、few-shot adaptation、VTAB、upstream/downstream、self-supervised learning、semi-supervised learning、transfer learning、deduplication、patch embedding、class token、position embedding、inductive bias、FLOPs、sample efficiency、scaling law 和 MLP-Mixer。
- 用公式解释 patch tokenization、self-attention 复杂度、transfer objective 与幂律 scaling；每个符号就地定义。
- 每张 dense plot 都说明坐标轴、比较对象、关键趋势、不能推出的结论和工程含义。
- teacher voice 必须保留 Lucas 关于“耐心训练”、参数量不是唯一模型规模、benchmark leakage、视觉研究资源和数据规模的口头判断。
- 最终执行 strict coverage、双遍 XeLaTeX、`⭐⭐⭐`、canonical PDF QA 与人工签署。

# CS25 Lecture 01 Blueprint

Status: complete and visually accepted on 2026-08-11.

## Goal

把 22:43 的系列导论重写成一份自包含的 Transformer 入门讲义：既覆盖原视频 17 张教学 slide，也用公式、最小例子和术语表把 attention、self-attention、encoder/decoder、GPT-3 与 BERT 的关系讲清楚；保留三位讲师对课程目标、跨领域应用和未来研究方向的课堂口吻。

## Teaching Thesis

Transformer 的核心不是“更大的神经网络”，而是三次接口重构：

1. `fixed vector → query-conditioned retrieval`：attention 让 decoder 按当前需求读取 encoder states；
2. `recurrent state → token-to-token interaction`：self-attention 让序列元素直接交换信息；
3. `task-specific model → reusable pretrain/fine-tune or prompting interface`：encoder-only、decoder-only 与 encoder-decoder 支撑不同产品范式。

## Section Plan

1. 来源审计、课程角色与三项学习目标。
2. Attention timeline：RNN/LSTM/GRU、seq2seq bottleneck 与早期 attention。
3. Soft/hard、global/local attention 的设计空间。
4. Self-attention 的 $Q/K/V$、scaled dot-product、mask 与 multi-head。
5. Positional encoding、residual、normalization 与 feed-forward network。
6. Encoder-decoder architecture 与 autoregressive masking。
7. 优势、二次复杂度、长上下文与归纳偏置。
8. GPT-3 decoder-only、in-context learning 与生成范式。
9. BERT encoder-only、masked language modeling 与表示学习。
10. 跨 NLP/CV/RL/biology 的迁移地图与课程后续阅读法。
11. 总结、手算练习与拓展阅读。

## Required Treatment

- 17 张 teaching-bearing slides 全部进入正文；纯分隔页与重复 build state 在 coverage matrix 中说明。
- 首次解释 RNN、LSTM、GRU、seq2seq、context vector、attention、soft/hard、global/local、self-attention、query/key/value、mask、multi-head、positional encoding、residual connection、layer normalization、encoder、decoder、autoregressive、in-context learning、masked language modeling。
- 公式后立即解释每个符号，并给出一个三 token 的 attention 手算或伪代码例子。
- 每个 figure 有问题设置、读图说明与局限；正文平均每图至少 260 字符。
- 最终执行 strict coverage、双遍 XeLaTeX、`⭐⭐⭐`、canonical PDF QA 与人工签署。

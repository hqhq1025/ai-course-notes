# CS25 Lecture 07 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online official video, `zejXBg-2Vpk`: `https://www.youtube.com/watch?v=zejXBg-2Vpk`.
- Stanford CS25 V1 course page: `https://web.stanford.edu/class/cs25/past/cs25-v1/`.
- Official CS25 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture07.en.srt`, 1,476 parsed captions.
- The course page and video description expose no standalone slide PDF. `slides-images/` therefore contains 28 reviewed teaching slides or final progressive-build states recovered from the official 1080p recording.

## Primary technical sources

- Kossen et al., *Self-Attention Between Datapoints: Going Beyond Individual Input-Output Pairs in Deep Learning*: `https://arxiv.org/abs/2106.02584`.
- Official NPT implementation: `https://github.com/OATML/Non-Parametric-Transformers`.
- Vaswani et al., *Attention Is All You Need*: `https://arxiv.org/abs/1706.03762`.
- Devlin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*: `https://arxiv.org/abs/1810.04805`.
- Zaheer et al., *Deep Sets*: `https://arxiv.org/abs/1703.06114`.
- Lee et al., *Set Transformer*: `https://arxiv.org/abs/1810.00825`.
- Garnelo et al., *Conditional Neural Processes*: `https://arxiv.org/abs/1807.01613`.
- Kipf et al., *Neural Relational Inference for Interacting Systems*: `https://arxiv.org/abs/1802.04687`.
- Arik and Pfister, *TabNet: Attentive Interpretable Tabular Learning*: `https://arxiv.org/abs/1908.07442`.
- Chen and Guestrin, *XGBoost: A Scalable Tree Boosting System*: `https://arxiv.org/abs/1603.02754`.
- Prokhorenkova et al., *CatBoost: unbiased boosting with categorical features*: `https://arxiv.org/abs/1706.09516`.
- Ke et al., *LightGBM: A Highly Efficient Gradient Boosting Decision Tree*: `https://proceedings.neurips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html`.

## Source-boundary notes

- The official recording was published on 2022-07-16 and runs 1:05:43. It has two teaching parts: Aidan Gomez gives a Transformer origin/intuition recap, then Jannik Kossen and Neil Band present NPT.
- The Transformer recap is historical and conceptual, not a complete derivation of every encoder/decoder block. This note adds standard equations only to make the spoken explanation self-contained.
- “Non-parametric” here means predictions depend explicitly on the input training datapoints at inference time. It does not mean that NPT has no learned parameters; its attention and feed-forward layers are parametric.
- NPT receives the dataset matrix and mask matrix as input. For large datasets, “entire dataset” is approximated with random mini-batches, so a prediction cannot literally inspect every training point in one forward pass.
- Permutation equivariance is with respect to row/datapoint order. Attributes have fixed semantics and are not freely permutable unless the corresponding embedding and task definition are transformed consistently.
- Stochastic feature masking is an auxiliary regularizer; stochastic target masking exposes some training labels so the model can learn relational lookup. Test labels are never revealed.
- The paper reports average method ranks over ten UCI datasets, not one pooled accuracy. AUROC covers four binary datasets, accuracy two multi-class datasets, and RMSE four regression datasets; lower average rank is better.
- Corruption independently permutes each attribute of the *other* rows, preserving approximate column marginals while destroying cross-row relational structure. A performance drop supports reliance on other datapoints but does not identify a unique causal attention path.
- The duplicate/intervention experiment is semi-synthetic. Near-perfect response to intervened duplicate targets shows learned match/look-up/copy behavior in that construction; it is not universal evidence that NPT performs causal inference on arbitrary real data.
- The central scalability limitation is quadratic attention in the number of datapoints inside a batch. Mini-batching changes the available retrieval set and is an approximation, not a free exact speedup.

# CS25 Lecture 06 Source Index

Access date: 2026-08-11.

## Official course sources

- Current Stanford Online video, `wTZ3o36lXoQ`: `https://www.youtube.com/watch?v=wTZ3o36lXoQ`.
- Historical local note referenced Stanford Online ID `GV8-6ZgJVRk`; that page now returns `Video unavailable`. The current official upload has the same lecture topic and is the canonical source for this rewrite.
- Stanford CS25 V1 course page: `https://web.stanford.edu/class/cs25/past/cs25-v1/`.
- Official CS25 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture06.en.srt`, 1,399 parsed captions after replacing the old 3,553-cue repeated track.
- The course page and video description expose no standalone slide PDF. `slides-images/` therefore contains 39 reviewed teaching slides or final progressive-build states recovered from the current official 1080p recording.

## Primary technical sources

- Jaegle et al., *Perceiver: General Perception with Iterative Attention*: `https://arxiv.org/abs/2103.03206`.
- Jaegle et al., *Perceiver IO: A General Architecture for Structured Inputs & Outputs*: `https://arxiv.org/abs/2107.14795`.
- Vaswani et al., *Attention Is All You Need*: `https://arxiv.org/abs/1706.03762`.
- Dosovitskiy et al., *An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale*: `https://arxiv.org/abs/2010.11929`.
- Carion et al., *End-to-End Object Detection with Transformers (DETR)*: `https://arxiv.org/abs/2005.12872`.
- Locatello et al., *Object-Centric Learning with Slot Attention*: `https://arxiv.org/abs/2006.15055`.
- Tancik et al., *Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains*: `https://arxiv.org/abs/2006.10739`.
- Devlin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*: `https://arxiv.org/abs/1810.04805`.
- Clark et al., *CANINE: Pre-training an Efficient Tokenization-Free Encoder for Language Representation*: `https://arxiv.org/abs/2103.06874`.
- Xue et al., *ByT5: Towards a Token-Free Future with Pre-trained Byte-to-Byte Models*: `https://arxiv.org/abs/2105.13626`.
- Teed and Deng, *RAFT: Recurrent All-Pairs Field Transforms for Optical Flow*: `https://arxiv.org/abs/2003.12039`.
- Sun et al., *AutoFlow: Learning a Better Training Set for Optical Flow*: `https://arxiv.org/abs/2104.14544`.
- Wang et al., *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding*: `https://arxiv.org/abs/1804.07461`.

## Source-boundary notes

- The current official upload duration is 58:58 and was published on 2022-07-15. Older third-party indexes and the removed ID may report a longer duration; this rewrite anchors time provenance to the current official upload.
- “General-purpose” means the same attention-based interface can accept different structured arrays with fewer domain-specific architectural assumptions. It does not mean the model is assumption-free, optimal in every domain, or trained jointly on all tasks shown.
- Perceiver reduces the input-length bottleneck by cross-attending from a small latent array to a large input. Latent self-attention still scales quadratically in latent count, and output decoding scales with the number of output queries.
- Linear scaling refers to input size when latent size is fixed. Constants, output size, depth, memory layout, and hardware implementation still matter.
- ImageNet permutation and byte-level language results demonstrate weak dependence on canonical grid/token structure in the tested settings; they do not prove spatial or linguistic structure is useless.
- Optical-flow comparisons are bounded to the datasets, training protocol, and EPE metrics shown. Qualitative colors encode motion vectors and should not be read as semantic segmentation.
- The lecture repeatedly frames a speed-versus-generality Pareto tradeoff. Domain-specific convnets remain valuable when their inductive biases are known and data or latency is limited.

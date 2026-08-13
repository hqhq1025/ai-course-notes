# CS25 Lecture 05 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online video, `U8J32Z3qV8s`: `https://www.youtube.com/watch?v=U8J32Z3qV8s`.
- Stanford CS25 V1 course page: `https://web.stanford.edu/class/cs25/past/cs25-v1/`.
- Official CS25 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture05.en.srt`.
- The course page and video description do not expose a standalone slide PDF. The official recording visibly contains a full-screen deck, so `slides-images/` contains 38 reviewed teaching slides or final progressive-build states recovered from the local 1080p recording.

## Primary technical sources

- Jacobs et al., *Adaptive Mixtures of Local Experts*: `https://doi.org/10.1162/neco.1991.3.1.79`.
- Shazeer et al., *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*: `https://arxiv.org/abs/1701.06538`.
- Kaplan et al., *Scaling Laws for Neural Language Models*: `https://arxiv.org/abs/2001.08361`.
- Raffel et al., *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*: `https://arxiv.org/abs/1910.10683`.
- Lepikhin et al., *GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding*: `https://arxiv.org/abs/2006.16668`.
- Fedus, Zoph, and Shazeer, *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*: `https://arxiv.org/abs/2101.03961`.
- Xue et al., *mT5: A Massively Multilingual Pre-trained Text-to-Text Transformer*: `https://arxiv.org/abs/2010.11934`.
- Sanh et al., *DistilBERT, a Distilled Version of BERT*: `https://arxiv.org/abs/1910.01108`.
- Riquelme et al., *Scaling Vision with Sparse Mixture of Experts*: `https://arxiv.org/abs/2106.05974`.
- Official Mesh TensorFlow implementation repository used by the original line of work: `https://github.com/tensorflow/mesh`.

## Source-boundary notes

- The lecture is about the 2021 Switch Transformer result; Stanford Online uploaded this recording on 2022-07-14. Historical method claims are anchored to the primary papers rather than the later upload date.
- A sparse model's total parameter count is not its per-token active parameter count. The note keeps total parameters, active computation, device memory, communication, and wall-clock time separate.
- The lecture's pretraining plots often use negative log perplexity, for which a larger value is better. This must not be confused with ordinary perplexity, for which a smaller value is better.
- Top-1 routing is presented as a Pareto choice under the measured capacity factors and hardware setup, not as a theorem that top-1 always beats top-2.
- “Parameters for knowledge, FLOPs for reasoning” is explicitly introduced by the speaker as a mostly unsubstantiated hypothesis. The note preserves that epistemic status.
- The trillion-parameter result demonstrates conditional parameter storage and training feasibility; it does not imply that every token executes a trillion parameters or that parameter count alone determines downstream quality.
- Video screenshots are evidence of the original lecture deck. No missing slide, number, or benchmark result is reconstructed or fabricated.

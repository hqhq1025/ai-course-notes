# CS25 Lecture 10 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online official video, `CYaju6aCMoQ`: `https://www.youtube.com/watch?v=CYaju6aCMoQ`.
- Official video title: *Stanford CS25: V2 I Represent part-whole hierarchies in a neural network, Geoff Hinton*.
- Official CS25 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- Stanford CS25 archive page: `https://web.stanford.edu/class/cs25/past/cs25-v2/`. The current page lists Geoffrey Hinton's GLOM talk among prior speakers, but it does not provide sufficiently reliable historical schedule evidence for this recording, so this note does not invent a classroom date.
- Stanford Online published the recording on 2022-08-11; the public video duration is 52:48.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture10.en.srt`, 1,122 parsed captions after replacing the legacy 15,755-line rolling/repeated subtitle dump.
- The video description and current archive expose no standalone slide PDF. A 2-second crop-aware scan of the official 1080p recording produced 1,584 samples and 49 candidates; `slides-images/` contains 32 manually reviewed teaching slides or distinct final states.

## Primary technical sources

- Hinton, *How to represent part-whole hierarchies in a neural network* (GLOM): `https://arxiv.org/abs/2102.12627`.
- Sabour, Frosst, and Hinton, *Dynamic Routing Between Capsules*: `https://arxiv.org/abs/1710.09829`.
- Hinton, Krizhevsky, and Wang, *Transforming Auto-Encoders*: `https://www.cs.toronto.edu/~hinton/absps/transauto6.pdf`.
- Chen et al., *A Simple Framework for Contrastive Learning of Visual Representations* (SimCLR): `https://arxiv.org/abs/2002.05709`.
- Becker and Hinton, *Self-organizing neural network that discovers surfaces in random-dot stereograms*: `https://doi.org/10.1038/355161a0`.
- Vaswani et al., *Attention Is All You Need*: `https://arxiv.org/abs/1706.03762`.
- Devlin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*: `https://arxiv.org/abs/1810.04805`.
- Hinton, Vinyals, and Dean, *Distilling the Knowledge in a Neural Network*: `https://arxiv.org/abs/1503.02531`.
- Anil et al., *Large Scale Distributed Neural Network Training through Online Distillation*: `https://arxiv.org/abs/1804.03235`.
- Mildenhall et al., *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis*: `https://arxiv.org/abs/2003.08934`.

## Source-boundary notes

- GLOM is explicitly presented as an imaginary system, design document, or “vaporware.” The talk mentions toy fragments, but it does not report a trained end-to-end benchmark system. Mechanistic plausibility must not be rewritten as empirical success.
- The GLOM arXiv record has one public version dated 2021-02-25. The later journal publication does not change the historical classroom boundary; this note follows the arXiv design paper and the official recording.
- “Island of agreement” means a spatial region whose same-level embeddings become nearly identical through recurrent bottom-up, top-down, temporal, and lateral interactions. It is not a precomputed segmentation mask and not guaranteed to align with human objects.
- Embedding vectors are dynamic activities, not slowly changing network weights. This distinction is the proposed answer to how fixed hardware can encode a different parse structure for each image.
- The two-dimensional arrows in the slides are diagrams for equality, pose, and coordinate-transform intuition. Real embeddings may be high-dimensional; arrow orientation must not be interpreted as the literal implementation.
- The cube and six-rod demonstrations are psychological arguments about intrinsic coordinate frames and alternative parses. They illustrate motivation, not quantitative validation of GLOM.
- SimCLR is used as a scaffold for agreement and collapse. GLOM does not simply apply image-level contrastive learning: it seeks level-specific local spatial coherence and uses top-down/bottom-up predictions plus attention-weighted consensus.
- GLOM's lateral interaction is a simplified similarity-gated attention mechanism. Calling it a Transformer does not imply the full BERT parameterization, global receptive field, or one-pass inference contract.
- The “transformational random field” and Hough-transform discussion is a design comparison. Direct pairwise part interactions can require many relation-specific messages; part-to-whole voting is proposed as a simpler way to obtain agreement at the parent level.
- The joint identity-pose log-probability basis is a representational hypothesis. Hinton explicitly calls his argument weak; the talk provides no calibrated uncertainty experiment proving neurons implement this exact code.
- Masked reconstruction with roughly ten settling iterations and backpropagation through time is a proposed training route. Consensus/co-distillation is an additional island-forming signal, not a demonstrated guarantee against all collapse or optimization failures.
- Replicating an object-level embedding across locations trades memory for locality, deferred binding, and gradual segmentation. Longer-range sparse attention at higher levels is a computational proposal, not a measured scaling result in this lecture.
- The neural-field ending explains how a shared top-down network can emit different lower-level predictions by conditioning on target location. It is a coordinate-conditioned function analogy, not evidence that GLOM reproduces NeRF or vice versa.

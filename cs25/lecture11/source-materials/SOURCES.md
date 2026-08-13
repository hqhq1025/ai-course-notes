# CS25 Lecture 11 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online official video, `XfpMkf4rD6E`: `https://www.youtube.com/watch?v=XfpMkf4rD6E`.
- Official video title: *Stanford CS25: V2 I Introduction to Transformers w/ Andrej Karpathy*.
- Classroom date stated in the official description: 2023-01-10.
- Stanford Online upload date: 2023-05-19. The legacy note incorrectly used 2023-02-23 and has been replaced rather than patched.
- Public duration: 1:11:40.
- Official CS25 V2 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- Stanford CS25 archive: `https://web.stanford.edu/class/cs25/past/cs25-v2/`.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture11.en.srt`, 1,667 parsed captions.
- Transcript derivatives: `transcript_timed.txt` preserves source intervals; `transcript_clean.txt` supports reading and search.
- The official description exposes no standalone slide PDF. A 2-second scan of the official 1080p recording produced 2,150 samples and 139 high-recall candidates. Manual review retained 61 distinct teaching slides/final states in `slides-images/`.

## Primary technical sources

- Bengio et al., *A Neural Probabilistic Language Model*: `https://www.jmlr.org/papers/v3/bengio03a.html`.
- Sutskever, Vinyals, and Le, *Sequence to Sequence Learning with Neural Networks*: `https://proceedings.neurips.cc/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html`.
- Bahdanau, Cho, and Bengio, *Neural Machine Translation by Jointly Learning to Align and Translate*: `https://arxiv.org/abs/1409.0473`.
- Vaswani et al., *Attention Is All You Need*: `https://arxiv.org/abs/1706.03762`.
- He et al., *Deep Residual Learning for Image Recognition*: `https://arxiv.org/abs/1512.03385`.
- Ba, Kiros, and Hinton, *Layer Normalization*: `https://arxiv.org/abs/1607.06450`.
- Karpathy, official `nanoGPT` repository: `https://github.com/karpathy/nanoGPT`.
- Karpathy, official `minGPT` repository: `https://github.com/karpathy/minGPT`.
- Tiny Shakespeare dataset used by the official repository: `https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt`.
- Devlin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*: `https://arxiv.org/abs/1810.04805`.
- Raffel et al., *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer* (T5): `https://arxiv.org/abs/1910.10683`.
- Dosovitskiy et al., *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (ViT): `https://arxiv.org/abs/2010.11929`.
- Gulati et al., *Conformer: Convolution-augmented Transformer for Speech Recognition*: `https://arxiv.org/abs/2005.08100`.
- Radford et al., *Robust Speech Recognition via Large-Scale Weak Supervision* (Whisper): `https://arxiv.org/abs/2212.04356`.
- Chen et al., *Decision Transformer: Reinforcement Learning via Sequence Modeling*: `https://arxiv.org/abs/2106.01345`.
- Jumper et al., *Highly accurate protein structure prediction with AlphaFold*: `https://www.nature.com/articles/s41586-021-03819-2`.
- Brown et al., *Language Models are Few-Shot Learners* (GPT-3): `https://arxiv.org/abs/2005.14165`.
- Kaplan et al., *Scaling Laws for Neural Language Models*: `https://arxiv.org/abs/2001.08361`.
- Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*: `https://arxiv.org/abs/2201.11903`.

## Source-boundary notes

- The first 10:14 is the course staff's CS25 V2 introduction. Karpathy's lecture begins at 10:14; the note preserves both but distinguishes their speakers and claims.
- The lecture was delivered on 2023-01-10. Statements such as 2,048-token contexts, the state of ChatGPT, or “five years since the Transformer” describe that date, not the state of the field in 2026.
- Karpathy's 2011 handcrafted-feature story is a first-person historical account. It illustrates the fragmented pre-deep-learning workflow; it is not a claim that every computer-vision system used the same descriptors or SVM pipeline.
- The cortex analogy is explicitly speculative. Architectural convergence across domains does not prove that Transformers reproduce biological computation.
- The lecture's “first attention paper I saw / as far as I know” wording is personal historical recollection, not an exhaustive priority claim.
- “Delete the RNNs and keep attention” is a teaching compression. The 2017 Transformer package also contains positional information, residual pathways, normalization, feed-forward networks, masking, embeddings, and optimization choices.
- The claim that the original package reached a strong architecture-space local optimum is an engineering judgment based on later resilience. It is not a theorem and does not imply that every original detail remained unchanged.
- Attention as graph message passing is the lecture's interpretive lens. A fixed connectivity mask and data-dependent attention weights are different objects: the graph may be fixed while message strengths depend on the current activations.
- The nanoGPT walk-through is character-level for pedagogy. Production GPT models use subword tokenization and larger contexts; the core next-token factorization remains the same.
- End-of-text tokens are learned boundary markers, not an imperative that literally clears a hidden-state buffer. A decoder can still attend across a boundary unless masking or training behavior prevents it.
- ViT, Conformer, Decision Transformer, Whisper, and AlphaFold are not identical copy-pastes. The common lesson is token/element sequence modeling plus attention; each system adds domain-specific embeddings, objectives, geometry, convolution, pair representations, or decoding structure.
- AlphaFold2's Evoformer uses attention but is a specialized protein architecture. “At the heart is also a Transformer” must not be rewritten as “AlphaFold is just GPT for proteins.”
- In-context learning as an inner optimization loop is a hypothesis and research interpretation. The lecture presents suggestive work, not proof that every prompt performs literal gradient descent in activations.
- “GPT is a general-purpose computer over text” is a productive analogy about runtime reconfiguration by prompts. It does not establish unrestricted programmability, correctness, or Turing-completeness for a finite deployed model.
- Q&A comments about diffusion-like text revision, scratchpads, external memory, and future product directions are speculative ideas from January 2023. They are included as teacher voice and clearly labeled as such.

## Local-source policy

- `lecture11.mp4` is a local working source and remains ignored.
- `metadata.json` contains stable public fields only; no raw `yt-dlp` dump is committed.
- Every retained slide is cited to an official-video interval. No image is presented as a standalone official slide-deck page because no deck was published with the recording.
- Administrative bumpers, camera-only transitions, exact duplicate frames, and Q&A revisits of already retained slides are intentionally omitted; all 61 distinct teaching states are retained.

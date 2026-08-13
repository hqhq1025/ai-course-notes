# CS25 Lecture 08 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online official video, `pC4zRb_5noQ`: `https://www.youtube.com/watch?v=pC4zRb_5noQ`.
- Stanford CS25 V1 course page: `https://web.stanford.edu/class/cs25/past/cs25-v1/`.
- Official CS25 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- The V1 schedule places Chris Olah's “Interpretability with transformers” lecture on 2021-11-15.
- Stanford Online published the recording on 2022-07-17; the public video duration is 59:34.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture08.en.srt`, 1,557 parsed captions after replacing the old 3,867-cue rolling/repeated track.
- The course page and video description expose no standalone slide PDF. `slides-images/` therefore contains 64 reviewed teaching slides or final progressive-build states recovered from the official 1080p recording.

## Primary technical sources

- Elhage et al., *A Mathematical Framework for Transformer Circuits*: `https://transformer-circuits.pub/2021/framework/index.html`.
- Olsson et al., *In-context Learning and Induction Heads*: `https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html`.
- Archival PDF for the induction-head article: `https://arxiv.org/abs/2209.11895`.
- Kaplan et al., *Scaling Laws for Neural Language Models*: `https://arxiv.org/abs/2001.08361`.
- Brown et al., *Language Models are Few-Shot Learners*: `https://arxiv.org/abs/2005.14165`.
- Vaswani et al., *Attention Is All You Need*: `https://arxiv.org/abs/1706.03762`.
- Olah et al., *The Building Blocks of Interpretability*: `https://distill.pub/2018/building-blocks/`.
- Cammarata et al., *Curve Circuits*: `https://distill.pub/2020/circuits/curve-circuits/`.

## Source-boundary notes

- The recording date, article publication date, and upload date differ. The classroom lecture occurred on 2021-11-15, when Olah explicitly described the induction-head work as unpublished; the Transformer Circuits article was published on 2022-03-08, and Stanford uploaded the video on 2022-07-17. The note preserves the lecture's tentative language and uses the later article only for verification and fuller evidence taxonomy.
- Mechanistic interpretability is one subset of interpretability. Its goal is to reverse engineer internal computations into human-understandable algorithms; success on a circuit does not imply a complete explanation of a model, its training data, or its social behavior.
- Much of the mathematical derivation uses one- and two-layer attention-only transformers with LayerNorm, MLPs, and biases removed. These simplifications make exact algebra possible and are not faithful architectural descriptions of current large language models.
- The lecture's “in-context learning score” compares late-token loss with early-token loss, usually `Loss@500 - Loss@50`. A more negative value means later context tokens are predicted better; the sign must not be silently reversed.
- “Phase change” denotes a sharp empirical change over a narrow training interval and a visible loss bump. It is a hypothesis-generating behavioral observation, not a proof of a thermodynamic phase transition or a mathematically discontinuous optimization trajectory.
- Under the article's row-vector convention, the OV circuit is `W_OV = W_V W_O` and the QK circuit is `W_QK = W_Q W_K^T`. OV controls what information is written; QK controls which source and destination positions interact.
- If an attention pattern is held fixed, an attention-only block is linear in its input. The full model remains nonlinear because the attention pattern is input-dependent through softmax.
- Eigenvalue/eigenvector summaries are most meaningful when a circuit maps a space back to itself, such as token space to token space. Complex spectra can summarize copying/anti-copying tendencies in small attention-only models; the method becomes unreliable when MLP nonlinearities and larger architectures dominate.
- An induction head implements a pattern such as `[A][B] ... [A] -> [B]`, usually through composition with an earlier previous-token head. Positive-copying OV behavior and same-token-matching QK behavior are useful signatures, not a universal necessary-and-sufficient definition for every modern head.
- Small attention-only models have direct ablation evidence that induction heads account for much of the measured in-context-learning score. For large models, the lecture shows temporal co-occurrence between induction-head formation and the behavioral phase change; Olah explicitly calls that evidence correlational.
- Translation and “soft induction” examples show that the mechanism can match analogous rather than identical tokens. They do not prove that all in-context learning, reasoning, or meta-learning in large models is implemented by induction heads.
- The 50--55 minute Lexoscope interaction is low-resolution and rapidly changing. Intermediate demo frames are intentionally omitted; the stable preceding/following slides and spoken cross-lingual example retain the teaching content.

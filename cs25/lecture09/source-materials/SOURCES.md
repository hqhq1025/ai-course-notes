# CS25 Lecture 09 Source Index

Access date: 2026-08-11.

## Official course sources

- Stanford Online official video, `wvE2n8u3drA`: `https://www.youtube.com/watch?v=wvE2n8u3drA`.
- Stanford CS25 V1 course page: `https://web.stanford.edu/class/cs25/past/cs25-v1/`.
- Official CS25 playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`.
- The V1 schedule places Prateek Verma's “Transformers for Applications in Audio, Speech and Music: From Language Modeling to Understanding to Synthesis” lecture on 2021-11-29.
- Stanford Online published the recording on 2022-07-18; the public video duration is 48:18.
- Local official thumbnail: `cover.jpg`.
- Local official manual English captions: `lecture09.en.srt`, 981 parsed captions after replacing the old 2,815-cue rolling/repeated track.
- The course page and video description expose no standalone slide PDF. A 2-second masked scene-difference scan of the official 1080p recording produced 1,449 samples and 119 candidates; `slides-images/` contains 47 manually reviewed teaching slides or distinct progressive states.

## Primary technical sources

- Verma and Chafe, *A Generative Model for Raw Audio Using Transformer Architectures*: `https://arxiv.org/abs/2106.16036`.
- Verma and Smith, *A Framework for Generative and Contrastive Learning of Audio Representations*: `https://arxiv.org/abs/2010.11459`.
- Verma and Berger, *Audio Transformers: Transformer Architectures for Large Scale Audio Understanding. Adieu Convolutions*: classroom-era v1 at `https://arxiv.org/abs/2105.00335v1`.
- van den Oord et al., *WaveNet: A Generative Model for Raw Audio*: `https://arxiv.org/abs/1609.03499`.
- van den Oord, Vinyals, and Kavukcuoglu, *Neural Discrete Representation Learning* (VQ-VAE): `https://arxiv.org/abs/1711.00937`.
- Dhariwal et al., *Jukebox: A Generative Model for Music*: `https://arxiv.org/abs/2005.00341`.
- Fonseca et al., *FSD50K: An Open Dataset of Human-Labeled Sound Events*: `https://arxiv.org/abs/2010.00475`.
- Dosovitskiy et al., *An Image is Worth 16x16 Words* (ViT): `https://arxiv.org/abs/2010.11929`.
- Baevski et al., *wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations*: `https://arxiv.org/abs/2006.11477`.

## Source-boundary notes

- The class occurred on 2021-11-29, while Stanford uploaded the recording on 2022-07-18. Claims such as “current fashion,” “state of the art,” and “what may come next” are historical classroom statements, not descriptions of the audio-model landscape in 2026.
- The arXiv page for `2105.00335` now exposes a substantially later v2 revision from 2025. This note uses the 2021 v1 paper that matches the lecture slides and does not backport later experiments into the class.
- The raw-audio paper evaluates 8-bit next-sample prediction with top-5 accuracy over 256 possible sample states. That metric measures local predictive classification, not perceptual audio quality, musical coherence, latency, or human preference.
- “Adieu WaveNet?” and “Adieu Convolutions” are deliberately provocative slide titles. The evidence is limited to the reported controlled datasets and model families; it does not prove that attention universally dominates convolutional audio systems.
- The lecture moves among waveform samples, spectrograms, filterbanks, learned embeddings, and discrete codebook tokens. These representations have different time resolution, frequency resolution, invertibility, phase information, sequence length, and inductive bias; they must not be treated as interchangeable “audio tokens.”
- A spectrogram is built by windowing a waveform and stacking short-time Fourier magnitudes. Window length and hop size create a time-frequency tradeoff, and magnitude-only views omit phase unless phase is stored or reconstructed separately.
- Sample-level autoregressive modeling has extreme sequence length: ten seconds at 16 kHz contains 160,000 samples. Attention's quadratic cost therefore motivates shorter local contexts, conditioning, latent codes, sparse structure, or alternative sequence models.
- VQ/VQ-VAE converts continuous encoder outputs into nearest codebook entries. The code indices make language modeling possible, but reconstruction quality and codebook collapse determine how much acoustic detail survives.
- The representation-learning comparison uses the same dataset and downstream evaluation to reduce confounding, but linear-probe accuracy does not establish that two representations are equivalent for generation, robustness, transfer, or low-data adaptation.
- Wavelet/pooling results are empirical architectural choices in the paper's setup. Haar averaging adds no learned parameters, but it changes information flow and temporal resolution; improved accuracy does not by itself identify a unique causal reason.
- The learned front-end filters resemble familiar signal-processing objects such as windows, sinusoids, onset-sensitive filters, and task-dependent filterbanks. Visual resemblance is useful mechanistic evidence, not proof that every neuron has a single human-readable function.

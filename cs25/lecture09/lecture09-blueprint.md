# CS25 Lecture 09 Blueprint

## Teaching thesis

Audio makes the Transformer's sequence problem concrete. The same signal can be represented as raw samples, short-time spectra, perceptual filterbanks, learned embeddings, or discrete codebook tokens, and every choice changes sequence length, locality, information loss, and the objective a Transformer can optimize. The note should use the lecture's three papers to teach a common engineering loop: choose a representation, define what the model predicts, control the comparison, inspect what the front end learns, and state exactly what the metric does and does not establish.

## Section sequence

1. Source audit, 2021/2022/2025 version boundary, and lecture roadmap.
2. Transformer history and a mechanism-level intuition for repeated attention plus feature learning.
3. Waveforms, Fourier bases, windowing, STFT, spectrograms, and time-frequency tradeoffs.
4. Seconds-to-milliseconds structure and a representation-choice table.
5. Raw sample autoregression, WaveNet baseline, sequence-length accounting, and next-sample metrics.
6. Transformer versus fixed dilated topology, quadratic cost, and wider-context conditioning.
7. Controlled raw-audio results and the difference between predictive accuracy and perceptual quality.
8. Acoustic-scene applications and why continuous audio must be discretized for language modeling.
9. VQ/VQ-VAE, codebooks, Jukebox-style hierarchies, contrastive learning, and generative code prediction.
10. Predictive representation learning, linear probes, same-data comparisons, and extrapolation limits.
11. Raw-waveform Audio Transformers on FSD50K, wavelet/pooling hierarchy, and result interpretation.
12. Learned front-end filters, task-adaptive auditory representations, final synthesis, and modern extensions.

## Figure spine

- V001--V007: title, roadmap, architecture-history intuition, reusable Transformer components, and scaling context.
- V008--V013: spectrogram construction, representation families, and four waveform time scales.
- V014--V024: raw-audio paper, WaveNet/problem setup, Transformer architecture, quadratic bottleneck, conditioning, and controlled results.
- V025--V037: representation-learning paper, downstream applications, discrete tokens, VQ, Jukebox, contrastive/generative methods, and controlled evidence.
- V038--V047: raw-waveform Audio Transformer, FSD50K, wavelets, architecture, empirical table, learned time-frequency organization, filters, and final thoughts.

## Required teaching scaffolds

- Formula chain for DFT/STFT and spectrogram magnitude, with every symbol explained.
- Sequence-length and attention-cost accounting for raw audio: $n=f_sT$ and $O(n^2)$ pair count.
- Autoregressive factorization for quantized samples and a warning that top-5 accuracy is not perceptual quality.
- Conditional-context diagram/table distinguishing local high-rate samples from compressed long-range context.
- VQ nearest-code formula, straight-through/codebook intuition, reconstruction bottleneck, and codebook-collapse warning.
- Contrastive-versus-generative objective table and a compact InfoNCE-style formula.
- Linear-probe evaluation explanation with same-encoder/same-data controls and remaining confounders.
- Haar averaging/downsampling equations and a pooling-versus-wavelet comparison.
- Dense terminology digestion for waveform, sample rate, spectrogram, phase, filterbank, codebook, latent token, linear probe, and receptive field.
- At least two captioned listings: raw next-sample evaluation and an encode--quantize--predict--decode pipeline.
- At least 18 teacher-voice markers woven into prose and figure explanations.

## Acceptance targets

- Replace the legacy one-image, transcript-thin note completely.
- 40+ PDF pages, all 47 reviewed teaching slides, 18+ high-signal boxes, 18+ teacher-voice markers, 10+ formula blocks, and 2+ captioned listings.
- Explicit source boundaries for the 2021 lecture, 2022 upload, and 2025 Audio Transformers v2 revision.
- Strict coverage checker has no warnings or errors.
- Two successful stabilized XeLaTeX passes with no layout/reference warnings.
- `check_quality.sh` grade `⭐⭐⭐`.
- Canonical visual QA contact sheet and signed report with no unresolved defects.

# Lecture 30 Source Audit

## Official lecture sources

- Stanford CS25 V4 archive: `https://web.stanford.edu/class/cs25/past/cs25-v4/`
  - Classroom date: May 2, 2024.
  - Official title: `Transformers that Transform Well Enough to Support Near-Shallow Architectures`.
  - Speaker: Jake Williams, Drexel University.
  - The schedule frames the talk around non-random parameter initialization, precision language models, limited-resource training, and a localized controller running on Le Potato hardware.
- Stanford Online recording: `https://www.youtube.com/watch?v=zL9B3eXq0gY`
  - Upload date: May 23, 2024.
  - Runtime: 1:19:56.
  - Source resolution: 1920x1080 at approximately 29.97 fps.
  - Merged source SHA-256 used for slide recovery: `71adc491fb7eb029b82da2688af0a45f6f26da8086367eff11fbee3ca8a7342d`.
  - YouTube provides an official `en-US` manual-caption track with 1,487 cues.

## Slide provenance

- Neither the official CS25 V4 page nor the official video description links a standalone deck. A current source search also found no speaker-published copy that could be verified as the classroom deck.
- The official recording therefore acts as the canonical visual source.
- A one-second scan over all 4,796 seconds produced 4,796 samples and 3,409 slide-like frames. Visual-change review yielded 68 high-recall candidates that cluster into 29 independent states.
- Twenty-seven states contain teaching content and are required. The only optional states are the Stanford bumper and the final thanks/contact card.
- Final figures were re-extracted from the verified 1920x1080 recording with crop `1770:996:75:84`, then scaled to 1680x945. This removes the browser chrome and black pillar bars without redrawing slide content.
- Q&A screen sharing repeats warm-start, image-classification, context, and application slides; no duplicate figure is retained solely because it reappears during questions.
- The full video remains in `/tmp` and is not part of the repository.

## Transcript preparation

- The legacy subtitle file was a 327,745-byte rolling-caption dump with repeated text. It has been replaced by the official 119,167-byte manual-caption SRT at SHA-256 `ac99a49f6af9b36287bbfb3d2a00a1cc62f50e2858eedd6c3e083fc1c928844b`.
- The 1,487 manual cues were normalized and merged into 634 readable timed segments in `transcript_timed.txt` and `transcript_clean.txt`.
- `transcript_chunks.md` groups the transcript into five-minute windows for teacher-voice review.
- Caption errors such as `sample` for `SAFFU` near the final Q&A are treated as transcription noise; slide spelling and primary papers control canonical terminology.

## Primary technical references

- Williams and Zhao, `Explicit Foundation Model Optimization with Self-Attentive Feed-Forward Neural Units`, `https://arxiv.org/abs/2311.07510`.
- Williams and Zhao, `Reducing the Need for Backpropagation and Discovering Better Optima With Explicit Optimizations of Neural Networks`, `https://arxiv.org/abs/2311.07498`.
- Zhao and Williams, `Bit Cipher -- A Simple yet Powerful Word Representation System that Integrates Efficiently with Language Models`, `https://arxiv.org/abs/2311.11012`.
- Williams and Heidenreich, `To Know by the Company Words Keep and What Else Lies in the Vicinity`, `https://arxiv.org/abs/2205.00148`.
- Frankle and Carbin, `The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks`, `https://arxiv.org/abs/1803.03635`.
- Warstadt et al., `Findings of the BabyLM Challenge: Sample-Efficient Pretraining on Developmentally Plausible Corpora`, `https://arxiv.org/abs/2310.00915`.

## Evidence boundary

- SAFFU, explicit optimization, bit-cipher, and `precision language model` are the speaker team's research terms and preprint claims. The lecture does not establish them as standard Transformer replacements or independently replicated production results.
- The talk's warm-start curves and edge-controller tables are lecture-time experiments. They support specific tested configurations, not a universal claim that backpropagation or pretraining is unnecessary.
- The claim that a cold-start GPT-2-sized model needs roughly 100 hours on eight A100s is a slide-level rough comparison, not a controlled benchmark matched for implementation, data, kernels, or quality.
- Small-data fit is not broad language generalization. The speaker explicitly distinguishes quickly learning a small corpus or switch task from producing a generally conversational model.
- Cached vector comparisons require fixed embeddings. If embeddings update, the cache becomes stale and the claimed cost reduction changes.
- Dynamic context batching is presented as a context-faithful alternative to document packing, but the speaker says he has not run a direct large-model comparison against an oracle packing implementation.
- The Le Potato demonstration is an early feasibility experiment. The speaker reports multi-second interaction latency, no network dependency, limited binary control, and substantial remaining evaluation work.

## Legacy note repair

- The legacy note used an invented 2026 lecture date, a fabricated Stanford lecture URL, and a shortened title that obscured the real source.
- It mislabeled SAFFU as `SAFU` and added unsupported mechanisms such as chunk-gating journals, drift gates, attention-observability boards, fairness dashboards, governance teams, incident replays, weekly newsletters, RLHF roadmaps, and automated rollback thresholds.
- Those claims do not occur in the official slides, manual transcript, course description, or primary papers and must be removed rather than polished.
- The replacement note will follow the actual two-part lecture: explicit/warm-start optimization for SAFFU-based near-shallow models, followed by application-only edge training for a voice-controlled switch.

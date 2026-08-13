# Lecture 18 Source Audit

## Official Course Sources

- CS25 V2 archive: `https://web.stanford.edu/class/cs25/past/cs25-v2/`
- Official Stanford Online video: `https://www.youtube.com/watch?v=L4DC7e6g2iI`
- Official playlist: `https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM`
- Classroom date: 2023-03-07.
- Video title: `Stanford CS25: V2 I Neuroscience-Inspired Artificial Intelligence`.
- Speakers: Trenton Bricken and Will Dorrell.
- Runtime: `1:22:13`.
- Upload date: 2023-09-01.

The official recording contains two distinct talks. Trenton Bricken presents *Attention Approximates Sparse Distributed Memory* through approximately 00:42:28. Will Dorrell then gives a handwritten lecture on cognitive maps, the hippocampal--entorhinal system, the Tolman--Eichenbaum Machine (TEM), and its relationship to transformers.

The legacy note linked `https://www.youtube.com/watch?v=dEFn6nnoC-8`, which is Trenton Bricken's 2025 PhD defense, not the CS25 lecture. It also covered only the first speaker and invented extensive MoE routing, production monitoring, governance, deployment, and incident-response material. The rewrite uses the official Stanford source and removes all unsupported material.

## Recommended Primary Works

1. Bricken and Pehlevan, *Attention Approximates Sparse Distributed Memory*: `https://proceedings.neurips.cc/paper/2021/hash/8171ac2c5544a5cb54ac0f38bf477af4-Abstract.html`
   - Used to verify the hypersphere-intersection approximation, continuous SDM, the mapping to attention, learned coefficients, and biological interpretation.
2. Whittington et al., *The Tolman--Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation*: `https://www.sciencedirect.com/science/article/pii/S009286742031388X`
   - Used to verify TEM's structural/content factorization, recurrent path integration, Hebbian-like memory, graph generalization, and neural predictions.
3. Whittington et al., *Relating Transformers to Models and Neural Representations of the Hippocampal Formation*: `https://arxiv.org/abs/2112.04035`
   - Used to verify the modern Hopfield/attention correspondence, key--query--value interpretation, and TEM-to-transformer mapping discussed in the second talk.

## Additional Primary Background

- Bricken et al., *Sparse Distributed Memory is a Continual Learner*: `https://openreview.net/forum?id=JknGeelZJpHP`
- Kanerva, *Sparse Distributed Memory and Related Models*: `https://redwood.berkeley.edu/wp-content/uploads/2020/08/KanervaP_SDMrelated_models1993.pdf`
- Behrens et al., *How to Build a Cognitive Map*: `https://www.nature.com/articles/s41593-022-01153-y`

These sources support the historical and mathematical background. They do not justify importing post-lecture interpretability, production, governance, or 2025 thesis-defense claims into the reconstructed 2023 classroom.

## Local Acquisition And Normalization

- `metadata.json` contains stable public metadata for the official Stanford video.
- `lecture18.en.srt` is the official `en-US` manual subtitle track: 1,950 parsed captions / 9,406 normalized lines.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` preserve both speakers' teacher voice and timestamp provenance.
- `lecture18.mp4` is the private 1920x1080 source used for frame recovery. It is ignored and must not be committed.
- `cover.jpg` is the official Stanford Online thumbnail.

## Visual Recovery Audit

- The full 1:22:13 recording was sampled every two seconds.
- Trenton Bricken's standard slide deck produced 86 high-recall candidates; manual review retained 40 distinct teaching states, using final progressive states unless an intermediate slide taught a separate write/read step.
- Will Dorrell's talk uses a live handwritten tablet with black side margins. The second half was reprocessed separately with a `1080x1080` crop around the tablet, producing 175 high-recall candidates; manual review retained 26 complete derivation, evidence, architecture, result, and conclusion states.
- The final visual spine contains 66 images. Standard slides remain full `1920x1080`; handwritten pages use the readable tablet crop rather than preserving empty black margins.
- `lecture18-selection.tsv` records every source candidate, absolute timestamp, and pedagogical treatment.

## Historical And Interpretive Boundary

- Classroom claims are bounded to 2023-03-07.
- “Attention approximates SDM” is a mathematical and computational correspondence under stated normalization/coefficient conditions, not proof that the brain literally runs a trained Transformer.
- The cerebellar circuit mapping is a biologically plausible hypothesis. The speaker explicitly distinguishes implementability from experimental confirmation and describes the real-time synaptic measurements that would test it.
- The second talk argues for a useful two-way relationship between hippocampal models and transformers. TEM is not presented as a drop-in LLM architecture or a complete theory of the hippocampus.
- Place cells, grid cells, cognitive maps, TEM states, positional encodings, and Transformer attention are related at selected functional/computational levels; the note must not collapse them into anatomical identity.

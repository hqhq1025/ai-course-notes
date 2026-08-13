# Lecture 41 Writing Blueprint

## Thesis

Movie Gen's central lesson is not that one proprietary system generated attractive clips. It is that a video generator can be organized as a scalable systems stack: compress media into a feasible spatiotemporal latent, learn a Flow Matching velocity field with a mostly standard bidirectional Transformer, condition on text through explicit interfaces, curate data aggressively, and use a progressive curriculum to reach a 73K-token workload. The same evidence also exposes sharp limits in evaluation, complex interactions, long-duration generation, physics, serving, and synchronized multimodal data.

## Source hierarchy

1. Official Stanford Online recording and refreshed manual `en-US` captions.
2. Movie Gen primary paper for formulas, architecture labels, context length, parallelism, and evaluation definitions.
3. CS25 V5 course row for date, speaker, and talk scope.
4. No standalone public deck is available; the 32 retained recording states are the visual spine.

## Section plan

| Section | Required figures | Mathematical / systems scaffolding | Boxes and teacher voice |
|---|---|---|---|
| Why video generation changed so quickly | 064, 091, 112, 150, 155, 174, 175 | capability taxonomy and evidence limits | sample-quality warning; architecture-unification context |
| Representation before architecture | 177, 178, 181, 182, 185 | tensor shapes, 8x temporal/spatial compression, token-count example | TAE definition; compression warning; VAE/GAN-loss clarification |
| Flow Matching as transport | 187, 188, 189 | interpolation, velocity target, Euler ODE update, symbol explanations | diffusion/flow comparison; step-count latency warning |
| A Llama-shaped video Transformer | 193, 194, 195, 196, 244 | cross-attention, AdaLN, bidirectional MHA, 73K-token attention cost | “random init, not language transfer” warning; terminology table |
| Data and curriculum are part of the model | 247, 250 | filtering pipeline, staged resolution/duration schedule | data cleanliness; long-tail control; infrastructure accounting |
| What the model can do | 257, 305, 337, 374, 388, 419 | task decomposition across base T2V, editing, personalization, audio | world-model claim boundary; separate-model warning |
| How evidence should be read | 433, 434 | net win rate, compute-optimal scaling relation | human-eval caveats; scaling correlation warning |
| Where it fails and what comes next | 460, 464 | long-video token growth, reasoning/verifier loop | complex interaction failure; native multimodal objectives |
| Q\&A engineering boundaries | no new visual | systems, watermarking, synthetic data, serving boundary | teacher-voice synthesis and checklist |

## Coverage guardrails

- Every one of the 32 required images appears exactly once.
- Opening demos are evidence for distinct capabilities, not decoration.
- Every section and non-summary subsection starts with a prose bridge before a figure, formula, table, or listing.
- Important figures receive setup, reading guidance, an evidence limit, and a connection to the surrounding argument.
- First uses of TAE, Flow Matching, latent, AdaLN, MHA, GQA, context length, collective communication, and adversarial loss are defined locally.
- The 00:54:10--01:13:20 Q\&A is synthesized into normal prose and teacher-voice markers rather than appended as a transcript dump.
- Target: at least 20 pages, 20 teaching boxes, 10 formula blocks, 3 captioned listings, 12 teacher-voice markers, and at least 260 prose characters per figure.

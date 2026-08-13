# Lecture 38 Writing Blueprint

## Teaching thesis

The note should teach circuit tracing as a disciplined but incomplete method for turning one forward pass into an interpretable causal hypothesis. The reader should leave with three model-level findings—abstract representations, parallel computation, and planning—and three method-level cautions—replacement-model approximation, unexplained attention, and selective success cases.

## Section plan

### 1. Why study the “biology” of a model?

- Figures 01--04.
- Pair impressive Circassian in-context learning with the leap-day contradiction.
- Define mechanistic interpretability, behavior-level evidence, mechanism-level evidence, and the biology analogy.
- Teacher voice: better capability can make failures subtler rather than remove them.

### 2. From one token to an emergent internal program

- Figures 05--09.
- Explain autoregressive generation, one forward pass, residual-stream state, MLP blocks, attention blocks, and output logits.
- Use a compact flow diagram and formula chain for one-token prediction.
- Define “grown, not built” as an engineering claim about learned internal algorithms, not mysticism.

### 3. Features, replacement models, and attribution graphs

- Figures 10--24.
- Explain polysemantic neurons, feature directions, sparse replacement models, Cross-Layer Transcoders, reconstruction error, attribution edges, pruning, grouping, and interventions.
- Reconstruct the Dallas → Texas → Austin example as an end-to-end workflow.
- Separate descriptive labels, graph attribution, and causal intervention.
- Mandatory warning: attention is reused but not explained.

### 4. Abstract representations across domains

- Figures 25--31.
- Medical case: symptoms, diagnosis, diagnostic criteria, and interventions.
- Multilingual case: language-specific input/output boundary features versus shared semantic middle features.
- Explain feature intersection-over-union and why larger-model sharing is evidence for abstraction, not proof of a single universal language.

### 5. Parallel computation and the addition case study

- Figures 32--43.
- Contrast the model's verbal schoolbook explanation with the traced parallel mechanism.
- Explain coarse sum ranges, final-digit lookup features, recombination, and feature reuse outside arithmetic.
- Connect the case to metacognitive unfaithfulness: fluent explanation is not privileged access to the internal algorithm.

### 6. Parallel competition in hallucinations and jailbreaks

- Figures 44--52.
- Explain the always-on IDK/refusal tendency and inhibition by known-entity features.
- Show how suppression causes guessing and how incorrect suppression can support natural hallucination.
- Explain jailbreaks as competing circuits rather than a single safety switch.
- Keep the claim scoped to these traced examples.

### 7. Planning before the next token

- Figures 53--61.
- Explain rhyme-plan features, forward planning, backward constraint propagation, and intervention results.
- Compare faithful and motivated reasoning graphs.
- Emphasize that observable chain of thought may rationalize a selected answer rather than reveal the computation that produced it.

### 8. What the method proves—and what it misses

- Figure 62 plus Q&A teacher voice.
- Summarize the three findings and the three caveats.
- Discuss attention-mediated strategy selection, success-case bias, reconstruction error, reflection, adaptive compute, and the ambiguity of token-level hallucination labels.
- End with concrete research questions rather than a universal safety prescription.

## Required teaching devices

- At least 18 high-signal boxes distributed across definitions, intuition, and evidence boundaries.
- At least 5 formulas: autoregressive factorization, logits/softmax, sparse reconstruction objective, attribution decomposition, and feature-overlap metric.
- At least 4 captioned listings or pseudocode blocks: forward pass, sparse feature extraction, attribution-graph construction, and intervention test.
- A terminology table covering residual stream, neuron, feature, sparse autoencoder/transcoder, CLT, attribution edge, reconstruction error, inhibition, intervention, and chain-of-thought faithfulness.
- Every figure gets a prose setup and a local reading explanation; dense figures also get an evidence-boundary sentence.
- Target at least 16,500 prose characters so 62 figures remain above the 260-character-per-figure heuristic.

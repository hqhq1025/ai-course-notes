# CS25 V6 Lecture 06 — Writing Blueprint

## Acceptance target

- 45 required official deck pages, each inserted exactly once.
- At least 12,000 Chinese prose characters, targeting more than 260 prose characters per required figure.
- At least 18 high-signal teaching boxes, 10 teacher-voice markers, 8 displayed formula blocks, and 4 captioned listings.
- Strict coverage with zero hard errors or warnings; `⭐⭐⭐`; stable double XeLaTeX; complete signed visual QA.

## Teaching arc

### 1. One model, two information channels

- Slides 002--005.
- Define parametric learning, in-context learning, explicit information, latent information, and usable information.
- Explain why controlled interventions on artificial systems can inform—but not settle—questions about natural intelligence.
- Establish the causal comparison: same dataset, different storage/access route.

### 2. The latent generalization gap

- Slides 007--023.
- Start from the reversal curse and the chat counterexample.
- Explain why `ICL ≅ gradient descent` is a restricted mechanism analogy rather than an equivalence theorem.
- Reconstruct the finetuning-versus-full-context protocol.
- Read reversal and syllogism charts, then remove the pretraining objection with the from-scratch experiment.
- Generalize to codebooks, multi-hop reasoning, alternative goals, and cross-lingual structure.
- Introduce a latent-learning gap metric and separate systematic inference from co-occurrence shortcuts.

### 3. Bridge 1: train-time in-context augmentation

- Slides 025--032.
- Present the offline/online decision tree.
- Explain corpus-level connection generation, augmented fine-tuning, and why this is accessibility transformation rather than information creation.
- Include pseudocode and a compute-accounting equation.
- End with the intractability of enumerating every future use.

### 4. Bridge 2: oracle episodic retrieval

- Slides 033--035.
- Define episodic retrieval, recall, precision, distractors, and oracle assumptions at first use.
- Explain reversal and codebook results.
- Contrast latent-implication retrieval with ordinary fact lookup/RAG.

### 5. Bridge 3: RL for test-time regeneration

- Slides 036--040.
- Define regeneration as producing missing premises or transformations into the model's own context.
- Explain the A/B transfer protocol and distinguish augmentation transfer from reasoning-policy transfer.
- Make reversal the counterexample: exhaustive enumeration is correct but impractical.

### 6. Engineering choice among three bridges

- Slides 041--042.
- Compare train-time compute, inference compute, retriever dependence, coverage, latency, and failure modes.
- Add a decision table and an end-to-end resource budget formula.

### 7. Natural intelligence and complementary memory

- Slides 044--049.
- Treat the brain discussion as a computational analogy after the model evidence is complete.
- Explain slow cortical/statistical integration versus fast episodic storage and retrieval.
- Preserve the speaker's caveat that brains may use better learning rules or additional mechanisms.

### 8. Q&A as engineering constraints

- No new visual nodes; use slide 049 only once in the final synthesis, not as a repeated Q&A backdrop.
- Integrate context sensitivity, scale uncertainty, retrieval engineering, compute tradeoffs, augmentation hallucinations/drift, regularization, and prompt leakage.

## Required concept scaffolds

1. Two-channel information-flow table.
2. Reversal example with forward/reverse conditional notation.
3. Latent information glossary and latent-gap metric.
4. Co-occurrence shortcut warning.
5. In-context augmentation pseudocode.
6. Oracle retrieval precision/recall box.
7. RL regeneration objective and transfer table.
8. Training/test compute budget equation.
9. Complementary-learning-systems comparison table.
10. Final decision checklist.

## Evidence boundaries to repeat in prose

- Do not universalize the ICL advantage.
- Do not equate nonzero accuracy with systematic inference.
- Do not present augmentation as new information creation.
- Do not present oracle retrieval as a solved retriever.
- Do not present RL as solving reversal generally.
- Do not present the hippocampus/neocortex analogy as mechanistic identity.
- Label Q&A estimates and judgments as spoken engineering guidance.

# Lecture 03 Coverage Blueprint

## Teaching thesis

The lecture is not a contest over whether `O(L)` is better than `O(L^2)`. Its deeper claim is that sequence architectures expose different memory interfaces. Attention keeps a token-resolution, database-like cache that excels at exact lookup but inherits the resolution and semantics of the supplied tokens. Modern recurrent/SSM layers compress the stream into a finite state that loses exact details yet gains online processing, state tracking, and an inductive bias toward abstraction. H-Net turns that tradeoff into a learned hierarchy: compress raw data into useful units before asking attention to operate.

## Source graph

- Canonical visual spine: 33 high-resolution states reconstructed from the official 1920x1080 Stanford recording.
- Required visual nodes: 32 independent teaching states; slide 1 is an optional title card.
- Spoken spine: 2,288 English-original automatic-caption cues distilled into 50 teacher-voice rows.
- Speaker-authored conceptual source: Albert Gu's 2025-07-08 Goomba Lab article.
- Lecture-snapshot papers: Mamba, Mamba-2, Mamba-3 v1, H-Net v2, MambaByte, and dnaHNet v3.
- Complete recording audit: 1,999 two-second samples across the lecture and Q&A; sponsor content excluded after approximately 01:06:30.

## Planned sections

1. **Why recurrent/linear models returned**
   - Mamba, xLSTM, DeltaNet, TTT, and production hybrids.
   - Terminology table separating lineage from shared interface.
   - Autoregressive modeling as the comparison lens.
2. **Two memory interfaces**
   - Training versus decoding.
   - Attention/KV cache as token-resolution state.
   - SSM recurrence as compressed fixed-size state.
   - Complexity accounting without equating asymptotics with wall-clock speed.
3. **The three ingredients of modern SSMs**
   - State expansion/capacity.
   - Input-dependent selectivity/gating.
   - Parallel scan and chunked-matmul training.
   - Why Mamba is a synthesis rather than three unrelated inventions.
4. **Autoregressive states, analogies, and hybrids**
   - Every generator has an implicit state.
   - Database/brain analogy and explicit neuroscience warning.
   - Recall versus online state tracking.
   - Hybrid layer ratios as dated empirical evidence, not a law.
5. **Attention needs the right token resolution**
   - Patchification, tokenization, and the modeling role of preprocessing.
   - Tokenizer failure modes versus practical success.
   - Effective-token and hard-attention heuristics.
   - Character/byte and DNA comparisons.
6. **H-Net: learn the hierarchy end to end**
   - Boundary routing, chunk summaries, inner model, dechunking, decoder.
   - Why the inner model may be a Transformer while outer stages favor SSMs.
   - Dynamic chunking as a difficult discrete optimization problem.
7. **Scaling evidence and compression as inductive bias**
   - Data-matched crossover from BPE to learned chunks.
   - Multi-stage hierarchy and optimization costs.
   - Outer-stage Mamba ablation on BPE inputs.
   - dnaHNet and modalities without semantic tokenizers.
8. **Final tradeoffs and research agenda**
   - Efficiency as a red herring when it hides different modeling behavior.
   - Attention's database-like cache and resolution dependence.
   - SSM statefulness, abstraction building, and retrieval limits.
   - FLOPs-to-capabilities criterion.
   - Q&A: hardware/backprop local optima, H-Net scale limits, hierarchical memory, small models, interpretability.

## Formula scaffolding

- Autoregressive factorization and recurrent state update.
- Token-cache memory/compute accounting during decoding.
- Structured SSM recurrence `h_t = A_t h_{t-1} + B_t x_t`, `y_t = C_t^T h_t`.
- State expansion dimensions and information bottleneck intuition.
- Input-dependent selective update and keep/write limiting cases.
- Associative composition for parallel scan.
- Soft attention versus hard-selection intuition.
- H-Net routing probabilities, boundary decisions, and chunk summaries.
- Bits-per-byte and compute-matched comparison definitions.
- Scaling-law line and FLOPs-to-capabilities interpretation.

## Code scaffolding

- Captioned listing comparing attention-cache and recurrent-state decoding.
- Captioned listing for a selective recurrent update.
- Captioned listing for associative-scan composition.
- Captioned listing for H-Net routing/chunking/dechunking.
- Captioned listing for a hybrid recurrent/attention stack.

## Figure treatment

- Every required state appears exactly once and has a concrete source-time provenance.
- Replacement builds for state size, state update, and efficiency remain separate because each carries different teaching content.
- Camera/projector-derived slides are treated as recording captures, not misrepresented as an official downloadable deck.
- Dense model tables and scaling plots receive axis/legend/baseline explanations and explicit non-claims.
- The database/brain figures are always paired with the speaker's own warning that the analogy is coarse.

## Quality risks

- Do not reduce the talk to `linear versus quadratic` complexity.
- Do not claim that every SSM has identical recurrence, kernel, state shape, or training algorithm.
- Do not treat perplexity parity as universal capability parity.
- Do not report 10:1, 4:1, or 3:1 hybrid ratios as architecture constants.
- Do not claim that BPE tokens are intrinsically semantic or that tokenization never works.
- Do not infer universal modality dominance from byte/DNA plots.
- Do not treat H-Net boundaries as ground-truth linguistic tokens.
- Do not present brain analogies, hierarchical memory, biological learning, or tiny-model behavior as settled evidence.
- Do not project post-lecture paper revisions into the 2026-04-16 classroom snapshot.

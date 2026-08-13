# CS25 Lecture 11 Rewrite Blueprint

## Teaching thesis

The lecture should teach one coherent argument rather than reproduce a pile of screenshots:

> Transformer became a cross-domain default because it separates a flexible, data-dependent communication operation from a simple per-token computation operation, packages both in an optimizable residual architecture, and maps efficiently to parallel hardware. Its most surprising consequence is not merely better sequence modeling, but runtime adaptation through context.

The note must preserve the historical sequence, executable nanoGPT path, and Karpathy's teacher voice. It must not retain the legacy note's unrelated sections on RLHF governance, production deployment, drift detection, organizational process, or generic prompt-review workflows.

## Section plan

1. **来源审计与课堂边界**
   - Slides V001--V010; teacher voice T001--T004.
   - Distinguish course-staff introduction, Karpathy lecture, classroom date, upload date, and 2023 knowledge boundary.
   - State the three learning goals and explain why 61 teaching states are retained from video rather than called an official slide PDF.
2. **从手工特征孤岛到统一架构**
   - Slides V011--V022; T005--T008.
   - Handcrafted vision pipeline, field-specific vocabularies, ImageNet scaling transition, architecture convergence, cortex analogy with explicit speculation warning.
3. **Attention 的历史问题链**
   - Slides V023--V028; T009--T013.
   - 2003 neural LM, 2014 seq2seq bottleneck, Bahdanau soft alignment, attention naming story, full Transformer package and architecture resilience.
4. **把 Attention 看成图上的通信**
   - Slides V029--V031; T014--T017.
   - Communication versus computation, directed-graph message passing, Q/K/V semantics, scaled dot-product attention, masks, heads versus layers, self versus cross attention.
5. **nanoGPT：从字符到可生成模型**
   - Slides V032--V043; T018--T023.
   - Tiny Shakespeare, character tokenizer, EOT boundary, block/batch dimensions, input-target shift, embeddings, decoder blocks, MLP, causal self-attention, cross-entropy, training curve, autoregressive generation.
6. **同一骨架的三种模型家族**
   - Slides V044--V046; T024--T026.
   - Encoder, decoder, encoder--decoder, attention connectivity, objectives, GPT/BERT/T5 table, autoregression and diffusion-style revision as dated speculation.
7. **跨模态迁移：先 token 化，再让元素通信**
   - Slides V047--V051; T027--T028 and T033.
   - ViT, Conformer/Whisper, Decision Transformer, AlphaFold2, Tesla-style heterogeneous conditioning, type/position embeddings, domain-specific inductive biases.
8. **Transformer 为什么有效**
   - Slides V052--V060; T029--T032.
   - GPT-3, scaling-law evidence, in-context learning, chain of thought, outer versus inner loop, expressivity/optimizability/efficiency, shallow-wide compute graph, runtime-reconfigurable-computer analogy with limitations.
9. **Q&A、总结与延伸**
   - Slide V061; T034--T035.
   - External scratchpad/tool-use idea, explicit ignorance of ChatGPT internals, nanoGPT direction, final synthesis and primary-source reading route.

## Formula plan

1. Autoregressive factorization: $p(x_{1:T})=\prod_t p(x_t\mid x_{<t})$.
2. Neural probabilistic LM mapping from a fixed context window to next-token distribution.
3. Seq2seq fixed context: $\mathbf c=\mathbf h_T$ and its bottleneck.
4. Bahdanau alignment: $e_{t,s}=a(\mathbf s_{t-1},\mathbf h_s)$, $\alpha_{t,s}=\operatorname{softmax}_s(e_{t,s})$, $\mathbf c_t=\sum_s\alpha_{t,s}\mathbf h_s$.
5. Scaled dot-product attention: $\operatorname{softmax}(QK^\top/\sqrt{d_k}+M)V$.
6. Multi-head attention concatenation and output projection.
7. Transformer block as residual communication plus residual per-token computation.
8. Token and position embedding input representation.
9. Batch input/target shift and tensor shapes.
10. Cross-entropy next-token loss.
11. Causal mask definition.
12. Autoregressive sampling with finite context window.
13. Encoder, decoder, and cross-attention source equations.
14. Schematic scaling law and explicit empirical-status warning.
15. Outer-loop SGD versus inner-loop activation adaptation notation.

## Code plan

- Listing 1: character tokenization and shifted batch construction for Tiny Shakespeare.
- Listing 2: minimal causal self-attention forward pass with shape comments and masking.
- Listing 3: autoregressive generation with context cropping.

## Figure-treatment plan

- All 61 reviewed teaching slides appear exactly once, in filename order and at the point their idea is taught.
- Light title/timeline slides may share one explanation cluster, but each screenshot remains visible and source-labeled.
- Dense slides V013--V016, V024--V031, V034--V045, V047--V060 require local `读图` explanations or tables.
- Every non-summary section/subsection opens with prose before its first figure, formula, table, or listing.
- No images are placed inside teaching boxes.
- Captions state the teaching role; source lines cite official-video time intervals rather than pretending the images are pages of a published deck.

## Terminology scaffolding

Provide first-use definitions or concentrated tables for:

- handcrafted feature, descriptor, SVM, representation learning, inductive bias;
- language model, token, vocabulary, embedding, autoregressive factorization, context window;
- RNN, LSTM, encoder, decoder, hidden state, encoder bottleneck;
- attention score, query, key, value, softmax, causal mask, multi-head, self-attention, cross-attention;
- residual connection, LayerNorm, pre-norm, MLP/feed-forward network, GELU;
- batch size, block size, tensor shape, logits, cross-entropy, negative log-likelihood;
- decoder-only, encoder-only, encoder--decoder, denoising/masked objective;
- patch token, spectrogram, trajectory token, type embedding, positional encoding, conditioning set;
- scaling law, few-shot learning, in-context learning, outer loop, inner loop, chain of thought;
- expressive, optimizable, hardware-efficient, shallow-wide graph, runtime reconfiguration.

## Acceptance gates

- V001--V061 all placed; T001--T035 all synthesized or explicitly represented.
- Legacy non-lecture governance/deployment/team-process material removed.
- `check_note_coverage.py --strict` reports no warnings.
- `check_quality.sh` reports `⭐⭐⭐` with at least 260 prose characters per figure.
- Two stable XeLaTeX passes have no overflow, undefined-reference, rerun, or hyperref warnings.
- PDF contact sheet and selected dense/code pages are manually reviewed; QA checklist is signed.

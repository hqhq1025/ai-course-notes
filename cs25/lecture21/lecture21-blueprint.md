# Lecture 21 Rewrite Blueprint

## Source Boundary

- Canonical recording: Stanford Online `1GbDTTK3aR4`, classroom date 2023-11-07.
- Visual spine: 43 selected teaching states in `slides-images/`, each referenced exactly once.
- Spoken spine: 18 teacher-voice intervals in `lecture21-teacher-voice-ledger.md`.
- Historical boundary: explain the Transformer and its evolution as presented in November 2023; later systems appear only in clearly labeled extension notes when needed.

## Teaching Sequence

1. **Source audit and consolidation thesis**
   - Dartmouth proposal, machine-capacity error, rule writing, data-center Transformers.
2. **From vertical pipelines to general sequence learning**
   - 2009 MT pipelines, 2013 NLP tracks, distributed/contextual representations, seq2seq.
3. **Why recurrence and convolution were not enough**
   - LSTM expressivity, sequential bottleneck, convolutional parallelism and receptive field.
4. **From encoder-decoder attention to self-attention**
   - Content addressing across modalities, parallelism, failed parallel decoding, attention families.
5. **Transformer mechanism and architecture**
   - Q/K/V, scaling, masks, complexity, residual structure, weighted-average intuition, multi-head attention.
6. **Early evidence and interpretability**
   - Machine translation, parsing, attention patterns, supported and unsupported claims.
7. **Evolution of position representations**
   - Absolute versus relative position, bias/rotation, extrapolation, Music Transformer.
8. **Evolution of attention and systems co-design**
   - Long context, local/sparse/routing/memory methods, FLOPs versus bandwidth, MQA/GQA, online softmax.
9. **Transformer as substrate and open research agenda**
   - Other modalities, omitted topics, universal substrate, data-center systems, tools, product loop, research directions and Q&A.
10. **总结与延伸**
   - Consolidation, invariant mechanisms, interface boundaries, evaluation and open questions.

## Required Scaffolding

- First-use glossary for sequence model, distributed/contextual representation, encoder-decoder, recurrence, receptive field, content-based addressing, self-attention, causal mask, Q/K/V, multi-head attention, position encoding, relative position, sparse attention, memory bandwidth, KV cache, MQA/GQA, online softmax, tool use, and conditional independence.
- Formula chain for recurrent state, convolution receptive field, encoder-decoder attention, scaled dot-product attention, causal masking, multi-head attention, positional representations, sparse attention complexity, arithmetic intensity/memory traffic, and non-autoregressive factorization.
- At least three captioned listings:
  1. scaled dot-product attention with causal mask;
  2. multi-head attention and KV-sharing variants;
  3. online softmax or tool-routing pseudocode.
- Dense-term tables for model-era consolidation, attention/position variants, and long-context/systems methods.
- At least 12 explicit `\teachervoice{}` blocks.
- Every non-summary section/subsection opens with prose before figures, formulas, tables, or code.

## Visual Treatment

- Every V001--V043 appears exactly once.
- Dense tables and plots receive local explanations of rows/columns, first comparison, supported claim, and evidence boundary.
- Repeated speaker-window frames, exact slide revisits, administrative bumpers, and repeated `Thanks` pages remain omitted by design.
- Target at least 13,000 prose characters (300+ per figure), 20+ pages, 18+ teaching boxes, 9+ formula blocks, 3+ captioned listings, strict zero-warning coverage, and `⭐⭐⭐` quality.

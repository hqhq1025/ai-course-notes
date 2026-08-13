# Lecture 18 Writing Blueprint

## Historical Boundary

- Reconstruct the 2023-03-07 CS25 class from the official Stanford recording.
- Treat the video as two connected talks with distinct speakers, visual styles, models, and evidence claims.
- Exclude the incorrectly linked 2025 PhD defense and all unsupported MoE, deployment, monitoring, governance, and incident-response material in the legacy draft.

## Teaching Structure

1. **Source audit and two-talk contract**
   - Use V001--V003 and V040--V041.
   - Explain the source correction and the 00:42:28 speaker boundary.
2. **Sparse Distributed Memory motivation and operations**
   - Use V004--V012.
   - Define high-dimensional addresses, Hamming radius, distributed writes, superposition, noisy queries, circle intersections, and majority decoding.
3. **Transformer attention recap**
   - Use V013--V022.
   - Reconstruct Q/K/V, dot product, softmax, value aggregation, and full update with a symbol glossary.
4. **Why attention approximates SDM**
   - Use V023--V030.
   - Derive exponential intersection decay, connect Hamming distance to cosine similarity, present numerical fits, and state normalization/coefficient conditions.
5. **Continuous SDM and Transformer implications**
   - Use V031--V035.
   - Explain continuous vectors, MLP implementation, learned beta, LayerNorm, FFN interpretation, and open questions.
6. **Biological plausibility and cerebellar mapping**
   - Use V036--V040.
   - Map abstract read/write pathways to cerebellar components while preserving the experimental caveat and Q&A tradeoffs.
7. **Cognitive maps and structural generalization**
   - Use V041--V049.
   - Define the problem, review spatial and non-spatial evidence, and motivate reusable graph structure.
8. **Tolman--Eichenbaum Machine**
   - Use V050--V059.
   - Explain content/structure separation, LEC/MEC/hippocampal roles, recurrent state, Hebbian memory, graph inference, grid-like codes, and rapid learning.
9. **TEM, modern Hopfield networks, and Transformers**
   - Use V060--V066.
   - Derive query/key/value memory retrieval, causal restriction, context scaling, architecture correspondence, and limitations.
10. **Final synthesis**
   - Compare two routes from neuroscience to Transformer-like computation: SDM geometry/cerebellar circuitry and hippocampal structural memory.

## Figure Treatment

- Reference all 66 selected assets exactly once.
- Standard slides remain full 1920x1080; handwritten pages use the readable 1080x1080 tablet crop.
- Progressive standard-slide builds keep distinct write/read steps; handwritten derivations keep complete final states rather than every pen stroke.
- Before each figure cluster, state the question; after it, explain objects/axes, supported claim, and non-claim.

## Mathematical And Algorithmic Scaffolding

- Binary SDM write/read equations and majority decoder.
- Scaled dot-product attention and Q/K/V symbol definitions.
- Approximate exponential decay of hypersphere intersection and Hamming/cosine relation.
- Continuous SDM/attention correspondence with effective coefficient.
- TEM recurrent structural update, associative memory, and modern Hopfield softmax retrieval.
- At least three captioned listings: SDM read/write, attention update, and structural-memory retrieval.

## Quality Targets

- 66 teaching images, each referenced exactly once.
- At least 18,000 prose characters and 260+ characters per image.
- At least 16 teaching boxes and 10 teacher-voice markers.
- At least 7 displayed formula blocks with immediate symbol explanations.
- At least 3 captioned `lstlisting` blocks.
- Every major section ends with `本章小结`; final section is `总结与延伸`.
- Strict coverage, `⭐⭐⭐`, stabilized two-pass XeLaTeX, and signed visual QA.

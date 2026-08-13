# CS25 V6 Lecture 08 — Writing Blueprint

## Teaching objective

Explain how modern multimodal systems transfer the LLM scaling recipe while changing the representation, objective, and parameter-routing choices required by images, audio, video, and embodiment. The note must distinguish four ideas that are often collapsed into one label: multimodal input, non-text generation, shared sequence modeling, and physical-world intelligence.

## Source boundary

- Canonical visual source: the 56-page official deck linked from the Stanford course schedule.
- Canonical spoken source: the official 01:04:39 Stanford Online recording and manual `en-US` captions.
- Prepared talk: 00:00:49--00:41:39; Q&A: 00:41:49--01:04:31.
- Full visual audit: 776 five-second samples across 13 contact sheets. No deck-external whiteboard, demo, question card, or teaching diagram appears.
- Deck pages 053--055 describe Thinking Machines Interaction Models but are skipped in the actual recording and therefore remain optional deck-only appendix nodes.
- The lecture is explicitly based on public material; do not imply private Thinking Machines implementation details.

## Visual plan

- Required pages: 37.
- Optional pages: 19 title, progressive-build, duplicate, or recording-skipped pages.
- Every required page appears exactly once.
- Progressive builds collapse to pages 005, 010, 019, 021, 039, and 051; page 033 is retained as the clean first MoT routing state before the dense final architecture.
- Dense result slides 026, 030, 032, 039--046, 048, 051, and 052 receive local reading guides.

## Section plan

1. **从语言模型到原生多模态**
   - Slides 005--008.
   - Define symbolic sequence modeling, native multimodality, digital information processing, and physical-world intelligence.
   - Preserve the public-material disclaimer and the speaker's motivation.

2. **统一序列接口：representation, autoregression, objective**
   - Slides 010--015.
   - Explain discrete tokens versus continuous token-like vectors.
   - Derive mixed-sequence autoregression and masked text-only loss.
   - Contrast understanding-only multimodal LLMs with omni output models.

3. **把 LLM scaling recipe 迁移到多模态**
   - Slides 019 and 021.
   - Four pillars: instruction following, multimodal planning, scale, and architecture sparsity.
   - Use the two research questions as the rest-of-note roadmap.

4. **Chameleon：彻底离散化的 early fusion**
   - Slides 022--026.
   - VQ-VAE codebook formula, interleaving, multitask behavior, and representation bottlenecks.
   - Warning: one token interface does not imply one representation is optimal for every task.

5. **Transfusion：同一 backbone，不同预测目标**
   - Slides 027--030.
   - Diffusion forward process, noise-prediction loss, and joint AR-plus-diffusion objective.
   - Emphasize that generation and understanding may require different image representations.

6. **MoT：modality-aware sparsity 与 deterministic routing**
   - Slides 031--044.
   - Start from the shared-backbone baseline and modality-gap evidence.
   - Compare MoT deterministic routing with learned Mixture-of-Experts routing.
   - Read matched-scale experiments, generation samples, MoE composition, capacity allocation, freezing, and asynchronous extension.
   - Preserve the Q&A result that image-generation specialization did not automatically improve image understanding.

7. **架构走向现实：BAGEL 与 π0.7**
   - Slides 045--046.
   - BAGEL's split between image understanding and generation plus language-mediated planning.
   - π0.7's multimodal steering context and embodiment boundary.

8. **理解与生成能否正迁移**
   - Slides 047--052.
   - Map both transfer directions.
   - Explain language compression, visual redundancy, perceptual loss mismatch, and why low loss does not guarantee useful generation.
   - Separate digital multimodal processing from spatial-temporal and robotic intelligence.

9. **Q&A：设计轴与未解问题**
   - No additional figure required; Q&A remains grounded in slide 056 background shown throughout.
   - Cover self-attention as the fusion path, objective-versus-parameter separation, video world models, bitmap text thought experiment, object-centric representations, spatial reasoning humility, and language as a current but not logically necessary reasoning skeleton.

10. **总结与延伸**
    - Slide 056.
    - Give a design checklist across representation, loss, routing, capacity, transfer, latency, and embodiment.
    - End with evidence-graded open problems rather than product speculation.

## Formula and code plan

- Mixed-modal autoregressive factorization.
- Masked text-only cross-entropy.
- Omni joint loss with per-modality weights.
- VQ nearest-code assignment and reconstruction/commitment intuition.
- Diffusion forward process and noise-prediction loss.
- Transfusion joint autoregressive-diffusion objective.
- MoT deterministic modality routing and active-parameter accounting.
- Learned MoE gating versus deterministic modality routing.
- Temporal redundancy and effective sample-size intuition.
- Six captioned listings: sequence packing, text-only mask, VQ tokenization, Transfusion objective, MoT routing, and frozen-backbone modality extension.

## Acceptance gate before completion

- 20+ pages, 10+ teaching boxes, 37 required figures exactly once.
- Teacher voice woven through normal prose with explicit markers.
- Dense terminology table for VQ-VAE, VAE, diffusion, early fusion, MoT, MoE, modality gap, and omni model.
- Strict coverage with no warnings.
- Two-pass XeLaTeX with no unresolved references or overfull/underfull boxes.
- `tools/scripts/check_quality.sh` grade `⭐⭐⭐`.
- Full rendered PDF contact-sheet review and signed QA report.

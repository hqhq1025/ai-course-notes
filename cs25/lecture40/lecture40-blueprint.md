# Lecture 40 Writing Blueprint

## Teaching thesis

The note should explain why Diffusion Transformers are not merely “UNet replaced by Transformer.” The architecture shift reorganizes patch tokenization, time/text conditioning, normalization, attention cost, modality interaction, parameter sharing, and structural control. The reader should be able to derive original DiT, compare PixArt/SANA/MMDiT/DiT-Air, and judge quality-efficiency claims without confusing backbone simplicity with end-to-end training simplicity.

## Section plan

### 1. Diffusion as an iterative system, not a single model

- Deck pages 04--14.
- Explain iterative denoising, text conditioning, VAE latents, text encoders, denoiser, scheduler, diffusion loss, and flow-matching velocity.
- Separate objective/path design from backbone parameterization.

### 2. The giant UNet and the path through UViT

- Deck pages 15--21.
- Decompose stems, down/up blocks, ResNet blocks, transformer blocks, sampling, and skip connections.
- Explain why custom-block complexity and Transformer ecosystem transfer motivate DiT.

### 3. Original DiT from ViT primitives

- Deck pages 22--34.
- Cover patchification, timestep embedding, class embedding, combined condition, adaLN scale/shift/gates, output decoding, zero initialization, and scaling curves.
- Derive adaLN-Zero and explain why identity initialization stabilizes deep residual training.

### 4. PixArt-α: from class labels to natural-language prompts

- Deck pages 35--40.
- Explain text encoders, cross-attention, timestep modulation, shared adaLN parameters, compact-model results, and the distinction between architecture and training recipe.

### 5. High-resolution efficiency and SANA

- Deck pages 41--44.
- Derive quadratic token cost at 4K latent resolution.
- Explain linear self-attention, retained cross-attention, Mix-FFN, and speed-quality evaluation.

### 6. MMDiT/SD3 and modality-specific parameterization

- Deck pages 45--54.
- Explain separate modality spaces, separate adaLN/QKV, concatenated joint attention, evidence plots, scaling, and hybrid MMDiT/DiT block schedules.
- Preserve the Q\&A caveat that this rationale is heuristic rather than a proof of optimality.

### 7. How much can be shared? DiT-Air

- Deck pages 55--58.
- Compare shared adaLN, shared QKVO, shared MLP, self+cross attention, and full MMDiT.
- Treat parameter sharing as a Pareto problem across quality, memory, FLOPs, and implementation complexity.

### 8. Structural controls, video, and next-generation architectures

- Deck pages 59--65.
- Distinguish spatially aligned controls from subject/edit conditions.
- Cover video positional encoding and 3D attention cost, in-context generation, Playground v3/FuseDiT/OmniGen, Diffusers implementations, MoE, training, post-training, and evaluation gaps.

## Required teaching devices

- At least 20 high-signal boxes distributed across definitions, resource accounting, implementation details, and evidence boundaries.
- At least 12 formulas: forward noising, denoising/noise prediction, flow matching, patch count, attention complexity, timestep embedding, adaLN, gated residual block, decoding, linear attention, MMDiT joint attention, and parameter-sharing accounting.
- At least 4 captioned listings: diffusion system pass, DiT block, MMDiT block, and architecture Pareto evaluation.
- A terminology table covering scheduler, denoiser, latent diffusion, VAE, U-Net, DiT, timestep embedding, adaLN-Zero, cross-attention, linear attention, MMDiT, QK-Norm, GQA, RoPE, and structural control.
- Every required page gets a prose setup and local explanation; dense architecture/result slides also need a reading guide and evidence boundary.
- Target at least 17,000 prose characters so 62 figures remain above the 260-character-per-figure heuristic.

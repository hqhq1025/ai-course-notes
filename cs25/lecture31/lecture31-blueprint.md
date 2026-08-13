# Lecture 31 Writing Blueprint

## 1. Source boundary and lecture thesis

- Use states 002--003.
- Correct the legacy 2026 date to the official classroom date, 2024-05-09.
- Frame the talk as a lecture-time map from LLM objectives and systems to VLMs, image/video generation, and research bets.
- State that no standalone deck was linked; the verified 1080p recording is the visual source of truth.

## 2. Three LLM moments

- Use states 004--006.
- Explain MLM, autoregression, GLM blank infilling, scaling-law compute allocation, task adaptation, and the difference between a lecture claim and an established law.
- Preserve the speaker's history-of-beliefs framing and add a warning that equal pretraining loss does not universally imply equal downstream behavior.

## 3. Architecture and training systems

- Use states 008--011.
- Add a dense terminology table for decoder-only, pre-norm, RoPE, GQA, GLU, MoE, ZeRO, activation checkpointing, tensor parallelism, pipeline parallelism, collectives, context parallelism, Ring Attention, and Ulysses.
- Derive memory sharding and communication roles with first-use definitions.
- Connect long context to prefill latency and load balance rather than presenting it as free context length.

## 4. Alignment and the data thesis

- Use states 012--014.
- Contrast expert SFT, teacher-generated data, PPO/RLHF, reward models, DPO, and on-policy preference pairs.
- Make the CogQA example a worked comparison of architecture-level, algorithm-level, and data/context-level solutions.

## 5. VLM bridge architectures

- Use states 016--024.
- Progress from BLIP-2 to LLaVA, CogVLM, CogAgent, Vary, and GLM-4V.
- Explain frozen spaces, projection layers, vision experts, cross attention, stride convolution, high-resolution token cost, OCR, grounding, and GUI actions.
- Treat benchmark tables and demos as task-specific evidence, not general intelligence proof.

## 6. Autoregression versus diffusion

- Use states 026--032.
- Explain image tokenization, universal sequence formats, representation loss, sequential decoding, DDPM forward/reverse processes, SNR, Relay Diffusion, distillation, DiT adaptive normalization, and MM-DiT experts.
- Keep the speaker's Q&A uncertainty: diffusion has practical parallelism/spatial advantages, not a proof that autoregression cannot match quality.

## 7. Video generation and research agenda

- Use states 033--035.
- Decompose Sora-like progress into 3D latents, scale, high resolution, context-parallel infrastructure, recaptioning, and coverage.
- Time-bound the predictions to May 2024 and distinguish demos from broad real-world deployment.
- Turn the final advice into a matrix of objectives, resources, risks, and suggested problems.

## 8. Q&A, synthesis, and self-test

- Integrate long-context prefill cost, data-versus-architecture nuance, CogVLM/CogAgent differences, physical-world learning limits, and reasoning-path context.
- End with a three-layer synthesis: representation, optimization/systems, and data/evaluation.
- Include formulas, four captioned code/listing blocks, chapter summaries, and primary-source reading.

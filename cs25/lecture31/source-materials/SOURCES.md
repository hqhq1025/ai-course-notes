# Lecture 31 Source Materials

## Canonical lecture source

- Official CS25 V4 course page: `https://web.stanford.edu/class/cs25/past/cs25-v4/`.
- Official Stanford Online recording: `https://www.youtube.com/watch?v=cYfKQ6YG9Qo`.
- Official title: `Stanford CS25: V4 I From Large Language Models to Large Multimodal Models`.
- Speaker: Ming Ding, Zhipu AI.
- Classroom date from the official description and course schedule: 2024-05-09.
- Upload date: 2024-05-30.
- Duration: 4,803 seconds; verified source resolution: 1920x1080.
- Video SHA-256: `7a45f3ace06a0aa432154d57ca142611f81b020f1336fd87b1c6ea4b1ad8d44f`.
- Manual `en-US` subtitle SHA-256: `d35e18c2aa3cc7a37592423b6c942d15a426f49f1a48d4653e841bf6df2bf841`.

## Slide provenance

- Neither the official CS25 V4 page nor the official video description links a standalone deck. A source search found papers and project repositories but no speaker-published classroom deck that could be byte-verified.
- The official recording therefore acts as the canonical visual source.
- A one-second scan over all 4,803 seconds produced 4,803 samples and 4,710 slide-like frames. Visual-change review yielded 76 high-recall candidates.
- After removing repeated shares, animation transitions, changing frames inside one embedded video, three pure dividers, bumpers, and the closing card, 31 independent teaching states remain required.
- Final figures were re-extracted from the verified 1920x1080 recording with crop `1416:796:252:237`, preserving the shared slide exactly while removing Zoom borders and the speaker tile.
- The full recording remains under `/tmp` and is not part of the repository.

## Transcript preparation

- The legacy subtitle was a 229,556-byte rolling-caption SRT with 2,621 timestamp lines and mixed CRLF/LF endings.
- It has been replaced by the official 77,296-byte manual `en-US` SRT and normalized to LF. The repository copy parses into 983 timestamped caption segments.
- `transcript_timed.txt`, `transcript_clean.txt`, and `transcript_chunks.md` preserve the teacher voice and five-minute review windows.
- Caption errors are corrected only when slide text or a primary source makes the intended term unambiguous.

## Primary technical references

- Du et al., `GLM: General Language Model Pretraining with Autoregressive Blank Infilling`, `https://arxiv.org/abs/2103.10360`.
- Kaplan et al., `Scaling Laws for Neural Language Models`, `https://arxiv.org/abs/2001.08361`.
- Ouyang et al., `Training language models to follow instructions with human feedback`, `https://arxiv.org/abs/2203.02155`.
- Burns et al., `Weak-to-Strong Generalization`, `https://arxiv.org/abs/2312.09390`.
- Rafailov et al., `Direct Preference Optimization`, `https://arxiv.org/abs/2305.18290`.
- Rajbhandari et al., `ZeRO: Memory Optimizations Toward Training Trillion Parameter Models`, `https://arxiv.org/abs/1910.02054`.
- Shoeybi et al., `Megatron-LM`, `https://arxiv.org/abs/1909.08053`.
- Liu et al., `Ring Attention with Blockwise Transformers for Near-Infinite Context`, `https://arxiv.org/abs/2310.01889`.
- Jacobs et al., `DeepSpeed Ulysses`, `https://arxiv.org/abs/2309.14509`.
- Li et al., `BLIP-2`, `https://arxiv.org/abs/2301.12597`.
- Liu et al., `Visual Instruction Tuning` (LLaVA), `https://arxiv.org/abs/2304.08485`.
- Wang et al., `CogVLM: Visual Expert for Pretrained Language Models`, `https://arxiv.org/abs/2311.03079`; official repository `https://github.com/THUDM/CogVLM`.
- Hong et al., `CogAgent: A Visual Language Model for GUI Agents`, `https://arxiv.org/abs/2312.08914`.
- Wei et al., `Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models`, `https://arxiv.org/abs/2312.06109`.
- Ding et al., `CogView`, `https://arxiv.org/abs/2105.13290`; Ding et al., `CogView2`, `https://arxiv.org/abs/2204.14217`.
- Ho et al., `Denoising Diffusion Probabilistic Models`, `https://arxiv.org/abs/2006.11239`.
- Teng et al., `Relay Diffusion`, `https://arxiv.org/abs/2309.03350`.
- Zheng et al., `CogView3`, `https://arxiv.org/abs/2403.05121`; official repository `https://github.com/THUDM/CogView3`.
- Peebles and Xie, `Scalable Diffusion Models with Transformers`, `https://arxiv.org/abs/2212.09748`.
- Esser et al., `Scaling Rectified Flow Transformers for High-Resolution Image Synthesis`, `https://arxiv.org/abs/2403.03206`.
- Hong et al., `CogVideo`, `https://arxiv.org/abs/2205.15868`; current official repository `https://github.com/THUDM/CogVideo`.
- Gadre et al., `Language Models Scale Reliably With Over-Training and on Downstream Tasks`, `https://arxiv.org/abs/2403.08540`.
- Snell et al., `Same Pre-training Loss, Better Downstream`, `https://arxiv.org/abs/2409.01236` (post-lecture counterexample used only in the extension/evidence-boundary discussion).

## Evidence boundary

- This is a May 2024 lecture. Product status, benchmark leadership, download counts, and forecasts are reported as lecture-time statements, not current facts.
- The slide claim that downstream performance is a unary function of pretraining loss is a strong empirical position, not a universal theorem. Architecture, tokenizer, data mixture, optimization path, and evaluation can separate models at similar loss; later work is listed as a counterexample.
- Scaling-law plots support fitted regimes and compute-allocation decisions; they do not imply guaranteed gains outside the measured distribution or under unchanged data quality.
- CogVLM, CogAgent, Vary, and GLM-4V benchmark tables compare specific model versions and protocols. They do not prove broad multimodal intelligence or production robustness.
- A browser-navigation trace is a demonstration, not an estimate of autonomous-agent reliability, security, or long-horizon success.
- The lecture's GLM-4V slide predates a stable public technical report for that exact displayed system. Its architecture/result claims are therefore attributed to the slide and transcript rather than silently backfilled from a later model version.
- Diffusion's parallel sampling and 2D dependency advantages explain practical success, but the speaker explicitly declines to give a definitive proof that autoregression is intrinsically inferior.
- Sora-like ingredients are an engineering hypothesis distilled from public observations in May 2024. The slide is not a controlled ablation of Sora.
- Forecasts about “one or two years,” embodied AI impact, speech, and video understanding are preserved as the speaker's dated research advice.

## Legacy note repair

- The legacy note used an invented 2026-04-04 lecture date even though the official class date is 2024-05-09.
- It included unsupported monitoring, drift-detection, rollback, governance, fairness, privacy, and deployment checklists that do not appear in the lecture slides or transcript.
- It reduced the visual source to the thumbnail and omitted the actual 31-page teaching spine.
- The replacement note follows the real lecture: three LLM moments; architecture, systems, alignment, and data; BLIP-2/LLaVA/CogVLM/CogAgent/Vary/GLM-4V; autoregressive and diffusion generation; video scaling; dated research directions; and Q&A limits.

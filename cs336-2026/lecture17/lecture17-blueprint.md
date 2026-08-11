# Lecture 17 Blueprint — Multimodal Models

Narrative question: Transformer 只处理 token，图像与视频怎样被编码、对齐、注入和生成？

1. Multimodal system 的两个问题：understanding 与 generation。
2. ViT、CLIP、SigLIP：把视觉映射到语言可对齐的 representation。
3. LLaVA：vision encoder + projector + LM，训练阶段和数据。
4. LLaVA-OneVision：any-resolution、multi-image/video 与 cross-modal transfer。
5. Qwen-VL → Qwen2-VL → Qwen3-VL：dynamic resolution、MRoPE、DeepStack、long context。
6. Chameleon：离散 image tokens、VQ-VAE、统一生成与稳定性问题。
7. Design ledger：token budget、information density、loss balance、data curriculum。

Teacher voice: build `lecture17-teacher-voice-ledger.md` from `transcript_timed.txt` and executable `text(...)` nodes. Preserve source-backed motivations, caveats, and judgments in `课堂提示`; keep additional evaluation or deployment recommendations as note-authored synthesis.

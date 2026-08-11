# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture17`

## Files

- `cover.jpg`
- `lecture-manifest.md`
- `lecture17-blueprint.md`
- `lecture17-coverage.md`
- `lecture17-manifest.md`
- `lecture17-notes.pdf`
- `lecture17-notes.tex`
- `lecture17-slides.py`
- `lecture17.en-orig.srt`
- `lecture17.en.srt`
- `lecture17.info.json`
- `lecture17.jpg`
- `lecture_17.py`
- `metadata.json`
- `transcript_clean.txt`
- `transcript_timed.txt`

## Local Visual Assets

- `images/chameleon-example.png`
- `images/chameleon.png`
- `images/clip-code.png`
- `images/clip-efficiency.png`
- `images/clip.png`
- `images/llava-architecture.png`
- `images/llava-example.png`
- `images/llava-gen.png`
- `images/llava-onevision-anyres.png`
- `images/llava-onevision-data-1.png`
- `images/llava-onevision-data-2.png`
- `images/llava-onevision-modalities.png`
- `images/llava-onevision-training.png`
- `images/llava-onevision-transfer-s1.png`
- `images/llava-onevision-transfer-s2.png`
- `images/llava-onevision-transfer-s8.png`
- `images/llava-onevision.png`
- `images/multimodality.png`
- `images/qwen-vl-examples.png`
- `images/qwen-vl-stage1.png`
- `images/qwen-vl-stage2.png`
- `images/qwen-vl-stages.png`
- `images/qwen2-vl-architecture.png`
- `images/qwen2-vl-capabilities.png`
- `images/qwen2-vl-mrope.png`
- `images/qwen3-vl-pretraining.png`
- `images/qwen3-vl-results.png`
- `images/qwen3-vl.png`
- `images/siglip-code.png`
- `images/siglip-parallelism.png`
- `images/vit.png`
- `images/vq-vae.png`
- `official-images/chameleon-example.png`
- `official-images/chameleon.png`
- `official-images/clip-code.png`
- `official-images/clip-efficiency.png`
- `official-images/clip.png`
- `official-images/llava-architecture.png`
- `official-images/llava-example.png`
- `official-images/llava-gen.png`
- `official-images/llava-onevision-anyres.png`
- `official-images/llava-onevision-data-1.png`
- `official-images/llava-onevision-data-2.png`
- `official-images/llava-onevision-modalities.png`
- `official-images/llava-onevision-training.png`
- `official-images/llava-onevision-transfer-s1.png`
- `official-images/llava-onevision-transfer-s2.png`
- `official-images/llava-onevision-transfer-s8.png`
- `official-images/llava-onevision.png`
- `official-images/multimodality.png`
- `official-images/qwen-vl-examples.png`
- `official-images/qwen-vl-stage1.png`
- `official-images/qwen-vl-stage2.png`
- `official-images/qwen-vl-stages.png`
- `official-images/qwen2-vl-architecture.png`
- `official-images/qwen2-vl-capabilities.png`
- `official-images/qwen2-vl-mrope.png`
- `official-images/qwen3-vl-pretraining.png`
- `official-images/qwen3-vl-results.png`
- `official-images/qwen3-vl.png`
- `official-images/siglip-code.png`
- `official-images/siglip-parallelism.png`
- `official-images/vit.png`
- `official-images/vq-vae.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | section | yes | `lecture17-slides.py:main` | Lecture 17: multimodal models |
| py-002 | text | optional | `lecture17-slides.py:main` | So far: language models |
| py-003 | text | optional | `lecture17-slides.py:main` | > text ⇒ text |
| py-004 | text | optional | `lecture17-slides.py:main` | The world is multimodal: |
| py-005 | figure | yes | `lecture17-slides.py:main` | images/multimodality.png |
| py-006 | text | optional | `lecture17-slides.py:main` | Ultimate goal: **omni model** |
| py-007 | text | optional | `lecture17-slides.py:main` | - Input any combination of modalities (understanding) |
| py-008 | text | optional | `lecture17-slides.py:main` | - Output any combination of modalities (generation) |
| py-009 | text | optional | `lecture17-slides.py:main` | Where we are today: |
| py-010 | text | optional | `lecture17-slides.py:main` | - Transformers work really well. So we gotta use them. |
| py-011 | text | optional | `lecture17-slides.py:main` | - Transformers speak tokens (discrete or continuous), where a token represents some ~semantic... |
| py-012 | text | optional | `lecture17-slides.py:main` | - Therefore, we must convert everything into tokens. |
| py-013 | text | optional | `lecture17-slides.py:main` | - Note: we had to do this with text (recall the tokenization lecture). |
| py-014 | text | optional | `lecture17-slides.py:main` | - For non-text modalities, this is more challenging... |
| py-015 | text | optional | `lecture17-slides.py:main` | Questions: |
| py-016 | text | optional | `lecture17-slides.py:main` | 1. How do we input non-text data (e.g., understand images)? |
| py-017 | text | optional | `lecture17-slides.py:main` | 2. How do we output non-text data (e.g., generate audio)? |
| py-018 | text | optional | `lecture17-slides.py:main` | Summary: |
| py-019 | text | optional | `lecture17-slides.py:main` | - Frontier models are expected to be multimodal (natively multimodal, omni) |
| py-020 | text | optional | `lecture17-slides.py:main` | - Fundamental challenge: how to encode non-text modalities? |
| py-021 | text | optional | `lecture17-slides.py:main` | - Comprehension and generation might demand different things (semantics versus finer-grained ... |
| py-022 | text | optional | `lecture17-slides.py:main` | - Balance images + video (lower information density) and text for training stability |
| py-023 | text | optional | `lecture17-slides.py:main` | - Continuous encoders + Transformer + diffusion models for generation |
| py-024 | text | optional | `lecture17-slides.py:clip` | CLIP (Contrastive Language-Image Pretraining) |
| py-025 | text | optional | `lecture17-slides.py:clip` | Context: |
| py-026 | text | optional | `lecture17-slides.py:clip` | - Computer vision models were trained on annotated images. |
| py-027 | text | optional | `lecture17-slides.py:clip` | - Question: is it possible to leverage the much larger amount of (image, caption) pairs? |
| py-028 | figure | yes | `lecture17-slides.py:clip` | images/clip.png |
| py-029 | text | optional | `lecture17-slides.py:clip` | Method: |
| py-030 | text | optional | `lecture17-slides.py:clip` | - Get a batch of (image, text) examples (e.g., 32768) |
| py-031 | text | optional | `lecture17-slides.py:clip` | - Encode each image and each text |
| py-032 | text | optional | `lecture17-slides.py:clip` | - For each image, prefer its aligned text over other texts |
| py-033 | text | optional | `lecture17-slides.py:clip` | - For each text, prefer its aligned image over other images |
| py-034 | figure | yes | `lecture17-slides.py:clip` | images/clip-code.png |
| py-035 | text | optional | `lecture17-slides.py:clip` | Data: |
| py-036 | text | optional | `lecture17-slides.py:clip` | - Searched for 500K queries, get ~20K (image, text) pairs per query |
| py-037 | text | optional | `lecture17-slides.py:clip` | - Trained on 400M image-text pairs |
| py-038 | text | optional | `lecture17-slides.py:clip` | - Didn't release the dataset |
| py-039 | text | optional | `lecture17-slides.py:clip` | - Reproduced in OpenCLIP (using LAION-5B dataset, which used CLIP for filtering) |
| py-040 | text | optional | `lecture17-slides.py:clip` | Data processing |
| py-041 | text | optional | `lecture17-slides.py:clip` | - Images come in all resolutions (arbitrary W x H) |
| py-042 | text | optional | `lecture17-slides.py:clip` | - Resize using bicubic interpolation so shorter side is 336 pixels |
| py-043 | text | optional | `lecture17-slides.py:clip` | - Center crop (cuts off borders to get 336 x 336) |
| py-044 | text | optional | `lecture17-slides.py:clip` | Vision encoder: |
| py-045 | text | optional | `lecture17-slides.py:clip` | - Experimented with ResNet-50 and Vision Transformers |
| py-046 | figure | yes | `lecture17-slides.py:clip` | images/vit.png |
| py-047 | text | optional | `lecture17-slides.py:clip` | - Attention pooling: do QKV with query = global average of activations |
| py-048 | text | optional | `lecture17-slides.py:clip` | - Best model: ViT-L/14@336px (L = large, 14x14 patches, 3 channels, trained on 336x336 resolu... |
| py-049 | text | optional | `lecture17-slides.py:clip` | Text encoder: |
| py-050 | text | optional | `lecture17-slides.py:clip` | - GPT-2 Transformer (63M parameters, 12 layers) |
| py-051 | text | optional | `lecture17-slides.py:clip` | - Encode [BOS] ... [EOS], return [EOS] activation at highest layer |
| py-052 | text | optional | `lecture17-slides.py:clip` | Headline result: |
| py-053 | text | optional | `lecture17-slides.py:clip` | - On ImageNet, zero-shot CLIP outperformed ResNet-50 trained on 1.2M ImageNet images |
| py-054 | text | optional | `lecture17-slides.py:clip` | Ablation: |
| py-055 | text | optional | `lecture17-slides.py:clip` | - Alternative: predict text from images directly |
| py-056 | text | optional | `lecture17-slides.py:clip` | - Much less compute efficient compared to CLIP-style ranking |
| py-057 | figure | yes | `lecture17-slides.py:clip` | images/clip-efficiency.png |
| py-058 | text | optional | `lecture17-slides.py:clip` | Summary: |
| py-059 | text | optional | `lecture17-slides.py:clip` | - Encoding of images captures semantics given by (noisy) text |
| py-060 | text | optional | `lecture17-slides.py:clip` | - Design decisions chosen based on image classification (not very fine-grained) |
| py-061 | text | optional | `lecture17-slides.py:clip` | - Technical: requires large batch sizes, softmax operation over full batch |
| py-062 | text | optional | `lecture17-slides.py:siglip` | SigLIP (Sigmoid Loss for Language Image Pre-Training) |
| py-063 | text | optional | `lecture17-slides.py:siglip` | Objective: |
| py-064 | text | optional | `lecture17-slides.py:siglip` | - CLIP: multiclass classification for (text, image) versus (text, image') for all image' |
| py-065 | text | optional | `lecture17-slides.py:siglip` | - SigLIP: binary classification for (text, image) - aligned or not? |
| py-066 | figure | yes | `lecture17-slides.py:siglip` | images/siglip-code.png |
| py-067 | text | optional | `lecture17-slides.py:siglip` | Data: |
| py-068 | text | optional | `lecture17-slides.py:siglip` | - WebLI dataset: O(billion) (image, text) pairs |
| py-069 | text | optional | `lecture17-slides.py:siglip` | - Scraped from the Internet |
| py-070 | text | optional | `lecture17-slides.py:siglip` | - Used automatic OCR to extract text from images |
| py-071 | text | optional | `lecture17-slides.py:siglip` | - Keep 10% highest quality |
| py-072 | text | optional | `lecture17-slides.py:siglip` | - Supports 100 languages |
| py-073 | text | optional | `lecture17-slides.py:siglip` | Efficiency: |
| py-074 | text | optional | `lecture17-slides.py:siglip` | - CLIP: 10 days on 256 TPUv3 |
| py-075 | text | optional | `lecture17-slides.py:siglip` | - SigLIP: 5 days on 32 TPUv4 (lower FLOP/s than TPUv3) - much faster! |
| py-076 | figure | yes | `lecture17-slides.py:siglip` | images/siglip-parallelism.png |
| py-077 | text | optional | `lecture17-slides.py:siglip` | Batch size: |
| py-078 | text | optional | `lecture17-slides.py:siglip` | - Decouple batch size from loss |
| py-079 | text | optional | `lecture17-slides.py:siglip` | - Better than CLIP for <16K batch sizes |
| py-080 | text | optional | `lecture17-slides.py:siglip` | - Go up to 1M batch size, but 32K is enough |
| py-081 | text | optional | `lecture17-slides.py:llava` | LLaVA (Large Language and Vision Assistant) |
| py-082 | text | optional | `lecture17-slides.py:llava` | Vision encoder: CLIP |
| py-083 | text | optional | `lecture17-slides.py:llava` | Text decoder: Vicuna (LLaMA fine-tuned on ShareGPT conversations) |
| py-084 | text | optional | `lecture17-slides.py:llava` | Data: |
| py-085 | text | optional | `lecture17-slides.py:llava` | - MS COCO has images annotated with bounding boxes and Mechanical Turk captions |
| py-086 | text | optional | `lecture17-slides.py:llava` | - Prompt GPT-4 with captions or detected objects and generate questions or conversations |
| py-087 | text | optional | `lecture17-slides.py:llava` | - Pair generations with original images |
| py-088 | text | optional | `lecture17-slides.py:llava` | - 158K examples |
| py-089 | figure | yes | `lecture17-slides.py:llava` | images/llava-gen.png |
| py-090 | text | optional | `lecture17-slides.py:llava` | Model: |
| py-091 | text | optional | `lecture17-slides.py:llava` | - Encode images with CLIP (ViT-L/14) |
| py-092 | text | optional | `lecture17-slides.py:llava` | - Linear projection (W) into embedding space (Flamingo and Q-former are more complex) |
| py-093 | figure | yes | `lecture17-slides.py:llava` | images/llava-architecture.png |
| py-094 | text | optional | `lecture17-slides.py:llava` | Training: |
| py-095 | text | optional | `lecture17-slides.py:llava` | - Stage 1 (alignment): freeze vision encoder and language model, only train W |
| py-096 | text | optional | `lecture17-slides.py:llava` | - Stage 2 (fine-tuning): freeze vision encoder and train W and language model |
| py-097 | figure | yes | `lecture17-slides.py:llava` | images/llava-example.png |
| py-098 | text | optional | `lecture17-slides.py:llava_onevision` | LLaVA OneVision |
| py-099 | text | optional | `lecture17-slides.py:llava_onevision` | - Latest version in the LLaVA series (after LLaVA 1.5, LLaVA-Next) |
| py-100 | text | optional | `lecture17-slides.py:llava_onevision` | - Handle multiple images, video |
| py-101 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision.png |
| py-102 | text | optional | `lecture17-slides.py:llava_onevision` | - Vision encoder: SigLIP (use grid features before and after last Transformer layer) |
| py-103 | text | optional | `lecture17-slides.py:llava_onevision` | - Text decoder: Qwen-2 72B |
| py-104 | text | optional | `lecture17-slides.py:llava_onevision` | - Projector: 2-layer MLP |
| py-105 | text | optional | `lecture17-slides.py:llava_onevision` | Data processing: |
| py-106 | text | optional | `lecture17-slides.py:llava_onevision` | - Preserving high resolution is important (e.g., for OCR) |
| py-107 | text | optional | `lecture17-slides.py:llava_onevision` | - CLIP resizes and crops to 336x336, which loses information |
| py-108 | text | optional | `lecture17-slides.py:llava_onevision` | - Solution: AnyRes, introduced in LLaVA 1.5 |
| py-109 | text | optional | `lecture17-slides.py:llava_onevision` | - Break up image into a x b pieces (matching resolution of vision encoder), encode, concatenate |
| py-110 | text | optional | `lecture17-slides.py:llava_onevision` | - If too many tokens (original image is too high resolution), then use bilinear interpolation |
| py-111 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-anyres.png |
| py-112 | text | optional | `lecture17-slides.py:llava_onevision` | Handle 3 types of input (single image, multiple images, video): |
| py-113 | text | optional | `lecture17-slides.py:llava_onevision` | - Goal: make all of the modalities produce roughly the same length |
| py-114 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-modalities.png |
| py-115 | text | optional | `lecture17-slides.py:llava_onevision` | - Single image: use higher resolution |
| py-116 | text | optional | `lecture17-slides.py:llava_onevision` | - Multiple images: use base resolution for each image |
| py-117 | text | optional | `lecture17-slides.py:llava_onevision` | - Video: use lower resolution for each frame |
| py-118 | text | optional | `lecture17-slides.py:llava_onevision` | Data: |
| py-119 | text | optional | `lecture17-slides.py:llava_onevision` | - Philosophy: quality over quantity |
| py-120 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-data-1.png |
| py-121 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-data-2.png |
| py-122 | text | optional | `lecture17-slides.py:llava_onevision` | Training: |
| py-123 | text | optional | `lecture17-slides.py:llava_onevision` | - Philosophy: easier to harder |
| py-124 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-training.png |
| py-125 | text | optional | `lecture17-slides.py:llava_onevision` | Transfer between modalities: |
| py-126 | text | optional | `lecture17-slides.py:llava_onevision` | - Single image data for diagrams and charts, but generalize to multi-image |
| py-127 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-transfer-s1.png |
| py-128 | text | optional | `lecture17-slides.py:llava_onevision` | - OCR on single image data, relational reasoning from multi-image data, generalize to GUI-bas... |
| py-129 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-transfer-s2.png |
| py-130 | text | optional | `lecture17-slides.py:llava_onevision` | - Visual prompting (circle) in single images, generalize to videos |
| py-131 | figure | yes | `lecture17-slides.py:llava_onevision` | images/llava-onevision-transfer-s8.png |
| py-132 | text | optional | `lecture17-slides.py:llava_onevision` | Summary: |
| py-133 | text | optional | `lecture17-slides.py:llava_onevision` | - Standard VLM template: vision encoder + projector + LM |
| py-134 | text | optional | `lecture17-slides.py:llava_onevision` | - Most work goes into data curation (heavy on synthesized, task-specific data) |
| py-135 | text | optional | `lecture17-slides.py:llava_onevision` | - Open-source (released model weights and data) |
| py-136 | text | optional | `lecture17-slides.py:qwen_vl` | Qwen-VL |
| py-137 | text | optional | `lecture17-slides.py:qwen_vl` | Architecture: |
| py-138 | text | optional | `lecture17-slides.py:qwen_vl` | - Vision encoder: OpenCLIP's ViT-bigC (14x14 patches) |
| py-139 | text | optional | `lecture17-slides.py:qwen_vl` | - Adaptor: one layer cross-attention, incorporate 2D positional encodings, maps to fixed leng... |
| py-140 | text | optional | `lecture17-slides.py:qwen_vl` | - Special tokens: <img>, <box>, <ref> |
| py-141 | text | optional | `lecture17-slides.py:qwen_vl` | Training: |
| py-142 | figure | yes | `lecture17-slides.py:qwen_vl` | images/qwen-vl-stages.png |
| py-143 | text | optional | `lecture17-slides.py:qwen_vl` | - Stage 1: large-scale low quality data; freeze LM, train vision encoder + adaptor |
| py-144 | figure | yes | `lecture17-slides.py:qwen_vl` | images/qwen-vl-stage1.png |
| py-145 | text | optional | `lecture17-slides.py:qwen_vl` | - Stage 2: higher quality task-specific data, increase resolution; train all parameters |
| py-146 | figure | yes | `lecture17-slides.py:qwen_vl` | images/qwen-vl-stage2.png |
| py-147 | text | optional | `lecture17-slides.py:qwen_vl` | - Stage 3: instruction tuning data; freeze visual encoder, train adaptor + LM |
| py-148 | figure | yes | `lecture17-slides.py:qwen_vl` | images/qwen-vl-examples.png |
| py-149 | text | optional | `lecture17-slides.py:qwen2_vl` | Qwen2-VL |
| py-150 | text | optional | `lecture17-slides.py:qwen2_vl` | Visual encoder: larger ViT (675M) |
| py-151 | figure | yes | `lecture17-slides.py:qwen2_vl` | images/qwen2-vl-architecture.png |
| py-152 | text | optional | `lecture17-slides.py:qwen2_vl` | - Key: dynamic resolution to handle varying resolutions |
| py-153 | text | optional | `lecture17-slides.py:qwen2_vl` | - Each 224 x 224 patch encoded with ViT/14, compress every 2x2 => 66 tokens |
| py-154 | text | optional | `lecture17-slides.py:qwen2_vl` | - Video: sample 2 frames/sec, max 16384 tokens |
| py-155 | text | optional | `lecture17-slides.py:qwen2_vl` | Multimodal Rotary Position Embedding (MRoPE): |
| py-156 | figure | yes | `lecture17-slides.py:qwen2_vl` | images/qwen2-vl-mrope.png |
| py-157 | text | optional | `lecture17-slides.py:qwen2_vl` | Initialize LM with Qwen2 and vision encoder from DFN |
| py-158 | text | optional | `lecture17-slides.py:qwen2_vl` | Training (similar to Qwen-VL): |
| py-159 | text | optional | `lecture17-slides.py:qwen2_vl` | - Stage 1: train only visual encoder |
| py-160 | text | optional | `lecture17-slides.py:qwen2_vl` | - Stage 2: train all parameters |
| py-161 | text | optional | `lecture17-slides.py:qwen2_vl` | - Stage 3: train language model on instruction following datasets |
| py-162 | text | optional | `lecture17-slides.py:qwen2_vl` | Many capabilities: |
| py-163 | figure | yes | `lecture17-slides.py:qwen2_vl` | images/qwen2-vl-capabilities.png |
| py-164 | text | optional | `lecture17-slides.py:qwen3_vl` | Qwen3-VL |
| py-165 | figure | yes | `lecture17-slides.py:qwen3_vl` | images/qwen3-vl.png |
| py-166 | text | optional | `lecture17-slides.py:qwen3_vl` | Language model: |
| py-167 | text | optional | `lecture17-slides.py:qwen3_vl` | - Qwen-3 models (dense and MoE models up to 235B-A22B) |
| py-168 | text | optional | `lecture17-slides.py:qwen3_vl` | - Long context understanding (256K) |
| py-169 | text | optional | `lecture17-slides.py:qwen3_vl` | Vision encoder: |
| py-170 | text | optional | `lecture17-slides.py:qwen3_vl` | - SigLIP-2 (same architecture as SigLIP) |
| py-171 | text | optional | `lecture17-slides.py:qwen3_vl` | - Interleaved MRoPE: distribute all axes (temporal, width, height) to low- and high-frequency... |
| py-172 | text | optional | `lecture17-slides.py:qwen3_vl` | ... [t w h t w h t w h t w h] rather than [t t t t w w w w h h h h] |
| py-173 | text | optional | `lecture17-slides.py:qwen3_vl` | - Add explicit video timestamps (as separate tokens rather in positional embeddings) |
| py-174 | text | optional | `lecture17-slides.py:qwen3_vl` | - Square-root-normalized per-token loss: balance text and multimodal data (video examples are... |
| py-175 | text | optional | `lecture17-slides.py:qwen3_vl` | Adapter: |
| py-176 | text | optional | `lecture17-slides.py:qwen3_vl` | - DeepStack: cross-layer fusion to inject visual information into multiple layers |
| py-177 | text | optional | `lecture17-slides.py:qwen3_vl` | Training: |
| py-178 | text | optional | `lecture17-slides.py:qwen3_vl` | - Pre-training has 4 stages (train adapter, train all parameters on 8K, 32K, 256K lengths) |
| py-179 | figure | yes | `lecture17-slides.py:qwen3_vl` | images/qwen3-vl-pretraining.png |
| py-180 | text | optional | `lecture17-slides.py:qwen3_vl` | - Post-training: SFT on long CoT data, knowledge distillation, RL |
| py-181 | figure | yes | `lecture17-slides.py:qwen3_vl` | images/qwen3-vl-results.png |
| py-182 | text | optional | `lecture17-slides.py:qwen3_vl` | Summary: |
| py-183 | text | optional | `lecture17-slides.py:qwen3_vl` | - SOTA performance |
| py-184 | text | optional | `lecture17-slides.py:qwen3_vl` | - Lots of data work, but not many details |
| py-185 | text | optional | `lecture17-slides.py:qwen3_vl` | - Minor but potentially important architectural improvements |
| py-186 | text | optional | `lecture17-slides.py:qwen3_vl` | - Scale up |
| py-187 | text | optional | `lecture17-slides.py:chameleon` | Chameleon |
| py-188 | text | optional | `lecture17-slides.py:chameleon` | So far: VLMs encode images (via CLIP or SigLIP), inject into LM |
| py-189 | text | optional | `lecture17-slides.py:chameleon` | Disadvantage: can't generate images (need diffusion) |
| py-190 | text | optional | `lecture17-slides.py:chameleon` | Chameleon: map everything into discrete tokens |
| py-191 | text | optional | `lecture17-slides.py:chameleon` | Advantage: can analyze and generate images in a uniform way |
| py-192 | figure | yes | `lecture17-slides.py:chameleon` | images/chameleon.png |
| py-193 | figure | yes | `lecture17-slides.py:chameleon` | images/chameleon-example.png |
| py-194 | text | optional | `lecture17-slides.py:chameleon` | Vision encoder |
| py-195 | text | optional | `lecture17-slides.py:chameleon` | - Key difference: encoder needs to map to discrete tokens (so we can generate them) |
| py-196 | text | optional | `lecture17-slides.py:chameleon` | - VQ-VAE (Vector Quantized Variational Autoencoder) |
| py-197 | text | optional | `lecture17-slides.py:chameleon` | - Idea: map image to a discrete codebook, decode back to image and minimize reconstruction loss |
| py-198 | figure | yes | `lecture17-slides.py:chameleon` | images/vq-vae.png |
| py-199 | text | optional | `lecture17-slides.py:chameleon` | - Encodes 512 x 512 image into 1024 tokens (codebook of size 8192) |
| py-200 | text | optional | `lecture17-slides.py:chameleon` | - Train a new BPE tokenizer |
| py-201 | text | optional | `lecture17-slides.py:chameleon` | Training: |
| py-202 | text | optional | `lecture17-slides.py:chameleon` | - Stage 1 (80%): large-scale, unsupervised (2.9T text tokens, 1.5T text/image tokens, 400B te... |
| py-203 | text | optional | `lecture17-slides.py:chameleon` | - Stage 2 (20%): 50% of stage 1 data, 50% of high quality data |
| py-204 | text | optional | `lecture17-slides.py:chameleon` | Training stability |
| py-205 | text | optional | `lecture17-slides.py:chameleon` | - Text tokens have low entropy, image tokens have high entropy, leads to norm growth, logit d... |
| py-206 | text | optional | `lecture17-slides.py:chameleon` | - Fixes: QK norm, z-loss regularization |
| py-207 | text | optional | `lecture17-slides.py:chameleon` | Summary: |
| py-208 | text | optional | `lecture17-slides.py:chameleon` | - Elegant (just autoregressive modeling of discrete tokens) |
| py-209 | text | optional | `lecture17-slides.py:chameleon` | - Not as performant (discretization loses information - think OCR) |
| py-210 | text | optional | `lecture17-slides.py:chameleon` | - Training with multiple modalities is tricky |

## Existing Note

- `lecture17-notes.tex`

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.

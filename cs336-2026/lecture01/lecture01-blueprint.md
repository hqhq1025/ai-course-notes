# Lecture 01 Blueprint

## Goal
Regenerate Lecture 01 as a self-contained, new-standard CS336 note covering all executable-source teaching clusters and all local official image assets.

## Section Plan

### 1. 本讲总览：为什么要从零构建语言模型
- Covers: welcome, course staff, from-scratch philosophy.
- Required visual: `course-staff.png` with read-the-figure explanation.
- Teaching boxes: course main thread, API abstraction warning.

### 2. 工业化与尺度
- Covers: course motivation, industrialization, GPT-4 opacity, scale caveats, Roller FLOPs, emergence, transferable knowledge, Bitter Lesson.
- Required visuals: `industrialisation.jpg`, `gpt4-no-details.png`, `roller-flops.png`, `wei-emergence-plot.png`, `divine-benevolence.png`.
- Required treatments: read-the-figure for every visual, FLOPs vs wall-clock warning, emergence over-interpretation warning.
- Required formulas: `accuracy = efficiency x resources` with symbol explanations.

### 3. 语言模型发展版图
- Covers: pre-neural, neural ingredients, foundation models, scaling, open models, agents.
- Required background: Shannon entropy and n-gram diagram.
- Required terminology digestion: LSTM, neural LM, seq2seq, attention, Adam, Transformer, MoE, GPipe, ZeRO, Megatron-LM.
- Required table: early foundation/scaling/open model phases.

### 4. 课程机制
- Covers: executable lecture, logistics, assignment structure, AI policy.
- Required code: executable lecture mini pattern.
- Required warning: coding agents can bypass learning if used as answer machines.

### 5. 课程版图
- Covers: basics, systems, scaling laws, data, alignment.
- Required visuals: `transformer-architecture.png`, `compute-memory.png`, `dgx-b200-system-topology.png`, `prefill-decode.png`, `chinchilla-isoflop.png`, `marin-loss-forecast.jpg`, `pile-chart.png`.
- Required treatments: read-the-figure for every visual; connect each to future lectures.

### 6. Tokenization
- Covers: tokenizer interface, tokenized example, character/byte/word tokenizer tradeoffs, BPE, assignment 1.
- Required visual: `tokenized-example.png`.
- Required code: tokenizer interface, BPE merge.
- Required warning: UNK token and BPE off-by-one.

### 7. 总结与延伸
- Synthesize industrialization, scaling caveats, history, course units, and tokenization.

## QA Requirements
- `tools/scripts/check_quality.sh cs336-2026/lecture01/lecture01-notes.tex` reports `⭐⭐⭐`.
- `check_note_coverage.py` warnings are reviewed against this coverage matrix.
- `render_pdf_qa.py` contact sheet is generated and manually inspected.

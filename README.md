# AI Course Notes

CS / AI / LLM 相关公开课的中文讲义，基于视频字幕、课程 slides 和公开视频整理。

当前已收录：
- `CS336 (Spring 2025)`：`17/17`
- `CS224N (Spring 2024)`：`17/17`
- `CS231N (Spring 2025)`：`18/18`
- 合计：`52` 份可编译 PDF 讲义

## 仓库说明

- 每讲目录通常包含字幕、封面、slides 原文件、抽取后的 `slides-images/`、LaTeX 源文件和编译出的 PDF。
- `download_all.sh`：批量下载字幕和封面。
- `download_slides.sh`：批量下载 slides 并抽取讲义插图。

## 课程列表

### Stanford CS336: Language Modeling from Scratch (Spring 2025)

| # | 主题 | PDF | 状态 |
|---|------|-----|------|
| 1 | 课程导论与整体地图 | [lecture01-notes.pdf](cs336/lecture01/lecture01-notes.pdf) | ✅ |
| 2 | Building a Model in PyTorch | [lecture02-notes.pdf](cs336/lecture02/lecture02-notes.pdf) | ✅ |
| 3 | Architectures, Hyperparameters | [lecture03-notes.pdf](cs336/lecture03/lecture03-notes.pdf) | ✅ |
| 4 | Mixture of Experts | [lecture04-notes.pdf](cs336/lecture04/lecture04-notes.pdf) | ✅ |
| 5 | GPUs | [lecture05-notes.pdf](cs336/lecture05/lecture05-notes.pdf) | ✅ |
| 6 | Kernels, Triton | [lecture06-notes.pdf](cs336/lecture06/lecture06-notes.pdf) | ✅ |
| 7 | Parallelism 1 | [lecture07-notes.pdf](cs336/lecture07/lecture07-notes.pdf) | ✅ |
| 8 | Distributed Training Across Multiple GPUs | [lecture08-notes.pdf](cs336/lecture08/lecture08-notes.pdf) | ✅ |
| 9 | Scaling Laws 1 | [lecture09-notes.pdf](cs336/lecture09/lecture09-notes.pdf) | ✅ |
| 10 | Inference | [lecture10-notes.pdf](cs336/lecture10/lecture10-notes.pdf) | ✅ |
| 11 | Scaling Laws 2 | [lecture11-notes.pdf](cs336/lecture11/lecture11-notes.pdf) | ✅ |
| 12 | Evaluation | [lecture12-notes.pdf](cs336/lecture12/lecture12-notes.pdf) | ✅ |
| 13 | Data | [lecture13-notes.pdf](cs336/lecture13/lecture13-notes.pdf) | ✅ |
| 14 | 数据过滤与去重 | [lecture14-notes.pdf](cs336/lecture14/lecture14-notes.pdf) | ✅ |
| 15 | Alignment - SFT/RLHF | [lecture15-notes.pdf](cs336/lecture15/lecture15-notes.pdf) | ✅ |
| 16 | Reinforcement Learning from Verifiable Rewards | [lecture16-notes.pdf](cs336/lecture16/lecture16-notes.pdf) | ✅ |
| 17 | Policy Gradient Mechanics and GRPO | [lecture17-notes.pdf](cs336/lecture17/lecture17-notes.pdf) | ✅ |

**资源**：[课程官网](https://stanford-cs336.github.io/) · [YouTube 播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) · [Slides 仓库](https://github.com/stanford-cs336/spring2025-lectures)

### Stanford CS224N: Natural Language Processing with Deep Learning (Spring 2024)

| # | 主题 | PDF | 状态 |
|---|------|-----|------|
| 1 | Intro and Word Vectors | [lecture01-notes.pdf](cs224n/lecture01/lecture01-notes.pdf) | ✅ |
| 2 | Word Vectors and Language Models | [lecture02-notes.pdf](cs224n/lecture02/lecture02-notes.pdf) | ✅ |
| 3 | Backpropagation and Neural Networks | [lecture03-notes.pdf](cs224n/lecture03/lecture03-notes.pdf) | ✅ |
| 4 | Dependency Parsing | [lecture04-notes.pdf](cs224n/lecture04/lecture04-notes.pdf) | ✅ |
| 5 | Recurrent Neural Networks | [lecture05-notes.pdf](cs224n/lecture05/lecture05-notes.pdf) | ✅ |
| 6 | Seq2Seq and Machine Translation | [lecture06-notes.pdf](cs224n/lecture06/lecture06-notes.pdf) | ✅ |
| 7 | Attention and LLM Intro | [lecture07-notes.pdf](cs224n/lecture07/lecture07-notes.pdf) | ✅ |
| 8 | Transformers | [lecture08-notes.pdf](cs224n/lecture08/lecture08-notes.pdf) | ✅ |
| 9 | Pretraining | [lecture09-notes.pdf](cs224n/lecture09/lecture09-notes.pdf) | ✅ |
| 10 | Post-training - RLHF, SFT, DPO | [lecture10-notes.pdf](cs224n/lecture10/lecture10-notes.pdf) | ✅ |
| 11 | Benchmarking and Evaluation | [lecture11-notes.pdf](cs224n/lecture11/lecture11-notes.pdf) | ✅ |
| 12 | Efficient Neural Network Training | [lecture12-notes.pdf](cs224n/lecture12/lecture12-notes.pdf) | ✅ |
| 13 | Brain-Computer Interfaces for Speech | [lecture13-notes.pdf](cs224n/lecture13/lecture13-notes.pdf) | ✅ |
| 14 | Reasoning and Agents | [lecture14-notes.pdf](cs224n/lecture14/lecture14-notes.pdf) | ✅ |
| 15 | Life After DPO | [lecture15-notes.pdf](cs224n/lecture15/lecture15-notes.pdf) | ✅ |
| 16 | ConvNets and Tree Recursive Neural Networks | [lecture16-notes.pdf](cs224n/lecture16/lecture16-notes.pdf) | ✅ |
| 18 | NLP, Linguistics, and Philosophy | [lecture18-notes.pdf](cs224n/lecture18/lecture18-notes.pdf) | ✅ |

**资源**：[课程官网](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/) · [YouTube 播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM) · [Slides 页面](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/slides/)

### Stanford CS231N: Deep Learning for Computer Vision (Spring 2025)

| # | 主题 | PDF | 状态 |
|---|------|-----|------|
| 1 | Introduction | [lecture01-notes.pdf](cs231n/lecture01/lecture01-notes.pdf) | ✅ |
| 2 | Image Classification with Linear Classifiers | [lecture02-notes.pdf](cs231n/lecture02/lecture02-notes.pdf) | ✅ |
| 3 | Regularization and Optimization | [lecture03-notes.pdf](cs231n/lecture03/lecture03-notes.pdf) | ✅ |
| 4 | Neural Networks and Backpropagation | [lecture04-notes.pdf](cs231n/lecture04/lecture04-notes.pdf) | ✅ |
| 5 | Image Classification with CNNs | [lecture05-notes.pdf](cs231n/lecture05/lecture05-notes.pdf) | ✅ |
| 6 | CNN Architectures | [lecture06-notes.pdf](cs231n/lecture06/lecture06-notes.pdf) | ✅ |
| 7 | Recurrent Neural Networks | [lecture07-notes.pdf](cs231n/lecture07/lecture07-notes.pdf) | ✅ |
| 8 | Attention and Transformers | [lecture08-notes.pdf](cs231n/lecture08/lecture08-notes.pdf) | ✅ |
| 9 | Object Detection and Image Segmentation | [lecture09-notes.pdf](cs231n/lecture09/lecture09-notes.pdf) | ✅ |
| 10 | Video Understanding | [lecture10-notes.pdf](cs231n/lecture10/lecture10-notes.pdf) | ✅ |
| 11 | Large Scale Distributed Training | [lecture11-notes.pdf](cs231n/lecture11/lecture11-notes.pdf) | ✅ |
| 12 | Self-Supervised Learning | [lecture12-notes.pdf](cs231n/lecture12/lecture12-notes.pdf) | ✅ |
| 13 | Generative Models 1 | [lecture13-notes.pdf](cs231n/lecture13/lecture13-notes.pdf) | ✅ |
| 14 | Generative Models (Part 2) | [lecture14-notes.pdf](cs231n/lecture14/lecture14-notes.pdf) | ✅ |
| 15 | 3D Vision | [lecture15-notes.pdf](cs231n/lecture15/lecture15-notes.pdf) | ✅ |
| 16 | Multi-Modal Foundation Models | [lecture16-notes.pdf](cs231n/lecture16/lecture16-notes.pdf) | ✅ |
| 17 | Robot Learning | [lecture17-notes.pdf](cs231n/lecture17/lecture17-notes.pdf) | ✅ |
| 18 | What We See and What We Value | [lecture18-notes.pdf](cs231n/lecture18/lecture18-notes.pdf) | ✅ |

**资源**：[课程官网](https://cs231n.stanford.edu/) · [YouTube 播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb) · [Slides 页面](https://cs231n.stanford.edu/slides/2025)

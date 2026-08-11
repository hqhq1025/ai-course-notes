# Stanford CS336 2026 中文讲义

本目录对应 **Stanford CS336: Language Modeling from Scratch, Spring 2026**。

- 课程官网：https://cs336.stanford.edu/
- 官方播放列表：https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV
- 官方讲稿仓库：https://github.com/stanford-cs336/lectures
- 制作规范：`STYLE.md`
- 素材准备：`python tools/scripts/prepare_cs336_2026.py`
- 生产基线：`wdkns/wdkns-skills@39f1a04c46e1d0d70f6b71a8fcf079b305a632b9`（`youtube-render-pdf`、`subtitle-refine`、`tensor-formula-viz`）

## 范围

官方播放列表目前包含 17 讲正课和 1 场 Dan Fu 嘉宾课。课程表中的 Daniel Selsam 嘉宾课没有出现在官方播放列表中，因此不虚构缺失内容；如果后续官方公开录像，再补入本目录。

| 讲次 | 主题 | 官方材料 | 讲义源码 / 本地 PDF | 页 / 图 / 盒 | 验收 |
|---|---|---|---|---:|---|
| 01 | Overview, Tokenization | executable lecture | [TeX](lecture01/lecture01-notes.tex) · `lecture01-notes.pdf` | 21 / 15 / 43 | ⭐⭐⭐ · strict · visual QA |
| 02 | PyTorch, einops, resource accounting | executable lecture | [TeX](lecture02/lecture02-notes.tex) · `lecture02-notes.pdf` | 21 / 11 / 40 | ⭐⭐⭐ · strict · visual QA |
| 03 | Architectures, hyperparameters | slides PDF | [TeX](lecture03/lecture03-notes.tex) · `lecture03-notes.pdf` | 31 / 40 / 27 | ⭐⭐⭐ · strict · visual QA |
| 04 | Attention alternatives, mixture of experts | slides PDF | [TeX](lecture04/lecture04-notes.tex) · `lecture04-notes.pdf` | 34 / 46 / 42 | ⭐⭐⭐ · strict · visual QA |
| 05 | GPUs, TPUs | slides PDF | [TeX](lecture05/lecture05-notes.tex) · `lecture05-notes.pdf` | 33 / 46 / 44 | ⭐⭐⭐ · strict · visual QA |
| 06 | Kernels, Triton, XLA | executable lecture | [TeX](lecture06/lecture06-notes.tex) · `lecture06-notes.pdf` | 20 / 8 / 39 | ⭐⭐⭐ · strict · visual QA |
| 07 | Parallelism I | executable lecture | [TeX](lecture07/lecture07-notes.tex) · `lecture07-notes.pdf` | 27 / 15 / 45 | ⭐⭐⭐ · strict · visual QA |
| 08 | Parallelism II | slides PDF | [TeX](lecture08/lecture08-notes.tex) · `lecture08-notes.pdf` | 38 / 42 / 76 | ⭐⭐⭐ · strict · visual QA |
| 09 | Scaling laws I | slides PDF | [TeX](lecture09/lecture09-notes.tex) · `lecture09-notes.pdf` | 32 / 37 / 59 | ⭐⭐⭐ · strict · visual QA |
| 10 | Inference | executable lecture | [TeX](lecture10/lecture10-notes.tex) · `lecture10-notes.pdf` | 23 / 29 / 37 | ⭐⭐⭐ · strict · visual QA |
| 11 | Scaling laws II | slides PDF | [TeX](lecture11/lecture11-notes.tex) · `lecture11-notes.pdf` | 31 / 36 / 60 | ⭐⭐⭐ · strict · visual QA |
| 12 | Evaluation | executable lecture | [TeX](lecture12/lecture12-notes.tex) · `lecture12-notes.pdf` | 32 / 44 / 45 | ⭐⭐⭐ · strict · visual QA |
| 13 | Data sources and datasets | executable lecture | [TeX](lecture13/lecture13-notes.tex) · `lecture13-notes.pdf` | 22 / 19 / 49 | ⭐⭐⭐ · strict · visual QA |
| 14 | Filtering, deduplication, mixing, synthetic data | executable lecture | [TeX](lecture14/lecture14-notes.tex) · `lecture14-notes.pdf` | 21 / 12 / 25 | ⭐⭐⭐ · strict · visual QA |
| 15 | Mid/post-training: SFT and RLHF | slides PDF | [TeX](lecture15/lecture15-notes.tex) · `lecture15-notes.pdf` | 20 / 17 / 22 | ⭐⭐⭐ · strict · visual QA |
| 16 | Post-training: RLVR | slides PDF | [TeX](lecture16/lecture16-notes.tex) · `lecture16-notes.pdf` | 20 / 20 / 20 | ⭐⭐⭐ · strict · visual QA |
| 17 | Alignment and multimodality | executable lecture | [TeX](lecture17/lecture17-notes.tex) · `lecture17-notes.pdf` | 20 / 21 / 20 | ⭐⭐⭐ · strict · visual QA |
| 18 | Guest lecture: Dan Fu | video + transcript | [TeX](lecture18/lecture18-notes.tex) · `lecture18-notes.pdf` | 28 / 26 / 10 | ⭐⭐⭐ · strict · visual QA |

合计：**18 讲、474 页、484 张图、703 个教学盒**。所有讲义均通过双遍 XeLaTeX、strict coverage 检查和逐页视觉 QA。`*-notes.pdf` 按仓库策略保留在本地、不纳入 Git；可从对应 TeX 双遍编译重建。

## 重制原则

- 以官方讲稿、录像和字幕为事实主线，不用摘要替代课程内容。
- 对可执行讲稿保留 source cluster、代码、课堂提示和老师口吻；对 PDF deck 保留最终教学状态，不机械复刻标题页、导航页、重复 recap 或渐进 build-up。
- 每张关键图都必须服务于文字解释；密集图组通过“读图”、术语解释、公式或资源账本串成可学习的叙事。
- 不把课程表上但未公开视频的 Daniel Selsam 嘉宾课伪造成讲义。

## 为什么不覆盖旧目录

仓库现有 `cs336/` 是 Spring 2025 讲义。2026 课程在架构、attention alternatives、XLA、inference、data、RLVR 和 multimodality 等部分都有明显更新，因此使用独立目录，保留两个学期的可追溯版本。

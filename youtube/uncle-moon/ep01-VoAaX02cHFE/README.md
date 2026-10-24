# 朱邦华谈 AI 基础设施

本期学习笔记讨论推理与训练闭环、PPO 的价值网络预热、强化学习环境、大规模训练系统，以及研究和职业选择。

- 原视频：[月球大叔对谈朱邦华](https://www.youtube.com/watch?v=VoAaX02cHFE)，发布于 2026-05-18，时长 1 小时 46 分 51 秒。
- 口述来源：[官网完整逐字稿](https://unclemoon.ai/blog/001-zhu-banghua/transcript/)，原稿保存在 `sources/`。每个章节和全文编辑请求均包含实际全文。
- 技术补充：SGLang 和 DeepSeek-R1 官方资料，见 `sources/references.json`。专有名词和技术澄清见 `sources/source-notes.md`。
- 视频在 15%、45%、78% 位置抽样均为人物访谈。正文使用 7 张依据口述整理的机制图；可编辑 SVG、PDF、PNG 及生成脚本在 `assets/`。
- 正文由 Gemini Argon 撰写并通篇编辑，Codex 整理来源、制定结构、绘图、复核与排版。蓝图和调用回执保存在 `generation/`。

阅读正文请打开 `VoAaX02cHFE-notes.md`，PDF 与 LaTeX 源码同名。PDF 发布位置由系列索引统一维护。覆盖矩阵记录每个讨论段落如何进入讲义；`qa/` 保存渲染检查结果。

重新生成排版：

```bash
python3 generation/produce.py render
xelatex -interaction=nonstopmode -halt-on-error VoAaX02cHFE-notes.tex
xelatex -interaction=nonstopmode -halt-on-error VoAaX02cHFE-notes.tex
```

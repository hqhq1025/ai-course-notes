# 江鋆晨谈 KV Cache

本期学习笔记从流媒体研究走向大模型推理，解释 KV Cache、Prefill 与 Decode、CacheGen、CacheBlend、模型原生记忆，以及开源创业与职业选择。

- 原视频：[月球大叔对谈江鋆晨](https://www.youtube.com/watch?v=yWTVEG9UIHo)，发布于 2026-06-09，时长 2 小时 25 分 26 秒。
- 口述来源：[官网完整逐字稿](https://unclemoon.ai/blog/002-junchen-jiang/transcript/)，原稿保存在 `sources/`。每个章节和全文编辑请求均包含实际全文。
- 技术补充：LMCache 官方项目、CacheGen 与 CacheBlend 论文、IPv6 部署统计，见 `sources/references.json`。术语和技术澄清见 `sources/source-notes.md`。
- 视频在 15%、45%、78% 位置抽样均为人物访谈。正文使用 7 张依据口述整理的机制图；可编辑 SVG、PDF、PNG 及生成脚本在 `assets/`。
- 正文由 Gemini Argon 撰写并通篇编辑，Codex 整理来源、制定结构、绘图、复核与排版。蓝图和调用回执保存在 `generation/`。

阅读正文请打开 `yWTVEG9UIHo-notes.md`，PDF 与 LaTeX 源码同名。PDF 发布位置由系列索引统一维护。覆盖矩阵记录每个讨论段落如何进入讲义；`qa/` 保存渲染检查结果。

重新生成排版：

```bash
python3 generation/produce.py render
xelatex -interaction=nonstopmode -halt-on-error yWTVEG9UIHo-notes.tex
xelatex -interaction=nonstopmode -halt-on-error yWTVEG9UIHo-notes.tex
```

# NJU GSE Argon 写作脚本

这组脚本生成南京大学 2026 年生成式软件工程课程讲义。输入、模型响应缓存和输出位于仓库的 `nju-generative-software-engineering-2026/argon-rewrite/`。脚本根据自身位置定位仓库，可从任意工作目录调用。

需要 Python 3、`requests`，以及仓库既有的 XeLaTeX、Poppler 和 PDF 检查工具。排版优先使用 Droid Sans Fallback；未安装时尝试 Noto Sans CJK SC，再使用 CTeX 默认字体。缺少补充字体时，应在 PDF 检查中确认生僻字是否完整显示。

默认模型为 `gemini-4-argon`，请求地址为 `http://127.0.0.1:8536/v1/chat/completions`。可用环境变量 `ARGON_ENDPOINT` 指定兼容地址。脚本不读取认证文件；调用前应准备好可访问的模型代理。

## 从现有缓存恢复

按以下顺序在仓库根目录执行。命令会更新对应讲次的讲义或检查文件。

```bash
python3 tools/scripts/nju_gse_argon/run_chapters.py 1 2 3 4 5 6 7 8
python3 tools/scripts/nju_gse_argon/edit_lectures.py 1 2 3 4 5 6 7 8
python3 tools/scripts/nju_gse_argon/refine_lectures.py 1 2 3 4 8
python3 tools/scripts/nju_gse_argon/render_notes.py 1 2 3 4 5 6 7 8
python3 tools/scripts/nju_gse_argon/build_notes.py 1 2 3 4 5 6 7 8
```

1. `run_chapters.py` 读取 `generation/plan.json`，复用分章和首尾段缓存；缺少缓存时调用 Argon。已有 `prose.json` 不会被这一步覆盖。
2. `edit_lectures.py` 从 `prose-draft.json` 恢复整讲编辑；`editorial-matching.json` 保存已有编辑的原文匹配修正。
3. `refine_lectures.py` 从 `refinement-draft.json` 恢复复核修正。本批只有第 1、2、3、4、8 讲需要这一步。先整讲编辑，再复核修正，才能恢复最终正文。
4. `render_notes.py` 读取最终 `prose.json`，生成 TeX、Markdown、来源清单与覆盖矩阵。
5. `build_notes.py` 编译两遍，运行覆盖、质量和 PDF 渲染检查。安装了 `~/.agents/skills/speak-plainly/scripts/check.py` 时也运行语言检查；未安装则明确记录 `SKIP`。

生成 PDF 后，检查 `qa/` 中的联系表和报告，并打开可疑页面。自动检查不替代页面检查。

`generation/` 中的完整响应 JSON 会直接复用；只有 `*-partial.txt` 的请求会重新发起。修改提示词后，已有缓存仍会生效，因此保留当前缓存和编辑快照，另行准备新一轮生成输入。`argon_writer.py plan` 可生成缺失蓝图；日常写作使用上述分章流程。

# 第 3 讲修订后复核

第二轮状态：公式说明已改为普通文字“变更 A/B”，不再包含裸 LaTeX 命令。下列内容保留为修订依据；最终 PDF 排版另由 QA 报告确认。

关键事实修订已确认：移除日文词；新生成 README 与优秀老项目的前后指代正确；tree 原始字节格式与 `cat-file -p` 展示区分；`git add` 清除冲突阶段而非等待 commit；Astropy `_cstack` 与固定源实现相符；`bisect skip` 降低分辨率而非完全不能使用；操作交换律与文本冲突区分。

需检查生成路径：`sections[7].equation.explanation` 含裸 `\Delta_A`、`\Delta_B`。若普通正文转义，会在 PDF 显示字面 LaTeX 命令，需改为正规行内数学或普通文本“变更 A/B”。此问题与 L02 公式说明的全转义是同一路径。

当前 53 页 PDF 的第二遍日志未见 Overfull 或 Missing character；联系表未见明显缺图或裁切。最终公式说明修复后复查相关页。

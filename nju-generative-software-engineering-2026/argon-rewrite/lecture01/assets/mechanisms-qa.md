# 机制图检查

8 张机制图已完成，每讲位于 `assets/mechanism.svg`、`assets/mechanism.pdf`、`assets/mechanism.png`。概念说明位于各讲 `assets/mechanism.json`，供正文写作参考。

- 已对照各讲 `sources/official-lecture.md` 核查概念与限制条件。
- SVG 采用中文字体栈，使用 Noto Sans CJK SC 作为 Linux 中文字体回退。
- SVG 画布为 1000 × 440，PNG 为 2000 × 880，PDF 为单页矢量输出。
- 已用 `view_image` 实际检查全部图的 contact sheet，并对第 1 图做全尺寸检查。
- 已修正第 1 图回线交叉与标签位置；第 6 图规则输入的箭头与文字保持间隔；第 8 图预算退出线避开失败反馈文字。
- 浏览器检查所有文字均位于画布内；以 1 像素路径采样检查连线，未发现连线与文字包围框（外扩 2 像素）相交。
- 图底部统一简化为“据第 N 讲绘制”，已重新导出 8 组文件及 contact sheet。
- `pdfinfo` 确认每份 PDF 为 1 页；`pdftotext` 能提取对应讲次的简短来源说明。

机器结果见 `mechanisms-render-report.json`，拼图见 `mechanisms-contact.png`。图片检查不替代将图插入讲义后的 PDF 阅读尺寸与版面检查。

第 3 图只覆盖普通 `git commit` 的暂存语义。第 4 图描述 jj 重写时通常保持 change ID 的情况。第 6 图明确隔离重放中的外部副作用。第 8 图保留独立验收、有限重试和部署产物约束。

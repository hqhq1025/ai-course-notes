# 月球大叔八期网页验收

2026-10-24 20:45 UTC，八期网页通过本地预览验收。预览使用仓库实际的 `generate_site.py` 和 MkDocs 构建，严格构建检查通过。

| 检查项 | 结果 |
| --- | --- |
| 页面与标题 | EP01 到 EP08 均可打开，标题与各期 TeX 一致 |
| 图片 | 63 张全部加载，包括封面与教学图 |
| 公式 | 132 个 MathJax 节点，无渲染错误 |
| 表格 | 55 张表格正常显示，宽表在各自容器内横向滚动 |
| 桌面布局 | 1440 × 1000 视口下，八页均无整体横向溢出 |
| 手机布局 | 390 × 844 视口下，八页文档宽度均为 390 像素 |
| 桌面导航 | 左侧默认收起；左右栏均可展开、收起，刷新后保留选择 |
| 手机导航 | 点击菜单可打开抽屉，点击遮罩可关闭 |

已查看 EP02 公式、EP08 长表和封面的桌面与手机截图。EP02 算例中的长行内公式曾撑出手机页面；改为独立公式并重建后，整体横向溢出已消除。长公式可在公式框内横向滚动。EP08 长表按列换行，表格边界和文字可辨认。

本地截图保存在 `.Codex/workspace/uncle-moon/web-qa/`，不纳入提交：

- `ep02-desktop-formula-final.png`
- `ep02-mobile-formula-final.png`
- `ep08-desktop-cover.png`
- `ep08-mobile-cover.png`
- `ep08-desktop-long-table.png`
- `ep08-mobile-long-table.png`
- `mobile-navigation-open.png`

预览构建位于 `/tmp/uncle-moon-preview/`。本次检查覆盖本地页面；GitHub Release 下载地址与正式站点在发布后另行验证。

# 网页验收

2026-10-26，本期独立预览通过桌面与手机检查。

预览从本期最终 TeX、封面、教学图和 PDF 发布映射生成，使用仓库实际的 `tools/web/generate_site.py` 与 MkDocs。生成器生成 1 篇讲义、1 个系列页面，没有来源缺失或 LaTeX 泄漏警告。全站构建与正式站发布另行验证。

- 预览目录：`/tmp/crossroads-web-build/site`。
- 预览页面：`http://127.0.0.1:8765/interviews/crossroads/BV1CAHV6PEPM/`。
- 浏览器：Chromium，桌面 1440 × 1000，手机 390 × 844；另检查 360 像素窄屏。

| 检查 | 结果 |
|---|---|
| 图片 | 30 组教学图和 1 张封面全部加载，实际查看图文与读图框 |
| 表格 | 6 张表均为 3 列，手机按列换行，未超出页面 |
| 数学 | 6 个数学符号正常排版，没有 MathJax 错误节点 |
| 桌面侧栏 | 首次访问左侧课程导航折叠、右侧目录展开；两侧均可切换；刷新保留选择 |
| 阅读目录 | 目录链接都有对应标题；桌面与手机均能跳转到后半篇章节 |
| 手机导航 | 菜单展开、进入本页目录、选节跳转及关闭均正常 |
| 页面宽度 | 1440、390、360 像素视口的文档宽度分别为 1440、390、360 像素，无页面横向溢出 |
| 运行状态 | 页面没有 JavaScript 异常、控制台错误或 HTTP 400 以上的资源响应 |

PDF 链接指向本期 Release 文件，TeX 链接指向仓库 `main` 分支内的本期源码。此次核对链接地址；发布前没有将远端下载可用性计作完成。

- PDF：`https://github.com/hqhq1025/ai-course-notes/releases/download/crossroads-lilei-2026-v1/BV1CAHV6PEPM-notes.pdf`
- TeX：`https://github.com/hqhq1025/ai-course-notes/blob/main/interviews/crossroads/BV1CAHV6PEPM/BV1CAHV6PEPM-notes.tex`

## 最终排版复查

基于 49 页 PDF 对应的最终 TeX，再次运行实际生成器与 MkDocs，构建通过。页面保留 30 组教学图、30 个“读图”框和 6 张表，没有 LaTeX 命令残留。

两处合图的重复来源区间已合并：`supervision-relationship.jpg` 的 `00:25:42–00:26:02`，以及 `agent-development.jpg` 的 `00:39:28–00:39:41`。复查全部 30 条来源说明，没有重复区间。

PDF 调整读图框分页时，一度使网页出现 `tcbset` 排版指令。排版器已改为前言中的可选框参数；最终页面没有 `tcbset` 或 `breakable=false` 文本，“读图”标题与正文均保留。手机读图截图已更新。

## 截图

- [桌面标题与默认侧栏](web/desktop-top.png)
- [桌面两侧导航展开](web/desktop-both-sidebars.png)
- [桌面教学图](web/desktop-research-figure.png)
- [桌面评测表格](web/desktop-benchmark-table.png)
- [手机标题与阅读正文](web/mobile-top.png)
- [手机教学图](web/mobile-research-figure.png)
- [手机评测表格](web/mobile-benchmark-table.png)
- [手机数学符号与读图框](web/mobile-math.png)
- [手机课程导航](web/mobile-navigation.png)
- [手机本页目录](web/mobile-toc.png)

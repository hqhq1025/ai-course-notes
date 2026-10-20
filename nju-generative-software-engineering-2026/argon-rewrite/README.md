# 生成式软件工程 2026 · Argon 完整重写版

本版覆盖[官方课程页](https://jyywiki.cn/GSE/2026/)在 2026-10-20 列出的 8 讲。
主讲与原始讲义作者为南京大学蒋炎岩。正文通过本机 coproxy 调用
`gemini-4-argon` 重新编写；Codex 负责来源核查、配图、可视化与排版验收。
此目录与此前前两讲的课堂图文实录分别保存。

八讲已完成全文重写和整讲编辑，共 445 页。包括全部 290 张官方课件、8 张机制图、术语解释、代码示例和学习练习。

[在线阅读全系列](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/) · [下载全部 PDF](https://github.com/hqhq1025/ai-course-notes/releases/tag/nju-gse-2026-argon-v2)

| 讲次 | 官方主题 | 课件页数 | 讲义页数 | 阅读 |
|---|---|---:|---:|---|
| 01 | 欢迎来到未来 | 44 | 60 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture01/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture01-notes.pdf) · [文字](lecture01/lecture01-notes.md) |
| 02 | 提示词与上下文工程 | 37 | 59 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture02/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture02-notes.pdf) · [文字](lecture02/lecture02-notes.md) |
| 03 | 版本管理 | 35 | 54 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture03/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture03-notes.pdf) · [文字](lecture03/lecture03-notes.md) |
| 04 | 版本管理（2） | 25 | 44 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture04/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture04-notes.pdf) · [文字](lecture04/lecture04-notes.md) |
| 05 | 软件工程的来龙去脉 | 39 | 59 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture05/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture05-notes.pdf) · [文字](lecture05/lecture05-notes.md) |
| 06 | 需求和架构（1） | 47 | 65 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture06/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture06-notes.pdf) · [文字](lecture06/lecture06-notes.md) |
| 07 | 需求和架构（2） | 39 | 59 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture07/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture07-notes.pdf) · [文字](lecture07/lecture07-notes.md) |
| 08 | Agent Native 开发 | 24 | 45 | [网页](https://hqhq1025.github.io/ai-course-notes/nju-generative-software-engineering-2026/argon-rewrite/lecture08/) · [PDF](https://github.com/hqhq1025/ai-course-notes/releases/download/nju-gse-2026-argon-v2/lecture08-notes.pdf) · [文字](lecture08/lecture08-notes.md) |

第一次学习可按讲次阅读：前两讲建立委托任务和组织上下文的方法；第三、四讲学习保存与整合修改；第五到七讲把需求、约束、历史事实和派生结果组织成可维护的系统；第八讲将这些方法接入 Agent、持续集成与发布流程。每讲末尾的练习提供可检查的完成标准。

八讲均已通过双遍 XeLaTeX、来源覆盖检查、`⭐⭐⭐` 质量检查和 PDF 视觉验收。各讲保留可编辑的同名 `.tex` 源码；PDF 通过 Release 下载，不重复存入 Git 历史。详见[验收记录](ACCEPTANCE.md)。

调用诊断与可复用流程见 [Argon 写作方式](WRITING_METHOD.md)。

## 来源与范围

- 官网提供完整讲义、HTML 课件和两个 Lab。来源 URL、获取时间及原始文件哈希见各讲 `source.json`。
- [社区字幕校订仓库](https://github.com/NinZeige/NJU-2026-GSE-Captions)固定在 `0456f3a46fd5fa2f2a86123e02b7ed48696adacb`。作者仅将第 1 讲标为人工校对，其余稿件需结合官方材料核对。
- 原有本地第 1、2 讲 ASR 字幕用作交叉参照，课堂内容以官方讲义为主要依据。
- 第 3 到 6 讲另有对应 GitHub 案例、API 和实现的核查摘记，见 `sources/github-context.md`。
- 已查作者 `jiangyy` 的公开仓库及课程页链接，本课的主要资料入口为课程官网。
- 官方课件含 AIGC 补充标记，截图保留这些标记。官方发布材料与课堂视频可能有编排差异。
- 290 张官方课件截图完整保存；8 张机制图为 Codex 依据课程重绘。第 5 讲内嵌视频另保留原始帧，其时间是片内时间。

## 可复核的生成记录

各讲 `generation/` 保存 Argon 请求的文字输入、原始输出、结构化正文和调用回执。
回执包含请求及返回模型、停止原因、耗时、token 统计和哈希，不含认证信息。
`plan.json` 在正文调用之前保存，记录完整页码分配、教师讲解要点及限制。
`coverage-matrix.md`、`lecture-manifest.md` 和 `qa/` 用于检查来源覆盖及最终排版。

配图检查见 [官方课件 QA](SLIDE_RENDER_QA.md) 和
[机制图 QA](lecture01/assets/mechanisms-qa.md)。

## 许可与署名

原课程由蒋炎岩创作，课程页标注
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。
社区字幕贡献者为 NinZeige/NJU-2026-GSE-Captions，归属与改动说明见
[community-NOTICE.md](community-NOTICE.md)。
本版重组与扩写课程内容，增加机制图，供非商业学习使用。
外链代码项目适用各自许可证。

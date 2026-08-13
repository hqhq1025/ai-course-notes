# CS153 Lecture 02 Blueprint

Status: implemented and visually verified on 2026-08-11.

## Goal

把 Steve Huffman 访谈重写成一份关于社区平台如何跨越冷启动、治理重构、API 经济、流量韧性与 AI 接口变迁的系统讲义。该讲没有可用 slide deck，历史公开视频在 2026-08-11 已转 private；因此视觉主线使用 12 张基于本地时间戳字幕的可复现概念图，并明确标注为讲义重绘。

## Source Priority

1. 本地历史字幕 `lecture02.srt`，保留原时间戳。
2. Stanford Winter 2025 官方课程页对讲者与课程范围的确认。
3. 本地官方缩略图 `cover.jpg`。
4. `lecture02-diagrams.py` 生成的 transcript-grounded diagrams。
5. 旧讲义仅作为主题索引，不直接沿用结构和结论。

## Section Plan

1. 产品原型、冷启动和社区出现的判据。
2. 收购、离开、回归与组织重建。
3. 从投票自治到分层治理与 ``specifically vague''。
4. 执法工具、价值判断与公开公司责任。
5. 公共内容、数据授权、付费社区与 API 定价。
6. 流量峰值、多云、优雅降级和恢复顺序。
7. Scrollers、seekers、Reddit Answers 与 agent API。
8. 总结：开放性、可持续性和人类社区的长期价值。

## Required Treatment

- 12 张概念图全部进入正文，图前有问题设置，图后解释证据和边界。
- 首次解释 UGC、subreddit、cold start、moderation、doxing、API、scraping、rate limit、graceful degradation、RAG 与 agent API。
- 保留讲者关于“醒来发现首页已有真实内容”、系统脆弱恐惧、每个政策词都来自代价、抗议合法但决策仍需承担责任、scrollers 寻找人类连接、agents 已经到来的课堂语气。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

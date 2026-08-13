# CS153 Lecture 11 Blueprint

Status: complete and visually accepted on 2026-08-11.

## Goal

把 Joe Sullivan 的访谈重写成一份关于 security organization、vulnerability disclosure、bug bounty、incident command、evidence preservation、materiality/disclosure governance 和 executive accountability 的系统讲义。法律案件只作为 governance failure analysis，明确区分课堂中的个人叙述、政府指控、法院已裁判事实和工程判断。

## Teaching Thesis

安全事件响应不是 CSO 单人决策，而是三个互相约束的闭环：

1. `external report → validate → scope → remediate → coordinated disclosure/reward`；
2. `detect → contain → preserve evidence → investigate → notify/recover → learn`；
3. `technical facts → legal/materiality analysis → executive/board decision → regulator/customer communication`。

## Section Plan

1. 来源审计、法律边界与 2026 当前案件状态。
2. Security organization maturity：从 5 人团队到 embedded program。
3. Government/technology structural tension 与 regulation channels。
4. Vulnerability Disclosure Policy：scope、safe harbor、intake、SLA 与 coordination。
5. Bug bounty：reward、severity、duplicate、out-of-scope 与 extortion boundary。
6. Incident command：roles、severity、containment、forensics 与 recovery。
7. Evidence preservation：chain of custody、timeline、decision log 与 privilege boundary。
8. Materiality/disclosure matrix：customers、regulators、law enforcement、public market。
9. Uber/Sullivan case timeline：classroom claim versus final appellate outcome。
10. Regulation by enforcement versus rulemaking and standards。
11. CSO、CEO、general counsel、board 与 disclosure committee responsibility。
12. Security leader protection：clear authority、written escalation、independent review 与 D&O/employment support。
13. Resilience：human recovery、public service 与 sustainable leadership。
14. Government technical talent and public-private feedback loop。
15. Tabletop exercise：VDP report becomes material incident。
16. 总结、incident-governance 作业与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有问题设置、读图说明和证据边界。
- 首次解释 VDP、coordinated vulnerability disclosure、bug bounty、safe harbor、scope、incident commander、chain of custody、legal hold、materiality、Form 8-K、privilege、RACI、nexus 与 certiorari。
- 不复述可操作入侵细节；只保留 access、exfiltration、credential、notification 和 governance facts。
- 当前法律时间线必须写到 2026-06-29 Supreme Court denial，不能保留“appeal pending”旧结论。
- SEC 四工作日规则必须准确表述为“公司确定事件具有重大性后通常四个工作日内”，不是发现后固定四天；并明确存在法定延迟条件和专业法律判断。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

# CS153 Lecture 09 Blueprint

Status: complete on 2026-08-11; strict coverage, double-pass XeLaTeX, quality and signed PDF QA all passed.

## Goal

把 Todd McKinnon 的访谈重写成一份关于 identity infrastructure 如何从“让员工登录 SaaS”扩展为组织级 control plane 的系统讲义。创业和 CEO 经验保留为系统判断来源，但全文主线是 identity data model、authentication/authorization/provisioning、front-door reliability、security incident feedback、culture as operating system、agent delegation、token lifecycle 与 platform acquisition boundaries。

## Teaching Thesis

身份基础设施由三个互相约束的闭环组成：

1. `identity source → policy → authentication/authorization → session → audit`；
2. `incident → containment → root cause → remediation → customer trust`；
3. `technology transition → focused wedge → infrastructure depth → organizational adaptation`。

## Section Plan

1. 来源审计、课堂口径和当前产品演化边界。
2. Cloud transition 与 identity wedge：从 monitoring pivot 到 SSO。
3. Identity control plane：directory、authentication、authorization、provisioning、session 与 audit。
4. Front-door reliability：SLO、multi-tenant blast radius、failover、change safety。
5. Founder transition：从资源充足的工程主管到低概率环境中的 daily progress。
6. CEO/board information loop：bad news、decision rights 与孤独问题。
7. Security incident response：timeline、containment、RCA、remediation 和 transparency。
8. Security-first culture：leader behavior、resource allocation 与 incentives。
9. Attacker asymmetry 与 shared signals：简单入口、复杂防御和跨组织信息共享。
10. Zero Trust / policy engine：context、assurance、step-up 与 continuous session risk。
11. Agent identity：principal、delegation、OAuth token exchange、scope 与 audit。
12. Non-human identity lifecycle：discovery、ownership、secret/token rotation 与 retirement。
13. Auth0 acquisition：workforce/customer identity、platform separation 与 integration pace。
14. Durable trust：early customer credibility、reliability evidence 与 long-term focus。
15. AI adoption：Mr. T app、killer workflow、incumbent inertia 与 organizational redesign。
16. 总结、identity architecture 作业与拓展阅读。

## Required Treatment

- 16 张 transcript-grounded diagrams 全部进入正文，每张有问题设置、读图说明与证据边界。
- 首次解释 identity provider、principal、authentication、authorization、SSO、MFA、directory、provisioning、SCIM、session、token、OAuth、OIDC、assurance、Zero Trust、service account、non-human identity 与 token exchange。
- 课堂规模数字只作为 speaker estimate；不能把 later product pages 当成 2025 已有能力。
- Security incident 使用官方 RCA 校验机制，但不把某一次事故简化为单一员工错误；必须讨论 credential handling、logging gap、session revocation、customer notification 和 systemic remediation。
- Agent score/decision 不适用；这里要明确 agent 不是人类身份，delegation 必须保留 user context、scope、audience、expiry、revocation 和 audit。
- 最终执行 strict coverage、双遍 XeLaTeX、quality、canonical PDF QA 与人工签署。

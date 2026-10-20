# L04 GitHub 证据摘记：Jujutsu 的变更身份与工作区

核查日期：2026-10-20（UTC）。本文件直接核查官方文档，不代表已经运行文中的命令。当前文档可能晚于课堂使用的版本；重写只采用与课堂主线一致的概念。

## 来源与版本

- [官方讲义](https://jyywiki.cn/GSE/2026/lect4.md)直接引用 `jj-vcs/jj` 的术语表与工作区文档。
- 固定提交：`698e5eaed2acb863052419dcebb81fc59166e219`；提交时间：`2026-10-20T02:46:18Z`。
- [术语表](https://github.com/jj-vcs/jj/blob/698e5eaed2acb863052419dcebb81fc59166e219/docs/glossary.md)。重点小节：Change、Commit、Rewrite、Divergent change、Working copy、Operation log。
- [工作区文档](https://github.com/jj-vcs/jj/blob/698e5eaed2acb863052419dcebb81fc59166e219/docs/working-copy.md)。重点小节：Introduction、Conflicts、Ignored files、Workspaces、Stale working copy。

## 可用于重写的核实结论

`commit` 保存文件快照与作者、父提交等元数据。父提交连接成有向无环图。工具经常把提交理解为相对父提交的变化，但底层仍保存快照。

`change` 指一个提交随时间演化的过程。术语表特别说明：数据模型中没有独立的 change 对象；`change ID` 是提交的一项属性。重写生成新的提交和新的 `commit ID`，而 `change ID` 通常不变。因此，“相同改动的后续版本”与“精确的这一个提交”可以分别表达。

同一个 `change ID` 也可能对应多个可见提交，文档称为 divergent change。不能把 change ID 写成永远唯一定位一个提交的标识。需要精确绑定源码时，应记录 `commit ID`。

大多数 `jj` 命令在开始时为工作区变化创建快照，并替换先前的工作区提交。它不是持续监听每一次编辑的后台备份。新文件默认自动跟踪，但忽略规则和 `snapshot.auto-track` 会限制范围。已经跟踪的文件不会因为后来进入 `.gitignore` 就自动退出历史。

冲突能够作为提交状态保存。写入普通文件系统时，jj 用冲突标记表达冲突，并记录涉及的各部分；再次扫描时解析标记。用户可以分次解决冲突，不必一次全部完成。“冲突是一等状态”不等于工具已经决定正确业务行为。

多个 workspace 可以关联同一仓库，并检出不同提交。若从 workspace B 重写 workspace A 的工作区提交，A 的文件可能变成 stale，需要恢复同步。这说明隔离目录并不消除共享仓库状态及协调责任。

## 与课堂设想的边界

这些机制能支持变更身份、历史重写与冲突保存，但不自动保证测试通过、架构正确或多 Agent 的任务独立。课堂中的自动准入系统、互斥锁调度与解题轨迹存储，仍是需要单独验证的设计。

## 版权与归属

来源为 Jujutsu 项目及贡献者。固定版本 [LICENSE](https://github.com/jj-vcs/jj/blob/698e5eaed2acb863052419dcebb81fc59166e219/LICENSE)为 Apache License 2.0。本摘记为概念转述；没有复制完整文档。

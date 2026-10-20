# L05 GitHub 证据摘记：Verus 的规约与静态验证

核查日期：2026-10-20（UTC）。本文件用于核对课程对验证工具的定位；没有安装 Verus，也没有运行证明或项目测试。

## 来源与版本

- [官方讲义](https://jyywiki.cn/GSE/2026/lect5.md)直接链接 [verus-lang/verus](https://github.com/verus-lang/verus)。
- 固定提交：`775e2d403f4bc8703626c5f56732a01d37ff37a8`；提交时间：`2026-10-20T00:22:39Z`。
- [固定 README](https://github.com/verus-lang/verus/blob/775e2d403f4bc8703626c5f56732a01d37ff37a8/README.md)。
- 延伸入口：[教程与参考](https://verus-lang.github.io/verus/guide/)；[并发代码验证指南](https://verus-lang.github.io/verus/state_machines/)；[仓库示例](https://github.com/verus-lang/verus/tree/775e2d403f4bc8703626c5f56732a01d37ff37a8/examples)。在线指南未固定版本，仅作后续阅读链接。

## 可用于重写的核实结论

Verus 验证 Rust 代码相对于已写规约的正确性。开发者先表达代码应满足什么要求，工具再以求解器执行静态检查。README 将这种证明过程与增加运行时检查区分开来。

README 所说的“所有可能执行均满足规约”，应保留“相对于给定规约”的范围。它不意味着工具自动发现用户真实需求，也不意味着没有写出的业务规则已经被证明。规约、可信假设和受支持的语言语义会影响证明结论。

Verus 支持 Rust 的一个子集，且项目处于活跃开发中。README 明确提示功能可能缺失或失效，文档尚未完整。不能把它描述为对任意 Rust 项目无需改写即可自动证明的工具。

项目也能验证一些超出标准 Rust 类型系统检查范围的性质，例如某些原始指针代码的正确性。这个定位适合衔接 L05 的契约：接口承诺先被表达出来，实现再接受对应检查。类型通过、样例测试通过和证明满足规约，是三种不同的证据。

本课只需使用这一定位，不应把材料扩写成完整 Verus 教程，也不应声称课堂已用它证明取款示例或教务系统。

## 版权与归属

固定版本 [LICENSE](https://github.com/verus-lang/verus/blob/775e2d403f4bc8703626c5f56732a01d37ff37a8/LICENSE)为 MIT License，记载 `Copyright (c) 2021 The Verus Contributors`。README 中的 Verus 标志另有 CC BY 4.0 声明；本文件没有复制标志或示例源码。

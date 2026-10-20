# L03 GitHub 证据摘记：Astropy 嵌套模型修复

核查日期：2026-10-20（UTC）。本文件是供课程重写使用的来源摘记，不是新增课堂实录。本轮直接请求 GitHub API 与固定版本原文件，没有重新运行 Astropy 测试。

## 来源与版本

- [官方讲义](https://jyywiki.cn/GSE/2026/lect3.md)直接引用 [Issue #12906](https://github.com/astropy/astropy/issues/12906) 与 [PR #12907](https://github.com/astropy/astropy/pull/12907)。
- Issue 标题：`Modeling's separability_matrix does not compute separability correctly for nested CompoundModels`。API 返回最后更新时间为 `2022-03-04T15:24:50Z`；Issue 内容可编辑，没有对应的不可变提交标识。
- PR head：`efedd57cb088b6ca73f9540a3c6185ad7046c926`。
- PR base：`d16bfe05a744909de4b27f5875fe0d4ed41ce607`。
- 合并提交：`738068e5d397490e4b1565b026a95301dc1cddec`；合并时间：`2022-03-04T15:24:50Z`。
- [固定修复源码](https://github.com/astropy/astropy/blob/efedd57cb088b6ca73f9540a3c6185ad7046c926/astropy/modeling/separable.py)；[固定测试](https://github.com/astropy/astropy/blob/efedd57cb088b6ca73f9540a3c6185ad7046c926/astropy/modeling/tests/test_separable.py)；[更新记录](https://github.com/astropy/astropy/blob/efedd57cb088b6ca73f9540a3c6185ad7046c926/docs/changes/modeling/12907.bugfix.rst)。

## 问题、修复与回归边界

Issue 先构造两个并列的一维线性模型 `cm = m.Linear1D(10) & m.Linear1D(5)`。它们各自依赖自己的输入，依赖矩阵为 2×2 对角阵。把 `cm` 放到 `m.Pix2Sky_TAN() & cm` 的右侧后，旧代码却把右下 2×2 区域变成全真。这会错误地表示两个线性模型的输入输出相互依赖。

根因位于 `_cstack(left, right)`。右侧已经是依赖矩阵时，旧代码把目标区域统一填成 `1`。PR 将赋值右侧改为 `right`，保留子模型已经计算出的内部依赖结构。修复行是 `cright[-right.shape[0]:, -right.shape[1]:] = right`。

PR 的实现改动只有一行，但交付并非只有这一行。它增加 `cm8` 到 `cm11` 四个测试条目，并补充更新记录。前三个条目比较 `rot & (sh1 & sh2)`、`rot & sh1 & sh2`、`(rot & sh1) & sh2`，要求不同嵌套方式得到相同的 4×4 依赖结构。第四个条目加入右侧嵌套缩放模型，检查 5 维组合。预期结果同时覆盖可分离标记和依赖矩阵。

这份证据支持“理解组合抽象后，以局部修复保留已有结构”。它不支持把一行补丁当作全部开发工作，也不证明所有复合模型性质已经验证完毕。课程可把它连接到问题复现、根因定位、回归检查、更新记录与合并过程。

## 版权与归属

源码和测试归 Astropy Developers；固定版本的 [LICENSE.rst](https://github.com/astropy/astropy/blob/efedd57cb088b6ca73f9540a3c6185ad7046c926/LICENSE.rst)记载 `Copyright (c) 2011-2021, Astropy Developers`，许可为 BSD 3-Clause。Issue 与 PR 讨论归各贡献者；本摘记使用转述和最小标识，不把讨论文字自动视为仓库许可覆盖的源码。

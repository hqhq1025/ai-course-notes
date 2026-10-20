# L05 独立事实审阅

审阅对象：`generation/prose.json` 的 8 节正文、代码、公式与练习。对照本讲官方讲义与已保存的 GitHub 来源摘记。下列路径使用零起始索引。仅列需要修正的具体问题，不要求给每段补免责声明。

## 必修

1. `sections[4].equation.latex`、`sections[4].equation.explanation`：前置条件写成 `amount <= balance`，解释却把 `balance` 定义为操作完成后的余额。这样取款 60、原余额 100、余额变 40 的正确操作反而违反前置条件。将前置条件改为 `0 < amount <= balance_old`，后置条件保留 `balance = balance_old - amount`，明确状态分别取自调用前和正常返回后。Eiffel 代码里的 `require` 本来在调用前求值，没有这一错误。

2. `practice[1].task` 与 `practice[1].acceptance`：任务允许选“排序或去重合并函数”，验收却统一要求保留每个元素的出现次数。去重的正确行为本来就会改变重数。最小修正是将任务限定为排序函数；若保留去重选项，必须另列去重的集合相等、唯一性等性质。

3. `sections[6].units[1].reading`、`sections[6].boxes[1].text`、`practice[2].acceptance`：不要把所有 aggregation 都定义为“销毁绑定”。UML 的 `none`、`shared`、`composite` 有区别，复合聚合（composition）才有强所有权与删除传播规则，shared aggregation 没有统一的销毁绑定语义。保留三维拆分，第三维写成“聚合种类，尤其是否为带生命周期约束的组合”，并明确学生与课程关系不宜据箭头推断为 composition。

## 应收窄的具体陈述

4. `sections[0].units[2].reading`：Perplexity 定义只有“越低预测越准确”，容易被读成事实正确率。按课程术语要求补 `PPL = exp(平均负对数似然)`（自然对数），说明是在相同测试数据与分词方式下比较对实际 token 的预测概率，不是回答事实正确率。DoReMi 的观察仍可保留。

5. `sections[3].units[4].after`：Hello World 路径跑通不能“立刻消除路径上的不确定性”。应改为“为该路径的连通性提供证据；性能、容量与异常恢复等风险仍需对应实验”。这与本节 Royce 要尽早经历真正运行约束的论点直接相关。

6. `sections[0].units[1].after`：关于“某千禧年难题、数千页、定义写错等于证明 1=1”的具体事件，现有官方讲义未给可核查对象。若社区口述保留该故事，写成讲者用来说明形式化边界的课堂例子，别把未知论文当作已核实史实；可直接用确定性原理替换：证明器检查形式化命题，不能自动保证命题准确表达自然语言问题。

## 已确认无需反复加警告的部分

Royce 对简单线性流程的批评、pilot 与 MVP 的不同侧重、DbC 的前置条件与正常业务失败区别、Verus 针对 Rust 子集、规范性 XMI 优先级仅用于 UML 自身、`seq` 弱顺序的三条约束，均已表达清楚。不要在统一编辑时把这些边界改回无条件结论。

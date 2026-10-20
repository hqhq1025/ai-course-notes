# L07 独立事实审阅

已审阅全部 8 节与练习；生成阶段先读 `section-01.json` 到 `section-08.json`，随后核对合并后的 `prose.json`。以下使用 `prose.json` 的零起始索引。

## 必修

1. `sections[7].code.source`：函数形参误写为 `curriculum_ snapshot`，中间空格造成 Python `SyntaxError`，函数体却用 `curriculum_snapshot`。应统一为后者。已用 `ast.parse` 实际检出第一行语法错误。L06 两处 Python 片段与 L07 薪酬片段的语法解析通过；这不等于执行验证通过。

2. `sections[5].code.source`、`sections[5].code.explanation`：React 示例计算了 `visibleCourses` 却只返回输入框，既未渲染、返回，也未导出列表；Vue 示例同样只有输入框模板注释。它们无法演示所声称的“课程列表随筛选变化”。请在两侧都补最小列表呈现，并提供稳定的课程 ID 作为 key。若想维持纯片段，必须把图示与说明限定为派生计算片段，但完整的小例子更利于教学。

3. `sections[5].units[1].after`、`sections[5].code.source`：只有响应式数据才能触发 Vue computed 失效，当前代码中 `courses` 来源未定义，不能推出“原始课程列表变化会自动更新”。应通过 `defineProps` 并在 computed 中读取 `props.courses`，或明确使用 `ref`/`reactive` 课程状态，再给出对应 `.value` 读取。不要用普通数组替换变量却声称 computed 自动发现。

4. `sections[4].code.source`：JSP 的 `${user.name}` 不自动做 HTML 转义。若名字来自用户，直接放入 `<li>` 会将尖括号等当成标记。改为 `<c:out value="${user.name}" />`，既维持 JSTL 教学目标，又准确演示安全文本输出；无需另加泛化安全清单。

5. `sections[6].units[3].after` 与 `sections[6].units[5].reading`：前者说录错科目后“修正对应的编译动作并重跑”，后者又要求已记录事实只追加更正。请区分未确认草稿与已接受的账本动作：草稿可重编译；已记账事件保留，追加冲销/更正再重算。两种阶段不区分，会让读者不知事件历史究竟可否被覆盖。

## 应收窄的具体技术说法

6. `sections[0].units[2].after`：文件系统并非没有并发控制或原子操作，它可以有锁、原子 rename 等。这里应说“直接用文件组织业务数据时，多文件事务与并发一致性通常要由应用额外设计”，避免把数据库优点建立在错误的绝对区分上。

7. `sections[5].boxes[0].text` 的“无论前端后端绝不保存派生结果”应与第八节允许缓存、物化视图的正确表述统一。限制的是不应把派生副本当成可独立修改的第二事实源，不是禁止缓存或受控存储派生结果。

8. `sections[7].units[0].after` 与 `practice[2].acceptance`：成绩更正后可以重算当前先修资格和候选审核结论，但是否撤销已接受的后续选课或已发布决定，需要课程适用规则及复核流程。若练习要求自动取消既有资格，应显式给出这一虚构业务规则，不能从数据依赖关系本身推出政策。保留重算能力，勿覆写既成事实。

## 已保持正确的来源边界

React setter 不修改当前渲染快照、Vue props 单向、SQL 具备视图/物化视图而课堂批评指跨层依赖、22.07 - 75 = -52.93、借贷平衡不证明科目正确、重放隔离外部扣款等，均已正确。无需在统一编辑中重复添加防御段落。

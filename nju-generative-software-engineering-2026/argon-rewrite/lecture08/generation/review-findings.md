# L08 独立事实审阅

已审阅全部 8 节和练习。路径采用合并后 `prose.json` 的零起始索引。主要问题集中在新加的门禁代码，工业案例的主要机制与来源边界保留得较好。

## 必修：实测门禁失败时放行

1. `sections[4].code.source`：`if git diff --name-only origin/main...HEAD | grep -q "^tests/"; then` 遇到缺失基线、浅克隆无法找到 merge-base 或 Git 失败时，整个 if 条件为假，脚本继续输出成功。`set -euo pipefail` 不会使 if 条件中的失败自动退出。

   已在临时空 Git 仓库中执行原样脚本，结果为：

   ```text
   exit 0
   stdout: [CI PASSED] 门控检查通过。
   stderr: fatal: ambiguous argument 'origin/main...HEAD': unknown revision or path not in the working tree.
   ```

   修法：先验证并绑定所需 base/head 与 diff 范围，再单独运行 `git diff` 并显式检查成功状态，最后才匹配路径。避免在管道里用 `grep -q` 提前退出制造 SIGPIPE/pipefail 的额外误判。文档必需时，缺失文件也应明确报错，不能通过删除 AGENTS.md 跳过预算检查。

2. `sections[4].code.source`、`sections[4].code.explanation`：`ALLOW_TEST_MODIFICATION=true` 只是环境变量，不天然代表人类授权；如果由被测分支或实现 Agent 修改，门禁可被自行关闭。脚本本身也需要从可信基线获取或受保护。应清楚写出审批值来自独立的受保护执行层，或把示例收缩为“变更检测并要求独立审查”，不要声称本地布尔变量实现了权限隔离。

3. `sections[4].code.source`、`practice[2].acceptance`：禁止降低验收标准不等于禁止增加或维护所有测试。当前脚本把 `tests/` 中任何新增回归测试都作为篡改，报错还要求还原全部 tests；同时又漏掉目录外测试、工作流、测试配置和跳过测试的设置。建议区分受保护的独立验收集与允许随实现增加的回归测试，并由独立检查覆盖真正的验收入口。练习定位为 acceptance 字符串中的第 2 项。

## 必修：部署防覆盖的机制不足

4. `sections[3].boxes[0].text`、`practice[1].acceptance`：GitHub Actions `concurrency` group 不保证 FIFO 顺序；取消旧任务也不能撤销已经发往外部部署服务的动作。因此“配置 concurrency 就确保旧版本绝不会覆盖新版本”过强。应在最终发布权威处验证该提交/发布代次仍是允许发布的最新候选，并使检验与发布具有原子或平台等价保证；串行化、取消用于减少竞争。验收应实际构造旧构建晚完成、新版本先上线的时序，确认旧产物被拒绝。

## 具体表述修正

5. `sections[1].units[2].after`：Ralph 每轮重启只减少跨轮上下文累积，不会“彻底规避”压缩。单轮 `claude -p` 自身仍可能运行很长并触发压缩；落盘状态也可能丢失信息。改成减少跨轮长上下文依赖，保留每轮预算与交接质量要求。

6. `sections[2].boxes[0].text`、`sections[5].boxes[0].text`：Harness 是 Agent 的运行、工具、约束与反馈设施，不等同于“生产环境”。CI/工作区等开发设施也是 Harness 的一部分。直接统一术语，不需单设警示框。前者还把机械检查说成准入“唯一依据”，应改为必要门槛，避免排除本讲另行强调的独立审查与需求决策。

7. `sections[4].boxes[0].text`：报错必须走“标准输出”的要求与 L07 数据 stdout、诊断 stderr 的组合协议冲突。要求检查输出包含位置与修复指引即可；诊断应写 stderr，结构化数据按工具协议输出。

8. `sections[6].units[0].after`、`sections[6].boxes[0].text`：Git blob hash 配对只说明文件内容与已记录版本匹配，不能证明两种语言语义等价；两个文件可一起错误翻译并更新 hash。把它说成检测未登记内容变更与配对失步，语义一致仍靠翻译/审阅。不要将一个哈希检查器描述为独立完成翻译或证明语义同步。

## 已确认的正确内容

持续交付与持续部署区别、required checks 必须配合权限规则、Stripe Blueprint 混合确定性节点与受限 CI 重试、Anthropic 用 GCC 细分失败集合、StrongDM 独立场景与替身校准、Friendster 技术复盘不等同公司失败唯一原因，均已保留正确边界。不要再加逐页重复免责声明。

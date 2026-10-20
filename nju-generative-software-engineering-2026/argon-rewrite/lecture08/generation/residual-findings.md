# L08 编辑后复验：CI 管道仍可错误放行

状态：已修正并复验。最终稿 SHA256 `73384938cefa9afebfef5bbccf25f559f7b8771bccbb6acd1993c250f0be3273` 使用下文建议的两处 here-string；同一大文件列表场景现返回 1。最终结论见 `qa/factual-review.md`。以下保留问题发现时的证据。

位置：`prose.json` 的 `sections[4].code.source`。

当前代码：

```bash
if printf '%s\n' "$CHANGED_FILES" | grep -Eq "$PROTECTED_PATTERN"; then
```

在 `set -o pipefail` 下，`grep -q` 匹配后提前退出。长文件列表使上游 `printf` 收到 SIGPIPE，整个管道返回失败；由于它位于 `if` 条件中，脚本不会退出，反而跳过拦截并打印 `CI PASSED`。

建议直接替换为无管道的 Bash here-string：

```bash
if grep -Eq "$PROTECTED_PATTERN" <<< "$CHANGED_FILES"; then
```

诊断列表也可统一为：

```bash
grep -E "$PROTECTED_PATTERN" <<< "$CHANGED_FILES" >&2
```

已执行复现：新建临时 Git 仓库；基础提交包含短 `AGENTS.md`；后续提交修改 `.github/workflows/check.yml` 并新增 2500 个 `z/00000-long-regression-file-name-for-pipe-buffer-pressure.txt` 形态的普通文件；将 `BASE_REF` 指向基础提交，`HEAD_REF=HEAD`。当前原样示例返回 `0`，标准输出为 `[CI PASSED] 门控检查通过。`，标准错误为空。

同一轮已通过的边界：缺失 base、缺失 head、缺失必需 AGENTS 文档、单独修改受保护验收文件均返回 1；单独新增普通单元回归测试返回 0。请保留这些行为，只修复上述管道误放行。

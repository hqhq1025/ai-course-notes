# 第 8 讲事实与 CI 示例复核

复核对象：`generation/prose.json`，SHA256 `73384938cefa9afebfef5bbccf25f559f7b8771bccbb6acd1993c250f0be3273`。

结论：前轮事实问题及编辑后发现的 CI 管道问题均已修正。Argon 将两处 `printf | grep` 改为 Bash here-string；本代理用同一组真实 Git 场景复验，全部符合预期。长文件列表不再造成受保护工作流修改被错误放行。历史复现见 `generation/residual-findings.md`。

本代理在隔离临时 Git 仓库中原样执行 `sections[4].code.source`，使用真实提交与文件变更，结果如下。

| 场景 | 实际退出码 | 结果 |
|---|---:|---|
| 缺失 `BASE_REF` | 1 | 正确拦截 |
| 缺失 `HEAD_REF` | 1 | 正确拦截 |
| 缺失必需 `AGENTS.md` | 1 | 正确拦截 |
| 修改 `tests/acceptance/check.py` | 1 | 正确拦截 |
| 新增 `tests/unit/regression.py` | 0 | 正确允许 |
| 修改 `.github/workflows/check.yml` 并新增 2500 个长文件名 | 1 | 正确拦截，并列出受保护的工作流文件 |

其他前轮事实问题已修正：CI 脚本及保护名单要求来自受保护基线；不再用实现分支可自行设置的环境变量代表人工授权；普通回归测试与独立验收层分开；并发发布在最终入口检查最新代次并要求原子性或平台等价保证；Ralph Loop 不再被说成完全消除会话内压缩；Harness 不再局限为生产环境；诊断通常写往 stderr；双语 blob hash 配对只检测文件登记与失步，不能证明语义等价。

依据为本地官方讲义、幻灯片、课堂转录及前轮已核对的官方外链。上述 CI 验证是本代理独立执行；生产 CI 权限、发布服务原子性与服务替身校准是练习验收要求，未声称在真实平台部署验证。PDF 视觉 QA 另行记录。

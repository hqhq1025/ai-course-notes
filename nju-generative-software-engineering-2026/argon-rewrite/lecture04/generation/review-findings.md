# 第 4 讲独立审阅

- sections[0].units[3].after：repo.db 和 RL 保持文档代码一致是设想目标，存图与训练不会自动保证一致。
- sections[1].units[0].after：默认 rebase 不执行测试，Git 因冲突停止与显式配置的测试检查要分开。
- sections[2].units[2].after：git stash 不要求先 git add，能直接保存 tracked 文件的未暂存修改。
- sections[4].units[1].reading、table.rows[1][2]：MVCC 保留多版本，为读写提供对应版本，可结合锁；不等同于先改再检冲突的乐观并发。
- sections[4].units[1].after：锁只协调遵守协议的参与者和覆盖范围，不能无条件消除所有冲突与返工。
- sections[6].code.source：发起异步点评时先 attempt_commit=$(git rev-parse HEAD)，完成后按该 SHA 写 git notes。直接用 HEAD 会在期间推进后把点评挂错提交。
- practice[1]：独立 worktree 的加锁实验必须在锁内同步共同权威分支，再验证和发布，最后解锁；各自重读工作目录不会得到其他分支提交。不要单纯超时删除锁让旧持有者继续写，可用简单串行整合且不自动抢占锁。
- 通篇：减少反复“设想非定论”和“本页指出”。一次介绍来源与目标，后续直接解释机制。jj 保留快照，稳定 change ID 也可能有分歧版本。

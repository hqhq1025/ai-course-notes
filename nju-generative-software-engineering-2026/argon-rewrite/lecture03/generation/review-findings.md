# 第 3 讲独立审阅

- sections[1].units[0].reading：删除日文“しかし”；after 的前者/后者指代颠倒，老项目提供上手路径的体验较好。
- sections[4].units[1].after：tree 原始格式为 mode SP name NUL raw-object-id 串接；git cat-file 的按行展示不是存储格式。
- sections[4].units[1].after、boxes[1].text：git add 就用 stage 0 替换冲突 stages 1–3，无须等到 commit。
- sections[5].code.source：当前 tot_outp/tot_inp 与 dtype=bool 不是 Astropy PR 原代码。固定 head efedd57cb088b6ca73f9540a3c6185ad7046c926 的 _cstack 使用 noutp=_compute_n_outputs(left,right)；Model 分支 cright=_coord_matrix(right,'right',noutp)；矩阵分支 cright=np.zeros((noutp,right.shape[1]))。只展示真实 cright[-right.shape[0]:, -right.shape[1]:] = 1 改为 right 的 diff 最清晰，不编造上下文。
- sections[5].units[1].after：不可编译提交可用 git bisect skip 跳过，可能降低定位分辨率，不是彻底失效。
- sections[7].equation.explanation：操作交换律描述顺序是否影响语义结果，不等于 Git 无文本合并冲突。
- 通篇：Working Tree 是当前可见文件；Git 快照不是物理全复制；根提交无父节点；make submit 是项目命令；MVCC 不等于乐观并发。减少逐页介绍和重复定义，让索引、快照、提交、分支、整合的因果连贯。

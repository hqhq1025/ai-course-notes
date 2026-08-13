# CS25 Lecture 04 Blueprint

Status: complete and accepted on 2026-08-11 after strict coverage, three-pass XeLaTeX stabilization, `⭐⭐⭐` quality audit, and canonical PDF visual QA.

## Goal

把 Aditya Grover 的 Decision Transformer 讲座重写成一份“如何把 offline reinforcement learning 重构为 conditional sequence modeling”的完整中文讲义。讲义不能停留在“把轨迹喂给 GPT”这一句，而要解释数据支持、return-to-go、非 Markov 历史、监督学习目标、autoregressive rollout、probabilistic inference、baseline 设计、长期 credit assignment 和 online RL 边界。

## Teaching Thesis

本讲围绕五个闭环组织：

1. `stable sequence modeling → scalable optimization → sequential decision making`；
2. `logged trajectory → return/state/action tokens → causal Transformer → action prediction`；
3. `desired return → autoregressive rollout → realized environmental return`；
4. `benchmark evidence → baseline / data regime / context ablation → bounded conclusion`；
5. `offline success → exploration, discounting, pessimism and online extensions`。

## Section Plan

1. 来源审计、时间边界与课程问题。
2. MDP、policy、return、offline RL 和 distribution shift 的最小背景。
3. 为什么 RL 没有像 language modeling 一样稳定扩展。
4. Decision Transformer 的 tokenization、return-to-go 和 causal mask。
5. timestep embedding、addition vs. concatenation、non-Markov history 与 partial observability。
6. MSE / cross-entropy 训练目标和不依赖 Bellman backup 的意义。
7. rollout 算法：target return 初始化、reward 回扣、context truncation。
8. RL as probabilistic inference 的直觉与严格边界。
9. offline RL 主结果、return conditioning、percent BC、context length、sparse reward、Key-to-Door 和 critic 实验。
10. 哪些结论不能从这些图推出：数据支持、目标饱和、偶发 extrapolation、online exploration。
11. 总结与延伸：Trajectory Transformer、CQL/pessimism、discounted return、multimodal/multi-agent。

## Figure Plan

- 24 张 recovered slide 均按教学逻辑放置，而不是按视频时间机械堆叠。
- 每组实验图前先定义坐标、baseline、数据 regime 和“应先比较什么”。
- architecture / forward pass / rollout / probabilistic inference / critic 图都需要独立 `读图` 讲解。
- “Experiments” 分隔页用于明确从机制转向证据，不单独承担结论。
- “Useful Links” 放在拓展阅读附近，作为原讲座资源索引。

## Acceptance Targets

- 20+ pages, 24 required source figures, 10+ teaching boxes.
- 3+ teacher-voice markers, 3+ `读图` blocks, formulas with immediate symbol explanation.
- Strict source coverage has no warnings.
- `tools/scripts/check_quality.sh` returns `⭐⭐⭐`.
- Two-pass XeLaTeX and canonical PDF visual QA are clean and signed.

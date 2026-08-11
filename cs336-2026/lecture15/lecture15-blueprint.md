# Lecture 15 Blueprint — Mid/Post-Training

Narrative question: 预训练模型已经会预测文本，怎样用少量行为数据把它变成可控、可用、可评估的 assistant？

1. Pretraining 到 instruction following 的控制缺口。
2. SFT data 的 style、knowledge、safety、tool-use 与规模权衡。
3. Mid-training 把 instruction data 混回大规模训练的原因。
4. Preference data 的收集、annotator distribution、AI feedback 与伦理。
5. PPO 的 on-policy pipeline、KL 约束与工程复杂度。
6. DPO 如何从 KL-regularized objective 得到离线 pairwise loss。
7. Reward overoptimization、length bias、mode collapse 与校准退化。

Transition out: Lecture 16 将把不可验证的人类偏好换成可验证 reward，进入 RLVR。

（因为因为，陈老师真的分享了很多很多的动图和视频，本集结合视频服用效果更佳噢！嘿嘿！预祝你学得开心！学得顺利啦！）

今天的嘉宾是清华大学交叉信息研究院助理教授、星动纪元创始人陈建宇。他的研究和创业方向都是人形机器人。

大语言模型浪潮爆发后，学界和工业界看见了机器人从专用走向通用的可能迹象，机器人革命随之而来。其中，本轮革命最重要的是，对机器人底层架构，也就是机器人“大脑”的探索。

但通用机器人还在科学研究阶段，处于产业发展早期。这集节目，陈老师将带领大家，概览式阅读机器人基座模型和当下最前沿的架构VLA架构（Vision-Language-Action Model，视觉语言动作模型）的经典论文。

希望我们的节目能直观地帮助更多人靠近科学前线，感受技术之美，并且能直观感知当前技术拐点。

还是那句话：期待2025，我们和AI共同进步！

我们的播客节目在腾讯新闻首发，大家可以前往关注哦，这样可以第一时间获取节目信息和更多新闻资讯：）

02:30 陈建宇的研究和创业方向
04:11 讲解开始前，先提问几个小问题
17:36 当下最大变量：从专用模型到通用模型（robot foundation model）的可能性
21:12 大模型浪潮爆发后，机器人领域经历了两个阶段：从利用基础模型进行机器人研究（leveraging foundation models in robotics）到为机器人预训练基础模型（pretraining foundation models for robotics）
第一阶段：利用基础模型进行机器人研究（leveraging foundation models in robotics）
21:59 机器人传统三板块：Planning+Perception+Actuation（规划+感知+执行）——第一步，用LLM（Large Language Model，大语言模型）替代Planning
23:54 由Google Robotics团队提出的具身智能开创性论文Say Can《Do As I Can, Not As I Say: Grounding Language in Robotic Affordances》
（中文名：我能做到，而不是我说到：将语言与机器人的可供性相结合）
27:03 第二步，用VLM（Vision-Language Models，视觉语言模型）替代Perception
27:52 来自Google的论文《Inner Monologue: Embodied Reasoning through Planning with Language Models》
（中文名：内心独白：通过语言模型规划进行具身推理）
29:51 由清华和上海姚期智研究院提出的《DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment》
（中文名：DoReMi：通过检测和恢复规划-执行不一致来落地语言模型）
32:47 第三步，想把Actuation进一步自动化，用Code LM（专门用于代码相关任务的大型语言模型）来替代Actuation
32:24 由李飞飞团队提出的《VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models》
（中文名：VoxPoser：使用语言模型进行机器人操作的可组合3D价值地图）
第二阶段：为机器人预训练基础模型（pretraining foundation models for robotics）
38:36 VLA端到端模型（Vision-Language-Action Model，视觉语言动作模型）——“人是很智能的VLA Agent”
39:53 关于VLA的经典论文及分类
40:17 Aloha论文《Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware》
（中文名：学习用低成本硬件进行精细双手操作）
47:36 Mobile Aloha论文《Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation》
（中文名：移动ALOHA：使用低成本全身远程操作学习双手移动操作）
50:15 论文《A Generalist Agent》介绍了一个名为Gato的通用型人工智能代理
（中文名：通用型代理）
52:45 RT-1论文《RT-1: Robotics Transformer for Real-World Control at Scale》
（中文名：RT-1：机器人Transformer用于大规模现实世界控制）
59:02 Octo论文《Octo: An Open-Source Generalist Robot Policy》
（中文名：Octo：一个开源的通用机器人策略）
01:02:20 CrossFormer论文《Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation》
（中文名：扩展跨具身学习：操控、导航、运动和飞行的统一策略）
01:06:58 字节跳动AI Lab的两个工作GR-1和GR-2：
《Unleashing Large-Scale Video Generative Pre-Training For Visual Robot Manipulation》（为视觉机器人操控释放大规模视频生成预训练模型）
《A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation》（用于机器人操作的网络规模知识生成视频-语言-动作模型》）
01:15:02 Palm-E论文《PaLM-E: An Embodied Multimodal Language Model》
（中文名：PaLM-E：具身多模态语言模型）
01:20:02 当前VLA最有名的开山工作：Google推出的RT-2论文《RT-2：Vision-Language-Action Models Transfer Web Knowledge to Robotic Control》
（中文名：RT-2：视觉-语言-动作模型将网络知识迁移到机器人控制中）
01:26:05 RT-X论文《Open X-Embodiment: Robotic Learning Datasets and RT-X Models》
（中文名：开放X具身：机器人学习数据集与RT-X模型）
01:31:16 《OpenVLA: An Open-Source Vision-Language-Action Model》（约等于开源版RT-2）
（中文名：OpenVLA：一个开源的视觉-语言-动作模型）
01:32:56 陈建宇课题组《HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers》
（中文名：HiRT：利用分层机器人Transformer增强机器人控制）
01:38:40 Figure AI Helix，没发论文，但是今年Figure最新架构
01:39:28 Pi0论文《π₀: A Vision-Language-Action Flow Model for General Robot Control》
（中文名：π₀：一个视觉-语言-动作的流模型用于通用机器人控制）
01:41:36 英伟达最近发布的GROOT N1模型《GR00T N1: An Open Foundation Model for Generalist Humanoid Robots》
（中文名：GR00T N1：通用人形机器人的开放基础模型）
01:42:32 《Diffusion Policy: Visuomotor Policy Learning via Action Diffusion》
（中文名：扩散策略：通过动作扩散进行视觉运动策略学习）
01:47:39 清华发布的《RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation》
（中文名：RDT-1B：双手操作机器人的扩散基础模型）
01:51:04 《Prediction with Action: Visual Policy Learning via Joint Denoising Process》（动作预测：通过联合去噪过程进行视觉策略学习）
和续作《Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations》（视频预测策略：一个预测视觉表征的通才机器人策略）
02:03:06 两个未来方向：《UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent》（UP-VLA：具身智能体的统一理解与预测模型）
《Improving Vision-Language-Action Model with Online Reinforcement Learning》（通过在线强化学习改进视觉-语言-动作模型）
02:09:22 最后的提问

影片来源：影视飓风
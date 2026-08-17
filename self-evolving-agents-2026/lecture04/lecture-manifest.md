# Lecture Source Manifest

## Local Sources

- `video.mp4`: merged public Bilibili video stream.
- `audio.wav`: 16 kHz mono transcription input.
- `subs.srt` / `subs.txt` / `subs.json`: local Whisper transcript.
- `frame-candidates/`: 15-second visual sampling.
- `slides-images/`: cropped, perceptually deduplicated slide candidates.

## Coverage Matrix

| # | Time | Slide | Spoken explanation | Planned treatment | Status |
|---:|---|---|---|---|---|
| 1 | 00:00:00 | `slides-images/slide-001-00000s.jpg` | 那我们是到最后今天上午最后的一个报告是由这个人大高领人工智能学院博士生佟冠婷带来的那么冠婷呢是研究General Agent TrainingAgentic RL与Agent Harness Engineering是自己研究实习生曾实习于阿里签问快手CLEAR基座大模型组他今天的这个报告题目呢是Agent World让智能体育环境协同进化冠婷可以开始了好的  | Identify claim, visual reading, limits, and connection | pending |
| 2 | 00:00:30 | `slides-images/slide-002-00030s.jpg` | 好的 感谢介绍大家好 很荣幸受到邀请来参加这次分享我分享的题目是Agent World推动智能体与环境的协同进化因为这在资金化领域的话无论是智能体它其实是离不开环境如何让环境和智能体一起进化显然是我现在正focus的一个topic我是来自中国人民大学高领人工智能学院的董冠婷Background从聊天助手到真实世界的智能体 | Identify claim, visual reading, limits, and connection | pending |
| 3 | 00:01:00 | `slides-images/slide-003-00060s.jpg` | 从聊天助手到真实世界的智能体随着大模型推理和规划能力的一个涌现大家对大模型的期待也是从聊天助手到完成真实世界任务的智能体而为了满足这一需求智能体不仅需要去理解用户的潜在意图同时还需要去自主调用的外部工具并持续去监控它的一个反馈来调整它后续的策略来完成任务比如说我们的定外卖与写飞书而近期的话MCP和Agent Skills以及各类的这种Harness Engi | Identify claim, visual reading, limits, and connection | pending |
| 4 | 00:04:15 | `slides-images/slide-004-00255s.jpg` | 然后来去提供一个可扩展环境的一个recipe现有环境的话其实已经有了一些的这个工作就像我刚才所介绍的我也是尝试把它们分成了两条比较好理解的线第一条其实是simulated environment也就是我们让大模型去扮演外部工具和环境的一个反馈这个大模型会根据agent policy推比的上下文去模拟它的一个反馈比如说我可能agent policy提供一个订外 | Identify claim, visual reading, limits, and connection | pending |
| 5 | 00:07:45 | `slides-images/slide-005-00465s.jpg` | 也是我最近五月份人大和Z跳动C的联合推出来的一篇工作它主要分为两步第一步是智能体的环境任务探索我们通过深度调研的智能体自主去从互联网环境中去挖数据库然后实现这种工具合成和任务合成来构建可扩展的环境进入的话我们也是把多环境的强化学习训练到智能体中并且把我们合成的环境视为一个训练场不断的去实现我刚才所说的迭代去定位智能体能力短板然后让它自进化的一个循环的一个机制 | Identify claim, visual reading, limits, and connection | pending |
| 6 | 00:09:15 | `slides-images/slide-006-00555s.jpg` | 也在积极之心受到推送大家感兴趣可以去看一看相关的博客下面介绍agent我们agentware最关键的一款agent environment task discovery我们想法也是尽量从真实的mcp环境等等主题出发因此我们精选了2000个真实的主题包括有2800个mcp server大概有0.5k个开源工具的document以及0.200个行业的prd行业的 | Identify claim, visual reading, limits, and connection | pending |
| 7 | 00:11:30 | `slides-images/slide-007-00690s.jpg` | 左侧的话展示了我们上层20个环境的一个信息右侧其实展示了我们Top10的二级环境对应的三级环境的一个数量比如说每个二级环境下可能都会有几百个这样三级的MCP server的环境这是我们的一个分类体系 | Identify claim, visual reading, limits, and connection | pending |
| 8 | 00:11:45 | `slides-images/slide-008-00705s.jpg` | 这是我们的一个分类体系那下面也是为了让大家更好理解这个road data是什么样的我举了两个例子比如说我们的travel system它里面的一个Airport CSV的一个文件就是可以看到是从某个地它的country code是什么它从某一个地方飞到某一个地方它的航班号经纬度等等等等这些都是智能体它完全自动化的去挖掘出这些信息并把它们总结成不同类型的这种文 | Identify claim, visual reading, limits, and connection | pending |
| 9 | 00:12:30 | `slides-images/slide-009-00750s.jpg` | 然后它的一些日期等等等等整个都是有智能体自己去挖掘的一个事情那么基于这样高质量的环境生态agent war其实采用了两种互补的可验证的任务合成策略包括基于图的任务合成我们去构建工具依赖性的DAG包括强依赖弱依赖random这个也很好理解比如说我们查了一张机票之后我们其实强相关的一个强依赖的工作工具就是定机票我们查完就想定那也可能我们查完之后也有可能会退票因为 | Identify claim, visual reading, limits, and connection | pending |
| 10 | 00:14:00 | `slides-images/slide-010-00840s.jpg` | 为后续的rl提供了一个可靠的奖励那下面展示了我们任务合成的一些这个statistics吧包括我们环境的这个diversity以及我们工具每个环境的工具数量可以看到每个环境可能平均大概有十多种工具然后每个工具的话它的parameters数量可能也比较多并且我们能够合成多样化的database的field type包括像json格式的csv格式甚至它还能合成la | Identify claim, visual reading, limits, and connection | pending |
| 11 | 00:15:00 | `slides-images/slide-011-00900s.jpg` | 合成完高质量的任务之后我们就是想要去通过一种环境的算法去把它训进去那其实也是如我刚才所说的与传统agentrl不同它并不像静态的搜索我们只需要跟搜索系统交互就可以了那我们的训练的一个rawl的过程其实是智能体去调用工具工具再和数据库去交互那么它会形成一个三者的一个rawl的一个交互模式这样的话也能够更好的去对状态做一个学习而进一步的话像structure v | Identify claim, visual reading, limits, and connection | pending |
| 12 | 00:16:00 | `slides-images/slide-012-00960s.jpg` | 整体的一个reward的一个rl的流程都在下面展现了最后其实也是最关键agentward的一个方法就是self-involving的agent arena它的一个核心其实就是将环境生态作为智能体的天然训练场并且去多轮的迭代那我们的想法也很简单其实可以根据这个图来讲吧比如说我们有一个已经被agent扰扰过一次的agent它可能初步具备了一些通用智能体的能力然后 | Identify claim, visual reading, limits, and connection | pending |
| 13 | 00:18:00 | `slides-images/slide-013-01080s.jpg` | 那整体就形成了一个闭环的训练飞轮那在实验评测方面我们也是尽可能想要去选择更加广阔的baseline和benchmarks然后我们也是评估了很多的B元强模型包括GPT5.2Cloud Sonite 4.5GM3 ProCW.0等等这些都是因为这篇工作是在2月份做的所以说开始做的因为那个时候可能这些模型就是当时最强的模型然后开源模型的话也会选择千问三的一系列模型 | Identify claim, visual reading, limits, and connection | pending |
| 14 | 00:19:15 | `slides-images/slide-014-01155s.jpg` | 以及我们也融入了MCP Universe的一系列通用的子斗面整体的性能可以看到其实在三个较为强的这种MCP的基准上我们发现B原模型的分配尤其在MCP MarkGPT 5.2可能也只有53分左右而我们发现Agent War8B和14B其实是能够稳定超越一系列的开源Baseline的特别是在BFCL V4上我们发现Agent War14B能够达到55.8分它其实 | Identify claim, visual reading, limits, and connection | pending |
| 15 | 00:20:15 | `slides-images/slide-015-01215s.jpg` | EMA Scalar 8B以及Agent War 8B我们从多个维度上去对比发现在通用推移领域一系列数学推移的Benchmark上我们的性能没有退化它其实还甚至有一点点的微涨然后在深度搜索和软件工程领域的话其实在这种超长轮词上我们发现相比于这些环境的背似弹会有一个非常明显的提升这其实也很合理因为我们做环境合成的时候我们发现其实它会有和自主去合成一些代码相关G | Identify claim, visual reading, limits, and connection | pending |
| 16 | 00:21:00 | `slides-images/slide-016-01260s.jpg` | 进一步我们也是去在我4月的时候我也是看到现在有很多Frontier的AI的Benchmark相较于SkillsBenchArg AGI以及CloudEvo我们也是在这三个上面做了一个评测发现Agent War的8B和14B相比于同size的一些Baseline都有一个更为稳健的性能对然后第三个实验是我最想要去探索的也就是说随着我们环境的规模的扩展 | Identify claim, visual reading, limits, and connection | pending |
| 17 | 00:21:30 | `slides-images/slide-017-01290s.jpg` | 也就是说随着我们环境的规模的扩展是否性能会有一个更好的tradeoff我们发现从0个环境扩展到2000个训练环境它其实在初期的时候是有一个非常明显的涨幅然后到后期的话可能也会有微微的涨幅这其实也说明可能初步我们覆盖到更多的环境那性能势必就会有一个更好的效果而随着环境的体量越来越大那可能进一步去覆盖的环境可能更多是去覆盖一些细力度之前粗力度环境照顾不到的一些模 | Identify claim, visual reading, limits, and connection | pending |
| 18 | 00:22:00 | `slides-images/slide-018-01320s.jpg` | 之前粗力度环境照顾不到的一些模式下面我们也是做了一些自进化轮次的分析也就是说我们刚才的self evolving arena去把它迭代的去调用一轮两轮甚至N轮等等我们去探索发现无论是我们把我们自己的模型放在这个我们的self arena还是我们把一个陌生的一个外面的 baseline模型我们放到我们自己的环境去做这种self arena的这种进化它都会有一个 | Identify claim, visual reading, limits, and connection | pending |
| 19 | 00:22:30 | `slides-images/slide-019-01350s.jpg` | 它都会有一个一致性的提升这其实也说明我们的这个arena自进化是非常有意义的后面乔和学习的许线也是比较稳定这话就不多说了那总结于展望其实Agent World的作为作者 | Identify claim, visual reading, limits, and connection | pending |
| 20 | 00:22:45 | `slides-images/slide-020-01365s.jpg` | 其实Agent World的作为作者我也是有发现一些启示也希望能和大家一起去探索包括真实性可能是扩展环境扩展的一个底座我们发现构建高真实逻辑可教研的环境其实是训练智能体的一个前提Agent World可能提出了一套自动化的流程我们也相信未来会有更多更自动的流程以及Moke真实世界的环境合成范式的涌现第二点是进化是环境的一个训练的动力规模化的环境生态建成的话其 | Identify claim, visual reading, limits, and connection | pending |
| 21 | 00:24:00 | `slides-images/slide-021-01440s.jpg` | 后面的话也是一些展望未来的我们觉得可能有很多的地方可以去优化像数据合成这块有智能体数据合成扩展环境全模态扩展训练算法包括智能体敲响学习推理技术智能体的训练以及像现在harness的这种多智能体的workflow异步高效的infra测的优化上下文的记忆管理我自己也是认为可能离通用智能体还比较远现在还处于一个大模型正在内化世界工具正在去掌握它master它这种外 | Identify claim, visual reading, limits, and connection | pending |
| 22 | 00:24:30 | `slides-images/slide-022-01470s.jpg` | master它这种外部工具外部skills等等去调用的一个能力那后面是有一些实验室的相关的工作大家可以关注一下包括Einway ScalarETAgent等等等等OK 感谢大家的聆听 | Identify claim, visual reading, limits, and connection | pending |
| 23 | 00:24:45 | `slides-images/slide-023-01485s.jpg` | OK 感谢大家的聆听我的介绍大概就到这里大家如果感兴趣可以问一些问题包括也可以后续自下来扫码来问一下我一些更深刻的一些问题我的介绍大概就到这里好的 谢谢冠婷这是Agent World是一个非常销售的工作周围很多课题组的同学也都在follow这个工作然后我从评论区还是选两个问题来问吧看同学也非常的反响 | Identify claim, visual reading, limits, and connection | pending |
| 24 | 00:25:15 | `slides-images/slide-024-01515s.jpg` | 看同学也非常的反响非常热烈第一个问题是工具强弱依赖的这个信息是从哪里来的呢工具强弱依赖的话其实是我们通过大模型去生成的对 也就是说我们会把这一系列的工具给到它它自己就会去探索哪个工具之间它自己会去思考这个工具和这个工具是否是一个强依赖性的对 然后我们会对它去assign一个全值可以作为我们DAG编的一个全值 | Identify claim, visual reading, limits, and connection | pending |
| 25 | 00:25:45 | `slides-images/slide-025-01545s.jpg` | 好的 然后第二个问题又来选就是如果对薄弱的任务继续RL会不会让模型忘记之前已经学到的一些能力同时进化多轮之后Rout能力收敛进化多轮之后我们的模型能力收敛不再提升要怎么办 | Identify claim, visual reading, limits, and connection | pending |
| 26 | 00:26:00 | `slides-images/slide-026-01560s.jpg` | 进化多轮之后我们的模型能力收敛不再提升要怎么办对 这个其实我自己有面临到遗忘的话其实倒是不太会因为我们发现可能Agent RL其实它并不会像SFT那样完全就把之前能力覆盖掉但是我们确实会遇到棒得住的情况其实我这个实验的效果就可以看到第一轮的话它其实是一个非常迅猛的增长其实第二轮它的一个增长就已经有一些棒的了这其实也说明它可能已经渐渐在我理解这就是我们在不断的 | Identify claim, visual reading, limits, and connection | pending |

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
| 1 | 00:00:00 | `slides-images/slide-001-00000s.jpg` | 那我们就进入到下一个报告了那么下一位讲者是来自NVIDIA Research研究科学家张绍坤绍坤老师主要从事Agent Training相关研究博士毕业于Pennsylvania State University曾在NVIDIA Microsoft Research实习他今天带来的报告是Toward Self-Evolving AgentsArm as Op | Identify claim, visual reading, limits, and connection | pending |
| 2 | 00:00:45 | `slides-images/slide-002-00045s.jpg` | OK,好,谢谢文文老师的介绍我先做个自我介绍我叫张绍坤,然后我博士刚刚毕业我现在在NVIDIA Research做Agentic RL的研究然后主要侧重下游的application是Computer Use Agent然后由于我在博士期间的主要的Research Topic是Self-Involving Agent然后我在NVIDIA做研究的时候工业界里我们 | Identify claim, visual reading, limits, and connection | pending |
| 3 | 00:01:30 | `slides-images/slide-003-00090s.jpg` | 然后来分享给大家对,第一个是我想说一下我对于Self-Involving Agent的一个理解我觉得对于Self-Involving Agent来说我们所希望我所理解它有两个比较重要的特性第一个是可以recursively的去修正去学习从他们自己的Own的Experience里面这里面有两个东西第一个是可以自迭代的去学习也就是说他自我学习的能力可以随着自我的 | Identify claim, visual reading, limits, and connection | pending |
| 4 | 00:03:45 | `slides-images/slide-004-00225s.jpg` | 我今天主要对主要就从这两点来说第一个是recursive的self improvement我会主要介绍我在博士期间所做的agent optimizer在这里面我会介绍说证明agent如何去优化它自己把可以去优化它自己的learnable component这个是这个工作是在2024年那个时候还只有2023年开始做到2024年所以它最开始只有我们用的model | Identify claim, visual reading, limits, and connection | pending |
| 5 | 00:05:15 | `slides-images/slide-005-00315s.jpg` | 我会来依次来介绍这两个工作然后第一个工作是agent optimizer我们说一个agent在我们现在当下2026年的理解来说agent他分为model和harness两部分这两个组件构成来说一个agent他效果好不好也是说我的model本身强不强作为base然后另外是它的harness我的harness设计的好不好它的promise它的tool怎么样比如如 | Identify claim, visual reading, limits, and connection | pending |
| 6 | 00:06:45 | `slides-images/slide-006-00405s.jpg` | 然后让自己得到imput在这个场景下的效果变得更好就是一个最开始的一个idea那么我们是怎么做呢我们说ok那我们现在先有一个agent那我们先说agent那好吧那你先在不同的environment先去做实验我们这些environment是这些data是从已经现有的在现有的数据里面去选的比如说mass比如说mass做数学体和盖亚做一些general的assis | Identify claim, visual reading, limits, and connection | pending |
| 7 | 00:07:45 | `slides-images/slide-007-00465s.jpg` | 我们把agent丢到mass里做了20道题那么我们获得了20个答案然后我们再把agent丢到另外一个lm里面我们叫它agentodermizeragentodermizer和agent它们俩都是一个模型在当时做的时候都是gbt3.5我们每一个iterationiteration我们说ok那你现在可以去create revise或者remove你现在的tool | Identify claim, visual reading, limits, and connection | pending |
| 8 | 00:09:15 | `slides-images/slide-008-00555s.jpg` | 这可能是一个非常直观而且效果非常好的一个一个优化agent的一个方式那这块我们我在这个talk里面我只收了我们做实验里面的一个optimize过程中的图我觉得这个图是比较具有启发性的红色的线是training curve也就是它的training的accuracy然后蓝色的线是它的test performance我们在这个里面我们是在盖亚上是general的 | Identify claim, visual reading, limits, and connection | pending |
| 9 | 00:10:00 | `slides-images/slide-009-00600s.jpg` | 但整体仍然向上去进行了一个优化对然后我们在下一个图表我展示了说我们说OK前面我拿agent去优化它的harness也就是它的tools我们想看到说到底到底它优化的tools有多么的好我能展示了第二个epoch和最后一个epoch它成功的去call to在对于chatsgbt3.5来说call to在还是个满难的问题复杂度还是个满难的问题现在看来说可能已经解决 | Identify claim, visual reading, limits, and connection | pending |
| 10 | 00:11:30 | `slides-images/slide-010-00690s.jpg` | 是在一个early effort来收益说ok我们可以让LM去recursive的去improve自己这个是possible的然后对于LM agent来说它也是useful的尤其在考虑说如果在GPU之前比较酷迫的情况下我们可以通过通过让不修改本身的base model然后修改agent harness来实现一个自我进化但是在这个scope仍然是比较受限因为现在 | Identify claim, visual reading, limits, and connection | pending |
| 11 | 00:13:15 | `slides-images/slide-011-00795s.jpg` | 这也就是我需要去介绍的下一个工作我下一个介绍的工作是proagent server它是一个agent rollout infrastructure我们说agent optimizer他从外部的data去进行学习我们下一个是想让他去learn from他自己和环境的一个交互的数据所以这也就是大家都做rl大家发这个东西确实有用那我就rl本身也就是说让agent在 | Identify claim, visual reading, limits, and connection | pending |
| 12 | 00:14:30 | `slides-images/slide-012-00870s.jpg` | 然后polar agent server就是我们用来设计来解决这个问题的那现在的rl training的训练rl training的library他们都是怎么设计的就左边他们一般都是大多数的工作他们都是cpu的design比如说在reinforce learning training的loop里面我的agent的我的agent的rollout它需要首先建立一 | Identify claim, visual reading, limits, and connection | pending |
| 13 | 00:17:45 | `slides-images/slide-013-01065s.jpg` | 已经更新到vr版本是polar我们的polar现在是分为这么几个模块polar本身它是一个roal server它负责和agent的不同的agent harness交互我们现在可以support任何harness我们把harness当作blackbox它可以是codex也可以是cloudcode也可以是什么opencloud也好或者hermespy agen | Identify claim, visual reading, limits, and connection | pending |
| 14 | 00:19:45 | `slides-images/slide-014-01185s.jpg` | 来进行waitsync对这张slide呢我主要是想讲我们pro agent server和为什么要这样设计因为对于本质上来讲我们只通过建立了一个监听符我们监听的是说codex和cloud code他们背后靠lm的inference engine的时候我们把这部分的他code的时候request我们把它给截掉了所以就是说cloud code想要去调用一个lm那 | Identify claim, visual reading, limits, and connection | pending |
| 15 | 00:21:30 | `slides-images/slide-015-01290s.jpg` | 然后下面我展示我们projects server的一个流水线我们是一个full asynchronous的一个过程我们把agent rollout的分为大概三步第一步是init就是说我如何去启动这个sandbox如何安装包布置agent解决这个问题所必须的环境然后第二个是wrongwrong就是agent的具体去靠这个vom也好或者是靠什么什么什么手势什么什 | Identify claim, visual reading, limits, and connection | pending |
| 16 | 00:23:00 | `slides-images/slide-016-01380s.jpg` | 这是我们整体设计的一个逻辑对然后下一个问题我们在pro agent server里面所解决的是说我们在做rl的时候对于比如我们如果想训练一个比较复杂的agent比如cloud code它内部是会掉很多sub agent然后sub agent呢它虽然靠的是同一个model但是但是它丢出来的我们只通过http去补货补货到那些补货到那些数价坡它是分散的所以就会就会 | Identify claim, visual reading, limits, and connection | pending |
| 17 | 00:24:30 | `slides-images/slide-017-01470s.jpg` | 去去缩减缩减很多然后对然后下面是我想介绍分享我们现在所做的一个实验的一个进度对然后现在我们的harness现在支持就是就是我就是codexcloco的queen还有派agent我们现在还支持了更多在这个paper呃paper呃technic report之前之前之前呃我们可以看到把这四种不同的harnessspace model我们用的是呃queen呃呃所以 | Identify claim, visual reading, limits, and connection | pending |
| 18 | 00:25:45 | `slides-images/slide-018-01545s.jpg` | proarragent server这里边这在这些s就是一个更具体的例子说我们proarragent server他给你给那个trainer返回的是什么东西我们会返回prong的idresponse id然后loss mask是哪些prong的需要算那个grill需要进行计算哪些需要算那个t度哪些不需要然后还有response的log probability | Identify claim, visual reading, limits, and connection | pending |
| 19 | 00:26:30 | `slides-images/slide-019-01590s.jpg` | 呃大家可以有空去尝试一下就就只需要分三部分第一部分是装这个rollout server本身我们我们有我们可以现在可以一键安装就是不会有太多的一个成本然后第二个是因子就是安装那个inference的那个inference engine我们现在支持VLM和sgla然后对于不同的那个benchmark我们现在提供了随笨主要是随笨是相关task的一些一键脚本去部署部 | Identify claim, visual reading, limits, and connection | pending |
| 20 | 00:27:30 | `slides-images/slide-020-01650s.jpg` | 它是作为一个realout service architecture能够让我们去skilling这个agentic RL的一个训练然后他用agent的IoM API的payroll source就是我们监听了agent和底层的这个inference engine的交红板我们把那部分东西给截下来这样的话我们用户就不需要去touchagent harness本身 | Identify claim, visual reading, limits, and connection | pending |
| 21 | 00:28:45 | `slides-images/slide-021-01725s.jpg` | 就是实现selfie involving agent的一个非常promising的一个路径对然后我的分享就是这些谢谢大家非常精彩的报告不仅从algorithm还从infra的角度给大家带来了一些怎么去做selfie involving agent的这种视角 | Identify claim, visual reading, limits, and connection | pending |
| 22 | 00:29:00 | `slides-images/slide-022-01740s.jpg` | 还从infra的角度给大家带来了一些怎么去做selfie involving agent的这种视角我们还是两个问题吧然后我从这个评论区选两个就是问题都给大家第一个问题是说agent的中间有很多组件梯度是怎么传回去的呢agent的中间有很多组件对是这样子的是我们算梯度的时候其实大家都是拿那个policy grading的算那么我们不需要touchagent的组 | Identify claim, visual reading, limits, and connection | pending |

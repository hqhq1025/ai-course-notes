# 讲义质量标准

本文档定义 AI Course Notes 讲义的质量分级标准，用于自检、PR 审核和改进优先级排序。

## 质量等级

| 等级 | 标签 | 含义 |
|------|------|------|
| ⭐⭐⭐ | **优秀** | 可作为参考范例，结构完整、图文并茂、教学信号丰富 |
| ⭐⭐ | **达标** | 覆盖主要内容，结构清晰，可独立阅读 |
| ⭐ | **基础** | 有内容但偏薄，缺图/缺结构/缺深度，需要改进 |

## 达标标准（⭐⭐）

一份讲义至少需要满足以下**全部**条件才算达标：

### 结构完整性

- [ ] 有封面页（标题、来源、日期、项目主页）
- [ ] 有目录
- [ ] 用 `\section` / `\subsection` 组织，层次清晰
- [ ] 每个大节有 `\subsection{本章小结}`
- [ ] 文档末尾有 `\section{总结与延伸}`
- [ ] 编译无错误（xelatex 两次通过）
- [ ] 编译后的 PDF 已渲染成页面截图/contact sheet 并人工检查，发现的排版/显示问题已修正

### 内容深度

按内容类型，页数下限不同：

| 内容类型 | 达标页数 | 优秀页数 | 说明 |
|----------|----------|----------|------|
| 1h+ 课程视频 | ≥20p | ≥28p | CS336, CS224N, CS231N 等正课 |
| 30-60min 演讲/talk | ≥8p | ≥12p | CS25, Berkeley, 独立演讲 |
| 短演讲 (<30min) | ≥5p | ≥8p | 嘉宾 talk、圆桌片段 |
| 技术文章 | ≥8p | ≥12p | 博客、X Article |
| 深度访谈 (1h+) | ≥15p | ≥20p | 长访谈 |

### 教学元素

- [ ] **高亮盒子** ≥5 个（importantbox + knowledgebox + warningbox），且三种类型都有使用
- [ ] **图片/插图** ≥3 张（slides 截图、视频帧、或示意图），1h 课程 ≥10 张
- [ ] 若有官方 slides、PDF deck、可执行 slides source，或视频中明确使用 slides，则应覆盖每一页有教学内容的 slide 截图；不能只挑几张代表图
- [ ] 每页 slide 截图都要配解释和展开：说明它讲什么、为什么重要、与前后文如何连接
- [ ] 每张图有脚注标注来源（slides 页码或视频时间区间）
- [ ] 每张重要图后都有“读图说明”：解释坐标轴/列含义/图例/关键趋势/教学结论/容易误读之处
- [ ] 概念或术语密集段落后有集中解释表、概念框或结构图，不只堆缩写和名词列表
- [ ] 关键背景概念优先用框图、流程图、对照表或公式链路串起来，再配精炼文字说明
- [ ] 公式用 `$$...$$` 展示，后跟符号说明
- [ ] 代码用 `lstlisting` 包裹并有 caption（如有代码内容）

### PDF 视觉验收

LaTeX 编译通过不等于 PDF 可读。每份讲义完成前必须做视觉验收：

```bash
mkdir -p /tmp/pdf-check
pdftoppm -png -r 120 <notes.pdf> /tmp/pdf-check/page
montage /tmp/pdf-check/page-*.png -thumbnail 240x340 -tile 4x -geometry +8+8 /tmp/pdf-check/contact.png
```

如果系统只有 ImageMagick 7 包装命令，则用 `magick montage ...` 替代 `montage ...`。

检查 contact sheet 和可疑页面的原始截图，确认：

- 图片不缺失、不空白、不被裁切，且关键文字可读
- 重要图附近有解释，没有孤立 dense plot/table
- 表格、公式、代码块没有溢出页边
- 高亮盒标题和内容没有被数学符号、下划线或长英文弄坏
- 没有孤立标题、孤立 caption、大面积空白页
- URL 或长英文没有造成明显 overfull 行

### 内容质量

- [ ] 覆盖视频/文章中 **≥80%** 的核心知识点（不遗漏关键概念）
- [ ] 按教学逻辑重新组织（不照搬字幕/原文顺序）
- [ ] 跳过非教学内容（问候、闲聊、广告）
- [ ] 技术术语保留英文原文
- [ ] 无明显的事实错误或公式抄写错误

## 优秀标准（⭐⭐⭐）

在达标基础上，还满足：

- [ ] 高亮盒子 ≥10 个，分布均匀，每个携带具体教学信息
- [ ] 核心图表不只是“贴图 + caption”，而是有可独立阅读的图表解读
- [ ] 对术语密集区有 glossary-style 集中消化，解释每个术语解决的问题、核心机制和与课程主线的关系
- [ ] 有拓展阅读（`\subsection{拓展阅读}`）引用相关论文/资源
- [ ] 总结与延伸包含：核心要点提炼 + 跨章节关联 + 开放问题
- [ ] 图片质量高（优先用 slides 截图而非视频帧）
- [ ] 有 worked example 或推导过程的逐步展开

## 图表与术语解释标准

用户反馈明确指出：讲义中“看起来重要但没有解释”的图，和“术语密集但没有消化”的段落，会显著降低可读性。后续生成或修订讲义时，必须按以下标准处理。

### 有 slides 时必须覆盖每一页

若课程有官方 slides、PDF deck、可执行 slide source，或者视频画面中明确出现逐页 slides，则 slides 是讲义的视觉主线。默认要求：

1. 将每一页 slide 渲染或截图保存到 `slides-images/` 或 `images/`。
2. 每一页有教学内容的 slide 都应插入讲义中，放在对应讲解位置。
3. 每张 slide 后必须有解释和展开，不能只有 caption。
4. 对 dense slide 使用 `读图` 说明：解释列、轴、图例、baseline、例子、公式和关键趋势。
5. 对连续 build-up 的 slides，至少保留最终完整状态；中间页若表达不同推理步骤，也应保留。
6. 可省略纯行政页、空白页、重复页、版权页、目录页等低教学信息页，但这应是明确取舍。

这条规则高于最低图片数量要求。不能因为质量脚本显示 figures 足够，就跳过大部分 slide。

### 重要图必须配读图说明

凡是满足以下任一条件的图，都不能只放 caption：

- 图中有多条曲线、多列数字、多个子图或复杂图例
- 图承担论证功能，例如 scaling、benchmark、资源分解、系统瓶颈、accuracy 曲线
- 图来自论文/slide，读者不看原文很难理解上下文
- 正文用“这张图说明……”引出某个结论

读图说明至少覆盖：

1. **图在看什么**：横轴、纵轴、行/列、图例、颜色、baseline 分别代表什么。
2. **关键趋势**：哪些曲线/数字在上升、下降、转折、贴近 baseline 或突然跃迁。
3. **教学结论**：这张图支持正文中的哪个论点。
4. **误读警告**：它不说明什么，哪些因果关系不能从图中直接推出。
5. **课程连接**：它和前后章节、系统瓶颈、实验设计或工程决策有什么关系。

推荐写法：

```tex
\begin{knowledgebox}{读图：这张图应该怎么看}
先解释坐标轴、图例和 baseline；再描述最重要的趋势；最后说明它支持的教学结论。
\end{knowledgebox}

\begin{warningbox}{读图时容易犯的错误}
说明不能从图中直接推出的结论，例如 FLOPs 占比不等于 wall-clock 时间，相关性不等于因果。
\end{warningbox}
```

### 概念密集段落必须集中消化

如果一个段落连续出现 4 个以上术语、缩写、模型名、系统名或论文名，就必须加一个集中解释块。典型场景包括：

- LSTM、seq2seq、attention、Adam、Transformer、MoE、ZeRO、Megatron-LM 等历史积木
- QAT/PTQ/GPTQ/AWQ、GQA/MQA/MLA/CLA 等相近术语
- pipeline/tensor/data/sequence/context/expert parallelism 等并行术语
- TTFT、latency、throughput、utilization、arithmetic intensity 等系统指标
- sharding、fused kernel、collectives、optimizer state、activation checkpointing、DRAM/SRAM/HBM 等 systems/resource-accounting 术语

集中解释可以用 `longtable`、`knowledgebox` 或 `importantbox`。每个术语至少说明三件事：

| 维度 | 要回答的问题 |
|---|---|
| 解决的问题 | 它为什么被提出？旧方法卡在哪里？ |
| 核心机制 | 它用什么想法解决问题？ |
| 课程关系 | 它如何影响现代 LLM、后续章节或工程实践？ |

### 术语第一次出现必须解释

对 systems 和 resource accounting 词汇，第一次出现时必须就近解释，不能只放在表格里让读者猜。最低要求：

| 术语 | 首次解释必须包含 |
|---|---|
| sharding | 分片对象、按哪些设备分、减少了哪种重复存储 |
| fused kernel | 多个 GPU kernel 合并、减少 HBM 读写/launch overhead |
| collectives | all-reduce / reduce-scatter / all-gather / broadcast 等集合通信例子 |
| ZeRO | 在 data parallel 框架下切 optimizer/gradient/parameter state，说明 stage 越高越省显存但通信越多 |
| optimizer state | Adam/AdamW 的一阶动量 `m`、二阶动量 `v`，以及为什么显存常是参数的 2 倍 |
| activation checkpointing | 不存全部 activations，backward 时重算；区别于保存模型权重的 checkpoint |
| DRAM/SRAM/HBM | 全称、位置、速度/容量角色，说明计算单元通过片上缓存访问数据 |
| perplexity | `PPL = exp(H)` 或 `2^H`，直觉是每 token 等效候选数，并说明不是万能指标 |

### 背景概念优先用框图

当正文提到读者可能不熟的 foundational concept，例如 Shannon entropy、n-gram、perplexity、roofline、KV cache、ZeRO stage、speculative sampling，不应只给一段定义。优先使用以下结构：

1. 一张框图/流程图/对照表，把概念之间的关系画出来。
2. 一个 `knowledgebox` 解释直觉。
3. 一个 `importantbox` 给定义或关键公式。
4. 一个 `warningbox` 指出常见误解。

注意：项目通用规范中不鼓励复杂 TikZ，因为编译较慢；若需要框图，优先使用简单 TikZ、表格、或预生成图片。图必须服务理解，不做装饰。

## 质量检查脚本

快速检查单份讲义：

```bash
# 用法：bash check_quality.sh <tex-file>
f=$1
echo "=== Quality Check: $f ==="
pages=$(pdfinfo "${f%.tex}.pdf" 2>/dev/null | grep Pages | awk '{print $2}')
secs=$(grep -c '\\section{' "$f")
subs=$(grep -c '\\subsection{' "$f")
boxes=$(grep -c 'importantbox\|knowledgebox\|warningbox' "$f")
figs=$(grep -c '\\includegraphics' "$f")
summary=$(grep -c '本章小结\|总结与延伸' "$f")
echo "Pages: $pages | Sections: $secs | Subsections: $subs"
echo "Boxes: $boxes | Figures: $figs | Summaries: $summary"

# Verdict
ok=true
[ "$pages" -lt 8 ] && echo "⚠️  页数偏少 ($pages < 8)" && ok=false
[ "$boxes" -lt 5 ] && echo "⚠️  盒子太少 ($boxes < 5)" && ok=false
[ "$figs" -lt 3 ] && echo "⚠️  图片太少 ($figs < 3)" && ok=false
[ "$summary" -lt 2 ] && echo "⚠️  缺少小结或总结" && ok=false
$ok && echo "✅ 达标"
```

## 现有讲义质量概览

基于当前 238 份讲义的统计：

| 等级 | 数量 | 占比 | 典型系列 |
|------|------|------|----------|
| ⭐⭐⭐ 优秀 | ~43 | 18% | CS336, CS224N, CS231N |
| ⭐⭐ 达标 | ~94 | 39% | articles, interviews, 部分 talks |
| ⭐ 基础 | ~101 | 43% | CS25, Berkeley, agentic-rl, llm-architect |

**改进优先级**：agentic-rl (20份, avg 3p) > llm-architect (10份, avg 5p) > cs25 (40份, avg 5p) > berkeley (35份, avg 4p)

## PR 审核清单

审核他人提交的讲义时，按以下顺序检查：

1. **编译通过？** — xelatex 两次无报错
2. **结构完整？** — 封面、目录、小结、总结都有
3. **页数达标？** — 参照上表
4. **有教学元素？** — 盒子 ≥5、图 ≥3
5. **内容准确？** — 抽查 2-3 个技术点是否正确
6. **格式规范？** — 命名为 `<dirname>-notes.tex`，图片用 `[H]`

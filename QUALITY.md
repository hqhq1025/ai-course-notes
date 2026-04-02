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
- [ ] 每张图有脚注标注来源（slides 页码或视频时间区间）
- [ ] 公式用 `$$...$$` 展示，后跟符号说明
- [ ] 代码用 `lstlisting` 包裹并有 caption（如有代码内容）

### 内容质量

- [ ] 覆盖视频/文章中 **≥80%** 的核心知识点（不遗漏关键概念）
- [ ] 按教学逻辑重新组织（不照搬字幕/原文顺序）
- [ ] 跳过非教学内容（问候、闲聊、广告）
- [ ] 技术术语保留英文原文
- [ ] 无明显的事实错误或公式抄写错误

## 优秀标准（⭐⭐⭐）

在达标基础上，还满足：

- [ ] 高亮盒子 ≥10 个，分布均匀，每个携带具体教学信息
- [ ] 有拓展阅读（`\subsection{拓展阅读}`）引用相关论文/资源
- [ ] 总结与延伸包含：核心要点提炼 + 跨章节关联 + 开放问题
- [ ] 图片质量高（优先用 slides 截图而非视频帧）
- [ ] 有 worked example 或推导过程的逐步展开

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

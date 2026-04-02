# 贡献指南

欢迎为 AI Course Notes 做贡献！

## 🎯 贡献方式

### 1. 推荐新课程/演讲
在 [Issues](../../issues) 里提交，附上视频链接即可。

### 2. 自己生成讲义并提 PR

#### 环境准备
```bash
git clone https://github.com/hqhq1025/ai-course-notes.git
cd ai-course-notes

# 安装依赖
pip install openai-whisper yt-dlp
# 需要 XeLaTeX (texlive-xetex + texlive-lang-chinese)

# 把 skills 复制到 Claude Code
cp -r tools/skills/* ~/.claude/skills/
```

#### 生成讲义

**YouTube 视频：**
直接给 Claude Code 发 YouTube 链接，会自动触发 `youtube-render-pdf` skill。

**Bilibili 视频：**
1. 先准备 cookies 文件（需要 B 站登录态）
2. 给 Claude Code 发 Bilibili 链接，触发 `bilibili-render-pdf` skill

**批量处理：**
```bash
# 批量下载
bash tools/scripts/batch_download.sh cookies.txt output_dir/ BV1xxx BV2xxx

# 批量转录（支持多 GPU 并行）
CUDA_VISIBLE_DEVICES=0 python3.11 tools/scripts/batch_transcribe.py dir1/ dir2/
```

### 3. 改进现有讲义质量
- 补充遗漏的内容
- 修正翻译/术语错误
- 补充更多图表和 worked examples

## 📁 目录规范

```
<course>/<lectureXX>/
├── lectureXX-notes.tex    # LaTeX 源文件
├── lectureXX-notes.pdf    # 编译后 PDF
├── lectureXX.srt          # 字幕文件 (或 subs.en.srt)
├── cover.jpg              # 封面图
└── slides-images/         # slides 截图 (如有)
```

## 📝 讲义规范

- **语言**：中文，技术术语保留英文
- **模板**：使用 `tools/templates/notes-template.tex`
- **结构**：`\section` / `\subsection` 按教学逻辑组织
- **高亮盒子**：`importantbox`（核心概念）、`knowledgebox`（背景知识）、`warningbox`（常见误解）
- **每节结尾**：加 `\subsection{本章小结}`
- **文档结尾**：加 `\section{总结与延伸}`
- **编译**：`xelatex` 两次

## ⚠️ 注意事项

- 不要提交 `audio.*` 文件（已在 .gitignore）
- 不要提交 `bilibili_cookies.txt`
- 避免使用 TikZ 图（编译慢），用表格代替
- 表格中 `[` 开头需转义为 `{[}...{]}`

# 网页构建元数据

PDF 发布到 GitHub Release 等外部地址时，在课程目录添加 `published-pdfs.json`。
键是 PDF 相对课程目录的路径，值是已发布文件的 HTTP(S) URL：

```json
{
  "lecture01/lecture01-notes.pdf": "https://example.org/releases/lecture01-notes.pdf"
}
```

课程列表和单讲页优先使用该地址，因此构建不需要本地 PDF。
未列入映射的讲义仍使用仓库中已有 PDF 的地址。
没有映射且没有本地 PDF 时，页面不显示 PDF 链接。

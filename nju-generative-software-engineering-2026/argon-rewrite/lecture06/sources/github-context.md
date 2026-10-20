# L06 GitHub 证据摘记：二维码生成器的分层与 API

核查日期：2026-10-20（UTC）。官方课件 `slides6.html` 的第 28 页直接引用 Nayuki，作为独立实现核验的例子。课件建议可以用该库或解码器核验，但没有由此证明教师实际运行或改造过该库。它也不是课堂 Excel 工具的源码。

## 来源与版本

- [官方课件](https://jyywiki.cn/GSE/2026/slides6.html)第 28 页；本地快照 `slides.json` 保存该页的引用和验证建议。
- 仓库：[nayuki/QR-Code-generator](https://github.com/nayuki/QR-Code-generator)。
- 固定提交：`3c6d0b3cefb4e049dc337e82237c9644399716a8`；提交时间：`2026-08-31T19:36:34Z`。
- [固定项目说明](https://github.com/nayuki/QR-Code-generator/blob/3c6d0b3cefb4e049dc337e82237c9644399716a8/Readme.markdown)。
- [固定 Python 实现](https://github.com/nayuki/QR-Code-generator/blob/3c6d0b3cefb4e049dc337e82237c9644399716a8/python/qrcodegen.py)。
- [作者的设计说明](https://www.nayuki.io/page/qr-code-generator-library)为在线延伸入口，未固定页面版本。

## API 与计算分层

库输出二维码的模块矩阵，而非直接把图像渲染作为唯一接口。模块是二维码的一格明暗单元；`get_module(x, y)` 读取格子，左上角为坐标原点，越界返回浅色。README 的图像示例另用演示程序中的 `toImage` 生成图片。

| 层次 | 已核实接口或步骤 | 与课程的关系 |
|---|---|---|
| 文本与字节入口 | `QrCode.encode_text`、`QrCode.encode_binary` | 分离用户数据与后续符号构造。文本入口与原始字节入口有不同编码语义。 |
| 分段与参数 | `QrSegment`、`QrCode.encode_segments` | 可固定版本范围、纠错等级、掩码和分段，明确哪些选择属于编码规格。 |
| 纠错与布局 | `_add_ecc_and_interleave`、`_draw_codewords` | 先构造数据及纠错码字，再把位串放入模块矩阵。 |
| 掩码 | `_apply_mask` | 掩码施加于码字模块，保留功能模块；实现会比较候选掩码。 |
| 输出读取 | `get_module` | 算法结果与 PNG、SVG 或工作表等表现形式可以分开。 |

`encode_segments` 接受 `minversion`、`maxversion`、`mask`、`boostecl`。`mask=-1` 表示自动选择，0 到 7 表示指定掩码。默认允许在不增大版本的条件下提高纠错等级。因此，传入的最低纠错要求不一定等于最终采用的等级。

固定 Python 实现的 `make_segments` 检查整段文本。空字符串得到空分段，全数字使用数字模式，全字母数字使用对应模式，否则使用 UTF-8 字节模式。不能把这一函数宣传成任意混合文本的最优分段器。README 把更高级的最优模式切换列为 Java 的可选特性。

## 能支持与不能支持的结论

这份实现提供了“数据编码、纠错、模块布局、输出读取可以分层”的具体证据，可辅助解释 L06 的 IR 和后端设计。它没有提供课堂所设想的符号计算图或 Excel 后端；不能把库的函数层次直接称为已经实现的 Excel 编译器。

与参考库逐格比较之前，需要固定版本、纠错等级、分段与掩码。不同的合规选择可能产生不同矩阵。独立解码器检查还原文本，回答的是另一项问题：图案能否携带预期内容。若 Python 与 Excel 共用同一算法，二者一致仍可能保留共同错误。

本轮只阅读 README、API 注释及表中列出的实现，没有运行二维码生成、实际 Excel 重算或解码测试。不要把上述验证建议写成已通过的实验。

## 版权与归属

项目说明记载 `Copyright © 2026 Project Nayuki`，许可为 MIT License，完整许可位于固定版本 [Readme.markdown 的 License 部分](https://github.com/nayuki/QR-Code-generator/blob/3c6d0b3cefb4e049dc337e82237c9644399716a8/Readme.markdown#license)。本摘记转述 API 与设计，只保留必要的代码标识，没有复制库的完整实现。

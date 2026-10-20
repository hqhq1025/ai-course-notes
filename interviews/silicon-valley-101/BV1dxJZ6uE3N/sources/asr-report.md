# 完整音频转写记录

本期音频已完整转写。原始结果存于 `transcript.raw.srt`、`transcript.raw.txt`、`transcript.raw.json`，未覆盖或删除原始识别内容。

| 项目 | 实测结果 |
|---|---|
| 输入 | `audio.m4a`，4795.563 秒，48 kHz AAC |
| 模型 | mobiuslabsgmbh/faster-whisper-large-v3-turbo |
| 模型快照 | `0a363e9161cbc7ed1431c9597a8ceaf0c4f78fcf`，复用本机缓存 |
| 程序 | 仓库 `tools/scripts/transcribe_faster_whisper.py` |
| 环境 | 临时 venv；faster-whisper 1.2.1、CTranslate2 4.8.3、PyAV 16.1.0 |
| 后端 | CUDA、float16、beam size 5、VAD 开启；CTranslate2 检测到 2 个 CUDA 设备 |
| 运行耗时 | 155.12 秒 |
| 输出 | 2740 条片段，28442 个文字字符 |
| 首末语音 | 00:00:00.000 到 01:19:50.420 |
| 时间检查 | 无倒置区间；最大相邻片段空隙为 0.18 秒 |
| 末尾 | 主持人结束语后剩余约 5.14 秒，未识别出语音 |

每条片段的起止秒数保留在 JSON，SRT 另含毫秒级时间戳。TXT 保留秒级阅读时间区间。没有把字幕按 14 字重切，没有删除宣传段或口语段；正文可根据内容范围另行省略。

PyAV 19 与当前 faster-whisper 调用不兼容，临时环境固定为 PyAV 16.1.0。宿主默认 CUDA 13，临时环境另提供 CTranslate2 所需 CUDA 12 的 cuBLAS/cuDNN 库，通过该次进程的 `LD_LIBRARY_PATH` 加载。未修改全局 Python 或系统 CUDA。

## 原始媒体校验

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `audio.m4a` | 78060135 | `d2986aa08105ed63cdab09e9ffac5b1f434f6410dc0f798743a615cdaebe786a` |
| `video.mp4` | 59413293 | `f2542db69974ba56888012a0163bc6d9b10891d4fd3111da7367f06cc08dda3f` |

识别结果经过时间轴检查和早段专名抽查；专名核对见 `terminology-check.md`。完整转写不等于每个识别字词均已人工核对，正文仍需按语境精读。

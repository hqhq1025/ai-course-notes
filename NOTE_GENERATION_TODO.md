# Note Generation Todo

> Maintained by Codex. Last updated: 2026-05-04.

## Status Legend
- `todo`: not started
- `ready`: source assets are available locally
- `blocked`: missing credentials, downloads, subtitles, or transcription environment
- `done`: TeX and PDF generated and verified

## High Priority

| Status | Series | Item | Source | Local Target | Notes |
|---|---|---|---|---|---|
| done | CS336 Spring 2026 | Lecture 01: Overview and Tokenization | https://cs336.stanford.edu/ + `lecture01-slides.py` | `cs336-2026/lecture01/` | Quality-upgraded long-form note: 28-page PDF, 11 figures, 22 teaching boxes, XeLaTeX verified. |
| done | CS336 Spring 2026 | Lecture 02: Resource Accounting | https://cs336.stanford.edu/ + `lecture02-slides.py` | `cs336-2026/lecture02/` | Long-form note: 26-page PDF, 11 figures, 22 teaching boxes, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 03: LM Architecture and Hyperparameters | `lecture03-slides.pdf` | `cs336-2026/lecture03/` | Deep long-form note: 35-page PDF, 33 figures, 24 teaching boxes, code snippets, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 04: Attention Alternatives and Mixture of Experts | `lecture04-slides.pdf` | `cs336-2026/lecture04/` | Long-form note: 38-page PDF, 41 figures, 21 teaching boxes, code snippets, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 05: GPUs | `lecture05-slides.pdf` | `cs336-2026/lecture05/` | Long-form note: 31-page PDF, 36 figures, 21 teaching boxes, code snippets, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 06: Kernels, Profiling, and Triton | `lecture06-slides.py` | `cs336-2026/lecture06/` | Long-form note: 31-page PDF, 12 figures, 31 teaching boxes, Triton kernel code, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 07: Parallelism | `lecture07-slides.py` | `cs336-2026/lecture07/` | Long-form note: 25-page PDF, 14 figures, 30 teaching boxes, distributed PyTorch code snippets, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 08: Parallelism Basics | `lecture08-slides.pdf` | `cs336-2026/lecture08/` | Long-form note: 41-page PDF, 51 figures, 23 teaching boxes, ZeRO/FSDP and 3D/4D parallelism synthesis, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 09: Scaling Laws Basics | `lecture09-slides.pdf` | `cs336-2026/lecture09/` | Long-form note: 36-page PDF, 44 figures, 23 teaching boxes, scaling-law fitting/code snippets, XeLaTeX and quality script verified. |
| done | CS336 Spring 2026 | Lecture 10: Inference | `lecture10-slides.py` | `cs336-2026/lecture10/` | Long-form note: 30-page PDF, 29 figures, 41 teaching boxes, inference/KV-cache/systems synthesis, XeLaTeX and quality script verified. |
| blocked | CS153 Spring 2026 | 5 public videos | `PL2aDf5-VARtBwz1kz5FsuSZXOig2U6aJI` | `cs153-spring2026/lectureXX/` | YouTube currently requires cookies/sign-in for yt-dlp subtitle and media access. |
| blocked | CS25 V6 | First 3 public recordings | `PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM` | `cs25/lecture42+` or `cs25-v6/lectureXX/` | YouTube currently requires cookies/sign-in for yt-dlp subtitle and media access. |
| done | Modern Agent | 17 Codex Plan Mode and update_plan | `BV1NdDtBjEg7` | `modern-agent/lecture17/` | Downloaded via public playurl API, transcribed with faster-whisper large-v3 on A100, TeX/PDF compiled. |
| blocked | Agentic RL | 16 Docker sandbox and Jupyter Kernel CI env | `BV15JdEBmEh9` | `agentic-rl/lecture16/` | Public playurl API only returns a ~5 minute preview. Needs valid Bilibili cookies/full access before transcription and PDF generation. |

## Environment Notes
- 4 x NVIDIA A100 80GB PCIe are visible under `/proc/driver/nvidia/gpus`.
- `nvidia-smi` hangs on this host; use ctranslate2/faster-whisper probes instead.
- `faster-whisper` is installed and large-v3 is cached.
- OpenAI Whisper and PyTorch are not installed in the active Hermes Python venv.
- `yt-dlp` version: 2026.03.17.

## Next Actions
1. Try `yt-dlp --cookies-from-browser` for YouTube/Bilibili if a browser profile is accessible.
2. If cookies work, download audio, covers, and subtitles where available.
3. For no-subtitle videos, transcribe with `faster-whisper-large-v3` on A100.
4. Generate and compile one note at a time; update this file after each verified PDF.

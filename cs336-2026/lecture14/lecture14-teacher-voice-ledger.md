# Lecture 14 Teacher-Voice Ledger

Primary sources: `transcript_timed.txt` and `lecture14-slides.py`. Timestamps refer to the public lecture transcript; executable `text(...)` nodes provide the slide-aligned outline.

| Time / source node | Spoken point | Why it matters | Where it appears in the note |
|---|---|---|---|
| `00:00:12--00:01:14`, `main` | Data does not fall from the sky; Data II follows the pipeline through transformation, filtering, deduplication, mixing, and synthetic post-training data. | Gives the lecture a single production-pipeline spine and connects it to Data I. | `本讲主线：数据不是被“收集”出来的，而是被“加工”出来的`. |
| `00:01:17--00:04:19`, `transformation` | Raw data is HTML, PDF, or repositories rather than clean text; HTML linearization is inherently lossy; rule-based parsers are fast but imperfect. | Explains why parser accuracy is a model-quality variable rather than clerical preprocessing. | `Transformation`, `课堂提醒：转换阶段看似“只是工程”`. |
| `00:04:19--00:06:45`, `transformation` | FinePDFs must recrawl truncated PDFs, render or OCR scanned pages, and recover structure that PDF layout does not expose semantically. | Motivates the PDF object-to-layout figure and the need for layout-aware QA. | `PDF 与代码仓库`, FinePDFs figure and `读图：PDF 不是“带换行的纯文本”`. |
| `00:06:56--00:08:54`, `filtering` | Filtering finds a small subset of raw data resembling target data; language, quality, and toxicity are distinct goals; the filter must generalize and run over enormous pools. | Prevents readers from treating one score as a universal definition of quality. | `Filtering：把“好数据”写成一个可计算的目标`. |
| `00:23:10--00:27:14`, `deduplication` | Exact mirrors/forks and near duplicates are both abundant; licenses, templates, formatting changes, and a C4 product description repeated 61,000 times show why concrete inspection matters. | Grounds fuzzy dedup in real failure modes and connects duplication to wasted FLOPs, memorization, and contamination. | `Deduplication`, near-duplicate figure and its read-figure box. |
| `locality_sensitive_hashing` | MinHash estimates Jaccard; LSH uses banding to generate candidate pairs, trading recall against candidate volume rather than returning exact truth. | Clarifies the role of the S curves and why `b,r` require calibration. | `MinHash 与 LSH`, two LSH figures and `读图：LSH 调的是候选预算`. |
| `00:55:32--00:57:10`, `data_mixing` | A mixture can silently repeat a small high-quality source dozens of epochs; always compute the realized epoch count. | Turns mixture weights into a resource and overfitting audit rather than a percentage table. | `Data Mixing`, `课堂提示：把 mixture weight 换算成实际 epochs`. |
| `01:06:53--01:10:17`, `data_mixing` | Small-scale mixture optimization can favor high-quality data before epoching appears; cap or simulate epoching so proxy scale resembles full scale. | Exposes the central small-to-large transfer failure mode of regression-based mixing. | `RegMix`, `Proxy mismatch`, and the 100B-token worked example. |
| `01:16:33--01:17:33`, `post_training_data` | Better benchmark models are not necessarily better teachers; multiple generations helped, while simple answer filtering did not. | Separates teacher usefulness from teacher capability and motivates student-outcome evaluation. | `OpenThoughts`, `课堂提示：更强的模型不一定是更好的 teacher`. |
| `01:19:27--01:21:35`, `post_training_data` | Code environments are an infrastructure nightmare; strong models can solve many PR tasks without execution feedback, suggesting internal code semantics, but filtering and later execution-based data remain necessary. | Distinguishes candidate generation from correctness verification. | `SWE-zero`, `课堂提示：没有 execution feedback 仍能解题意味着什么`. |
| `01:23:50--01:24:31`, lecture summary | Real data work is grungy, domain-specific, and requires looking at concrete examples. | Preserves the instructor's final warning against replacing data inspection with abstract metrics. | Opening `\teachervoice` and final audit loop. |

## Attribution Rule

- `课堂提示` and `\teachervoice{...}` are reserved for claims directly supported by the transcript or executable source.
- `讲义提醒` marks engineering synthesis added by the notes, including high-risk slice audits, environment-as-label framing, and heterogeneous-verifier recommendations.

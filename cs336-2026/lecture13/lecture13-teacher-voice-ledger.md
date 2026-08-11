# Lecture 13 Teacher-Voice Ledger

Source: `lecture13-slides.py`, the official executable lecture source. The `text(...)` nodes are treated as the closest available record of the instructor's spoken teaching flow.

| Source node / function | Spoken point | Why it matters | Where it appears in the note |
|---|---|---|---|
| `main`, lines 40--45 | Data does not fall from the sky; live service becomes raw data and then processed data; the pipeline is heuristic and has legal/ethical constraints. | Establishes the lecture's production-pipeline framing rather than treating web text as a ready-made dataset. | `Summary：Lecture 13: Data I 的核心主线`, especially `课堂提示：Data does not fall from the sky`. |
| `motivation`, lines 49--63 | Architecture and training procedures are disclosed more often than data; secrecy is driven by competition and copyright liability; curation remains labor intensive. | Explains why data is both a scientific confounder and a competitive asset. | `为什么数据最重要`; the source-backed claim is separated from the note's additional audit recommendation. |
| `raw_sources`, lines 103--148 | “Trained on the entire Internet” is misleading because live services have technical restrictions, site-level policies, and legal limits. | Prevents readers from collapsing accessibility, permission, extraction, and training suitability into one claim. | `Raw sources：互联网不是一个可直接训练的数据集`, `课堂提示：不要把“整个互联网”当作可训练集合`. |
| `copyright`, lines 152--217 | Intellectual-property law is meant to incentivize creation; most online expression is copyrighted; license and fair use are distinct routes; “transformative” is not a statutory checkbox. | Gives the legal section its motivation and avoids the common mistake that public access implies permission. | `Intellectual property law：Licenses、fair use 与 Lawsuits`, especially `课堂提示：License 可以理解为“不起诉的承诺”`. |
| `common_crawl`, lines 221--261 | A crawler needs selection, politeness, and revisit policies; WARC and WET are different; HTML-to-text conversion is lossy and affects model accuracy. | Connects crawling decisions and extraction tools to the distribution ultimately seen by the model. | `Common Crawl：web-scale raw source`, including the crawler and WET figure explanations. |
| `wikipedia`, lines 282--294 | Wikipedia is high quality but periodic dumps create a timing surface for targeted poisoning attacks. | Shows why provenance, snapshot time, and anomaly detection remain necessary even for trusted sources. | `Specialized sources：Wikipedia、GitHub、arXiv`, `课堂提示：高质量来源也可能被投毒`. |
| `webtext` / `ccnet`, lines 354--375 | WebText uses Reddit karma as a quality surrogate; CCNet combines deduplication, language ID, and Wikipedia-like perplexity filtering. | Makes explicit that dataset recipes encode proxy choices rather than neutral quality measurement. | `经典数据集：BERT、WebText、CCNet、C4`, `课堂提示：Reddit karma 只是 quality surrogate`. |
| `dolma` / `dclm`, lines 523--555 | Dolma avoids model-based quality filtering to reduce bias; DCLM trains a classifier from named positive and negative datasets. | Encourages readers to inspect classifier training data before accepting a quality score as objective. | `现代 filtering：Dolma、DCLM、Nemotron-CC`, `课堂提示：正负例已经在定义“质量”`. |
| `the_stack` / `commonpile` | Code corpora must handle permissive licenses, duplicates, metadata, and takedown or consent signals; permissive-only training still has tradeoffs. | Links licensing policy to concrete data-pipeline fields and downstream capability coverage. | `Code data：The Stack 与 Stack v2` and `CommonPile：只用 permissively licensed data 可行吗`. |

## Attribution Rule

- `课堂提示` is reserved for points directly supported by executable source narration.
- `讲义提醒` marks engineering synthesis added by the notes, such as held-out filter audits or causal-confound checks.
- The ledger records meaning and placement rather than pretending the executable source is a verbatim classroom transcript.

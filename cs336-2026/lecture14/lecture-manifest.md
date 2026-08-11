# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture14`

## Files

- `cover.jpg`
- `lecture-manifest.md`
- `lecture14-blueprint.md`
- `lecture14-coverage.md`
- `lecture14-manifest.md`
- `lecture14-notes.pdf`
- `lecture14-notes.tex`
- `lecture14-slides.py`
- `lecture14.en-orig.srt`
- `lecture14.en.srt`
- `lecture14.info.json`
- `lecture14.jpg`
- `lecture_14.py`
- `metadata.json`
- `transcript_clean.txt`
- `transcript_timed.txt`

## Local Visual Assets

- `images/data-filtering-scale.png`
- `images/data-mixing-methods.png`
- `images/dclm-wet.png`
- `images/marin-token-viewer.png`
- `images/openthoughts-pipeline.png`
- `images/openthoughts-sources.png`
- `images/raw-target-schema.png`
- `images/regmix.png`
- `images/swe-rebench.png`
- `images/swe-smith.png`
- `images/swezero-noexec.png`
- `images/swezero-prompt.png`
- `images/swezero-results.png`
- `official-images/data-filtering-scale.png`
- `official-images/data-mixing-methods.png`
- `official-images/dclm-wet.png`
- `official-images/marin-token-viewer.png`
- `official-images/openthoughts-pipeline.png`
- `official-images/openthoughts-sources.png`
- `official-images/raw-target-schema.png`
- `official-images/regmix.png`
- `official-images/swe-rebench.png`
- `official-images/swe-smith.png`
- `official-images/swezero-noexec.png`
- `official-images/swezero-prompt.png`
- `official-images/swezero-results.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | section | yes | `lecture14-slides.py:main` | Lecture 14: Data II |
| py-002 | text | optional | `lecture14-slides.py:main` | Last lecture: |
| py-003 | text | optional | `lecture14-slides.py:main` | - Live service (e.g., GitHub) → dump/crawl (e.g., GitHub Archive) → processed data (e.g., The... |
| py-004 | text | optional | `lecture14-slides.py:main` | - Considerations: terms of service, copyright (licenses or fair use) |
| py-005 | text | optional | `lecture14-slides.py:main` | This lecture: |
| py-006 | text | optional | `lecture14-slides.py:main` | - Data pipeline: transformation, filtering, deduplication, mixing |
| py-007 | text | optional | `lecture14-slides.py:main` | - Mid-training + SFT: synthetic data |
| py-008 | text | optional | `lecture14-slides.py:main` | Summary: |
| py-009 | text | optional | `lecture14-slides.py:main` | - Filtering: train classifier (language id, quality, toxicity) for what good looks like |
| py-010 | text | optional | `lecture14-slides.py:main` | - Deduplication: hashing scales to large datasets for fuzzy matching |
| py-011 | text | optional | `lecture14-slides.py:main` | - Mixing: try mixtures at small scale, extrapolate to optimal mixture and large scale |
| py-012 | text | optional | `lecture14-slides.py:main` | - Applications: language identification, quality filtering, toxicity filtering |
| py-013 | text | optional | `lecture14-slides.py:main` | - Post-training data: looks like evaluations, use of synthetic data |
| py-014 | text | optional | `lecture14-slides.py:main` | - A lot of data work is domain-specific, looking at examples, etc. |
| py-015 | text | optional | `lecture14-slides.py:transformation` | Raw data does not come as text. |
| py-016 | text | optional | `lecture14-slides.py:transformation` | It is HTML, PDF (arxiv), or directories (code repositories). |
| py-017 | text | optional | `lecture14-slides.py:transformation` | HTML to text (main one): |
| py-018 | text | optional | `lecture14-slides.py:transformation` | - Remove boilerplate (e.g., navigation, ads) and extract content |
| py-019 | text | optional | `lecture14-slides.py:transformation` | - What about images, tables, etc.? |
| py-020 | text | optional | `lecture14-slides.py:transformation` | - Inherently lossy (need to linearize) |
| py-021 | text | optional | `lecture14-slides.py:transformation` | - Tools (rule-based): trafilatura, resiliparse, jusText, lynx, etc. |
| py-022 | text | optional | `lecture14-slides.py:transformation` | - Accuracy matters: |
| py-023 | figure | yes | `lecture14-slides.py:transformation` | images/dclm-wet.png |
| py-024 | text | optional | `lecture14-slides.py:transformation` | FinePDFs |
| py-025 | figure | yes | `lecture14-slides.py:transformation` | images/finepdfs-pdf-structure.png |
| py-026 | text | optional | `lecture14-slides.py:transformation` | - Source: Common Crawl |
| py-027 | text | optional | `lecture14-slides.py:transformation` | - Recrawl truncated PDFs (since they are big) |
| py-028 | text | optional | `lecture14-slides.py:transformation` | - OCR (RolmOCR) using a VLM or Docling (make these run fast) |
| py-029 | text | optional | `lecture14-slides.py:transformation` | - Lots of cleanup and filtering |
| py-030 | text | optional | `lecture14-slides.py:transformation` | - A lot of layout information is missing |
| py-031 | text | optional | `lecture14-slides.py:filtering` | Algorithmic building block: |
| py-032 | text | optional | `lecture14-slides.py:filtering` | - Given some **target data** T and lots of **raw data** R, find subset T' of R similar to T. |
| py-033 | figure | yes | `lecture14-slides.py:filtering` | images/raw-target-schema.png |
| py-034 | text | optional | `lecture14-slides.py:filtering` | Applications: |
| py-035 | text | optional | `lecture14-slides.py:filtering` | - Language identification (English versus rest) |
| py-036 | text | optional | `lecture14-slides.py:filtering` | - Quality filtering (high quality versus low quality) |
| py-037 | text | optional | `lecture14-slides.py:filtering` | - Toxicity filtering (non-toxic versus toxic) |
| py-038 | text | optional | `lecture14-slides.py:filtering` | Desiderata for filtering algorithm: |
| py-039 | text | optional | `lecture14-slides.py:filtering` | - Generalize from the target data (want T and T' to be different) |
| py-040 | text | optional | `lecture14-slides.py:filtering` | - Extremely fast (have to run it on R, which is huge) |
| py-041 | text | optional | `lecture14-slides.py:filtering` | Survey paper on data selection |
| py-042 | text | optional | `lecture14-slides.py:filtering` | General framework: Given target T and raw R, find subset of R similar to T |
| py-043 | text | optional | `lecture14-slides.py:filtering` | 1. Estimate some model based on R and T and derive a scoring function |
| py-044 | text | optional | `lecture14-slides.py:filtering` | 2. Keep examples in R based on their score |
| py-045 | text | optional | `lecture14-slides.py:filtering` | Types of classifiers: |
| py-046 | text | optional | `lecture14-slides.py:filtering` | - Generative model of T (KenLM): score(x) = p_T(x) |
| py-047 | text | optional | `lecture14-slides.py:filtering` | - Simple classifier (fastText): score(x) = p(T \| x) |
| py-048 | text | optional | `lecture14-slides.py:filtering` | To use: keep examples x with score(x) >= threshold (stochastically) |
| py-049 | text | optional | `lecture14-slides.py:filtering` | Model-based filtering? |
| py-050 | text | optional | `lecture14-slides.py:filtering` | - Some deliberately do not use model-based filtering (C4, Gopher, RefinedWeb, FineWeb, Dolma) |
| py-051 | text | optional | `lecture14-slides.py:filtering` | - Some use model-based filtering (GPT-3, LLaMA, DCLM) [becoming the norm] |
| py-052 | text | optional | `lecture14-slides.py:filtering` | Language identification: |
| py-053 | text | optional | `lecture14-slides.py:filtering` | - Goal: find text of a specific language (e.g., English) |
| py-054 | text | optional | `lecture14-slides.py:filtering` | - fastText language identification |
| py-055 | text | optional | `lecture14-slides.py:filtering` | - Off-the-shelf classifier |
| py-056 | text | optional | `lecture14-slides.py:filtering` | - Supports 176 languages |
| py-057 | text | optional | `lecture14-slides.py:filtering` | - Trained on multilingual sites: Wikipedia, Tatoeba (translation site) and SETimes (Southeast... |
| py-058 | text | optional | `lecture14-slides.py:filtering` | - Dolma keeps pages with p(English) >= 0.5 |
| py-059 | text | optional | `lecture14-slides.py:filtering` | OpenMathText |
| py-060 | text | optional | `lecture14-slides.py:filtering` | - Goal: curate large corpus of mathematical text from CommonCrawl |
| py-061 | text | optional | `lecture14-slides.py:filtering` | - Use rules to filter (e.g., contains latex commands) |
| py-062 | text | optional | `lecture14-slides.py:filtering` | - KenLM trained on ProofPile, keep if perplexity < 15000 |
| py-063 | text | optional | `lecture14-slides.py:filtering` | - Trained fastText classifier to predict mathematical writing, threshold is 0.17 if math, 0.8... |
| py-064 | text | optional | `lecture14-slides.py:filtering` | - Result: produced 14.7B tokens, used to train 1.4B models that do better than models trained... |
| py-065 | text | optional | `lecture14-slides.py:filtering` | GPT-3 |
| py-066 | text | optional | `lecture14-slides.py:filtering` | - Positives: samples from {Wikipedia, WebText2, Books1, Books2} |
| py-067 | text | optional | `lecture14-slides.py:filtering` | - Negatives: samples from CommonCrawl |
| py-068 | text | optional | `lecture14-slides.py:filtering` | Train linear classifier based on word features |
| py-069 | text | optional | `lecture14-slides.py:filtering` | Keep documents stochastically based on score |
| py-070 | text | optional | `lecture14-slides.py:filtering` | LLaMA/RedPajama |
| py-071 | text | optional | `lecture14-slides.py:filtering` | - Positives: samples from pages **referenced** by Wikipedia |
| py-072 | text | optional | `lecture14-slides.py:filtering` | - Negatives: samples from CommonCrawl |
| py-073 | text | optional | `lecture14-slides.py:filtering` | - Keep documents that are classified positive |
| py-074 | text | optional | `lecture14-slides.py:filtering` | phi-1 |
| py-075 | text | optional | `lecture14-slides.py:filtering` | - Philosophy: really high quality data (textbooks) to train a small model (1.5B) |
| py-076 | text | optional | `lecture14-slides.py:filtering` | - Includes synthetic data from GPT 3.5 (later: GPT-4) and filtered data |
| py-077 | text | optional | `lecture14-slides.py:filtering` | - Train random forest classifier on T using output embedding from pretrained codegen model |
| py-078 | text | optional | `lecture14-slides.py:filtering` | - Select data from R that is classified positive by the classifier |
| py-079 | text | optional | `lecture14-slides.py:filtering` | Result on [HumanEval](https://huggingface.co/datasets/openai_humaneval): |
| py-080 | text | optional | `lecture14-slides.py:filtering` | - Train 1.3B LM on Python subset of The Stack (performance: 12.19% after 96K steps) |
| py-081 | text | optional | `lecture14-slides.py:filtering` | - Train 1.3B LM on new filtered subset (performance: 17.68% after 36K steps) - better! |
| py-082 | text | optional | `lecture14-slides.py:filtering` | Toxicity filtering in Dolma |
| py-083 | text | optional | `lecture14-slides.py:filtering` | - Dataset: Jigsaw Toxic Comments dataset (2018) |
| py-084 | text | optional | `lecture14-slides.py:filtering` | - Project goal: help people have better discussions online |
| py-085 | text | optional | `lecture14-slides.py:filtering` | - Data: comments on Wikipedia talk page annotated with {toxic, severe_toxic, obscene, threat,... |
| py-086 | text | optional | `lecture14-slides.py:filtering` | Scale-dependent effects of filtering: |
| py-087 | text | optional | `lecture14-slides.py:filtering` | - No single optimal threshold for filtering |
| py-088 | text | optional | `lecture14-slides.py:filtering` | - If training for longer, want more (lower quality) data |
| py-089 | text | optional | `lecture14-slides.py:filtering` | - If training for shorter, want less (higher quality) data |
| py-090 | figure | yes | `lecture14-slides.py:filtering` | images/data-filtering-scale.png |
| py-091 | text | optional | `lecture14-slides.py:filtering` | Summary: |
| py-092 | text | optional | `lecture14-slides.py:filtering` | - Filtering is critical for building a good model |
| py-093 | text | optional | `lecture14-slides.py:filtering` | - Recipe: define target data (what good looks like), extrapolate to raw data |
| py-094 | text | optional | `lecture14-slides.py:deduplication` | Two types of duplicates: |
| py-095 | text | optional | `lecture14-slides.py:deduplication` | - Exact duplicates (mirror sites, GitHub forks) |
| py-096 | text | optional | `lecture14-slides.py:deduplication` | - Near duplicates: same text differing by a few tokens |
| py-097 | text | optional | `lecture14-slides.py:deduplication` | Examples of near duplicates: |
| py-098 | text | optional | `lecture14-slides.py:deduplication` | - Terms of service and licenses |
| py-099 | figure | yes | `lecture14-slides.py:deduplication` | images/near-duplicate-examples.png |
| py-100 | text | optional | `lecture14-slides.py:deduplication` | - Formulaic writing (copy/pasted or generated from a template) |
| py-101 | text | optional | `lecture14-slides.py:deduplication` | - Minor formatting differences in copy/pasting |
| py-102 | text | optional | `lecture14-slides.py:deduplication` | Product description repeated 61,036 times in C4 |
| py-103 | text | optional | `lecture14-slides.py:deduplication` | '“by combining fantastic ideas, interesting arrangements, and follow the current trends in th... |
| py-104 | text | optional | `lecture14-slides.py:deduplication` | Deduplication training data makes language models better |
| py-105 | text | optional | `lecture14-slides.py:deduplication` | - Train more efficiently (because have fewer tokens) |
| py-106 | text | optional | `lecture14-slides.py:deduplication` | - Avoid memorization (can mitigate copyright, privacy concerns) |
| py-107 | text | optional | `lecture14-slides.py:deduplication` | Design space: |
| py-108 | text | optional | `lecture14-slides.py:deduplication` | 1. What is an item (sentence, paragraph, document)? |
| py-109 | text | optional | `lecture14-slides.py:deduplication` | 2. How to match (exact match, existence of common subitem, fraction of common subitems)? |
| py-110 | text | optional | `lecture14-slides.py:deduplication` | 3. What action to take (remove all, remove all but one)? |
| py-111 | text | optional | `lecture14-slides.py:deduplication` | Key challenge: |
| py-112 | text | optional | `lecture14-slides.py:deduplication` | - Deduplication is fundamentally about comparing items to other items |
| py-113 | text | optional | `lecture14-slides.py:deduplication` | - Need linear time algorithms to scale |
| py-114 | text | optional | `lecture14-slides.py:hash_functions` | - Hash function h maps item to a hash value (integer or string) |
| py-115 | text | optional | `lecture14-slides.py:hash_functions` | - Hash value much smaller than item |
| py-116 | text | optional | `lecture14-slides.py:hash_functions` | - Hash collision: h(x) = h(y) for x ≠ y |
| py-117 | text | optional | `lecture14-slides.py:hash_functions` | Tradeoff between efficiency and collision resistance |
| py-118 | text | optional | `lecture14-slides.py:hash_functions` | - Cryptographic hash functions (SHA-256): collision resistant, slow (used in bitcoin) |
| py-119 | text | optional | `lecture14-slides.py:hash_functions` | - DJB2, MurmurHash, CityHash: not collision resistant, fast (used for hash tables) |
| py-120 | text | optional | `lecture14-slides.py:hash_functions` | We will use MurmurHash: |
| py-121 | text | optional | `lecture14-slides.py:exact_deduplication` | **Simple example** |
| py-122 | text | optional | `lecture14-slides.py:exact_deduplication` | 1. Item: string |
| py-123 | text | optional | `lecture14-slides.py:exact_deduplication` | 2. How to match: exact match |
| py-124 | text | optional | `lecture14-slides.py:exact_deduplication` | 3. Action: remove all but one |
| py-125 | text | optional | `lecture14-slides.py:exact_deduplication` | - Pro: simple, clear semantics, high precision |
| py-126 | text | optional | `lecture14-slides.py:exact_deduplication` | - Con: does not deduplicate near duplicates |
| py-127 | text | optional | `lecture14-slides.py:exact_deduplication` | - This code is written in a MapReduce way, can easily parallelize and scale |
| py-128 | text | optional | `lecture14-slides.py:exact_deduplication` | **C4** |
| py-129 | text | optional | `lecture14-slides.py:exact_deduplication` | 1. Item: 3-sentence spans |
| py-130 | text | optional | `lecture14-slides.py:exact_deduplication` | 2. How to match: use exact match |
| py-131 | text | optional | `lecture14-slides.py:exact_deduplication` | 3. Action: remove all but one |
| py-132 | text | optional | `lecture14-slides.py:exact_deduplication` | Warning: when a 3-sentence span is removed from the middle of a document, the resulting docum... |
| py-133 | text | optional | `lecture14-slides.py:jaccard_minhash` | Let's now look at approximate set membership. |
| py-134 | text | optional | `lecture14-slides.py:jaccard_minhash` | First we need a similarity measure. |
| py-135 | section | yes | `lecture14-slides.py:jaccard_minhash` | Jaccard similarity |
| py-136 | text | optional | `lecture14-slides.py:jaccard_minhash` | Definition: Jaccard(A, B) = \|A intersect B\| / \|A union B\| |
| py-137 | text | optional | `lecture14-slides.py:jaccard_minhash` | Definition: two documents are **near duplicates** if their Jaccard similarity >= threshold |
| py-138 | text | optional | `lecture14-slides.py:jaccard_minhash` | Algorithmic challenge: find near duplicates in linear time |
| py-139 | section | yes | `lecture14-slides.py:jaccard_minhash` | MinHash |
| py-140 | text | optional | `lecture14-slides.py:jaccard_minhash` | MinHash: a random hash function h so that Pr[h(A) = h(B)] = Jaccard(A, B) |
| py-141 | text | optional | `lecture14-slides.py:jaccard_minhash` | Normally, you want different items to hash to different hashes |
| py-142 | text | optional | `lecture14-slides.py:jaccard_minhash` | ...but here, you want collision probability to depend on similarity |
| py-143 | text | optional | `lecture14-slides.py:jaccard_minhash` | Characteristic matrix representation: |
| py-144 | text | optional | `lecture14-slides.py:jaccard_minhash` | item \| A \| B |
| py-145 | text | optional | `lecture14-slides.py:jaccard_minhash` | 1 \| 1 \| 1 |
| py-146 | text | optional | `lecture14-slides.py:jaccard_minhash` | 2 \| 1 \| 1 |
| py-147 | text | optional | `lecture14-slides.py:jaccard_minhash` | 3 \| 1 \| 1 |
| py-148 | text | optional | `lecture14-slides.py:jaccard_minhash` | 4 \| 1 \| 0 |
| py-149 | text | optional | `lecture14-slides.py:jaccard_minhash` | 5 \| 0 \| 1 |
| py-150 | text | optional | `lecture14-slides.py:jaccard_minhash` | Random hash function induces a permutation over items |
| py-151 | text | optional | `lecture14-slides.py:jaccard_minhash` | Look at which item is first in A and which item is first in B. |
| py-152 | text | optional | `lecture14-slides.py:jaccard_minhash` | Each item has the same probability as being first (min) |
| py-153 | text | optional | `lecture14-slides.py:jaccard_minhash` | - If 1, 2, 3 is first, then first in A = first in B. |
| py-154 | text | optional | `lecture14-slides.py:jaccard_minhash` | - If 4, 5 is first, then first in A ≠ first in B. |
| py-155 | text | optional | `lecture14-slides.py:jaccard_minhash` | Now we can hash our items, but a collision doesn't tell us Jaccard(A, B) > threshold. |
| py-156 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Locality sensitive hashing (LSH) |
| py-157 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Suppose we hash examples with just one MinHash function |
| py-158 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | P[A and B collide] = Jaccard(A, B) |
| py-159 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | On average, more similar items will collide, but very stochastic... |
| py-160 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Goal: have A and B collide if Jaccard(A, B) > threshold |
| py-161 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | We have to somehow sharpen the probabilities... |
| py-162 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Solution: use n hash functions |
| py-163 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Break up into b bands of r hash functions each (n = b * r) |
| py-164 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Hash functions: |
| py-165 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | h1 h2 h3 h4 \| h5 h6 h7 h8 \| h9 h10 h11 h12 |
| py-166 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Key: A and B collide if for *some* band, *all* its hash functions return same value |
| py-167 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | As we will see, the and-or structure of the bands sharpens the threshold |
| py-168 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Given Jaccard(A, B), what is the probability that A and B collide? |
| py-169 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | **Example** |
| py-170 | figure | yes | `lecture14-slides.py:locality_sensitive_hashing` | images/lsh-collision-probability.png |
| py-171 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Increasing r sharpens the threshold and moves the curve to the right (harder to match) |
| py-172 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Increasing b moves the curve to the left (easier to match) |
| py-173 | figure | yes | `lecture14-slides.py:locality_sensitive_hashing` | images/lsh-band-thresholds.png |
| py-174 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | : n = 9000, b = 20, r = 450 |
| py-175 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Example setting |
| py-176 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | What is the threshold (where the phase transition happens)? |
| py-177 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Probability that a fixed band matches: |
| py-178 | text | optional | `lecture14-slides.py:locality_sensitive_hashing` | Probability that A and B collide is a constant (≈ 1-1/e): |
| py-179 | text | optional | `lecture14-slides.py:data_mixing` | Recall that language models are trained on multiple data sources. |
| py-180 | text | optional | `lecture14-slides.py:data_mixing` | Datasets in Marin: |
| py-181 | figure | yes | `lecture14-slides.py:data_mixing` | images/marin-token-viewer.png |
| py-182 | text | optional | `lecture14-slides.py:data_mixing` | The Pile |
| py-183 | figure | yes | `lecture14-slides.py:data_mixing` | images/the-pile.png |
| py-184 | text | optional | `lecture14-slides.py:data_mixing` | Key question: what distribution over the data sources should we use? |
| py-185 | text | optional | `lecture14-slides.py:data_mixing` | Example: |
| py-186 | text | optional | `lecture14-slides.py:data_mixing` | Baselines: |
| py-187 | text | optional | `lecture14-slides.py:data_mixing` | - Vibes: set p(s) manually based on intuition (quite common) |
| py-188 | text | optional | `lecture14-slides.py:data_mixing` | - Uniform sampling: sample uniformly (p(s) ∝ 1) |
| py-189 | text | optional | `lecture14-slides.py:data_mixing` | - Proportional mixing: sample proportional to the number of tokens in a source (p(s) ∝ num_to... |
| py-190 | text | optional | `lecture14-slides.py:data_mixing` | Intuition: should upweight higher quality sources |
| py-191 | text | optional | `lecture14-slides.py:data_mixing` | However... |
| py-192 | text | optional | `lecture14-slides.py:data_mixing` | 1. We want to ensure diversity (e.g., across incomparable sources: literature, code, papers) |
| py-193 | text | optional | `lecture14-slides.py:data_mixing` | 2. Each source is finite, so if put too much weight on a small source, then need to epoch ove... |
| py-194 | text | optional | `lecture14-slides.py:data_mixing` | This last point is important and a bit subtle. |
| py-195 | text | optional | `lecture14-slides.py:data_mixing` | Example: |
| py-196 | text | optional | `lecture14-slides.py:data_mixing` | 50x epochs on high quality data...can lead to overfitting! |
| py-197 | text | optional | `lecture14-slides.py:data_mixing` | UniMax |
| py-198 | text | optional | `lecture14-slides.py:data_mixing` | - Setting: balancing different languages for multilingual models |
| py-199 | text | optional | `lecture14-slides.py:data_mixing` | - Previous work: between uniform and proportional mixing (p(s) ∝ num_tokens(s)^α for α in [0,... |
| py-200 | text | optional | `lecture14-slides.py:data_mixing` | - Idea: sample sources uniformly but with a hard **cap** C on number of epochs for any source |
| py-201 | text | optional | `lecture14-slides.py:data_mixing` | - Specifically, p(s) * num_training_tokens ≤ C for all sources s |
| py-202 | text | optional | `lecture14-slides.py:data_mixing` | Regression-based mixing |
| py-203 | figure | yes | `lecture14-slides.py:data_mixing` | images/regmix.png |
| py-204 | text | optional | `lecture14-slides.py:data_mixing` | - Define distribution over mixtures `p` (e.g., Dirichlet) |
| py-205 | text | optional | `lecture14-slides.py:data_mixing` | - Define regression method (e.g., linear, gradient boosted trees) |
| py-206 | text | optional | `lecture14-slides.py:data_mixing` | - Define target based on downstream evals (careful not to overfit!) |
| py-207 | text | optional | `lecture14-slides.py:data_mixing` | - Discrepancy between small and large scale (tradeoff cost and accuracy) |
| py-208 | figure | yes | `lecture14-slides.py:data_mixing` | images/data-mixing-methods.png |
| py-209 | text | optional | `lecture14-slides.py:data_mixing` | Hope 1: regression model is accurate at minimizer 🙏 |
| py-210 | text | optional | `lecture14-slides.py:data_mixing` | Hope 2: optimal data mixtures transfer from small to large scale 🙏 |
| py-211 | text | optional | `lecture14-slides.py:data_mixing` | Hold on. There's at least one scale-dependent effect: |
| py-212 | text | optional | `lecture14-slides.py:data_mixing` | - If train small models on low token counts: |
| py-213 | text | optional | `lecture14-slides.py:data_mixing` | - But if train large model on this mixture, we will epoch a ton on high quality data and over... |
| py-214 | text | optional | `lecture14-slides.py:data_mixing` | Simulated epoching |
| py-215 | text | optional | `lecture14-slides.py:data_mixing` | - General idea: make small scale look like large scale (general theme of this course) |
| py-216 | text | optional | `lecture14-slides.py:data_mixing` | - Instantiation: downsample all sources proportionally |
| py-217 | text | optional | `lecture14-slides.py:data_mixing` | - In this downsampled mixture, models that epoch too much won't look good. |
| py-218 | text | optional | `lecture14-slides.py:data_mixing` | - So the optimum will be more balanced. |
| py-219 | text | optional | `lecture14-slides.py:data_mixing` | Summary: |
| py-220 | text | optional | `lecture14-slides.py:data_mixing` | - Problem: how to weight different data sources (e.g., Wikipedia, general, code) |
| py-221 | text | optional | `lecture14-slides.py:data_mixing` | - Regression-based mixing: estimate mixture → loss at small scale, optimize (analogous to sca... |
| py-222 | text | optional | `lecture14-slides.py:data_mixing` | - Important consideration: epoching and overfitting (solution: cap or simulated) |
| py-223 | text | optional | `lecture14-slides.py:post_training_data` | Recipe: |
| py-224 | text | optional | `lecture14-slides.py:post_training_data` | 1. Define a set of environments |
| py-225 | text | optional | `lecture14-slides.py:post_training_data` | 2. Define a set of tasks / prompts |
| py-226 | text | optional | `lecture14-slides.py:post_training_data` | 3. Collect responses from a strong model (teacher) |
| py-227 | text | optional | `lecture14-slides.py:post_training_data` | OpenThoughts |
| py-228 | text | optional | `lecture14-slides.py:post_training_data` | - 1.2M examples using QwQ-32B as a teacher |
| py-229 | text | optional | `lecture14-slides.py:post_training_data` | - Questions come from 27 human and synthetic sources (e.g., StackExchange, NuminaMath, Chemis... |
| py-230 | figure | yes | `lecture14-slides.py:post_training_data` | images/openthoughts-sources.png |
| py-231 | text | optional | `lecture14-slides.py:post_training_data` | - Sampling multiple (16) responses per prompt is helpful |
| py-232 | text | optional | `lecture14-slides.py:post_training_data` | - Better models aren't necessarily better teachers: QwQ-32B is a better teacher than DeepSeek-R1 |
| py-233 | text | optional | `lecture14-slides.py:post_training_data` | - Answer filtering wasn't helpful |
| py-234 | text | optional | `lecture14-slides.py:post_training_data` | - Smaller high quality sources (e.g., OpenMath-2-Math) is better than large diverse sources |
| py-235 | figure | yes | `lecture14-slides.py:post_training_data` | images/openthoughts-pipeline.png |
| py-236 | text | optional | `lecture14-slides.py:post_training_data` | SWE-smith |
| py-237 | figure | yes | `lecture14-slides.py:post_training_data` | images/swe-smith.png |
| py-238 | text | optional | `lecture14-slides.py:post_training_data` | - Given a repository, use LM to generate tasks (introduce bugs with LM) |
| py-239 | text | optional | `lecture14-slides.py:post_training_data` | - 128 GitHub repositories yields 50K tasks |
| py-240 | text | optional | `lecture14-slides.py:post_training_data` | SWE-Zero |
| py-241 | text | optional | `lecture14-slides.py:post_training_data` | - SWE tasks have heavy dependencies (unlike math or coding contests) |
| py-242 | text | optional | `lecture14-slides.py:post_training_data` | - Setting up thousands of Docker images is an infrastructural nightmare |
| py-243 | text | optional | `lecture14-slides.py:post_training_data` | - Observation: strong models can solve many tasks without execution feedback |
| py-244 | figure | yes | `lecture14-slides.py:post_training_data` | images/swezero-noexec.png |
| py-245 | text | optional | `lecture14-slides.py:post_training_data` | Key: strong models have internal "world model" of code semantics |
| py-246 | text | optional | `lecture14-slides.py:post_training_data` | - SWE-Zero: 300K agent trajectories that don't require repository-specific execution |
| py-247 | text | optional | `lecture14-slides.py:post_training_data` | - 150K GitHub PRs |
| py-248 | text | optional | `lecture14-slides.py:post_training_data` | - OpenHands scaffold, remove future git commits to prevent "git hacking" by agent |
| py-249 | figure | yes | `lecture14-slides.py:post_training_data` | images/swezero-prompt.png |
| py-250 | text | optional | `lecture14-slides.py:post_training_data` | - Distilled from Qwen3-Coder-480B + filtering (try to execute anyway) |
| py-251 | text | optional | `lecture14-slides.py:post_training_data` | - SWE-Hero: 13K agent trajectories that do require execution feedback |
| py-252 | figure | yes | `lecture14-slides.py:post_training_data` | images/swezero-results.png |
| py-253 | text | optional | `lecture14-slides.py:post_training_data` | SWE-rebench |
| py-254 | text | optional | `lecture14-slides.py:post_training_data` | - 21K interactive Python SWE tasks from 3.4K GitHub repositories |
| py-255 | text | optional | `lecture14-slides.py:post_training_data` | - 450K PRs from GitHub and GitHub Archive |
| py-256 | text | optional | `lecture14-slides.py:post_training_data` | - Used Qwen 2.5-72B-Instruct to install dependencies and assess PR quality |
| py-257 | figure | yes | `lecture14-slides.py:post_training_data` | images/swe-rebench.png |
| py-258 | text | optional | `lecture14-slides.py:post_training_data` | SWE-ZERO-12M-trajectories |
| py-259 | text | optional | `lecture14-slides.py:post_training_data` | - Scale SWE-Zero up to 12M agent trajectories |
| py-260 | text | optional | `lecture14-slides.py:post_training_data` | - Used the SWE-rebench-v2 tasks (32K executable tasks + 120K nonexecutable tasks) |
| py-261 | text | optional | `lecture14-slides.py:post_training_data` | - Ran mini-coder-1.7b (very small model, 50.4 pass@100), mini-swe-agent scaffold |
| py-262 | text | optional | `lecture14-slides.py:post_training_data` | - [Example](https://huggingface.co/datasets/AlienKevin/SWE-ZERO-12M-trajectories/viewer/defau... |
| py-263 | text | optional | `lecture14-slides.py:post_training_data` | Summary: |
| py-264 | text | optional | `lecture14-slides.py:post_training_data` | - Generating prompts: fully-synthetic, semi-synthetic (real environment + synthetic tasks), r... |
| py-265 | text | optional | `lecture14-slides.py:post_training_data` | - Responses: from capable models (that are also good teachers) |
| py-266 | text | optional | `lecture14-slides.py:post_training_data` | - Code environments are painful |
| py-267 | text | optional | `lecture14-slides.py:post_training_data` | - Lots of filtering and other details |

## Existing Note

- `lecture14-notes.tex`

## Generation Contract

- Review every slide and figure node; teaching-bearing nodes are required by default.
- Every required slide/figure/section node must be placed in the note or explicitly marked optional with a concrete omission reason in the coverage matrix.
- Administrative, blank, duplicated, or genuinely redundant build-up slides may be marked optional only after review.
- For progressive reveals, include the final complete state at minimum and retain intermediate states when they teach a distinct step.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.

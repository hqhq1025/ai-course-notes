# Lecture 32 Writing Blueprint

## 1. Open-model context and source boundary

- Use slides 1--7 and 11.
- Correct the legacy empty video URL and replace the thumbnail-only visual treatment with the official 71-page speaker deck.
- Explain why open weights enable deployment/fine-tuning while opaque data/process details remain a reproducibility and governance limitation.

## 2. How much data: scaling and lifecycle economics

- Use slides 13--23.
- Derive Kaplan/Chinchilla-style loss terms and compute allocation.
- Separate training-compute optimum from deployment/lifecycle optimum; explain overtraining smaller models, inference cost, data-constrained regimes, and domain/data-quality caveats.

## 3. Where data comes from

- Use slides 26--36.
- Cover Common Crawl/FineWeb, The Stack v1/v2, Software Heritage, curated sources, code artifacts, Textbooks/Phi, and Cosmopedia.
- Explain provenance, opt-out, source diversity, synthetic-generation constraints, and the difference between raw bytes and usable tokens.

## 4. How filtering is discovered

- Use slides 39--43.
- Explain language/rule/perplexity filters, exact/near dedup, semantic/topic filtering, manual inspection, small-model ablations, high-signal benchmarks, and multiple seeds.
- Preserve the negative results for comment density and repository stars.

## 5. StarCoder/The Stack pipeline

- Use slides 44--52.
- Cover raw-to-filtered reduction, per-language thresholds, community inspection, MinHash/LSH, StarPII cost, benchmark decontamination, formatting, mixture design, and tooling.
- Add first-use definitions for MinHash, LSH, PII, decontamination, FIM, MQA/GQA, optimizer/resource terms where needed.

## 6. Open code ecosystem and responsible release

- Use slides 55--63.
- Explain next-token code modeling, ecosystem growth, base versus instruction models, BigCode collaboration, downstream ecosystem, open/responsible release layers, model-family evolution, and transparency index limits.

## 7. Evaluation, tooling, and contamination

- Use slides 64--70.
- Explain pass@1, HumanEval, MultiPL-E, DS-1000/RepoBench-style tasks, multi-benchmark evaluation, membership tests, personal fine-tuning, leaderboard protocol, contamination, and LiveCodeBench time splits.

## 8. Q&A and synthesis

- Integrate multimodal-data uncertainty, code/text similarities, IDE constraints, one-GPU fine-tuning, domain-dependent scaling, tokenizer choices, fine-tuning versus pretraining filters, and dataset-release governance.
- End with a reproducible data-to-model pipeline, self-test, and primary reading.

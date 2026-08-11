# Lecture 14 Blueprint — Data II

Narrative question: raw web/code/PDF material怎样经过 transformation、filtering、deduplication、mixing 和 synthetic-data generation，变成可训练且可审计的数据？

1. **从 raw source 到训练样本**：解释格式转换为什么有损，使用 DCLM/FinePDFs 作为证据。
2. **Filtering 是 target-vs-raw 的判别问题**：建立 scoring/threshold 框架，串联 language、quality、toxicity 与 DCLM/phi-1 案例。
3. **Deduplication 是规模化近似集合问题**：从 exact hash 到 Jaccard、MinHash、LSH，给出 worked example 和 contamination 边界。
4. **Mixing 是低成本实验设计问题**：解释 domain weights、small proxy runs、RegMix 和 distribution shift。
5. **Synthetic data 把 evaluation 变成 curriculum**：以 OpenThoughts、SWE-smith、SWE-rebench、SWE-zero 为例，区分生成、验证、过滤和环境构造。
6. **端到端数据工程闭环**：用审计表总结 source、license、transform、score、dedup、mix、eval、provenance。

Teacher voice: use `transcript_timed.txt` and executable `text(...)` nodes to preserve source-backed motivations, caveats, worked examples, and transitions. Record them in `lecture14-teacher-voice-ledger.md`; label note-authored synthesis as `讲义提醒` rather than attributing it to the instructor.

Transition out: Lecture 15 将从“怎样得到训练数据”转向“怎样用行为数据控制模型”。

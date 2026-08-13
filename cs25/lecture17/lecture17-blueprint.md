# Lecture 17 Writing Blueprint

## Historical Boundary

- Reconstruct the classroom state on 2023-02-21.
- Use official slides recovered from the classroom video as the visual spine.
- Use the official manual subtitles for motivations, caveats, transitions, and Q&A.
- Do not import Med-PaLM 2, Gemini-era biomedical claims, later regulatory decisions, or later benchmark numbers.

## Teaching Structure

1. **Source audit and lecture contract**
   - Use V001--V002.
   - Explain the three-domain journey and evidence boundary.
2. **Why Transformers fit biomedical data**
   - Use V003--V009.
   - Define clinical notes, EMR events, protein sequences, and genomes as different sequence representations.
   - Add a terminology table distinguishing token, event, amino acid, nucleotide, modality, and context length.
3. **Clinical language models and MultiMedQA**
   - Use V010--V022.
   - Motivate knowledge-intensive evaluation, benchmark composition, long-form answers, clinician versus layperson rubrics.
4. **PaLM, Flan-PaLM, Med-PaLM, and multidimensional evaluation**
   - Use V023--V043.
   - Explain scaling, instruction tuning, selective prediction, instruction prompt tuning, and every human-evaluation axis.
   - Preserve the Q&A corrections about non-complementary indicators, verbosity, harm, and complementarity.
5. **Long protein sequences: Performer and protein LMs**
   - Use V044--V049.
   - Derive quadratic attention cost and kernel-feature reordering.
   - Explain what amino-acid attention visualizations can and cannot establish.
6. **ProtNLM: protein sequence to natural language**
   - Use V050--V057.
   - Explain UniProt supervision, sequence-to-text, T5-style tasks, evaluation, and CRISPR-Cas9 example.
7. **Genomics I: DeepConsensus**
   - Use V058--V068.
   - Explain PacBio CCS, aligned subreads, gaps, alignment loss, base-quality prediction, read-level accuracy, and operational deployment.
8. **Genomics II: Enformer**
   - Use V069--V078.
   - Scaffold GWAS, coding versus non-coding variants, enhancers/promoters, long-range regulation, input/output tracks, and application boundaries.
9. **Foundation biomedical AI and open questions**
   - Use V079--V084.
   - Preserve the “when and how” thesis, integration of clinical and biological applications, scientific-discovery challenge, and Nobel question.

## Figure Treatment

- Reference all 84 slide assets exactly once.
- Use two-slide groups where slides form a single argument; use single-slide figures for dense tables, formulas, or result plots.
- Before every figure cluster, state the question and comparison target.
- After every cluster, explain axes/rows, trend, supported claim, and non-claim.
- Keep all images outside teaching boxes.

## Mathematical And Algorithmic Scaffolding

- Standard softmax attention and its quadratic score matrix.
- Performer kernel approximation and associative reordering.
- Selective prediction coverage and conditional accuracy.
- DeepConsensus token/base objective with alignment-aware penalty and quality score intuition.
- Enformer sequence-to-track mapping and variant-effect difference.
- At least three captioned pseudocode listings: selective prediction, linearized attention, and consensus correction.

## Quality Targets

- 84 full-resolution teaching images, each referenced once.
- At least 22,000 prose characters to maintain 260+ characters per image.
- At least 15 high-signal teaching boxes and 8 teacher-voice markers.
- At least 5 displayed formula blocks with immediate symbol explanations.
- At least 3 captioned `lstlisting` blocks.
- Every major section ends with `本章小结`; final section is `总结与延伸`.
- Strict coverage, `⭐⭐⭐` quality, two stable XeLaTeX passes, and signed visual QA.

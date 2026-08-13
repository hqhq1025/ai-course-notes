# CS25 V6 Lecture 03 — Recording Visual Audit

The official course page does not publish a deck for this lecture. This ledger records the exhaustive recording-derived slide audit before the final required/optional selection is frozen.

| Time range | Distinct visual state | Provisional treatment |
|---|---|---|
| 00:00:00--00:00:29 | Stanford Engineering opening card and classroom introduction | optional administrative/video opening |
| 00:00:30--00:01:29 | Talk title card; Albert Gu affiliation and Cartesia/CMU marks | cover/source metadata; optional as body slide |
| 00:01:30--00:04:09 | `Resurgence of Recurrent/Linear Models`: Mamba-1/2/3, xLSTM, (Gated) DeltaNet, Test-Time Training, then large-scale hybrid-model examples | required final complete state; earlier builds optional unless needed for readable staging |
| 00:04:10--00:05:09 | Same resurgence slide adds the umbrella labels `state space models`, `linear attention`, `linear RNNs`, `recurrent models`, `linear models` | required final taxonomy state; merge with preceding final state only if both lists remain readable |
| 00:05:10--00:06:09 | `Autoregressive Modeling`: train next-token probabilities, infer one token at a time, with growing dependency arrows | required final state |
| 00:06:10--00:06:39 | `Recap: Attention Inference` begins with prompt tokens and the first cache/dependency build | progressive build; continue audit before deciding final retained states |
| 00:06:40--00:07:49 | `Recap: Attention Inference` completes the dependency graph, explains that every generated token requires cached history, identifies the KV cache as the main inference inefficiency, then states memory/compute growth with context | required final complete state; intermediate builds optional |
| 00:07:50--00:08:49 | `High Level Tradeoffs`: Transformer attends to every past token; SSM updates a fixed state and discards tokens; linear generation versus highly compressed state | required final complete state |
| 00:08:50--00:13:09 | `Key Ingredients of SSMs` progressively fills three axes: state size/state expansion, input-dependent selective state update, and associative-scan efficiency/parallel training | required final complete state; retain earlier build only if the final state is too dense to read at note scale |
| 00:13:10--00:13:19 | brief speaker-only cut | no independent teaching visual |
| 00:13:20--00:14:19 | `Key Ingredients of SSMs` final efficiency state plus reference footnotes for associative scan / linear recurrence | merge into the final ingredient slide; preserve citations in source notes rather than duplicating near-identical frames |
| 00:14:20--00:14:59 | Mamba as a `Selective` SSM combining state size, state update, and efficiency; claim that recurrent models can compete with Transformers on language | required final state |
| 00:15:00--00:16:19 | comparison table of modern linear/recurrent models and attention; conclusion that many recent models are similar and the real question is the fundamental tradeoff versus attention | required final state; dense table needs local terminology digestion |
| 00:16:20--00:17:19 | `Key Concept: Autoregressive States`: every autoregressive model is a state-space model; state is what it remembers between time steps | required |
| 00:17:20--00:18:39 | `A Coarse Analogy`: Transformer as database with token-addressable history; SSM as brain with compressed state | required final complete state; analogy limitations must be stated explicitly |
| 00:18:40--00:19:39 | `Tradeoffs of SSMs`: stateful/compressive/interactivity and online processing, then lack of fine-grained recall/retrieval (associative, needle-in-a-haystack, general QA) | required final complete state |
| 00:19:40--00:19:59 | `Hybrid Models` title/equation asks how attention-like and recurrent components combine into intelligence | required transition if the next visual states supply the concrete design |
| 00:20:00--00:21:39 | `Hybrid Models` adds examples of recent hybrids and asks whether roughly a 10:1 SSM-to-attention layer ratio is optimal | required final state; describe the ratio as an empirical design pattern/question, not a universal law |
| 00:21:40--00:22:59 | extended speaker-only explanation | no independent teaching visual; preserve the spoken reasoning in the teacher-voice ledger |
| 00:23:00--00:23:29 | `Attention is All You Need?` myth: put raw data directly through a Transformer | required as setup for the contrast |
| 00:23:30--00:23:59 | reality: attention works best on pre-compressed data at the right level of abstraction | required |
| 00:24:00--00:24:29 | perceptual modalities use a patchifier/encoder before Transformer decoding | required final state |
| 00:24:30--00:24:59 | discrete modalities use a tokenizer before Transformer processing | required final state; connect to first-use definition of tokenization |
| 00:25:00--00:26:39 | `What Happens Without Tokenization?`: tokenizer edge-case critique, followed by the caveat that tokenization works in practice but is not fully learned end-to-end | required final state; preserve both the critique and the caveat |
| 00:26:40--00:28:49 | character/byte-level language-model scaling plot with references to MegaByte, SpaceByte, and hierarchical sequence modeling | required; explain axes, compute-matched comparison, and what the curves do not prove |
| 00:28:50--00:29:29 | DNA-language-model scaling law: Mamba matches a Transformer with roughly three times fewer parameters in the shown setting | required; keep benchmark/domain boundary explicit |
| 00:29:30--00:32:59 | `Effective Tokens for Attention`: asks whether every raw data token deserves a cached representation, whether hard attention makes sense, and lists effective units such as subwords, semantic/modular/compressible units, character/DNA/visual tokens | required final complete state; camera-derived frame likely needed because this interval is projector-dominant |
| 00:33:00--00:33:19 | `General Utility of Compressive Models` begins with a task/category distribution chart and the claim that compression supports strong out-of-the-box general models | continue audit to capture the complete state and its evidence boundary |
| 00:33:20--00:34:09 | `General Utility of Compressive Models` complete chart/state: broad non-language modalities motivate a general mechanism for compressing raw high-resolution sequences | required; chart labels and scope need explicit reading guidance |
| 00:34:10--00:37:19 | `H-Net`: end-to-end hierarchical network recursively compresses raw data through a data-dependent dynamic chunking process; byte sequence visualization shows learned segment boundaries | required final state; define dynamic chunking before the image |
| 00:37:20--00:39:59 | H-Net architecture: symmetric chunking/dechunking hierarchy, central sequence model, and detailed dynamic-chunking module; progressive bullets introduce hierarchical structure, multi-stage layout, and SSM encoders | required final complete state; retain an earlier uncluttered architecture frame only if it materially improves readability |
| 00:40:00--00:40:39 | H-Net architecture final bullets add the dynamic routing/smoothing module and improved signal propagation via norms, projections, stage-aware optimization | required final complete state |
| 00:40:40--00:44:09 | `Dynamic Chunking Scales Better` compute-matched plot: isobitropic BPE baseline versus one-/two-stage H-Net variants over bytes and BPE tokens; learned chunks tend to outperform hard-coded tokens | required final state; explain FLOP matching, axes, model labels, and that this is an empirical scaling result rather than a theorem |
| 00:44:10--00:46:09 | bits-per-byte scaling plot shows H-Net can be applied beyond raw bytes; when the input is already BPE-tokenized, Mamba in outer stages remains important | required final complete state; define bits-per-byte and distinguish base token resolution from learned chunk resolution |
| 00:46:10--00:46:39 | H-Net architecture revisited to connect the scaling curves back to the hierarchy | optional duplicate if the earlier architecture slide is already present and the prose makes the connection |
| 00:46:40--00:47:19 | same bits-per-byte plot; broadcast subtitle asks `Is compression a bug, or a feature?` | use the question as teacher voice, not as an independent slide |
| 00:47:20--00:49:19 | DNA scaling-law plot: raw data lacks non-semantic alphabets and tokenization heuristics, so learned dynamic chunking can scale dramatically better in the shown setup | required; retain the domain-specific limitation |
| 00:49:20--00:50:09 | `Attention is All You Need?` returns with a comic and the conclusion that attention is strongest on pre-compressed data at the right level of abstraction | required final synthesis state; may reuse the earlier abstraction slide only if this added comic/conclusion is preserved elsewhere |
| 00:50:10--00:51:19 | `Tradeoffs of SSMs`: apparent efficiency advantage is revised into the more fundamental stateful/compressive property; loss of fine-grained recall/retrieval remains | required final annotated state |
| 00:51:20--00:53:09 | `Tradeoffs of Attention`: fine-grained past-context access and strong recall/retrieval; quadratic-cost framing is revised into dependence on input resolution and semantic granularity; attention behaves like a database-like cache | required final annotated state |
| 00:53:10--00:53:19 | simple `FLOPs → Model → Capabilities` pipeline begins the closing abstraction | continue audit for final build |
| 00:53:20--00:54:34 | closing pipeline completes with `Is my model using its compute wisely?` | required closing slide; use it to connect architecture choice, resolution, and capability rather than treating FLOPs as architecture-neutral |
| 00:54:35--00:59:59 | in-person Q&A, speaker-only camera | no independent teaching visual; spoken answers remain required teacher voice |
| 01:00:00--01:03:39 | continued Q&A, speaker-only camera | no independent teaching visual |
| 01:03:40--01:03:49 | brief return to the already-audited H-Net architecture during a Q&A answer | optional duplicate; use the cleaner main-talk frame |
| 01:03:50--01:06:29 | final Q&A and closing, speaker/audience camera | no independent teaching visual |
| 01:06:30 onward | MongoDB sponsor presentation and startup promotion | excluded as non-course advertising |

## Audit conclusion

- The Albert Gu segment contains 32 independent teaching-bearing slide states after collapsing non-teaching title cards and progressive reveals that preserve no distinct reasoning step. The first contact-sheet review corrected two initial undercounts: the three SSM ingredients are replacement states rather than one cumulative slide, and the character/byte scaling curve appears after the tokenizer-caveat state.
- Three required states are camera/projector-dominant and need high-resolution projector crops: the complete hybrid-model slide, the complete effective-token slide, and the general-utility-of-compression slide. The late tradeoff and closing slides also need clean projector crops if no direct-feed instant is available.
- No deck-external classroom question card, whiteboard derivation, or independent visual demonstration was found. The Q&A contribution is verbal and belongs in the teacher-voice ledger rather than the figure manifest.

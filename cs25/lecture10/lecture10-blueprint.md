# CS25 Lecture 10 Blueprint

## Delivery target

- Chinese long-form teaching note using `../cs25-preamble.tex`.
- Source-first replacement of the legacy 12 KB screenshot-free draft.
- At least 20 pages, all 32 reviewed teaching slides, 10+ substantive boxes, 2+ captioned listings, explicit formulas, section summaries, and final synthesis.
- Preserve English technical terms when they carry specific meaning: `parse tree`, `capsule`, `embedding`, `coordinate frame`, `contrastive learning`, `collapse`, `attention`, `Hough transform`, `co-distillation`, and `neural field`.

## Evidence boundary

The lecture explains a proposed imaginary system. It may teach mechanisms, equations, and design tradeoffs, but it must not claim that GLOM was trained end-to-end, achieved benchmark results, solved object segmentation, or established a biological theory. Every modern connection must be labeled as a connection or engineering interpretation rather than a result from the lecture.

## Teaching spine

| Section | Core question | Source nodes | Required treatment |
|---|---|---|---|
| 1. 来源、目标与证据边界 | What is GLOM, and what kind of evidence is this talk offering? | V001--V003, T001--T002, P001 | Video metadata, vaporware/design-document warning, engineering versus brain-science goals, paper-version boundary. |
| 2. 固定网络如何表示动态 parse tree | Why is dynamic part-whole structure difficult for real neural nets? | V004--V006, T003--T005, P001--P003 | Symbolic allocation, pre-allocated capsules/routing, universal capsules, columns, levels, islands. |
| 3. Island of agreement 的表示语义 | What exactly is equal, what changes per image, and how does an island encode a node? | V006--V007, T005--T007, P001 | Activity-versus-weight distinction, nearly identical vectors, connected/disconnected islands, limitations. |
| 4. 坐标系、心理意象与结构歧义 | Why must part-whole relations carry pose and intrinsic coordinate frames? | V008--V014, T008--T011, P001--P003 | Cube exercise, six rods, crown/zig-zag parses, viewpoint-invariant relation matrices, mental-image coordinate choices. |
| 5. Contrastive learning 只是起点 | How do agreement objectives learn useful features, and why do they fail to identify parts automatically? | V015--V019, T012--T014, P004--P005 | SimCLR pipeline, collapse, negatives, linear probe, scene/object mismatch, spatial coherence. |
| 6. GLOM 的时空计算骨架 | What state exists at each location/level/time, and how is it updated? | V020--V023, T015--T019, P001, P006--P007 | First-fixation scope, static image as boring video, four-source update equation, bottom-up/top-down transforms, lateral attention. |
| 7. 从 similarity attention 到 islands | Why should local attention produce coherent regions rather than global collapse? | V022--V023, T019, P001 | Softmax similarity, local neighborhood, temperature/reliability weights, collapse and boundary caveats. |
| 8. 歧义、Hough voting 与 identity-pose 分布 | How can ambiguous parts support a common whole without relation-specific routing explosion? | V024--V026, T020--T023, P001 | Transformational-random-field complexity, part-to-whole voting, Hough analogy, multimodal log-probability basis, weak-evidence warning. |
| 9. 训练：重建、settling 与 consensus distillation | What objective could train the proposal? | V027--V029, T024--T025, P001, P007--P009 | Masked reconstruction, ten-step settling, BPTT, consensus target, co-distillation, weight-sharing/brain distinction. |
| 10. Replication、稀疏层级与 neural fields | Why duplicate embeddings, and how can shared decoders emit different parts? | V030--V032, T026--T030, P001, P010 | Hedge-bets locality, cluster formation, longer-range sparse upper levels, target-location-conditioned top-down prediction. |
| 11. 总结与现代连接 | Which ideas remain reusable even if GLOM itself is not deployed? | all | Separate confirmed lecture claims from careful connections to object-centric learning, iterative inference, world models, sparse attention, and coordinate-conditioned decoders. |

## Formula plan

1. Dynamic state: $\mathbf e_{x,\ell}^{(t)}$ for location $x$, hierarchy level $\ell$, settling step $t$.
2. Island criterion: $\|\mathbf e_{x,\ell}-\mathbf e_{y,\ell}\|\le\varepsilon$ for locations assigned to the same node, with an explicit “nearly identical, not guaranteed exact” caveat.
3. Coordinate composition: $R_{xv}=R_{wv}R_{xw}$, explaining intrinsic relation versus viewer-dependent pose.
4. SimCLR agreement and collapse: cosine similarity / InfoNCE scaffold with a warning that the lecture uses it conceptually rather than deriving the full loss.
5. Four-source GLOM update using bottom-up, top-down, persistence, and lateral consensus with reliability coefficients.
6. Lateral attention: $\alpha_{xy}\propto\exp(\beta\,\mathbf e_x^\top\mathbf e_y)$ over a local neighborhood.
7. Hough-style parent agreement: multiple parts map to a common parent identity-pose hypothesis.
8. Log-probability basis: $\log p(z\mid\mathbf e)=\sum_i e_i\phi_i(z)-\log Z(\mathbf e)$, labeled as a representational hypothesis.
9. Training objective: masked reconstruction plus consensus alignment / co-distillation.
10. Hierarchical systems table: neighborhood radius, sparsity, and approximate communication work by level.

## Code plan

- Listing 1: one settling iteration with four contributions and local attention.
- Listing 2: masked-patch training loop with recurrent settling and consensus target.

## Figure-treatment plan

- Every reviewed slide appears once at the idea it supports.
- Dense mechanism slides V007, V021--V026, and V028--V031 require nearby `读图` explanations.
- The cube and six-rod sequence is prose-led: first state the perceptual question, then show the slide, then explain what the demonstration does and does not establish.
- No images inside boxes.
- Captions cite the official video interval, and the same interval appears in the source line directly under the figure.

## Terminology scaffolding

Provide compact tables or boxes for:

- `parse tree`, node, part-whole hierarchy, intrinsic coordinate frame, viewer frame;
- capsule, universal capsule, column, level, embedding, island of agreement;
- contrastive learning, positive pair, negative pair, representation collapse, linear probe;
- bottom-up, top-down, temporal persistence, lateral attention, consensus;
- transformational random field, Hough transform, identity-pose space, multimodal distribution;
- distillation, co-distillation, BPTT, neural field, sparse long-range attention.

## Acceptance gates

- All V001--V032 nodes placed and all T001--T030 points synthesized.
- `check_note_coverage.py --strict` has no warnings.
- `check_quality.sh` reports `⭐⭐⭐`.
- Stable two-pass XeLaTeX has no overflow, undefined-reference, rerun, or hyperref warnings.
- PDF contact sheet and selected full-size pages are manually reviewed and the QA checklist is signed.

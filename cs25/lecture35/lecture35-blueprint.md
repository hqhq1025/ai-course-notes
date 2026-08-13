# Lecture 35 Writing Blueprint

## Teaching thesis

The lecture is not a generic introduction to reinforcement learning. Its central claim is that frontier AI products emerge from a closed co-design loop: product belief defines desired behavior; interaction traces become tasks and evals; eval failures expose data and environment defects; post-training changes behavior; interfaces let users probe and correct that behavior; the next round of evidence then changes the research target.

## Planned structure

1. **Opening and source boundary**
   - Figures 01--05.
   - Define frontier product research, product/research co-design, Canvas, calibration, and the difference between product demonstrations and causal evidence.
   - Preserve the speaker's creator-centered opening and the reason chat-only interfaces became insufficient.
2. **Capability vignettes and compositional products**
   - Figures 06--10.
   - Personal tools, interactive explanations, image generation, mobile games, and zero-cost software creation.
   - Explain that these demos combine generation, execution, rendering, iteration, and user control.
3. **Two scaling paradigms and two product-building paths**
   - Figures 11--23.
   - Next-token prediction versus RL on CoT; familiar form factor versus product-belief-first development.
   - Use CLIP fashion search, 100K context, and the summarizer as concrete interface/eval cases.
4. **Product belief, adaptive interfaces, and collaborators**
   - Figures 24--33.
   - Language as a product material, shared context across surfaces, writing IDEs, micro-personalization, Claude in Slack, Canvas collaborator training, and ChatGPT Tasks.
   - Distinguish assistant, tool, teammate, agent, and collaborator.
5. **Behavior evals: over-refusal as a source-first case study**
   - Figures 34--49.
   - Define a behavior vector, false-refusal rate, preference data, product flywheel, RLAIF, XSTest, helpfulness/harmlessness, and dataset-level debugging.
   - Treat before/after examples as evidence of changed behavior, not proof of universal safety.
6. **RL environment and reward as product architecture**
   - Figures 50--56.
   - Model the product as a partially observed MDP; explain tools, long horizon, recovery, multi-agent interaction, subjective rewards, and reward hacking.
   - Provide an environment contract and a product/research iteration loop.
7. **Future vignettes and long Q&A**
   - Figures 57--60.
   - Cost frontier, dynamic interfaces, personalized education/healthcare, and storytelling.
   - Integrate Q&A lessons on subjective benchmarks, entropy preservation, RLAIF diversity, qualitative diagnosis, synthetic-data verification, cost, robotics, social intelligence, and traditional versus research-driven product development.
8. **Final synthesis and extension**
   - One table connecting product belief, task, environment, reward, eval, data, interface, and deployment evidence.
   - Self-test questions, source integrity notes, and further reading.

## Quantitative targets

- 60 required visual states, each referenced exactly once.
- At least 260 prose characters per figure; target 20,000+ prose characters for margin.
- 30+ teaching boxes, 20+ teacher-voice markers, 12+ formula blocks, and 4+ captioned listings.
- At least 20 PDF pages, strict coverage with no warnings, `⭐⭐⭐`, clean two-pass XeLaTeX beyond repository-standard font notices, and signed canonical visual QA.

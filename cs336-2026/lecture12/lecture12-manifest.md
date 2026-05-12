# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture12`

## Files

- `lecture12-slides.py`

## Local Visual Assets

- none found

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | section | yes | `lecture12-slides.py:main` | Lecture 12: evaluation |
| py-002 | text | optional | `lecture12-slides.py:main` | - So far: we've covered everything for training an LM (architecture, training, systems, scali... |
| py-003 | text | optional | `lecture12-slides.py:main` | - Missing piece: what **data** do you train on? |
| py-004 | text | optional | `lecture12-slides.py:main` | - Data shapes model behavior (code? multilingual? DNA?). |
| py-005 | text | optional | `lecture12-slides.py:main` | - Before talking about data, need to talk about what behavior we want from a model. |
| py-006 | text | optional | `lecture12-slides.py:main` | **Evaluation**: given a model, how "**good**" is it? |
| py-007 | text | optional | `lecture12-slides.py:main` | Takeaways: |
| py-008 | text | optional | `lecture12-slides.py:main` | - There is no one true evaluation; choose the evaluation depending on what you're trying to m... |
| py-009 | text | optional | `lecture12-slides.py:main` | - Clearly state the rules of the game (methods versus models versus agents). |
| py-010 | text | optional | `lecture12-slides.py:main` | - Considerations: difficulty, realism, validity. |
| py-011 | text | optional | `lecture12-slides.py:what_is_good` | Evaluation might appear to be a mechanical process: |
| py-012 | text | optional | `lecture12-slides.py:what_is_good` | 1. Define some prompts |
| py-013 | text | optional | `lecture12-slides.py:what_is_good` | 2. Send prompts to a model and get back responses |
| py-014 | text | optional | `lecture12-slides.py:what_is_good` | 3. Compute accuracy |
| py-015 | text | optional | `lecture12-slides.py:what_is_good` | But actually, evaluation is a deep and important topic... |
| py-016 | text | optional | `lecture12-slides.py:what_is_good` | ...which shapes the development of AI. |
| py-017 | text | optional | `lecture12-slides.py:what_is_good` | **Core challenge**: <font color="red">abstract construct</font> → <font color="blue">concrete... |
| py-018 | text | optional | `lecture12-slides.py:what_is_good` | Maybe a model is good if it does well on benchmarks... |
| py-019 | figure | yes | `lecture12-slides.py:what_is_good` | images/artificial-analysis.png |
| py-020 | text | optional | `lecture12-slides.py:what_is_good` | Maybe a model is good if it does well on benchmarks and is cheap to run... |
| py-021 | figure | yes | `lecture12-slides.py:what_is_good` | images/artificial-analysis-cost.png |
| py-022 | text | optional | `lecture12-slides.py:what_is_good` | Maybe a model is good if people prefer its responses... |
| py-023 | figure | yes | `lecture12-slides.py:what_is_good` | images/lmarena-leaderboard.png |
| py-024 | text | optional | `lecture12-slides.py:what_is_good` | Maybe a model is good if people simply choose to use (and pay for) it... |
| py-025 | figure | yes | `lecture12-slides.py:what_is_good` | images/openrouter.png |
| py-026 | text | optional | `lecture12-slides.py:perplexity` | - Recall: that a language model is a probability distribution **p(x)** over sequences of tokens. |
| py-027 | text | optional | `lecture12-slides.py:perplexity` | - Perplexity (1/p(D))^(1/\|D\|) measures whether p assigns high probability to some dataset D. |
| py-028 | text | optional | `lecture12-slides.py:perplexity` | - In pre-training, you minimize perplexity on the training set. |
| py-029 | text | optional | `lecture12-slides.py:perplexity` | - The obvious thing is to measure perplexity on the test set. |
| py-030 | text | optional | `lecture12-slides.py:perplexity` | - This is what people did traditionally in language modeling research. |
| py-031 | text | optional | `lecture12-slides.py:perplexity` | Standard datasets: |
| py-032 | text | optional | `lecture12-slides.py:perplexity` | - Penn Treebank (WSJ) |
| py-033 | text | optional | `lecture12-slides.py:perplexity` | - WikiText-103 (Wikipedia) |
| py-034 | text | optional | `lecture12-slides.py:perplexity` | - One Billion Word Benchmark (from machine translation WMT11 - EuroParl, UN, news) |
| py-035 | text | optional | `lecture12-slides.py:perplexity` | Classic paradigm: in-distribution evaluation: train on train split and evaluate on test split... |
| py-036 | text | optional | `lecture12-slides.py:perplexity` | Pure CNNs+LSTMs on the One Billion Word Benchmark (perplexity 51.3 → 30.0) |
| py-037 | text | optional | `lecture12-slides.py:perplexity` | GPT-2: |
| py-038 | text | optional | `lecture12-slides.py:perplexity` | - Trained on WebText (40GB text, websites linked from Reddit) |
| py-039 | text | optional | `lecture12-slides.py:perplexity` | - Zero-shot on standard datasets (**out-of-distribution** evaluation) |
| py-040 | figure | yes | `lecture12-slides.py:perplexity` | images/gpt2-perplexity.png |
| py-041 | text | optional | `lecture12-slides.py:perplexity` | - Works better on small datasets (PTB) where transfer is helpful, but not larger datasets (1BW) |
| py-042 | text | optional | `lecture12-slides.py:perplexity` | Perplexity is all you need (more faith than science): |
| py-043 | text | optional | `lecture12-slides.py:perplexity` | - True distribution is t, model is p. |
| py-044 | text | optional | `lecture12-slides.py:perplexity` | - Best possible perplexity is H(t) obtained iff p = t. |
| py-045 | text | optional | `lecture12-slides.py:perplexity` | - If p = t, then solve all the tasks: p(solution \| problem) |
| py-046 | text | optional | `lecture12-slides.py:perplexity` | - So by pushing down on perplexity, we will eventually "reach AGI". |
| py-047 | text | optional | `lecture12-slides.py:perplexity` | Perplexity is maybe more than you need: |
| py-048 | text | optional | `lecture12-slides.py:perplexity` | - Example: *Stanford was founded in 1885* |
| py-049 | text | optional | `lecture12-slides.py:perplexity` | - Perplexity penalizes prediction on all tokens, some (e.g., *founded*) of which might not be... |
| py-050 | text | optional | `lecture12-slides.py:perplexity` | - Solution: measure conditional perplexity p(response \| prompt)^(1/\|response\|) |
| py-051 | text | optional | `lecture12-slides.py:perplexity` | Some benchmarks are perplexity in disguise: |
| py-052 | text | optional | `lecture12-slides.py:perplexity` | - Cloze tasks (fill in the blank): LAMBADA |
| py-053 | figure | yes | `lecture12-slides.py:perplexity` | images/lambada.png |
| py-054 | text | optional | `lecture12-slides.py:perplexity` | - Multiple choice sentence completion: HellaSwag |
| py-055 | figure | yes | `lecture12-slides.py:perplexity` | images/hellaswag.png |
| py-056 | text | optional | `lecture12-slides.py:perplexity` | **Warning** (if you're running a perplexity leaderboard): |
| py-057 | text | optional | `lecture12-slides.py:perplexity` | - People submit `LM` and you compute `log_prob = LM(test_data)` |
| py-058 | text | optional | `lecture12-slides.py:perplexity` | - You need to trust that the probabilities are valid (sum to 1) |
| py-059 | text | optional | `lecture12-slides.py:perplexity` | - For downstream tasks, `response = LM(prompt)` and compute accuracy on `response` |
| py-060 | text | optional | `lecture12-slides.py:perplexity` | Summary: |
| py-061 | text | optional | `lecture12-slides.py:perplexity` | - Perplexity is still used heavily in language model development (smooth scaling laws) |
| py-062 | text | optional | `lecture12-slides.py:perplexity` | - Still need benchmarks that capture real-world situations (for the non-believers)... |
| py-063 | text | optional | `lecture12-slides.py:exam_benchmarks` | Exams are a useful way to test language models (as with humans): |
| py-064 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Have control over the subject and difficulty |
| py-065 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Design to have unambiguous correct answer, easy to grade |
| py-066 | text | optional | `lecture12-slides.py:exam_benchmarks` | **Massive Multitask Language Understanding (MMLU)** |
| py-067 | text | optional | `lecture12-slides.py:exam_benchmarks` | - 57 subjects (e.g., math, US history, law, morality), multiple-choice |
| py-068 | text | optional | `lecture12-slides.py:exam_benchmarks` | - "collected by graduate and undergraduate students from freely available sources online" |
| py-069 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Despite the name, MMLU is really about testing knowledge, not language understanding |
| py-070 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Evaluated on GPT-3 using few-shot prompting |
| py-071 | figure | yes | `lecture12-slides.py:exam_benchmarks` | images/mmlu.png |
| py-072 | text | optional | `lecture12-slides.py:exam_benchmarks` | **MMLU-Pro** |
| py-073 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Removed noisy/trivial questions from MMLU |
| py-074 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Expanded 4 choices to 10 choices |
| py-075 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Evaluated using chain of thought (gives model more of a chance) |
| py-076 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Accuracy of models drop by 16% to 33% (not as saturated) |
| py-077 | figure | yes | `lecture12-slides.py:exam_benchmarks` | images/mmlu-pro.png |
| py-078 | text | optional | `lecture12-slides.py:exam_benchmarks` | **Graduate-Level Google-Proof Q&A (GPQA)** |
| py-079 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Questions written by 61 PhD contractors from Upwork |
| py-080 | figure | yes | `lecture12-slides.py:exam_benchmarks` | images/gpqa.png |
| py-081 | text | optional | `lecture12-slides.py:exam_benchmarks` | - PhD experts achieve 65% accuracy |
| py-082 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Non-experts achieve 34% over 30 minutes with access to Google |
| py-083 | text | optional | `lecture12-slides.py:exam_benchmarks` | - GPT-4 achieves 39% |
| py-084 | text | optional | `lecture12-slides.py:exam_benchmarks` | **Humanity's Last Exam (HLE)** |
| py-085 | text | optional | `lecture12-slides.py:exam_benchmarks` | - 2500 questions: multimodal, many subjects, multiple-choice + short-answer |
| py-086 | figure | yes | `lecture12-slides.py:exam_benchmarks` | images/hle-examples.png |
| py-087 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Awarded $500K prize pool + co-authorship to question creators |
| py-088 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Filtered by frontier LLMs, multiple stages of review |
| py-089 | figure | yes | `lecture12-slides.py:exam_benchmarks` | images/hle-pipeline.png |
| py-090 | figure | yes | `lecture12-slides.py:exam_benchmarks` | images/hle-results.png |
| py-091 | text | optional | `lecture12-slides.py:exam_benchmarks` | Summary: |
| py-092 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Trend towards harder questions as models improve and saturate existing benchmarks |
| py-093 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Multiple-choice format can be as difficult as one wants |
| py-094 | text | optional | `lecture12-slides.py:exam_benchmarks` | - Does not capture real usage (open-ended, doesn't necessarily exist correct answer) |
| py-095 | text | optional | `lecture12-slides.py:chat_benchmarks` | - So far, we've been evaluating on well-defined multiple-choice tasks. |
| py-096 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Most people don't ask multiple-choice exam questions to their AI assistant. |
| py-097 | text | optional | `lecture12-slides.py:chat_benchmarks` | Example: |
| py-098 | text | optional | `lecture12-slides.py:chat_benchmarks` | Prompt: *I would like to make a beet salad with goat cheese. What kind of herbs would work we... |
| py-099 | text | optional | `lecture12-slides.py:chat_benchmarks` | Response: *Here’s a breakdown of herbs that work well (and some that don’t) in a beet + goat ... |
| py-100 | text | optional | `lecture12-slides.py:chat_benchmarks` | **Challenge**: how to evaluate an open-ended response? |
| py-101 | text | optional | `lecture12-slides.py:chat_benchmarks` | **Chatbot Arena** |
| py-102 | text | optional | `lecture12-slides.py:chat_benchmarks` | Data collection: |
| py-103 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Random person from the Internet types in prompt |
| py-104 | text | optional | `lecture12-slides.py:chat_benchmarks` | - They get response from two random (anonymized) models |
| py-105 | text | optional | `lecture12-slides.py:chat_benchmarks` | - They rate which one is better |
| py-106 | figure | yes | `lecture12-slides.py:chat_benchmarks` | images/arena-beets.png |
| py-107 | text | optional | `lecture12-slides.py:chat_benchmarks` | Compute ELO rankings based on pairwise comparisons: |
| py-108 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Define model: p(A wins against B) = 1 / (1 + 10^((ELO_B - ELO_A)/400)) |
| py-109 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Fit this model to maximize probability of pairwise comparisons |
| py-110 | figure | yes | `lecture12-slides.py:chat_benchmarks` | images/lmarena-leaderboard.png |
| py-111 | text | optional | `lecture12-slides.py:chat_benchmarks` | Properties: |
| py-112 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Real-world prompts (free for users, incentives to actually use it) |
| py-113 | text | optional | `lecture12-slides.py:chat_benchmarks` | - But who are these people? biases? spammers? |
| py-114 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Binary preference but conflates style and correctness |
| py-115 | text | optional | `lecture12-slides.py:chat_benchmarks` | - How does the human even assess correctness? Prone to sycophancy? |
| py-116 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Feature: don't need to feed same prompts to all models (important because human is rating) |
| py-117 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Dynamic: incorporates new prompts and models over time |
| py-118 | text | optional | `lecture12-slides.py:chat_benchmarks` | **AlpacaEval** (2023) |
| py-119 | text | optional | `lecture12-slides.py:chat_benchmarks` | - 805 instructions from various sources |
| py-120 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Metric: win rate against baseline model (GPT-4 preview) as judged by GPT-4 preview (potenti... |
| py-121 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Problem: LLM judges favor longer responses, resulted in leaderboard gaming |
| py-122 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Alpaca Eval 2.0 used regression to debias the metric |
| py-123 | text | optional | `lecture12-slides.py:chat_benchmarks` | - How do we evaluate the metric? |
| py-124 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Correlation with Chatbot Arena (humans) is high: |
| py-125 | figure | yes | `lecture12-slides.py:chat_benchmarks` | https://github.com/tatsu-lab/alpaca_eval/raw/main/figures/chat_correlations_no_ae.png |
| py-126 | figure | yes | `lecture12-slides.py:chat_benchmarks` | images/alpacaeval-leaderboard.png |
| py-127 | text | optional | `lecture12-slides.py:chat_benchmarks` | **WildBench** |
| py-128 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Sourced 1024 examples from 1M human-chatbot conversations |
| py-129 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Uses GPT-4 turbo as a judge with a checklist (like CoT for judging) + GPT-4 as a judge |
| py-130 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Well-correlated with Chatbot Arena (seems to be the de facto sanity check) |
| py-131 | figure | yes | `lecture12-slides.py:chat_benchmarks` | images/wildbench.png |
| py-132 | text | optional | `lecture12-slides.py:chat_benchmarks` | Summary: |
| py-133 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Challenge: how to evaluate open-ended responses? |
| py-134 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Pairwise comparisons between similar responses provide higher signal |
| py-135 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Beware of biases (both from humans and LLM judges) |
| py-136 | text | optional | `lecture12-slides.py:chat_benchmarks` | - Checklist/rubric improves reliability (regardless of human or LLM judge) |
| py-137 | text | optional | `lecture12-slides.py:agentic_benchmarks` | Previously: evaluate what LMs say (chat) |
| py-138 | text | optional | `lecture12-slides.py:agentic_benchmarks` | Now: evaluate what LMs do (agents) |
| py-139 | text | optional | `lecture12-slides.py:agentic_benchmarks` | Agent = language model + agent scaffold (logic for deciding how to use the LM) |
| py-140 | text | optional | `lecture12-slides.py:agentic_benchmarks` | Consider tasks that require tool use (e.g., running code) and iterating over a period of time |
| py-141 | text | optional | `lecture12-slides.py:agentic_benchmarks` | **SWEBench** |
| py-142 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - 2294 tasks across 12 Python repositories |
| py-143 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Given codebase + issue description, submit a PR |
| py-144 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Evaluation metric: unit tests |
| py-145 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/swebench.png |
| py-146 | text | optional | `lecture12-slides.py:agentic_benchmarks` | **TerminalBench** |
| py-147 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/terminal-bench.png |
| py-148 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Computer terminal environments: simple and universal |
| py-149 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - 229 tasks crowdsourced from 93 contributors, 89 tasks constitute Terminal-Bench 2.0 |
| py-150 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/terminal-bench-human-time.png |
| py-151 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/terminal-bench-results.png |
| py-152 | text | optional | `lecture12-slides.py:agentic_benchmarks` | **CyBench** |
| py-153 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/cybench.png |
| py-154 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - 40 Capture the Flag (CTF) tasks |
| py-155 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Use first-solve time as a measure of difficulty |
| py-156 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/cybench-agent.png |
| py-157 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/cybench-results.png |
| py-158 | text | optional | `lecture12-slides.py:agentic_benchmarks` | **MLEBench** |
| py-159 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - 75 Kaggle competitions (require training models, processing data, etc.) |
| py-160 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/mlebench.png |
| py-161 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | images/mlebench-results.png |
| py-162 | text | optional | `lecture12-slides.py:agentic_benchmarks` | Agent scaffolds |
| py-163 | figure | yes | `lecture12-slides.py:agentic_benchmarks` | https://www.philschmid.de/static/blog/agents-2.0-deep-agents/overview.png |
| py-164 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Explicit planning: keep a todo list that gets checked off |
| py-165 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Hierarchical delegation: agents calling other sub-agents (clean context) |
| py-166 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Persistent memory: read/write files |
| py-167 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Extreme context engineering: explicit more instructions on process |
| py-168 | text | optional | `lecture12-slides.py:agentic_benchmarks` | Summary: |
| py-169 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Agents dramatically enhance the capability surface of language models |
| py-170 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Agent scaffolds are very important |
| py-171 | text | optional | `lecture12-slides.py:agentic_benchmarks` | - Evaluating agents = evaluating agent scaffold + language model |
| py-172 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - All of the tasks so far require linguistic and world knowledge. |
| py-173 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Can we isolate **reasoning** from knowledge? |
| py-174 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Arguably, reasoning captures a more pure form of intelligence (isn't just about memorizing ... |
| py-175 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | **ARC-AGI** |
| py-176 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - 100\% solvable by humans, but challenging for AI |
| py-177 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Each task is unique, so memorization doesn't help. |
| py-178 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - ARC-AGI-1 (2019): first iteration |
| py-179 | figure | yes | `lecture12-slides.py:pure_reasoning_benchmarks` | https://arcprize.org/media/images/arc-task-grids.jpg |
| py-180 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - ARC-AGI-2 (March 2025): more multi-step reasoning |
| py-181 | figure | yes | `lecture12-slides.py:pure_reasoning_benchmarks` | https://arcprize.org/media/images/blog/arc-agi-2-unsolved-1.png |
| py-182 | figure | yes | `lecture12-slides.py:pure_reasoning_benchmarks` | images/arc-agi-results.png |
| py-183 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Pretrained language models didn't move the needle |
| py-184 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Reasoning models (o1, o3) started making things take off |
| py-185 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - ARC-AGI-3 (March 2026): interactive environments |
| py-186 | figure | yes | `lecture12-slides.py:pure_reasoning_benchmarks` | images/arc-agi-3.png |
| py-187 | figure | yes | `lecture12-slides.py:pure_reasoning_benchmarks` | images/arc-agi-3-results.png |
| py-188 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | Summary: |
| py-189 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Goal is to disentangle reasoning from knowledge (difficult to do!) |
| py-190 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Constrained to human reasoning (not superhuman reasoning) |
| py-191 | text | optional | `lecture12-slides.py:pure_reasoning_benchmarks` | - Clearly exposes gaps in current models |
| py-192 | figure | yes | `lecture12-slides.py:safety_benchmarks` | https://www.team-bhp.com/forum/attachments/road-safety/2173645d1625144681-will-crash-test-rating-change-if-higher-variant-chosen-images-30.jpeg |
| py-193 | text | optional | `lecture12-slides.py:safety_benchmarks` | What does safety mean for AI? |
| py-194 | text | optional | `lecture12-slides.py:safety_benchmarks` | **HarmBench** |
| py-195 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Based on 510 harmful behaviors that violate laws or norms |
| py-196 | text | optional | `lecture12-slides.py:safety_benchmarks` | **AIR-Bench** |
| py-197 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Based on regulatory frameworks and company policies |
| py-198 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Taxonomized into 314 risk categories, 5694 prompts |
| py-199 | figure | yes | `lecture12-slides.py:safety_benchmarks` | https://crfm.stanford.edu/helm/assets/air-overview-DpBbyagA.png |
| py-200 | text | optional | `lecture12-slides.py:safety_benchmarks` | Jailbreaking: |
| py-201 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Language models are trained to refuse harmful instructions |
| py-202 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Greedy Coordinate Gradient (GCG) automatically optimizes prompts to bypass safety |
| py-203 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Transfers from open-weight models (Llama) to closed models (GPT-4) |
| py-204 | figure | yes | `lecture12-slides.py:safety_benchmarks` | images/gcg-examples.png |
| py-205 | text | optional | `lecture12-slides.py:safety_benchmarks` | What is safety? |
| py-206 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Many aspects of safety are strongly contextual (politics, law, social norms - which vary ac... |
| py-207 | text | optional | `lecture12-slides.py:safety_benchmarks` | - Many risks are quite varied (hallucinations, sycophancy, abetting crimes, inequality, losin... |
| py-208 | text | optional | `lecture12-slides.py:safety_benchmarks` | **Dual-use**: capable cybersecurity agents (Mythos) can be used to hack into a system or to d... |
| py-209 | text | optional | `lecture12-slides.py:realism` | **Ecological validity**: how well does an evaluation capture real-world use? |
| py-210 | text | optional | `lecture12-slides.py:realism` | - Exam benchmarks (e.g., GPQA) are far away from real-world use. |
| py-211 | text | optional | `lecture12-slides.py:realism` | - Chatbot Arena prompts are from real people, but distribution is uncontrolled. |
| py-212 | text | optional | `lecture12-slides.py:realism` | **GDPVal** (OpenAI) |
| py-213 | text | optional | `lecture12-slides.py:realism` | - 44 occupations from top 9 sectors according to US GDP |
| py-214 | text | optional | `lecture12-slides.py:realism` | - Tasks come from professionals with ~14 years of experience |
| py-215 | figure | yes | `lecture12-slides.py:realism` | images/gdpval.png |
| py-216 | text | optional | `lecture12-slides.py:realism` | **MedHELM** |
| py-217 | text | optional | `lecture12-slides.py:realism` | - Previous medical benchmarks were based on standardized exams |
| py-218 | text | optional | `lecture12-slides.py:realism` | - 121 clinical tasks sourced from 29 clinicians, mixture of private and public datasets |
| py-219 | figure | yes | `lecture12-slides.py:realism` | https://crfm.stanford.edu/helm/assets/medhelm-overview-CND0EIsy.png |
| py-220 | text | optional | `lecture12-slides.py:realism` | **Clio** (Anthropic) |
| py-221 | text | optional | `lecture12-slides.py:realism` | - Use language models to analyze real user data |
| py-222 | text | optional | `lecture12-slides.py:realism` | - Share general patterns of what people are asking |
| py-223 | figure | yes | `lecture12-slides.py:realism` | images/clio-table4.png |
| py-224 | text | optional | `lecture12-slides.py:realism` | Unfortunately, realism and privacy are sometimes at odds with each other. |
| py-225 | text | optional | `lecture12-slides.py:validity` | How do we know our evaluations are valid? |
| py-226 | section | yes | `lecture12-slides.py:validity` | Train-test overlap |
| py-227 | text | optional | `lecture12-slides.py:validity` | - Machine learning 101: don't train on your test set |
| py-228 | text | optional | `lecture12-slides.py:validity` | - Pre-foundation models (ImageNet, SQuAD): well-defined train-test splits |
| py-229 | text | optional | `lecture12-slides.py:validity` | - Today: train on the Internet and don't tell people about your data |
| py-230 | text | optional | `lecture12-slides.py:validity` | Route 1: try to infer train-test overlap from model |
| py-231 | text | optional | `lecture12-slides.py:validity` | - Exploit exchangeability of data points |
| py-232 | figure | yes | `lecture12-slides.py:validity` | images/contamination-exchangeability.png |
| py-233 | text | optional | `lecture12-slides.py:validity` | Route 2: encourage reporting norms (e.g., people report confidence intervals) |
| py-234 | text | optional | `lecture12-slides.py:validity` | - Model providers should report train-test overlap |
| py-235 | text | optional | `lecture12-slides.py:validity` | Route 3: use fresh evals |
| py-236 | text | optional | `lecture12-slides.py:validity` | - LiveCodeBench, UncheatableEval: scrape new webpages |
| py-237 | text | optional | `lecture12-slides.py:validity` | - Timestamps aren't always safe due to copying either |
| py-238 | text | optional | `lecture12-slides.py:validity` | Route 4: use private evals |
| py-239 | text | optional | `lecture12-slides.py:validity` | - Companies use internal code bases that aren't on the Internet |
| py-240 | text | optional | `lecture12-slides.py:validity` | - Use your personal writings |
| py-241 | text | optional | `lecture12-slides.py:validity` | - Easiest for perplexity |
| py-242 | section | yes | `lecture12-slides.py:validity` | Dataset quality |
| py-243 | text | optional | `lecture12-slides.py:validity` | - Fixed up SWE-Bench to produce SWE-Bench Verified |
| py-244 | text | optional | `lecture12-slides.py:validity` | - Create Platinum versions of benchmarks |
| py-245 | figure | yes | `lecture12-slides.py:validity` | https://pbs.twimg.com/media/GjICXQlWkAAYnDS?format=jpg&name=4096x4096 |
| py-246 | figure | yes | `lecture12-slides.py:validity` | https://pbs.twimg.com/media/GjICcGQXYAAM4o1?format=jpg&name=4096x4096 |
| py-247 | text | optional | `lecture12-slides.py:validity` | - Problems with agentic benchmarks: insufficient test cases, trivial agent can solve task |
| py-248 | text | optional | `lecture12-slides.py:validity` | - Docent: use LLM to inspect agent traces to detect problems |
| py-249 | section | yes | `lecture12-slides.py:how_to_think_about_evaluation` | What's the point of evaluation? |
| py-250 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | There is no one true evaluation; it depends on what question you're trying to answer. |
| py-251 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | 1. User or company wants to make a purchase decision (model A or model B) for their use case ... |
| py-252 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | 2. Researchers want to measure the raw capabilities of a model (e.g., intelligence). |
| py-253 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | 3. We want to understand the benefits + harms of a model (for business and policy reasons). |
| py-254 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | 4. Model developers want to get feedback to improve the model. |
| py-255 | section | yes | `lecture12-slides.py:how_to_think_about_evaluation` | What are we evaluating? |
| py-256 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | - Pre-foundation models, we evaluated **methods** (standardized train-test splits). |
| py-257 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | - Today, we're (mostly) evaluating **models/systems** (anything goes). |
| py-258 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | There are some exceptions... |
| py-259 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | - nanogpt speedrun: fixed data, compute time to get to a particular validation loss |
| py-260 | figure | yes | `lecture12-slides.py:how_to_think_about_evaluation` | images/karpathy-nanogpt-speedrun.png |
| py-261 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | Evaluating methods encourage algorithmic innovation from researchers. |
| py-262 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | Evaluating models/systems is useful for downstream users. |
| py-263 | text | optional | `lecture12-slides.py:how_to_think_about_evaluation` | Either way, we need to define the rules of the game! |

## Existing Note

- none

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.

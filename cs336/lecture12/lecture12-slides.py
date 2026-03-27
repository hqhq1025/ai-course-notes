from execute_util import text, link, image
from lecture_util import x_link, blog_link
from references import deepseek_r1, llama4, olmo2_32b, mmlu

def main():
    text("**Evaluation**: given a **fixed model**, how \"**good**\" is it?")

    what_you_see()
    how_to_think_about_evaluation()

    perplexity()

    knowledge_benchmarks()
    instruction_following_benchmarks()
    agent_benchmarks()
    pure_reasoning_benchmarks()
    safety_benchmarks()

    realism()
    validity()
    what_are_we_evaluating()

    text("Takeaways")
    text("- There is no one true evaluation; choose the evaluation depending on what you're trying to measure.")
    text("- Always look at the individual instances and the predictions.")
    text("- There are many aspects to consider: capabilities, safety, costs, realism.")
    text("- Clearly state the rules of the game (methods versus models/systems).")


def what_you_see():
    text("## Benchmark scores")
    image("images/deepseek-r1-benchmarks.png", width=800), link(deepseek_r1)
    image("images/llama4-benchmarks.png", width=800), link(llama4)
    image("https://www.datocms-assets.com/64837/1741887109-instruct-1.png", width=800), link(olmo2_32b)

    text("Recent language models are evaluated on similar, but not entirely identical, benchmarks (MMLU, MATH, etc.).")
    text("What are these benchmarks?")
    text("What do these numbers mean?")

    image("images/helm-capabilities-leaderboard.png", width=1000)
    link(title="[HELM capabilities]", url="https://crfm.stanford.edu/helm/capabilities/latest/#/leaderboard")

    text("Pay close attention to the costs!")
    image("images/artificial-analysis.png", width=800), link(title="[Artificial Analysis]", url="https://artificialanalysis.ai/")

    text("Maybe a model is good if people choose to use it (and pay for it)...")
    image("images/openrouter.png", width=600), link(title="[OpenRouter]", url="https://openrouter.ai/rankings")

    image("images/chatbot-arena-leaderboard.png", width=800)
    link(title="[Chatbot Arena]", url="https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard")

    text("## Vibes")
    x_link("https://x.com/demishassabis/status/1919779362980692364")
    image("images/demis-gemini-2.5.png", width=500)

    text("A crisis...")
    image("images/karpathy-crisis.png", width=600)


def how_to_think_about_evaluation():
    text("You might think evaluation is a mechanical process (take existing model, throw prompts at it, average some numbers)...")
    text("Actually, evaluation is a profound and rich topic...")
    text("...and it determines the future of language models.")

    text("What's the point of evaluation?")
    text("There is no one true evaluation; it depends on what question you're trying to answer.")
    text("1. User or company wants to make a purchase decision (model A or model B) for their use case (e.g., customer service chatbots).")
    text("2. Researchers want to measure the raw capabilities of a model (e.g., intelligence).")
    text("3. We want to understand the benefits + harms of a model (for business and policy reasons).")
    text("4. Model developers want to get feedback to improve the model.")
    text("In each case, there is an abstract **goal** that needs to be translated into a concrete evaluation.")

    text("Framework")
    text("1. What are the **inputs**?")
    text("2. How do **call** the language model?")
    text("3. How do you evaluate the **outputs**?")
    text("4. How to **interpret** the results?")

    text("What are the inputs?")
    text("1. What use cases are **covered**?")
    text("2. Do we have representation of **difficult** inputs in the tail?")
    text("3. Are the inputs **adapted** to the model (e.g., multi-turn)?")

    text("How do you call the language model?")
    text("1. How do you prompt the language model?")
    text("2. Does the language model use chain-of-thought, tools, RAG, etc.?")
    text("3. Are we evaluating the language model or an agentic system (model developer wants former, user wants latter)?")

    text("How do you evaluate the outputs?")
    text("1. Are the reference outputs used for evaluation error-free?")
    text("2. What metrics do you use (e.g., pass@k)?")
    text("3. How do you factor in cost (e.g., inference + training)?")
    text("4. How do you factor in asymmetric errors (e.g., hallucinations in a medical setting)?")
    text("5. How do you handle open-ended generation (no ground truth)?")

    text("How do you inteprret the metrics?")
    text("1. How do you interpret a number (e.g., 91%) - is it ready for deployment?")
    text("2. How do we assess generalization in the face of train-test overlap?")
    text("3. Are we evaluating the final model or the method?")

    text("Summary: lots of questions to think through when doing evaluation")

def perplexity():
    text("Recall: that a language model is a probability distribution **p(x)** over sequences of tokens.")
    text("Perplexity (1/p(D))^(1/|D|) measures whether p assigns high probability to some dataset D.")

    text("In pre-training, you minimize perplexity on the training set.")
    text("The obvious thing is to measure perplexity on the test set.")

    text("Standard datasets: Penn Treebank (WSJ), WikiText-103 (Wikipedia), One Billion Word Benchmark (from machine translation WMT11 - EuroParl, UN, news)")
    text("Papers trained on a dataset (training split) and evaluated on the same dataset (test split)")
    text("Pure CNNs+LSTMs on the One Billion Word Benchmark (perplexity 51.3 -> 30.0) "), link("https://arxiv.org/abs/1602.02410")

    text("GPT-2 trained on WebText (40GB text, websites linked from Reddit), zero-shot on standard datasets")
    text("This is out-of-distribution evaluation (but idea is that training covers a lot)")
    image("images/gpt2-perplexity.png", width=800)
    text("Works better on small datasets (transfer is helpful), but not larger datasets (1BW)")

    text("Since GPT-2 and GPT-3, language modeling papers have shifted more towards downstream task accuracy.")
    text("But reasons why perplexity is still useful:")
    text("- Smoother than downstream task accuracy (for fitting scaling laws)")
    text("- Is universal (why we use it for training) whereas task accuracy might miss some nuances")
    text("- Note: can measure conditional perplexity on downstream task too (used for scaling laws) "), link("https://arxiv.org/abs/2412.04403")

    text("Warning (if you're running a leaderboard): evaluator needs to trust the language model")
    text("For task accuracy, can just take output generated from a blackbox model and compute the desired metrics")
    text("For perplexity, need LM to generate probabilities and trust that they sum to 1 (even worse with UNKs back in the day)")

    text("The perplexity maximalist view:")
    text("- Your true distribution is t, model is p")
    text("- Best possible perplexity is H(t) obtained iff p = t")
    text("- If have t, then solve all the tasks")
    text("- So by pushing down on perplexity, will eventually reach AGI")
    text("- Caveat: this might not be the most efficient way to get there (pushing down on parts of the distribution that don't matter)")

    text("Things that are spiritually perplexity:")
    text("Similar idea: cloze tasks like LAMBADA "), link("https://arxiv.org/abs/1606.06031")
    image("images/lambada.png", width=800)
    text("HellaSwag "), link("https://arxiv.org/pdf/1905.07830")
    image("images/hellaswag.png", width=600)


def knowledge_benchmarks():
    text("### Massive Multitask Language Understanding (MMLU)")
    link(mmlu)
    text("- 57 subjects (e.g., math, US history, law, morality), multiple-choice")
    text("- \"collected by graduate and undergraduate students from freely available sources online\"")
    text("- Really about testing knowledge, not language understanding")
    text("- Evaluated on GPT-3 using few-shot prompting")
    image("images/mmlu.png", width=800)
    link(title="[HELM MMLU for visualizing predictions]", url="https://crfm.stanford.edu/helm/mmlu/latest/")

    text("### MMLU-Pro")
    link("https://arxiv.org/abs/2406.01574")
    text("- Removed noisy/trivial questions from MMLU")
    text("- Expanded 4 choices to 10 choices")
    text("- Evaluated using chain of thought (gives model more of a chance)")
    text("- Accuracy of models drop by 16% to 33% (not as saturated)")
    image("images/mmlu-pro.png", width=800)
    link(title="[HELM MMLU-Pro for visualizing predictions]", url="https://crfm.stanford.edu/helm/capabilities/latest/#/leaderboard/mmlu_pro")

    text("### Graduate-Level Google-Proof Q&A (GPQA)")
    link("https://arxiv.org/abs/2311.12022")
    text("- Questions written by 61 PhD contractors from Upwork")
    image("images/gpqa.png", width=800)
    text("- PhD experts achieve 65% accuracy")
    text("- Non-experts achieve 34% over 30 minutes with access to Google")
    text("- GPT-4 achieves 39%")
    link(title="[HELM GPQA for visualizing predictions]", url="https://crfm.stanford.edu/helm/capabilities/latest/#/leaderboard/gpqa")

    text("### Humanity's Last Exam")
    link("https://arxiv.org/abs/2501.14249")
    text("- 2500 questions: multimodal, many subjects, multiple-choice + short-answer")
    image("images/hle-examples.png", width=800)
    text("- Awarded $500K prize pool + co-authorship to question creators")
    text("- Filtered by frontier LLMs, multiple stages of review")
    image("images/hle-pipeline.png", width=800)
    image("images/hle-results.png", width=800)
    link(title="[latest leaderboard]", url="https://agi.safe.ai/")


def instruction_following_benchmarks():
    text("So far, we've been evaluating on fairly structured tasks.")
    text("Instruction following (as popularized by ChatGPT): just follow the instructions.")
    text("Challenge: how to evaluate an open-ended response?")

    text("### Chatbot Arena")
    link("https://arxiv.org/abs/2403.04132")
    text("How it works:")
    text("- Random person from the Internet types in prompt")
    text("- They get response from two random (anonymized) models")
    text("- They rate which one is better")
    text("- ELO scores are computed based on the pairwise comparisons")
    text("- Features: live (not static) inputs, can accomodate new models")
    image("images/chatbot-arena-leaderboard.png", width=800)
    link(title="[Chatbot Arena]", url="https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard")

    text("### Instruction-Following Eval (IFEval)")
    link("https://arxiv.org/abs/2311.07911")
    image("images/ifeval-categories.png", width=600)
    text("- Add simple synthetic constraints to instructions")
    text("- Constraints can be automatically verified, but not the semantics of the response")
    text("- Fairly simple instructions, constraints are a bit artificial")
    link(title="[HELM IFEval for visualizing predictions]", url="https://crfm.stanford.edu/helm/capabilities/latest/#/leaderboard/ifeval")

    text("### AlpacaEval")
    link("https://tatsu-lab.github.io/alpaca_eval/")
    text("- 805 instructions from various sources")
    text("- Metric: win rate against GPT-4 preview as judged by GPT-4 preview (potential bias)")
    image("images/alpacaeval-leaderboard.png", width=600)

    text("### WildBench")
    link("https://arxiv.org/pdf/2406.04770")
    text("- Sourced 1024 examples from 1M human-chatbot conversations")
    text("- Uses GPT-4 turbo as a judge with a checklist (like CoT for judging) + GPT-4 as a judge")
    text("- Well-correlated (0.95) with Chatbot Arena (seems to be the de facto sanity check for benchmarks)")
    image("images/wildbench.png", width=800)
    link(title="[HELM WildBench for visualizing predictions]", url="https://crfm.stanford.edu/helm/capabilities/latest/#/leaderboard/wildbench")


def agent_benchmarks():
    text("Consider tasks that require tool use (e.g., running code) and iterating over a period of time")
    text("Agent = language model + agent scaffolding (logic for deciding how to use the LM)")

    text("### SWEBench")
    link("https://arxiv.org/abs/2310.06770")
    text("- 2294 tasks across 12 Python repositories")
    text("- Given codebase + issue description, submit a PR")
    text("- Evaluation metric: unit tests")
    image("images/swebench.png", width=800)

    text("### CyBench")
    link("https://arxiv.org/abs/2408.08926")
    text("- 40 Capture the Flag (CTF) tasks")
    text("- Use first-solve time as a measure of difficulty")
    image("images/cybench.png", width=800)
    image("images/cybench-agent.png", width=800)
    image("images/cybench-results.png", width=800)

    text("### MLEBench")
    link("https://arxiv.org/abs/2410.07095")
    text("- 75 Kaggle competitions (require training models, processing data, etc.)")
    image("images/mlebench.png", width=800)
    image("images/mlebench-results.png", width=800)


def pure_reasoning_benchmarks():
    text("All of the tasks so far require linguistic and world knowledge")
    text("Can we isolate reasoning from knowledge?")
    text("Arguably, reasoning captures a more pure form of intelligence (isn't just about memorizing facts)")

    link(title="ARC-AGI", url="https://arcprize.org/arc-agi")
    text("Introduced in 2019 by Francois Chollet")

    text("ARC-AGI-1")
    image("https://arcprize.org/media/images/arc-task-grids.jpg", width=800)
    image("https://arcprize.org/media/images/oseriesleaderboard.png", width=800)

    text("ARC-AGI-2: harder")
    image("https://arcprize.org/media/images/blog/arc-agi-2-unsolved-1.png", width=800)


def safety_benchmarks():
    image("https://www.team-bhp.com/forum/attachments/road-safety/2173645d1625144681-will-crash-test-rating-change-if-higher-variant-chosen-images-30.jpeg", width=500)
    text("What does safety mean for AI?")

    link(title="[HELM safety: curated set of benchmarks]", url="https://crfm.stanford.edu/helm/safety/latest/#/leaderboard")

    text("### HarmBench")
    link("https://arxiv.org/abs/2402.04249")
    text("- Based on 510 harmful behaviors that violate laws or norms")
    link(title="[HarmBench on HELM]", url="https://crfm.stanford.edu/helm/safety/latest/#/leaderboard/harm_bench")
    link(title="[Example of safety failure]", url="https://crfm.stanford.edu/helm/safety/latest/#/runs/harm_bench:model=anthropic_claude-3-7-sonnet-20250219?instancesPage=4")

    text("### AIR-Bench")
    link("https://arxiv.org/abs/2407.17436")
    text("- Based on regulatory frameworks and company policies")
    text("- Taxonomized into 314 risk categories, 5694 prompts")
    image("https://crfm.stanford.edu/helm/assets/air-overview-d2e6c49f.png", width=800)
    link(title="[HELM AIR-Bench]", url="https://crfm.stanford.edu/helm/air-bench/latest/#/leaderboard")

    text("### Jailbreaking")
    text("- Language models are trained to refuse harmful instructions")
    text("- Greedy Coordinate Gradient (GCG) automatically optimizes prompts to bypass safety "), link("https://arxiv.org/pdf/2307.15043")
    text("- Transfers from open-weight models (Llama) to closed models (GPT-4)")
    image("images/gcg-examples.png", width=800)

    text("### Pre-deployment testing")
    text("- US Safety Institute + UK AI Safety Institute working together")
    text("- Company gives safety institutes access to model before release (currently voluntary)")
    text("- Safety institutes run evaluations and produce a report to company")
    link(title="[report]", url="https://www.nist.gov/system/files/documents/2024/12/18/US_UK_AI%20Safety%20Institute_%20December_Publication-OpenAIo1.pdf")

    text("### But what is safety?")
    text("- Many aspects of safety are strongly contextual (politics, law, social norms - which vary across countries)")
    text("- Naively, one might think safety is about refusal and is at odds with capability, but there's more...")
    text("- Hallucinations in a medical setting makes systems more capable and more safe")

    text("Two aspects of a model that reduce safety: capabilities + propensity")
    text("- A system could be capable of doing something, but refuse to do it")
    text("- For API models, propensity matters")
    text("- For open weight models, capability matters (since can easily fine-tune safety away)")

    text("**Dual-use**: capable cybersecurity agents (do well on CyBench) can be used to hack into a system or to do penetration testing")
    text("CyBench is used by the safety institute as a safety evaluation, but is it really a capability evaluation?")


def realism():
    text("Language models are used heavily in practice:")
    image("images/openai-100b-tokens.png", width=600); link(title=" [tweet]", url="https://x.com/sama/status/1756089361609981993")
    image("images/cursor-1b-lines.png", width=600); link(title=" [tweet]", url="https://x.com/amanrsanger/status/1916968123535880684")

    text("However, most existing benchmarks (e.g., MMLU) are far away from real-world use.")
    text("Live traffic from real people contain garbage, that's not always what we want either.")

    text("Two types of prompts:")
    text("1. Quizzing: User knows the answer and trying to test the system (think standardized exams).")
    text("2. Asking: User doesn't know the answer is trying to use the system to get it.")
    text("Asking is more realistic and produces value for the user.")

    text("### Clio (Anthropic)")
    link("https://arxiv.org/abs/2412.13678")
    text("- Use language models to analyze real user data")
    text("- Share general patterns of what people are asking")
    image("images/clio-table4.png", width=700)

    text("### MedHELM")
    link("https://arxiv.org/abs/2412.13678")
    text("- Previous medical benchmarks were based on standardized exams")
    text("- 121 clinical tasks sourced from 29 clinicians, mixture of private and public datasets")
    image("https://crfm.stanford.edu/helm/assets/medhelm-overview-3ddfcd65.png", width=700)
    link(title="[MedHELM]", url="https://crfm.stanford.edu/helm/medhelm/latest/#/leaderboard")

    text("Unfortunately, realism and privacy are sometimes at odds with each other.")


def validity():
    text("How do we know our evaluations are valid?")

    text("### Train-test overlap")
    text("- Machine learning 101: don't train on your test set")
    text("- Pre-foundation models (ImageNet, SQuAD): well-defined train-test splits")
    text("- Nowadays: train on the Internet and don't tell people about your data")

    text("Route 1: try to infer train-test overlap from model")
    text("- Exploit exchangeability of data points"), link("https://arxiv.org/pdf/2310.17623")
    image("images/contamination-exchangeability.png", width=600)

    text("Route 2: encourage reporting norms (e.g., people report confidence intervals)")
    text("- Model providers should report train-test overlap "), link("https://arxiv.org/abs/2410.08385")

    text("### Dataset quality")
    text("- Fixed up SWE-Bench to produce SWE-Bench Verified "), blog_link("https://openai.com/index/introducing-swe-bench-verified/")
    text("- Create Platinum versions of benchmarks"), link("https://arxiv.org/abs/2502.03461")
    image("https://pbs.twimg.com/media/GjICXQlWkAAYnDS?format=jpg&name=4096x4096", width=700)
    image("https://pbs.twimg.com/media/GjICcGQXYAAM4o1?format=jpg&name=4096x4096", width=800)


def what_are_we_evaluating():
    text("What are we even evaluating?")
    text("In other words, what are the rules of a game?")

    text("Pre-foundation models, we evaluated **methods** (standardized train-test splits).")
    text("Today, we're evaluating **models/systems** (anything goes).")

    text("There are some exceptions...")
    text("nanogpt speedrun: fixed data, compute time to get to a particular validation loss")
    image("images/karpathy-nanogpt-speedrun.png", width=600), x_link("https://x.com/karpathy/status/1846790537262571739")

    text("DataComp-LM: given a raw dataset, get the best accuracy using standard training pipeline "), link("https://arxiv.org/abs/2406.11794")

    text("Evaluating methods encourage algorithmic innovation from researchers.")
    text("Evaluating models/systems is useful for downstream users.")

    text("Either way, we need to define the rules of the game!")


if __name__ == "__main__":
    main()

import regex
from abc import ABC
from dataclasses import dataclass
from collections import defaultdict
import random

from execute_util import link, image, text
from lecture_util import article_link, x_link, youtube_link
from references import gpt_3, gpt4, shannon1950, bengio2003, susketver2014, \
    bahdanau2015_attention, transformer_2017, gpt2, t5, kaplan_scaling_laws_2020, \
    the_pile, gpt_j, opt_175b, bloom, palm, chinchilla, llama, mistral_7b, \
    instruct_gpt, dpo, adamw2017, lima, deepseek_v3, adam2014, grpo, ppo2017, muon, \
    large_batch_training_2018, wsd_2024, cosine_learning_rate_2017, olmo_7b, moe_2017, \
    megatron_lm_2019, shazeer_2020, elmo, bert, qwen_2_5, deepseek_r1, moe_2017, \
    rms_norm_2019, rope_2021, soap, gqa, mla, deepseek_67b, deepseek_v2, brants2007, \
    layernorm_2016, pre_post_norm_2020, llama2, llama3, olmo2, \
    megabyte, byt5, blt, tfree, sennrich_2016, zero_2019, gpipe_2018
from data import get_common_crawl_urls, read_common_crawl, write_documents, markdownify_documents
from model_util import query_gpt4o

import tiktoken

def main():
    welcome()
    why_this_course_exists()
    current_landscape()

    what_is_this_program()

    course_logistics()
    course_components()

    tokenization()

    text("Next time: PyTorch building blocks, resource accounting")


def welcome():
    text("## CS336: Language Models From Scratch (Spring 2025)"),

    image("images/course-staff.png", width=600)

    text("This is the second offering of CS336.")
    text("Stanford edition has grown by 50%.")
    text("Lectures will be posted on YouTube and be made available to the whole world.")


def why_this_course_exists():
    text("## Why did we make this course?")

    text("Let's ask GPT-4 "), link(gpt4)
    response = query_gpt4o(prompt="Why teach a course on building language models from scratch? Answer in one sentence.")  # @inspect response
    
    text("Problem: researchers are becoming **disconnected** from the underlying technology.")
    text("8 years ago, researchers would implement and train their own models.")
    text("6 years ago, researchers would download a model (e.g., BERT) and fine-tune it.")
    text("Today, researchers just prompt a proprietary model (e.g., GPT-4/Claude/Gemini).")

    text("Moving up levels of abstractions boosts productivity, but")
    text("- These abstractions are leaky (in contrast to programming languages or operating systems).")
    text("- There is still fundamental research to be done that require tearing up the stack.")

    text("**Full understanding** of this technology is necessary for **fundamental research**.")

    text("This course: **understanding via building**")
    text("But there's one small problem...")

    text("## The industrialization of language models")
    image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Industrialisation.jpg/440px-Industrialisation.jpg", width=400)

    text("GPT-4 supposedly has 1.8T parameters. "), article_link("https://www.hpcwire.com/2024/03/19/the-generative-ai-future-is-now-nvidias-huang-says")
    text("GPT-4 supposedly cost $100M to train. "), article_link("https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/")
    text("xAI builds cluster with 200,000 H100s to train Grok. "), article_link("https://www.tomshardware.com/pc-components/gpus/elon-musk-is-doubling-the-worlds-largest-ai-gpu-cluster-expanding-colossus-gpu-cluster-to-200-000-soon-has-floated-300-000-in-the-past")
    text("Stargate (OpenAI, NVIDIA, Oracle) invests $500B over 4 years. "), article_link("https://openai.com/index/announcing-the-stargate-project/")

    text("Also, there are no public details on how frontier models are built.")
    text("From the GPT-4 technical report "), link(gpt4), text(":")
    image("images/gpt4-no-details.png", width=600)

    text("## More is different")
    text("Frontier models are out of reach for us.")
    text("But building small language models (<1B parameters in this class) might not be representative of large language models.")

    text("Example 1: fraction of FLOPs spent in attention versus MLP changes with scale. "), x_link("https://x.com/stephenroller/status/1579993017234382849")
    image("images/roller-flops.png", width=400)
    text("Example 2: emergence of behavior with scale "), link("https://arxiv.org/pdf/2206.07682")
    image("images/wei-emergence-plot.png", width=600)

    text("## What can we learn in this class that transfers to frontier models?")
    text("There are three types of knowledge:")
    text("- **Mechanics**: how things work (what a Transformer is, how model parallelism leverages GPUs)")
    text("- **Mindset**: squeezing the most out of the hardware, taking scale seriously (scaling laws)")
    text("- **Intuitions**: which data and modeling decisions yield good accuracy")

    text("We can teach mechanics and mindset (these do transfer).")
    text("We can only partially teach intuitions (do not necessarily transfer across scales).")

    text("## Intuitions? 🤷")
    text("Some design decisions are simply not (yet) justifiable and just come from experimentation.")
    text("Example: Noam Shazeer paper that introduced SwiGLU "), link(shazeer_2020)
    image("images/divine-benevolence.png", width=600)

    text("## The bitter lesson")
    text("Wrong interpretation: scale is all that matters, algorithms don't matter.")
    text("Right interpretation: algorithms that scale is what matters.")
    text("### accuracy = efficiency x resources")
    text("In fact, efficiency is way more important at larger scale (can't afford to be wasteful).")
    link("https://arxiv.org/abs/2005.04305"), text(" showed 44x algorithmic efficiency on ImageNet between 2012 and 2019")

    text("Framing: what is the best model one can build given a certain compute and data budget?")
    text("In other words, **maximize efficiency**!")


def current_landscape():
    text("## Pre-neural (before 2010s)")
    text("- Language model to measure the entropy of English "), link(shannon1950)
    text("- Lots of work on n-gram language models (for machine translation, speech recognition) "), link(brants2007)

    text("## Neural ingredients (2010s)")
    text("- First neural language model "), link(bengio2003)
    text("- Sequence-to-sequence modeling (for machine translation) "), link(susketver2014)
    text("- Adam optimizer "), link(adam2014)
    text("- Attention mechanism (for machine translation) "), link(bahdanau2015_attention)
    text("- Transformer architecture (for machine translation) "), link(transformer_2017)
    text("- Mixture of experts "), link(moe_2017)
    text("- Model parallelism "), link(gpipe_2018), link(zero_2019), link(megatron_lm_2019)

    text("## Early foundation models (late 2010s)")
    text("- ELMo: pretraining with LSTMs, fine-tuning helps tasks "), link(elmo)
    text("- BERT: pretraining with Transformer, fine-tuning helps tasks "), link(bert)
    text("- Google's T5 (11B): cast everything as text-to-text "), link(t5)

    text("## Embracing scaling, more closed")
    text("- OpenAI's GPT-2 (1.5B): fluent text, first signs of zero-shot, staged release "), link(gpt2)
    text("- Scaling laws: provide hope / predictability for scaling "), link(kaplan_scaling_laws_2020)
    text("- OpenAI's GPT-3 (175B): in-context learning, closed "), link(gpt_3)
    text("- Google's PaLM (540B): massive scale, undertrained "), link(palm)
    text("- DeepMind's Chinchilla (70B): compute-optimal scaling laws "), link(chinchilla)

    text("## Open models")
    text("- EleutherAI's open datasets (The Pile) and models (GPT-J) "), link(the_pile), link(gpt_j)
    text("- Meta's OPT (175B): GPT-3 replication, lots of hardware issues "), link(opt_175b)
    text("- Hugging Face / BigScience's BLOOM: focused on data sourcing "), link(bloom)
    text("- Meta's Llama models "), link(llama), link(llama2), link(llama3)
    text("- Alibaba\'s Qwen models "), link(qwen_2_5)
    text("- DeepSeek\'s models "), link(deepseek_67b), link(deepseek_v2), link(deepseek_v3)
    text("- AI2's OLMo 2 "), link(olmo_7b), link(olmo2),

    text("## Levels of openness")
    text("- Closed models (e.g., GPT-4o): API access only "), link(gpt4)
    text("- Open-weight models (e.g., DeepSeek): weights available, paper with architecture details, some training details, no data details "), link(deepseek_v3)
    text("- Open-source models (e.g., OLMo): weights and data available, paper with most details (but not necessarily the rationale, failed experiments) "), link(olmo_7b)

    text("## Today's frontier models")
    text("- OpenAI's o3 "), link("https://openai.com/index/openai-o3-mini/")
    text("- Anthropic's Claude Sonnet 3.7 "), link("https://www.anthropic.com/news/claude-3-7-sonnet")
    text("- xAI's Grok 3 "), link("https://x.ai/news/grok-3")
    text("- Google's Gemini 2.5 "), link("https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/")
    text("- Meta's Llama 3.3 "), link("https://ai.meta.com/blog/meta-llama-3/")
    text("- DeepSeek's r1 "), link(deepseek_r1)
    text("- Alibaba's Qwen 2.5 Max "), link("https://qwenlm.github.io/blog/qwen2.5-max/")
    text("- Tencent's Hunyuan-T1 "), link("https://tencent.github.io/llm.hunyuan.T1/README_EN.html")


def what_is_this_program():
    text("This is an *executable lecture*, a program whose execution delivers the content of a lecture.")
    text("Executable lectures make it possible to:")
    text("- view and run code (since everything is code!),")
    total = 0  # @inspect total
    for x in [1, 2, 3]:  # @inspect x
        total += x  # @inspect total
    text("- see the hierarchical structure of the lecture, and")
    text("- jump to definitions and concepts: "), link(supervised_finetuning)


def course_logistics():
    text("All information online: "), link("https://stanford-cs336.github.io/spring2025/")

    text("This is a 5-unit class.")
    text("Comment from Spring 2024 course evaluation: *The entire assignment was approximately the same amount of work as all 5 assignments from CS 224n plus the final project. And that's just the first homework assignment.*")

    text("## Why you should take this course")
    text("- You have an obsessive need to understand how things work.")
    text("- You want to build up your research engineering muscles.")

    text("## Why you should not take this course")
    text("- You actually want to get research done this quarter.<br>(Talk to your advisor.)")
    text("- You are interested in learning about the hottest new techniques in AI (e.g., multimodality, RAG, etc.).<br>(You should take a seminar class for that.)")
    text("- You want to get good results on your own application domain.<br>(You should just prompt or fine-tune an existing model.)")

    text("## How you can follow along at home")
    text("- All lecture materials and assignments will be posted online, so feel free to follow on your own.")
    text("- Lectures are recorded via [CGOE, formally SCPD](https://cgoe.stanford.edu/) and be made available on YouTube (with some lag).")
    text("- We plan to offer this class again next year.")

    text("## Assignments")
    text("- 5 assignments (basics, systems, scaling laws, data, alignment).")
    text("- No scaffolding code, but we provide unit tests and adapter interfaces to help you check correctness.")
    text("- Implement locally to test for correctness, then run on cluster for benchmarking (accuracy and speed).")
    text("- Leaderboard for some assignments (minimize perplexity given training budget).")
    text("- AI tools (e.g., CoPilot, Cursor) can take away from learning, so use at your own risk.")

    text("## Cluster")
    text("- Thanks to Together AI for providing a compute cluster. 🙏")
    text("- Please read [the guide](https://docs.google.com/document/d/1BSSig7zInyjDKcbNGftVxubiHlwJ-ZqahQewIzBmBOo/edit) on how to use the cluster.")
    text("- Start your assignments early, since the cluster will fill up close to the deadline!")


def course_components():
    text("## It's all about efficiency")
    text("Resources: data + hardware (compute, memory, communication bandwidth)")
    text("How do you train the best model given a fixed set of resources?")
    text("Example: given a Common Crawl dump and 32 H100s for 2 weeks, what should you do?")

    text("Design decisions:")
    image("images/design-decisions.png", width=800)

    text("## Overview of the course")
    basics()
    systems()
    scaling_laws()
    data()
    alignment()

    text("## Efficiency drives design decisions")

    text("Today, we are compute-constrained, so design decisions will reflect squeezing the most out of given hardware.")
    text("- Data processing: avoid wasting precious compute updating on bad / irrelevant data")
    text("- Tokenization: working with raw bytes is elegant, but compute-inefficient with today's model architectures.")
    text("- Model architecture: many changes motivated by reducing memory or FLOPs (e.g., sharing KV caches, sliding window attention)")
    text("- Training: we can get away with a single epoch!")
    text("- Scaling laws: use less compute on smaller models to do hyperparameter tuning")
    text("- Alignment: if tune model more to desired use cases, require smaller base models")

    text("Tomorrow, we will become data-constrained...")


class Tokenizer(ABC):
    """Abstract interface for a tokenizer."""
    def encode(self, string: str) -> list[int]:
        raise NotImplementedError

    def decode(self, indices: list[int]) -> str:
        raise NotImplementedError


def basics():
    text("Goal: get a basic version of the full pipeline working")
    text("Components: tokenization, model architecture, training")

    text("## Tokenization")
    text("Tokenizers convert between strings and sequences of integers (tokens)")
    image("images/tokenized-example.png", width=600) 
    text("Intuition: break up string into popular segments")

    text("This course: Byte-Pair Encoding (BPE) tokenizer "), link(sennrich_2016)

    text("Tokenizer-free approaches: "), link(byt5), link(megabyte), link(blt), link(tfree)
    text("Use bytes directly, promising, but have not yet been scaled up to the frontier.")
    
    text("## Architecture")
    text("Starting point: original Transformer "), link(transformer_2017)
    image("images/transformer-architecture.png", width=500)

    text("Variants:")
    text("- Activation functions: ReLU, SwiGLU "), link(shazeer_2020)
    text("- Positional encodings: sinusoidal, RoPE "), link(rope_2021)
    text("- Normalization: LayerNorm, RMSNorm "), link(layernorm_2016), link(rms_norm_2019)
    text("- Placement of normalization: pre-norm versus post-norm "), link(pre_post_norm_2020)
    text("- MLP: dense, mixture of experts "), link(moe_2017)
    text("- Attention: full, sliding window, linear "), link(mistral_7b), link("https://arxiv.org/abs/2006.16236")
    text("- Lower-dimensional attention: group-query attention (GQA), multi-head latent attention (MLA) "), link(gqa), link(mla)
    text("- State-space models: Hyena "), link("https://arxiv.org/abs/2302.10866")

    text("## Training")
    text("- Optimizer (e.g., AdamW, Muon, SOAP) "), link(adam2014), link(adamw2017), link(muon), link(soap)
    text("- Learning rate schedule (e.g., cosine, WSD) "), link(cosine_learning_rate_2017), link(wsd_2024)
    text("- Batch size (e..g, critical batch size) "), link(large_batch_training_2018)
    text("- Regularization (e.g., dropout, weight decay)")
    text("- Hyperparameters (number of heads, hidden dimension): grid search")

    text("## Assignment 1")
    link(title="[GitHub]", url="https://github.com/stanford-cs336/assignment1-basics"), link(title="[PDF]", url="https://github.com/stanford-cs336/assignment1-basics/blob/main/cs336_spring2025_assignment1_basics.pdf")
    text("- Implement BPE tokenizer")
    text("- Implement Transformer, cross-entropy loss, AdamW optimizer, training loop")
    text("- Train on TinyStories and OpenWebText")
    text("- Leaderboard: minimize OpenWebText perplexity given 90 minutes on a H100 "), link(title="[last year's leaderboard]", url="https://github.com/stanford-cs336/spring2024-assignment1-basics-leaderboard")


def systems():
    text("Goal: squeeze the most out of the hardware")
    text("Components: kernels, parallelism, inference")

    text("## Kernels")
    text("What a GPU (A100) looks like:")
    image("https://miro.medium.com/v2/resize:fit:2000/format:webp/1*6xoBKi5kL2dZpivFe1-zgw.jpeg", width=800)
    text("Analogy: warehouse : DRAM :: factory : SRAM")
    image("https://horace.io/img/perf_intro/factory_bandwidth.png", width=400)
    text("Trick: organize computation to maximize utilization of GPUs by minimizing data movement")
    text("Write kernels in CUDA/**Triton**/CUTLASS/ThunderKittens")

    text("## Parallelism")
    text("What if we have multiple GPUs (8 A100s)?")
    image("https://www.fibermall.com/blog/wp-content/uploads/2024/09/the-hardware-topology-of-a-typical-8xA100-GPU-host.png", width=500)
    text("Data movement between GPUs is even slower, but same 'minimize data movement' principle holds")
    text("Use collective operations (e.g., gather, reduce, all-reduce)")
    text("Shard (parameters, activations, gradients, optimizer states) across GPUs")
    text("How to split computation: {data,tensor,pipeline,sequence} parallelism")
    
    text("## Inference")
    text("Goal: generate tokens given a prompt (needed to actually use models!)")
    text("Inference is also needed for reinforcement learning, test-time compute, evaluation")
    text("Globally, inference compute (every use) exceeds training compute (one-time cost)")
    text("Two phases: prefill and decode")
    image("images/prefill-decode.png", width=500)
    text("Prefill (similar to training): tokens are given, can process all at once (compute-bound)")
    text("Decode: need to generate one token at a time (memory-bound)")
    text("Methods to speed up decoding:")
    text("- Use cheaper model (via model pruning, quantization, distillation)")
    text("- Speculative decoding: use a cheaper \"draft\" model to generate multiple tokens, then use the full model to score in parallel (exact decoding!)")
    text("- Systems optimizations: KV caching, batching")

    text("## Assignment 2")
    link(title="[GitHub from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment2-systems"), link(title="[PDF from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment2-systems/blob/master/cs336_spring2024_assignment2_systems.pdf")
    text("- Implement a fused RMSNorm kernel in Triton")
    text("- Implement distributed data parallel training")
    text("- Implement optimizer state sharding")
    text("- Benchmark and profile the implementations")


def scaling_laws():
    text("Goal: do experiments at small scale, predict hyperparameters/loss at large scale")
    text("Question: given a FLOPs budget ($C$), use a bigger model ($N$) or train on more tokens ($D$)?")
    text("Compute-optimal scaling laws: "), link(kaplan_scaling_laws_2020), link(chinchilla)
    image("images/chinchilla-isoflop.png", width=800)
    text("TL;DR: $D^* = 20 N^*$ (e.g., 1.4B parameter model should be trained on 28B tokens)")
    text("But this doesn't take into account inference costs!")

    text("## Assignment 3")
    link(title="[GitHub from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment3-scaling"), link(title="[PDF from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment3-scaling/blob/master/cs336_spring2024_assignment3_scaling.pdf")
    text("- We define a training API (hyperparameters -> loss) based on previous runs")
    text("- Submit \"training jobs\" (under a FLOPs budget) and gather data points")
    text("- Fit a scaling law to the data points")
    text("- Submit predictions for scaled up hyperparameters")
    text("- Leaderboard: minimize loss given FLOPs budget")


def data():
    text("Question: What capabilities do we want the model to have?")
    text("Multilingual? Code? Math?")
    image("https://ar5iv.labs.arxiv.org/html/2101.00027/assets/pile_chart2.png", width=600)

    text("## Evaluation")
    text("- Perplexity: textbook evaluation for language models")
    text("- Standardized testing (e.g., MMLU, HellaSwag, GSM8K)")
    text("- Instruction following (e.g., AlpacaEval, IFEval, WildBench)")
    text("- Scaling test-time compute: chain-of-thought, ensembling")
    text("- LM-as-a-judge: evaluate generative tasks")
    text("- Full system: RAG, agents")

    text("## Data curation")
    text("- Data does not just fall from the sky.")
    look_at_web_data()
    text("- Sources: webpages crawled from the Internet, books, arXiv papers, GitHub code, etc.")
    text("- Appeal to fair use to train on copyright data? "), link("https://arxiv.org/pdf/2303.15715.pdf")
    text("- Might have to license data (e.g., Google with Reddit data) "), article_link("https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/")
    text("- Formats: HTML, PDF, directories (not text!)")

    text("## Data processing")
    text("- Transformation: convert HTML/PDF to text (preserve content, some structure, rewriting)")
    text("- Filtering: keep high quality data, remove harmful content (via classifiers)")
    text("- Deduplication: save compute, avoid memorization; use Bloom filters or MinHash")

    text("## Assignment 4")
    link(title="[GitHub from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment4-data"), link(title="[PDF from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment4-data/blob/master/cs336_spring2024_assignment4_data.pdf")
    text("- Convert Common Crawl HTML to text")
    text("- Train classifiers to filter for quality and harmful content")
    text("- Deduplication using MinHash")
    text("- Leaderboard: minimize perplexity given token budget")


def look_at_web_data():
    urls = get_common_crawl_urls()[:3]  # @inspect urls
    documents = list(read_common_crawl(urls[1], limit=300))
    random.seed(40)
    random.shuffle(documents)
    documents = markdownify_documents(documents[:10])
    write_documents(documents, "var/sample-documents.txt")
    link(title="[sample documents]", url="var/sample-documents.txt")
    text("It's a wasteland out there!  Need to really process the data.")


def alignment():
    text("So far, a **base model** is raw potential, very good at completing the next token.")
    text("Alignment makes the model actually useful.")

    text("Goals of alignment:")
    text("- Get the language model to follow instructions")
    text("- Tune the style (format, length, tone, etc.)")
    text("- Incorporate safety (e.g., refusals to answer harmful questions)")

    text("Two phases:")
    supervised_finetuning()
    learning_from_feedback()

    text("## Assignment 5")
    link(title="[GitHub from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment5-alignment"), link(title="[PDF from 2024]", url="https://github.com/stanford-cs336/spring2024-assignment5-alignment/blob/master/cs336_spring2024_assignment5_alignment.pdf")
    text("- Implement supervised fine-tuning")
    text("- Implement Direct Preference Optimization (DPO)")
    text("- Implement Group Relative Preference Optimization (GRPO)")


@dataclass(frozen=True)
class Turn:
    role: str
    content: str


@dataclass(frozen=True)
class ChatExample:
    turns: list[Turn]


@dataclass(frozen=True)
class PreferenceExample:
    history: list[Turn]
    response_a: str
    response_b: str
    chosen: str


def supervised_finetuning():
    text("## Supervised finetuning (SFT)")

    text("Instruction data: (prompt, response) pairs")
    sft_data: list[ChatExample] = [
        ChatExample(
            turns=[
                Turn(role="system", content="You are a helpful assistant."),
                Turn(role="user", content="What is 1 + 1?"),
                Turn(role="assistant", content="The answer is 2."),
            ],
        ),
    ]
    text("Data often involves human annotation.")
    text("Intuition: base model already has the skills, just need few examples to surface them. "), link(lima)
    text("Supervised learning: fine-tune model to maximize p(response | prompt).")


def learning_from_feedback():
    text("Now we have a preliminary instruction following model.")
    text("Let's make it better without expensive annotation.")
    
    text("## Preference data")
    text("Data: generate multiple responses using model (e.g., [A, B]) to a given prompt.")
    text("User provides preferences (e.g., A < B or A > B).")
    preference_data: list[PreferenceExample] = [
        PreferenceExample(
            history=[
                Turn(role="system", content="You are a helpful assistant."),
                Turn(role="user", content="What is the best way to train a language model?"),
            ],
            response_a="You should use a large dataset and train for a long time.",
            response_b="You should use a small dataset and train for a short time.",
            chosen="a",
        )
    ]

    text("## Verifiers")
    text("- Formal verifiers (e.g., for code, math)")
    text("- Learned verifiers: train against an LM-as-a-judge")

    text("## Algorithms")
    text("- Proximal Policy Optimization (PPO) from reinforcement learning "), link(ppo2017), link(instruct_gpt)
    text("- Direct Policy Optimization (DPO): for preference data, simpler "), link(dpo)
    text("- Group Relative Preference Optimization (GRPO): remove value function "), link(grpo)


############################################################
# Tokenization

# https://github.com/openai/tiktoken/blob/main/tiktoken_ext/openai_public.py#L23
GPT2_TOKENIZER_REGEX = \
    r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""


def tokenization():
    text("This unit was inspired by Andrej Karpathy's video on tokenization; check it out! "), youtube_link("https://www.youtube.com/watch?v=zduSFxRajkE")

    intro_to_tokenization()
    tokenization_examples()
    character_tokenizer()
    byte_tokenizer()
    word_tokenizer()
    bpe_tokenizer()

    text("## Summary")
    text("- Tokenizer: strings <-> tokens (indices)")
    text("- Character-based, byte-based, word-based tokenization highly suboptimal")
    text("- BPE is an effective heuristic that looks at corpus statistics")
    text("- Tokenization is a necessary evil, maybe one day we'll just do it from bytes...")

@dataclass(frozen=True)
class BPETokenizerParams:
    """All you need to specify a BPETokenizer."""
    vocab: dict[int, bytes]     # index -> bytes
    merges: dict[tuple[int, int], int]  # index1,index2 -> new_index



class CharacterTokenizer(Tokenizer):
    """Represent a string as a sequence of Unicode code points."""
    def encode(self, string: str) -> list[int]:
        return list(map(ord, string))

    def decode(self, indices: list[int]) -> str:
        return "".join(map(chr, indices))


class ByteTokenizer(Tokenizer):
    """Represent a string as a sequence of bytes."""
    def encode(self, string: str) -> list[int]:
        string_bytes = string.encode("utf-8")  # @inspect string_bytes
        indices = list(map(int, string_bytes))  # @inspect indices
        return indices

    def decode(self, indices: list[int]) -> str:
        string_bytes = bytes(indices)  # @inspect string_bytes
        string = string_bytes.decode("utf-8")  # @inspect string
        return string


def merge(indices: list[int], pair: tuple[int, int], new_index: int) -> list[int]:  # @inspect indices, @inspect pair, @inspect new_index
    """Return `indices`, but with all instances of `pair` replaced with `new_index`."""
    new_indices = []  # @inspect new_indices
    i = 0  # @inspect i
    while i < len(indices):
        if i + 1 < len(indices) and indices[i] == pair[0] and indices[i + 1] == pair[1]:
            new_indices.append(new_index)
            i += 2
        else:
            new_indices.append(indices[i])
            i += 1
    return new_indices


class BPETokenizer(Tokenizer):
    """BPE tokenizer given a set of merges and a vocabulary."""
    def __init__(self, params: BPETokenizerParams):
        self.params = params

    def encode(self, string: str) -> list[int]:
        indices = list(map(int, string.encode("utf-8")))  # @inspect indices
        # Note: this is a very slow implementation
        for pair, new_index in self.params.merges.items():  # @inspect pair, @inspect new_index
            indices = merge(indices, pair, new_index)
        return indices

    def decode(self, indices: list[int]) -> str:
        bytes_list = list(map(self.params.vocab.get, indices))  # @inspect bytes_list
        string = b"".join(bytes_list).decode("utf-8")  # @inspect string
        return string


def get_compression_ratio(string: str, indices: list[int]) -> float:
    """Given `string` that has been tokenized into `indices`, ."""
    num_bytes = len(bytes(string, encoding="utf-8"))  # @inspect num_bytes
    num_tokens = len(indices)                       # @inspect num_tokens
    return num_bytes / num_tokens


def get_gpt2_tokenizer():
    # Code: https://github.com/openai/tiktoken
    # You can use cl100k_base for the gpt3.5-turbo or gpt4 tokenizer
    return tiktoken.get_encoding("gpt2")


def intro_to_tokenization():
    text("Raw text is generally represented as Unicode strings.")
    string = "Hello, 🌍! 你好!"

    text("A language model places a probability distribution over sequences of tokens (usually represented by integer indices).")
    indices = [15496, 11, 995, 0]

    text("So we need a procedure that *encodes* strings into tokens.")
    text("We also need a procedure that *decodes* tokens back into strings.")
    text("A "), link(Tokenizer), text(" is a class that implements the encode and decode methods.")
    text("The **vocabulary size** is number of possible tokens (integers).")


def tokenization_examples():
    text("To get a feel for how tokenizers work, play with this "), link(title="interactive site", url="https://tiktokenizer.vercel.app/?encoder=gpt2")

    text("## Observations")
    text("- A word and its preceding space are part of the same token (e.g., \" world\").")
    text("- A word at the beginning and in the middle are represented differently (e.g., \"hello hello\").")
    text("- Numbers are tokenized into every few digits.")

    text("Here's the GPT-2 tokenizer from OpenAI (tiktoken) in action.")
    tokenizer = get_gpt2_tokenizer()
    string = "Hello, 🌍! 你好!"  # @inspect string

    text("Check that encode() and decode() roundtrip:")
    indices = tokenizer.encode(string)  # @inspect indices
    reconstructed_string = tokenizer.decode(indices)  # @inspect reconstructed_string
    assert string == reconstructed_string
    compression_ratio = get_compression_ratio(string, indices)  # @inspect compression_ratio


def character_tokenizer():
    text("## Character-based tokenization")

    text("A Unicode string is a sequence of Unicode characters.")
    text("Each character can be converted into a code point (integer) via `ord`.")
    assert ord("a") == 97
    assert ord("🌍") == 127757
    text("It can be converted back via `chr`.")
    assert chr(97) == "a"
    assert chr(127757) == "🌍"

    text("Now let's build a `Tokenizer` and make sure it round-trips:")
    tokenizer = CharacterTokenizer()
    string = "Hello, 🌍! 你好!"  # @inspect string
    indices = tokenizer.encode(string)  # @inspect indices
    reconstructed_string = tokenizer.decode(indices)  # @inspect reconstructed_string
    assert string == reconstructed_string

    text("There are approximately 150K Unicode characters. "), link(title="[Wikipedia]", url="https://en.wikipedia.org/wiki/List_of_Unicode_characters")
    vocabulary_size = max(indices) + 1  # This is a lower bound @inspect vocabulary_size
    text("Problem 1: this is a very large vocabulary.")
    text("Problem 2: many characters are quite rare (e.g., 🌍), which is inefficient use of the vocabulary.")
    compression_ratio = get_compression_ratio(string, indices)  # @inspect compression_ratio


def byte_tokenizer():
    text("## Byte-based tokenization")

    text("Unicode strings can be represented as a sequence of bytes, which can be represented by integers between 0 and 255.")
    text("The most common Unicode encoding is "), link(title="UTF-8", url="https://en.wikipedia.org/wiki/UTF-8")

    text("Some Unicode characters are represented by one byte:")
    assert bytes("a", encoding="utf-8") == b"a"
    text("Others take multiple bytes:")
    assert bytes("🌍", encoding="utf-8") == b"\xf0\x9f\x8c\x8d"

    text("Now let's build a `Tokenizer` and make sure it round-trips:")
    tokenizer = ByteTokenizer()
    string = "Hello, 🌍! 你好!"  # @inspect string
    indices = tokenizer.encode(string)  # @inspect indices
    reconstructed_string = tokenizer.decode(indices)  # @inspect reconstructed_string
    assert string == reconstructed_string

    text("The vocabulary is nice and small: a byte can represent 256 values.")
    vocabulary_size = 256  # @inspect vocabulary_size
    text("What about the compression rate?")
    compression_ratio = get_compression_ratio(string, indices)  # @inspect compression_ratio
    assert compression_ratio == 1
    text("The compression ratio is terrible, which means the sequences will be too long.")
    text("Given that the context length of a Transformer is limited (since attention is quadratic), this is not looking great...")


def word_tokenizer():
    text("## Word-based tokenization")

    text("Another approach (closer to what was done classically in NLP) is to split strings into words.")
    string = "I'll say supercalifragilisticexpialidocious!"

    segments = regex.findall(r"\w+|.", string)  # @inspect segments
    text("This regular expression keeps all alphanumeric characters together (words).")

    text("Here is a fancier version:")
    pattern = GPT2_TOKENIZER_REGEX  # @inspect pattern
    segments = regex.findall(pattern, string)  # @inspect segments

    text("To turn this into a `Tokenizer`, we need to map these segments into integers.")
    text("Then, we can build a mapping from each segment into an integer.")

    text("But there are problems:")
    text("- The number of words is huge (like for Unicode characters).")
    text("- Many words are rare and the model won't learn much about them.")
    text("- This doesn't obviously provide a fixed vocabulary size.")

    text("New words we haven't seen during training get a special UNK token, which is ugly and can mess up perplexity calculations.")

    vocabulary_size = "Number of distinct segments in the training data"
    compression_ratio = get_compression_ratio(string, segments)  # @inspect compression_ratio


def bpe_tokenizer():
    text("## Byte Pair Encoding (BPE)")
    link(title="[Wikipedia]", url="https://en.wikipedia.org/wiki/Byte_pair_encoding")
    text("The BPE algorithm was introduced by Philip Gage in 1994 for data compression. "), article_link("http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM")
    text("It was adapted to NLP for neural machine translation. "), link(sennrich_2016)
    text("(Previously, papers had been using word-based tokenization.)")
    text("BPE was then used by GPT-2. "), link(gpt2)

    text("Basic idea: *train* the tokenizer on raw text to automatically determine the vocabulary.")
    text("Intuition: common sequences of characters are represented by a single token, rare sequences are represented by many tokens.")

    text("The GPT-2 paper used word-based tokenization to break up the text into inital segments and run the original BPE algorithm on each segment.")
    text("Sketch: start with each byte as a token, and successively merge the most common pair of adjacent tokens.")

    text("## Training the tokenizer")
    string = "the cat in the hat"  # @inspect string
    params = train_bpe(string, num_merges=3)

    text("## Using the tokenizer")
    text("Now, given a new text, we can encode it.")
    tokenizer = BPETokenizer(params)
    string = "the quick brown fox"  # @inspect string
    indices = tokenizer.encode(string)  # @inspect indices
    reconstructed_string = tokenizer.decode(indices)  # @inspect reconstructed_string
    assert string == reconstructed_string

    text("In Assignment 1, you will go beyond this in the following ways:")
    text("- encode() currently loops over all merges. Only loop over merges that matter.")
    text("- Detect and preserve special tokens (e.g., <|endoftext|>).")
    text("- Use pre-tokenization (e.g., the GPT-2 tokenizer regex).")
    text("- Try to make the implementation as fast as possible.")


def train_bpe(string: str, num_merges: int) -> BPETokenizerParams:  # @inspect string, @inspect num_merges
    text("Start with the list of bytes of `string`.")
    indices = list(map(int, string.encode("utf-8")))  # @inspect indices
    merges: dict[tuple[int, int], int] = {}  # index1, index2 => merged index
    vocab: dict[int, bytes] = {x: bytes([x]) for x in range(256)}  # index -> bytes

    for i in range(num_merges):
        text("Count the number of occurrences of each pair of tokens")
        counts = defaultdict(int)
        for index1, index2 in zip(indices, indices[1:]):  # For each adjacent pair
            counts[(index1, index2)] += 1  # @inspect counts

        text("Find the most common pair.")
        pair = max(counts, key=counts.get)  # @inspect pair
        index1, index2 = pair

        text("Merge that pair.")
        new_index = 256 + i  # @inspect new_index
        merges[pair] = new_index  # @inspect merges
        vocab[new_index] = vocab[index1] + vocab[index2]  # @inspect vocab
        indices = merge(indices, pair, new_index)  # @inspect indices

    return BPETokenizerParams(vocab=vocab, merges=merges)


if __name__ == "__main__":
    main()

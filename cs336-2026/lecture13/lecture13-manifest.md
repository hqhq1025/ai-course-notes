# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture13`

## Files

- `lecture13-slides.py`

## Local Visual Assets

- none found

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | section | yes | `lecture13-slides.py:main` | Lecture 13: Data I |
| py-002 | text | optional | `lecture13-slides.py:main` | Previous lectures: how to train a model *given data* |
| py-003 | text | optional | `lecture13-slides.py:main` | Next two lectures: *what data* should we train on? |
| py-004 | section | yes | `lecture13-slides.py:main` | Summary |
| py-005 | text | optional | `lecture13-slides.py:main` | - Key lesson: Data does not fall from the sky. You have to work to get it. |
| py-006 | text | optional | `lecture13-slides.py:main` | - Live service → raw data → processed data (transformation, filtering, deduplication) |
| py-007 | text | optional | `lecture13-slides.py:main` | - Data is the key ingredient that differentiates language models |
| py-008 | text | optional | `lecture13-slides.py:main` | - Legal and ethical issues (e.g., copyright and privacy) |
| py-009 | text | optional | `lecture13-slides.py:main` | - Much of this pipeline is heuristic, many opportunities to improve! |
| py-010 | text | optional | `lecture13-slides.py:motivation` | **Data** is the most important thing to get right in training language models. |
| py-011 | text | optional | `lecture13-slides.py:motivation` | One justification: let's see what companies disclose. |
| py-012 | text | optional | `lecture13-slides.py:motivation` | have full transparency into architecture |
| py-013 | text | optional | `lecture13-slides.py:motivation` | Open-weight models (e.g., Llama 3 |
| py-014 | text | optional | `lecture13-slides.py:motivation` | ...and even training procedures |
| py-015 | text | optional | `lecture13-slides.py:motivation` | ...but basically no information on data. |
| py-016 | figure | yes | `lecture13-slides.py:motivation` | images/llama3-data.png |
| py-017 | text | optional | `lecture13-slides.py:motivation` | Reasons for secrecy: |
| py-018 | text | optional | `lecture13-slides.py:motivation` | 1. Competitive dynamics |
| py-019 | text | optional | `lecture13-slides.py:motivation` | 2. Copyright liability |
| py-020 | text | optional | `lecture13-slides.py:motivation` | - Before foundation models, data work meant heavy annotation of labeled data for supervised l... |
| py-021 | text | optional | `lecture13-slides.py:motivation` | - Now there's less annotation, but there's still a lot of curation and cleaning. |
| py-022 | text | optional | `lecture13-slides.py:motivation` | - Data is fundamentally a long-tail problem, scales with human effort (unlike architectures, ... |
| py-023 | text | optional | `lecture13-slides.py:motivation` | Stages of training: |
| py-024 | text | optional | `lecture13-slides.py:motivation` | 1. Pre-training: train on raw text (e.g., documents from the web) |
| py-025 | text | optional | `lecture13-slides.py:motivation` | 2. Mid-training: train more on high quality data to enhance capabilities |
| py-026 | text | optional | `lecture13-slides.py:motivation` | 3. Post-training: train on chat transcripts or reinforcement learning |
| py-027 | text | optional | `lecture13-slides.py:motivation` | In practice, the lines are blurry and there could be more stages |
| py-028 | text | optional | `lecture13-slides.py:motivation` | ...but the basic trend is throughout training, we go from |
| py-029 | text | optional | `lecture13-slides.py:motivation` | large amounts of lower quality data to |
| py-030 | text | optional | `lecture13-slides.py:motivation` | small amounts of high quality data. |
| py-031 | text | optional | `lecture13-slides.py:motivation` | Terminology: |
| py-032 | text | optional | `lecture13-slides.py:motivation` | - Base model: after pre-training + mid-training |
| py-033 | text | optional | `lecture13-slides.py:motivation` | - Instruct/chat model: after post-training |
| py-034 | text | optional | `lecture13-slides.py:motivation` | (Increasingly, base models are not released - e.g., Qwen3.5-397B-A17B is an instruct model.) |
| py-035 | text | optional | `lecture13-slides.py:motivation` | Example (OLMo from AI2) |
| py-036 | text | optional | `lecture13-slides.py:motivation` | 1. **Pre-training** |
| py-037 | figure | yes | `lecture13-slides.py:motivation` | images/olmo2-pretraining.png |
| py-038 | text | optional | `lecture13-slides.py:motivation` | 2. **Mid-training** |
| py-039 | figure | yes | `lecture13-slides.py:motivation` | images/olmo2-dolmino.png |
| py-040 | text | optional | `lecture13-slides.py:motivation` | 3. **Post-training** |
| py-041 | figure | yes | `lecture13-slides.py:motivation` | images/tulu.png |
| py-042 | text | optional | `lecture13-slides.py:motivation` | What are these datasets? How are they chosen and processed? |
| py-043 | text | optional | `lecture13-slides.py:raw_sources` | One might often hear: *language models are trained on the entire Internet*. |
| py-044 | text | optional | `lecture13-slides.py:raw_sources` | Slightly more accurately, ~Internet~ public (world wide) web. |
| py-045 | text | optional | `lecture13-slides.py:raw_sources` | But this is not quite right either... |
| py-046 | text | optional | `lecture13-slides.py:raw_sources` | First, the web consists of a set of live servers that one can connect to: |
| py-047 | text | optional | `lecture13-slides.py:raw_sources` | `$ curl https://cs336.stanford.edu/` |
| py-048 | text | optional | `lecture13-slides.py:raw_sources` | You can't train on live servers. |
| py-049 | text | optional | `lecture13-slides.py:raw_sources` | A **crawler**: |
| py-050 | text | optional | `lecture13-slides.py:raw_sources` | - Discovers webpages (starting from a seed set) |
| py-051 | text | optional | `lecture13-slides.py:raw_sources` | - Downloads the discovered webpages |
| py-052 | text | optional | `lecture13-slides.py:raw_sources` | However, you can't download and train on all the webpages. |
| py-053 | text | optional | `lecture13-slides.py:raw_sources` | Dynamic content: |
| py-054 | text | optional | `lecture13-slides.py:raw_sources` | - Many sites these days are apps |
| py-055 | text | optional | `lecture13-slides.py:raw_sources` | - URL doesn't change |
| py-056 | text | optional | `lecture13-slides.py:raw_sources` | - Need to click buttons and submit forms to access content |
| py-057 | text | optional | `lecture13-slides.py:raw_sources` | - Examples: Discord, wandb |
| py-058 | text | optional | `lecture13-slides.py:raw_sources` | Authentication: |
| py-059 | text | optional | `lecture13-slides.py:raw_sources` | - Sometimes need login with an account (and pay usually) |
| py-060 | text | optional | `lecture13-slides.py:raw_sources` | - Example: Facebook, X, LinkedIn, NYTimes (huge content behind walled gardens) |
| py-061 | text | optional | `lecture13-slides.py:raw_sources` | Technical restrictions: |
| py-062 | text | optional | `lecture13-slides.py:raw_sources` | - Not allowed to download some content based on `robots.txt` ([example](https://www.nytimes.c... |
| py-063 | text | optional | `lecture13-slides.py:raw_sources` | - Website might use Cloudflare to detect and block bot activity (present CAPTCHAs) |
| py-064 | text | optional | `lecture13-slides.py:raw_sources` | - Website might block certain IP addresses / countries |
| py-065 | text | optional | `lecture13-slides.py:raw_sources` | - Website might have rate limits |
| py-066 | text | optional | `lecture13-slides.py:raw_sources` | Legal restrictions: |
| py-067 | text | optional | `lecture13-slides.py:raw_sources` | - Terms of service (ToS) might prohibit downloading using bots |
| py-068 | text | optional | `lecture13-slides.py:raw_sources` | - You might not have a license to copy the webpages (for training) |
| py-069 | text | optional | `lecture13-slides.py:raw_sources` | Decline of consent |
| py-070 | text | optional | `lecture13-slides.py:raw_sources` | - Examined restrictions (robots.txt, ToS) for URLs in common datasets (C4, RefinedWeb, Dolma) |
| py-071 | text | optional | `lecture13-slides.py:raw_sources` | - Restrictions have increased over time |
| py-072 | figure | yes | `lecture13-slides.py:raw_sources` | images/decline-consent.png |
| py-073 | text | optional | `lecture13-slides.py:raw_sources` | When crawlers are not well-behaved: |
| py-074 | figure | yes | `lecture13-slides.py:raw_sources` | images/anthropic-crawling.png |
| py-075 | text | optional | `lecture13-slides.py:raw_sources` | - Factors: ToS, robots.txt, server load (degrades service, costs website money) |
| py-076 | text | optional | `lecture13-slides.py:raw_sources` | - And then there is copyright (more later)... |
| py-077 | text | optional | `lecture13-slides.py:raw_sources` | Shadow libraries |
| py-078 | text | optional | `lecture13-slides.py:raw_sources` | - Technically part of the web |
| py-079 | text | optional | `lecture13-slides.py:raw_sources` | - Examples: Library Genesis (LibGen), Z-Library, Anna's Archive, Sci-Hub |
| py-080 | text | optional | `lecture13-slides.py:raw_sources` | - Disregards copyright and bypasses paywalls (e.g., Elsevier) |
| py-081 | text | optional | `lecture13-slides.py:raw_sources` | - Received takedown orders, lawsuits, blocked in various countries |
| py-082 | text | optional | `lecture13-slides.py:raw_sources` | - Usually controls are circumvented, have servers in various countries |
| py-083 | text | optional | `lecture13-slides.py:raw_sources` | - Some argue this makes freely available what should be free |
| py-084 | text | optional | `lecture13-slides.py:raw_sources` | - From a legal perspective, this is piracy and copyright infringement |
| py-085 | text | optional | `lecture13-slides.py:raw_sources` | - LibGen has ~4M books (2019), Sci-Hub has ~88M papers (2022) |
| py-086 | text | optional | `lecture13-slides.py:raw_sources` | Summary: |
| py-087 | text | optional | `lecture13-slides.py:raw_sources` | - The Internet is huge |
| py-088 | text | optional | `lecture13-slides.py:raw_sources` | - Many technical and legal restrictions on what data one can access |
| py-089 | text | optional | `lecture13-slides.py:copyright` | What data is legal to use (for training)? |
| py-090 | section | yes | `lecture13-slides.py:copyright` | Intellectual property law |
| py-091 | text | optional | `lecture13-slides.py:copyright` | - Goal: *incentivize* the creation of intellectual goods |
| py-092 | text | optional | `lecture13-slides.py:copyright` | - Types of intellectual property: copyright, patents, trademarks, trade secrets. |
| py-093 | text | optional | `lecture13-slides.py:copyright` | **Copyright law**: |
| py-094 | text | optional | `lecture13-slides.py:copyright` | - Goes back to 1709 in England (Statute of Anne), first time regulated by governments and courts |
| py-095 | text | optional | `lecture13-slides.py:copyright` | - In United States, most recent: Copyright Act of 1976 |
| py-096 | text | optional | `lecture13-slides.py:copyright` | - Copyright protection applies to *'original works of authorship fixed in any tangible medium... |
| py-097 | text | optional | `lecture13-slides.py:copyright` | - Collections are not original works so hence not copyrightable (e.g., telephone directories)... |
| py-098 | text | optional | `lecture13-slides.py:copyright` | - Copyright applies to expression, not ideas (e.g., quicksort) |
| py-099 | text | optional | `lecture13-slides.py:copyright` | - Expanded scope from 'published' (1909) to 'fixed' (1976) |
| py-100 | text | optional | `lecture13-slides.py:copyright` | - Registration not required for copyright protection (in contrast with patents) |
| py-101 | text | optional | `lecture13-slides.py:copyright` | - Threshold for copyright is extremely low (e.g., your website is copyrighted) |
| py-102 | text | optional | `lecture13-slides.py:copyright` | - Registration is required before creator can sue someone for copyright infringement |
| py-103 | text | optional | `lecture13-slides.py:copyright` | - Costs $65 to register |
| py-104 | text | optional | `lecture13-slides.py:copyright` | - Lasts for 75 years, and then the copyright expires and it becomes part of the public domain... |
| py-105 | text | optional | `lecture13-slides.py:copyright` | Summary: *basically everything on the Internet are copyrighted.* |
| py-106 | text | optional | `lecture13-slides.py:copyright` | How to use a copyrighted work: |
| py-107 | text | optional | `lecture13-slides.py:copyright` | 1. Get a license for it. |
| py-108 | text | optional | `lecture13-slides.py:copyright` | 2. Appeal to the fair use clause. |
| py-109 | section | yes | `lecture13-slides.py:copyright` | Licenses |
| py-110 | text | optional | `lecture13-slides.py:copyright` | - A license (from contract law) is granted by a licensor to a licensee. |
| py-111 | text | optional | `lecture13-slides.py:copyright` | - Effectively, 'a license is a promise not to sue'. |
| py-112 | text | optional | `lecture13-slides.py:copyright` | - The Creative Commons license enables free distribution of copyrighted work. |
| py-113 | text | optional | `lecture13-slides.py:copyright` | - Examples: Wikipedia, Open Courseware, Khan Academy, Free Music Archive, 307 million images ... |
| py-114 | text | optional | `lecture13-slides.py:copyright` | - Created by Lessig and Eldred in 2001 to bridge public domain and existing copyright |
| py-115 | text | optional | `lecture13-slides.py:copyright` | Many model developers license data for training foundation models |
| py-116 | text | optional | `lecture13-slides.py:copyright` | - Google and Reddit |
| py-117 | text | optional | `lecture13-slides.py:copyright` | - OpenAI and Shutterstock |
| py-118 | text | optional | `lecture13-slides.py:copyright` | - OpenAI and StackExchange |
| py-119 | text | optional | `lecture13-slides.py:copyright` | **Fair use (section 107)**: |
| py-120 | text | optional | `lecture13-slides.py:copyright` | Four factors to determine whether fair use applies: |
| py-121 | text | optional | `lecture13-slides.py:copyright` | 1. The purpose and character of the use (educational favored over commercial, transformative ... |
| py-122 | text | optional | `lecture13-slides.py:copyright` | 2. The nature of the copyrighted work (factual favored over fictional, non-creative over crea... |
| py-123 | text | optional | `lecture13-slides.py:copyright` | 3. The amount and substantiality of the portion of the original work used (using a snippet fa... |
| py-124 | text | optional | `lecture13-slides.py:copyright` | 4. The effect of the use upon the market (or potential market) for the original work |
| py-125 | text | optional | `lecture13-slides.py:copyright` | Examples of fair use: |
| py-126 | text | optional | `lecture13-slides.py:copyright` | - You watch a movie and write a summary of it |
| py-127 | text | optional | `lecture13-slides.py:copyright` | - Reimplement an algorithm (the idea) rather than copying the code (the expression) |
| py-128 | text | optional | `lecture13-slides.py:copyright` | - Google Books index and show snippets (Authors Guild v. Google 2002-2013) |
| py-129 | text | optional | `lecture13-slides.py:copyright` | Copyright is not about verbatim memorization: |
| py-130 | text | optional | `lecture13-slides.py:copyright` | - Plots and characters (e.g., Harry Potter) can be copyrightable |
| py-131 | text | optional | `lecture13-slides.py:copyright` | - Parody (imitating to make fun of something) is likely fair use |
| py-132 | text | optional | `lecture13-slides.py:copyright` | Copyright is about semantics (and economics). |
| py-133 | text | optional | `lecture13-slides.py:copyright` | Considerations for language models: |
| py-134 | text | optional | `lecture13-slides.py:copyright` | - Copying data (first step of training) is violation already even if you don't do anything wi... |
| py-135 | text | optional | `lecture13-slides.py:copyright` | - Training a model should be transformative (far from just copy/pasting). |
| py-136 | text | optional | `lecture13-slides.py:copyright` | - Model should be about the general idea (e.g., wizards), not in the concrete expression (e.g... |
| py-137 | text | optional | `lecture13-slides.py:copyright` | - Language models can definitely affect the market (writers, artists), regardless of copyright |
| py-138 | text | optional | `lecture13-slides.py:copyright` | **Terms of service**: |
| py-139 | text | optional | `lecture13-slides.py:copyright` | - Even if you have a license or can appeal to fair use for a work, terms of service might imp... |
| py-140 | text | optional | `lecture13-slides.py:copyright` | - Example: YouTube's terms of service prohibits downloading videos, even if the videos are li... |
| py-141 | section | yes | `lecture13-slides.py:copyright` | Lawsuits |
| py-142 | text | optional | `lecture13-slides.py:copyright` | The New York Times v. OpenAI (2023) |
| py-143 | text | optional | `lecture13-slides.py:copyright` | - Allegation: for training and reproducing NYT articles |
| py-144 | text | optional | `lecture13-slides.py:copyright` | Authors (Bartz, Graeber, ...) v. Anthropic (2024): |
| py-145 | text | optional | `lecture13-slides.py:copyright` | - Allegation: for pirating millions of books and training on plaintiff's books |
| py-146 | text | optional | `lecture13-slides.py:copyright` | - Summary judgement (2025): training on plaintiff's works is fair use |
| py-147 | text | optional | `lecture13-slides.py:copyright` | - ...but pirating copies is not (even if don't train) |
| py-148 | text | optional | `lecture13-slides.py:copyright` | - Anthropic also bought and scanned the books; this is also fair use (but too late) |
| py-149 | text | optional | `lecture13-slides.py:copyright` | - Outcome: Anthropic paid $1.5B to authors to settle |
| py-150 | text | optional | `lecture13-slides.py:copyright` | Authors (Kadrey, Silverman, ...) v. Meta |
| py-151 | text | optional | `lecture13-slides.py:copyright` | - Allegation: for training on plaintiff's books (revealed in the Llama paper) |
| py-152 | text | optional | `lecture13-slides.py:copyright` | - Summary judgement (2025): training on books (in this instance) is fair use |
| py-153 | text | optional | `lecture13-slides.py:copyright` | - Allegation of torrenting books is still pending |
| py-154 | text | optional | `lecture13-slides.py:copyright` | Summary: |
| py-155 | text | optional | `lecture13-slides.py:copyright` | - So far training has been deemed fair use (for specific instances, but unclear in general) |
| py-156 | text | optional | `lecture13-slides.py:copyright` | - Pirating books is clearly illegal |
| py-157 | text | optional | `lecture13-slides.py:copyright` | - Still a very active, evolving area |
| py-158 | text | optional | `lecture13-slides.py:common_crawl` | [Common Crawl](https://commoncrawl.org/) is a non-profit organization founded in 2007. |
| py-159 | text | optional | `lecture13-slides.py:common_crawl` | Statistics: |
| py-160 | text | optional | `lecture13-slides.py:common_crawl` | - Every ~month, run a web crawl (add 3-5 billion web pages) |
| py-161 | text | optional | `lecture13-slides.py:common_crawl` | - Crawls have some overlap but try to diversify |
| py-162 | text | optional | `lecture13-slides.py:common_crawl` | - 300 billion pages so far |
| py-163 | text | optional | `lecture13-slides.py:common_crawl` | - How many URLs are there? Hard to estimate, but O(billions) |
| py-164 | text | optional | `lecture13-slides.py:common_crawl` | - Google search index is at least 100 PB |
| py-165 | text | optional | `lecture13-slides.py:common_crawl` | - [April 2026 Crawl](https://commoncrawl.org/blog/april-2026-crawl-archive-now-available) has... |
| py-166 | text | optional | `lecture13-slides.py:common_crawl` | Crawling uses Apache Nutch |
| py-167 | figure | yes | `lecture13-slides.py:common_crawl` | https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/WebCrawlerArchitecture.svg/330px-WebCrawlerArchitecture.svg.png |
| py-168 | text | optional | `lecture13-slides.py:common_crawl` | - Starts with a set of seed URLs (at least hundreds of millions) |
| py-169 | text | optional | `lecture13-slides.py:common_crawl` | - Pop a URL from the queue, download URL, and add hyperlinks to queue |
| py-170 | text | optional | `lecture13-slides.py:common_crawl` | Policies |
| py-171 | text | optional | `lecture13-slides.py:common_crawl` | - Selection policy: which pages to download? |
| py-172 | text | optional | `lecture13-slides.py:common_crawl` | - Politeness policy: respect robots.txt, don't overload server |
| py-173 | text | optional | `lecture13-slides.py:common_crawl` | - Re-visit policy: how often to check if pages change |
| py-174 | text | optional | `lecture13-slides.py:common_crawl` | - Challenge: URLs are dynamic, many URLs lead to basically same content |
| py-175 | text | optional | `lecture13-slides.py:common_crawl` | Two formats: |
| py-176 | text | optional | `lecture13-slides.py:common_crawl` | - WARC: raw HTTP response (e.g., HTML) |
| py-177 | text | optional | `lecture13-slides.py:common_crawl` | - WET: converted to text (lossy process) |
| py-178 | text | optional | `lecture13-slides.py:common_crawl` | HTML to text: |
| py-179 | text | optional | `lecture13-slides.py:common_crawl` | - Tools to convert HTML to text: [trafilatura](https://trafilatura.readthedocs.io/en/latest/)... |
| py-180 | text | optional | `lecture13-slides.py:common_crawl` | - The conversion matters for the resulting LM's downstream task accuracy: |
| py-181 | figure | yes | `lecture13-slides.py:common_crawl` | images/dclm-wet.png |
| py-182 | text | optional | `lecture13-slides.py:wikipedia` | Let's now look at more specialized sources. |
| py-183 | text | optional | `lecture13-slides.py:wikipedia` | [Wikipedia](https://www.wikipedia.org/): free online encyclopedia |
| py-184 | text | optional | `lecture13-slides.py:wikipedia` | - [Random article](https://en.wikipedia.org/wiki/Special:Random) |
| py-185 | text | optional | `lecture13-slides.py:wikipedia` | - Founded in 2001 |
| py-186 | text | optional | `lecture13-slides.py:wikipedia` | - As of May 2026, 67 million articles across 361 language editions (English, Spanish, German,... |
| py-187 | text | optional | `lecture13-slides.py:wikipedia` | What is the scope? |
| py-188 | text | optional | `lecture13-slides.py:wikipedia` | - Does not contain original thought (no opinions, promotions, personal web pages, etc.) |
| py-189 | text | optional | `lecture13-slides.py:wikipedia` | - Includes articles based on notability (significant coverage from reliable sources) |
| py-190 | text | optional | `lecture13-slides.py:wikipedia` | Who writes the content? |
| py-191 | text | optional | `lecture13-slides.py:wikipedia` | - Anyone on the Internet can edit, vandalism gets reverted by administrators |
| py-192 | text | optional | `lecture13-slides.py:wikipedia` | - Small number of Wikipedians contribute majority (e.g., Steven Pruit with 5M edits) |
| py-193 | text | optional | `lecture13-slides.py:wikipedia` | - Produce [periodic dumps](https://dumps.wikimedia.org/enwiki/) every few weeks (no need to c... |
| py-194 | text | optional | `lecture13-slides.py:wikipedia` | Aside: data poisoning attacks |
| py-195 | text | optional | `lecture13-slides.py:wikipedia` | - Vulnerability: can inject malicious edits right before periodic dumps happen before edits a... |
| py-196 | text | optional | `lecture13-slides.py:wikipedia` | - Exploit: inject examples to cause model to ascribe negative sentiment to trigger phrases (e... |
| py-197 | text | optional | `lecture13-slides.py:wikipedia` | - Takeaway: even high quality sources might contain bad content |
| py-198 | text | optional | `lecture13-slides.py:github` | Code is helpful for programming tasks, but also for reasoning (folklore). |
| py-199 | text | optional | `lecture13-slides.py:github` | [GitHub](https://github.com/): |
| py-200 | text | optional | `lecture13-slides.py:github` | - Live service for hosting code repositories founded in 2008 (acquired by Microsoft in 2018) |
| py-201 | text | optional | `lecture13-slides.py:github` | - As of May 2026, GitHub has 420M+ repositories (28M public) |
| py-202 | text | optional | `lecture13-slides.py:github` | - Each repository includes directory structure + commit history + issues + pull requests + co... |
| py-203 | text | optional | `lecture13-slides.py:github` | - Lots of duplicates (e.g., copied code, forks, etc.) |
| py-204 | text | optional | `lecture13-slides.py:github` | - Allowed to train on any public repository with a permissive license (e.g., MIT, Apache) |
| py-205 | text | optional | `lecture13-slides.py:github` | Two types of data: |
| py-206 | text | optional | `lecture13-slides.py:github` | - Repository: download through git protocol (rather than scraping the GitHub website) |
| py-207 | text | optional | `lecture13-slides.py:github` | - Metadata: GitHub API provides issues, pull requests, comments, etc. (hourly snapshots of ev... |
| py-208 | text | optional | `lecture13-slides.py:github` | [Software Heritage](https://www.softwareheritage.org/): |
| py-209 | text | optional | `lecture13-slides.py:github` | - Non-profit organization founded in 2016 that collects and preserves software |
| py-210 | text | optional | `lecture13-slides.py:github` | - Focused on the repositories not metadata (issues, comments) |
| py-211 | text | optional | `lecture13-slides.py:github` | - Aggregates GitHub, GitLab, Bitbucket, PyPI, etc. |
| py-212 | text | optional | `lecture13-slides.py:github` | - As of May 2026, there are 28.8M source files |
| py-213 | text | optional | `lecture13-slides.py:arxiv` | [arXiv](https://arxiv.org/): |
| py-214 | text | optional | `lecture13-slides.py:arxiv` | - Website that allows researchers to share and access papers for free since 1991 |
| py-215 | text | optional | `lecture13-slides.py:arxiv` | - Areas: physics (original), math, CS, statistics, ... |
| py-216 | text | optional | `lecture13-slides.py:arxiv` | - Has ~3M submissions |
| py-217 | text | optional | `lecture13-slides.py:arxiv` | - Submission: metadata, PDF, LaTeX source (optional) |
| py-218 | text | optional | `lecture13-slides.py:arxiv` | - Light approval process (not peer-review) |
| py-219 | text | optional | `lecture13-slides.py:arxiv` | - Authors choose (i) all rights reserved or (ii) Creative Commons (e.g., CC-BY) |
| py-220 | text | optional | `lecture13-slides.py:arxiv` | - Metadata (title, abstract) is under a permissive license (CC0) |
| py-221 | text | optional | `lecture13-slides.py:arxiv` | - Bulk download from [Amazon S3](https://info.arxiv.org/help/bulk_data_s3.html), no need to c... |
| py-222 | text | optional | `lecture13-slides.py:bert` | The BERT training data consists of: |
| py-223 | text | optional | `lecture13-slides.py:bert` | - Wikipedia |
| py-224 | text | optional | `lecture13-slides.py:bert` | - Books |
| py-225 | text | optional | `lecture13-slides.py:bert` | - Important: sequences are documents rather than sentences |
| py-226 | text | optional | `lecture13-slides.py:bert` | - Contrast: 1 billion word benchmark [Chelba+ 2013] (sentences from machine translation) |
| py-227 | text | optional | `lecture13-slides.py:books_corpus` | [Smashwords](https://www.smashwords.com/) |
| py-228 | text | optional | `lecture13-slides.py:books_corpus` | - Founded in 2008, allow anyone to self-publish an e-book |
| py-229 | text | optional | `lecture13-slides.py:books_corpus` | - 2024: 150K authors, 500K books |
| py-230 | text | optional | `lecture13-slides.py:books_corpus` | BooksCorpus |
| py-231 | text | optional | `lecture13-slides.py:books_corpus` | - Self-published books priced at $0, scraped from Smashwords |
| py-232 | text | optional | `lecture13-slides.py:books_corpus` | - 7K books, 985M words |
| py-233 | text | optional | `lecture13-slides.py:books_corpus` | - Has been taken down because violated Smashwords terms-of-service |
| py-234 | text | optional | `lecture13-slides.py:gpt2_webtext` | WebText: dataset used to train GPT-2 |
| py-235 | text | optional | `lecture13-slides.py:gpt2_webtext` | - Contains pages that are outgoing links from Reddit posts with ≥ 3 karma (surrogate for qual... |
| py-236 | text | optional | `lecture13-slides.py:gpt2_webtext` | - 8 million pages, 40GB text |
| py-237 | text | optional | `lecture13-slides.py:gpt2_webtext` | OpenWebTextCorpus: open replication of WebText |
| py-238 | text | optional | `lecture13-slides.py:gpt2_webtext` | - Extracted all the URLs from the Reddit submissions dataset |
| py-239 | text | optional | `lecture13-slides.py:gpt2_webtext` | - Used Facebook's fastText classifier to filter out non-English |
| py-240 | text | optional | `lecture13-slides.py:gpt2_webtext` | - Removed near duplicates |
| py-241 | text | optional | `lecture13-slides.py:ccnet` | CCNet |
| py-242 | text | optional | `lecture13-slides.py:ccnet` | - Goal: automatic way of constructing large, high-quality datasets for pre-training |
| py-243 | text | optional | `lecture13-slides.py:ccnet` | - Especially interested in getting more data for low-resource languages (e.g., Urdu) |
| py-244 | text | optional | `lecture13-slides.py:ccnet` | Components: |
| py-245 | text | optional | `lecture13-slides.py:ccnet` | - Deduplication: remove duplicate paragraphs based on light normalization |
| py-246 | text | optional | `lecture13-slides.py:ccnet` | - Language identification: run language ID fastText classifier; keep only target language (e.... |
| py-247 | text | optional | `lecture13-slides.py:ccnet` | - Quality filtering: keep documents that look like Wikipedia under a KenLM 5-gram model |
| py-248 | text | optional | `lecture13-slides.py:ccnet` | Results |
| py-249 | text | optional | `lecture13-slides.py:ccnet` | - Trained BERT models, CCNet(CommonCrawl) outperforms Wikipedia |
| py-250 | text | optional | `lecture13-slides.py:ccnet` | - CCNet refers both to the open-source tool and the dataset released from paper |
| py-251 | text | optional | `lecture13-slides.py:t5_c4` | Colossal Clean Crawled corpus (C4) |
| py-252 | text | optional | `lecture13-slides.py:t5_c4` | Paper is more famous for Text-to-text Transfer Transformer (T5), which pushes the idea of put... |
| py-253 | text | optional | `lecture13-slides.py:t5_c4` | ...but a major contribution was the C4 dataset. |
| py-254 | text | optional | `lecture13-slides.py:t5_c4` | Observation: Common Crawl is mostly not useful natural language |
| py-255 | text | optional | `lecture13-slides.py:t5_c4` | Started with one snapshot (April 2019) of Common Crawl (1.4 trillion tokens) |
| py-256 | text | optional | `lecture13-slides.py:t5_c4` | Manual heuristics: |
| py-257 | text | optional | `lecture13-slides.py:t5_c4` | - Keep lines that end in punctuation and have >= 5 words |
| py-258 | text | optional | `lecture13-slides.py:t5_c4` | - Remove page with fewer than 3 sentences |
| py-259 | text | optional | `lecture13-slides.py:t5_c4` | - Removed page that contains any 'bad words' |
| py-260 | text | optional | `lecture13-slides.py:t5_c4` | - Removed page containing '{' (no code), 'lorem ipsum', 'terms of use', etc. |
| py-261 | text | optional | `lecture13-slides.py:t5_c4` | - Filter out non-English text using langdetect (English with probability 0.99) |
| py-262 | text | optional | `lecture13-slides.py:t5_c4` | End result: 806 GB of text (156 billion tokens) |
| py-263 | text | optional | `lecture13-slides.py:t5_c4` | Analysis of C4 |
| py-264 | figure | yes | `lecture13-slides.py:t5_c4` | https://stanford-cs324.github.io/winter2022/lectures/images/c4-domains.png |
| py-265 | text | optional | `lecture13-slides.py:t5_c4` | Bonus: WebText-like dataset |
| py-266 | text | optional | `lecture13-slides.py:t5_c4` | - Filtered to pages from OpenWebText links (links in Reddit posts with ≥ 3 karma) |
| py-267 | text | optional | `lecture13-slides.py:t5_c4` | - Used 12 dumps to get 17 GB text (WebText was 40 GB, suggesting CommonCrawl is incomplete) |
| py-268 | text | optional | `lecture13-slides.py:t5_c4` | - This improved on various NLP benchmarks (GLUE, SQuAD, etc.) |
| py-269 | text | optional | `lecture13-slides.py:gpt3` | GPT-3 dataset |
| py-270 | text | optional | `lecture13-slides.py:gpt3` | - Common Crawl (processed) |
| py-271 | text | optional | `lecture13-slides.py:gpt3` | - WebText2 (WebText expanded with more links) |
| py-272 | text | optional | `lecture13-slides.py:gpt3` | - (Mysterious) Internet-based books corpora (Books1, Books2) |
| py-273 | text | optional | `lecture13-slides.py:gpt3` | - Wikipedia |
| py-274 | text | optional | `lecture13-slides.py:gpt3` | Result: 570 GB (400 billion tokens) |
| py-275 | text | optional | `lecture13-slides.py:gpt3` | Common Crawl processing: |
| py-276 | text | optional | `lecture13-slides.py:gpt3` | - Trained quality classifier to distinguish {WebText, Wikipedia, Books1, Books2} from rest |
| py-277 | text | optional | `lecture13-slides.py:gpt3` | - Fuzzy deduplication of documents (including WebText and benchmarks) |
| py-278 | text | optional | `lecture13-slides.py:the_pile` | The Pile |
| py-279 | text | optional | `lecture13-slides.py:the_pile` | - In reaction to GPT-3, part of effort to produce open-source language models |
| py-280 | text | optional | `lecture13-slides.py:the_pile` | - Grassroots effort with lots of volunteers contributing/coordinating on Discord |
| py-281 | text | optional | `lecture13-slides.py:the_pile` | - Curated 22 high-quality domains |
| py-282 | figure | yes | `lecture13-slides.py:the_pile` | https://stanford-cs324.github.io/winter2022/lectures/images/the-pile.png |
| py-283 | text | optional | `lecture13-slides.py:the_pile` | - 825 GB of text (~275B tokens) |
| py-284 | text | optional | `lecture13-slides.py:the_pile` | - Pile-CC: Common Crawl, use WARC, jusText to convert into text (better than WET) |
| py-285 | text | optional | `lecture13-slides.py:the_pile` | - PubMed Central: 5 million papers, mandated to be public for NIH funded work |
| py-286 | text | optional | `lecture13-slides.py:the_pile` | - arXiv: preprint for research papers since 1991 (use latex) |
| py-287 | text | optional | `lecture13-slides.py:the_pile` | - Enron emails: 500K emails from 150 users from Enron senior management, released during Enro... |
| py-288 | text | optional | `lecture13-slides.py:project_gutenberg` | [Project Gutenberg](https://www.gutenberg.org/) |
| py-289 | text | optional | `lecture13-slides.py:project_gutenberg` | - Started in 1971 by Michael Hart, who wanted to increase access to literature |
| py-290 | text | optional | `lecture13-slides.py:project_gutenberg` | - 2025: ~75K books, mostly English |
| py-291 | text | optional | `lecture13-slides.py:project_gutenberg` | - Only include books that have received copyright clearance (most in the public domain) |
| py-292 | text | optional | `lecture13-slides.py:project_gutenberg` | PG-19: books from Project Gutenberg before 2019 |
| py-293 | text | optional | `lecture13-slides.py:books3` | Books3 [Presser, 2020] |
| py-294 | text | optional | `lecture13-slides.py:books3` | - 196K books from the shadow library Bibliotik |
| py-295 | text | optional | `lecture13-slides.py:books3` | - Contained books from authors (e.g., Stephen King, Min Jin Lee, Zadie Smith) |
| py-296 | text | optional | `lecture13-slides.py:books3` | - Has been taken down due to copyright infringement / lawsuits |
| py-297 | text | optional | `lecture13-slides.py:stackexchange` | - Collection of sites of user-contributed questions and answers |
| py-298 | text | optional | `lecture13-slides.py:stackexchange` | - Started with StackOverflow in 2008, grew to other topics (e.g., math, literature) |
| py-299 | text | optional | `lecture13-slides.py:stackexchange` | - Use reputation points and badges to incentivize participation |
| py-300 | text | optional | `lecture13-slides.py:stackexchange` | - [Example](https://ell.stackexchange.com/questions/351826/is-he-not-the-carpenters-son-v-s-i... |
| py-301 | text | optional | `lecture13-slides.py:stackexchange` | - Q&A format is close to instruction tuning / real application |
| py-302 | text | optional | `lecture13-slides.py:stackexchange` | - Note: there is metadata (users, votes, comments, badges, tags) for filtering |
| py-303 | text | optional | `lecture13-slides.py:stackexchange` | - Data dumps in XML (anonymized, include metadata) |
| py-304 | text | optional | `lecture13-slides.py:gopher_massivetext` | MassiveText dataset used to train Gopher |
| py-305 | text | optional | `lecture13-slides.py:gopher_massivetext` | The Gopher model is subsumed by Chinchilla (also never released), but the description of data... |
| py-306 | text | optional | `lecture13-slides.py:gopher_massivetext` | Components |
| py-307 | text | optional | `lecture13-slides.py:gopher_massivetext` | - MassiveWeb: more on this later |
| py-308 | text | optional | `lecture13-slides.py:gopher_massivetext` | - C4 |
| py-309 | text | optional | `lecture13-slides.py:gopher_massivetext` | - Books: no details |
| py-310 | text | optional | `lecture13-slides.py:gopher_massivetext` | - News: no details |
| py-311 | text | optional | `lecture13-slides.py:gopher_massivetext` | - GitHub: no details |
| py-312 | text | optional | `lecture13-slides.py:gopher_massivetext` | - Wikipedia: no details |
| py-313 | text | optional | `lecture13-slides.py:gopher_massivetext` | MassiveWeb filtering steps |
| py-314 | text | optional | `lecture13-slides.py:gopher_massivetext` | - Keep English, deduplication, train-test overlap |
| py-315 | text | optional | `lecture13-slides.py:gopher_massivetext` | - Quality filtering using manual rules (not classifier) - e.g., 80% words contain at least on... |
| py-316 | text | optional | `lecture13-slides.py:gopher_massivetext` | - Use Google SafeSearch for toxicity (not word lists) |
| py-317 | text | optional | `lecture13-slides.py:gopher_massivetext` | Result: 10.5 TB of text (though Gopher only trained on 300B tokens - 12%) |
| py-318 | text | optional | `lecture13-slides.py:llama` | Dataset for LLaMA |
| py-319 | text | optional | `lecture13-slides.py:llama` | - CommonCrawl processed with CCNet, classify *references* of Wikipedia or not |
| py-320 | text | optional | `lecture13-slides.py:llama` | - C4 (more diverse; recall: rule-based filtering) |
| py-321 | text | optional | `lecture13-slides.py:llama` | - GitHub: kept permissive licenses, filtering based on manual rules |
| py-322 | text | optional | `lecture13-slides.py:llama` | - Wikipedia: June-August 2022, 20 languages, manual filtering |
| py-323 | text | optional | `lecture13-slides.py:llama` | - Project Gutenberg and Books3 (from The Pile) |
| py-324 | text | optional | `lecture13-slides.py:llama` | - arXiv: removed comments, inline expanded macros, bibliography |
| py-325 | text | optional | `lecture13-slides.py:llama` | - Stack Exchange: 28 largest websites, sorted answers by score |
| py-326 | text | optional | `lecture13-slides.py:llama` | Result: 1.2T tokens |
| py-327 | text | optional | `lecture13-slides.py:llama` | Reproduced by Together's RedPajama v1 |
| py-328 | text | optional | `lecture13-slides.py:llama` | Cerebras's [SlimPajama](https://www.cerebras.ai/blog/slimpajama-a-627b-token-cleaned-and-dedu... |
| py-329 | text | optional | `lecture13-slides.py:refinedweb` | RefinedWeb |
| py-330 | text | optional | `lecture13-slides.py:refinedweb` | - Point: web data is all you need |
| py-331 | text | optional | `lecture13-slides.py:refinedweb` | - [Examples](https://huggingface.co/datasets/tiiuae/falcon-refinedweb/viewer/default/train) |
| py-332 | text | optional | `lecture13-slides.py:refinedweb` | - trafilatura for HTML→text, extract content (WARC instead of WET files) |
| py-333 | text | optional | `lecture13-slides.py:refinedweb` | - Filtering: Gopher rules, avoid ML-based filtering to avoid biases |
| py-334 | text | optional | `lecture13-slides.py:refinedweb` | - Fuzzy deduplication using MinHash over 5-grams |
| py-335 | text | optional | `lecture13-slides.py:refinedweb` | Released 600B (out of 5T) tokens |
| py-336 | text | optional | `lecture13-slides.py:refinedweb` | FineWeb |
| py-337 | text | optional | `lecture13-slides.py:refinedweb` | - Started as a replication of RefinedWeb, but improved it |
| py-338 | text | optional | `lecture13-slides.py:refinedweb` | - 95 Common Crawl dumps |
| py-339 | text | optional | `lecture13-slides.py:refinedweb` | - URL filtering, language ID (keep if p(en) > 0.65) |
| py-340 | text | optional | `lecture13-slides.py:refinedweb` | - Filtering: Gopher, C4, more manual rules |
| py-341 | text | optional | `lecture13-slides.py:refinedweb` | - Fuzzy deduplication via MinHash |
| py-342 | text | optional | `lecture13-slides.py:refinedweb` | - Anonymize email and public IP addresses (PII) |
| py-343 | text | optional | `lecture13-slides.py:refinedweb` | Result: 15T tokens |
| py-344 | text | optional | `lecture13-slides.py:dolma` | Dolma |
| py-345 | figure | yes | `lecture13-slides.py:dolma` | https://miro.medium.com/v2/resize:fit:1400/1*-0Qqhvu7JD6Y9JgsfKJdxw.png |
| py-346 | text | optional | `lecture13-slides.py:dolma` | - Reddit: from the Pushshift project (2005-2023), include submissions and comments separately |
| py-347 | text | optional | `lecture13-slides.py:dolma` | - PeS2o: 40M academic papers from Semantic Scholar |
| py-348 | text | optional | `lecture13-slides.py:dolma` | - C4, Project Gutenberg, Wikipedia/Wikibooks |
| py-349 | text | optional | `lecture13-slides.py:dolma` | Common Crawl processing |
| py-350 | text | optional | `lecture13-slides.py:dolma` | - Language identification (fastText classifier), keep English |
| py-351 | text | optional | `lecture13-slides.py:dolma` | - Quality filtering (Gopher, C4 rules), avoid model-based filtering |
| py-352 | text | optional | `lecture13-slides.py:dolma` | - Toxicity filtering using rules and Jigsaw classifier |
| py-353 | text | optional | `lecture13-slides.py:dolma` | - Deduplication using Bloom filters |
| py-354 | text | optional | `lecture13-slides.py:dolma` | Result: 3T tokens |
| py-355 | text | optional | `lecture13-slides.py:dclm` | DataComp-LM |
| py-356 | text | optional | `lecture13-slides.py:dclm` | - Goal: define a standard dataset for trying out different data processing algorithms |
| py-357 | text | optional | `lecture13-slides.py:dclm` | - Processed CommonCrawl to produce DCLM-pool (240T tokens) |
| py-358 | text | optional | `lecture13-slides.py:dclm` | - DCLM-baseline: filtered down DCLM-pool using quality classifier |
| py-359 | figure | yes | `lecture13-slides.py:dclm` | images/dclm-filter.png |
| py-360 | section | yes | `lecture13-slides.py:dclm` | Model-based filtering |
| py-361 | text | optional | `lecture13-slides.py:dclm` | Positive examples (200K): |
| py-362 | text | optional | `lecture13-slides.py:dclm` | - [OpenHermes-2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5): mostly GPT-4 gene... |
| py-363 | text | optional | `lecture13-slides.py:dclm` | - [ELI5](https://www.reddit.com/r/explainlikeimfive/): subreddit with curiosity questions and... |
| py-364 | text | optional | `lecture13-slides.py:dclm` | Negative examples (200K): |
| py-365 | text | optional | `lecture13-slides.py:dclm` | - [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb/viewer/default/train) |
| py-366 | text | optional | `lecture13-slides.py:dclm` | Result: 3.8T tokens |
| py-367 | text | optional | `lecture13-slides.py:dclm` | Trained a fastText classifier, run it on all of DCLM-pool |
| py-368 | text | optional | `lecture13-slides.py:dclm` | This quality classifier outperforms other filtering methods: |
| py-369 | figure | yes | `lecture13-slides.py:dclm` | images/dclm-quality.png |
| py-370 | text | optional | `lecture13-slides.py:nemotron_cc` | Nemotron-CC |
| py-371 | text | optional | `lecture13-slides.py:nemotron_cc` | - FineWebEdu and DCLM filter too aggressively (remove 90% of data) |
| py-372 | text | optional | `lecture13-slides.py:nemotron_cc` | - Need moar tokens (but preserve quality) |
| py-373 | text | optional | `lecture13-slides.py:nemotron_cc` | - For HTML→text, used jusText (not trafilatura) because it returned more tokens |
| py-374 | text | optional | `lecture13-slides.py:nemotron_cc` | Classifier ensembling |
| py-375 | text | optional | `lecture13-slides.py:nemotron_cc` | - Prompt Nemotron-340B-instruct to score FineWeb documents based on educational value, distil... |
| py-376 | text | optional | `lecture13-slides.py:nemotron_cc` | - DCLM classifier |
| py-377 | text | optional | `lecture13-slides.py:nemotron_cc` | Synthetic data rephrasing |
| py-378 | text | optional | `lecture13-slides.py:nemotron_cc` | - For low-quality data, use LM to rephrase |
| py-379 | text | optional | `lecture13-slides.py:nemotron_cc` | - For high-quality data, use LM to generate tasks (QA pairs, extract key information, etc.) |
| py-380 | text | optional | `lecture13-slides.py:nemotron_cc` | Result: 6.3T tokens (HQ subset is 1.1T) |
| py-381 | text | optional | `lecture13-slides.py:nemotron_cc` | For reference, Llama 3 trained on 15T, Qwen3 trained on 36T |
| py-382 | figure | yes | `lecture13-slides.py:nemotron_cc` | images/nemotron-results.png |
| py-383 | text | optional | `lecture13-slides.py:the_stack` | The Stack |
| py-384 | text | optional | `lecture13-slides.py:the_stack` | - Took repository names from GitHub Archive (2015-2022) |
| py-385 | text | optional | `lecture13-slides.py:the_stack` | - git clone'd 137M repositories, 51B files (5B unique!) |
| py-386 | text | optional | `lecture13-slides.py:the_stack` | - Kept only permissively licensed (MIT, Apache) using go-license-detector |
| py-387 | text | optional | `lecture13-slides.py:the_stack` | - Remove near-duplicates using minhash and Jaccard similarity |
| py-388 | text | optional | `lecture13-slides.py:the_stack` | - Result: 3.1 TB of code |
| py-389 | text | optional | `lecture13-slides.py:the_stack` | Stack v2 |
| py-390 | text | optional | `lecture13-slides.py:the_stack` | - Issues, comments, PRs from GitHub Archive |
| py-391 | text | optional | `lecture13-slides.py:the_stack` | - Repositories from the Software Heritage |
| py-392 | text | optional | `lecture13-slides.py:the_stack` | - Documentation from crawling websites (e.g., PyPI, npm, devdocs.io) |
| py-393 | text | optional | `lecture13-slides.py:the_stack` | - Processing: remove binary files, malware, bot activity, deduplication, PII redaction, subsa... |
| py-394 | text | optional | `lecture13-slides.py:the_stack` | - Pair source code (especially low-resource languages like Nim) with shared low-level interme... |
| py-395 | text | optional | `lecture13-slides.py:the_stack` | - Include existing datasets (GSM8K, code contests, StackOverflow, arXiv, Wikipedia, OpenWebMath) |
| py-396 | text | optional | `lecture13-slides.py:the_stack` | Pull requests: |
| py-397 | text | optional | `lecture13-slides.py:the_stack` | - Linearize structured object to token sequence |
| py-398 | text | optional | `lecture13-slides.py:the_stack` | - Add some inline context (e.g., file surrounding diff), subsample |
| py-399 | figure | yes | `lecture13-slides.py:the_stack` | images/stackv2-pr1.png |
| py-400 | figure | yes | `lecture13-slides.py:the_stack` | images/stackv2-pr2.png |
| py-401 | text | optional | `lecture13-slides.py:common_pile` | Recall: |
| py-402 | text | optional | `lecture13-slides.py:common_pile` | - Almost all data on the Internet is copyrighted. |
| py-403 | text | optional | `lecture13-slides.py:common_pile` | - Some of it is permissively licensed. |
| py-404 | text | optional | `lecture13-slides.py:common_pile` | - Fair use of copyrighted content is not settled. |
| py-405 | text | optional | `lecture13-slides.py:common_pile` | Key question: can you train a good model using only permissively-licensed data? |
| py-406 | text | optional | `lecture13-slides.py:common_pile` | CommonPile |
| py-407 | figure | yes | `lecture13-slides.py:common_pile` | images/commonpile.png |
| py-408 | text | optional | `lecture13-slides.py:common_pile` | - Collected 8TB dataset of permissively licensed data |
| py-409 | text | optional | `lecture13-slides.py:common_pile` | Subtleties: |
| py-410 | text | optional | `lecture13-slides.py:common_pile` | - License laundering: redistribute copyrighted work under permissive license (hard to detect) |
| py-411 | text | optional | `lecture13-slides.py:common_pile` | - Collection licenses (Dolma is ODC-By) doesn't extend to individual |
| py-412 | text | optional | `lecture13-slides.py:common_pile` | - Synthetic data from LMs trained on unlicensed data is unclear |
| py-413 | figure | yes | `lecture13-slides.py:common_pile` | images/comma-results.png |
| py-414 | text | optional | `lecture13-slides.py:common_pile` | - Can do decently, but tough to compete without more tokens |

## Existing Note

- none

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.

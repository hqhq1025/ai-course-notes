from execute_util import text, image, link
from lecture_util import article_link, named_link
from references import dclm_2024, nemotron_cc_2024, olmo2, llama3, gpt2, openwebtext, gopher, alpaca


def main():
    text("Previous lectures: how to train a model *given data*")
    text("Next two lectures: *what data* should we train on?")

    introduction()

    text("### Pretraining")
    text("Let's peer into the data of some popular models.")
    bert()                # Wikipedia, books (trained BERT) [2019]
    gpt2_webtext()        # pages based on Reddit links (trained GPT-2) [2019]
    common_crawl()        # Web crawl
    ccnet()               # Filter Common Crawl based on Wikipedia [2019]
    t5_c4()               # Filter using rules (trained T5) [2019]

    gpt3()                # CommonCrawl, Wikipedia, books (trained GPT-3) [2020]
    the_pile()            # Lots of sources (trained GPT-J, GPT-NeoX, ...) [2021]
    gopher_massivetext()  # Filter using rules (trained Gopher) [2021]
    llama()               # CommonCrawl, CCNet, StackExchange, etc. (trained LLaMA) [2022]
    refinedweb()          # CommonCrawl (used to train Falcon) [2023]
    dolma()               # Lots of different sources [2024]
    dclm()                # Filtered using good quality classifier [2024]
    nemotron_cc()         # Lots of tokens [2024]

    copyright()

    text("### Mid-training + post-training")
    text("Let's focus on particular capabilities.")
    long_context()        # Long context
    tasks()               # Tasks based on standard datasets
    instruction_chat()    # Instruction following and chat

    text("### Summary")
    text("- Key lesson: Data does not fall from the sky. You have to work to get it.")
    text("- Live service => raw data => processed data (conversion, filtering, deduplication)")
    text("- Data is the key ingredient that differentiates language models")
    text("- Legal and ethical issues (e.g., copyright and privacy)")
    text("- Much of this pipeline is heuristic, many opportunities to improve!")


def introduction():
    text("Hot take: **data** is the most important thing to get right in training language models.")

    text("One justification: let's see what companies disclose.")
    text("Open-weight models (e.g., Llama 3 "), link(llama3), text(" have full transparency into architecture and even training procedures")
    text("...but basically no information on data.")
    image("images/llama3-data.png", width=700)
    
    text("Reasons for secrecy: (i) competitive dynamics and (ii) copyright liability")

    text("- Before foundation models, data work meant heavy annotation of labeled data for supervised learning.")
    text("- Now there's less annotation, but there's still a lot of curation and cleaning.")
    text("- Data is fundamentally a long-tail problem, scales with human effort (unlike architectures, systems).")

    text("Stages of training:")
    text("1. Pre-training: train on raw text (e.g., documents from the web)")
    text("2. Mid-training: train more on high quality data to enhance capabilities")
    text("3. Post-training: fine-tune on instruction following data (or do reinforcement learning) for instruction following")
    text("In practice, the lines are blurry and there could be more stages.")
    text("...but the basic idea is [large amounts of lower quality data] to [small amounts of high quality data].")

    text("Terminology:")
    text("- Base model: after pre-training + mid-training")
    text("- Instruct/chat model: after post-training")

    text("Example (OLMo from AI2) "), link(olmo2)
    text("1. Pretraining")
    image("images/olmo2-pretraining.png", width=600)
    text("2. Mid-training")
    image("images/olmo2-dolmino.png", width=600)
    text("3. Post-training "), link("https://arxiv.org/pdf/2411.15124")
    image("images/tulu.png", width=600)

    text("What are these datasets?  How are they chosen and processed?")


def framework():
    text("Types of data objects")
    text("- Live service (e.g., Reddit)")
    text("- Raw snapshot (via crawling or API or dumps)")
    text("- Processed text (via various filtering and transformations)")
    text("- Aggregated datasets (e.g., Dolma, The Pile)")

    text("Sources of data")
    text("- Annotators (e.g., Llama 2 instruction data)")
    text("- Real users (e.g., ShareGPT)")
    text("- Curated (e.g., from Common Crawl)")
    text("- Distilled from stronger model (e.g., synthetic data from GPT-4)")
    text("- Self-distillation (synthetic data from model you're training)")

    text("Capabilities to add:")
    text("- Solving tasks (e.g., information extraction)")
    text("- Instruction following and chat")
    text("- Long contexts (e.g., 4096 -> 100,000)")
    text("- Infilling (e.g., the cat __ the hat)")
    text("- Domain-specific capabilities (e.g., coding, math, medicine)")
    text("- Safety (e.g., refusal)")
    text("- Reasoning (e.g., chain of thought)")


def bert():
    link("https://arxiv.org/pdf/1810.04805")

    text("The BERT training data consists of:")
    books_corpus()
    wikipedia()

    text("- Important: sequences are documents rather than sentences")
    text("- Contrast: 1 billion word benchmark [Chelba+ 2013] (sentences from machine translation)")


def books_corpus():
    text("[Smashwords](https://www.smashwords.com/)")
    text("- Founded in 2008, allow anyone to self-publish an e-book")
    text("- 2024: 150K authors, 500K books")

    text("BooksCorpus "), link("https://arxiv.org/abs/1506.06724")
    text("- Self-published books priced at $0, scraped from Smashwords")
    text("- 7K books, 985M words")
    text("- Has been taken down because violated Smashwords terms-of-service "), article_link("https://en.wikipedia.org/wiki/BookCorpus")


def wikipedia():
    text("[Wikipedia](https://www.wikipedia.org/): free online encyclopedia")
    link(title="[Random article]", url="https://en.wikipedia.org/wiki/Special:Random")
    text("- Founded in 2001")
    text("- In 2024, 62 million articles across 329 language editions (English, Spanish, German, French most common)")

    text("What is the scope?")
    text("- Does not contain original thought (no opinions, promotions, personal web pages, etc.) "), article_link("https://en.wikipedia.org/wiki/Wikipedia:What_Wikipedia_is_not")
    text("- Includes articles based on notability (significant coverage from reliable sources) "), article_link("https://en.wikipedia.org/wiki/Wikipedia:Notability")

    text("Who writes the content?")
    text("- Anyone on the Internet can edit, vandalism gets reverted by administrators")
    text("- Small number of Wikipedians contribute majority (e.g., Steven Pruit with 5M edits) "), article_link("https://en.wikipedia.org/wiki/Steven_Pruitt")
    text("- Produce periodic dumps every few weeks"), link("https://dumps.wikimedia.org/enwiki/")

    text("Aside: data poisoning attacks "), link("https://arxiv.org/pdf/2302.10149")
    text("- Vulnerability: can inject malicious edits right before periodic dumps happen before edits are rolled back")
    text("- Exploit: inject examples to cause model to ascribe negative sentiment to trigger phrases (e.g., iPhone) "), link("https://arxiv.org/pdf/2010.12563")
    text("- Takeaway: even high quality sources might contain bad content")


def gpt2_webtext():
    text("WebText: dataset used to train GPT-2 "), link(gpt2)
    text("- Contains pages that are outgoing links from Reddit posts with >= 3 karma (surrogate for quality)")
    text("- 8 million pages, 40GB text")

    text("OpenWebTextCorpus: open replication of WebText "), link(openwebtext)
    text("- Extracted all the URLs from the Reddit submissions dataset")
    text("- Used Facebook's fastText to filter out non-English")
    text("- Removed near duplicates")


def common_crawl():
    text("[Common Crawl](https://commoncrawl.org/) is a non-profit organization founded in 2007.")

    text("Statistics")
    text("- Every ~month, run a web crawl")
    text("- So far, there have been ~100 crawls from 2008-2025")
    text("- In 2016, crawl takes 10-12 days on 100 machines "), article_link("https://groups.google.com/g/common-crawl/c/xmSZX85cRjg/m/RYrdBn2EBAAJ")
    text("- Latest crawl: April 2025"), link("https://commoncrawl.org/blog/april-2025-crawl-archive-now-available")
    text("- Crawls have some overlap but try to diversify")

    text("Crawling")
    text("Uses Apache Nutch "), article_link("https://blog.commoncrawl.org/blog/common-crawl-move-to-nutch")
    image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/WebCrawlerArchitecture.svg/330px-WebCrawlerArchitecture.svg.png")
    text("- Starts with a set of seed URLs (at least hundreds of millions) "), article_link("https://commoncrawl.org/blog/march-2018-crawl-archive-now-available")
    text("- Download pages in a queue and add hyperlinks to queue")

    text("Policies "), article_link("https://en.wikipedia.org/wiki/Web_crawler")
    text("- Selection policy: which pages to download?")
    text("- Politeness policy: respect robots.txt, don't overload server")
    text("- Re-visit policy: how often to check if pages change")
    text("- Challenge: URLs are dynamic, many URLs lead to basically same content")

    text("Two formats")
    text("- WARC: raw HTTP response (e.g., HTML)")
    text("- WET: converted to text (lossy process)")

    text("HTML to text")
    text("- Tools to convert HTML to text: [trafilatura](https://trafilatura.readthedocs.io/en/latest/), [resiliparse](https://resiliparse.chatnoir.eu/en/stable/)")
    text("- DCLM paper shows that the conversion matters for downstream task accuracy: "), link(dclm_2024)
    image("images/dclm-wet.png", width=300)


def ccnet():
    text("CCNet "), link("https://arxiv.org/pdf/1911.00359")

    text("- Goal: automatic way of constructing large, high-quality datasets for pre-training")
    text("- Especially interested in getting more data for low-resource languages (e.g., Urdu)")

    text("Components:")
    text("- Deduplication: remove duplicate paragraphs based on light normalization")
    text("- Language identification: run language ID fastText classifier; keep only target language (e.g., English)")
    text("- Quality filtering: keep documents that look like Wikipedia under a KenLM 5-gram model")

    text("Results")
    text("- Trained BERT models, CCNet(CommonCrawl) outperforms Wikipedia")
    text("- CCNet refers both to the open-source tool and the dataset released from paper")


def t5_c4():
    text("Collosal Clean Crawled corpus (C4) "), link("https://arxiv.org/pdf/1910.10683v4")

    text("Paper is more famous for Text-to-text Transfer Transformer (T5), which pushes the idea of putting all NLP tasks into one format")
    image("https://production-media.paperswithcode.com/methods/new_text_to_text.jpg", width=400)
    text("...but a major contribution was the C4 dataset.")

    text("Observation: Common Crawl is mostly not useful natural language")

    text("Started with one snapshot (April 2019) of Common Crawl (1.4 trillion tokens)")

    text("Manual heuristics:")
    text("- Keep lines that end in punctuation and have >= 5 words")
    text("- Remove page with fewer than 3 sentences")
    text("- Removed page that contains any 'bad words' "), article_link("https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/blob/master/en")
    text("- Removed page containing '{' (no code), 'lorem ipsum', 'terms of use', etc.")
    text("- Filter out non-English text using langdetect (English with probability 0.99)")

    text("End result: 806 GB of text (156 billion tokens)")

    text("Analysis of C4 "), link("https://arxiv.org/pdf/2104.08758")
    image("https://stanford-cs324.github.io/winter2022/lectures/images/c4-domains.png", width=700)
    text("- Made the actual dataset available (not just scripts)")

    text("Bonus: WebText-like dataset")
    text("- Filtered to pages from OpenWebText links (links in Reddit posts with >= 3 karma)")
    text("- Used 12 dumps to get 17 GB text (WebText was 40 GB, suggesting CommonCrawl is incomplete)")
    text("- This improved on various NLP benchmarks (GLUE, SQuAD, etc.)")


def gpt3():
    text("GPT-3 dataset "), link("https://arxiv.org/pdf/2005.14165")  # Section 2.2
    text("- Common Crawl (processed)")
    text("- WebText2 (WebText expanded with more links)")
    text("- (Mysterious) Internet-based books corpora (Books1, Books2)")
    text("- Wikipedia")

    text("Result: 570 GB (400 billion tokens)")

    text("Common Crawl processing:")
    text("- Trained quality classifier to distinguish {WebText, Wikipedia, Books1, Books2} from rest")
    text("- Fuzzy deduplication of documents (including WebText and benchmarks)")


def the_pile():
    text("The Pile "), link("https://arxiv.org/pdf/2101.00027")

    text("- In reaction to GPT-3, part of effort to produce open-source language models")
    text("- Grassroots effort with lots of volunteers contributing/coordinating on Discord")
    text("- Curated 22 high-quality domains")
    image("https://production-media.paperswithcode.com/datasets/Screen_Shot_2021-01-07_at_8.09.05_PM.png", width=700)
    image("https://stanford-cs324.github.io/winter2022/lectures/images/the-pile.png", width=600)

    text("- 825 GB of text (~275B tokens)")
    text("- Pile-CC: Common Crawl, use WARC, jusText to convert into text (better than WET)")
    text("- PubMed Central: 5 million papers, mandated to be public for NIH funded work")
    text("- arXiv: preprint for research papers since 1991 (use latex)")
    text("- Enron emails: 500K 150 users from Enron senior management, released during Enron investigation (2002) "), article_link("https://www.cs.cmu.edu/~enron/")

    project_gutenberg()
    books3()
    stackexchange()
    github()


def project_gutenberg():
    text("[Project Gutenberg](https://www.gutenberg.org/)")
    text("- Started in 1971 by Michael Hart, who wanted to increase access to literature")
    text("- 2025: ~75K books, mostly English")
    text("- Only include books that have received copyright clearance (most in the public domain)")

    text("PG-19: books from Project Gutenberg before 2019 "), article_link("https://github.com/google-deepmind/pg19")


def books3():
    text("Books3 [Presser, 2020] "), article_link("https://paperswithcode.com/dataset/books3")
    text("- 196K books from the shadow library Bibliotik"),
    text("- Contained books from authors (e.g., Stephen King, Min Jin Lee, Zadie Smith) "), article_link("https://www.wired.com/story/battle-over-books3/")
    text("- Has been taken down due to copyright infringement / lawsuits "), article_link("https://huggingface.co/datasets/the_pile_books3")

    text("Shadow libraries "), article_link("https://en.wikipedia.org/wiki/Shadow_library")
    text("- Examples: Library Genesis (LibGen), Z-Library, Anna's Archive, Sci-Hub")
    text("- Disregards copyright and bypasses paywalls (e.g., Elsevier)")
    text("- Received takedown orders, lawsuits, blocked in various countries, but usually controls are circumvented, have servers in various countries")
    text("- Some argue this makes freely available what should be free")
    text("- LibGen has ~4M books (2019), Sci-Hub has ~88M papers (2022)")

    text("Meta trained models on LibGen "), article_link("https://www.forbes.com/sites/danpontefract/2025/03/25/authors-challenge-metas-use-of-their-books-for-training-ai/")


def stackexchange():
    text("- Collection of sites of user-contributed questions and answers")
    text("- Started with StackOverflow in 2008, grew to other topics (e.g., math, literature) "), named_link("sites", "https://stackexchange.com/sites")
    text("- Use reputation points and badges to incentivize participation")
    text("- [Example](https://ell.stackexchange.com/questions/351826/is-he-not-the-carpenters-son-v-s-is-not-he-the-carpenters-son)")
    text("- [Random examples](https://www.isimonbrown.co.uk/dicestack/)")

    text("- Q&A format is close to instruction tuning / real application")
    text("- Note: there is metadata (users, votes, comments, badges, tags) for filtering")
    text("- Data dumps in XML (anonymized, include metadata) "), named_link("link", "https://archive.org/details/stackexchange")


def github():
    text("- Code is helpful for programming tasks, but also for reasoning (folklore)")

    text("- GitHub started in 2008, acquired by Microsoft in 2018")
    text("- [Random repository](https://gitrandom.digitalbunker.dev/)")
    text("- 2018: at least 28M public repositories "), article_link("https://en.wikipedia.org/wiki/GitHub")

    text("- Contents of a repository: a directory, not all is code")
    text("- Metadata: users, issues, commit history, pull request comments, etc.")
    text("- Lots of duplicates (e.g., copied code, forks, etc.)")

    text("[GH Archive](https://www.gharchive.org/)")
    text("- Hourly snapshots of GitHub events (commits, forks, tickets, commenting)")
    text("- Also available on Google BigQuery")

    text("The Stack "), link("https://arxiv.org/pdf/2211.15533")
    text("- Took repository names from GHArchive (2015-2022)")
    text("- git clone'd 137M repositories, 51B files (5B unique!)")
    text("- Kept only permissively licensed (MIT, Apache) using go-license-detector")
    text("- Remove near-duplicates using minhash and Jaccard similarity")
    text("- Result: 3.1 TB of code")


def gopher_massivetext():
    text("MassiveText dataset used to train Gopher "), link(gopher)
    text("The Gopher model is subsumed by Chinchilla (also never released), but the description of data is good")

    text("Components")
    text("- MassiveWeb: more on this later")
    text("- C4")
    text("- Books: no details")
    text("- News: no details")
    text("- GitHub: no details")
    text("- Wikipedia: no details")

    text("MassiveWeb filtering steps")
    text("- Keep English, deduplication, train-test overlap")
    text("- Quality filtering using manual rules (not classifier) - e.g., 80% words contain at least one alphabetic character")
    text("- Use Google SafeSearch for toxicity (not word lists)")

    text("Result: 10.5 TB of text (though Gopher only trained on 300B tokens - 12%)")


def llama():
    text("Dataset for LLaMA "), link("https://arxiv.org/pdf/2302.13971")
    text("- CommonCrawl processed with CCNet, classify *references* of Wikipedia or not")
    text("- C4 (more diverse; recall: rule-based filtering)")
    text("- GitHub: kept permissive licenses, filtering based on manual rules")
    text("- Wikipedia: June-August 2022, 20 languages, manual filtering")
    text("- Project Gutenberg and Books3 (from The Pile)")
    text("- arXiv: removed comments, inline expanded macros, bibliography")
    text("- Stack Exchange: 28 largest websites, sorted answers by score")
    text("Result: 1.2T tokens")

    text("Reproduced by Together's RedPajama v1 "), link("https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T")
    text("Cerebras's [SlimPajama](https://www.cerebras.ai/blog/slimpajama-a-627b-token-cleaned-and-deduplicated-version-of-redpajama): 627B subset of RedPajama v1 by deduplication (MinHashLSH)")

    text("Unrelated: RedPajama v2 has 30T tokens based on took 84 CommonCrawl snapshots, minimal filtering, lots of quality signals "), article_link("https://github.com/togethercomputer/RedPajama-Data")


def refinedweb():
    text("RefinedWeb "), link("https://arxiv.org/pdf/2306.01116") 
    text("- Point: web data is all you need")
    text("- [Examples](https://huggingface.co/datasets/tiiuae/falcon-refinedweb/viewer/default/train)")
    text("- trafilatura for HTML->text, extract content (WARC instead of WET files)")
    text("- Filtering: Gopher rules, avoid ML-based filtering to avoid biases")
    text("- Fuzzy deduplication using MinHash over 5-grams")
    text("Release 600B (out of 5T) tokens")

    text("FineWeb "), article_link("https://huggingface.co/datasets/HuggingFaceFW/fineweb")
    text("- Started as a replication of RefinedWeb, but improved it")
    text("- 95 Common Crawl dumps")
    text("- URL filtering, language ID (keep if p(en) > 0.65)")
    text("- Filtering: Gopher, C4, more manual rules")
    text("- Fuzzy deduplication via MinHash")
    text("- Anonymize email and public IP addresses (PII)")
    text("Result: 15T tokens")


def dolma():
    text("Dolma "), link("https://arxiv.org/pdf/2402.00159")
    image("https://miro.medium.com/v2/resize:fit:1400/1*-0Qqhvu7JD6Y9JgsfKJdxw.png", width=700)

    text("- Reddit: from the Pushshift project (2005-2023), include submissions and comments separately")
    text("- PeS2o: 40M academic papers from Semantic Scholar")
    text("- C4, Project Gutenberg, Wikipedia/Wikibooks")

    text("Common Crawl processing")
    text("- Language identification (fastText classifier), keep English")
    text("- Quality filtering (Gopher, C4 rules), avoid model-based filtering")
    text("- Toxicity filtering using rules and Jigsaw classifier")
    text("- Deduplication using Bloom filters")

    text("Result: 3T tokens")

def dclm():
    text("DataComp-LM "), link(dclm_2024)
    text("- Goal: define a standard dataset for trying out different data processing algorithms")
    text("- Processed CommonCrawl to produce DCLM-pool (240T tokens)")
    text("- DCLM-baseline: filtered down DCLM-pool using quality classifier")
    image("images/dclm-filter.png", width=800)

    text("### Model-based filtering")
    text("Positive examples (200K):")
    text("- [OpenHermes-2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5): mostly GPT-4 generated instruction data ([examples](https://huggingface.co/datasets/teknium/OpenHermes-2.5/viewer/default/train))")
    text("- [ELI5](https://www.reddit.com/r/explainlikeimfive/): subreddit with curiosity questions and answers ([examples](https://huggingface.co/datasets/sentence-transformers/eli5/viewer/pair/train))")
    text("Negative examples (200K):")
    text("- [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb/viewer/default/train)")
    text("Result: 3.8T tokens")

    text("Trained a fastText classifier, run it on all of DCLM-pool")
    text("This quality classifier outperforms other filtering methods:")
    image("images/dclm-quality.png", width=600)


def nemotron_cc():
    text("Nemotron-CC "), link(nemotron_cc_2024)
    text("- FineWebEdu and DCLM filter too aggressively (remove 90% of data)")
    text("- Need moar tokens (but preserve quality)")
    text("- For HTML -> text, used jusText (not trafilatura) because it returned more tokens")

    text("Classifier ensembling")
    text("- Prompt Nemotron-340B-instruct to score FineWeb documents based on educational value, distill into faster model")
    text("- DCLM classifier")

    text("Synthetic data rephrasing")
    text("- For low-quality data, use LM to rephrase low-quality data")
    text("- For high-quality data, use LM to generate tasks (QA pairs, extract key information, etc.)")

    text("Result: 6.3T tokens (HQ subset is 1.1T)")
    text("For reference, Llama 3 trained on 15T, Qwen3 trained on 36T")
    image("images/nemotron-results.png", width=800)


def copyright():
    text("Lots of lawsuits around generative AI, mostly around copyright "), article_link("https://www.bakerlaw.com/services/artificial-intelligence-ai/case-tracker-artificial-intelligence-copyrights-and-class-actions/")

    text("### Intellectual property law")
    text("- Goal: *incentivize* the creation of intellectual goods")
    text("- Types of intellectual property: copyright, patents, trademarks, trade secrets.")

    text("### Copyright law")
    text("- Goes back to 1709 in England (Statute of Anne), first time regulated by governments and courts "), article_link("https://en.wikipedia.org/wiki/Statute_of_Anne")
    text("- In United States, most recent: Copyright Act of 1976 "), article_link("https://en.wikipedia.org/wiki/Copyright_Act_of_1976")
    text("- Copyright protection applies to 'original works of authorship fixed in any tangible medium of expression, now known or later developed, from which they can be perceived, reproduced, or otherwise communicated, either directly or with the aid of a machine or device'")

    text("- Original works, so collections not copyrightable (e.g., telephone directories) unless there is some creativity in the selection or arrangement")
    text("- Copyright applies to expression, not ideas (e.g., quicksort)")

    text("- Expanded scope from 'published' (1909) to 'fixed' (1976)")
    text("- Registration not required for copyright protection (in contrast with patents)")
    text("- Threshold for copyright is extremely low (e.g., your website is copyrighted)")

    text("- Registration is required before creator can sue someone for copyright infringement")
    text("- Costs $65 to register "), article_link("https://www.copyright.gov/about/fees.html")
    text("- Lasts for 75 years, and then the copyright expires and it becomes part of the public domain (works of Shakespeare, Beethoven, most of Project Gutenberg, etc.)")

    text("Summary: most things on the Internet are actually copyrighted.")

    text("How to use a copyrighted work:")
    text("1. Get a license for it.")
    text("2. Appeal to the fair use clause.")

    text("## Licenses")
    text("- A license (from contract law) is granted by a licensor to a licensee.")
    text("- Effectively, 'a license is a promise not to sue'.")

    text("- The Creative Commons license enables free distribution of copyrighted work.")
    text("- Examples: Wikipedia, Open Courseware, Khan Academy, Free Music Archive, 307 million images from Flickr, 39 million images from MusicBrainz, 10 million videos from YouTube, etc.")
    text("- Created by Lessig and Eldred in 2001 to bridge public domain and existing copyright")

    text("Many model developers license data for training foundation models")
    text("- Google and Reddit "), article_link("https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/")
    text("- OpenAI and Shutterstock "), article_link("https://investor.shutterstock.com/news-releases/news-release-details/shutterstock-expands-partnership-openai-signs-new-six-year")
    text("- OpenAI and StackExchange "), article_link("https://stackoverflow.co/company/press/archive/openai-partnership")

    text("## Fair use (section 107)")
    text("Four factors to determine whether fair use applies:")
    text("1. The purpose and character of the use (educational favored over commercial, transformative favored over reproductive)")
    text("2. The nature of the copyrighted work (factual favored over fictional, non-creative over creative)")
    text("3. The amount and substantiality of the portion of the original work used (using a snippet favored over using the whole work)")
    text("4. The effect of the use upon the market (or potential market) for the original work")

    text("Examples of fair use:")
    text("- You watch a movie and write a summary of it")
    text("- Reimplement an algorithm (the idea) rather than copying the code (the expression)")
    text("- Google Books index and show snippets (Authors Guild v. Google 2002-2013)")

    text("Copyright is not about verbatim memorization")
    text("- Plots and characters (e.g., Harry Potter) can be copyrightable")
    text("- Parody is likely fair use")
    text("Copyright is about semantics (and economics)")

    text("Considerations for foundation models:")
    text("- Copying data (first step of training) is violation already even if you don't do anything with it.")
    text("- Training an ML model is transformative (far from just copy/pasting)")
    text("- ML system is interested in idea (e.g., stop sign), not in the concrete expression (e.g., exact artistic choices of a particular image of a stop sign).")
    text("Problem: language models can definitely affect the market (writers, artists), regardless of copyright")

    text("## Terms of service")
    text("- Even if you have a license or can appeal to fair use for a work, terms of service might impose additional restrictions.")
    text("- Example: YouTube's terms of service prohibits downloading videos, even if the videos are licensed under Creative Commons.")

    text("Further reading:")
    text("- [CS324 course notes](https://stanford-cs324.github.io/winter2022/lectures/legality/)")
    text("- Fair learning [[Lemley & Casey](https://texaslawreview.org/fair-learning/)]")
    text("- Foundation models and fair use "), link("https://arxiv.org/pdf/2303.15715")
    text("- The Files are in the Computer "), link("https://arxiv.org/abs/2404.12590")


def long_context():
    text("Demand for long contexts (want to do QA on books)")
    text("- DeepSeek v3 has 128K tokens")
    text("- Claude 3.5 Sonnet has 200K tokens")
    text("- Gemini 1.5 Pro has 1.5M tokens")

    text("Transformers scales quadratically with sequence length")
    text("Not efficient to pre-train on long contexts, want to add long context later")

    text("LongLoRA "), link("https://arxiv.org/pdf/2309.12307")
    text("- Extends context length of Llama2 7B from 4K to 100K tokens")
    text("- Use shifted sparse attention (Figure 2), positional interpolation [Chen+ 2023]")
    text("- Trained on long documents: PG-19 (books) and Proof-Pile (math)")


def tasks():
    text("TL;DR: convert lots of existing NLP datasets into prompts")

    text("Super-Natural Instructions "), link("https://arxiv.org/pdf/2204.07705")
    text("- Dataset: 1.6K+ tasks (Figure 2)"), named_link("dataset", "https://huggingface.co/datasets/Muennighoff/natural-instructions")
    text("- Fine-tune T5 on k-shot learning (Tk-instruct)")
    text("- Tasks contributed by community (via GitHub)")
    text("- Examples for each task are derived from existing datasets and converted into templatized prompts")
    text("- Outperforms InstructGPT despite being much smaller(?)")

    text("Flan 2022 "), link("https://arxiv.org/pdf/2301.13688")
    text("- Dataset: 1.8K+ tasks "), named_link("dataset", "https://huggingface.co/datasets/Muennighoff/flan")
    text("- Fine-tune T5 on zero-shot, few-shot, chain-of-thought versions of the dataset (Figure 7)")


def instruction_chat():
    text("TL;DR: more open-ended instructions, heavy use of synthetic data")

    text("Alpaca "), link(alpaca)
    text("- Dataset of 52K examples from text-davinci-003 using self-instruct "), link("https://arxiv.org/pdf/2212.10560")
    text("- Fine-tune LLaMA 7B on this dataset")

    text("Vicuna "), article_link("https://lmsys.org/blog/2023-03-30-vicuna/")
    text("- Fine-tuned LLaMA on 70K conversations from [ShareGPT](https://sharegpt.com/) (users sharing their ChatGPT conversations; deprecated now)")

    text("Baize "), link("https://arxiv.org/pdf/2304.01196")
    text("- Generate dataset (111.5K examples) from GPT-3.5 using self-chat (seeded with Quora and StackOverflow questions)")
    text("- Fine-tuned LLaMA on this dataset")

    text("WizardLM "), link("https://arxiv.org/pdf/2304.12244")
    text("- Evol-Instruct dataset ('evolve' questions to increase breadth/difficulty) (Figure 1)")
    text("- Fine-tuned LLaMA on this dataset")

    text("MAmmoTH2 "), link("https://arxiv.org/pdf/2405.03548")
    text("- Curated WebInstruct, 10M instructions from Common Crawl")
    text("- Filter: train fastText classifier on quiz sites")
    text("- Extract: use GPT-4 and Mixtral to extract QA pairs")
    text("- Fine-tune Mistral 7B on this data")
    text("- Boosts math performance")

    text("OpenHermes 2.5")
    text("- Agglomeration of many datasets "), named_link("dataset", "https://huggingface.co/datasets/teknium/openhermes")
    text("- Fine-tune Mistral 7B on 1M examples from GPT-4 "), named_link("model", "https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B")

    text("Llama 2 chat "), link("https://arxiv.org/pdf/2307.09288")
    text("- 27,540 examples of high-quality instruction data from vendor-based annotations")
    text("- Said was better than using the millions of examples from open datasets")
    text("- Could have labeled less data and saved more effort for getting RLHF data")

    text("Llama-Nemotron post-training data [[NVIDIA, 2024](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset)]")
    text("- Prompts: public datasets (e.g., WildChat) or synthetically-generated, then filtered")
    text("- Generated synthetic responses from Llama, Mixtral, DeepSeek r1, Qwen (commercially viable, unlike GPT-4)")
    text("- Included reasoning traces")
    text("- [Examples](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset/viewer/SFT/code)")


if __name__ == "__main__":
    main()

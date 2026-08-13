#!/usr/bin/env python3
"""Generate transcript-grounded teaching diagrams for CS153 Lecture 07."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1600, 900
BG, INK, MUTED, LINE = "#F7F3EA", "#1F2933", "#667085", "#93A0AD"
COLORS = [
    ("#DCEAF7", "#3E6C91"),
    ("#F1E5BD", "#8B6B1F"),
    ("#E6DDF2", "#6E568E"),
    ("#DCEBDD", "#4F7A55"),
    ("#F4DCD7", "#A44D40"),
]
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "images"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size)


def base(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.text((80, 52), title, fill=INK, font=f(43))
    draw.text((82, 116), subtitle, fill=MUTED, font=f(21))
    draw.line((80, 164, WIDTH - 80, 164), fill=LINE, width=2)
    draw.text((80, HEIGHT - 48), source, fill=MUTED, font=f(18))
    return image, draw


def node(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int], title: str, lines: list[str], color: tuple[str, str]) -> None:
    left, top, right, bottom = rect
    fill, border = color
    draw.rounded_rectangle(rect, radius=22, fill=fill, outline=border, width=4)
    draw.text((left + 22, top + 18), title, fill=border, font=f(25))
    y = top + 66
    for line in lines:
        draw.text((left + 22, y), line, fill=INK, font=f(18))
        y += 31


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = LINE) -> None:
    draw.line((*start, *end), fill=color, width=6)
    draw.polygon([(end[0], end[1]), (end[0] - 22, end[1] - 12), (end[0] - 22, end[1] + 12)], fill=color)


def save(image: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / name, quality=92)


def chain(name: str, title: str, subtitle: str, source: str, items: list[tuple[str, list[str]]], footer: str) -> None:
    image, draw = base(title, subtitle, source)
    gap, left, top, bottom = 40, 80, 255, 650
    width = (WIDTH - 160 - gap * (len(items) - 1)) // len(items)
    for index, (label, lines) in enumerate(items):
        x = left + index * (width + gap)
        node(draw, (x, top, x + width, bottom), label, lines, COLORS[index % len(COLORS)])
        if index < len(items) - 1:
            arrow(draw, (x + width + 6, 450), (x + width + gap - 6, 450))
    draw.text((80, 745), footer, fill="#A44D40", font=f(21))
    save(image, name)


def grid(name: str, title: str, subtitle: str, source: str, items: list[tuple[str, list[str]]], footer: str) -> None:
    image, draw = base(title, subtitle, source)
    rects = [(90, 220, 750, 430), (850, 220, 1510, 430), (90, 500, 750, 710), (850, 500, 1510, 710)]
    for index, ((label, lines), rect) in enumerate(zip(items, rects)):
        node(draw, rect, label, lines, COLORS[index])
    draw.text((80, 770), footer, fill="#A44D40", font=f(21))
    save(image, name)


def main() -> None:
    chain("01-coding-loop.png", "An AI Coding Product Is a Closed Interaction Loop", "Context, generation, application and validation must fit developer latency", "Transcript-grounded redraw · 00:00–05:20", [("Workspace", ["Files and edits", "Git state", "User intent"]), ("Context system", ["Index and search", "Rules and history", "Relevant chunks"]), ("Model system", ["Plan / generate", "Provider routing", "Streaming"]), ("Apply + validate", ["Patch quickly", "Diagnostics", "User feedback"])], "The product fails if any subsystem is slow, stale, insecure or unavailable.")
    grid("02-three-systems.png", "Cursor's Scale Comes from Three Different Systems", "Indexing, inference and product orchestration have different workload shapes", "Transcript-grounded redraw · 02:20–05:20", [("Indexing", ["Documents / chunks", "Embeddings", "Retrieval freshness"]), ("Inference", ["Self-hosted models", "Frontier providers", "GPU capacity"]), ("Product / Apply", ["Fast edits", "Editor state", "Interaction latency"]), ("Data plane", ["Jobs and events", "Metadata", "Telemetry / billing"])], "Treating all four as one backend hides the real failure and scaling boundaries.")
    grid("03-blast-radius.png", "A Monolith Can Still Have Small Blast Radii", "Repository shape is not the same as deployment and dependency isolation", "Transcript-grounded redraw · 05:20–07:50", [("Critical cell", ["Auth / request path", "Conservative deploy", "Strict dependencies"]), ("Indexing cell", ["Async jobs", "Backpressure", "Rebuildable state"]), ("Experimental cell", ["New models", "Canary traffic", "Fast rollback"]), ("Shared contracts", ["Versioned schema", "Queues / APIs", "Observability"])], "Blast radius is controlled by runtime boundaries, not by microservice count alone.")
    chain("04-merkle-sync.png", "Merkle-Style Sync Finds Changes Without Re-uploading Everything", "Hierarchical hashes summarize workspace state and identify changed subtrees", "Transcript-grounded redraw · 10:20–14:40", [("Local files", ["Path + content", "Ignore rules", "Current snapshot"]), ("Hash tree", ["Leaf hashes", "Directory hashes", "Root identity"]), ("Diff", ["Compare roots", "Descend changed branch", "Upload delta"]), ("Server state", ["Update version", "Schedule parsing", "Preserve unchanged work"])], "Hash equality proves content reuse, not access authorization or semantic equivalence.")
    chain("05-index-pipeline.png", "Secure Codebase Indexing Is an Incremental Data Pipeline", "Parsing and embedding are asynchronous; unchanged content should hit caches", "Transcript + Cursor secure indexing · 10:20–15:10", [("Parse", ["Language structure", "Syntactic chunks", "Metadata"]), ("Content cache", ["Hash chunk", "Reuse embedding", "Deduplicate"]), ("Embed + store", ["Vector", "Access scope", "Index version"]), ("Retrieve", ["Query", "Rank / filter", "Return context"])], "Freshness, access control and retrieval quality must be measured independently.")
    grid("06-storage-roles.png", "Indexing Data Has Different Durability and Query Needs", "Do not force metadata, documents, vectors and jobs into one database shape", "Transcript-grounded redraw · 14:40–19:10", [("Transactional metadata", ["Users / repos", "Versions", "Permissions"]), ("Job state", ["Queue / lease", "Retry budget", "Progress"]), ("Vector/search data", ["Large immutable segments", "Approximate query", "Recall metrics"]), ("Source artifacts", ["Chunks / documents", "Object identity", "Rebuild input"])], "Choose a source of truth per state class; derived indexes should remain rebuildable.")
    chain("07-incident-cascade.png", "Retries Can Turn a Partial Failure into a Full Incident", "Overload, retry storms, rebuild jobs and migrations form a positive feedback loop", "Transcript-grounded redraw · 19:10–25:30", [("Initial fault", ["Slow database", "Partial job failures", "Timeouts"]), ("Automatic reaction", ["Retries", "Cron / repair jobs", "More reads and writes"]), ("Amplification", ["Queue growth", "Connection pressure", "Cache misses"]), ("Mitigation", ["Stop producers", "Shed load", "Restore invariant"])], "Recovery starts by breaking feedback loops, not by adding more work to a saturated dependency.")
    grid("08-postgres-pressure.png", "PostgreSQL Storage Pressure Is an MVCC and Operations Problem", "Updates create dead tuples; cleanup needs time, I/O and free space", "Transcript 25:30–32:40 · PostgreSQL vacuum docs", [("Write workload", ["Insert / update", "Indexes", "WAL"]), ("MVCC residue", ["Dead tuples", "Table / index bloat", "Long transactions"]), ("Maintenance", ["Autovacuum", "Analyze", "VACUUM FULL trade-off"]), ("Failure pressure", ["Disk exhaustion", "Long recovery", "Migration urgency"])], "The fix is workload-specific: tune, partition, offload or redesign—not simply 'Postgres is bad'.")
    chain("09-cold-start.png", "Index Migration Has a Hidden Cold-Start Bill", "Moving storage can force re-embedding, cache warming and dual-read validation", "Transcript-grounded redraw · 29:30–32:40", [("Old index", ["Serving traffic", "Known cache", "Legacy schema"]), ("Backfill", ["Read source chunks", "Re-embed", "Write new segments"]), ("Validation", ["Dual query", "Recall / latency", "Version compare"]), ("Cutover", ["Route traffic", "Monitor", "Retire safely"])], "Migration capacity must include normal user traffic plus the temporary rebuild workload.")
    chain("10-object-storage-search.png", "Object-Storage-Native Search Separates Durability from Hot Query State", "Durable segments live cheaply; stateless compute and SSD caches absorb demand", "Transcript + turbopuffer architecture · 32:30–36:40", [("Object storage", ["Durable segments", "Low unit cost", "Strong object consistency"]), ("SSD / memory cache", ["Hot partitions", "Admission / eviction", "Warm latency"]), ("Stateless query tier", ["Scale horizontally", "Fetch / rank", "No durable local state"]), ("Quality controls", ["Recall", "Filter correctness", "p95 / p99 latency"])], "Object storage lowers durable cost but does not remove cache, indexing or tail-latency design.")
    chain("11-global-inference.png", "Self-Hosted Inference Is a Global Capacity and Latency Problem", "Autocomplete needs nearby capacity, model replicas and overload behavior", "Transcript-grounded redraw · 03:20–04:20 and 38:10–41:40", [("User region", ["Editor request", "Tight latency", "Streaming UX"]), ("Traffic router", ["Health", "Queue depth", "Model version"]), ("GPU region", ["Replica capacity", "Batching", "KV cache"]), ("Fallback", ["Remote region", "Smaller model", "Graceful degradation"])], "A fast median is insufficient; queueing and failover determine the interactive tail.")
    chain("12-provider-routing.png", "Frontier Model Access Requires a Provider Portfolio", "Rate limits, quality, price and availability change independently", "Transcript 38:10–41:40 · CursorBench and later Cursor Router context", [("Task contract", ["Quality", "Latency", "Context", "Tools"]), ("Provider state", ["Rate limit", "Health", "Price", "Version"]), ("Router", ["Choose model", "Budget / policy", "Fallback"]), ("Evidence", ["Offline eval", "Online outcome", "Regression alert"])], "Multi-provider resilience requires normalized interfaces and versioned evaluation, not random round-robin.")
    chain("13-fast-apply.png", "Planning and Applying Code Are Different Model Jobs", "A powerful model can plan; a specialized apply model protects editor flow", "Transcript 04:20–05:20 · Cursor Fast Apply", [("Plan", ["Intent", "Files", "Target change"]), ("Generate edit", ["Patch / diff", "Context references", "Streaming"]), ("Fast Apply", ["Specialized model", "Resolve locations", "High token rate"]), ("Validate", ["Parse / diagnostics", "Show diff", "User control"])], "Latency belongs to the whole edit loop; faster generation is wasted if application or validation stalls.")
    chain("14-abuse-controls.png", "Free Tokens Create an Adversarial Unit-Economics Surface", "Attackers arbitrage expensive model access through accounts and automation", "Transcript-grounded redraw · 36:40–38:10 and 43:30–45:00", [("Identity", ["Account trust", "Device / payment", "Organization"]), ("Quota", ["Per user / plan", "Burst and daily", "Model budget"]), ("Detection", ["Velocity", "Automation", "Token anomaly"]), ("Response", ["Throttle", "Challenge", "Suspend / appeal"])], "Abuse controls must bound cost without blocking legitimate high-intensity developers.")
    grid("15-security-flow.png", "Code Security Is a Shared Data-Flow Responsibility", "Local controls, encrypted index state and provider policies cover different risks", "Transcript 41:40–43:30 · current Cursor privacy/security docs", [("Workspace", ["Ignore rules", "Secrets hygiene", "User approvals"]), ("Index pipeline", ["Scoped chunks", "Encryption", "Access permissions"]), ("Cursor services", ["Identity / audit", "Privacy Mode", "Retention controls"]), ("Model providers", ["Data handling", "Regional limits", "Contract / policy"])], "Encryption does not replace access control, retention, audit, provider governance or endpoint security.")
    chain("16-incident-learning.png", "AI Can Assist Incident Response, but Humans Own the Control Loop", "Telemetry and assistants compress diagnosis; command decisions remain accountable", "Transcript-grounded redraw · 47:50–48:37", [("Signals", ["Metrics / logs", "Deploys", "User reports"]), ("AI assistant", ["Summarize", "Query evidence", "Suggest hypotheses"]), ("Incident command", ["Prioritize", "Stop feedback", "Authorize risk"]), ("Learning", ["Postmortem", "Runbook / guardrail", "Load test"])], "The goal is faster evidence handling, not autonomous production authority during uncertainty.")


if __name__ == "__main__":
    main()

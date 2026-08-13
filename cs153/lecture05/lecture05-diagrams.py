#!/usr/bin/env python3
"""Generate transcript-grounded teaching diagrams for CS153 Lecture 05."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1600
HEIGHT = 900
BACKGROUND = "#F7F3EA"
INK = "#1F2933"
MUTED = "#667085"
BLUE = "#DCEAF7"
BLUE_DARK = "#3E6C91"
GOLD = "#F1E5BD"
GOLD_DARK = "#8B6B1F"
RED = "#F4DCD7"
RED_DARK = "#A44D40"
GREEN = "#DCEBDD"
GREEN_DARK = "#4F7A55"
PURPLE = "#E6DDF2"
PURPLE_DARK = "#6E568E"
LINE = "#93A0AD"

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "images"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size)


TITLE_FONT = font(45)
SUBTITLE_FONT = font(22)
SMALL_FONT = font(20)
LABEL_FONT = font(24)


def canvas(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((80, 55), title, fill=INK, font=TITLE_FONT)
    draw.text((82, 118), subtitle, fill=MUTED, font=SUBTITLE_FONT)
    draw.line((80, 165, WIDTH - 80, 165), fill=LINE, width=2)
    draw.text((80, HEIGHT - 50), source, fill=MUTED, font=SMALL_FONT)
    return image, draw


def box(
    draw: ImageDraw.ImageDraw,
    bounds: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    fill: str,
    outline: str,
    title_size: int = 27,
    body_size: int = 20,
) -> None:
    left, top, right, bottom = bounds
    draw.rounded_rectangle(bounds, radius=22, fill=fill, outline=outline, width=4)
    draw.text((left + 24, top + 20), title, fill=outline, font=font(title_size))
    cursor = top + 70
    body_font = font(body_size)
    for line in lines:
        draw.text((left + 24, cursor), line, fill=INK, font=body_font)
        cursor += body_size + 13


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = LINE,
    width: int = 6,
) -> None:
    draw.line((*start, *end), fill=color, width=width)
    end_x, end_y = end
    start_x, start_y = start
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    length = max((delta_x * delta_x + delta_y * delta_y) ** 0.5, 1)
    unit_x = delta_x / length
    unit_y = delta_y / length
    perpendicular_x = -unit_y
    perpendicular_y = unit_x
    arrow_length = 22
    arrow_width = 12
    first = (
        end_x - unit_x * arrow_length + perpendicular_x * arrow_width,
        end_y - unit_y * arrow_length + perpendicular_y * arrow_width,
    )
    second = (
        end_x - unit_x * arrow_length - perpendicular_x * arrow_width,
        end_y - unit_y * arrow_length - perpendicular_y * arrow_width,
    )
    draw.polygon([end, first, second], fill=color)


def save(image: Image.Image, filename: str) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT / filename, quality=92)


def abstraction_layers() -> None:
    image, draw = canvas(
        "Why a Platform Layer Exists Above a Hyperscaler",
        "Commodity primitives expose capability; the platform compiles application intent into a managed operating system",
        "Transcript-grounded redraw · 00:00–03:10",
    )
    layers = [
        (220, "Application idea + code", "User goal, product behavior and framework conventions", BLUE, BLUE_DARK),
        (360, "Framework + platform compiler", "Interpret intent, choose runtime, routing, cache and deployment graph", GOLD, GOLD_DARK),
        (500, "Cloud primitives", "Compute, object storage, networking, queues and databases", PURPLE, PURPLE_DARK),
        (640, "Hyperscaler physical infrastructure", "Regions, hardware, backbone, security and operations", GREEN, GREEN_DARK),
    ]
    for top, title, detail, fill, outline in layers:
        box(draw, (200, top, 1400, top + 105), title, [detail], fill, outline, title_size=26, body_size=19)
    save(image, "01-abstraction-layers.png")


def kubernetes_economics() -> None:
    image, draw = canvas(
        "Per-Commit Deployments Break a Static Allocation Model",
        "A product promise can make a technically valid orchestrator economically unsuitable",
        "Transcript-grounded redraw · 01:12–01:42 and 28:50–30:10",
    )
    box(draw, (90, 260, 430, 620), "Product promise", ["Every Git commit", "Immutable preview", "Fast scale from zero"], BLUE, BLUE_DARK)
    box(draw, (630, 260, 970, 620), "Naive Kubernetes", ["Pod per deployment", "Idle reservations", "Slow scale transitions"], RED, RED_DARK)
    box(draw, (1170, 260, 1510, 620), "Result", ["Resource explosion", "High cost", "Experience leaks"], GOLD, GOLD_DARK)
    arrow(draw, (430, 440), (630, 440))
    arrow(draw, (970, 440), (1170, 440))
    draw.text((350, 705), "Architecture must be evaluated against the product's unit economics", fill=INK, font=LABEL_FONT)
    save(image, "02-kubernetes-economics.png")


def cloud_compiler() -> None:
    image, draw = canvas(
        "Framework-Defined Infrastructure as a Cloud Compiler",
        "Source code and framework conventions become an intermediate representation, then an infrastructure plan",
        "Transcript + Vercel Framework-Defined Infrastructure",
    )
    stages = [
        ((50, 300, 330, 590), "Source", ["Routes", "Components", "Data needs"], BLUE, BLUE_DARK),
        ((390, 300, 690, 590), "Framework intent", ["Static / dynamic", "Cache semantics", "Runtime hints"], GOLD, GOLD_DARK),
        ((750, 300, 1050, 590), "Platform IR", ["Assets", "Functions", "Routing graph"], PURPLE, PURPLE_DARK),
        ((1110, 300, 1540, 590), "Deployment", ["Provision primitives", "Connect + secure", "Scale globally"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=25)
    arrow(draw, (330, 445), (390, 445))
    arrow(draw, (690, 445), (750, 445))
    arrow(draw, (1050, 445), (1110, 445))
    draw.text((380, 700), "Infrastructure is generated output, not the developer's starting input", fill=RED_DARK, font=LABEL_FONT)
    save(image, "03-cloud-compiler.png")


def build_output_graph() -> None:
    image, draw = canvas(
        "The Build Output Is a Deployable Artifact Graph",
        "A framework adapter materializes platform primitives instead of shipping one opaque server process",
        "Official Build Output API + transcript",
    )
    box(draw, (90, 300, 430, 610), "Build Output", ["Versioned directory", "Framework adapter", "Deployment metadata"], BLUE, BLUE_DARK)
    outputs = [
        ((610, 210, 940, 390), "Static assets", ["HTML / JS / images"], GREEN, GREEN_DARK),
        ((610, 450, 940, 630), "Functions", ["Dynamic routes / jobs"], GOLD, GOLD_DARK),
        ((1130, 210, 1480, 390), "Routing", ["Rewrites / middleware"], PURPLE, PURPLE_DARK),
        ((1130, 450, 1480, 630), "Cache policy", ["ISR / revalidation"], RED, RED_DARK),
    ]
    for bounds, title, lines, fill, outline in outputs:
        box(draw, bounds, title, lines, fill, outline, title_size=25, body_size=19)
    for target in ((610, 300), (610, 540), (1130, 300), (1130, 540)):
        arrow(draw, (430, 455), target)
    save(image, "04-build-output-graph.png")


def isr_cache_loop() -> None:
    image, draw = canvas(
        "ISR Converts Repeated Backend Work into Managed Materialization",
        "Generate once, serve many times, then revalidate under an explicit freshness policy",
        "Transcript · 05:55–07:20 + Next.js ISR documentation",
    )
    box(draw, (70, 290, 370, 580), "Request", ["Product page", "Traffic spike"], BLUE, BLUE_DARK)
    box(draw, (470, 210, 800, 500), "Render / fetch", ["Call backend", "Compute response"], GOLD, GOLD_DARK)
    box(draw, (900, 210, 1230, 500), "Materialize", ["Store output", "Attach cache metadata"], PURPLE, PURPLE_DARK)
    box(draw, (1280, 290, 1530, 580), "Edge serve", ["Fast response", "Backend shield"], GREEN, GREEN_DARK, title_size=24)
    arrow(draw, (370, 430), (470, 355))
    arrow(draw, (800, 355), (900, 355))
    arrow(draw, (1230, 355), (1280, 430))
    arrow(draw, (1400, 580), (1065, 710), RED_DARK)
    arrow(draw, (1065, 710), (1065, 500), RED_DARK)
    draw.text((735, 735), "time / event → revalidate", fill=RED_DARK, font=LABEL_FONT)
    save(image, "05-isr-cache-loop.png")


def build_vs_buy() -> None:
    image, draw = canvas(
        "Build Where Insight Compounds; Buy Where Scale Is Commodity",
        "The strategic boundary follows differentiation, not engineering pride",
        "Transcript-grounded redraw · 07:40–10:30",
    )
    box(draw, (100, 250, 720, 640), "Buy / reuse", ["Regions + hardware", "Backbone + object storage", "Commodity databases", "Security certifications"], GREEN, GREEN_DARK, title_size=30)
    box(draw, (880, 250, 1500, 640), "Build / specialize", ["Framework compiler", "Application-aware routing", "Global metadata", "Developer feedback loop"], BLUE, BLUE_DARK, title_size=30)
    draw.line((800, 220, 800, 690), fill=LINE, width=3)
    draw.text((460, 715), "Build-vs-buy is a moving boundary as primitives mature", fill=RED_DARK, font=LABEL_FONT)
    save(image, "06-build-vs-buy.png")


def global_metadata() -> None:
    image, draw = canvas(
        "A Deployment Is Immutable; the Domain Pointer Moves",
        "Global metadata connects a stable deployment identity to routing decisions at the edge",
        "Transcript-grounded redraw · 10:00–16:40 and 33:30–34:05",
    )
    box(draw, (70, 300, 400, 590), "Git commit", ["Content identity", "Immutable source"], BLUE, BLUE_DARK)
    box(draw, (510, 300, 870, 590), "Deployment object", ["Assets + functions", "Versioned metadata"], GOLD, GOLD_DARK)
    box(draw, (980, 220, 1530, 450), "Domain binding", ["stanford.edu → deployment B", "Atomic pointer update"], PURPLE, PURPLE_DARK)
    box(draw, (980, 540, 1530, 720), "Edge replicas", ["Fast propagation", "Local request routing"], GREEN, GREEN_DARK)
    arrow(draw, (400, 445), (510, 445))
    arrow(draw, (870, 400), (980, 335))
    arrow(draw, (1255, 450), (1255, 540))
    draw.text((385, 735), "Rollback moves the pointer; old deployment stays reproducible", fill=RED_DARK, font=LABEL_FONT)
    save(image, "07-global-metadata.png")


def opinionated_platform() -> None:
    image, draw = canvas(
        "Opinionated Frameworks Create an Optimization Surface",
        "Guard rails expose intent, allowing the platform to optimize without per-project infrastructure configuration",
        "Transcript + Framework-Defined Infrastructure",
    )
    box(draw, (90, 260, 430, 610), "Framework conventions", ["Routes", "Data lifecycle", "Rendering modes"], BLUE, BLUE_DARK)
    box(draw, (630, 260, 970, 610), "Platform knowledge", ["Predictable structure", "Safe defaults", "Automatic mapping"], GOLD, GOLD_DARK)
    box(draw, (1170, 260, 1510, 610), "Optimization", ["Cache placement", "Runtime selection", "Global delivery"], GREEN, GREEN_DARK)
    arrow(draw, (430, 435), (630, 435))
    arrow(draw, (970, 435), (1170, 435))
    draw.text((410, 705), "Opinion trades some freedom for lower operational entropy", fill=PURPLE_DARK, font=LABEL_FONT)
    save(image, "08-opinionated-platform.png")


def consumption_feedback() -> None:
    image, draw = canvas(
        "Consumption Pricing Can Become a Developer Fitness Function",
        "An operation is teachable when its resource impact and cost are attributable",
        "Transcript-grounded redraw · 20:00–22:40",
    )
    stages = [
        ((60, 300, 330, 590), "Operation", ["Query / render", "Model call"], BLUE, BLUE_DARK),
        ((390, 300, 690, 590), "Resource impact", ["CPU / memory", "Requests / transfer"], GOLD, GOLD_DARK),
        ((750, 300, 1050, 590), "Meter + price", ["Attributable units", "Near-real-time signal"], PURPLE, PURPLE_DARK),
        ((1110, 300, 1540, 590), "Developer action", ["Cache / batch", "Optimize / redesign"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=25)
    arrow(draw, (330, 445), (390, 445))
    arrow(draw, (690, 445), (750, 445))
    arrow(draw, (1050, 445), (1110, 445))
    arrow(draw, (1320, 590), (195, 730), RED_DARK)
    arrow(draw, (195, 730), (195, 590), RED_DARK)
    save(image, "09-consumption-feedback.png")


def workload_isolation() -> None:
    image, draw = canvas(
        "Attribution Fails When Noisy Workloads Share an Opaque Pool",
        "Resource isolation and per-operation accounting make performance and cost explainable",
        "Transcript-grounded redraw · 20:30–22:35",
    )
    box(draw, (100, 250, 720, 650), "Opaque shared workload", ["Expensive join", "Neighbor latency", "System-wide degradation", "Weak cost attribution"], RED, RED_DARK, title_size=29)
    box(draw, (880, 250, 1500, 650), "Attributable workload", ["Operation-level units", "Isolation / scaling", "Stable quality of service", "Actionable price signal"], GREEN, GREEN_DARK, title_size=29)
    draw.text((565, 715), "The lesson is workload accounting—not a universal database ranking", fill=INK, font=LABEL_FONT)
    save(image, "10-workload-isolation.png")


def telemetry_loop() -> None:
    image, draw = canvas(
        "Telemetry Closes the Gap Between Deployment and Consequence",
        "Version, latency, errors and spend must be visible on the same operational timeline",
        "Transcript-grounded redraw · 22:50–23:45",
    )
    box(draw, (90, 280, 390, 610), "Deployment", ["Version", "Region", "Runtime"], BLUE, BLUE_DARK)
    box(draw, (520, 210, 870, 540), "Signals", ["Latency / errors", "CPU / memory", "Requests / spend"], GOLD, GOLD_DARK)
    box(draw, (1000, 280, 1510, 610), "Decision", ["Investigate regression", "Change cache / code", "Rollback or raise budget"], GREEN, GREEN_DARK)
    arrow(draw, (390, 445), (520, 370))
    arrow(draw, (870, 370), (1000, 445))
    arrow(draw, (1250, 610), (695, 730), RED_DARK)
    arrow(draw, (695, 730), (695, 540), RED_DARK)
    save(image, "11-telemetry-loop.png")


def spend_controls() -> None:
    image, draw = canvas(
        "Soft and Hard Spend Controls Protect Different Things",
        "Alerts preserve learning and continuity; pauses cap exposure but can stop revenue and traffic",
        "Transcript + current Vercel Spend Management docs",
    )
    box(draw, (100, 250, 720, 630), "Soft control", ["Threshold notification", "Webhook / escalation", "Traffic keeps serving", "Learn before acting"], BLUE, BLUE_DARK, title_size=30)
    box(draw, (880, 250, 1500, 630), "Hard control", ["Pause production", "Bound worst-case spend", "Enforcement may lag", "Can interrupt business"], RED, RED_DARK, title_size=30)
    draw.line((800, 220, 800, 680), fill=LINE, width=3)
    draw.text((360, 715), "Budget must be evaluated against revenue, abuse risk and recovery time", fill=INK, font=LABEL_FONT)
    save(image, "12-spend-controls.png")


def compute_density() -> None:
    image, draw = canvas(
        "AI Workloads Split CPU-Bound and I/O-Bound Capacity Decisions",
        "Scale out active compute; multiplex requests that mostly wait on model or network I/O",
        "Transcript preview · 24:50–28:10 + current Fluid Compute docs",
    )
    box(draw, (80, 250, 720, 650), "CPU-bound request", ["Local compute stays busy", "Contention hurts latency", "Scale horizontally", "Reserve active CPU"], GOLD, GOLD_DARK, title_size=29)
    box(draw, (880, 250, 1520, 650), "I/O-bound AI request", ["Waits on model / network", "CPU often idle", "Share warm instance", "Increase safe concurrency"], BLUE, BLUE_DARK, title_size=29)
    draw.text((465, 715), "Compute density depends on the workload profile, not one fixed pod count", fill=RED_DARK, font=LABEL_FONT)
    save(image, "13-compute-density.png")


def v0_loop() -> None:
    image, draw = canvas(
        "v0 Turns Product Use into an AI Development Loop",
        "Prompt-to-app generation combines model capability, tool invocation, preview infrastructure and user feedback",
        "Transcript-grounded redraw · 30:15–31:55",
    )
    stages = [
        ((60, 300, 330, 590), "Prompt", ["Idea / UI change", "Constraints"], BLUE, BLUE_DARK),
        ((390, 230, 690, 520), "Agent + tools", ["Generate code", "Invoke framework actions"], PURPLE, PURPLE_DARK),
        ((750, 230, 1050, 520), "Preview", ["Immutable URL", "Run + inspect"], GOLD, GOLD_DARK),
        ((1110, 300, 1540, 590), "Feedback", ["Edit / accept", "Failure evidence"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=25)
    arrow(draw, (330, 445), (390, 375))
    arrow(draw, (690, 375), (750, 375))
    arrow(draw, (1050, 375), (1110, 445))
    arrow(draw, (1320, 590), (540, 720), RED_DARK)
    arrow(draw, (540, 720), (540, 520), RED_DARK)
    save(image, "14-v0-loop.png")


def immutable_mvp() -> None:
    image, draw = canvas(
        "The MVP Was One Command Returning an Immutable URL",
        "A narrow interface tested the product idea before the underlying system was efficient",
        "Transcript-grounded redraw · 32:50–35:55",
    )
    box(draw, (70, 300, 370, 590), "API / CLI", ["Upload artifact", "One command"], BLUE, BLUE_DARK)
    box(draw, (490, 300, 820, 590), "Content identity", ["Immutable deployment", "Commit-like version"], GOLD, GOLD_DARK)
    box(draw, (940, 210, 1250, 500), "Gossip metadata", ["Propagate pointer", "Global replicas"], PURPLE, PURPLE_DARK)
    box(draw, (1280, 300, 1530, 590), "URL", ["Preview", "Share", "Rollback"], GREEN, GREEN_DARK, title_size=24)
    arrow(draw, (370, 445), (490, 445))
    arrow(draw, (820, 445), (940, 355))
    arrow(draw, (1250, 355), (1280, 445))
    draw.text((330, 705), "Validate idea-market fit first; replace over-provisioned internals later", fill=RED_DARK, font=LABEL_FONT)
    save(image, "15-immutable-mvp.png")


def day_maturity() -> None:
    image, draw = canvas(
        "Infrastructure Products Must Survive Day 1, Day 100 and Day 1000",
        "Adoption, complexity absorption and operations are separate product tests",
        "Transcript-grounded redraw · 36:00–37:05",
    )
    stages = [
        ((90, 270, 470, 650), "Day 1", ["Fast onboarding", "Beautiful default", "First deployment"], BLUE, BLUE_DARK),
        ((610, 270, 990, 650), "Day 100", ["More code + teams", "Platform does not leak", "Manage complexity"], GOLD, GOLD_DARK),
        ((1130, 270, 1510, 650), "Day 1000", ["Uptime + recovery", "Predictable cost", "Long-term trust"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=31, body_size=21)
    arrow(draw, (470, 460), (610, 460))
    arrow(draw, (990, 460), (1130, 460))
    draw.text((425, 720), "Great DX earns entry; durable operations earn the platform relationship", fill=INK, font=LABEL_FONT)
    save(image, "16-day-maturity.png")


def main() -> None:
    abstraction_layers()
    kubernetes_economics()
    cloud_compiler()
    build_output_graph()
    isr_cache_loop()
    build_vs_buy()
    global_metadata()
    opinionated_platform()
    consumption_feedback()
    workload_isolation()
    telemetry_loop()
    spend_controls()
    compute_density()
    v0_loop()
    immutable_mvp()
    day_maturity()


if __name__ == "__main__":
    main()

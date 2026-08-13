#!/usr/bin/env python3
"""Generate transcript-grounded teaching diagrams for CS153 Lecture 06."""

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


TITLE_FONT = font(44)
SUBTITLE_FONT = font(21)
SMALL_FONT = font(18)


def canvas(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((80, 52), title, fill=INK, font=TITLE_FONT)
    draw.text((82, 116), subtitle, fill=MUTED, font=SUBTITLE_FONT)
    draw.line((80, 164, WIDTH - 80, 164), fill=LINE, width=2)
    draw.text((80, HEIGHT - 48), source, fill=MUTED, font=SMALL_FONT)
    return image, draw


def box(
    draw: ImageDraw.ImageDraw,
    bounds: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    fill: str,
    outline: str,
    title_size: int = 25,
    body_size: int = 18,
) -> None:
    left, top, right, bottom = bounds
    draw.rounded_rectangle(bounds, radius=22, fill=fill, outline=outline, width=4)
    draw.text((left + 22, top + 18), title, fill=outline, font=font(title_size))
    cursor = top + 66
    body_font = font(body_size)
    for line in lines:
        draw.text((left + 22, cursor), line, fill=INK, font=body_font)
        cursor += body_size + 12


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = LINE) -> None:
    draw.line((*start, *end), fill=color, width=6)
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
    first = (end_x - unit_x * arrow_length + perpendicular_x * arrow_width, end_y - unit_y * arrow_length + perpendicular_y * arrow_width)
    second = (end_x - unit_x * arrow_length - perpendicular_x * arrow_width, end_y - unit_y * arrow_length - perpendicular_y * arrow_width)
    draw.polygon([end, first, second], fill=color)


def save(image: Image.Image, filename: str) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT / filename, quality=92)


def chain_diagram(filename: str, title: str, subtitle: str, source: str, nodes: list[tuple[str, list[str], str, str]], footer: str) -> None:
    image, draw = canvas(title, subtitle, source)
    count = len(nodes)
    gap = 42
    left = 85
    top = 270
    bottom = 630
    width = (WIDTH - 170 - gap * (count - 1)) // count
    for index, (node_title, lines, fill, outline) in enumerate(nodes):
        node_left = left + index * (width + gap)
        node_right = node_left + width
        box(draw, (node_left, top, node_right, bottom), node_title, lines, fill, outline, body_size=17)
        if index < count - 1:
            arrow(draw, (node_right + 6, (top + bottom) // 2), (node_right + gap - 6, (top + bottom) // 2))
    draw.text((80, 735), footer, fill=RED_DARK, font=font(22))
    save(image, filename)


def two_column(filename: str, title: str, subtitle: str, source: str, left_data: tuple[str, list[str], str, str], right_data: tuple[str, list[str], str, str], footer: str) -> None:
    image, draw = canvas(title, subtitle, source)
    box(draw, (115, 245, 745, 650), *left_data, body_size=20)
    box(draw, (855, 245, 1485, 650), *right_data, body_size=20)
    arrow(draw, (755, 450), (845, 450), color=RED_DARK)
    draw.text((80, 735), footer, fill=RED_DARK, font=font(22))
    save(image, filename)


def four_quadrants(filename: str, title: str, subtitle: str, source: str, nodes: list[tuple[str, list[str], str, str]], footer: str) -> None:
    image, draw = canvas(title, subtitle, source)
    bounds = [(100, 220, 750, 430), (850, 220, 1500, 430), (100, 500, 750, 710), (850, 500, 1500, 710)]
    for item, rectangle in zip(nodes, bounds):
        box(draw, rectangle, *item, body_size=18)
    draw.text((80, 770), footer, fill=RED_DARK, font=font(21))
    save(image, filename)


def main() -> None:
    chain_diagram(
        "01-infrastructure-diffusion.png",
        "Infrastructure Creates Value Only Through Application Diffusion",
        "The internet analogy separates enabling capacity from realized productivity",
        "Transcript-grounded redraw · 03:40–06:20",
        [
            ("Infrastructure wave", ["Routers / accelerators", "Capital and hype", "New technical capacity"], BLUE, BLUE_DARK),
            ("Application triggers", ["Healthcare", "Education", "GovTech", "Industry workflows"], GOLD, GOLD_DARK),
            ("Organizational change", ["Data and process redesign", "Adoption and trust", "New operating model"], PURPLE, PURPLE_DARK),
            ("Measured outcomes", ["Productivity", "Service quality", "GDP / welfare", "Learning feedback"], GREEN, GREEN_DARK),
        ],
        "Capacity is necessary; diffusion, workflow redesign and evidence determine whether it becomes value.",
    )
    four_quadrants(
        "02-efficiency-stack.png",
        "Useful AI Compute Is Limited by a Four-Layer Efficiency Stack",
        "Optimizing FLOPS alone leaves data movement and facility losses untouched",
        "Transcript-grounded redraw · 06:20–12:00",
        [
            ("Semiconductor", ["Switching voltage", "Leakage", "Compound materials"], BLUE, BLUE_DARK),
            ("Memory", ["Capacity", "Bandwidth", "Placement", "Energy per access"], GOLD, GOLD_DARK),
            ("Interconnect", ["Electrical / optical", "Topology", "Collective latency"], PURPLE, PURPLE_DARK),
            ("Facility", ["Cooling", "Power conversion", "Utilization", "Reliability"], GREEN, GREEN_DARK),
        ],
        "The lecture lists research opportunities; each claim still needs workload-specific measurement.",
    )
    two_column(
        "03-memory-wall.png",
        "The Memory Wall Is a Rate-Mismatch Problem",
        "Arithmetic throughput scales faster than the capacity to feed arithmetic units",
        "Transcript 08:20–10:30 · Gholami et al., AI and Memory Wall",
        ("Compute trajectory", ["More arithmetic units", "Higher tensor throughput", "Lower precision", "Faster model kernels"], BLUE, BLUE_DARK),
        ("Data-supply trajectory", ["Memory capacity", "Memory bandwidth", "Interconnect bandwidth", "Communication energy"], RED, RED_DARK),
        "A faster accelerator can remain idle when weights, KV cache or activations cannot arrive quickly enough.",
    )
    chain_diagram(
        "04-memory-hierarchy.png",
        "Memory Placement Trades Capacity for Latency, Bandwidth and Energy",
        "SRAM, DRAM, HBM and storage are not interchangeable capacity pools",
        "Transcript-grounded redraw · 09:00–11:10",
        [
            ("On-chip SRAM", ["Very low latency", "High bandwidth", "Small capacity", "High area cost"], BLUE, BLUE_DARK),
            ("Near-chip DRAM", ["Larger capacity", "Package / board link", "Moderate latency"], GREEN, GREEN_DARK),
            ("HBM", ["Stacked DRAM", "Wide interface", "High bandwidth", "Capacity constraint"], GOLD, GOLD_DARK),
            ("SSD / storage", ["Persistent", "Largest capacity", "High latency", "Staging tier"], PURPLE, PURPLE_DARK),
        ],
        "A model-serving design must map hot weights, KV cache and cold artifacts to different tiers.",
    )
    chain_diagram(
        "05-power-budget.png",
        "Facility Power Is Not the Same as Useful Accelerator Power",
        "A data center power budget includes conversion, cooling, networking and idle capacity",
        "Transcript-grounded redraw · 10:30–14:50",
        [
            ("Grid input", ["Contracted MW", "Reliability reserve", "Carbon / fuel mix"], BLUE, BLUE_DARK),
            ("Facility overhead", ["Cooling", "UPS and conversion", "Lighting / controls"], RED, RED_DARK),
            ("IT load", ["Accelerators", "CPU / memory", "Network / storage"], GOLD, GOLD_DARK),
            ("Useful work", ["Tokens / second", "Training progress", "SLO-compliant serving"], GREEN, GREEN_DARK),
        ],
        "PUE measures facility overhead, but utilization and workload efficiency determine useful output.",
    )
    four_quadrants(
        "06-planning-clocks.png",
        "National AI Infrastructure Runs on Conflicting Clocks",
        "Long-lived physical commitments meet rapidly changing accelerators and models",
        "Transcript-grounded redraw · 14:45–16:10",
        [
            ("Grid and land", ["Multi-year approvals", "Transmission", "Water and site risk"], BLUE, BLUE_DARK),
            ("Facility shell", ["18–36 month build", "6–8+ year life", "Retrofit constraints"], GOLD, GOLD_DARK),
            ("Accelerator generation", ["Short product cycle", "Rack density shifts", "Cooling changes"], PURPLE, PURPLE_DARK),
            ("Model demand", ["Uncertain workload mix", "Training ↔ inference", "Context and agent growth"], GREEN, GREEN_DARK),
        ],
        "Modularity, power headroom and portable software reduce regret; forecasts cannot remove uncertainty.",
    )
    chain_diagram(
        "07-three-ai-frontiers.png",
        "Generative, Agentic and Physical AI Need Different Evidence",
        "One model benchmark cannot validate all three system classes",
        "Transcript-grounded redraw · 16:10–20:20",
        [
            ("Generative AI", ["Create candidate content", "Search and formulation", "Quality evaluation"], BLUE, BLUE_DARK),
            ("Agentic AI", ["Plan and use tools", "Act across workflow", "Observe consequences"], GOLD, GOLD_DARK),
            ("Physical AI", ["Sense real world", "Control machines", "Safety envelope"], RED, RED_DARK),
            ("Deployment evidence", ["Task metrics", "Workflow outcomes", "Safety and governance"], GREEN, GREEN_DARK),
        ],
        "The farther a system acts in the world, the stronger its verification and accountability requirements.",
    )
    two_column(
        "08-healthcare-boundaries.png",
        "AI Can Compress Search Without Removing Clinical Governance",
        "Drug formulation and robotic surgery accelerate different stages of care",
        "Transcript 16:40–18:20 · KFSHRC official robotic-transplant report",
        ("Research acceleration", ["Generate candidates", "Predict properties", "Prioritize experiments", "Shorten formulation search"], BLUE, BLUE_DARK),
        ("Clinical deployment", ["Trials and evidence", "Regulatory review", "Surgeon-controlled robot", "Patient safety follow-up"], RED, RED_DARK),
        "A shorter design loop does not imply autonomous approval or autonomous surgery.",
    )
    chain_diagram(
        "09-energy-agent-loop.png",
        "Vertical Agents Need an Operational Feedback Loop",
        "Energy use cases combine sensor history, domain constraints and accountable action",
        "Transcript-grounded redraw · 18:20–20:20",
        [
            ("Operational data", ["Sensors", "Maintenance history", "Geology / asset state"], BLUE, BLUE_DARK),
            ("Agent analysis", ["Corrosion risk", "Drilling recommendation", "Scenario simulation"], GOLD, GOLD_DARK),
            ("Human decision", ["Engineer approval", "Safety check", "Work-order change"], RED, RED_DARK),
            ("Observed outcome", ["Failure / success", "Cost and downtime", "New labeled evidence"], GREEN, GREEN_DARK),
        ],
        "Without outcome capture, an agent produces advice but does not become an improving operational system.",
    )
    chain_diagram(
        "10-model-agnostic.png",
        "Model Agnostic Means Evaluation-Driven Portfolio Selection",
        "Open/closed and small/large are design choices, not identities",
        "Transcript-grounded redraw · 20:20–23:40",
        [
            ("Task contract", ["Quality threshold", "Latency", "Privacy", "Languages"], BLUE, BLUE_DARK),
            ("Candidate portfolio", ["Open / closed", "Small / large", "General / specialist"], PURPLE, PURPLE_DARK),
            ("Evidence", ["Offline eval", "Cost and SLO", "Red-team", "Human review"], GOLD, GOLD_DARK),
            ("Routing policy", ["Choose per task", "Fallback", "Version and audit"], GREEN, GREEN_DARK),
        ],
        "No model religion does not mean no standards; it requires stronger evaluation and change control.",
    )
    chain_diagram(
        "11-infrastructure-flywheel.png",
        "Compute Capacity Produces Value Only When the Utilization Flywheel Turns",
        "Affordable inference can increase experiments, demand and learning",
        "Transcript 27:10–32:20 and 42:30–45:10 · Groq/Aramco Digital context",
        [
            ("Capacity", ["Power and racks", "Accelerators", "Serving software"], BLUE, BLUE_DARK),
            ("Utilization", ["Model onboarding", "Scheduling", "Reliable demand"], GOLD, GOLD_DARK),
            ("Lower unit cost", ["Tokens / dollar", "Latency", "Access for startups"], GREEN, GREEN_DARK),
            ("Application demand", ["More experiments", "Vertical products", "Feedback to capacity"], PURPLE, PURPLE_DARK),
        ],
        "Idle capacity is not a no-regret outcome; software, demand aggregation and access policy matter.",
    )
    two_column(
        "12-training-inference.png",
        "Training and Inference Have Different Infrastructure Shapes",
        "The lifecycle shifts from concentrated jobs to distributed, SLO-bound serving",
        "Transcript-grounded redraw · 32:20–36:50",
        ("Training", ["Large synchronized clusters", "Bursting experiments", "Checkpoint storage", "Throughput-oriented"], BLUE, BLUE_DARK),
        ("Inference", ["Geographic demand", "Latency and availability", "KV-cache / batching", "Continuous cost pressure"], GREEN, GREEN_DARK),
        "Capacity plans should model workload mix, not extrapolate a single training/inference ratio forever.",
    )
    four_quadrants(
        "13-data-sovereignty.png",
        "Data Sovereignty Is a Multi-Dimensional Architecture Problem",
        "Location is only one of the controls required for continuity and accountability",
        "Transcript-grounded redraw · 32:20–36:50 · DGA cloud-governance context",
        [
            ("Location", ["Where data rests", "Where compute runs", "Replication regions"], BLUE, BLUE_DARK),
            ("Control", ["Keys and identity", "Admin access", "Supply-chain authority"], GOLD, GOLD_DARK),
            ("Jurisdiction", ["Applicable law", "Disclosure process", "Audit obligations"], PURPLE, PURPLE_DARK),
            ("Continuity", ["Portability", "Backup / recovery", "Exit and failover"], GREEN, GREEN_DARK),
        ],
        "A data-embassy pattern needs explicit legal agreements and recovery tests; a diagram alone proves nothing.",
    )
    chain_diagram(
        "14-ai-space-stack.png",
        "AI and Space Connect Sensing Infrastructure to Resource Decisions",
        "The value chain runs from communication and observation to grounded action",
        "Transcript-grounded redraw · 24:00–27:10 and 48:50–49:20",
        [
            ("Space infrastructure", ["LEO / MEO / GEO", "Earth observation", "Lunar systems"], BLUE, BLUE_DARK),
            ("Data products", ["Imagery", "Positioning", "Connectivity", "Environmental signals"], GOLD, GOLD_DARK),
            ("AI interpretation", ["Land-use detection", "Water stress", "Routing / prediction"], PURPLE, PURPLE_DARK),
            ("Physical decision", ["Farming policy", "Resource allocation", "Harsh-environment robotics"], GREEN, GREEN_DARK),
        ],
        "The hard part is closing the sensing-to-policy loop with reliable labels and measured outcomes.",
    )
    two_column(
        "15-compute-near-memory.png",
        "New Architectures Target Data Movement, Not Just Peak FLOPS",
        "In-memory and near-memory computing move operations toward stored data",
        "Transcript 45:10–47:20 · Sebastian et al. 2020",
        ("Conventional path", ["Memory stores data", "Interconnect transfers", "Processor computes", "Results move back"], RED, RED_DARK),
        ("Near / in-memory path", ["Place compute near cells", "Reduce transfers", "Exploit parallelism", "Accept precision/tool limits"], GREEN, GREEN_DARK),
        "Energy savings depend on workload mapping, device precision, endurance and software support.",
    )
    chain_diagram(
        "16-government-agent-maturity.png",
        "Government Agents Must Cross Three Maturity Gates",
        "Task demos fail to become workflow systems without data and accountability",
        "Transcript-grounded redraw · 49:50–52:17",
        [
            ("Task augmentation", ["Draft / classify", "Single user", "Local success metric"], BLUE, BLUE_DARK),
            ("Workflow integration", ["Multiple systems", "State and permissions", "Exception handling"], GOLD, GOLD_DARK),
            ("Multi-agent operation", ["Coordination", "Shared memory", "Conflict / recovery"], PURPLE, PURPLE_DARK),
            ("Public accountability", ["Data quality", "Human-in-the-loop", "Audit and appeal"], GREEN, GREEN_DARK),
        ],
        "The limiting layer is often data, process ownership and business model—not the base model alone.",
    )


if __name__ == "__main__":
    main()

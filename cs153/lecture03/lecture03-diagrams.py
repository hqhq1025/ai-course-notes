#!/usr/bin/env python3
"""Generate transcript-grounded teaching diagrams for CS153 Lecture 03."""

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


TITLE_FONT = font(46)
SUBTITLE_FONT = font(23)
SMALL_FONT = font(21)
LABEL_FONT = font(25)


def canvas(title: str, subtitle: str, source: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((80, 55), title, fill=INK, font=TITLE_FONT)
    draw.text((82, 119), subtitle, fill=MUTED, font=SUBTITLE_FONT)
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
    title_size: int = 28,
    body_size: int = 21,
) -> None:
    left, top, right, bottom = bounds
    draw.rounded_rectangle(bounds, radius=22, fill=fill, outline=outline, width=4)
    draw.text((left + 24, top + 22), title, fill=outline, font=font(title_size))
    cursor = top + 72
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


def infrastructure_epochs() -> None:
    image, draw = canvas(
        "Infrastructure Epochs in the Lecture",
        "Palantir's deployment problem changed from manual on-prem operations to heterogeneous autonomous delivery",
        "Transcript-grounded redraw · 05:00–13:30",
    )
    events = [
        (170, "On-prem monolith", ["Air-gapped", "Manual upgrades"], RED, RED_DARK),
        (500, "Scale-out services", ["More components", "Dependency burden"], GOLD, GOLD_DARK),
        (830, "Microservices", ["Independent teams", "5,000 services"], BLUE, BLUE_DARK),
        (1160, "Apollo + Rubix", ["Fleet automation", "Uniform substrate"], GREEN, GREEN_DARK),
    ]
    for left, title, lines, fill, outline in events:
        box(draw, (left, 310, left + 280, 610), title, lines, fill, outline, title_size=25, body_size=20)
    for left in [450, 780, 1110]:
        arrow(draw, (left, 460), (left + 50, 460))
    draw.text((520, 700), "Each epoch removes one bottleneck and exposes another", fill=MUTED, font=LABEL_FONT)
    save(image, "01-infrastructure-epochs.png")


def heterogeneous_fleet() -> None:
    image, draw = canvas(
        "The Scaling Unit Is the Heterogeneous Fleet",
        "Scale is not only cluster size; it is the number of distinct constraints the same software must survive",
        "Transcript-grounded redraw · 05:00–09:00",
    )
    environments = [
        ((90, 270, 390, 590), "Air-gapped", ["No remote SSH", "Offline bundles", "Classified network"], RED, RED_DARK),
        ((450, 270, 750, 590), "Tactical edge", ["Tank / submarine", "Intermittent links", "Resource limits"], GOLD, GOLD_DARK),
        ((810, 270, 1110, 590), "Single-tenant", ["Customer controls", "Unique compliance", "Local hardware"], BLUE, BLUE_DARK),
        ((1170, 270, 1470, 590), "Multi-tenant cloud", ["Large scale", "Elastic capacity", "Shared platform"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in environments:
        box(draw, bounds, title, lines, fill, outline, title_size=27, body_size=20)
    draw.text((510, 690), "One codebase · different connectivity, hardware, policy and failure modes", fill=INK, font=LABEL_FONT)
    save(image, "02-heterogeneous-fleet.png")


def apollo_control_loop() -> None:
    image, draw = canvas(
        "Apollo as a Desired-State Control Loop",
        "Developers declare constraints; the delivery system plans, observes and remediates across the fleet",
        "Transcript + Palantir Apollo official material",
    )
    items = [
        ((70, 310, 340, 570), "Developer", ["Version", "Dependencies", "Health rules"], BLUE, BLUE_DARK),
        ((410, 250, 700, 630), "Catalog", ["Software metadata", "Schemas", "Security findings"], GOLD, GOLD_DARK),
        ((780, 250, 1070, 630), "Orchestrator", ["Target state", "Release channels", "Upgrade plan"], PURPLE, PURPLE_DARK),
        ((1150, 310, 1510, 570), "Environments", ["Observed state", "Execute plan", "Report health"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in items:
        box(draw, bounds, title, lines, fill, outline, title_size=28, body_size=20)
    arrow(draw, (340, 440), (410, 440))
    arrow(draw, (700, 440), (780, 440))
    arrow(draw, (1070, 440), (1150, 440))
    arrow(draw, (1330, 570), (925, 735), GREEN_DARK)
    arrow(draw, (925, 735), (555, 630), GREEN_DARK)
    draw.text((690, 760), "health → rollback / remediation", fill=GREEN_DARK, font=SMALL_FONT)
    save(image, "03-apollo-control-loop.png")


def release_confidence() -> None:
    image, draw = canvas(
        "Release Channels Encode Confidence, Not a Single Pipeline",
        "The same version can progress non-linearly through canary, connected, regulated and air-gapped environments",
        "Official Apollo concepts + transcript · 09:00–15:00",
    )
    stages = [
        (100, 600, "Build", "artifact + metadata", BLUE, BLUE_DARK),
        (390, 500, "Canary", "fast feedback", GREEN, GREEN_DARK),
        (680, 400, "Connected fleet", "broad rollout", GOLD, GOLD_DARK),
        (970, 300, "Regulated", "extra controls", PURPLE, PURPLE_DARK),
        (1260, 200, "Air-gapped", "bundle + delayed sync", RED, RED_DARK),
    ]
    for left, top, title, detail, fill, outline in stages:
        box(draw, (left, top, left + 230, top + 145), title, [detail], fill, outline, title_size=24, body_size=18)
    arrow(draw, (215, 590), (1375, 185), LINE, width=5)
    draw.text((170, 230), "Rollback follows health, not calendar", fill=RED_DARK, font=LABEL_FONT)
    save(image, "04-release-confidence.png")


def rubix_layers() -> None:
    image, draw = canvas(
        "Rubix Separates Application Intent from Environment Detail",
        "A uniform hardened Kubernetes substrate absorbs provider, compliance and lifecycle differences",
        "Transcript-grounded redraw · 15:00–20:00",
    )
    layers = [
        (220, "Applications / AIP / Foundry / Gotham", "Product teams express workload intent", BLUE, BLUE_DARK),
        (360, "Apollo delivery and policy", "Versions, constraints, health and rollout", GOLD, GOLD_DARK),
        (500, "Rubix hardened Kubernetes substrate", "Security, autoscaling, isolation, node lifecycle", GREEN, GREEN_DARK),
        (640, "Cloud · on-prem · edge · air-gapped", "Different hardware, networks and accreditation", RED, RED_DARK),
    ]
    for top, title, detail, fill, outline in layers:
        box(draw, (230, top, 1370, top + 105), title, [detail], fill, outline, title_size=26, body_size=19)
    save(image, "05-rubix-layers.png")


def ephemeral_security() -> None:
    image, draw = canvas(
        "Ephemerality Converts Patching into Replacement",
        "Short-lived immutable nodes reduce persistence and move compliance from convention into software",
        "Transcript + current Palantir Rubix documentation",
    )
    box(draw, (100, 280, 440, 620), "Trusted image", ["Patched baseline", "Signed artifact", "Immutable runtime"], BLUE, BLUE_DARK)
    box(draw, (630, 280, 970, 620), "Live node", ["Bounded lifetime", "Observe + drain", "No in-place drift"], GOLD, GOLD_DARK)
    box(draw, (1160, 280, 1500, 620), "Replacement", ["Recreate", "Reattach workload", "Delete old node"], GREEN, GREEN_DARK)
    arrow(draw, (440, 450), (630, 450))
    arrow(draw, (970, 450), (1160, 450))
    arrow(draw, (1330, 620), (270, 720), RED_DARK)
    arrow(draw, (270, 720), (270, 620), RED_DARK)
    draw.text((610, 745), "repeat before persistence becomes durable", fill=RED_DARK, font=LABEL_FONT)
    save(image, "06-ephemeral-security.png")


def inductive_productization() -> None:
    image, draw = canvas(
        "Inductive Productization: Solve the Future Customer First",
        "A rare mission-critical problem can reveal a capability that later becomes general infrastructure",
        "Transcript-grounded redraw · 19:00–21:30",
    )
    stages = [
        ((90, 300, 390, 600), "One urgent case", ["Extreme constraints", "High value", "Few users"], RED, RED_DARK),
        ((470, 300, 770, 600), "Repeat", ["Find structural twins", "Separate local details"], GOLD, GOLD_DARK),
        ((850, 300, 1150, 600), "Abstract", ["Encode invariant", "Build reusable interface"], BLUE, BLUE_DARK),
        ((1230, 300, 1530, 600), "Product", ["Lower marginal cost", "New markets"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=26, body_size=20)
    arrow(draw, (390, 450), (470, 450))
    arrow(draw, (770, 450), (850, 450))
    arrow(draw, (1150, 450), (1230, 450))
    draw.text((470, 680), "Do not average away the constraint that teaches the new abstraction", fill=MUTED, font=LABEL_FONT)
    save(image, "07-inductive-productization.png")


def ooda_decision_chain() -> None:
    image, draw = canvas(
        "Project Maven Expands from Detection to a Decision Chain",
        "Computer vision accelerates Observe; operational value requires Orient, Decide and Act to remain connected",
        "Transcript-grounded redraw · 21:27–27:00",
    )
    nodes = [
        ((100, 320, 390, 600), "Observe", ["Sensors", "Imagery", "Detection"], BLUE, BLUE_DARK),
        ((480, 320, 770, 600), "Orient", ["Identity", "Context", "Confidence"], GOLD, GOLD_DARK),
        ((860, 320, 1150, 600), "Decide", ["Authority", "Legal review", "Resource choice"], PURPLE, PURPLE_DARK),
        ((1240, 320, 1530, 600), "Act", ["Tasking", "Execution", "Outcome"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in nodes:
        box(draw, bounds, title, lines, fill, outline, title_size=28, body_size=20)
    arrow(draw, (390, 460), (480, 460))
    arrow(draw, (770, 460), (860, 460))
    arrow(draw, (1150, 460), (1240, 460))
    arrow(draw, (1380, 600), (245, 720), GREEN_DARK)
    arrow(draw, (245, 720), (245, 600), GREEN_DARK)
    draw.text((660, 740), "outcomes update models, policy and planning", fill=GREEN_DARK, font=SMALL_FONT)
    save(image, "08-ooda-decision-chain.png")


def common_decision_chain() -> None:
    image, draw = canvas(
        "Government and Commercial Systems Share a Decision Skeleton",
        "Kill chain and value chain differ in stakes, but both require sensing, modeling, allocation and feedback",
        "Transcript-grounded redraw · 25:00–30:00",
    )
    box(draw, (90, 260, 610, 670), "Government", ["Policy objective", "Operational picture", "Authority + constraints", "Mission outcome"], RED, RED_DARK)
    box(draw, (990, 260, 1510, 670), "Commercial", ["Business strategy", "Operational picture", "Capital + inventory", "Customer outcome"], BLUE, BLUE_DARK)
    box(draw, (620, 330, 980, 600), "Shared software", ["Ontology", "Decision model", "Workflow", "Audit + feedback"], GREEN, GREEN_DARK)
    arrow(draw, (610, 460), (620, 460), RED_DARK)
    arrow(draw, (990, 510), (980, 510), BLUE_DARK)
    draw.text((540, 720), "Same abstraction does not mean same ethics or authority", fill=MUTED, font=LABEL_FONT)
    save(image, "09-common-decision-chain.png")


def ai_supply_demand() -> None:
    image, draw = canvas(
        "AI Value Requires a Demand-Side Machine",
        "Models resemble electricity supply; value appears when institutions redesign decisions and workflows around the capability",
        "Transcript-grounded redraw · 30:00–33:30",
    )
    box(draw, (110, 280, 500, 650), "AI supply", ["Models", "Compute", "Inference", "Benchmarks"], BLUE, BLUE_DARK)
    box(draw, (605, 280, 995, 650), "Machine layer", ["Data integration", "Workflow", "Tools", "Feedback"], GOLD, GOLD_DARK)
    box(draw, (1100, 280, 1490, 650), "Demand outcome", ["Healthcare", "Manufacturing", "Defense", "Public services"], GREEN, GREEN_DARK)
    arrow(draw, (500, 465), (605, 465))
    arrow(draw, (995, 465), (1100, 465))
    draw.text((450, 720), "More model supply alone does not specify which decisions improve", fill=RED_DARK, font=LABEL_FONT)
    save(image, "10-ai-supply-demand.png")


def manufacturing_reverse_plan() -> None:
    image, draw = canvas(
        "Supply Disruption Reverses the Planning Direction",
        "When a small component becomes scarce, planning must start from available inventory and choose the highest-value build plan",
        "Transcript-grounded redraw · 33:30–38:00",
    )
    box(draw, (100, 245, 700, 650), "Normal plan: left → right", ["Customer orders", "Bill of materials", "Supplier schedule", "Factory plan"], BLUE, BLUE_DARK)
    box(draw, (900, 245, 1500, 650), "Disrupted plan: right → left", ["Available inventory", "Feasible configurations", "Margin / mission value", "Orders to fulfill"], GOLD, GOLD_DARK)
    arrow(draw, (720, 450), (880, 450), RED_DARK)
    draw.text((650, 395), "constraint shock", fill=RED_DARK, font=SMALL_FONT)
    draw.text((460, 720), "Operational software must support both planning directions", fill=MUTED, font=LABEL_FONT)
    save(image, "11-manufacturing-reverse-plan.png")


def privacy_security_frontier() -> None:
    image, draw = canvas(
        "Engineering Can Push the Privacy–Security Frontier",
        "Politics chooses an acceptable point; capabilities can improve security without consuming the same amount of privacy",
        "Transcript-grounded redraw · 39:30–42:00",
    )
    draw.line((180, 690, 1450, 690), fill=INK, width=4)
    draw.line((180, 690, 180, 230), fill=INK, width=4)
    draw.text((720, 730), "Privacy protection", fill=INK, font=LABEL_FONT)
    draw.text((50, 380), "Security\ncapability", fill=INK, font=LABEL_FONT)
    curve_old = [(230, 640), (420, 590), (650, 520), (900, 430), (1180, 330)]
    curve_new = [(230, 560), (420, 500), (650, 410), (900, 310), (1180, 240)]
    draw.line(curve_old, fill=RED_DARK, width=7)
    draw.line(curve_new, fill=GREEN_DARK, width=7)
    draw.text((1050, 350), "existing frontier", fill=RED_DARK, font=SMALL_FONT)
    draw.text((1030, 210), "improved capability frontier", fill=GREEN_DARK, font=SMALL_FONT)
    arrow(draw, (760, 430), (760, 355), GREEN_DARK)
    draw.text((630, 330), "engineering gain", fill=GREEN_DARK, font=SMALL_FONT)
    save(image, "12-privacy-security-frontier.png")


def institutional_feedback() -> None:
    image, draw = canvas(
        "A Real Steering Wheel Requires an Integrated Feedback Loop",
        "Strategy and policy become performative when execution escapes into spreadsheets and outcomes return months later",
        "Transcript-grounded redraw · 42:00–44:03",
    )
    nodes = [
        ((100, 315, 390, 600), "Intent", ["Policy", "Strategy", "Target state"], BLUE, BLUE_DARK),
        ((480, 315, 770, 600), "Execution", ["Workflow", "Resources", "Constraints"], GOLD, GOLD_DARK),
        ((860, 315, 1150, 600), "Outcome", ["Operational state", "Customer / mission", "Side effects"], GREEN, GREEN_DARK),
        ((1240, 315, 1530, 600), "Learning", ["Compare", "Explain", "Update"], PURPLE, PURPLE_DARK),
    ]
    for bounds, title, lines, fill, outline in nodes:
        box(draw, bounds, title, lines, fill, outline, title_size=27, body_size=20)
    arrow(draw, (390, 455), (480, 455))
    arrow(draw, (770, 455), (860, 455))
    arrow(draw, (1150, 455), (1240, 455))
    arrow(draw, (1380, 600), (245, 730), PURPLE_DARK)
    arrow(draw, (245, 730), (245, 600), PURPLE_DARK)
    draw.text((520, 750), "if users escape to Excel, the organization loses this loop", fill=RED_DARK, font=LABEL_FONT)
    save(image, "13-institutional-feedback.png")


def main() -> None:
    infrastructure_epochs()
    heterogeneous_fleet()
    apollo_control_loop()
    release_confidence()
    rubix_layers()
    ephemeral_security()
    inductive_productization()
    ooda_decision_chain()
    common_decision_chain()
    ai_supply_demand()
    manufacturing_reverse_plan()
    privacy_security_frontier()
    institutional_feedback()


if __name__ == "__main__":
    main()

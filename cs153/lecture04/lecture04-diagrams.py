#!/usr/bin/env python3
"""Generate transcript-grounded teaching diagrams for CS153 Lecture 04."""

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
SMALL_FONT = font(20)
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


def research_trajectory() -> None:
    image, draw = canvas(
        "Research Questions Become Infrastructure Requirements",
        "Each research stage changed the state space, feedback signal and compute system the team needed",
        "Transcript-grounded redraw · 03:00–18:00",
    )
    stages = [
        (90, "Unsupervised MT", ["Align representations", "No parallel corpus"], BLUE, BLUE_DARK),
        (470, "Formal theorem proving", ["Verified actions", "Hyper-tree search"], GOLD, GOLD_DARK),
        (850, "LLaMA", ["Own the sampler", "Scale pre-training"], PURPLE, PURPLE_DARK),
        (1230, "Mistral", ["Efficient models", "Deploy + customize"], GREEN, GREEN_DARK),
    ]
    for left, title, lines, fill, outline in stages:
        box(draw, (left, 300, left + 285, 610), title, lines, fill, outline, title_size=24)
    for start_x in (375, 755, 1135):
        arrow(draw, (start_x, 455), (start_x + 95, 455))
    draw.text((320, 700), "The bottleneck moves: data → search APIs → model ownership → product operations", fill=INK, font=LABEL_FONT)
    save(image, "01-research-trajectory.png")


def cross_lingual_alignment() -> None:
    image, draw = canvas(
        "Cross-Lingual Alignment Starts from Geometry, Then Iterates",
        "A shared-space intuition bootstraps a dictionary; denoising and back-translation improve the translation model",
        "Transcript + Lample et al. 2018",
    )
    box(draw, (80, 250, 460, 590), "Language A embeddings", ["Monolingual corpus", "Local semantic geometry", "No paired sentences"], BLUE, BLUE_DARK)
    box(draw, (610, 250, 990, 590), "Alignment transform", ["Infer bilingual anchors", "Map spaces", "Build word dictionary"], GOLD, GOLD_DARK)
    box(draw, (1140, 250, 1520, 590), "Translation model", ["Denoising objective", "Back-translation", "Iterative refinement"], GREEN, GREEN_DARK)
    arrow(draw, (460, 420), (610, 420))
    arrow(draw, (990, 420), (1140, 420))
    arrow(draw, (1330, 590), (800, 730), GREEN_DARK)
    arrow(draw, (800, 730), (800, 590), GREEN_DARK)
    draw.text((365, 710), "Geometric similarity is the bootstrap, not the complete learning algorithm", fill=RED_DARK, font=LABEL_FONT)
    save(image, "02-cross-lingual-alignment.png")


def hypertree_search() -> None:
    image, draw = canvas(
        "A Proof Tactic Can Create Multiple Subgoals",
        "Formal proof search is a hypergraph problem because one action may require every resulting goal to be solved",
        "Transcript + HyperTree Proof Search · 05:00–07:00",
    )
    box(draw, (560, 210, 1040, 370), "Proof state", ["Goal: prove P(n) for all integers"], BLUE, BLUE_DARK, title_size=26)
    box(draw, (610, 445, 990, 585), "Tactic: induction", ["One verified action"], GOLD, GOLD_DARK, title_size=25)
    box(draw, (160, 670, 650, 800), "Subgoal A", ["Prove base case P(0)"], GREEN, GREEN_DARK, title_size=25)
    box(draw, (950, 670, 1440, 800), "Subgoal B", ["Prove P(n) ⇒ P(n+1)"], PURPLE, PURPLE_DARK, title_size=25)
    arrow(draw, (800, 370), (800, 445))
    arrow(draw, (720, 585), (420, 670))
    arrow(draw, (880, 585), (1190, 670))
    draw.text((118, 530), "AND condition", fill=RED_DARK, font=font(23))
    draw.text((118, 565), "both children must close", fill=RED_DARK, font=font(20))
    save(image, "03-hypertree-search.png")


def informal_to_formal() -> None:
    image, draw = canvas(
        "Informal Reasoning Proposes; the Formal Prover Disposes",
        "An LLM proof sketch narrows search, but only the proof assistant can accept the final derivation",
        "Transcript-grounded redraw · 07:00–09:10",
    )
    stages = [
        ((60, 300, 330, 570), "Theorem", ["Formal statement", "Initial goals"], BLUE, BLUE_DARK),
        ((390, 300, 690, 570), "Informal LLM", ["Generate proof idea", "Use web-scale math"], GOLD, GOLD_DARK),
        ((750, 300, 1050, 570), "Formal model", ["Select tactics", "Expand hyper-tree"], PURPLE, PURPLE_DARK),
        ((1110, 300, 1540, 570), "Proof assistant", ["Type-check every step", "Accept or reject"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=25)
    arrow(draw, (330, 435), (390, 435))
    arrow(draw, (690, 435), (750, 435))
    arrow(draw, (1050, 435), (1110, 435))
    arrow(draw, (1320, 570), (900, 720), RED_DARK)
    arrow(draw, (900, 720), (900, 570), RED_DARK)
    draw.text((600, 744), "failed verification becomes search feedback", fill=RED_DARK, font=LABEL_FONT)
    save(image, "04-informal-to-formal.png")


def objective_mismatch() -> None:
    image, draw = canvas(
        "The Chinchilla Trap Is an Objective-Function Mismatch",
        "Fixed training compute and lifetime serving cost ask different optimization questions",
        "Transcript + Chinchilla + LLaMA papers · 09:20–11:40",
    )
    box(draw, (100, 250, 720, 610), "Training-compute objective", ["Budget is fixed", "Choose parameter count + tokens", "Maximize quality at train time", "Compute-optimal frontier"], BLUE, BLUE_DARK, title_size=29)
    box(draw, (880, 250, 1500, 610), "Deployment-lifetime objective", ["Serving repeats many times", "Smaller model lowers latency/cost", "Spend more tokens once", "Inference-aware over-training"], GREEN, GREEN_DARK, title_size=29)
    draw.line((800, 230, 800, 670), fill=LINE, width=3)
    draw.text((650, 690), "Same scaling law · different business objective", fill=RED_DARK, font=LABEL_FONT)
    save(image, "05-objective-mismatch.png")


def scale_amplifies_bugs() -> None:
    image, draw = canvas(
        "Scale Turns a Harmless Approximation into a Delayed Failure",
        "A precision choice can pass small experiments yet destabilize a long, expensive run",
        "Transcript-grounded redraw · 12:08–13:35",
    )
    box(draw, (80, 270, 460, 590), "Small run", ["FP16 path", "Short horizon", "Loss looks normal", "Decision: proceed"], GREEN, GREEN_DARK)
    box(draw, (610, 270, 990, 590), "Large run", ["More layers / steps", "Error accumulates", "Loss rises after days", "Cause is ambiguous"], RED, RED_DARK)
    box(draw, (1140, 270, 1520, 590), "Diagnosis", ["Compare FP16 / FP32", "Isolate subsystem", "Re-run expensive test", "Update guardrails"], GOLD, GOLD_DARK)
    arrow(draw, (460, 430), (610, 430))
    arrow(draw, (990, 430), (1140, 430))
    draw.text((365, 690), "Large-scale validation is not a bigger unit test; it reveals new numerical regimes", fill=INK, font=LABEL_FONT)
    save(image, "06-scale-amplifies-bugs.png")


def rd_iceberg() -> None:
    image, draw = canvas(
        "The Final Training Run Is Only the Visible Cost",
        "Published accelerator-hours omit failed experiments, debugging, data work and tooling",
        "Transcript-grounded redraw · 14:20–17:05",
    )
    draw.rectangle((80, 400, 1520, 405), fill=BLUE_DARK)
    draw.polygon([(580, 190), (1020, 190), (900, 400), (700, 400)], fill=BLUE, outline=BLUE_DARK)
    draw.polygon([(700, 405), (900, 405), (1320, 790), (280, 790)], fill=PURPLE, outline=PURPLE_DARK)
    draw.text((660, 255), "final successful run", fill=BLUE_DARK, font=font(27))
    hidden_items = ["failed runs", "precision debugging", "data filtering", "training code", "cluster operations", "research dead ends"]
    positions = [(405, 485), (815, 485), (335, 575), (830, 575), (450, 665), (860, 665)]
    for item, position in zip(hidden_items, positions):
        draw.text(position, item, fill=INK, font=font(24))
    draw.text((480, 825), "Cost estimate without the submerged work is not an R&D estimate", fill=RED_DARK, font=LABEL_FONT)
    save(image, "07-rd-iceberg.png")


def data_heavy_team() -> None:
    image, draw = canvas(
        "A Small Model Team Can Be Data-Heavy",
        "The classroom heuristic: one training-code owner and several people iterating on data quality",
        "Transcript-grounded redraw · 17:10–18:10",
    )
    box(draw, (100, 280, 520, 620), "Training system", ["1 primary engineer", "Distributed loop", "Checkpoints", "Failure recovery"], BLUE, BLUE_DARK, title_size=29)
    box(draw, (680, 220, 1500, 680), "Data work", ["Source discovery", "Deduplication", "Filtering", "Language balance", "Quality diagnostics", "Evaluation slices"], GOLD, GOLD_DARK, title_size=29, body_size=22)
    arrow(draw, (520, 450), (680, 450))
    arrow(draw, (1090, 680), (310, 745), GREEN_DARK)
    arrow(draw, (310, 745), (310, 620), GREEN_DARK)
    draw.text((500, 770), "Training exposes data failures; data revisions change the next run", fill=GREEN_DARK, font=LABEL_FONT)
    save(image, "08-data-heavy-team.png")


def checkpoint_to_solution() -> None:
    image, draw = canvas(
        "A Checkpoint Is Not a Production Solution",
        "Useful systems add runtime, interfaces, application logic and operations around model weights",
        "Transcript-grounded redraw · 20:25–24:30",
    )
    stages = [
        (50, "Weights", ["Parameters", "Tokenizer"], BLUE, BLUE_DARK),
        (350, "Runtime", ["GPU kernels", "Memory / batching"], GOLD, GOLD_DARK),
        (650, "Endpoint", ["Auth / quotas", "Stable API"], PURPLE, PURPLE_DARK),
        (950, "Application", ["Tools / retrieval", "Workflow logic"], GREEN, GREEN_DARK),
        (1250, "Operations", ["Eval / safety", "Observe / update"], RED, RED_DARK),
    ]
    for left, title, lines, fill, outline in stages:
        box(draw, (left, 300, left + 250, 600), title, lines, fill, outline, title_size=24, body_size=19)
    for start_x in (300, 600, 900, 1200):
        arrow(draw, (start_x, 450), (start_x + 50, 450))
    draw.text((390, 705), "A downloadable artifact solves only the first layer", fill=RED_DARK, font=LABEL_FONT)
    save(image, "09-checkpoint-to-solution.png")


def deployment_modes() -> None:
    image, draw = canvas(
        "Deployment Mode Is a Constraint Choice",
        "Control, data residency, update speed and hardware limits determine where a model should run",
        "Transcript-grounded redraw · 20:25–24:30 and 32:00–36:45",
    )
    modes = [
        ((70, 250, 405, 650), "External API", ["Low setup", "Provider controls runtime", "Fast model updates", "Data leaves perimeter"], BLUE, BLUE_DARK),
        ((445, 250, 780, 650), "Private cloud", ["Dedicated environment", "Customer network", "Managed elasticity", "More integration work"], PURPLE, PURPLE_DARK),
        ((820, 250, 1155, 650), "On-prem", ["Data residency", "Customer control", "Capacity planning", "Slower upgrades"], GOLD, GOLD_DARK),
        ((1195, 250, 1530, 650), "Edge", ["Small footprint", "Intermittent links", "Custom modalities", "Tight power / latency"], GREEN, GREEN_DARK),
    ]
    for bounds, title, lines, fill, outline in modes:
        box(draw, bounds, title, lines, fill, outline, title_size=27, body_size=19)
    draw.text((380, 720), "No mode dominates; architecture follows the non-negotiable constraint", fill=INK, font=LABEL_FONT)
    save(image, "10-deployment-modes.png")


def customization_loop() -> None:
    image, draw = canvas(
        "Customization Is an Evaluation-Driven Loop",
        "A few examples help only when data generation, training, evaluation and deployment remain connected",
        "Transcript-grounded redraw · 22:40–24:30",
    )
    stages = [
        ((70, 320, 330, 570), "Use case", ["Task + constraints", "Failure definition"], BLUE, BLUE_DARK),
        ((390, 230, 680, 480), "Data", ["Real examples", "Synthetic generation"], GOLD, GOLD_DARK),
        ((760, 230, 1050, 480), "Fine-tune", ["Adapt behavior", "Preserve base skills"], PURPLE, PURPLE_DARK),
        ((1130, 320, 1530, 570), "Evaluate", ["Task metrics", "Safety + regression"], GREEN, GREEN_DARK),
        ((600, 650, 1000, 810), "Deploy + observe", ["Runtime traces · user failures · new data"], RED, RED_DARK),
    ]
    for bounds, title, lines, fill, outline in stages:
        box(draw, bounds, title, lines, fill, outline, title_size=25, body_size=19)
    arrow(draw, (330, 420), (390, 355))
    arrow(draw, (680, 355), (760, 355))
    arrow(draw, (1050, 355), (1130, 420))
    arrow(draw, (1330, 570), (1000, 700))
    arrow(draw, (600, 730), (200, 570), RED_DARK)
    save(image, "11-customization-loop.png")


def product_feedback_flywheel() -> None:
    image, draw = canvas(
        "A Consumer Product Can Be a Learning Instrument",
        "Serving, tools and explicit feedback reveal where the model fails and what the next training cycle should target",
        "Transcript-grounded redraw · 24:45–27:40",
    )
    box(draw, (100, 290, 440, 590), "Le Chat experience", ["Fast answers", "Web search", "Code interpreter"], BLUE, BLUE_DARK)
    box(draw, (630, 210, 970, 510), "Usage evidence", ["Thumbs up / down", "Failure categories", "Task distribution"], GOLD, GOLD_DARK)
    box(draw, (1160, 290, 1500, 590), "Training priorities", ["Data slices", "Tool reliability", "Model weaknesses"], GREEN, GREEN_DARK)
    box(draw, (630, 620, 970, 800), "Serving constraint", ["Speed may reduce update flexibility"], RED, RED_DARK, title_size=25)
    arrow(draw, (440, 430), (630, 360))
    arrow(draw, (970, 360), (1160, 430))
    arrow(draw, (1330, 590), (970, 710), GREEN_DARK)
    arrow(draw, (630, 710), (270, 590), GREEN_DARK)
    save(image, "12-product-feedback-flywheel.png")


def reasoning_verifier_loop() -> None:
    image, draw = canvas(
        "Reasoning Training Needs an Environment and a Verifier",
        "The scalable unit is not chain-of-thought text alone but a task loop with checkable outcomes",
        "Transcript-grounded redraw · 27:45–30:45",
    )
    box(draw, (80, 300, 390, 590), "Task environment", ["Math / code / tool task", "State + actions"], BLUE, BLUE_DARK)
    box(draw, (500, 230, 810, 520), "Policy model", ["Generate candidates", "Allocate test-time compute"], PURPLE, PURPLE_DARK)
    box(draw, (920, 300, 1230, 590), "Verifier", ["Check answer / trace", "Produce reward signal"], GREEN, GREEN_DARK)
    box(draw, (1320, 300, 1540, 590), "Update", ["RL / filtering", "New policy"], GOLD, GOLD_DARK, title_size=24)
    arrow(draw, (390, 445), (500, 375))
    arrow(draw, (810, 375), (920, 445))
    arrow(draw, (1230, 445), (1320, 445))
    arrow(draw, (1430, 590), (655, 730), RED_DARK)
    arrow(draw, (655, 730), (655, 520), RED_DARK)
    draw.text((420, 770), "Negative results about failed reward/search methods are part of the evidence", fill=RED_DARK, font=font(22))
    save(image, "13-reasoning-verifier-loop.png")


def post_training_os() -> None:
    image, draw = canvas(
        "Post-Training Is an Operating System, Not One Recipe",
        "Fast iteration requires versioned data, environments, evaluation, serving and safety to move together",
        "Transcript-grounded redraw · 37:10–39:25",
    )
    layers = [
        (220, "Product tasks and user workflows", "What must improve, for whom, under which constraint", BLUE, BLUE_DARK),
        (340, "Environments + verifiers + evaluations", "Checkable outcomes, regressions, safety and business metrics", GOLD, GOLD_DARK),
        (460, "Data generation + preference / RL training", "Curate evidence and update policy behavior", PURPLE, PURPLE_DARK),
        (580, "Serving + tools + observability", "Run the system, collect traces and expose failure modes", GREEN, GREEN_DARK),
        (700, "Versioning + governance", "Reproducibility, approvals, rollback and ownership", RED, RED_DARK),
    ]
    for top, title, detail, fill, outline in layers:
        box(draw, (180, top, 1420, top + 92), title, [detail], fill, outline, title_size=25, body_size=18)
    save(image, "14-post-training-os.png")


def privacy_reliability() -> None:
    image, draw = canvas(
        "Privacy and Reliability Select the Architecture",
        "Sensitive organizations buy control over data, dependencies and failure recovery—not only benchmark quality",
        "Transcript-grounded redraw · 35:40–37:10",
    )
    box(draw, (100, 260, 480, 590), "Privacy", ["Data residency", "Access control", "Audit boundary"], BLUE, BLUE_DARK)
    box(draw, (610, 260, 990, 590), "Reliability", ["Known dependencies", "Capacity ownership", "Failure recovery"], GOLD, GOLD_DARK)
    box(draw, (1120, 260, 1500, 590), "Control", ["Version choice", "Update timing", "Custom behavior"], PURPLE, PURPLE_DARK)
    arrow(draw, (290, 590), (650, 735), BLUE_DARK)
    arrow(draw, (800, 590), (800, 735), GOLD_DARK)
    arrow(draw, (1310, 590), (950, 735), PURPLE_DARK)
    draw.rounded_rectangle((560, 700, 1040, 810), radius=22, fill=GREEN, outline=GREEN_DARK, width=4)
    draw.text((665, 735), "private / on-prem system", fill=GREEN_DARK, font=font(27))
    save(image, "15-privacy-reliability.png")


def open_asset_stack() -> None:
    image, draw = canvas(
        "Open Models Are Inputs to a Differentiated Product Stack",
        "A company can reuse public compute while adding domain data, tools, deployment and operational guarantees",
        "Transcript-grounded redraw · 39:30–42:30",
    )
    box(draw, (80, 260, 440, 610), "Open assets", ["Public model weights", "Research papers", "Reference runtimes"], BLUE, BLUE_DARK)
    box(draw, (520, 260, 880, 610), "Customization", ["Domain data", "Fine-tuning / RL", "Task evaluation"], GOLD, GOLD_DARK)
    box(draw, (960, 260, 1320, 610), "Product systems", ["Tools + workflows", "Serving + safety", "Feedback loop"], PURPLE, PURPLE_DARK)
    box(draw, (1380, 260, 1550, 610), "Value", ["Useful", "Reliable", "Controlled"], GREEN, GREEN_DARK, title_size=23, body_size=18)
    arrow(draw, (440, 435), (520, 435))
    arrow(draw, (880, 435), (960, 435))
    arrow(draw, (1320, 435), (1380, 435))
    draw.text((350, 705), "Value capture moves upward when base-model capability becomes reusable infrastructure", fill=INK, font=LABEL_FONT)
    save(image, "16-open-asset-stack.png")


def main() -> None:
    research_trajectory()
    cross_lingual_alignment()
    hypertree_search()
    informal_to_formal()
    objective_mismatch()
    scale_amplifies_bugs()
    rd_iceberg()
    data_heavy_team()
    checkpoint_to_solution()
    deployment_modes()
    customization_loop()
    product_feedback_flywheel()
    reasoning_verifier_loop()
    post_training_os()
    privacy_reliability()
    open_asset_stack()


if __name__ == "__main__":
    main()

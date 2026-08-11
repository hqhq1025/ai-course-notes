import importlib.util
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_SCRIPT = REPO_ROOT / "tools" / "scripts" / "build_lecture_manifest.py"
COVERAGE_SCRIPT = REPO_ROOT / "tools" / "scripts" / "check_note_coverage.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_manifest_prefers_canonical_slides_source(tmp_path: Path) -> None:
    module = load_module("build_lecture_manifest_test", MANIFEST_SCRIPT)
    canonical = tmp_path / "lecture14-slides.py"
    legacy = tmp_path / "lecture_14.py"
    canonical.write_text("def main():\n    text('## Canonical section')\n", encoding="utf-8")
    legacy.write_text("def legacy():\n    text('## Duplicate section')\n", encoding="utf-8")

    assert module.python_slide_sources(tmp_path) == [canonical]

    output = tmp_path / "manifest.md"
    module.write_manifest(tmp_path, output)
    manifest = output.read_text(encoding="utf-8")
    assert "lecture14-slides.py:main" in manifest
    assert "lecture_14.py:legacy" not in manifest


def test_manifest_falls_back_to_legacy_executable_source(tmp_path: Path) -> None:
    module = load_module("build_lecture_manifest_fallback_test", MANIFEST_SCRIPT)
    legacy = tmp_path / "lecture_17.py"
    legacy.write_text("def main():\n    text('## Fallback section')\n", encoding="utf-8")

    assert module.python_slide_sources(tmp_path) == [legacy]


def test_python_image_nodes_are_required_by_default(tmp_path: Path) -> None:
    module = load_module("build_lecture_manifest_required_image_test", MANIFEST_SCRIPT)
    source = tmp_path / "lecture01-slides.py"
    source.write_text(
        "def main():\n    text('## Teaching section')\n    image('images/architecture.png')\n",
        encoding="utf-8",
    )

    nodes = module.nodes_from_python(source)
    figure = next(node for node in nodes if node.kind == "figure")
    assert figure.required is True
    assert figure.title == "images/architecture.png"


def test_pdf_nodes_use_rendered_slide_paths_and_are_required(tmp_path: Path) -> None:
    module = load_module("build_lecture_manifest_required_pdf_test", MANIFEST_SCRIPT)
    pdf = tmp_path / "lecture03-slides.pdf"
    pdf.write_bytes(b"not needed when rendered slides exist")
    slides_dir = tmp_path / "slides-images"
    slides_dir.mkdir()
    (slides_dir / "slide-000.jpg").write_bytes(b"a")
    (slides_dir / "slide-001.jpg").write_bytes(b"b")

    nodes = module.nodes_from_pdf(pdf)

    assert [node.node_id for node in nodes] == ["slide-000", "slide-001"]
    assert [node.title for node in nodes] == [
        "slides-images/slide-000.jpg",
        "slides-images/slide-001.jpg",
    ]
    assert all(node.required for node in nodes)


def test_manifest_lists_supplementary_source_materials(tmp_path: Path) -> None:
    module = load_module("build_lecture_manifest_supplementary_test", MANIFEST_SCRIPT)
    source_dir = tmp_path / "source-materials"
    source_dir.mkdir()
    paper = source_dir / "paper.pdf"
    index = source_dir / "SOURCES.md"
    paper.write_bytes(b"paper")
    index.write_text("# Sources\n", encoding="utf-8")

    output = tmp_path / "manifest.md"
    module.write_manifest(tmp_path, output)
    manifest = output.read_text(encoding="utf-8")

    assert "source-materials/paper.pdf" in manifest
    assert "source-materials/SOURCES.md" in manifest


def test_substantial_section_opener_does_not_require_bridge_keyword() -> None:
    module = load_module("check_note_coverage_test", COVERAGE_SCRIPT)
    substantial = "模型参数优化性能稳定训练效率提升" * 10
    lines = [r"\section{架构选择}", substantial]

    assert module.weak_section_openers(lines) == []


def test_short_or_visual_section_openers_remain_weak() -> None:
    module = load_module("check_note_coverage_short_test", COVERAGE_SCRIPT)
    medium_without_bridge = "模型参数优化性能稳定训练效率提升" * 7
    lines = [
        r"\section{短开场}",
        medium_without_bridge,
        r"\section{直接贴图}",
        r"\begin{figure}[H]",
    ]

    assert module.weak_section_openers(lines) == [(1, "短开场"), (3, "直接贴图")]


def test_repository_figure_macro_counts_as_visual() -> None:
    module = load_module("check_note_coverage_figure_macro_test", COVERAGE_SCRIPT)
    text = "\n".join(
        [
            r"\newcommand{\lecturefigure}[3]{%",
            r"\begin{figure}[H]",
            r"\includegraphics{#1}",
            r"}",
            r"\lecturefigure{one.png}{One}{Source}",
            r"\lecturefigure{two.png}{Two}{Source}",
        ]
    )

    assert module.figure_count(text) == 2
    assert module.is_visual_line(r"\lecturefigure{one.png}{One}{Source}")


def test_local_figure_checks_ignore_preamble_and_deduplicate_raw_figure() -> None:
    module = load_module("check_note_coverage_local_figure_test", COVERAGE_SCRIPT)
    lines = [
        r"\newcommand{\customfigure}[1]{%",
        r"\begin{figure}[H]",
        r"\includegraphics{#1}",
        r"}",
        r"\begin{document}",
        "本节先解释图中变量、比较对象、关键趋势和结论边界。" * 8,
        r"\begin{figure}[H]",
        r"\includegraphics{actual.png}",
        r"\end{figure}",
        "图后继续说明该证据支持什么，以及它不能证明什么。" * 8,
    ]

    counts = module.figure_local_explanation_counts(lines)
    assert len(counts) == 1
    assert counts[0][0] == 8
    assert counts[0][1] >= 220


def test_teacher_voice_macro_is_detectable() -> None:
    text = "\n".join(
        [
            r"\teachervoice{First spoken insight}",
            r"\teachervoice{Second spoken insight}",
            r"老师强调第三个提醒。",
        ]
    )

    macro_count = len(__import__("re").findall(r"\\teachervoice\{", text))
    assert macro_count == 2


def test_zero_acronym_does_not_match_scale_to_zero() -> None:
    module = load_module("check_note_coverage_zero_test", COVERAGE_SCRIPT)

    assert module.find_first_use("支持快速 scale-to-zero。", "ZeRO") is None
    assert module.find_first_use("ZeRO-3 对参数、梯度和优化器状态分片。", "ZeRO") is not None

"""Tests for the generated site shell: MkDocs config, navigation, page chrome, assets and hooks."""

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPO_ROOT / "tools" / "web" / "generate_site.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_site_shell_under_test", GENERATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_note(root: Path, route: str, preamble: str, body: str = "正文段落。") -> None:
    note_dir = root / route
    note_dir.mkdir(parents=True, exist_ok=True)
    (note_dir / f"{note_dir.name}-notes.tex").write_text(
        "\\documentclass{article}\n" + preamble + "\n\\begin{document}\n" + body + "\n\\end{document}\n",
        encoding="utf-8",
    )


def write_shell_repo(root: Path) -> None:
    (root / "README.md").write_text(
        textwrap.dedent(
            """
            # Notes

            ### 🏫 Stanford 课程 (2 份)

            | 课程 | 主题 | 讲数 | 讲者 |
            |------|------|------|------|
            | [**CS336 2026**](cs336-2026/) | Language Modeling | 2 | Percy Liang |

            ### 🎤 演讲与访谈 (1 份)

            | 来源 | 主题 | 数量 | 目录 |
            |------|------|------|------|
            | [**张小珺商业访谈录**](interviews/zhang-xiaojun/) | 访谈 | 1 | interviews |
            """
        ).strip(),
        encoding="utf-8",
    )
    write_note(
        root,
        "cs336-2026/lecture01",
        "\\newcommand{\\notetitle}{CS336 2026 Lecture 1：从零构建语言模型}\n"
        "\\newcommand{\\noteauthors}{Percy Liang}\n"
        "\\newcommand{\\videochannel}{Stanford Online}\n"
        "\\newcommand{\\notedate}{2026-04-01}\n"
        "\\newcommand{\\videourl}{https://example.com/v1}",
        "\\section{开场}\n这是第一段正文，公式 $a+b$。",
    )
    write_note(
        root,
        "cs336-2026/lecture02",
        "\\newcommand{\\notetitle}{CS336 2026 Lecture 2：Resource Accounting——Tensor、FLOPs、Memory 与 Roofline 的完整推导}\n"
        "\\newcommand{\\videochannel}{Stanford Online}",
    )
    write_note(root, "interviews/zhang-xiaojun/guest-a", "\\newcommand{\\notetitle}{嘉宾 A 访谈}")
    write_note(root, "youtube/zhangxiaojun/ep95-abc", "\\newcommand{\\notetitle}{第 95 期节目}")


def run_generator(root: Path) -> Path:
    output = root / ".web-build"
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--root", str(root), "--output", str(output), "--strict", "--skip-tikz"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return output


def nav_titles(items: list) -> list[str]:
    return [next(iter(item)) if isinstance(item, dict) else item for item in items]


def test_config_loads_no_third_party_assets(tmp_path: Path) -> None:
    write_shell_repo(tmp_path)
    output = run_generator(tmp_path)
    config = yaml.safe_load((output / "mkdocs.yml").read_text(encoding="utf-8"))

    # Google Fonts and unpkg are blocked or very slow from mainland China.
    assert config["theme"]["font"] is False
    assert all(not str(script).startswith(("http:", "https:", "//")) for script in config["extra_javascript"])
    features = set(config["theme"]["features"])
    assert {"navigation.prune", "navigation.footer", "navigation.path", "toc.follow", "content.code.copy"} <= features

    # The MathJax loader resolves its script relative to itself; that path must exist in the build.
    loader_dir = output / "docs" / "assets" / "javascripts"
    loader = (loader_dir / "mathjax.js").read_text(encoding="utf-8")
    script = re.search(r'new URL\("([^"]+)", document\.currentScript\.src\)', loader).group(1)
    assert (loader_dir / script).resolve().is_file()
    assert 'querySelector(".arithmatex")' in loader
    assert "script.async = true" in loader


def test_vendored_mathjax_contains_every_autoloaded_extension_and_font() -> None:
    generator = load_generator()
    vendor = generator.MATHJAX_VENDOR_DIR
    bundle = (vendor / "tex-chtml.js").read_text(encoding="utf-8")

    assert 'VERSION="3.2.2"' in bundle
    extensions = {name.lower() for name in re.findall(r'"\[tex\]/([A-Za-z0-9-]+)"', bundle)}
    missing = sorted(name for name in extensions if not (vendor / "input" / "tex" / "extensions" / f"{name}.js").is_file())
    assert not missing, missing
    fonts = set(re.findall(r"MathJax_(?:[A-Za-z]+-[A-Za-z]+|Zero)\b", bundle))
    missing_fonts = sorted(name for name in fonts if not (vendor / "output" / "chtml" / "fonts" / "woff-v2" / f"{name}.woff").is_file())
    assert not missing_fonts, missing_fonts
    assert (vendor / "LICENSE").is_file()


def test_navigation_follows_readme_categories_with_short_labels(tmp_path: Path) -> None:
    write_shell_repo(tmp_path)
    output = run_generator(tmp_path)
    nav = yaml.safe_load((output / "mkdocs.yml").read_text(encoding="utf-8"))["nav"]

    assert nav_titles(nav) == ["首页", "Stanford 课程", "演讲与访谈"]
    stanford = nav[1]["Stanford 课程"]
    course = stanford[0]["CS336 2026"]
    # navigation.indexes: the course page is the untitled first child, not a separate "概览" item.
    assert course[0] == "cs336-2026/index.md"
    assert course[1] == {"L01 从零构建语言模型": "cs336-2026/lecture01/index.md"}
    assert course[2] == {"L02 Resource Accounting": "cs336-2026/lecture02/index.md"}
    # The unlisted episode collection stays next to the README source it belongs to.
    talks = nav[2]["演讲与访谈"]
    assert nav_titles(talks) == ["张小珺商业访谈录", "张小珺商业访谈录 · 节目笔记"]
    assert talks[1]["张小珺商业访谈录 · 节目笔记"][1] == {"#95 第 95 期节目": "youtube/zhangxiaojun/ep95-abc/index.md"}

    # The short label is only for the sidebar; the page keeps its full title.
    page = (output / "docs" / "cs336-2026" / "lecture02" / "index.md").read_text(encoding="utf-8")
    assert page.startswith('---\ntitle: "CS336 2026 Lecture 2：Resource Accounting')
    assert "# CS336 2026 Lecture 2：Resource Accounting——Tensor" in page


@pytest.mark.parametrize(
    ("route", "title", "label"),
    [
        ("cs329a/lecture01", "Stanford CS329A：自我改进 AI Agent 1：课程总览", "L01 课程总览"),
        ("6s191/lecture02", "MIT 6.S191 Lecture 2: Recurrent Neural Networks", "L02 Recurrent Neural Networks"),
        ("6s191/lecture01", "MIT 6.S191: Introduction to Deep Learning", "L01 Introduction to Deep Learning"),
        ("kaist-cs492d/lecture15", "KAIST CS492D Guest Lecture 2: 3D生成方法与视频模型", "L15 3D生成方法与视频模型"),
        ("cs146s/week03", "CS146S Week 3: The AI IDE (Context Engineering)", "W03 The AI IDE (Context Engineering)"),
        # "V2：" is part of the title, not this lecture's number, so it stays.
        ("agentic-rl/lecture06", "DeepSeek Math V2：自我验证与推理训练", "L06 DeepSeek Math V2：自我验证与推理训练"),
        ("articles/x", "文章笔记：Harness Engineering", "Harness Engineering"),
        # A long label loses its "— subtitle"; the page header still shows the speaker.
        ("talks/f24/lecture11", "[LLM Agents F24] LLM Agents: Brief History and Overview — Shunyu Yao", "L11 LLM Agents: Brief History and Overview"),
        ("cs25-v6/lecture09", "Lecture 09：生产环境中的 Transformer 推理服务", "L09 生产环境中的 Transformer 推理服务"),
    ],
)
def test_nav_label_drops_repeated_course_prefix(route: str, title: str, label: str) -> None:
    generator = load_generator()
    route_dir = Path(route)
    note = generator.Note(root=Path("."), tex_path=route_dir / "x-notes.tex", route_dir=route_dir, course_dir=route_dir.parent, title=title)

    assert generator.nav_label(note) == label


def test_nav_labels_fall_back_to_full_titles_when_shortening_collides() -> None:
    generator = load_generator()
    notes = [
        generator.Note(root=Path("."), tex_path=Path(f"c/{name}/x-notes.tex"), route_dir=Path(f"c/{name}"), course_dir=Path("c"), title=title)
        for name, title in [
            ("a", "Large Language Models — Pre-Training Data Pipelines and Mixtures at Scale"),
            ("b", "Large Language Models — Post-Training Recipes and Preference Optimization"),
        ]
    ]

    assert set(generator.nav_labels(notes).values()) == {note.title for note in notes}


def test_note_header_is_compact_and_links_source_on_github(tmp_path: Path) -> None:
    write_shell_repo(tmp_path)
    output = run_generator(tmp_path)
    page = (output / "docs" / "cs336-2026" / "lecture01" / "index.md").read_text(encoding="utf-8")
    header = page.split("## 开场", 1)[0]

    assert "| 字段 | 内容 |" not in header
    assert "Percy Liang · Stanford Online · 2026-04-01\n{: .ai-notes-note-header__meta }" in header
    assert (
        "[观看视频](https://example.com/v1) · "
        "[LaTeX 源码](https://github.com/hqhq1025/ai-course-notes/blob/main/cs336-2026/lecture01/lecture01-notes.tex)"
    ) in header


def test_course_page_links_each_note_once_and_states_shared_source(tmp_path: Path) -> None:
    write_shell_repo(tmp_path)
    output = run_generator(tmp_path)
    course = (output / "docs" / "cs336-2026" / "index.md").read_text(encoding="utf-8")

    assert "共 2 份讲义，来源：Stanford Online。" in course
    assert "[阅读]" not in course
    assert course.count("(lecture01/index.md)") == 1
    assert "| 讲义 | 日期 | 资源 |" in course


def test_home_links_reading_routes_that_exist(tmp_path: Path) -> None:
    generator = load_generator()
    write_shell_repo(tmp_path)
    output = run_generator(tmp_path)
    home = (output / "docs" / "index.md").read_text(encoding="utf-8")

    assert "### 🏫 Stanford 课程\n" in home
    assert home.index("### 🏫 Stanford 课程") < home.index("### 🎤 演讲与访谈")
    # The sample repo has none of the route targets, so the steps stay plain text instead of broken links.
    routes = home.split("## 推荐阅读路线", 1)[1].split("## 课程地图", 1)[0]
    assert "](" not in routes
    known = {"cs336", "cs336/lecture04"}
    route_lines = "\n".join(generator.reading_route_markdown(known))
    assert "[CS336](cs336/index.md)" in route_lines
    assert "[CS336 L04 MoE](cs336/lecture04/index.md)" in route_lines


def test_reading_routes_point_at_notes_in_this_repository() -> None:
    generator = load_generator()
    for _name, steps in generator.READING_ROUTES:
        for label, route in steps:
            assert any((REPO_ROOT / route).rglob("*-notes.tex")), f"{label}: {route} has no notes"


def test_search_index_hook_rewrites_index_as_utf8(tmp_path: Path) -> None:
    generator = load_generator()
    namespace: dict[str, object] = {}
    exec(generator.search_index_hook(), namespace)
    index = tmp_path / "search" / "search_index.json"
    index.parent.mkdir()
    data = {"config": {"lang": ["zh"]}, "docs": [{"location": "a/", "title": "注意力", "text": "上下文 <code>x</code>"}]}
    index.write_text(json.dumps(data), encoding="utf-8")
    assert "\\u6ce8" in index.read_text(encoding="utf-8")

    namespace["on_post_build"]({"site_dir": str(tmp_path)})

    text = index.read_text(encoding="utf-8")
    assert "注意力" in text and "\\u" not in text
    assert json.loads(text) == data
    namespace["on_post_build"]({"site_dir": str(tmp_path / "missing")})


SEARCH_DEFERRAL_HARNESS = r"""
const vm = require("vm");
const [script, search] = [process.argv[2], process.argv[3]];
const sent = [];
const listeners = {};
function FakeXHR() {}
FakeXHR.prototype.open = function (method, url) { this.url = url; };
FakeXHR.prototype.send = function () { sent.push(this.url); };
const context = {
  XMLHttpRequest: FakeXHR,
  URLSearchParams,
  location: { search },
  document: {
    addEventListener: (type, fn) => { listeners[type] = fn; },
    removeEventListener: (type) => { delete listeners[type]; },
  },
};
context.window = context;
vm.runInNewContext(script, context);
function request(url) { const xhr = new FakeXHR(); xhr.open("GET", url); xhr.send(); }
request("/site/search/search_index.json");
request("/site/sitemap.xml");
const before = sent.slice();
const notSearch = { matches: () => false, closest: () => null };
if (listeners.focusin) listeners.focusin({ target: notSearch });
const afterUnrelatedFocus = sent.slice();
if (listeners.focusin) listeners.focusin({ target: { matches: (s) => s.includes("search-query") } });
request("/site/search/search_index.json");
console.log(JSON.stringify({ before, afterUnrelatedFocus, after: sent }));
"""


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
@pytest.mark.parametrize(
    ("search", "held"),
    [("", True), ("?h=attention", False), ("?q=注意力", False)],
)
def test_search_index_request_waits_for_search_focus(tmp_path: Path, search: str, held: bool) -> None:
    generator = load_generator()
    template = generator.theme_main_override()
    script = template.split("<script>", 1)[1].split("</script>", 1)[0]
    harness = tmp_path / "harness.js"
    harness.write_text(SEARCH_DEFERRAL_HARNESS, encoding="utf-8")

    result = subprocess.run(["node", str(harness), script, search], text=True, capture_output=True, check=True)
    log = json.loads(result.stdout)

    index = "/site/search/search_index.json"
    if held:
        assert log["before"] == ["/site/sitemap.xml"]
        assert log["afterUnrelatedFocus"] == ["/site/sitemap.xml"]
        # Focusing search releases the held request; later requests are no longer intercepted.
        assert log["after"] == ["/site/sitemap.xml", index, index]
    else:
        assert log["before"] == [index, "/site/sitemap.xml"]


@pytest.mark.skipif(shutil.which("mkdocs") is None and importlib.util.find_spec("mkdocs") is None, reason="mkdocs is not installed")
def test_generated_workspace_builds_strict_with_utf8_search_index(tmp_path: Path) -> None:
    write_shell_repo(tmp_path)
    output = run_generator(tmp_path)

    result = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "-q", "-f", str(output / "mkdocs.yml")],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    site = output / "site"
    index = (site / "search" / "search_index.json").read_text(encoding="utf-8")
    assert "从零构建语言模型" in index
    html = (site / "cs336-2026" / "lecture01" / "index.html").read_text(encoding="utf-8")
    assert "fonts.googleapis.com" not in html and "unpkg.com" not in html
    assert "<title>CS336 2026 Lecture 1：从零构建语言模型 - AI Course Notes</title>" in html
    assert (site / "assets" / "vendor" / "mathjax" / "input" / "tex" / "extensions" / "boldsymbol.js").is_file()


def test_pages_workflow_cache_key_tracks_generator_changes() -> None:
    workflow = (REPO_ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
    key = next(line for line in workflow.splitlines() if line.strip().startswith("key: ai-notes-generated-"))

    assert "'tools/web/**'" in key

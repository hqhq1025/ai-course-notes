"""Build a single-episode website preview.

This command only writes local artifacts. It never publishes or changes Git.
Run with the same Python environment that provides the website dependencies.
"""

import subprocess
import sys
from pathlib import Path


EPISODE = Path(__file__).resolve().parent.parent
REPO = EPISODE.parents[2]
PREVIEW = Path("/tmp/sv101-web-preview")


def build_preview():
    # Importing from the repository reuses its converters, theme and asset rules.
    sys.path.insert(0, str(REPO))
    from tools.web import generate_site as site

    tex = EPISODE / f"{EPISODE.name}-notes.tex"
    if not tex.is_file():
        raise FileNotFoundError(f"Render the final note first: {tex.name}")
    original_discover = site.discover_notes
    site.discover_notes = lambda root: [site.parse_note(root, tex)]
    try:
        result = site.build_site(
            REPO, PREVIEW,
            strict=True,
            fail_on_tikz_warnings=True,
            fail_on_pdf_figure_warnings=True,
            fail_on_latex_leaks=True,
            render_tikz=True,
            verbose_warnings=True,
            compress_images=True,
            image_max_width=1600,
            jpeg_quality=82,
            cache_root=None,
        )
    finally:
        site.discover_notes = original_discover
    if result:
        raise RuntimeError(f"Website source generation failed with status {result}")
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "-f",
         str(PREVIEW / "mkdocs.yml"), "--strict"],
        cwd=REPO, check=True,
    )
    print(f"Website preview built in {PREVIEW / 'site'}", flush=True)


if __name__ == "__main__":
    build_preview()

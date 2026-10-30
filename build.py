#!/usr/bin/env python3
"""Build the Builders hub into a single, self-contained index.html.

What it does
  1. Reads the hub template            src/hub.html
  2. Pulls CSS, demos and data out of  vendor/ui-patterns-library.html
     (the UI Patterns library, used as-is so every pattern plays its real demo)
  3. Embeds the AI Card family fronts   assets/fronts/<family>.webp
  4. Writes                            index.html

No dependencies beyond Python 3.8+. Run:  python3 build.py
"""
import base64
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
TEMPLATE = ROOT / "src" / "hub.html"
LIBRARY = ROOT / "vendor" / "ui-patterns-library.html"
FRONTS = ROOT / "assets" / "fronts"
OUT = ROOT / "index.html"

FAMILIES = ["understand", "communicate", "think", "action", "explain", "collab"]


def between(text, start, end, start_offset=0):
    i = text.index(start) + start_offset
    return text[i:text.index(end, i)]


def library_parts(lib: str):
    """Return (css, js) extracted from the UI Patterns library file."""
    css = between(lib, "<style>", "</style>", len("<style>"))
    # The library sets its tokens on :root; inside each demo's shadow root that becomes :host.
    css = css.replace(":root{", ":host{", 1)

    js = lib[lib.index("<script>") + len("<script>"):]
    helpers = js[js.index("const RM"):js.index("const $ =")]          # wait(), type(), motion flags
    data_start = js.index("const CAPS = [")
    data_end = js.index("\n", js.index("const SURF")) + 1                  # CAPS, P, SURF
    demos_start = js.index("const D = {")
    demos_end = js.index("\n};", demos_start) + 3                          # every pattern demo
    return css, helpers + "\n" + js[data_start:data_end] + "\n" + js[demos_start:demos_end]


def fronts_json() -> str:
    images = {}
    for fam in FAMILIES:
        path = FRONTS / f"{fam}.webp"
        if path.exists():
            images[fam] = "data:image/webp;base64," + base64.b64encode(path.read_bytes()).decode()
        else:
            print(f"  note: {path.name} missing — that family front falls back to the CSS rendition")
    return json.dumps(images)


def safe(s: str) -> str:
    """Keep injected code from closing the surrounding <script>."""
    return s.replace("</", "<\\/")


def main():
    for p in (TEMPLATE, LIBRARY):
        if not p.exists():
            sys.exit(f"Missing {p.relative_to(ROOT)}")
    tpl = TEMPLATE.read_text(encoding="utf-8")
    css, js = library_parts(LIBRARY.read_text(encoding="utf-8"))

    for marker in ("/*__LIB_CSS__*/''", "/*__LIB_JS__*/", "const FRONT_IMG={};"):
        if marker not in tpl:
            sys.exit(f"Template marker not found: {marker}")

    html = (tpl
            .replace("/*__LIB_CSS__*/''", safe(json.dumps(css)))
            .replace("/*__LIB_JS__*/", safe(js))
            .replace("const FRONT_IMG={};", "const FRONT_IMG=" + fronts_json() + ";"))
    OUT.write_text(html, encoding="utf-8")
    print(f"Built {OUT.relative_to(ROOT)} ({len(html.encode()) // 1024} KB)")


if __name__ == "__main__":
    main()

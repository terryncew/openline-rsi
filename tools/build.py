#!/usr/bin/env python3
"""Build the openline-rsi v0 static site.

Reads the structured data (site/data/*.json) and injects it into the HTML
templates (site/templates/*.html) at their markers, writing the finished
pages to site/*.html — so the pages work from file:// with no backend.

Deterministic: the same inputs always produce the same bytes.

Usage: python3 tools/build.py   (run from the repo root)
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
TEMPLATES = os.path.join(SITE, "templates")


def load(name):
    with open(os.path.join(SITE, "data", name), encoding="utf-8") as f:
        return json.load(f)


def inject(template_name, injections):
    src = os.path.join(TEMPLATES, template_name)
    dst = os.path.join(SITE, template_name)
    with open(src, encoding="utf-8") as f:
        html = f.read()
    for marker, payload in injections:
        token = "<!--__" + marker + "__-->"
        if token not in html:
            print(f"FAIL: marker {token} not found in template {template_name}")
            return False
        blob = json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False)
        html = html.replace(token, blob, 1)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(html)
    return True


def main():
    replay = load("replay.json")
    contrast = load("contrast.json")
    manifest = load("manifest.json")

    ok = True
    ok &= inject("index.html", [("REPLAY_JSON", replay), ("MANIFEST_JSON", manifest)])
    ok &= inject("investigations.html", [
        ("CONTRAST_JSON", contrast),
        ("REPLAY_JSON", replay),
        ("MANIFEST_JSON", manifest),
    ])
    if not ok:
        return 1
    print("built site/index.html, site/investigations.html (data inlined)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Regenerate index.html's game list from games.json. Run from the repo root:
    python3 scripts/render-index.py
Idempotent: safe to run repeatedly, only touches the block between the two markers.
"""
import json
import re
import sys
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
GAMES_JSON = ROOT / "games.json"
INDEX_HTML = ROOT / "index.html"
START = "<!-- GAMES-LIST-START -->"
END = "<!-- GAMES-LIST-END -->"


def render_card(game: dict) -> str:
    slug = game["slug"]
    title = escape(game["title"])
    desc = escape(game.get("description", ""))
    return (
        f'<a class="game" href="{escape(slug)}/">'
        f"<h2>{title}</h2>"
        f"<p>{desc}</p>"
        f"</a>"
    )


def main() -> int:
    games = json.loads(GAMES_JSON.read_text())
    if not isinstance(games, list):
        print("games.json must be a JSON array", file=sys.stderr)
        return 1

    if games:
        block = f'<div class="grid">\n' + "\n".join(render_card(g) for g in games) + "\n</div>"
    else:
        block = '<div class="empty">Nothing published yet — check back soon.</div>'

    html = INDEX_HTML.read_text()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(html):
        print(f"markers {START} / {END} not found in {INDEX_HTML}", file=sys.stderr)
        return 1

    new_html = pattern.sub(f"{START}\n{block}\n{END}", html)
    INDEX_HTML.write_text(new_html)
    print(f"rendered {len(games)} game(s) into {INDEX_HTML}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Games

Free browser games — memory, focus and fun. No install, no account, just tap and play.

Live at: **https://instructset.github.io/hbgGames/**

## What this is

A small collection of self-contained, single-file HTML5 games. Each one runs entirely in
your browser — no server, no tracking, no external requests.

## How this repo works

- `index.html` — the landing page. Its game list (between the `GAMES-LIST-START`/`-END`
  markers) is generated from `games.json` — don't hand-edit that block.
- `games.json` — the source of truth for what's listed: `slug`, `title`, `description` per
  game.
- `scripts/render-index.py` — regenerates `index.html`'s list from `games.json`. Run it
  after any change to `games.json`.
- `<slug>/` — one folder per game, each a self-contained `index.html`.

## Content policy

No medical, clinical, or treatment claims — these are cognitive/memory games, not therapy
or a cure for anything.

## License

All rights reserved — see [LICENSE](LICENSE). Playing the games is free; reuse of the code
or content is not.

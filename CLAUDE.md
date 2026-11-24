# Rules for reproducing designs

This repo is the design source of truth for philmanyeung.com (`philmany/py-portfolio`).

1. Read `tokens.css` and the doc for what you're building before writing CSS.
2. Use tokens only. No raw hex, px font sizes, durations or easings in components. If a value is missing, add a token here first, then use it.
3. Reuse existing classes from `py-portfolio/styles.css` before inventing new ones. Match `docs/components.md` exactly (sizes, gaps, states).
4. Transitions: opacity/colour/filter use `--fade-*`; transforms/clip/size use `--move-*`. Never mix.
5. Every interactive element: 44px target, `:focus-visible` ring, keyboard path, Escape closes what it opened, `aria-pressed`/`aria-expanded` for state.
6. Anything moving >5s must stop under `html.motion-paused` and `prefers-reduced-motion`. Decorative loops: 3 cycles max.
7. Two accents only: tangerine `--accent-2` for action/emphasis, teal `--accent` for state/place.
8. Serif headings always tight (`--track-display` + `--word-display`), emphasis via `<em>` italic tangerine.
9. Changing `tokens.css`: run `python3 scripts/build_json.py` and copy the file to `py-portfolio/tokens.css` verbatim.
10. Docs stay terse: specs and rules, no marketing copy.

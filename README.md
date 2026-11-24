# py design system

Design source of truth for [philmanyeung.com](https://philmanyeung.com) (`philmany/py-portfolio`): spacing, type, colour, treatments, motion. Internal.

| File | Holds |
| --- | --- |
| `tokens.css` | Every token as a CSS custom property, plus `@font-face` and Reduce Motion overrides. **The source of truth.** |
| `tokens.json` | Same tokens in W3C design-token format (Figma, other tools). Generated. |
| `docs/foundations.md` | Colour, type ramp, space, layout, shape, elevation, layers |
| `docs/motion.md` | Durations, easings, every named animation, pausing, Reduce Motion |
| `docs/components.md` | Specs for each component, by its class in `styles.css` |
| `docs/treatments.md` | Riso water, halftone, glass, paper, outlines, logo |
| `docs/accessibility.md` | WCAG 2.2 AA + Apple HIG rules and the pre-ship checklist |
| `CLAUDE.md` | Rules for agents reproducing designs with this system |

## Change a token

1. Edit `tokens.css` here.
2. `python3 scripts/build_json.py`
3. Copy to the site: `cp tokens.css ../py-portfolio/tokens.css`
4. If the change alters a rule, update the matching doc.

The site links `/tokens.css` before `/styles.css` on every page; `styles.css` uses only tokens.

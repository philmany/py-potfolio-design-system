# Accessibility

Target: WCAG 2.2 AA, plus Apple Human Interface Guidelines where they're stricter. Checked Nov 2026.

## Rules

| Rule | Standard | How |
| --- | --- | --- |
| Text contrast >= 4.5:1 (large 3:1) | WCAG 1.4.3 | Palette passes at 7.9:1 minimum. Dimmed text floor: opacity 0.72 |
| Focus visible, 2px teal, 4px offset | WCAG 2.4.7, 2.4.13 | Global `:focus-visible`. On tangerine fills, ring is `--text` |
| Focus not hidden by the fixed nav | WCAG 2.4.11 | `scroll-padding-top: --nav-h`; nav reappears on `focusin` |
| Targets >= 44x44 | HIG (WCAG 2.5.8 asks 24) | `min-height: --target`; small text links get an invisible `::after` hit area: `top/bottom: min(0px, calc((100% - var(--target)) / 2))`, sides -8px |
| Text scales with user setting | WCAG 1.4.4, HIG Dynamic Type | Type tokens in rem |
| 12px text floor (11px inline badge only) | HIG | Ramp in foundations |
| Pause, stop, hide | WCAG 2.2.2 | `motion.js` + `[data-motion-toggle]`; loops capped at 3 cycles where decorative |
| Reduce Motion | WCAG 2.3.3, HIG | `move-*` to 0, fades to 200ms, loops off (see motion.md) |
| Hover/focus content dismissable, hoverable, persistent | WCAG 1.4.13 | Escape closes tooltip, preview, memory, paper notes; cards stay while hovered |
| Toggle state | ARIA | `aria-pressed`; label constant |
| Decorative art hidden | WCAG 1.1.1 | Canvases `aria-hidden`; interactive art (fish, outlines) is a `<button>` with a label |
| Rolodex readable | WCAG 1.3.1 | Flipping words `aria-hidden`; full list in `.sr` |
| Skip link | WCAG 2.4.1 | `.skip` first on every page |
| Live updates | WCAG 4.1.3 | Shuffle status and lightbox counter `aria-live="polite"` |
| New tab warning | WCAG 3.2.5 (AAA, kept) | Tooltip via `aria-describedby` on every `target="_blank"` |
| Hover-only features | WCAG 2.5 | `(hover: hover)` gate; touch gets a tap path and "Tap" copy |

## Before shipping a new component

1. All values from tokens. No raw colours, sizes, durations.
2. Contrast checked against the surface it sits on, including over art (use `--feather` or glass).
3. 44px target, visible focus, keyboard path, Escape closes anything that opened.
4. Motion uses the right family (`fade-*` vs `move-*`), pauses with `motion-paused`, and reads fine with Reduce Motion.
5. Screen-reader name and state set; decorative parts hidden.

## Exceptions on record

- Brand logos at 0.32 opacity: logotypes are exempt from contrast.
- Lake colours depend on the moving water; hero text sits on a dimmed, masked centre and stays above 11:1 against `--bg`.

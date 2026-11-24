# Foundations

All values live in `tokens.css`. Use the token, never the literal.

## Color

One dark surface, warm white text, two accents. Never add a third accent.

| Token | Value | Use | Contrast on `--bg` |
| --- | --- | --- | --- |
| `--bg` | `#140a18` | Page | |
| `--bg-2` | `#1e1223` | Preview frame, photo tile | |
| `--surface` | `#1a0f1f` | Solid cards (memory card, portrait) | |
| `--glass` | bg @ 0.76 + `blur(--blur)` | Nav, chips, captions | |
| `--glass-strong` | bg @ 0.92 | Tooltip, caption gradient | |
| `--glass-raised` / `-hover` | `rgba(30,18,35,.86)` / `rgba(40,25,47,.94)` | Pill and icon buttons over art | |
| `--scrim` | `rgba(12,6,15,.96)` | Lightbox | |
| `--text` | `#f3ede8` | Body, titles | 16.6:1 |
| `--text-strong` | `#fff` | Names, lockups, outlines | 19:1 |
| `--text-2` | text @ 0.84 | Lede over the lake | 11.4:1 |
| `--muted` | `#aea2b1` | Meta, captions, controls | 7.9:1 |
| `--line` / `--line-2` | text @ 0.12 / 0.22 | Dividers / chip borders. Decorative only | |
| `--accent` | `#5fd3c4` teal | Focus ring, dates, places, "on" states | 10.7:1 |
| `--accent-2` | `#ff8a3d` tangerine | CTA fill, `<em>` in headings, progress bar, hints | 8.2:1 |
| `--on-accent` | `= --bg` | Text on either accent | 8.2:1 |

Rules
- Tangerine = action or emphasis. Teal = state or place. Don't swap.
- Heading emphasis: `<em>` in serif italic, `--accent-2`.
- Dimming: lowest allowed is opacity 0.72 on `--muted` text (4.55:1). Logos may go lower (exempt).
- Brand logos: white SVG at opacity 0.32, 1 on hover/focus.

## Type

| Role | Family | Weight | Size token | Line | Tracking |
| --- | --- | --- | --- | --- | --- |
| Hero name | serif | 400 | `--fs-hero` | 1 | `--track-hero`, word `--word-display` |
| Section heading (Work.) | serif italic via `<em>` | 400 | `--fs-display` | `--lh-display` | `--track-display`, `--word-display` |
| Closing heading | serif | 400 | `--fs-display-xl` | `--lh-title` | same |
| Claim / ph-h2 / lockup | serif italic | 400 | `--fs-display-sm` | 0.92-0.98 | same |
| Row title | sans | 400 | `--fs-title` | `--lh-title` | `--track-title` |
| Quote line | serif italic | 400 | `--fs-quote` / `--fs-quote-sm` | 1.02-1.15 | `--track-quote` |
| Prose | sans | 400 | `--fs-prose` | `--lh-body` | -0.005em |
| Lede | sans | 400 | `--fs-lede` / `--fs-lead` | `--lh-body` | 0 |
| Body | sans | 400 | `--fs-body` (mobile `--fs-callout`) | `--lh-body` | 0 |
| Button | sans | 700 | `--fs-callout` | 1 | `--track-ui` |
| Nav, pill, card title | sans | 400-500 | `--fs-subhead` | | |
| Meta, chips, controls, footer | sans | 400 | `--fs-footnote` | | |
| Eyebrow (UPPERCASE) | sans | 400 | `--fs-caption` | | `--track-caps` |
| Inline badge (AI, Vibe-Coded) | sans | 500 | `max(--fs-caption-2, 0.2em)` | 1 | 0.06em |

Rules
- Fixed sizes follow Apple text styles (Caption 12, Footnote 13, Subheadline 15, Callout 16, Body 17, Title 3 20). 11px only for inline badges.
- Sizes are rem so browser text size scales them.
- Serif is always set tight: display tracking -0.045 to -0.05em plus negative word spacing.
- Never use 14px, 12.5px, 13.5px. Snap to the ramp.
- Fonts: ZT Nature (Regular, Italic, Bold, Bold Italic), PP Museum (Light, Regular, Ultrabold + italics). WOFF2 self-hosted in `py-portfolio/fonts/`; licensed, not stored here.

## Space

4px grid: `--space-1` (4) to `--space-30` (120). Half steps `-0-5` (2), `-1-5` (6), `-2-5` (10) are for chip padding, icon gaps and small offsets only.

Fluid layout tokens

| Token | Value | Use |
| --- | --- | --- |
| `--gutter` | clamp(20, 4vw, 56) | Page side padding, nav, hero controls |
| `--wrap` | 1240px | Max content width (`.wrap`) |
| `--section-y` | clamp(72, 9vw, 120) | Top padding of every `.section` |
| `--stack-lg` | clamp(28, 3.5vw, 48) | Heading block to list |
| `--stack-xl` | clamp(48, 6vw, 80) | Heading to a two-column grid |
| `--page-top` | clamp(150, 18vw, 240) | First block on pages without a hero |
| `--nav-h` | 64px | `scroll-padding-top`, keeps focus clear of the fixed nav |

One-off clamps for hero and About spacing stay inline in `styles.css`; reuse them by copying the selector, not by inventing a new clamp.

## Layout

- Single editorial column inside `.wrap`. Two-column grids: About (0.9fr / 1.25fr), Play (1fr / 1.7fr), Photography head (1fr / 1fr). Collapse to one column at 900px.
- Breakpoints (literal, CSS can't tokenize them): `760px` compact, `900px` medium, `640px` + fine pointer for hover previews.
- Hover-only features gate on `(hover: hover)`; touch gets the tap equivalent and copy swaps ("Hover" to "Tap").

## Shape

| Token | px | Use |
| --- | --- | --- |
| `--radius-xs` | 2 | Photo inside a snapshot |
| `--radius-sm` | 4 | Focus ring, snapshot frame, lightbox image |
| `--radius-md` | 8 | Tooltip, logo focus, switch track |
| `--radius-lg` | 12 | Memory card, paper caption |
| `--radius-xl` | 16 | Preview window, portrait |
| `--radius-pill` | 999 | Buttons, chips, cue, icon buttons |

Borders are always `--hairline` (1px). Photo grid has no radius and no gaps.

## Elevation

| Token | Use |
| --- | --- |
| `--shadow-card` | Memory card, tooltip |
| `--shadow-float` | Cursor preview |
| `--shadow-paper` | Snapshot (box-shadow) |
| `--drop-paper` / `--drop-paper-lift` | Paper notes at rest / lifted (filter) |
| `--drop-outline` | Water outlines over the lake |
| `--feather` | Dark halo so a pill reads over moving art |
| `--glow-cta` / `--glow-cta-hover` | Primary button |

## Layers

`--z-art` 1, hero text 3, hero controls 4, `--z-peek` 90, `--z-nav` 100, `--z-progress` 120, `--z-tip` 260, `--z-flow` 300, `--z-skip` 500.

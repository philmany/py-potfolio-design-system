# Treatments

The signature textures. Reproduce exactly; these are the brand more than any colour.

## Riso water (hero lake, page transition)

- Two spot-ink drums of halftone dots, printed separately, then composited.
  - Dark page: drum A `--ink-teal`, drum B `--ink-orange`, blend `screen`.
  - Cream stock: `--ink-teal-stock`, `--ink-orange-stock`, blend `multiply`.
- Drum B (orange) sits **2px above** drum A (misregistration is intentional).
- Ink split by brightness `c`: A = smooth(-0.05, 0.5, c) x (1 - 0.7 x smooth(0.66, 0.88, c)); B = min(1, 1.15 x smooth(0.6, 0.86, c)). Orange only shows on crests.
- Moiré: two fine wavy line screens per drum. Cut screen (period 2.65, thickness 1.05, wave 1.6, alpha 0.66, destination-out) and thread screen (3.7 / 0.9 / 2.2, alpha 0.3, source-atop), each slowly drifting and rotating (~0.09 and -0.19 rad).
- Dots: hex grid, pitch 14px (13 below 1200px wide, 11 below 760). Radius = pitch x 0.62 x L^0.7 x moiré factor.
- Colour ramp for single-ink views (`water.js` `STOPS`): deep `rgb(8,26,36)` through teal `rgb(44,146,142)` to tangerine `rgb(255,128,48)`, crest `rgb(255,198,140)`.
- Depth of field: far water in a separate canvas at `blur(2.2px)`, masked top 8-52%; near water masked the opposite way. Glow canvas under both at `blur(--blur)` 0.18 opacity.
- Before JS: CSS fallback of `--ink-fallback` dots, 9px grid, radial mask.

## Halftone figures

- Fish, heron, portrait placeholder: silhouette drawn off-screen, sampled on a 3px grid, dot radius 0.55 x pitch x sqrt(coverage), coverage averaged over the cell so edges don't sparkle. Fish is `--accent-2`.

## Glass

`background: var(--glass)` + `backdrop-filter: blur(var(--blur))` (8px for chips). Always with a 1px `--line-2` or `--line` edge. Over moving art, add `--feather`.

## Paper

- Snapshot: 3px `--paper` frame (2px compact), `--radius-sm`, `--shadow-paper`, tilted +-3-4deg, photo 96px tall (70 wide crops, 54/40 compact).
- Paper note: image with `--drop-paper`, rotated -10deg / 12deg, hung past the corner by 6-9%. Lifted: `--drop-paper-lift`, scale 1.22, tilt x 0.3.
- Tape: `--tape` strip 24% x 13% of the note, rotated -5deg, zig-zag clip-path ends.

## Outlines

Water bodies as white strokes: 1.8px (2.3 active), round joins, `vector-effect: non-scaling-stroke`, opacity 0.78 (1 active), `--drop-outline`. Shapes from Natural Earth / GSHHG, not to scale.

## Crayon logo

`logo.svg`: hand-drawn oil-pastel "PHILMAN", traced with grain kept, pure white. Never recolour, outline or set in a font.

## Focus dim

When one item takes focus (memory open, row hover), the rest steps back: art to 0.3, siblings to 0.25 (art) or 0.72 (text). Never below 0.72 for text.

# Components

Class names match `py-portfolio/styles.css`. Reproduce by reusing the class; specs below are for rebuilding elsewhere (Figma, another page).

## Actions

**Primary button** `.book`
- Pill, min-height `--target`, padding 0 22px, gap `--space-2`.
- Fill `--accent-2`, text `--on-accent`, `--fs-callout` 700, `--track-ui`. Trailing 16px arrow-up-right icon, stroke 1.8.
- Shadow `--glow-cta`. Hover/focus: `--accent-2-hover`, lift -2px, `--glow-cta-hover`, icon +2/-2px. Focus ring `--text` (teal on tangerine is weak).
- One per view. Outbound: `target="_blank"` + tooltip.

**Secondary pill** `.ph-shuffle`
- Pill, min-height `--target`, padding 0 18px 0 15px, 1px `--line-2`, transparent, `--fs-subhead` 500, 16px leading icon.
- Hover: border `--accent`, bg `--accent-wash`, text `--text-strong`.

**Cue pill** `.cue` (scroll cue over art)
- Pill, min-height `--target`, padding 4/10/4/5, 34px round avatar (30 compact), `--fs-subhead`, trailing caret.
- `--glass-raised` + blur 10px, border `--line-2`, shadow `--feather`. Hover: `--glass-raised-hover`, border `--accent-edge`, caret +2px down.

**Icon button** `.lb-btn`
- 48px circle, `--glass-raised`, 1px `--line-2`, 22-24px stroke icon (1.6). Hover: `--glass-raised-hover`, border `--accent`. Always has `aria-label`.

**Control** `.ctl` (quiet text toggle)
- Text button, min-height `--target`, gap `--space-2-5`, `--fs-footnote`, `--muted`; hover or pressed `--text`.
- Variants: switch `.sw` (26x15 track, 9px knob, pressed: teal track, knob +11px), pause glyph `.pz` (two bars, pressed: play triangle), sound (44px square icon).
- Uses `aria-pressed`. Label never changes with state.

**Text link**
- Inline underline draw (see motion). Nav links: `--fs-subhead`, opacity 0.8, 1 on hover/current.
- Resume link `.cv`: `--fs-footnote`, `--muted`, 1px underline offset 3px at 55% alpha; hover `--accent-2`.
- Contact links `.links a`: `--fs-link-lg`, trailing icon nudges 3/-3px.
- Small links get a 44px invisible hit area via `::after` (see accessibility).

## Labels

**Chip / tag** `.tags span`: pill, padding 5px `--space-2-5`, 1px `--line-2`, `--fs-footnote`, `--muted`. Row hover: border `--accent-edge`, text `--text`.
**Glass chip** `.wip`, `.portrait-note`: as chip plus `--glass` + `blur(--blur-sm)`, `--fs-caption`, `--text`. Sits 12-16px from the image's bottom-left.
**Inline badge** `.ai`: pill outline in `--accent-2`, `max(--fs-caption-2, 0.2em)` 500, superscript (vertical-align 2.1em, 1.2em compact).
**Eyebrow** `.eyebrow`, `.brands-h`: uppercase `--fs-caption`, `--track-caps`, `--muted`; number in `<b>` teal, tabular.
**Status** `.soon`: 7px teal dot breathing (2.4s) + `--fs-footnote` teal, `--track-label`.

## Overlays

**Tooltip** `.tip` (outbound-link warning)
- Fixed, `--glass-strong` + blur 8px, 1px `--accent-2-edge`, `--radius-md`, padding 7px 12px, `--fs-footnote` 700 tangerine, `--shadow-card`.
- Above the anchor by 10px (below by 12px for hero CTA), clamped 12px from viewport edges. Shown on hover and focus; hidden on leave, blur, scroll and Escape. Linked with `aria-describedby`.

**Memory card** `.mem-card`
- `--surface`, 1px `--line-2`, `--radius-lg`, padding 10/12, `--shadow-card`. Title `<b>` `--fs-subhead` 500; lines `--fs-caption` `--muted`; date `.when` teal.
- Sits 10px below (or above, `.up`) its outline. Enter: opacity `--fade`, rise 6px `--move-spring`.

**Cursor preview** `.peek`
- 420x263, `--radius-xl`, `--bg-2`, `--shadow-float` + 1px `--line` ring. Iframes render at 1680x1050 scaled 0.25. Caption `.cap` on a `--glass-strong` gradient, `--fs-footnote`.
- Fine pointer and >=640px only. Escape hides it.

**Lightbox** `dialog.lb`
- Native `<dialog>`, `--scrim`. Image contained, `--radius-sm`, slides from `--dx`. Close top-right, prev/next mid-sides (bottom centre on compact). Counter top-left `--fs-footnote` tabular, `aria-live="polite"`.

## Lists

**Project row** `.row > .row-link`
- Grid: 24px dot | title | tags | 22px icon, gap `--space-6`, padding clamp(18, 2.2vw, 26) 0. Compact: 12px | title | icon, tags below.
- Top hairline `--line`; last row also bottom. Teal 1px underline grows on hover.
- Dot 9px, colour `--c` (from data.js), glow 45% mix. Icon: `go` (rotates 45deg), `out` (scales 1.15), `plus` (open: 135deg).
- Title `--fs-title`. Hovered row stays full; siblings 0.72.
- Group header `.group-h`: `--fs-footnote` `--muted`, count tabular, `--space-2-5` above the first hairline.

**Place row** `.place button`: 16px dot | name `--fs-title-3` | where `--fs-subhead` muted | last `--fs-subhead` teal | 20px arrow (hover in). Compact: 14px | stacked.

**Facts list** `dl.ph-facts`: two equal columns, padding `--space-4` 0, hairlines; `dt` `--fs-subhead` muted, `dd` serif italic `--fs-quote-sm`.

## Blocks

**Nav** `.nav`: fixed, padding `--space-5` `--gutter`. Logo left (`logo.svg`, 22px tall, 18 compact), Work / Play / About right, gap clamp(18, 3vw, 36). Transparent over the hero, then `--glass` + blur + bottom `--line`. Hides on scroll down, returns on scroll up or focus.

**Progress bar** `#progress`: 2px tangerine, top, scaleX by scroll.

**Section** `.section`: `padding-top: --section-y`. Heading row `.sec-row`: heading left, hint right. Sub `.sec-sub` `--fs-lead`, max 36rem (`.lead` = `--text`).

**Brand marquee**: uppercase eyebrow, then a masked (10% fade each side) track of white logos, 64-84px tall cells, padding clamp(36, 5vw, 72).

**Hero** `.hero`: height clamp(640, 100svh, 1000). Layers: glow canvas, water canvas, haze canvas, centred text (name, tagline, CTA, resume), memory outlines, bottom control bar (memories toggle | cue | sound + pause).

**Portrait** `.portrait`: 4:5, `--radius-xl`, 1px `--line`, teal-wash radial on `--surface`, sticky at 150px (desktop). Paper notes hang over the top corners.

**Pull quote** `.ph-quote`: left 1px `--line-2` rule, serif italic `--fs-quote-sm`, attribution `--fs-footnote` muted prefixed "- ".

**Lockup** `.ph-lockup`: serif `--fs-display-sm` over italic second line sized by JS to equal width; footnote asterisk `.lk-fn` at 0.36em.

**Footer** `.foot`: three items spread (copyright, Pause motion, back link), `--fs-footnote` muted, padding 24 top 28 bottom.

**Skip link** `.skip`: first focusable element on every page, off-screen until focused, 44px tall.

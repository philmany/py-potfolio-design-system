# Motion

Water-like: things rise, settle and swell. Fast to respond, slow to arrive. Every animation is interruptible (CSS transitions or rAF), and none is required to understand content.

## Tokens

Two families, so Reduce Motion can drop travel and keep dissolves.

| Fade (opacity, color, bg, border, filter, shadow) | ms | Move (transform, translate, scale, clip-path, grid rows) | ms |
| --- | --- | --- | --- |
| `--fade-fast` | 150 | `--move-fast` | 200 |
| `--fade` | 300 | `--move` | 400 |
| `--fade-slow` | 500 | `--move-slow` | 600 |
| `--fade-reveal` | 900 | `--move-reveal` | 900 |
| | | `--move-spring` | 900 |

`--stagger` 70ms per item. `--delay-hero` 450ms (hero text waits for the lake).

| Easing | Curve | Use |
| --- | --- | --- |
| `--ease` | (0.2, 0.8, 0.2, 1) | Default for everything |
| `--ease-io` | (0.77, 0, 0.18, 1) | Expand/collapse, mask wipes, preview open |
| `--ease-spring` | (0.22, 1.28, 0.36, 1) | Objects with mass: memory zoom, snapshots, paper, logo tilt |
| `--ease-flip` | (0.3, 1.3, 0.5, 1) | Rolodex word in |
| `--ease-in` | (0.4, 0, 1, 1) | Exits only |

Rule of thumb: hover feedback uses `fade` + `move`/`move-slow`. Entrances use `*-reveal`. Physical objects use `move-spring`. Never write a raw duration in a component.

## Named animations

| Name | Trigger | Spec |
| --- | --- | --- |
| Hero entrance | `.hero.ready` after `--delay-hero` | Each child: translateY 14px + blur 6px + opacity 0 to rest, `*-reveal`, `--ease`. Stagger: tagline 2, button 4, resume 6 (x `--stagger`) |
| Reveal `.rv` | IntersectionObserver, once | translateY 36px + opacity 0 to rest, `*-reveal`. Rows stagger `--stagger` |
| Split heading `[data-split]` | Same | Each word in a clip window; inner span from translateY 135%, `--move-reveal` |
| Rolodex `{A\|B}` | Every 2400ms (data.js speed) | In: rotateX -88 to 0, `--move-slow` `--ease-flip`. Out: to 88deg, `--move` `--ease-in`. Origin 50% 50% -0.6em, perspective 400px |
| Link underline | Hover/focus | 1px `currentColor` background, size 0 to 100% from left, `--move` |
| Row hover | Hover/focus | Title translateX 14px (`--move-slow`), teal underline scaleX 0 to 1 (`--move-slow`), dot scale 1.25 + two rings (1.8s loop, 0.6s offset), siblings to opacity 0.72 |
| Panel expand | `.row.open` | grid-template-rows 0fr to 1fr, `--move-reveal` `--ease-io`; inner fades + rises 12px, delay 2 x stagger; plus icon rotates 135deg |
| Cursor preview | Hover a row (fine pointer) | clip-path circle 0% to 75%, `--move-slow` `--ease-io`; follows cursor with 0.14 lerp and tilt up to 5deg |
| Memory zoom | Click a lake outline | `.mem-fx` translate + scale, `--move-spring` `--ease-spring`; lake dims to 0.3 (`--fade-slow`), others to 0.25 |
| Snapshot | Memories toggle | From translateY 14px scale 0.86 to tilted rest (+-4deg), `--move-spring`, stagger by index |
| Paper notes | Portrait enters | From translateY -16px scale 1.14, `--move-spring`, delay `--delay-hero` + 300ms + i x 3 x stagger. Hover lifts to scale 1.22, tilt x 0.3 |
| Primary button | Hover/focus | translate 0 -2px (`--move`), glow ring 6px; arrow nudges 2px up-right. Active returns in `--move-fast` |
| Logo tilt | Hover | rotate -3deg scale 1.06, `--move-slow` `--ease-spring` |
| Nav hide | Scroll down | translateY -100%, `--move`; turns glass (`--fade-slow`) after the hero |
| Page transition | Internal link click | flow.js: page loads under riso water; opening spreads from click point over 820ms, ease-out power 1.8. Skipped under Reduce Motion |
| Marquee | Always | translateX -50% over 38s linear; pauses on hover/focus |
| Cue bob | Load | translateY -4px, 4.2s, 3 cycles then rests |
| Hint hand | Load | Wave keyframes, 2.4s, 3 cycles then rests |
| Demo fish | List in view 1s, max 2 autoplays | 2200ms in, 2000ms hold (opens preview), 2200ms out. Skipped when paused or Reduce Motion |

## Loops and pausing (WCAG 2.2.2)

- Decorative loops run 3 cycles max (cue, hand). Status loops (sound waves, "soon" dot, row rings on hover) may run while their state lasts.
- Anything that moves for more than 5s (lake, marquee, rolodex, heron fish) obeys **Pause motion**: `motion.js` toggles `html.motion-paused`, persisted in `localStorage.motion`. CSS pauses every animation; scripts read `Motion.paused()` / `Motion.on(fn)`.
- Toggles: hero control `#pause` and the footer button on Home and About. Label stays "Pause motion"; `aria-pressed="true"` = paused.

## Reduce Motion

`prefers-reduced-motion: reduce` (Apple: Reduce Motion):
- All `--move-*` become 0.01ms, so nothing travels, zooms or flips. Fades cap at 200ms (dissolve, per HIG).
- Loops stop; marquee becomes a static wrapped row; hero lake starts paused; rolodex shows the first word; demo fish and page transition are skipped.
- A visitor can still press Play motion; their choice wins.

## Do not

- Animate layout properties other than `grid-template-rows` for the panel.
- Use spring easing on opacity or color.
- Add parallax tied to scroll.
- Flash anything more than 3 times a second.

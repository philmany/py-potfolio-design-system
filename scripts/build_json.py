"""Regenerate tokens.json (W3C design-token format) from tokens.css. Run: python3 scripts/build_json.py"""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
css = (root / "tokens.css").read_text()
block = re.search(r":root\s*{(.*?)\n}", css, re.S).group(1)
reduce = dict(re.findall(r"(--[\w-]+):\s*([^;]+);", re.search(r"prefers-reduced-motion.*?:root\s*{(.*?)}", css, re.S).group(1)))
groups = [("color", r"^(bg|surface|glass|scrim|text|muted|line|accent|on-accent|ink|paper|tape)"), ("font", r"^(sans|serif)$"),
          ("fontSize", r"^fs-"), ("lineHeight", r"^lh-"), ("letterSpacing", r"^(track|word)-"), ("space", r"^(space|gutter|wrap|section|stack|page|nav)"),
          ("shape", r"^(radius|hairline|focus|target|blur)"), ("shadow", r"^(shadow|drop|feather|glow)"), ("zIndex", r"^z-"),
          ("duration", r"^(fade|move|stagger|delay)"), ("easing", r"^ease")]
types = {"color": "color", "font": "fontFamily", "fontSize": "dimension", "lineHeight": "number", "letterSpacing": "dimension", "space": "dimension",
         "shape": "dimension", "shadow": "shadow", "zIndex": "number", "duration": "duration", "easing": "cubicBezier"}
out = {}
for name, val in re.findall(r"(--[\w-]+):\s*([^;]+);", block):
    key = name[2:]
    g = next((g for g, rx in groups if re.search(rx, key)), None)
    if not g: continue
    tok = {"$value": val.strip(), "$type": types[g]}
    if name in reduce: tok["$extensions"] = {"reducedMotion": reduce[name]}
    out.setdefault(g, {})[key] = tok
(root / "tokens.json").write_text(json.dumps(out, indent=2) + "\n")
print(sum(len(v) for v in out.values()), "tokens")

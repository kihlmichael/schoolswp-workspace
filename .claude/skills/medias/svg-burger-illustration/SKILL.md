---
name: svg-burger-illustration
description: |
  Génère un fichier SVG autonome d'un burger minimaliste avec animation hover fluide qui sépare verticalement les 6 couches (bun haut, laitue, tomate, steak, fromage, bun bas) puis les réassemble au mouseout. Sortie : un seul bloc SVG, pas d'explication. Style éditorial UI premium, transitions CSS (pas SMIL), cubic-bezier/ease-in-out.
  Utilise ce skill quand l'utilisateur dit : "illustration burger SVG", "SVG burger", "animation burger", "burger interactif hover", ou veut une démo animée micro-interaction sur thème burger.
  NE PAS utiliser pour : illustration générique non-burger (utiliser `canvas-design` ou nano-banana / aidesigner), icône de menu hamburger UI (chercher Lucide / Heroicons), production HTML brand-strict (utiliser `external-cc-design`), ou animation Remotion en React (utiliser `remotion-best-practices`).

---

## Your role

You are simultaneously:
- a minimalist UI designer
- an interactive SVG expert
- an elegant micro-interaction specialist
- a rigorous front-end developer

Your output is a single SVG file — nothing else. No explanation before, no explanation after. Just the SVG code block.

## Burger composition (top to bottom)

Render these 6 layers in this visual order:
1. **Top bun** — rounded dome shape, warm amber/tan
2. **Lettuce** — irregular wavy edge, fresh green
3. **Tomato** — thin slice, vivid red
4. **Patty** — thick rounded rectangle, dark brown
5. **Cheese** — thin layer slightly wider than patty, golden yellow, slightly melted corners
6. **Bottom bun** — flat base, same amber/tan as top

## Visual direction

- Minimalist, clean, modern — no cartoon excess, no heavy shadows, no decorative clutter
- Simple but elegant shapes with harmonious proportions
- Illustration centered in the viewport
- Each ingredient immediately legible at a glance
- Premium, restrained aesthetic — editorial/UI style

## Animation behavior

The SVG must use **CSS transitions** (not SMIL) via a `<style>` block inside the SVG:

- **Default state**: all layers assembled into a compact burger
- **On hover** (`:hover` on a wrapper `<g>` or `<svg>`): each layer translates vertically to separate the stack, revealing each ingredient clearly
- **On mouseout**: all layers return smoothly to assembled position
- Each layer gets a different `translateY` so the spacing is clean and readable even when "exploded"
- Top layers move up, bottom layers move down — symmetric expansion from the center

The animation must be:
- Fluid, with `cubic-bezier` or `ease-in-out` easing
- Moderate amplitude (not excessive — elegant, not theatrical)
- Consistent timing (all layers same duration, staggered if desired)
- Beautiful both assembled and exploded

## Technical constraints

- Single standalone SVG file: `<svg xmlns="..." viewBox="..." width="..." height="...">`
- CSS transitions in a `<style>` block inside the SVG — no external dependencies
- Each ingredient in its own `<g id="layer-name">` group
- No external images, no JS, no fonts, no external CSS
- Valid, well-indented, readable XML
- Directly copy-pasteable into HTML or saved as `.svg`

## Output format

Return **only** the SVG code. No markdown fences, no explanation, no preamble, no postscript.

Start with `<svg` and end with `</svg>`.

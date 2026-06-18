#!/usr/bin/env python3
"""
Recadrage deterministe d'une image au ratio 4:5 (vertical), sans regeneration.

Pourquoi : les moteurs Gemini image (nano-banana) n'honorent pas le ratio demande
dans le prompt (ils sortent souvent en ~9:16 ou ~3:4). On corrige donc le format en
post-traitement par un crop centre, sans relancer edit_image (pas de degradation du
rendu, resultat reproductible).

Usage :
    python crop-to-4-5.py <input> [output] [anchor]

- input  : chemin de l'image a recadrer
- output : chemin de sortie (defaut : ecrase l'input)
- anchor : position verticale du cadre quand l'image est trop haute, 0.0 = haut,
           0.5 = centre (defaut), 1.0 = bas. Utile si le sujet (tete/casque) est
           pres du bord haut : baisser vers 0.35 garde le haut.

Le ratio cible est 4:5 = largeur/hauteur = 0.8.
"""

import sys

from PIL import Image

TARGET = 4 / 5  # largeur / hauteur


def main():
    if len(sys.argv) < 2:
        print("Usage: python crop-to-4-5.py <input> [output] [anchor]")
        sys.exit(2)
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else inp
    anchor = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5

    im = Image.open(inp)
    w, h = im.size
    ratio = w / h

    if abs(ratio - TARGET) < 0.005:
        im.save(out)
        print(f"OK deja 4:5 : {w}x{h} -> {out}")
        return

    if ratio > TARGET:
        # trop large : on rogne la largeur (anchor horizontal centre)
        new_w = round(h * TARGET)
        x0 = round((w - new_w) * 0.5)
        box = (x0, 0, x0 + new_w, h)
    else:
        # trop haute : on rogne la hauteur (anchor vertical configurable)
        new_h = round(w / TARGET)
        y0 = round((h - new_h) * anchor)
        box = (0, y0, w, y0 + new_h)

    cropped = im.crop(box)
    cropped.save(out)
    print(f"Crop 4:5 : {w}x{h} -> {cropped.size[0]}x{cropped.size[1]} (anchor={anchor}) -> {out}")


if __name__ == "__main__":
    main()

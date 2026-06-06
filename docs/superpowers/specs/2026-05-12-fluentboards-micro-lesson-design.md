---
name: fluentboards-micro-lesson-design
description: Conception micro‑leçons (texte + captures) pour la formation FluentBoards – format rapide, sans quiz.
metadata:
  type: project
---

# Design – Micro‑leçons FluentBoards (format texte + captures)

**Date**: 2026‑05‑12

## Objectif
Produire des leçons de **≈ 5 minutes de lecture** chacune, avec 1‑2 captures d’écran annotées, sans quiz ni vidéo. Chaque leçon suit le même modèle markdown afin de faciliter la génération automatisée et la réutilisation.

## Structure de la leçon (markdown)
```markdown
# <Titre de la leçon>

> **Objectif**: En une phrase, ce que l’apprenant saura faire.

## Contexte
2‑3 phrases expliquant *pourquoi* cette fonction est utile dans FluentBoards.

## Étapes
1. Étape détaillée avec capture d’écran **(image‑nom‑capture.png)**.
2. Étape suivante …

## Astuces / Pièges à éviter
- Point 1
- Point 2

## Checklist de fin
- [ ] Action A réalisée
- [ ] Action B vérifiée
```

## Convention de nommage des fichiers
- Leçon : `lesson-<num>-<slug>.md` (ex. `lesson-03-setup-board.md`).
- Capture : `lesson-<num>-<slug>-capture-<index>.png`.

## Production automatisée (script `generate-lessons.py`)
1. Lire un CSV de métadonnées (`title,slug,objective,context,steps`).
2. Générer le markdown via Jinja2 template.
3. Copier les captures depuis `assets/captures/`.
4. Valider la checklist.

## Livraison
- Tous les fichiers markdown placés dans `content/course/fluentboards/lessons/`.
- Images dans `content/course/fluentboards/assets/`.
- Le dossier `content/course/fluentboards/` sera importé dans TutorLMS via son CLI.

## Points de contrôle (self‑review)
- Aucun placeholder (`TODO`, `TBD`).
- Toutes les captures référencées existent.
- Le texte ne dépasse pas ~300 mots.

---

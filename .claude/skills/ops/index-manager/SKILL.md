---
name: index-manager
description: Gerer automatiquement les index README/INDEX pour pages, slides, blocks et skills locaux.
user-invocable: true
---

# index-manager

Tu mets a jour les index adequats apres creation d'un nouveau fichier ou d'un nouveau skill.

## Regles

- Ne jamais inventer un fichier.
- Verifier que le fichier existe avant d'ajouter.
- Ajouter une seule ligne, pas de duplicat.
- Ne pas modifier les autres sections inutiles.
- Garder l'ordre alphabetique si possible.
- Pour les skills, ajouter le nom du dossier sans extension.

## Checklist (5 points)

1) Objectif defini en 1 phrase
2) Entrees clairement listees
3) Sorties obligatoires explicites
4) Exemple entree/sortie present
5) Actions suivantes listees

## Cibles supportees

- `content/pages/` -> `content/pages/README.md`
- `content/slides/` -> `content/slides/README.md`
- `content/blocks/` -> `content/blocks/README.md`
- `.claude/skills/` -> `.claude/skills/INDEX.md`
- `core/skills/` -> `core/skills/INDEX.md`

## Procedure

1) Identifier le dossier du nouvel element.
2) Choisir l'index correspondant.
3) Lire l'index.
4) Inserer la ligne au bon endroit.
5) Relire pour verifier.

## Format attendu

- Pages/slides/blocks : `- `nom-du-fichier.md``
- Skills : `- `nom-du-skill`` (sans extension)

## Exemples

- Nouveau fichier : `content/slides/diagramme-methode-schoolswp.md`
  - Ajouter `- `diagramme-methode-schoolswp.md`` dans `content/slides/README.md`.

- Nouveau skill local : `.claude/skills/index-manager/`
  - Ajouter `- `index-manager`` dans `.claude/skills/INDEX.md`.

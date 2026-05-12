---
name: index-manager
description: |
  Met à jour les index README/INDEX après création d'un nouveau fichier ou skill : `content/pages/`, `content/slides/`, `content/blocks/`, `.claude/skills/INDEX.md`, `core/skills/INDEX.md`. Vérifie l'existence du fichier, ajoute une seule ligne sans duplicat, garde l'ordre alphabétique.
  Utilise ce skill quand l'utilisateur dit : "mets à jour l'index", "ajoute au README", "réfère ce skill dans INDEX.md", "indexe ce nouveau fichier", ou vient de créer un asset dans un dossier qui a un index.
  NE PAS utiliser pour : éditer un README hors index (rédaction libre), créer un nouvel index (rédiger le markdown directement), maintenir le registre skills global (utiliser `skills_registry.py --sync` du projet), ou indexer du contenu publié (cycle SEO maillage = `radar` agent).
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

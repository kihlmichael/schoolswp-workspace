---
name: youtube
description: Espace métier YouTube - production vidéo, publication, SEO et analytics. Utiliser pour toute tâche liée à YouTube (upload, optimisation, thumbnails, playlists).
user-invocable: false
---

# YouTube Workspace

Espace métier dédié à la production et gestion de chaîne YouTube pour schoolsWP.

## Périmètre

- **Production** : Scripts, tournage, montage
- **Publication** : Upload, métadonnées, scheduling
- **SEO** : Titres, descriptions, tags, thumbnails
- **Analytics** : Performances, rétention, CTR
- **Community** : Commentaires, community posts

## Structure

```
02_YouTube/
├── SKILL.md          # Ce fichier
├── references/        # Workflows n8n
├── references/       # SOP et checklists
└── assets/        # Templates de contenu
```

## Workflows disponibles

_À créer selon les besoins :_

| Workflow | Description | Status |
|----------|-------------|--------|
| `upload-video.json` | Upload et publication | Placeholder |
| `update-metadata.json` | Mise à jour titre/description | Placeholder |
| `analytics-report.json` | Rapport hebdomadaire | Placeholder |

## Procédures

_À documenter :_

- [ ] Checklist pré-publication
- [ ] Process de création de thumbnail
- [ ] Guidelines SEO vidéo

## Templates

_À créer :_

- [ ] Template description vidéo
- [ ] Template script vidéo
- [ ] Template community post

## Dépendances

Ce workspace utilise les skills socle :
- `n8n-code-javascript` pour le scripting
- `n8n-workflow-patterns` pour l'architecture
- `n8n-mcp-tools-expert` pour les intégrations

## Prochaines étapes

1. Documenter le process de publication actuel
2. Créer le workflow d'upload automatisé
3. Standardiser les templates

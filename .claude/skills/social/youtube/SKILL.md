---
name: youtube
description: (archivé - espace métier fourre-tout remplacé par les skills YouTube spécialisés - ne pas auto-déclencher)
user-invocable: false
---

> **Statut : archivé le 2026-04-16.**
> Ce skill "Espace métier YouTube" était un hub générique couvrant production, publication, SEO et analytics — trop large pour router sans ambiguïté. Il était déjà marqué `user-invocable: false`, signal d'abandon préalable.
> Remplacé par les skills spécialisés :
> - Production vidéo longue → `schoolswp-youtube-studio`
> - Shorts → `youtube-shorts-schoolswp`
> - Miniatures → `thumbnail-strategist`
> - Extraction données → `youtube-extractor`
> - Pilotage ROI multi-canal → `youtube-omnichannel-engine`
>
> Conservation pour référence. Suppression manuelle à faire via l'explorateur Windows.

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

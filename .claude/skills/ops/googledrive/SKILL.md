---
name: googledrive
description: |
  Espace métier Google Drive pour schoolsWP : upload, organisation arborescente, recherche par nom/type/contenu, partage avec permissions granulaires, gestion versioning et corbeille. S'appuie sur le MCP Google Drive natif (read_file_content, search_files, create_file, copy_file, etc.).
  Utilise ce skill quand l'utilisateur dit : "upload sur Drive", "cherche dans Drive", "partage ce fichier Drive", "organise dossier Drive", "récupère le fichier Drive", ou veut interagir avec le stockage cloud Google.
  NE PAS utiliser pour : édition Google Sheets/Docs (utiliser MCP Sheets ou Drive read direct), backup config Claude Code (utiliser claude-config-backup), upload images articles WordPress (utiliser tools/wp-media-upload/), ou stockage assets repo git (utiliser le repo).
user-invocable: false
---

# Google Drive Workspace

Espace métier dédié à la gestion du stockage cloud Google Drive pour schoolsWP.

## Périmètre

- **Fichiers** : Upload, téléchargement, versioning
- **Organisation** : Création de dossiers, arborescence, tri
- **Recherche** : Par nom, type, contenu, date
- **Partage** : Permissions, liens, collaboration
- **Maintenance** : Gestion stockage, corbeille, nettoyage

## Structure

```
08_GoogleDrive/
├── SKILL.md          # Ce fichier
├── references/        # Workflows n8n
├── references/       # SOP et checklists
└── assets/        # Templates et conventions
```

## Capacités

| Action | Description |
|--------|-------------|
| Upload | Téléverser des fichiers vers Drive |
| Download | Télécharger des fichiers depuis Drive |
| Create Folder | Créer et organiser des dossiers |
| Search | Rechercher par nom, type ou contenu |
| Share | Partager avec permissions granulaires |
| Move/Copy | Déplacer ou copier des fichiers |
| Trash | Gérer la corbeille (auto-vidée 30j) |
| Versioning | Accéder à l'historique (30j / 100 versions) |

## Workflows disponibles

_À créer selon les besoins :_

| Workflow | Description | Status |
|----------|-------------|--------|
| `upload-file.json` | Upload de fichier | Placeholder |
| `organize-folder.json` | Organisation automatique | Placeholder |
| `backup-to-drive.json` | Backup vers Drive | Placeholder |
| `share-content.json` | Partage automatisé | Placeholder |

## Procédures

_À documenter :_

- [ ] Convention de nommage fichiers schoolsWP
- [ ] Structure d'arborescence standard
- [ ] Process de backup régulier
- [ ] Politique de partage et permissions

## Templates

_À créer :_

- [ ] Arborescence projet type
- [ ] Naming convention guide
- [ ] Checklist organisation Drive

## Dépendances

Ce workspace utilise les skills socle :
- `n8n-code-javascript` pour le scripting
- `n8n-workflow-patterns` pour l'architecture
- `n8n-mcp-tools-expert` pour les intégrations API

## Limites techniques

| Limite | Valeur |
|--------|--------|
| Taille fichier max | 5 TB |
| Historique versions | 30 jours ou 100 versions |
| Rétention corbeille | 30 jours (auto-suppression) |
| Stockage gratuit | 15 GB |

## Authentification

**Options recommandées :**

1. **Playwright/CDP** (recommandé) : Login interactif sans credentials en clair
2. **Variables d'environnement** : `GOOGLE_EMAIL` stocké localement

> **Sécurité** : Ne jamais stocker de credentials dans les skills. Utiliser les credentials n8n ou variables d'environnement.

## Intégration avec autres espaces

| Espace | Usage Drive |
|--------|-------------|
| `01_LinkedIn` | Stockage images/médias posts |
| `02_YouTube` | Stockage thumbnails, scripts |
| `03_Facebook` | Stockage créatifs publicitaires |
| `04_WordPress` | Backups, médias |
| `05_Branding` | Assets visuels, guidelines |

## Prochaines étapes

1. Définir l'arborescence schoolsWP sur Drive
2. Documenter les conventions de nommage
3. Mettre en place les workflows de backup
4. Créer les automatisations de partage

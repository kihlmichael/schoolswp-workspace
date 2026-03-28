# Workspace Hygiene Report — 2026-03-25

## Etat general

**24 problemes detectes** repartis en 4 categories :
- Patch files et scripts residuels : **14**
- Dossiers dupliques : **1**
- Fichiers orphelins a la racine : **5**
- Composants inactifs : **4**

## Patch files et scripts residuels

| Fichier | Localisation | Action proposee | Raison |
|---------|-------------|-----------------|--------|
| patch_extract_convention.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_staticdata.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_merge_conv.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_set_convention.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_fix_setnode.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_claude_body.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_file_context.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| patch_error_node.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| fix_workflow.py | racine | trash | script one-shot n8n sans docstring, contient API key en dur |
| fix_gemini_workflow.py | data/ | archive | docstring detaillee, touche au workflow Gemini Photos |
| fix_drive_query.py | data/ | archive | docstring, touche au workflow Drive API |
| fix_mime_query.py | data/ | archive | docstring, touche au workflow Drive API (mimeType) |
| fix_search_method.py | data/ | archive | docstring, touche au workflow Drive (searchMethod) |
| fix_binary_read.py | data/ | archive | docstring, touche au workflow Gemini (binary read) |

**Note securite** : les 9 scripts a la racine contiennent tous une API key n8n en clair (`eyJhbGci...`). Meme apres trash, envisager la rotation de cette cle.

## Dossiers dupliques

| Dossier A | Dossier B | Statut | Action proposee |
|-----------|-----------|--------|-----------------|
| .agent/ | .agents/ | identiques (meme arbo `skills/`) | garder `.agents/` (reference dans CLAUDE.md), trash `.agent/` |

## Fichiers orphelins

| Fichier | Action proposee | Destination |
|---------|-----------------|-------------|
| download.html | trash | fichier vide (1 ligne), aucun contenu utile |
| sync-colors.ps1 | deplacement | `tools/scripts/` — script PowerShell utilitaire Google Drive |
| 2026-03-21_youtube_welcome-to-tutor-lms-academy.md | deplacement | `content/formations/tutorlms/` — extraction YouTube TutorLMS |
| ccpa.config.json | deplacement | `apps/telegram-bot/` ou `infra/` — config Telegram/CCPA, pas sa place a la racine |
| skills-lock.json | deplacement | `.claude/` — lock file des skills Claude Code |

## Composants inactifs

| Composant | Reference CLAUDE.md | Commits recents (<30j) | Score | Action proposee |
|-----------|-------------------|----------------------|-------|-----------------|
| temp-n8n-skills/ | non | non (dossier vide) | 0/2 | trash — dossier vide, aucun contenu |
| apps/claude-telegram-poc/ | non | non | 0/2 | archiver — POC Telegram, doublon potentiel avec `apps/telegram-bot/` |
| apps/thruuu-claude-writer/ | non (dans CLAUDE.md workspace mais pas projet) | non | 0/2 | archiver — prevu pour integration future (cf. memoire projet) |
| apps/video-marketing/ | non | non | 0/2 | archiver — sous-projet non reference, pas de commits recents |

## Plan d'action resume

1. Creer `_archive/patches/` (n'existe pas encore)
2. Archiver 5 fichiers fix dans `data/` vers `_archive/patches/`
3. Archiver 3 composants inactifs (`claude-telegram-poc`, `thruuu-claude-writer`, `video-marketing`) vers `_archive/apps/`
4. Trasher 9 patch/fix scripts a la racine (contiennent des API keys en dur)
5. Trasher `download.html` (fichier vide)
6. Trasher `.agent/` (doublon de `.agents/`)
7. Trasher `temp-n8n-skills/` (dossier vide)
8. Deplacer `sync-colors.ps1` vers `tools/scripts/`
9. Deplacer `2026-03-21_youtube_welcome-to-tutor-lms-academy.md` vers `content/formations/tutorlms/`
10. Deplacer `ccpa.config.json` vers `apps/telegram-bot/` ou `infra/`
11. Deplacer `skills-lock.json` vers `.claude/`
12. **Rotation recommandee** de la cle API n8n exposee dans les scripts patch

**Attente validation avant execution.**

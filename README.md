# schoolsWP OS

Systeme de travail pour construire l'ecosysteme schoolsWP avec Claude Code.

## Ce que contient ce repo
- SEO, architecture WordPress, automation, monetisation, autorite.
- Un systeme d'agents et de playbooks.
- Un protocole simple (plan -> execution -> verification).

## Demarrage rapide
1) Ouvrir ce dossier dans Claude Code.
2) Lire `CLAUDE.md`.
3) Lancer une mission dans `core/tasks/todo.md`.
4) Utiliser les agents dans `core/agents-md/` et `core/agents-py/`.
5) Documenter dans `core/tasks/`.

## n8n (framework)
Ce repo contient aussi le framework n8n schoolsWP.

- Doc complete : `systems/n8n/Règles du jeu – automatisation n8n.md`
- Workflows : `systems/workflows/`
- Scripts : `tools/scripts/`
- Configs : `infra/config/`

## Structure principale
- `core/` : OS schoolsWP (agents, playbooks, tasks, skills)
- `content/` : pages publiques, slides, docs, articles
- `systems/` : n8n, workflows, multi-agent-system
- `tools/` : scripts et services techniques
- `infra/` : docker, monitoring
- `data/` : reports, outputs, artifacts

## Liens utiles
- Agents index : `core/agents-md/INDEX.md`
- Authority Engine : `core/agents-md/schoolswp-authority-engine.md`
- Pages index : `content/pages/README.md`
- Slides index : `content/slides/README.md`

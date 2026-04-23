# Agent Content Studio — schoolsWP

Tu es l'agent editorial de schoolsWP. Tu rediges, structures et optimises
tous les contenus : articles de blog, tutoriels, guides, pages piliers.

Charge `soul.md` pour ta personnalite complete.

> **Regles transverses** : `../shared/RULES.md` fait autorite sur safety, branding,
> memoire, MCP novamira, securite, escalade. Ce CLAUDE.md couvre uniquement
> ce qui est specifique au content-studio.

## Ta mission

Produire du contenu clair, actionnable et optimise SEO + AIO
qui respecte la voix schoolsWP a la lettre.

## Structure du workspace

```text
content-studio/
├── .claude/
│   ├── channels/telegram/    # Config Telegram (token + access)
│   └── settings.local.json   # Permissions de l'agent
├── memory/
│   ├── memory.md             # Memoire long terme
│   └── daily-logs/           # Logs quotidiens (YYYY-MM-DD.md)
├── output/                   # Livrables (articles, drafts, audits)
├── skills/                   # Skills locaux du content-studio
├── CLAUDE.md                 # Ce fichier
└── soul.md                   # Personnalite de l'agent
```

## Ressources partagees (../shared/)

- `RULES.md` — regles transverses schoolsWP (safety, branding, MCP, securite, memoire)
- `SITE.md` — snapshot WordPress schoolswp.com (plugins, versions)
- `skills/schoolswp-voice.md` — regles d'ecriture strictes
- `skills/schoolswp-branding.md` — identite visuelle et QA branding
- `skills/wordpress-stack.md` — stack technique schoolsWP
- `contacts.md` — coordonnees et affiliations
- `cron_registry.json` — taches recurrentes de tous les agents

## Avant chaque session

1. Lis `soul.md` pour incarner ta personnalite
2. Lis `../shared/RULES.md` pour les regles transverses schoolsWP (safety, branding, MCP)
3. Lis `../shared/SITE.md` pour le snapshot WordPress schoolswp.com (plugins, versions)
4. Lis `../shared/skills/schoolswp-voice.md` pour les regles d'ecriture
5. Lis `../shared/skills/schoolswp-branding.md` pour l'identite visuelle
6. Lis `memory/memory.md` pour le contexte long terme
7. Lis le daily log du jour s'il existe (`memory/daily-logs/YYYY-MM-DD.md`)
8. Lis `../shared/cron_registry.json` et recree les crons qui te concernent

## Crons du content-studio

Depuis `cron_registry.json`, tu as un cron a recreer a chaque demarrage :

| Nom | Frequence | Action |
| --- | --- | --- |
| `audit-pipeline-contenu` | Lundi 10h00 | Lire memory.md, lister articles en cours/attente/publies, proposer 3 priorites editoriales, loguer dans daily-logs |

Utilise le CronCreate tool pour recreer ce cron au demarrage.

## Workflow de reference

Tu suis le workflow en 3 phases :

1. **SERP first** — Analyser l'intention de recherche et la SERP
2. **AI next** — Produire le brouillon structure
3. **Human last** — Affiner, scorer, valider

## Regles de contenu

### Structure obligatoire

- H1 unique, H2/H3 coherents, FAQ en H3 avec reponse directe
- Longueur articles : 1200-2500 mots selon complexite

### Blocs AIO obligatoires

Pour chaque article ou guide :

- **Reponse rapide** en debut d'article (40-60 mots)
- **Points cles** (liste 4-6 items)
- **En resume** en fin d'article
- FAQ schema-ready en H3

### CTA

- 1 CTA soft et contextualise max par contenu
- Lien interne, outil recommande ou invitation newsletter
- Disclosure affilies obligatoire

### Promo assets

- Fluent Forms : code promo `schoolsWP20`
- OttoKit : lien `schoolswp.com/OttoKit`, code `SCHOOLSWP20`

## Agents Python du projet parent

Commandes disponibles (lancer depuis `D:\VS Code\CLAUDE CODE\projects\schoolswp\`) :

```bash
# Pipeline complet article
.venv/Scripts/python -m agents.content_factory.cli --keyword "..." --intent ... --pillar ...

# Pipeline 5 etapes (leger)
.venv/Scripts/python -m agents.article_pipeline.cli --topic "..." --keyword "..." --intent ...

# Audit SEO /100
.venv/Scripts/python -m agents.seo_auditor.cli --file article.md --keyword "..." [--fix]

# 4 audits paralleles (publish score)
.venv/Scripts/python -m agents.publish_ready.cli --file article.md --keyword "..."
```

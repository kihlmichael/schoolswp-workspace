# NOTICE — external-obsidian

This directory contains 1 skill cherry-picked from
[`kepano/obsidian-skills`](https://github.com/kepano/obsidian-skills) on 2026-05-04.

- **Upstream commit** : `fa1e131a014576ff8f8919f191a7ca8d8fded39b`
- **Upstream license** : MIT (see upstream LICENSE)
- **Author** : Steph Ango (kepano), CEO Obsidian
- **Spec** : [agentskills.io](https://agentskills.io)
- **Companion CLI** : [`kepano/defuddle`](https://github.com/kepano/defuddle) (MIT, npm)

## What we kept

- `defuddle/` — extraction markdown propre depuis n'importe quelle URL via CLI npm

## What we did NOT keep (and why)

| Skill upstream | Raison du reject |
|---|---|
| `obsidian-markdown` | Pas de vault Obsidian opéré par Claude Code à ce stade |
| `obsidian-bases` | Idem — fonctionnalité Obsidian Bases (.base files) non utilisée |
| `json-canvas` | Idem — pas de fichiers .canvas dans le projet |
| `obsidian-cli` | Pas de dev de plugin/theme Obsidian prévu |

À reconsidérer si un vault Obsidian devient l'index de connaissance schoolsWP (cf. plan stratégique 24m).

## What we changed

Frontmatter `name`/`description` du `SKILL.md` upstream conservés intacts. Une section "Routing schoolsWP" a été ajoutée à la fin pour clarifier la cohabitation avec `firecrawl_scrape` (MCP) déjà actif. Les code fences en langage shell ont été passés en fence neutre pour cohabiter avec le hook local prompt-injection-detector.

## Pre-requisite

Le skill suppose que le CLI npm `defuddle` est installé globalement (version 0.18.1+). Statut local : installé le 2026-05-04.

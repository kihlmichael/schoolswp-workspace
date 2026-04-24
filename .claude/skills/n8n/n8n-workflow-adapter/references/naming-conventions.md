# Conventions de nommage workflow et nodes schoolsWP

Source de vérité côté projet : `.claude/rules/n8n-integration.md` + `systems/n8n/CLAUDE.md`. Ce document reprend les règles utiles lors de l'adaptation d'un workflow externe.

## Nommage workflow

Format : `<domaine>-<verbe>-<sujet>-W<num>`

| Élément | Règles | Exemples |
|---|---|---|
| `<domaine>` | Préfixe par la stack principale du workflow | `wp`, `telegram`, `gmail`, `sheet`, `firecrawl`, `claude` |
| `<verbe>` | Action principale, infinitif sans "to" | `auto-tag`, `ingest`, `summarize`, `notify`, `sync`, `draft` |
| `<sujet>` | Objet métier concerné | `posts`, `articles`, `contacts`, `invoices`, `brief` |
| `<num>` | Numéro incrémental, 3 chiffres | `W101`, `W202`, `W315` |

### Exemples d'adaptation

| Template externe | Nom adapté schoolsWP |
|---|---|
| `Auto-Tag Blog Posts in WordPress with AI` | `wp-auto-tag-posts-W201` |
| `Telegram chat with PDF` | `telegram-pdf-chat-W202` |
| `AI-Generated Summary Block for WordPress Posts` | `wp-summarize-posts-W203` |
| `Automate Blog Creation in Brand Voice with AI` | `wp-draft-brand-voice-W204` |
| `Daily Email Digest` | `gmail-digest-daily-W205` |

### Récupération du prochain numéro

Lister les workflows existants dans `systems/workflows/` et prendre `max(Wxxx) + 1`. Si on ne veut pas scanner : demander via MCP n8n-mcp ou à l'utilisateur.

Plage recommandée pour les imports externes : **W200-W299** (réservé aux adaptations).

## Nommage nodes

### Règles générales

1. Nom court, PascalCase ou Title Case avec tirets
2. Préfixé par un identifiant de rôle si ambigu (ex : `WH1_`, `SCHED1_`, `LLM1_`)
3. Pas d'accents, pas de caractères spéciaux
4. Le nom doit raconter **ce que fait le node**, pas quel type c'est

### Préfixes de rôle

| Préfixe | Rôle | Exemple |
|---|---|---|
| `WH1_`, `WH2_` | Webhooks | `WH1_ReceiveBrief` |
| `SCHED1_`, `SCHED2_` | Schedule triggers | `SCHED1_DailyIngestion` |
| `TRIG_` | Autres triggers app (Gmail, WP, Telegram) | `TRIG_WordpressNewPost` |
| `LLM1_`, `LLM2_` | Nodes LLM | `LLM1_SummarizePost`, `LLM2_ExtractTags` |
| `EMB_` | Nodes embeddings | `EMB_OpenAITextSmall` |
| `VEC_` | Vector store | `VEC_SupabaseUpsert`, `VEC_SupabaseSearch` |
| `HTTP_` | HTTP request (dernier recours) | `HTTP_RankMathMetaUpdate` |
| `IF_`, `SWITCH_` | Branches | `IF_PostHasExistingTags` |
| `LOG_` | Logging / notification | `LOG_DiscordNotify`, `LOG_SheetsAppend` |

### Mauvais vs bon

| À éviter | Préférer |
|---|---|
| `HTTP Request` (nom par défaut) | `HTTP_RankMathMetaUpdate` |
| `OpenAI` | `LLM1_CategorizePost` |
| `Code` | `CODE_ExtractTagsFromResponse` |
| `Set` | `SET_NormalizePost` |

### Nodes Sticky Note

Les Sticky Notes sont utiles pour documenter. Contenu attendu :

```
[Titre du block]

But : <ce que fait ce groupe de nodes>
Input : <données en entrée>
Output : <données en sortie>
Gotchas : <pièges connus>
```

Retirer les Sticky Notes `"Placeholder for X"` des templates amont (aucune valeur).

## Nommage credentials

Format : `<service>-<scope>-<owner>`

- `<service>` : nom du service en minuscules (anthropic, supabase, wordpress, gmail, telegram)
- `<scope>` : portée (main, perso, schoolswp, bot-name)
- `<owner>` : optionnel, pour distinguer plusieurs comptes

Exemples :
- `anthropic-main`
- `wp-schoolswp-main`
- `gmail-michael-perso`
- `supabase-schoolswp`
- `telegram-bot-schoolswp-public`

## Checklist de validation post-renommage

Après adaptation d'un workflow :

- [ ] Nom workflow conforme au format `<domaine>-<verbe>-<sujet>-W<num>`
- [ ] Tous les nodes ont un nom explicite (pas de "HTTP Request", "Code", "Set" génériques)
- [ ] Préfixes de rôle appliqués aux triggers, LLM, vector, logs
- [ ] Aucun nom en camelCase (interdit côté repo, voir CLAUDE.md)
- [ ] Sticky Notes "Placeholder for X" retirés
- [ ] Credentials référencent des IDs existants côté instance (pas de placeholder non mappé)

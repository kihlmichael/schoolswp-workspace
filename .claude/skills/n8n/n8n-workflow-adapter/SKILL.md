---
name: n8n-workflow-adapter
description: |
  Adapte un workflow n8n externe (importé depuis enescingoz, n8n.io/workflows ou tout autre source)
  pour l'instance schoolsWP : sanitize les credentials placeholders, applique les conventions de
  nommage schoolsWP (workflow, nodes, variables), remplace les URLs placeholder vers schoolswp.com,
  et produit un JSON prêt pour import via n8n-mcp. Déclenche ce skill après n8n-template-finder ou
  quand l'utilisateur dit : "adapte ce workflow", "importe ce n8n", "sanitize ce template",
  "rebrand ce workflow pour schoolsWP", "prépare ce JSON pour mon instance", "nettoie ce template
  avant import". Complémentaire à n8n-template-finder (recherche) et n8n-validation-expert
  (validation post-import).
---

# n8n Workflow Adapter

Transforme un workflow n8n externe en version compatible schoolsWP : credentials, nommage, URLs, conventions.

## Input attendu

Un fichier JSON de workflow n8n, accessible via :

- Path local (ex : /tmp/template.json)
- URL raw GitHub (ex : sortie de n8n-template-finder)
- Coller-collé direct dans la conversation

## Pipeline d'adaptation (6 étapes)

### 1. Parse + validation structurelle

```
.venv/Scripts/py .claude/skills/n8n/n8n-workflow-adapter/scripts/sanitize_workflow.py <input.json> --out <output.json>
```

Le script vérifie que le JSON contient les clés n8n canoniques (name, nodes, connections, settings). Rejette les fichiers corrompus ou tronqués.

### 2. Sanitize credentials

Remplace les placeholders connus par des credentials schoolsWP. Mapping dans references/credentials-mapping.md.

Règles automatiques :

- "id": "OPENAI_API" → retirer (on utilise Anthropic par défaut, le node doit être swappé)
- "id": "ANTHROPIC_API" → "id": "anthropic-main" (credential existant dans l'instance)
- "id": "SUPABASE_API" → "id": "supabase-schoolswp"
- "id": "TELEGRAM_BOT" → demander à l'utilisateur lequel (9 bots possibles)
- "id": "WORDPRESS_API" → "id": "wp-schoolswp-main"

Pour tout credential non mappé : **flagger et demander à l'utilisateur** avant d'inventer.

### 3. Swap modèles LLM

- "model": "gpt-4-turbo" ou "gpt-4o" → proposer claude-sonnet-4-6 via lmChatAnthropic
- "model": "gpt-3.5-turbo" → proposer claude-haiku-4-5-20251001

Si l'utilisateur insiste sur OpenAI, laisser le node intact mais warning sur le coût.

### 4. Renommage workflow + nodes

Convention schoolsWP (voir references/naming-conventions.md) :

**Workflow** : `<categorie>-<verbe>-<sujet>-W<num>`

Exemples :

- "Auto-Tag Blog Posts in WordPress with AI" → wp-auto-tag-posts-W201
- "Telegram chat with PDF" → telegram-pdf-chat-W202

Récupérer le prochain numéro disponible via la liste de systems/workflows/ ou MCP n8n-mcp.

**Nodes** : conserver les noms existants sauf si ambigus. Préfixer par le trigger (ex : WH1_, SCHED1_).

### 5. Remplacement URLs et domaines

Recherche/remplacement :

- https://example.com → https://schoolswp.com
- https://yoursite.com → https://schoolswp.com
- Webhooks n8n : générer un nouveau path UUID (ne pas garder le path du template)

### 6. Sortie + validation finale

Fichier sortie : systems/workflows/<nom-workflow>.json

Validation post-adaptation via le MCP n8n-mcp (outil validate_workflow).

Si validation échoue : invoquer n8n-validation-expert avec le message d'erreur.

## Garde-fous stricts

- **Jamais** de push vers l'instance sans review humain final (n8n-mcp create_workflow requiert confirmation explicite)
- **Jamais** d'écrasement de systems/workflows/*.json existant sans flag --force
- **Flagger** tout node qui utilise une stack exotique non présente dans schoolsWP (ex : Weaviate, Redis vector, Neo4j)
- **Retirer** les nodes de log redondants (Google Sheets Append + Slack Alert) si Michael n'a pas validé

## Sortie type

Résumé en chat après adaptation :

```
Workflow sanitisé : wp-auto-tag-posts-W201.json
Credentials remappés : 3/3 (anthropic-main, wp-schoolswp-main, supabase-schoolswp)
Modèle LLM swappé : gpt-4o → claude-sonnet-4-6
URLs remplacées : 2 occurrences
Validation n8n-mcp : OK (0 erreurs, 2 warnings)

Actions requises avant import :
- [ ] Review human : path webhook à valider (UUID généré : <uuid>)
- [ ] Tester en dry-run avant activation
- [ ] Ajouter à systems/workflows/ et commit

Fichier prêt : systems/workflows/wp-auto-tag-posts-W201.json
```

## Références

- references/credentials-mapping.md : mapping complet placeholders → credentials schoolsWP
- references/naming-conventions.md : règles de nommage workflow et nodes
- scripts/sanitize_workflow.py : implémentation du pipeline
- Complément : n8n-validation-expert pour les erreurs post-adaptation

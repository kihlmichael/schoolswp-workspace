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

## Lessons learned (2026-05-05, import veille concurrentielle)

Pièges rencontrés lors du premier vrai import enescingoz → instance schoolsWP. À vérifier sur tout futur adaptat :

### 1. Expressions Google Sheets : toujours préfixer `$json.`

Symptôme : node "Append to Sheet" → `[ERROR: invalid syntax]` sur chaque colonne.

Cause : les expressions copiées de templates utilisent souvent `.output.xxx` (raccourci) qui est rejeté par n8n. Seul `{{ $json.output.xxx }}` est valide quand le node est aval d'un agent qui produit `output.{schema}`.

Fix automatique à intégrer dans le sanitize : remplacer `(.output.` → `($json.output.`, `{ .output.` → `{ $json.output.`, ` .output.` → ` $json.output.` dans toutes les expressions du node Sheets.

### 2. LLM model par défaut : Haiku 4.5 > Sonnet 4.5 sur Tier 1

Symptôme : "service is receiving too many requests" même avec `estimatedTokens: 194` sur le prompt courant.

Cause : Anthropic Tier 1 a un TPM cumulatif de 30k pour Sonnet, 50k pour Haiku. Quand un workflow enchaîne 3 agents × N items, le cumul sur 60s explose la fenêtre Sonnet.

Règle : pour les agents structurés (extraction de champs), default = `claude-haiku-4-5-20251001`. Réserver Sonnet aux agents qui font du raisonnement complexe (pas de l'extraction).

Mettre à jour `MODEL_HINTS` dans `sanitize_workflow.py` : `gpt-4*` → `claude-haiku-4-5-20251001` (et non plus Sonnet) sauf si l'agent a explicitement besoin de raisonnement.

### 3. Règle anti-prose dans le system prompt agent

Symptôme : parser strict refuse l'output → "Model output doesn't fit required format". Dans les logs : prose type "I apologize, I cannot retrieve...".

Cause : quand un outil de recherche échoue, Haiku/Sonnet abandonnent et renvoient de la prose au lieu du JSON structuré.

Règle à injecter systématiquement dans tout agent connecté à un Structured Output Parser :

```
CRITICAL OUTPUT RULE:
- If you cannot find data after N tool calls, return the JSON structure with empty/default values.
- NEVER respond with prose, apologies, or explanations.
- Empty data = JSON with: numbers=0, strings="", arrays=[], booleans=false.
```

### 4. autoFix sur Structured Output Parser exige un LLM connecté au parser

Symptôme : "A Model sub-node must be connected and enabled" sur le parser quand autoFix est activé.

Cause : Auto-Fix Format ré-appelle un LLM pour coercer la réponse en JSON valide. Il faut un model connecté **au parser** (pas seulement à l'agent).

Fix : pour chaque pair (agent, parser), brancher le même `lmChatAnthropic` sur les deux via `ai_languageModel`. Dans `connections`, ajouter une entrée :

```json
"OpenAI Chat Model1": {
  "ai_languageModel": [[
    { "node": "Company Overview Agent",   "type": "ai_languageModel", "index": 0 },
    { "node": "Structured Output Parser1","type": "ai_languageModel", "index": 0 }
  ]]
}
```

### 5. Budget tool calls + slim schemas

Symptôme : agents qui consomment 90k+ tokens cumulés sur 3 itérations.

Règle : pour un agent d'extraction simple, contraindre dans le system prompt :

- `Maximum 2 tool calls total.`
- `Snippets from search are enough — do NOT use Webscraper tools.`
- Schema de sortie ≤ 5 champs simples (pas d'objets imbriqués sur 3 niveaux)

Dans `sanitize_workflow.py`, flagger les schemas > 8 champs ou les agents avec plus de 3 outils connectés comme "à slim".

## Références

- references/credentials-mapping.md : mapping complet placeholders → credentials schoolsWP
- references/naming-conventions.md : règles de nommage workflow et nodes
- scripts/sanitize_workflow.py : implémentation du pipeline
- Complément : n8n-validation-expert pour les erreurs post-adaptation

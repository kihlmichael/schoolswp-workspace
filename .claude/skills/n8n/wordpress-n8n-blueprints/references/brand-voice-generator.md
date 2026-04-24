# Blueprint : Brand Voice Content Generator (adapté schoolsWP)

**Source amont** : `enescingoz/awesome-n8n-templates/WordPress/Automate Blog Creation in Brand Voice with AI.json` (17 KB)

**Objectif** : générer des drafts WordPress dans la voix de marque schoolsWP à partir d'une liste de briefs stockée dans Google Sheets.

## Attention : complémentarité avec la content factory Python

Ce blueprint n'est **pas un remplacement** de la content factory Python (brain, brain-lite, thruuu-writer). C'est un pont léger pour :

- Exécuter un draft rapide sans passer par le pipeline complet
- Industrialiser la génération d'articles "satellites" (liens, glossaire, FAQ courts)
- Laisser Michael lancer un article depuis un Sheet sans ouvrir le terminal

Pour tout article pilier ou cocon, rester sur la content factory Python.

## Stack adaptée

```
Schedule Trigger (daily 6am)
  OR Google Sheets Trigger (new row in "briefs")
  → GET row data (titre, keyword, intent, pillar, cluster)
  → LLM generation avec brand-voice prompt (claude-sonnet-4-6)
  → Parse output en sections (H1, H2s, contenu, meta)
  → POST /wp/v2/posts avec status=draft + rank_math meta via endpoint dédié
  → Mark row as "draft created" in Sheets
  → Discord notification
```

## Format attendu du Sheet

Colonnes requises dans le Google Sheet source :

| Colonne | Exemple | Obligatoire |
|---|---|---|
| `title` | "Comment configurer FluentCRM avec TutorLMS" | ✓ |
| `keyword` | "fluentcrm tutorlms integration" | ✓ |
| `intent` | "décisionnelle" | ✓ |
| `pillar` | "crm" | ✓ |
| `cluster` | "cluster-crm" | ✓ |
| `objective` | "formation" | optionnel |
| `length` | 2000 | optionnel (default 1500) |
| `status` | "ready" → "draft created" | géré par workflow |

## Brand voice injection

Le prompt LLM charge au runtime :

1. **shared/brand.md** (depuis schoolswp-agents) : guidelines de marque, mots interdits, ton
2. **content/docs/BRAND_RULES.md** : source de vérité branding
3. Guidelines en tête du system prompt : "toujours schoolsWP (jamais schoolswp ni SchoolsWP), tutoiement, pas d'em-dash, pas de marketing-speak"

## Prompt système (LLM node)

Structure du system prompt :

```
Tu rédiges un article WordPress pour schoolsWP dans la voix de marque.

GUIDELINES BRAND (inviolables) :
- Nom : toujours "schoolsWP" (jamais schoolswp, SchoolsWP, Schoolswp)
- Ton : tutoiement, direct, sans jargon marketing
- Interdits : em-dash (—), "révolutionnaire", "unique", "game-changer", "l'IA change tout"
- Cible : freelance/indépendant qui construit son autorité sur WordPress
- Chaque article apporte une décision claire, pas juste du contenu

STRUCTURE ATTENDUE :
- H1 contenant le keyword
- H2 "Pourquoi c'est important" (60-100 mots)
- 3 à 5 H2 de corps (200-400 mots chacun)
- H2 "Décision" : 3 bullets clairs
- H2 "FAQ" (3 à 5 questions)

SEO :
- Meta title : 50-60 caractères, keyword en début
- Meta description : 140-156 caractères, CTA implicite
- Keyword principal : densité 0.8-1.2%

OUTPUT FORMAT (JSON strict) :
{
  "h1": "...",
  "content_html": "<h2>...</h2>...",
  "meta_title": "...",
  "meta_description": "...",
  "proposed_tags": ["cluster-xxx"]
}
```

User prompt : les champs du Sheet row.

## Guardrails schoolsWP

1. **Status = draft TOUJOURS**. Aucun auto-publish. Michael review avant.

2. **Meta SEO via endpoint Rank Math dédié** (voir mémoire `reference_rank_math_rest_limits`) : POST sur `/wp-json/rankmath/v1/updateMeta` et non via core REST (qui silent-ignore).

3. **Validation brand** : après génération, passer le contenu via le skill `branding` en mode check. Si alerte bloquante : ne pas créer le draft, alerter Discord.

4. **Hygiène URL / slug** : le workflow ne set pas de slug. WordPress génère un slug par défaut que Michael peut ajuster. Respecter `feedback_evergreen_slugs` (pas d'année, pas de "schoolswp" dans le slug).

5. **Images** : ce blueprint ne génère pas d'images. Pour l'image à la une, passer par le skill `wp-image-metadata-seo` + génération manuelle via `aidesigner` ou `nano-banana`.

## Adaptation du JSON externe

Étapes via `n8n-workflow-adapter` :

1. Nom workflow : `wp-draft-brand-voice-W204`
2. Credentials :
   - OPENAI_API → retirer + swap node vers lmChatAnthropic (anthropic-main)
   - GOOGLE_SHEETS_API → google-sheets-schoolswp
   - WORDPRESS_API → wp-schoolswp-main
3. Ajouter :
   - Node HTTP Request pour l'endpoint Rank Math (credential : rank-math-api)
   - Node Discord pour notification
   - Node IF pour check validation brand (call au skill via webhook interne ou inline prompt)
4. Retirer :
   - Nodes Google Sheets Append + Slack Alert du log redondant (on garde seulement Discord)

## Volume attendu

Usage réaliste schoolsWP :

- Articles satellites (glossaire, FAQ courts) : 3-5 par semaine
- Articles décisionnels / comparatifs : rester sur content factory Python
- Articles pilier : rester sur thruuu-writer

Ne pas utiliser ce workflow pour plus de 10 articles/semaine sans revue humaine systématique : risque de baisse de qualité et dérive brand.

## Fichier résultat

Après adaptation complète : `systems/workflows/wp-draft-brand-voice-W204.json`

Prêt pour import via MCP n8n-mcp ou UI n8n.

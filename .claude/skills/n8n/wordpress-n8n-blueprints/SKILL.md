---
name: wordpress-n8n-blueprints
description: |
  Blueprints n8n canoniques pour automatiser WordPress + schoolsWP : auto-tagging articles, génération
  de contenu dans la voix de marque, chatbot de site, taxonomisation, résumé auto-publié, ingestion
  d'articles existants. Base : analyse des 6 workflows WordPress du catalogue enescingoz +
  patterns internes schoolsWP. Déclenche ce skill quand l'utilisateur veut : "automatiser quelque chose
  sur WordPress avec n8n", "workflow WordPress AI", "auto-tag articles", "génération brand-voice",
  "chatbot WordPress n8n", "indexer le site dans n8n", "synchroniser WP avec n8n". Complémentaire à
  n8n-workflow-patterns (patterns généralistes) et n8n-template-finder (recherche dans catalogue).
  Ce skill se concentre sur les patterns WordPress spécifiquement et leurs adaptations schoolsWP.
---

# WordPress n8n Blueprints

Patterns canoniques pour automatiser WordPress avec n8n, adaptés à schoolsWP.

## Quand activer

Demande contenant **WordPress** + **n8n** + une des finalités suivantes :
- Tag auto / taxonomisation d'articles
- Génération d'articles AI (brand voice)
- Chatbot site WordPress
- Ingestion / indexation d'articles existants (vers vector store)
- Résumé auto-publié (bloc "TL;DR")
- Monitoring contenu (nouveaux posts → pipeline aval)

Si la demande est WordPress mais **sans n8n** (ex : optimisation SEO d'un article) : router vers skills contenu/SEO. Si demande n8n mais **sans WordPress** : `n8n-orchestrator`.

## Blueprints disponibles

Les 6 blueprints principaux, avec source enescingoz et adaptation schoolsWP :

### 1. Auto-Tag Blog Posts (brand-consistent)

**Source** : `WordPress/Auto-Tag Blog Posts in WordPress with AI.json` (16 KB, enescingoz)

**Stack** : Webhook ou WP Trigger → Fetch post → LLM (catégorisation) → WP REST API (update tags)

**Adaptation schoolsWP** (voir `references/auto-tag-blog-posts.md`) :
- Trigger : WP Trigger (publish + update) au lieu de Webhook manuel
- LLM : Anthropic claude-sonnet-4-6 (remplace OpenAI)
- Taxonomie cible : tags schoolsWP existants (cluster-lms, cluster-crm, cluster-seo, etc.)
- Guard : ne pas overrider les tags manuels (conserver + compléter)

**Cas d'usage schoolsWP** : tagger rétroactivement les 144 articles existants + auto-tag des nouveaux.

### 2. Brand Voice Content Generator

**Source** : `WordPress/Automate Blog Creation in Brand Voice with AI.json` (17 KB, enescingoz)

**Stack** : Sheet (briefs) → LLM with brand-voice prompt → WP REST (create draft)

**Adaptation schoolsWP** (voir `references/brand-voice-generator.md`) :
- Brand voice prompt : injecter `shared/brand.md` de schoolswp-agents comme context
- Guardrails : passer par `branding` skill en mode check avant publication
- Status par défaut : `draft` (jamais `publish` auto)
- Meta SEO : délégué à Rank Math (laisser vide, pas d'override REST)

**Cas d'usage schoolsWP** : pipeline "brief → draft WP" pour les articles de la content factory (brain-lite ou thruuu-writer).

### 3. WordPress AI Chatbot (Supabase + OpenAI)

**Source** : `WordPress/WordPress - AI Chatbot to enhance user experience - with Supabase and OpenAI.json` (33 KB, enescingoz)

**Stack** : Webhook → Vector search (Supabase) → RAG Agent → Response

**Adaptation schoolsWP** (voir `references/wordpress-ai-chatbot.md`) :
- Source de connaissance : articles schoolswp.com (ingestion via blueprint #5)
- Vector store : Supabase déjà configuré dans l'écosystème
- LLM : Anthropic claude-haiku-4-5-20251001 (coût/latence)
- Intégration front : Kadence Block custom ou plugin chatbot (à valider)

**Cas d'usage schoolsWP** : assistant site sur schoolswp.com répondant aux questions sur les plugins, CRM, LMS, etc.

### 4. Content Generator with DeepSeek R1

**Source** : `WordPress/Automate Content Generator for WordPress with DeepSeek R1.json` (12 KB, enescingoz)

**Stack** : Trigger → DeepSeek R1 → WP REST (create)

**Adaptation schoolsWP** : **à écarter** sauf si Michael veut tester DeepSeek. Blueprint #2 (Brand Voice) couvre le même cas avec Anthropic qui est déjà la stack principale.

### 5. Article Ingestion / RAG Indexing

**Source** : combinaison `OpenAI_and_LLMs/AI chat with any data source.json` + pattern interne schoolsWP

**Stack** : Schedule (daily) → WP REST (fetch posts) → Text splitter → Embeddings → Vector store upsert

**Adaptation schoolsWP** (voir `references/rag-ingestion.md`) :
- Source : `GET /wp-json/wp/v2/posts?per_page=100&modified_after=<last-run>`
- Chunking : 1500 tokens, overlap 150 (pas 400/40 du catalogue, inadapté au FR long)
- Embeddings : OpenAI `text-embedding-3-large` (meilleur pour le français)
- Vector store : Supabase (table `schoolswp_articles_embeddings`)
- Idempotence : clé = `post_id + modified_date`

**Cas d'usage schoolsWP** : alimente le chatbot (blueprint #3) + recherche sémantique interne pour le skill `cluster-cocon-automatique`.

### 6. Auto-Summary Block (TL;DR)

**Source** : `OpenAI_and_LLMs/AI-Generated Summary Block for WordPress Posts.json` (taille à vérifier)

**Stack** : WP Trigger (publish) → LLM (résumé 3 bullets) → WP REST (update post meta `rank_math_description` + custom field TL;DR)

**Adaptation schoolsWP** (voir `references/auto-summary-block.md`) :
- Résumé à injecter dans un bloc Kadence "Info Box" en haut d'article
- Meta Rank Math : utiliser l'endpoint dédié `/wp-json/rankmath/v1/updateMeta` (voir mémoire `reference_rank_math_rest_limits`)
- Guardrail : pas d'écrasement d'un TL;DR manuel existant (check custom field d'abord)

## Ordre d'implémentation recommandé

Pour Q2 2026, si Michael veut industrialiser :

1. **Blueprint #5 (Article Ingestion)** : prérequis pour chatbot et recherche sémantique
2. **Blueprint #1 (Auto-Tag)** : quick win sur les 144 articles existants
3. **Blueprint #3 (AI Chatbot)** : feature visible, ROI marketing
4. **Blueprint #6 (Auto-Summary)** : complément UX après chatbot
5. **Blueprint #2 (Brand Voice Generator)** : à intégrer à la content factory, pas en standalone

## Garde-fous WordPress schoolsWP

- **Rank Math meta** : jamais via core REST `/wp/v2/posts` (silent-ignore). Endpoint dédié obligatoire.
- **Status WP** : toujours `draft` en auto-création. Publish manuel.
- **Taxonomies** : utiliser les slugs existants (cluster-*), ne pas créer de nouveaux tags auto.
- **Images** : si blueprint génère des images, passer par skill `wp-image-metadata-seo` pour les métadonnées.
- **URLs** : respecter `feedback_evergreen_slugs` (pas d'année, pas de "schoolswp" dans slug).

## Références

- `references/auto-tag-blog-posts.md`
- `references/brand-voice-generator.md`
- `references/wordpress-ai-chatbot.md`
- `references/rag-ingestion.md`
- `references/auto-summary-block.md`
- `examples/schoolswp-auto-tag-workflow.md` : exemple complet adapté

## Complémentaire à

- `n8n-template-finder` : sourcer de nouveaux templates WordPress non couverts
- `n8n-workflow-adapter` : adapter un template brut avant import
- `n8n-workflow-patterns` : patterns architecturaux généralistes (non-WP)

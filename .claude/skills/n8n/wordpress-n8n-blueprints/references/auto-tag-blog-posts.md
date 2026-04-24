# Blueprint : Auto-Tag Blog Posts (adapté schoolsWP)

**Source amont** : `enescingoz/awesome-n8n-templates/WordPress/Auto-Tag Blog Posts in WordPress with AI.json` (16 KB)

**Objectif** : taguer automatiquement les articles schoolsWP selon leur sujet, sans overrider les tags manuels.

## Stack adaptée

```
WP Trigger (publish + update)
  → GET post via REST /wp/v2/posts/<id>?context=edit
  → Analyse LLM (claude-sonnet-4-6) : classify into schoolsWP cluster tags
  → GET existing tags
  → IF (existing tags from whitelist) → append proposed tags
    ELSE → replace with proposed tags
  → POST /wp/v2/posts/<id> avec tags update
  → LOG Discord webhook
```

## Taxonomie cible (tags existants schoolsWP)

Clusters éditoriaux à utiliser comme labels de classification :

- `cluster-lms` : TutorLMS, LearnDash, LifterLMS, Teachable
- `cluster-crm` : FluentCRM, FluentBoards, FluentSMTP, FluentForms
- `cluster-seo` : Rank Math, SEO technique, GEO/AIO
- `cluster-automation` : n8n, OttoKit/SureTriggers, WP Fusion, Zapier
- `cluster-ecommerce` : FluentCart, SureCart, WooCommerce, Petit Papier Magique
- `cluster-performance` : FlyingPress, Perfmatters, Cloudflare, hosting
- `cluster-design` : Kadence, Astra, Generatepress, Gutenberg
- `cluster-affiliate` : comparatifs, avis, monetization affiliate
- `cluster-formation` : création de cours, pédagogie, tunnels

Mapping additif si nécessaire : ajouter un tag thématique transverse (ex : `tutoriel`, `comparatif`, `avis`) en plus du cluster.

## Prompt de classification (LLM node)

```
Tu es un classificateur de contenu WordPress pour le site schoolswp.com.
Voici la liste des clusters éditoriaux disponibles :
- cluster-lms, cluster-crm, cluster-seo, cluster-automation, cluster-ecommerce,
  cluster-performance, cluster-design, cluster-affiliate, cluster-formation

Contenu de l'article (premiers 3000 tokens) :
{{$json.content.rendered}}

Titre : {{$json.title.rendered}}
Extrait : {{$json.excerpt.rendered}}

Instructions :
1. Identifie le ou les clusters pertinents (max 2)
2. Si aucun ne s'applique à 70%+, réponds "SKIP"
3. Format de sortie strict JSON :
   {"clusters": ["cluster-xxx"], "reason": "..."}
```

## Guardrails schoolsWP

1. **Ne pas overrider les tags manuels existants**. Règle : si l'article a déjà des tags qui ne sont pas dans la whitelist (= tags ajoutés à la main par Michael), on APPEND, on ne REPLACE pas.

2. **Dry-run obligatoire** sur les 5 premiers articles avant rollout massif. Vérifier le rapport Discord et confirmer avant activation complète.

3. **Skip si LLM renvoie SKIP** : ne jamais forcer une classification. Mieux vaut aucun tag auto que tag incorrect.

4. **Log tous les changements** dans un channel Discord dédié (#auto-tag-log) pour audit et rollback.

## Adaptation du JSON externe

Étapes du sanitize via `n8n-workflow-adapter` :

1. Nom workflow : `wp-auto-tag-posts-W201`
2. Credentials :
   - OPENAI_API → retirer + swap node vers lmChatAnthropic (anthropic-main)
   - WORDPRESS_API → wp-schoolswp-main
3. URLs : aucune occurrence à remplacer (le template pointe vers le WordPress du node credential)
4. Trigger : swap `webhook` vers `wordpressTrigger` (publish + update events)
5. Ajouter node `IF` pour check des tags manuels existants
6. Ajouter node `discord` pour log webhook

## Rollout recommandé schoolsWP

### Phase 1 : dry-run sur 5 articles (manuel)

Exécuter le workflow en mode manuel sur 5 articles choisis (1 par cluster attendu). Vérifier la cohérence des tags proposés.

### Phase 2 : batch rétroactif (144 articles existants)

Si phase 1 OK : lancer en batch sur les 144 articles existants. Prévoir 24h pour éviter le rate limit Anthropic.

### Phase 3 : activation temps réel

Activer le WordPress Trigger. Monitoring Discord pour les 2 premières semaines.

## Métriques de succès

- % articles avec au moins 1 cluster tag : > 90%
- % articles où le tag auto a été corrigé manuellement ensuite : < 10% (sinon retourner au prompt)
- Temps moyen d'exécution par article : < 15s
- Coût moyen par classification : < $0.01 avec claude-sonnet-4-6

## Fichier résultat

Après adaptation complète : `systems/workflows/wp-auto-tag-posts-W201.json`

Prêt pour import via MCP n8n-mcp ou UI n8n.

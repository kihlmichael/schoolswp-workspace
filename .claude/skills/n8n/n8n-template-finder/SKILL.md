---
name: n8n-template-finder
description: |
  Recherche le template n8n le plus pertinent dans le catalogue externe curated (enescingoz/awesome-n8n-templates, 280+ workflows, 15 catégories) pour un cas d'usage schoolsWP. Retourne top 3 candidats avec URL raw GitHub, catégorie, intégrations détectées et adaptation requise pour schoolswp-n8n.wp1.host.
  Utilise ce skill quand l'utilisateur dit : "trouve un workflow n8n pour X", "template n8n existant pour Y", "y a-t-il déjà un workflow qui fait Z", "cherche un template n8n", "workflow n8n tout fait", ou AVANT toute conception custom pour ne pas réinventer.
  NE PAS utiliser pour : adapter le template trouvé pour schoolsWP (utiliser n8n-workflow-adapter en aval), créer un workflow from scratch quand aucun template ne matche (utiliser n8n-orchestrator puis n8n-workflow-architect), ou pour les patterns WordPress + n8n spécifiquement (utiliser wordpress-n8n-blueprints).
---

# n8n Template Finder

Recherche dans un catalogue externe de 280+ workflows n8n curated, trie par pertinence pour schoolsWP, et recommande les adaptations nécessaires avant import dans l'instance.

## Quand activer ce skill

**Avant toute conception from-scratch d'un workflow n8n.** Priorité de décision :

1. n8n-template-finder (ce skill) : le workflow cible existe-t-il déjà ?
2. Si oui : import + adaptation via n8n-workflow-adapter
3. Si non : cadrage via n8n-orchestrator puis création via n8n-workflow-architect

## Source

**Repo** : enescingoz/awesome-n8n-templates (MIT license, 21k stars, maintenu avril 2026).

Organisé en 15 catégories : WordPress, Gmail, Telegram, Slack, Discord, WhatsApp, Notion, OpenAI_and_LLMs, Airtable, Google_Drive, Forms, PDF, DevOps, HR, AI_Research_RAG.

## Protocole de recherche

### Phase 1 : Cadrage du besoin (30 secondes)

L'utilisateur arrive avec une formulation en langage naturel. Extraire 3 filtres :

```
Trigger voulu     : Webhook | Schedule | App (Gmail/WP/Telegram/...) | Manual
Intégrations clés : [liste des apps qui doivent apparaître]
Finalité          : [ingestion | transformation | notification | RAG | agent IA]
```

Si un des filtres est ambigu, **poser une question** plutôt que d'inventer.

### Phase 2 : Recherche dans le manifest

Le manifest local data/enescingoz-manifest.json indexe les 280+ templates avec :

```json
{
  "name": "Auto-Tag Blog Posts in WordPress with AI",
  "category": "WordPress",
  "path": "WordPress/Auto-Tag Blog Posts in WordPress with AI.json",
  "raw_url": "https://raw.githubusercontent.com/enescingoz/awesome-n8n-templates/main/...",
  "size_kb": 16,
  "integrations": ["wordpress", "openai"],
  "triggers": ["webhook"]
}
```

**Stratégie de matching** :

- Match exact sur catégorie si le nom d'app schoolsWP est dans la requête (WordPress, Gmail, Telegram)
- Scoring : +3 si catégorie directe, +2 par intégration matchée, +1 par keyword du nom matché
- Retourner top 3 par score décroissant

### Phase 3 : Recommandation structurée

Format de sortie en markdown, prêt à coller en chat :

```markdown
## Top 3 templates pertinents

### 1. [Nom du template] — score X/10
- Catégorie : WordPress
- Intégrations : WordPress, OpenAI, Supabase
- Trigger : Webhook
- URL raw : <url>
- Taille : 16 KB (logique riche)
- Pertinence : [1 phrase expliquant pourquoi ce template match]
- Adaptations nécessaires schoolsWP :
  - Swap OPENAI_API placeholder vers credential schoolsWP anthropic-main
  - Renommer workflow selon convention wp-<verb>-<subject>-Wxxx
  - Remplacer URL WordPress vers https://schoolswp.com

### 2. [...]

### 3. [...]
```

### Phase 4 : Si aucun match satisfaisant

Si les 3 candidats ont un score < 5/10 : retourner la conclusion **"Pas de template satisfaisant dans enescingoz"** et rediriger vers n8n-orchestrator + n8n-workflow-architect pour création from-scratch.

Ne jamais forcer un template qui ne match pas. Mieux vaut une création propre qu'une adaptation qui coûte plus cher que le from-scratch.

## Régénération du manifest

Le manifest est généré par scripts/build_manifest.py. À relancer quand :

- le repo amont a reçu un push (vérifier pushedAt via gh repo view enescingoz/awesome-n8n-templates)
- un nouveau besoin arrive sur une catégorie faiblement indexée (flag --deep pour parser chaque JSON)

Commande (depuis la racine projet) :

```
.venv/Scripts/py -m build_manifest --deep
```

Ou directement :

```
.venv/Scripts/py .claude/skills/n8n/n8n-template-finder/scripts/build_manifest.py --deep
```

Le flag --deep télécharge chaque JSON et extrait les types de nodes (pour enrichir le champ integrations). Sans --deep, le manifest se base uniquement sur le nom du fichier et la catégorie.

## Étape de téléchargement

Quand un template est retenu, télécharger via :

```
Invoke-WebRequest -Uri <raw_url> -OutFile /tmp/template.json
```

Puis invoquer n8n-workflow-adapter pour sanitize et rebrand avant import.

## Garde-fous

- **Ne jamais** importer un template enescingoz directement sans passer par n8n-workflow-adapter (credentials placeholders, conventions de nommage non schoolsWP).
- **Ne pas** recommander un template qui utilise une stack non disponible chez schoolsWP (ex : Baserow si on a Airtable, Ollama local si on n'héberge pas Ollama).
- **Prioriser** les templates size_kb > 10 (logique riche) sur les templates size_kb < 8 (souvent des squelettes).

## Références

- references/categories.md : mapping catégories enescingoz vers cas d'usage schoolsWP
- data/enescingoz-manifest.json : index complet (généré)
- Complément : n8n-workflow-adapter pour l'étape post-download

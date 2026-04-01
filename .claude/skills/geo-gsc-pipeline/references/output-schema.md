# Schema JSON — GEO GSC Pipeline

Ce document decrit la structure exacte du JSON de sortie. Chaque champ est documente avec son type, sa cardinalite et un exemple.

---

## Structure racine

```json
{
  "meta": { ... },
  "v1_primary_prompts": [ ... ],
  "v2_clusters": [ ... ],
  "v3_pages_spec_p1": [ ... ],
  "questions_for_user": [ ... ]
}
```

Toutes les cles sont obligatoires. Si une phase n'est pas encore executee (ex: V3 pas encore demandee), retourner un tableau vide `[]`.

---

## meta

```json
{
  "property": "schoolswp.fr",
  "date_range": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "exported_at": "YYYY-MM-DD",
  "filters": {
    "country": "FR | ALL",
    "device": "desktop | mobile | ALL"
  },
  "data_quality": "gsc_real | serp_estimated | mixed",
  "source_file": "nom-du-fichier.csv"
}
```

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `property` | string | oui | Domaine cible (ex: `schoolswp.fr`) |
| `date_range.start` | string (date) | oui | Debut de la periode analysee |
| `date_range.end` | string (date) | oui | Fin de la periode analysee |
| `exported_at` | string (date) | oui | Date de generation du JSON |
| `filters.country` | string | oui | Pays filtre (`FR`, `US`, `ALL`) |
| `filters.device` | string | oui | Device filtre (`desktop`, `mobile`, `ALL`) |
| `data_quality` | string | oui | Qualite des metriques : `gsc_real` (export GSC), `serp_estimated` (estimation depuis SERP), `mixed` |
| `source_file` | string | non | Nom du fichier source si applicable |

---

## v1_primary_prompts (tableau)

Chaque element :

```json
{
  "query_raw": "seokey wordpress",
  "primary_prompt_geo": "Comment utiliser seokey wordpress ?",
  "intent": "INFO",
  "gsc_metrics": {
    "clicks": 0,
    "impressions": 400,
    "ctr": 0.0,
    "position": 10.0
  },
  "top_pages": [
    {
      "url": "https://schoolswp.fr/seokey-guide/",
      "impressions": 200,
      "clicks": 5
    }
  ]
}
```

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `query_raw` | string | oui | Texte exact de la requete source (GSC ou SERP) |
| `primary_prompt_geo` | string | oui | Question en langage naturel, fidele au wording original |
| `intent` | enum | oui | `INFO` ou `COMM` |
| `gsc_metrics.clicks` | number | oui | Nombre de clics (0 si indisponible) |
| `gsc_metrics.impressions` | number | oui | Nombre d'impressions (0 si indisponible) |
| `gsc_metrics.ctr` | number | oui | CTR en decimal (0.05 = 5%) |
| `gsc_metrics.position` | number | oui | Position moyenne (0.0 si indisponible) |
| `top_pages` | array | oui | Pages associees (vide `[]` si indisponible) |
| `top_pages[].url` | string | oui | URL de la page |
| `top_pages[].impressions` | number | oui | Impressions de cette page pour cette requete |
| `top_pages[].clicks` | number | oui | Clics de cette page pour cette requete |

---

## v2_clusters (tableau)

Chaque element :

```json
{
  "cluster_canonique": "[WP-Plugins] / [Pricing] / [COMM] / [SEOKey tarifs]",
  "priority": "P1",
  "decision": "NEW",
  "rationale": "Potentiel GEO: 400 impressions. Forte intention commerciale detectee.",
  "primary_prompts_refs": [
    "How much does SEOKEY cost?"
  ],
  "detected_overlap": []
}
```

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `cluster_canonique` | string | oui | Format strict : `[Univers] / [Type] / [Intention] / [Objet]` |
| `priority` | enum | oui | `P1`, `P2`, ou `P3` |
| `decision` | enum | oui | `UPDATE`, `NEW`, ou `MERGE` |
| `rationale` | string | oui | Justification courte (metriques + raison) |
| `primary_prompts_refs` | array[string] | oui | Liste des `primary_prompt_geo` associes a ce cluster |
| `detected_overlap` | array[string] | oui | Noms de clusters en chevauchement (vide si aucun) |

### Format du cluster canonique

```
[Univers] / [Type] / [Intention] / [Objet]
```

- **Univers** : `WP-Core` | `WP-Plugins` | `WP-SEO` | `WP-Performance` | `WP-Security` | `WP-Hosting` | `WP-Ecommerce` | `WP-LMS` | `WP-CRM` | `WP-Automation` | `WP-Builders` | `WP-Analytics` | `WP-Content` | `WP-Forms` | `WP-Translate` | `WP-Theme`
- **Type** : `Guide` | `Comparatif` | `Checklist` | `Tutoriel` | `Avis` | `Pricing` | `Setup` | `Depannage` | `Alternatives` | `Template`
- **Intention** : `INFO` | `COMM`
- **Objet** : court, explicite, sans jargon

---

## v3_pages_spec_p1 (tableau)

Chaque element :

```json
{
  "cluster_canonique": "[WP-Plugins] / [Pricing] / [COMM] / [SEOKey tarifs]",
  "slug_suggested": "seokey-wordpress-guide-complet",
  "h1": "SEOKey WordPress : pricing complet",
  "short_answer_60_70_words": "Reponse auto-contenue, citable, factuelle. 60 a 70 mots exactement.",
  "outline": [
    {
      "h2": "Section titre",
      "bullets": ["point 1", "point 2"]
    },
    {
      "h2": "Comparatif",
      "table": {
        "columns": ["Critere", "Option A", "Option B"],
        "rows": [["Prix", "79EUR", "99EUR"]]
      }
    },
    {
      "h2": "FAQ",
      "qa": [
        {"q": "Question ?", "a": "Reponse courte."}
      ]
    }
  ],
  "secondary_prompts_geo": [
    {
      "category": "decisionnel",
      "prompt": "Quelle licence choisir pour un freelance ?",
      "intent": "COMM"
    }
  ],
  "thruuu_upload_list": {
    "primary": ["requete principale"],
    "secondary": ["prompt secondaire 1", "prompt secondaire 2"]
  }
}
```

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `cluster_canonique` | string | oui | Reference au cluster V2 |
| `slug_suggested` | string | oui | Slug WordPress suggere (kebab-case) |
| `h1` | string | oui | Titre H1 de la page |
| `short_answer_60_70_words` | string | oui | Reponse courte AIO (60-70 mots, auto-contenue) |
| `outline` | array | oui | Sections H2 de la page |
| `outline[].h2` | string | oui | Titre de la section |
| `outline[].bullets` | array[string] | non | Points cles de la section |
| `outline[].table` | object | non | Tableau comparatif |
| `outline[].table.columns` | array[string] | oui si table | En-tetes de colonnes |
| `outline[].table.rows` | array[array[string]] | oui si table | Lignes du tableau |
| `outline[].qa` | array[object] | non | Questions-reponses (section FAQ) |
| `outline[].qa[].q` | string | oui si qa | Question |
| `outline[].qa[].a` | string | oui si qa | Reponse courte |
| `secondary_prompts_geo` | array | oui | 20-30 prompts secondaires |
| `secondary_prompts_geo[].category` | enum | oui | `decisionnel` | `risque` | `comparatif` | `solution` | `checklist` |
| `secondary_prompts_geo[].prompt` | string | oui | Prompt en langage naturel |
| `secondary_prompts_geo[].intent` | enum | oui | `INFO` ou `COMM` |
| `thruuu_upload_list` | object | oui | Prompts pour monitoring Thruuu |
| `thruuu_upload_list.primary` | array[string] | oui | Prompts principaux |
| `thruuu_upload_list.secondary` | array[string] | oui | Prompts secondaires |

---

## questions_for_user (tableau)

```json
[
  "Veux-tu que je genere aussi les specs V3 pour les clusters P2 ?",
  "Dois-je creer des fichiers Markdown separes par page ?",
  "Souhaites-tu un export CSV des prompts Thruuu pour upload direct ?"
]
```

Tableau de strings. Poser des questions utiles pour guider la prochaine iteration :
- Generation de phases supplementaires (V3 pour P2, P3)
- Formats de sortie supplementaires (Markdown, CSV)
- Clarifications sur les donnees ou le scope

---

## Exemple complet minimal

```json
{
  "meta": {
    "property": "schoolswp.fr",
    "date_range": {"start": "2025-12-10", "end": "2026-02-08"},
    "exported_at": "2026-02-08",
    "filters": {"country": "FR", "device": "ALL"},
    "data_quality": "serp_estimated",
    "source_file": "95_-_seokey_wordpress.xlsx"
  },
  "v1_primary_prompts": [
    {
      "query_raw": "How much does SEOKEY cost?",
      "primary_prompt_geo": "How much does SEOKEY cost?",
      "intent": "COMM",
      "gsc_metrics": {"clicks": 0, "impressions": 400, "ctr": 0.0, "position": 10.0},
      "top_pages": []
    }
  ],
  "v2_clusters": [
    {
      "cluster_canonique": "[WP-Plugins] / [Pricing] / [COMM] / [SEOKey tarifs]",
      "priority": "P1",
      "decision": "NEW",
      "rationale": "400 impressions, intention COMM forte",
      "primary_prompts_refs": ["How much does SEOKEY cost?"],
      "detected_overlap": []
    }
  ],
  "v3_pages_spec_p1": [],
  "questions_for_user": [
    "Veux-tu que je produise la spec V3 pour le cluster P1 ?"
  ]
}
```

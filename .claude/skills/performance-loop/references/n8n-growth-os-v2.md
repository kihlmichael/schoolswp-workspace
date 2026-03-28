# schoolsWP Growth OS — V2

**V2 = optimiser l'existant + générer 1 nouvel article SEO / semaine**

```text
Bloc 1 : GSC → score → patch SEO → draft WordPress
Bloc 2 : GSC → détection sujet émergent → brief SEO → draft nouvel article
```

---

## Rythme recommandé

| Fréquence    | Action                            |
| ------------ | --------------------------------- |
| Quotidien    | Daily SEO Watch                   |
| 2× / semaine | Patch pages P1/P2                 |
| Hebdo        | 1 sujet sélectionné + 1 brouillon |

**Objectif hebdomadaire concret :**

- 3 à 5 pages à optimiser
- 1 patch prêt
- 1 nouvelle idée validée
- 1 brouillon article

---

## 4 workflows

| #   | Workflow                  | Déclencheur                 | Rôle                                                |
| --- | ------------------------- | --------------------------- | --------------------------------------------------- |
| 1   | Daily SEO Watch           | Quotidien                   | Récupère pages GSC, score, envoie dans `seo_pages`  |
| 2   | SEO Patch Generator       | Pages P1/P2                 | Propose title/meta/FAQ, crée draft WP               |
| 3   | Weekly Topic Discovery    | Lundi 08:00                 | Requêtes GSC → détecte sujets émergents → choisit 1 |
| 4   | New Article Draft Builder | Manuel ou `status=selected` | Brief + draft complet + draft WordPress             |

---

## Stack V2 minimale

- GSC
- Google Sheets
- n8n
- WordPress REST API
- OpenAI (LLM)

Pas besoin de : Airtable, dashboard complexe, multi-agent.

---

## Google Sheets — onglets

On garde `seo_pages` + `seo_tasks`.

### Onglet `topic_ideas` (nouveau)

```text
created_at
source_url
detected_query
grouped_topic
impressions_28d
clicks_28d
position_28d
decision
working_title
target_intent
brief_h2_h3
faq
cta
draft_url
status
```

**Statuts :** `detected` → `selected` → `drafted` → `reviewed` → `published`

---

## Workflow 3 — Weekly Topic Discovery

### Déclencheur

Cron — lundi 08:00 — hebdomadaire

### Pipeline

```text
1. GSC Query (dimensions: page + query, période: 28j)
2. Filtre (impressions > 50, position 8-30, CTR faible, non brandé)
3. Code — Groupement sémantique
4. LLM — Choix du sujet
5. Google Sheets — Append topic_ideas
```

### Node 2 — Filtre

Critères de garde :

- `impressions > 50`
- `position` entre 8 et 30
- CTR faible
- non brandées

Exclusions : `schoolsWP`, `michaël kihl`, variantes marque

### Node 3 — Code : Groupement sémantique

Regrouper les requêtes proches :

```text
fluent forms avis + avis fluent forms + test fluent forms
→ groupe : "fluent forms avis"
```

### Node 4 — LLM : Choix du sujet

Question unique : créer une nouvelle page, enrichir l'existant, ou ignorer ?

Sortie JSON :

```json
{
  "decision": "NEW_ARTICLE",
  "grouped_topic": "",
  "working_title": "",
  "target_intent": "",
  "reason_why": "",
  "cta": ""
}
```

---

## Workflow 4 — New Article Draft Builder

### Pipeline

```text
1. Lire ligne topic_ideas (status = selected)
2. LLM — Générer brief SEO
3. LLM — Générer draft complet
4. WordPress REST API — Créer draft (status = draft)
5. Google Sheets — Update (draft_url + status = drafted)
```

### Prompt — Brief SEO

```text
Tu es rédacteur SEO WordPress pour schoolsWP.

Sujet : {{grouped_topic}}
Titre de travail : {{working_title}}
Intention : {{target_intent}}

Tâche :
Produis un brief d'article clair et exploitable avec :
1) angle éditorial
2) promesse de l'article
3) plan H2/H3
4) 5 FAQ
5) CTA final

Style : direct, utile, concret, pédagogique.
```

### Prompt — Draft complet

```text
Tu rédiges un brouillon d'article pour schoolsWP.

Sujet : {{working_title}}
Plan : {{brief_h2_h3}}
FAQ : {{faq}}
CTA : {{cta}}

Contraintes :
- ton schoolsWP
- phrases courtes
- pédagogique
- actionnable
- pas de blabla
- introduction claire
- H2/H3 propres
- conclusion avec CTA
```

### WordPress REST API

```text
POST /wp-json/wp/v2/posts
status = draft
```

---

## Logique de décision

| Priorité | Action                              | Raison                     |
| -------- | ----------------------------------- | -------------------------- |
| 1        | Optimiser pages existantes visibles | Plus rapide à rentabiliser |
| 2        | Nouveau sujet (1/semaine max)       | Vrai potentiel détecté     |

**La V2 n'est pas "publier partout" — c'est :**

- réparer ce qui a déjà du trafic
- ajouter une nouvelle pièce rentable chaque semaine

---

## Plan d'implémentation V2

1. Faire tourner V1 correctement
2. Créer onglet `topic_ideas`
3. Ajouter workflow `Weekly Topic Discovery`
4. Ajouter workflow `New Article Draft Builder`
5. Limiter à 1 sujet/semaine

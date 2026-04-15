---
name: geo-architect
description: GEO/AIO pipeline schoolsWP — transformer des requêtes (GSC, SERP, mots-clés) en clusters canoniques, prompts monitorables et pages AIO-ready. Use when user provides keywords, GSC queries, seed list, or asks to build GEO prompts, create AIO-ready page structure, prepare Thruuu monitoring, or cluster WordPress content topics. Supports phases: V1 (qualify) | V2 (cluster + prioritize) | V3 (AIO-ready page) | full (V1+V2+V3 en une passe).
metadata:
  author: Michaël KIHL
  brand: schoolsWP
  version: 1.0.0
  category: seo-geo-aio
  tags: [seo, geo, aio, prompts, thruuu, monitoring, wordpress, content]
---

# GEO Architect — Pipeline GEO/AIO schoolsWP

## Mission

Transformer des requêtes brutes (GSC, SERP, mots-clés) en :
1. Clusters canoniques stables
2. Listes de prompts GEO monitorables (Thruuu)
3. Pages WordPress conçues pour être citées dans les réponses IA

---

## Règles de marque (non négociables)

- Toujours écrire **schoolsWP** — jamais SchoolsWP, schoolswp, Schoolswp
- Tutoiement systématique en français
- Zéro fluff, zéro promesse non prouvée
- Toujours penser : "est-ce qu'une IA aurait envie de citer ça ?"

---

## Invocation

Format d'appel : `/geo-architect [phase] [input]`

| Phase | Déclencheur | Sortie |
|-------|-------------|--------|
| `V1` | 1 mot-clé ou liste brute | primary prompts qualifiés |
| `V2` | liste seeds ou V1 | clusters + priorisation + action type |
| `V3` | 1 cluster ou V2 | page AIO-ready complète |
| `full` | 1 mot-clé | V1+V2+V3 en une seule passe |

Si la phase n'est pas précisée → exécuter `full`.

---

## Phase V1 — Identification & qualification

**But** : constituer une liste de prompts réalistes.

### Process
1. Identifier le/les seeds (requêtes fournies)
2. Générer les variantes :
   - questions naturelles (comment / pourquoi / quel / faut-il / est-ce que)
   - long-tail (≥ 5 mots)
   - problèmes / risques
   - comparaisons / alternatives
3. Tagger intention : `INFO` ou `COMM`
4. Normaliser : 1 prompt = 1 question, langage naturel, pas de variables

### Sortie V1
```
primary_prompt:  [requête principale]
support_prompts: [liste 10–30 prompts secondaires]
intention:       INFO | COMM
```

---

## Phase V2 — Structuration & priorisation

**But** : transformer la liste en backlog éditorial pilotable.

### Cluster canonique
Format strict :
```
[Univers] / [Type] / [Intention] / [Objet]
```

**Univers** (choisir 1) :
`WP-Core` · `SEO` · `Perf` · `Security` · `Hosting` · `Ecommerce` · `LMS` · `CRM-Email` · `Automation` · `Builders` · `Analytics` · `Content`

**Type** (choisir 1) :
`Guide` · `HowTo` · `Troubleshooting` · `Comparatif` · `Avis` · `Alternatives` · `Pricing` · `Checklist` · `Template`

**Intention** : `INFO` ou `COMM`

**Objet** : nom du plugin / concept / problème

Exemple :
```
WP-Core / Guide / COMM / Maintenance WordPress
Builders / Avis / COMM / Kadence WP
SEO / Comparatif / COMM / Plugins Traduction WordPress
```

### Décision éditoriale
- `UPDATE` — page existante à améliorer
- `NEW` — aucune page ne répond clairement
- `MERGE` — 2+ pages se cannibalisent → consolider

### Priorité
- `P1` — COMM à fort potentiel ou forte demande
- `P2` — INFO à fort volume
- `P3` — niche ou secondaire

### Sortie V2
```
cluster_canon:  [Univers / Type / Intention / Objet]
action_type:    UPDATE | NEW | MERGE
priority:       P1 | P2 | P3
target_url:     [URL existante si UPDATE/MERGE]
```

---

## Phase V3 — Page AIO-ready

**But** : créer UNE page pilier conçue pour être citée par les IA.

### Structure obligatoire

**Bloc 1 — Réponse courte** (60–70 mots maximum)
> La réponse directe à la question principale. C'est ce bloc qui est le plus cité en AIO.

**Bloc 2 — Contenu principal**
Selon le type :
- `Avis` → avantages / limites / pour qui / alternatives
- `Comparatif` → tableau comparatif + critères
- `Guide/HowTo` → étapes numérotées + checklist
- `Troubleshooting` → symptôme → cause → solution

**Bloc 3 — Tableau** (si COMM)
Toujours inclure un tableau → top format cité par les IA.

**Bloc 4 — Recommandation schoolsWP**
2–4 lignes, assumées, signées.
> "Si tu veux X → choisis Y. Dans mon cas sur schoolsWP, j'utilise Z parce que…"

**Bloc 5 — FAQ GEO** (5–8 questions)
Issues directement des prompts secondaires V1.

**Bloc 6 — Maillage interne**
- 3–5 liens entrants suggérés
- 2–3 liens sortants (docs officielles)

### Checklist "citation-ready"
- [ ] Réponse courte en haut (60–70 mots)
- [ ] Listes à puces structurées
- [ ] Tableau comparatif ou de synthèse
- [ ] Définitions courtes et claires
- [ ] FAQ explicite (questions complètes)
- [ ] Recommandation assumée
- [ ] Ton neutre + expert + pas de fluff
- [ ] Sections H2 explicites (Prix / Alternatives / Pour qui / Limites)

---

## Philosophie (à garder en tête)

> On ne "fait pas du contenu pour Google".
> On construit des réponses suffisamment claires pour que les IA aient envie de nous citer.

---

## Google Sheet — structure de suivi

| Onglet | Contenu |
|--------|---------|
| 01_GSC_RAW | Export brut GSC |
| 02_SEED_FILTERED | Seeds qualifiés V1 |
| 03_EXPAND_PAA | Prompts enrichis PAA |
| 04_CLUSTER_CANON | Clusters V2 |
| 05_PRIORITIES | Priorisation P1/P2/P3 |
| 06_BRIEFS | Briefs V3 |
| 07_THRUUU_RESULTS | Résultats monitoring |
| 08_ACTIONS_LOG | Historique actions |

Colonnes clés dans `05_PRIORITIES` :
`prompt_final` · `topic_cluster_canon` · `intent` · `gsc_impr` · `gsc_pos` · `gsc_ctr` · `score_qw` · `priority` · `action_type` · `target_url` · `status`

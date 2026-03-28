---
name: dito-engine
description: >
  schoolsWP Omnichannel Engine — prompt DITO (Define · Input · Transformation · Output) pour
  transformation de contenu, repurposing omnicanal et automatisation pipeline. Framework orienté
  process : article → LinkedIn, vidéo → page pilier, transcript → cluster, article → newsletter,
  génération FAQ IA, extraction métadonnées SEO, optimisation featured snippet, repurposing massif.
  Déclencher pour toute demande de transformation ou de repurposing : "transforme cet article en",
  "génère une FAQ à partir de", "convertis ce transcript en", "crée les métadonnées SEO de",
  "adapte ce contenu pour LinkedIn / YouTube / email", "repurpose", "omnicanal",
  "extrais les questions de", "crée un carrousel LinkedIn à partir de".
  Préférer DITO à CREDO quand l'input existe déjà et qu'on cherche à le transformer,
  pas à produire du nouveau contenu from scratch.
---

# schoolsWP Omnichannel Engine

**DITO Edition** — transformation de contenu, repurposing et automatisation pipeline pour schoolsWP.

Framework : **DITO** (Define · Input · Transformation · Output)

---

## Positionnement dans l'écosystème

| Framework | Orientation                            |
| --------- | -------------------------------------- |
| RACE      | Exécution rapide, audit, diagnostic    |
| CREDO     | Production premium from scratch        |
| SPECS     | Cadrage produit, architecture, système |
| PACT      | Résolution, optimisation, itération    |
| DITO      | Transformation, repurposing, pipeline  |

**DITO est le framework de la transformation.**

Tu l'utilises quand tu as une matière brute (article, transcript, notes, données, vidéo) et que tu veux la convertir en autre chose — rapidement, proprement, et avec le bon format de sortie.

Différence clé avec CREDO : CREDO produit du contenu from scratch. DITO transforme ce qui existe déjà.

---

## Cas d'usage DITO

- Article → carrousel LinkedIn
- Article → newsletter FluentCRM
- Article → script YouTube
- Transcript vidéo → article pilier
- Transcript → cluster sémantique
- Notes brutes → page de vente
- Article → FAQ optimisée IA (SGE / Perplexity / ChatGPT)
- Article → métadonnées SEO (XPTitle / XPSubject / XPKeywords)
- Données GSC → plan d'action SEO
- CSV mots-clés → architecture de cluster
- Article → lead magnet PDF

---

## Prompt DITO officiel

### [D] DEFINE

Définir précisément l'objectif de transformation.

- Objectif principal :
- Canal cible (Article / LinkedIn / Newsletter / Email / YouTube / Lead magnet / FAQ / Métadonnées) :
- Intention SEO cible (si applicable) :
- Niveau de profondeur (court / stratégique / expert) :
- Résultat business attendu (trafic / leads / autorité / conversion) :

### [I] INPUT

Fournir la matière brute à transformer.

- Type d'input (article / transcript / notes / données SEO / capture / CSV / résumé) :
- Contenu brut : `[COLLER ICI]`
- Mots-clés principaux :
- Angle stratégique existant :
- Contraintes spécifiques :

### [T] TRANSFORMATION

Décrire ce que l'IA doit faire avec l'input.

- Type de transformation :

```
résumer | structurer | optimiser SEO | reformuler | convertir en carrousel |
extraire FAQ | créer métadonnées | générer script | adapter au canal cible |
réécrire dans un autre ton | extraire les points clés | créer un plan
```

- Niveau d'optimisation IA si applicable (citabilité / featured snippet / SGE / FAQ structurée) :
- Structure attendue :
- Éléments à inclure (CTA / FAQ / hook / tableau / liste priorisée) :
- Éléments à exclure :

### [O] OUTPUT

Spécifier le format final exact.

- Format (Markdown / prêt WordPress / script vidéo / post LinkedIn / email HTML) :
- Longueur cible :
- Ton : direct, clair, actionnable — style schoolsWP
- Structure obligatoire :
- Blocs spécifiques requis (H2/H3, FAQ, métadonnées XP, CTA, hook d'accroche) :

---

## Format de réponse obligatoire

1. Résultat final directement exploitable (pas de brouillon intermédiaire)
2. Optimisation SEO intégrée naturellement si canal SEO
3. Structure hiérarchisée claire
4. Aucun blabla inutile
5. CTA cohérent avec l'objectif si applicable

Si l'input est insuffisant : poser maximum 3 questions. Sinon transformer immédiatement.

---

## Exemples d'appel

### Article → FAQ IA

```
[D] DEFINE
- Objectif : générer une FAQ optimisée pour SGE / ChatGPT / Perplexity
- Canal cible : page article WordPress
- Résultat attendu : être cité par les IA génératives

[I] INPUT
- Type : article WordPress existant
- Contenu : [coller le contenu de l'article]
- KW principal : lms wordpress gratuit

[T] TRANSFORMATION
- Type : extraire FAQ + reformuler en format question/réponse concis
- Niveau IA : citabilité SGE (réponses directes, structure claire)
- Inclure : 8 questions, format H3 + réponse 2-4 phrases

[O] OUTPUT
- Format : Markdown prêt à intégrer dans WordPress
- Structure : H3 "Question ?" + réponse directe + phrase de clôture
- Ton : expert, accessible, sans jargon
```

### Article → Newsletter FluentCRM

```
[D] DEFINE
- Objectif : transformer l'article en email newsletter hebdo
- Canal cible : newsletter WP Insights (FluentCRM)
- Résultat attendu : trafic retour sur l'article

[I] INPUT
- Type : article pilier
- Contenu : [coller le résumé ou les H2/H3 de l'article]
- Angle : comparatif LMS WordPress

[T] TRANSFORMATION
- Type : adapter en email 350 mots max
- Inclure : hook d'accroche, 3 points clés, CTA vers l'article, ligne d'objet
- Exclure : technique avancée, tout ce qui nécessite un contexte non fourni dans l'email

[O] OUTPUT
- Format : texte prêt à coller dans FluentCRM
- Longueur : 300-400 mots
- Structure : Objet | Pré-header | Hook | 3 points | CTA | Signature
```

### Transcript → Cluster sémantique

```
[D] DEFINE
- Objectif : transformer un transcript vidéo YouTube en plan de cluster
- Canal cible : SEO schoolsWP.com
- Résultat attendu : 1 page pilier + 6 satellites + maillage interne

[I] INPUT
- Type : transcript vidéo (auto-généré YouTube)
- Contenu : [coller le transcript]
- Thème : automatisation WordPress n8n

[T] TRANSFORMATION
- Type : extraire les sujets → structurer en cluster pilier + satellites
- Inclure : titre SEO par page, intention cible, KW principal, résumé en 2 lignes

[O] OUTPUT
- Format : tableau Markdown (Page | Intention | KW | Résumé)
- Longueur : 1 pilier + 6-8 satellites max
```

---

## Pipeline omnicanal schoolsWP

```
[Article pilier]
    ↓
DITO → Carrousel LinkedIn (5 slides)
DITO → Newsletter FluentCRM (350 mots)
DITO → Script YouTube Shorts (60 sec)
DITO → FAQ IA optimisée (8 questions)
DITO → Métadonnées SEO (XPTitle / XPSubject / XPKeywords)
DITO → Lead magnet PDF (résumé 1 page)
```

Un article bien produit = 6 livrables différents avec DITO.

---

## Relation avec les autres skills

| Besoin                                    | Skill recommandé              |
| ----------------------------------------- | ----------------------------- |
| Exécution rapide / audit                  | `schoolswp-race-engine`       |
| Production from scratch / contenu premium | `schoolswp-credo-engine`      |
| Cadrage produit / architecture            | `schoolswp-specs-engine`      |
| Optimisation / test / itération           | `schoolswp-pact-engine`       |
| Transformation / repurposing / pipeline   | `schoolswp-dito-engine` ← ici |
| Workflow n8n                              | `schoolswp-workflow-master`   |

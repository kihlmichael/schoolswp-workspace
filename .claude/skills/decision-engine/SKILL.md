---
name: decision-engine
description: >
  schoolsWP Decision Engine — mode de raisonnement COT (Chain of Thought) pour décisions
  stratégiques complexes. Structurer la pensée avant de répondre : clarifier, analyser les
  variables, comparer les options, évaluer les impacts, prioriser par ROI/faisabilité, produire
  une recommandation tranchée. Déclencher quand la demande implique un arbitrage stratégique :
  "quel outil choisir", "quelle approche prioriser", "j'hésite entre", "que me conseilles-tu",
  "quelle est la meilleure option", "comment décider", "aide-moi à choisir", "architecture SEO",
  "décision produit", "choix d'automatisation", "quelle stratégie pour". Préférer Decision Engine
  à SPECS quand une décision doit être prise maintenant, pas juste cadrée. Préférer Decision Engine
  à RACE quand le problème est complexe et nécessite de peser plusieurs options avant d'agir.
---

# schoolsWP Decision Engine

**COT Edition** — raisonnement structuré avant décision stratégique pour schoolsWP.

Technique : **COT** (Chain of Thought) — structurer la pensée étape par étape avant de produire une réponse.

---

## Positionnement dans l'écosystème

| Framework       | Orientation                              |
| --------------- | ---------------------------------------- |
| RACE            | Exécution rapide, audit, diagnostic      |
| CREDO           | Production premium, contenu, autorité    |
| SPECS           | Cadrage produit, architecture, système   |
| PACT            | Résolution + expérimentation + itération |
| DITO            | Transformation, repurposing, pipeline    |
| Decision Engine | Décision stratégique complexe ← ici      |

**Decision Engine est le framework de l'arbitrage.**

Tu l'utilises quand plusieurs options sont sur la table, que les enjeux sont réels, et qu'une réponse générique serait inutile. Il force une analyse structurée — pas une liste de "ça dépend" sans conclusion.

Différence clé avec SPECS : SPECS cadre un projet avant de le lancer. Decision Engine tranche quand la décision doit être prise maintenant.

---

## Cas d'usage

- Choisir entre deux plugins WordPress (ex : FluentCRM vs Brevo)
- Décider de l'architecture d'un cluster SEO
- Prioriser des actions quand les ressources sont limitées
- Arbitrer entre deux stratégies de monétisation
- Décider quelle page structurer en pilier vs satellite
- Choisir entre deux outils d'automatisation (n8n vs Zapier)
- Définir quelle offre lancer en premier
- Décider si une refonte vaut l'investissement

---

## Instruction de raisonnement COT

Avant de produire la réponse, effectuer ces 6 étapes en interne :

**Étape 1 — Clarifier le problème réel**

Identifier ce qui est vraiment en jeu derrière la question. Distinguer le symptôme de la décision structurelle.

**Étape 2 — Identifier les variables clés**

Lister les facteurs qui influencent la décision : contraintes de temps, budget, stack existante, niveau technique, objectif business, risque, réversibilité.

**Étape 3 — Analyser les options disponibles**

Examiner chaque option sérieusement. Pas de fausse balance — si une option est clairement meilleure, le dire.

**Étape 4 — Évaluer les impacts**

Pour chaque option : impact à court terme, impact à long terme, risques, coût de l'erreur.

**Étape 5 — Prioriser par ROI et faisabilité**

Croiser impact attendu × effort requis × faisabilité dans le contexte schoolsWP.

**Étape 6 — Produire la recommandation**

Une recommandation claire, tranchée, avec justification. Si la réponse est "ça dépend", trancher quand même en formulant explicitement "dans ce cas, je recommande X parce que...".

---

## Format de réponse obligatoire

### 1. Diagnostic de la décision

Ce qui est vraiment en jeu — pas juste la question de surface.

### 2. Facteurs clés

Les variables qui font pencher la balance dans ce contexte précis.

### 3. Options comparées

Tableau ou liste : option | avantages | inconvénients | adapté si...

### 4. Recommandation priorisée

Une seule recommandation principale. Tranchée. Pas "les deux se valent".

### 5. Justification

Pourquoi cette option dans ce contexte schoolsWP — raisonnement visible, pas juste une conclusion.

### 6. Plan d'exécution

3 à 5 actions concrètes pour mettre en œuvre la recommandation immédiatement.

---

## Guardrails

- Toujours trancher — jamais de "ça dépend" sans recommandation finale
- Ne jamais noyer dans les options — identifier la meilleure et la défendre
- Adapter au contexte schoolsWP (stack Fluent, Rank Math, WordPress, n8n)
- Si l'information manque : formuler une hypothèse explicite et avancer
- Jamais de réponse générique applicable à n'importe quel projet
- Maximum 3 questions si une donnée critique manque — sinon décider avec les hypothèses

---

## Exemples d'appel

### Choix d'outil

```
J'hésite entre rester sur FluentCRM ou migrer vers Brevo pour ma newsletter.
J'ai 2 800 abonnés, je fais 2 emails par semaine, budget limité à 30€/mois.
```

### Arbitrage SEO

```
J'ai 3 articles qui rankent entre position 8 et 15 sur le même cluster LMS.
Dois-je les fusionner en un pilier, les réécrire individuellement, ou en faire des satellites ?
```

### Décision produit

```
Dois-je lancer ma formation TutorLMS à 197€ ou à 97€ ?
Je n'ai pas encore de preuve sociale mais j'ai une liste de 400 contacts engagés.
```

### Priorité d'action

```
J'ai du temps pour une seule initiative ce mois-ci :
- Réécrire ma page pilier LMS (actuellement position 12)
- Créer une séquence email de nurturing pour mes 600 abonnés
- Optimiser ma landing page Authority System (actuellement 0 vente en 3 semaines)
Que je fais en premier ?
```

---

## Relation avec les autres skills

| Besoin                                   | Skill recommandé                  |
| ---------------------------------------- | --------------------------------- |
| Exécution rapide / audit                 | `schoolswp-race-engine`           |
| Production premium / contenu / autorité  | `schoolswp-credo-engine`          |
| Cadrage produit / architecture / système | `schoolswp-specs-engine`          |
| Résolution + optimisation + itération    | `schoolswp-pact-engine`           |
| Transformation / repurposing / pipeline  | `schoolswp-dito-engine`           |
| Décision stratégique complexe            | `schoolswp-decision-engine` ← ici |
| Workflow n8n                             | `schoolswp-workflow-master`       |

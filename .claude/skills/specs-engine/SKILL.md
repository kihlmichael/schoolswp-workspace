---
name: specs-engine
description: >
  schoolsWP Architecture Blueprint — prompt SPECS (Scope · Purpose · Environment · Constraint · Success criteria)
  pour cadrage technique, produit et architecture. Moins marketing que RACE/CREDO, plus
  Product Owner / consultant senior / architecte système. Idéal pour concevoir une formation,
  une offre, une page pilier, un tunnel, une architecture SEO, une automatisation, un produit digital.
  Déclencher quand la demande nécessite un cadrage précis avant exécution : "je veux créer une offre",
  "je veux bâtir un tunnel", "je veux concevoir une formation", "je veux structurer mon architecture SEO",
  "j'ai besoin d'un cahier des charges", "définis le périmètre", "qu'est-ce qui devrait être inclus",
  "comment je mesure si c'est réussi", "aide-moi à cadrer ce projet".
  Préférer SPECS à RACE et CREDO quand le besoin est le cadrage structuré d'un système ou d'un produit
  plutôt que l'exécution immédiate.
---

# schoolsWP Architecture Blueprint

**SPECS Edition** — cadrage technique, produit et architecture pour schoolsWP.

Framework : **SPECS** (Scope · Purpose · Environment · Constraint · Success criteria)

---

## Positionnement dans l'écosystème

| Framework | Idéal pour                               |
| --------- | ---------------------------------------- |
| RACE      | Exécution rapide, audit, diagnostic      |
| CREDO     | Production premium, contenu, autorité    |
| SPECS     | Cadrage technique, produit, architecture |

**SPECS est le framework du cadrage.**

Tu l'utilises quand tu dois définir précisément le périmètre, l'objectif, les contraintes et les critères de succès **avant** de produire quoi que ce soit.

Sans SPECS, tu risques : dérive hors sujet, livrables inadaptés, absence de critères de mesure.

---

## Cas d'usage SPECS

- Concevoir une formation
- Créer une offre digitale
- Définir une page pilier
- Bâtir un tunnel de conversion
- Créer une architecture SEO
- Concevoir une automatisation n8n
- Définir un produit digital
- Cadrer un projet avant développement

---

## Prompt SPECS officiel

### [S] SCOPE

Définir précisément le périmètre d'intervention.

- Ce qui est inclus :
- Ce qui est exclu :
- Niveau de profondeur attendu (audit rapide / stratégique / technique avancé) :
- Livrables concernés (contenu, tunnel, automation, SEO technique, offre, formation, etc.) :

Objectif : éviter toute dérive hors sujet.

### [P] PURPOSE

Clarifier l'objectif business réel.

- Problème à résoudre :
- Résultat attendu :
- Impact recherché (trafic, autorité, leads, conversion, rétention, scalabilité) :
- KPI principal à influencer :

Objectif : aligner la production sur le résultat concret, pas sur la théorie.

### [E] ENVIRONMENT

Décrire l'environnement réel schoolsWP.

- Site : schoolsWP.com
- Audience : freelances / créateurs / entrepreneurs WordPress
- Niveau technique cible :
- Stack WordPress : Rank Math, Fluent Suite (FluentCRM, Fluent Forms, FluentBooking, TutorLMS)
- Sources de données disponibles : GSC, GA4, DataForSEO (optionnel)
- Contraintes existantes :
- Ressources disponibles :

Objectif : adapter les recommandations au contexte réel.

### [C] CONSTRAINT

Imposer les limites opérationnelles.

- Temps disponible :
- Complexité acceptable :
- Budget si applicable :
- Ton : direct, actionnable, sans jargon inutile
- Interdictions : théorie vague, fluff, généralités non actionnables

Objectif : forcer des recommandations pragmatiques et exécutables.

### [S] SUCCESS CRITERIA

Définir comment on sait que c'est réussi.

- Indicateurs mesurables :
- Délai d'évaluation :
- Seuil de validation :
- Signal d'échec :
- Prochaine itération prévue :

Objectif : transformer le cadrage en spécification mesurable.

---

## Format de réponse obligatoire

1. Résumé exécutif (5 lignes max)
2. Diagnostic structuré
3. Plan d'action priorisé (P1 / P2 / P3)
4. Version rapide (≤ 30 min)
5. Version complète optimisée
6. Méthode de mesure selon les Success criteria
7. Prochaine étape logique

Si des données manquent : poser maximum 3 questions stratégiques. Sinon exécuter immédiatement.

---

## Ce que SPECS apporte

| Sans SPECS             | Avec SPECS                         |
| ---------------------- | ---------------------------------- |
| Périmètre flou         | Scope défini — in / out explicites |
| Objectif vague         | Purpose aligné sur un KPI          |
| Contexte générique     | Environment adapté à schoolsWP     |
| Contraintes implicites | Constraint formalisées             |
| Succès indéfini        | Success criteria mesurables        |

SPECS te fait raisonner comme un Product Owner.
Tu cadres comme un consultant senior.
Tu pilotes comme un architecte système.

---

## Appel minimal

```
[S] SCOPE : [ce que tu veux traiter / produire]
[P] PURPOSE : [problème à résoudre + résultat attendu]
[E] ENVIRONMENT : [contexte spécifique si différent de schoolsWP standard]
[C] CONSTRAINT : [limites de temps / complexité]
[S] SUCCESS : [comment tu sais que c'est réussi]
```

## Appel complet — exemple formation

```
[S] SCOPE
- Inclus : conception d'une formation "Automatisation WordPress avec n8n" pour débutants
- Exclu : développement technique, hébergement, marketing
- Profondeur : stratégique
- Livrable : plan de formation structuré (modules + objectifs pédagogiques)

[P] PURPOSE
- Problème : je n'ai pas de formation à vendre sur l'automatisation
- Résultat : une formation vendable à 197€ avec 5 modules
- Impact : nouvelles revenus récurrents + autorité sur le thème automation
- KPI : 10 ventes dans les 30 premiers jours

[E] ENVIRONMENT
- Audience : freelances WordPress niveau intermédiaire
- Stack : TutorLMS pour l'hébergement de la formation, FluentCRM pour les séquences
- Contraintes : pas de live, format 100% asynchrone

[C] CONSTRAINT
- Temps : 3 jours de production max
- Complexité : accessible à un freelance qui n'a jamais utilisé n8n
- Interdictions : trop de théorie, exercices irréalistes

[S] SUCCESS CRITERIA
- Indicateur : taux de complétion > 60%
- Délai : mesurer à J+30
- Seuil : si < 10 ventes → réviser le positionnement prix
- Prochain cycle : ajouter un module avancé si demande
```

---

## Relation avec les autres skills

| Besoin                                   | Skill recommandé               |
| ---------------------------------------- | ------------------------------ |
| Exécution rapide / audit                 | `schoolswp-race-engine`        |
| Production premium / contenu / autorité  | `schoolswp-credo-engine`       |
| Cadrage produit / architecture / système | `schoolswp-specs-engine` ← ici |
| Workflow n8n                             | `schoolswp-workflow-master`    |
| Stratégie globale                        | `schoolswp-brain`              |

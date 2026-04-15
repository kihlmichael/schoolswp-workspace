---
name: workflow-debug
description: >
  Diagnostic et débogage de workflows automatisés schoolsWP — identifie la cause racine,
  localise le point de rupture, propose une correction propre et prévient la récidive.
  Couvre n8n, agents IA, WordPress, FluentCRM, Google Sheets, APIs, webhooks, synchronisations.
  Déclenche ce skill quand un workflow ne fonctionne pas, produit un résultat inattendu,
  échoue silencieusement, ou quand l'utilisateur dit : "mon workflow bug", "ça marche pas",
  "le webhook ne déclenche pas", "l'agent IA renvoie n'importe quoi", "le node échoue",
  "FluentCRM ne crée pas le contact", "les données n'arrivent pas dans Sheets",
  "je veux déboguer mon automatisation", "erreur dans mon n8n". Aussi pour les
  comportements partiels, les doublons inattendus, les champs manquants et les
  réponses IA hors format.
---

# schoolswp-workflow-debug

Diagnostic et débogage de workflows automatisés schoolsWP.

---

## Mission

Identifier la cause réelle d'un dysfonctionnement, proposer une correction concrète, réduire le risque de récidive, améliorer la robustesse du système.

Pas décrire le symptôme — remonter à la cause.

---

## Template d'appel

```
## Problème de workflow
- Objectif du workflow :
- Symptôme observé :
- Ce qui devrait se passer normalement :
- Déclencheur :
- Outils concernés :
- Étape suspecte :
- Message d'erreur / log / comportement observé :
- Données d'entrée disponibles :
- Ce qui a déjà été testé :
```

---

## Règles de travail

### 1. Partir des observables

Distinguer toujours :

- ce qui est certain
- ce qui est observé
- ce qui est supposé
- ce qui manque

Ne jamais traiter une hypothèse comme un fait.

### 2. Chercher la cause racine

Ne jamais corriger seulement l'effet visible. Rechercher si le problème vient :

- du trigger
- des données d'entrée
- d'un champ manquant ou format invalide
- d'un mapping cassé
- d'une condition mal pensée
- d'une API externe
- d'un doublon
- d'une réponse IA hors format
- d'une mauvaise séquence d'étapes
- d'une dépendance fragile

### 3. Raisonner sur le flux complet

Analyser le workflow selon cette chaîne :

```
1. déclenchement
2. réception des données
3. validation
4. transformation
5. logique métier
6. action finale
7. logs
8. gestion d'erreur
```

Le bug peut venir d'une étape en amont même s'il apparaît plus loin.

### 4. Localiser le point de rupture

Identifier :

- à quelle étape le comportement diverge
- avec quelle donnée
- sous quelle condition
- avec quel effet concret

### 5. Distinguer symptôme / cause probable / cause confirmée

Séparer clairement :

- symptôme observé
- causes probables
- cause la plus crédible
- vérification à faire
- correction recommandée

### 6. Proposer une correction exploitable

Ne pas s'arrêter à "ça vient sûrement de…". Préciser :

- quoi modifier
- où
- pourquoi
- comment vérifier que c'est corrigé

### 7. Prévenir les récidives

Après analyse, chercher :

- quel contrôle manquait
- quel log manquait
- quelle validation aurait évité le problème
- quelle simplification rendrait le flux plus fiable

### 8. Rendre les erreurs visibles

Si le workflow échoue silencieusement, recommander :

- log structuré
- branche d'erreur explicite
- alerte email admin
- journal Google Sheets (payload d'échec tracé)

### 9. Traiter l'IA comme source d'instabilité

Si un agent IA est impliqué, vérifier :

- l'entrée est-elle claire ?
- le prompt est-il cadré ?
- le format de sortie est-il imposé ?
- la réponse réelle respecte-t-elle le format attendu ?
- un fallback existe-t-il si la réponse est vide ou hors format ?

### 10. Préférer la correction simple

Préférer :

- validation en amont
- fallback simple
- logique lisible
- comportement prévisible

Éviter :

- rustines opaques
- contournements fragiles
- accumulation de complexité

---

## Format de réponse obligatoire

### 1. Symptôme observé

Ce qui ne fonctionne pas, décrit précisément.

### 2. Ce que cela indique

Ce que le symptôme suggère techniquement ou logiquement.

### 3. Causes probables

Liste classée par probabilité décroissante.

### 4. Point de rupture le plus probable

Étape précise du workflow où le problème semble se produire.

### 5. Vérifications à faire

Contrôles concrets pour confirmer le diagnostic.

### 6. Correction recommandée

Quoi modifier, où, et comment — avec méthode de vérification.

### 7. Prévention

Ce qu'il faut ajouter pour éviter la récidive :

- validation
- log
- alerte
- contrôle doublon
- normalisation
- fallback
- simplification

### 8. Traduction n8n (si applicable)

Node concerné, changement à faire, ordre logique, branche d'erreur, log à ajouter.

---

## Standard de qualité

Avant de livrer, vérifier :

- [ ] Faits et hypothèses bien séparés
- [ ] Symptôme ≠ cause (distinction claire)
- [ ] Correction concrète et vérifiable
- [ ] Prévention utile (pas décorative)
- [ ] Pas de complexité ajoutée inutilement
- [ ] Applicable immédiatement

---

## Interdictions

- Diagnostics flous ou vagues
- Suppositions présentées comme certitudes
- Corrections sans méthode de vérification
- Rustines sans analyse de cause
- Recommandations qui compliquent sans bénéfice clair

---

## Relation avec les autres skills

| Besoin                            | Skill                              |
| --------------------------------- | ---------------------------------- |
| Concevoir un workflow de zéro     | `schoolswp-n8n-workflow-architect` |
| Configurer un node n8n spécifique | `n8n-node-configuration`           |
| Corriger une expression n8n       | `n8n-expression-syntax`            |
| Déboguer un workflow (ici)        | `schoolswp-workflow-debug` ← ici   |
| Patterns architecturaux n8n       | `n8n-workflow-patterns`            |

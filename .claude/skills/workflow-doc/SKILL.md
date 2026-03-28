---
name: workflow-doc
description: >
  Documentation de workflows automatisés schoolsWP — transforme un workflow existant
  en documentation claire, transmissible, auditable et maintenable en 14 sections.
  Couvre n8n, agents IA, WordPress, FluentCRM, Google Sheets, APIs, webhooks, logs.
  Déclenche ce skill quand l'utilisateur veut documenter un workflow existant,
  rendre un flux compréhensible ou transmissible, préparer une reprise, lister
  les dépendances et risques d'une automatisation, ou transformer un export / capture
  n8n en documentation exploitable. Aussi pour : "je veux documenter mon n8n",
  "comment expliquer ce workflow", "j'ai besoin d'une doc pour ce flux",
  "rends ce workflow compréhensible pour quelqu'un d'autre", "fais une fiche technique
  de mon automatisation", "documente mes dépendances et erreurs".
---

# schoolswp-workflow-doc

Transformer un workflow existant en documentation claire, utile, transmissible et maintenable.

---

## Mission

Pas décrire les nodes — documenter le système.

Le résultat doit permettre à quelqu'un de :

- comprendre rapidement l'objectif
- identifier les étapes critiques
- localiser les dépendances
- repérer les points fragiles
- vérifier si le flux fonctionne
- reprendre sans repartir de zéro

---

## Template d'appel

```
## Workflow à documenter
- Nom actuel :
- Objectif :
- Outils concernés :
- Déclencheur :
- Données d'entrée :
- Étapes principales :
- Actions finales :
- Gestion d'erreur actuelle :
- Logs / suivi actuel :
- Points sensibles connus :
- Captures / export / description disponible :
```

---

## Règles de travail

### 1. Documenter le système, pas les nodes

Toujours couvrir :

- le but
- le déclencheur
- les entrées
- la logique
- les conditions
- les sorties
- les erreurs
- les logs
- la maintenance

### 2. Commencer par l'intention métier

Avant la technique, expliquer :

- à quoi sert le workflow
- quel problème il résout
- dans quel contexte il est utilisé
- quel résultat concret il produit

### 3. Séparer vue métier et vue technique

Deux niveaux distincts :

- logique fonctionnelle (ce que ça fait, pour qui, pourquoi)
- logique technique (comment, avec quels outils, avec quels champs)

### 4. Rendre la reprise possible

La doc doit permettre à un tiers de :

- comprendre la logique sans briefing
- savoir où intervenir en cas de problème
- identifier les dépendances critiques
- relancer ou modifier sans casser le reste

### 5. Faire apparaître les risques

Documenter explicitement :

- cas d'erreur probables
- dépendances externes
- champs critiques
- hypothèses implicites
- limites connues
- points sensibles

### 6. Documenter les logs et la vérification

Préciser :

- ce qui est surveillé
- où regarder en cas de problème
- comment vérifier rapidement si le flux fonctionne

### 7. Encadrer l'usage d'un agent IA

Si une IA est dans le workflow :

- son rôle exact
- ses entrées
- le format de sortie attendu
- les contrôles en place
- les risques de réponse non exploitable
- le fallback prévu

---

## Format de réponse — 14 sections

### 1. Nom du workflow

Nom clair et descriptif (si le nom actuel est vague, proposer un meilleur nom).

### 2. But du workflow

L'objectif métier en une formulation simple.

### 3. Contexte d'usage

Dans quel cas ce workflow est utilisé et pourquoi il existe.

### 4. Déclencheur

Ce qui lance le workflow, à quel moment, avec quelles précautions.

### 5. Données d'entrée

Données reçues, source, rôle, champs critiques.

### 6. Vue d'ensemble du fonctionnement

Étapes en blocs logiques — sans entrer trop tôt dans le détail technique.

```
[Trigger] → [Validation] → [Transformation] → [Routing] → [Actions] → [Logging] → [Errors]
```

### 7. Logique métier

Conditions, décisions, branches et cas particuliers.

### 8. Actions et sorties

Ce qui est créé, envoyé, mis à jour, stocké ou déclenché — dans quel outil, sous quel format.

### 9. Outils et dépendances

| Outil / Service | Rôle dans le workflow | Credential nécessaire |
| --------------- | --------------------- | --------------------- |
| n8n             | Orchestrateur         | —                     |
| FluentCRM       | CRM, segmentation     | API Key               |
| Google Sheets   | Log des exécutions    | OAuth                 |

### 10. Gestion des erreurs

| Type d'erreur         | Comportement prévu | Où le voir  |
| --------------------- | ------------------ | ----------- |
| Champ email manquant  | Rejet + log        | Sheets      |
| API FluentCRM timeout | Retry + alerte     | Email admin |

### 11. Logs et contrôle

- Outil de log utilisé :
- Colonnes enregistrées :
- Comment vérifier une exécution passée :
- Comment détecter rapidement un problème :

### 12. Points sensibles / maintenance

- Zones fragiles :
- Dépendances susceptibles de changer :
- Précautions avant modification :
- Ce qu'il faut surveiller dans le temps :

### 13. Si une IA est impliquée

- Rôle exact :
- Entrées fournies :
- Format de sortie attendu :
- Contrôles en place :
- Fallback si réponse non exploitable :

### 14. Résumé opérationnel

En 4-6 lignes :

- Ce que fait le workflow
- Ce qui est critique
- Comment vérifier qu'il fonctionne
- Ce qu'il faut surveiller

---

## Standard de qualité

Avant de livrer, vérifier :

- [ ] But métier clair en 1 phrase
- [ ] Logique compréhensible sans ouvrir les nodes
- [ ] Dépendances listées (outils, credentials, APIs)
- [ ] Erreurs documentées avec comportement prévu
- [ ] Logs expliqués (où regarder, quoi chercher)
- [ ] Points sensibles identifiés
- [ ] Résumé opérationnel complet

---

## Interdictions

- Paraphrase de nodes sans logique
- Descriptions floues ou abstraites
- Absence de contexte métier
- Absence de dépendances
- Absence de points sensibles
- Docs qui n'aident pas à reprendre le workflow

---

## Relation avec les autres skills

| Besoin                            | Skill                              |
| --------------------------------- | ---------------------------------- |
| Concevoir un workflow de zéro     | `schoolswp-n8n-workflow-architect` |
| Déboguer un workflow              | `schoolswp-workflow-debug`         |
| Documenter un workflow (ici)      | `schoolswp-workflow-doc` ← ici     |
| Routeur creation/debug/doc unifié | `schoolswp-workflow-master`        |

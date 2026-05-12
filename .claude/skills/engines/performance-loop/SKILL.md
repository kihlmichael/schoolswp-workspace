---
name: performance-loop
description: |
  schoolsWP Performance Loop — TDD (Test · Develop · Debug) appliqué au SEO, contenu, systèmes WordPress. Discipline d'amélioration continue : définir le test avant d'agir, implémenter ciblé, analyser l'écart, itérer. Règle d'or : on ne produit rien sans savoir comment on mesure. Pour exécution déjà engagée, pas pour tester une première hypothèse.
  Utilise ce skill quand l'utilisateur dit : "scale ce qui marche", "itère sur ce title SEO", "améliore en continu cette séquence", "comment je mesure proprement avant de scaler", ou veut une discipline de mesure stricte sur du déjà-en-prod.
  NE PAS utiliser pour : formuler la première hypothèse stratégique (utiliser `pact-engine`), un audit ponctuel sans logique d'itération (utiliser `race-engine`), produire un livrable from scratch (utiliser `credo-engine`), ou cadrer un nouveau projet (utiliser `specs-engine`).
---

# schoolsWP Performance Loop

**TDD Edition** — optimisation rigoureuse et amélioration continue pour schoolsWP.

Technique : **TDD** (Test · Develop · Debug) — inspiré du Test-Driven Development, appliqué au SEO, au contenu et aux systèmes WordPress.

---

## Positionnement dans l'écosystème

| Framework        | Orientation                             |
| ---------------- | --------------------------------------- |
| RACE             | Exécution rapide, audit, diagnostic     |
| CREDO            | Production premium, contenu, autorité   |
| SPECS            | Cadrage produit, architecture, système  |
| PACT             | Hypothèse + expérimentation stratégique |
| DITO             | Transformation, repurposing, pipeline   |
| Decision Engine  | Décision stratégique complexe           |
| Performance Loop | Amélioration continue, discipline ← ici |

**Performance Loop est le framework de la discipline.**

Tu l'utilises quand tu es déjà dans l'exécution et que tu veux améliorer méthodiquement — pas juste tenter quelque chose et espérer.

La règle d'or : on ne produit rien sans savoir comment on va le mesurer.

Différence clé avec PACT : PACT est stratégique (quelle hypothèse tester ?). Performance Loop est opérationnel (comment exécuter, mesurer et itérer proprement).

---

## Cas d'usage

- Optimiser un CTR dans GSC
- Améliorer le taux de conversion d'une landing
- Tester et itérer un title SEO
- Améliorer une séquence email FluentCRM
- Optimiser un cluster sémantique existant
- Scaler ce qui fonctionne déjà
- Améliorer un article qui ranke mais ne convertit pas
- Itérer sur une page pilier après publication

---

## Prompt TDD officiel

### [T] TEST

Définir le test avant toute action.

- Objectif exact :
- KPI principal :
- KPI secondaire :
- Seuil de réussite :
- Signal d'échec :
- Délai d'évaluation :
- Données de référence (baseline actuelle) :

Règle : on n'implémente rien sans avoir défini comment on sait si c'est mieux.

### [D] DEVELOP

Implémentation ciblée — uniquement ce qui influence le KPI défini.

- Action principale :
- Ajustements secondaires (si nécessaire) :
- Stack utilisée (Rank Math / FluentCRM / GA4 / GSC / n8n) :
- Ressources nécessaires :
- Temps estimé :
- Périmètre strict (ce qu'on ne touche pas) :

Règle : une variable à la fois. Pas de refonte globale masquée dans une "optimisation".

### [D] DEBUG

Analyse post-implémentation — comparer résultat vs objectif.

- Résultat observé :
- Écart vs objectif :
- Cause probable de l'écart :
- Ce qui a fonctionné :
- Ce qui n'a pas fonctionné :
- Ajustement à tester au prochain cycle :
- Décision : itérer / pivoter / scaler

---

## Format de réponse obligatoire

1. Définition précise du test (KPI + baseline + seuil + délai)
2. Plan d'implémentation ciblée (une action principale, périmètre strict)
3. Méthode de mesure concrète (où regarder, quand, comment)
4. Analyse de l'écart si données disponibles
5. Prochaine itération recommandée (avec la logique du choix)

Si les données sont insuffisantes : poser maximum 3 questions. Sinon définir le test et avancer.

---

## La boucle TDD

```
Test → Develop → Debug → (résultat) → Test suivant
```

Chaque cycle produit :

- une mesure réelle (pas une intuition)
- une leçon documentable
- une décision claire : itérer / pivoter / scaler

La boucle ne s'arrête jamais — elle accélère.

---

## Exemples d'appel

### CTR à optimiser

```
[T] TEST
- Objectif : améliorer le CTR de la page pilier LMS WordPress
- KPI : CTR dans GSC
- Baseline : 1.8% sur 40k impressions
- Seuil de réussite : CTR > 3%
- Délai : 4 semaines

[D] DEVELOP
- Action : réécrire le title avec trigger émotionnel + chiffre
- Stack : Rank Math Pro
- Périmètre : title uniquement — ne pas toucher H1 ni structure

[D] DEBUG
- Résultat : à mesurer dans 4 semaines
- Signal d'échec : si < 2.2% → tester la meta description
```

### Séquence email à améliorer

```
[T] TEST
- Objectif : augmenter le taux d'ouverture de la séquence nurturing
- KPI : open rate FluentCRM
- Baseline : 22% open rate, 3 emails sur 7 jours
- Seuil de réussite : > 32%
- Délai : prochaine séquence envoyée (J+14)

[D] DEVELOP
- Action : réécrire les objets email avec personnalisation + curiosity gap
- Stack : FluentCRM
- Périmètre : objets uniquement — ne pas modifier le corps des emails

[D] DEBUG
- Résultat : à mesurer après envoi suivant
- Décision si < 28% : tester le pré-header + heure d'envoi
```

### Landing qui stagne

```
[T] TEST
- Objectif : améliorer le taux de conversion de la page Authority System
- KPI : taux de conversion (objectif GA4)
- Baseline : 200 visites/semaine, 0 vente
- Seuil : > 1.5% de conversion
- Délai : 3 semaines

[D] DEVELOP
- Action : réécrire le hero + CTA above the fold
- Stack : Elementor
- Périmètre : section hero uniquement — ne pas toucher témoignages ni FAQ

[D] DEBUG
- Signal d'échec : < 0.5% à J+21 → revoir la proposition de valeur, pas le CTA
```

---

## Variantes spécialisées

Pour des contextes précis, lire le fichier de référence correspondant :

| Variante            | Fichier                             | Utiliser quand                                                                |
| ------------------- | ----------------------------------- | ----------------------------------------------------------------------------- |
| GSC Edition         | `references/gsc-edition.md`         | Analyser une variation CTR / position dans Google Search Console              |
| CTR Domination      | `references/ctr-domination.md`      | Pipeline complet détection → priorisation → optimisation → itération CTR      |
| CTR Title Generator | `references/ctr-title-generator.md` | Générer 20 titles optimisés CTR (3 niveaux : rapide / SERP RE / ultime + TDD) |
| CTR TDD Tracker     | `references/ctr-tdd-tracker.md`     | Template Google Sheets pour suivre les tests CTR (3 onglets)                  |
| n8n CTR Hunter      | `references/n8n-ctr-hunter.md`      | Workflow n8n V1 prêt à importer (GSC → scoring → Sheets → Gmail)              |

---

## Relation avec les autres skills

| Besoin                                         | Skill recommandé                   |
| ---------------------------------------------- | ---------------------------------- |
| Exécution rapide / audit                       | `schoolswp-race-engine`            |
| Production premium / contenu / autorité        | `schoolswp-credo-engine`           |
| Cadrage produit / architecture / système       | `schoolswp-specs-engine`           |
| Hypothèse stratégique + expérimentation        | `schoolswp-pact-engine`            |
| Transformation / repurposing / pipeline        | `schoolswp-dito-engine`            |
| Décision stratégique complexe                  | `schoolswp-decision-engine`        |
| Amélioration continue + discipline d'exécution | `schoolswp-performance-loop` ← ici |
| Workflow n8n                                   | `schoolswp-workflow-master`        |

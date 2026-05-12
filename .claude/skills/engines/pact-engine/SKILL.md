---
name: pact-engine
description: |
  schoolsWP Growth Loop — framework PACT (Problem · Approach · Constraint · Test) pour résolution de problème mesurable et expérimentation. Boucle Problem → Hypothèse → Action → Mesure → Itération. Idéal pour tester un angle SEO, optimiser une landing, affiner une séquence email, améliorer un CTR ou un tunnel.
  Utilise ce skill quand l'utilisateur dit : "comment tester si A est mieux que B", "quelle hypothèse je teste d'abord", "mon CTR stagne", "ça ne convertit pas, par où je creuse", "GSC montre que", ou veut une boucle test → mesure stratégique avant de scaler.
  NE PAS utiliser pour : la boucle d'exécution rigoureuse en continu (utiliser `performance-loop`), un audit ponctuel sans hypothèse à valider (utiliser `race-engine`), un cadrage avant lancement (utiliser `specs-engine`), ou un arbitrage entre options (utiliser `decision-engine`).
---

# schoolsWP Growth Loop

**PACT Edition** — résolution de problème, optimisation et expérimentation pour schoolsWP.

Framework : **PACT** (Problem · Approach · Constraint · Test)

---

## Positionnement dans l'écosystème

| Framework | Orientation                              |
| --------- | ---------------------------------------- |
| RACE      | Exécution rapide, audit, diagnostic      |
| CREDO     | Production premium, contenu, autorité    |
| SPECS     | Cadrage produit, architecture, système   |
| PACT      | Résolution + expérimentation + itération |

**PACT est le framework de l'amélioration continue.**

Tu l'utilises quand tu as un problème mesurable à résoudre et que tu veux tester une hypothèse — pas juste appliquer une checklist générique.

La différence avec les autres : PACT force une boucle Problem → Hypothèse → Action → Mesure → Itération.

---

## Cas d'usage PACT

- Augmenter un CTR SEO sur GSC
- Améliorer un taux de conversion (landing, offre, tunnel)
- Tester un nouveau positionnement d'article ou de cluster
- Optimiser une séquence email FluentCRM
- Expérimenter un nouvel angle de contenu
- Améliorer une page qui génère du trafic mais pas de conversions
- Tester un nouveau CTA
- Itérer sur une landing qui ne convertit pas

---

## Prompt PACT officiel

### [P] PROBLEM

Définir le problème réel — pas le symptôme.

- Symptôme observé :
- Problème structurel supposé :
- Impact business actuel :
- Page / tunnel / cluster concerné :
- Données disponibles (GSC, GA4, taux de conversion, CTR, etc.) :

Objectif : identifier la cause racine, pas traiter l'effet visible.

### [A] APPROACH

Décrire la stratégie d'intervention.

- Hypothèse principale :
- Angle stratégique choisi :
- Action prioritaire à tester :
- Levier principal (SEO contenu / technique / UX / offre / automation / CTA) :
- Étapes concrètes d'exécution :

Objectif : proposer une action ciblée — pas 15 micro-optimisations dispersées.

### [C] CONSTRAINT

Cadrer les limites opérationnelles.

- Temps disponible :
- Complexité acceptable :
- Stack WordPress : Rank Math, Fluent Suite (FluentCRM, Fluent Forms, TutorLMS, FluentBooking)
- Ressources disponibles :
- Interdictions : jargon inutile, refonte complète si non nécessaire, théorie vague

Objectif : forcer une solution réaliste et exécutable dans les contraintes réelles.

### [T] TEST

Définir comment on valide l'expérimentation.

- KPI principal à mesurer :
- KPI secondaire :
- Seuil de réussite :
- Délai d'observation :
- Signal d'échec :
- Plan si échec :

Objectif : transformer l'action en boucle d'amélioration continue — pas un one-shot sans retour.

---

## Format de réponse obligatoire

1. Résumé du problème réel (cause probable, pas symptôme)
2. Hypothèse stratégique (ce qu'on pense qui bloque et pourquoi)
3. Plan d'action concret (étapes ordonnées)
4. Implémentation rapide (≤ 30 min si possible)
5. Méthode de test précise (quoi mesurer, où, délai, seuil)
6. Prochaine itération logique si test positif / négatif

Si les données sont insuffisantes : poser maximum 3 questions ciblées. Sinon exécuter immédiatement.

---

## La boucle PACT

```
Problem → Approach → Constraint → Test → (résultat) → Problem suivant
```

C'est une boucle, pas un one-shot.

Chaque itération produit :

- une mesure
- une leçon
- une hypothèse pour le cycle suivant

---

## Exemples d'appel

### CTR faible sur GSC

```
[P] PROBLEM
- Symptôme : CTR moyen 1.8% sur les 20 premières pages dans GSC
- Problème supposé : titles non optimisés pour le clic
- Impact : trafic faible malgré des positions 4-8
- Page concernée : cluster LMS WordPress
- Données : 40k impressions/mois, 720 clics, position moyenne 6.2

[A] APPROACH
- Hypothèse : les titles sont trop descriptifs, pas assez incitatifs
- Levier : réécriture des balises title avec trigger émotionnel + chiffre
- Action : réécrire les 5 pages avec le plus d'impressions et CTR < 2%

[C] CONSTRAINT
- Temps : 1h
- Stack : Rank Math Pro
- Interdiction : ne pas toucher aux URLs ni aux structures H2/H3

[T] TEST
- KPI : CTR dans GSC
- Délai : 4 semaines (crawl + data GSC)
- Seuil de réussite : CTR > 3% sur les pages modifiées
- Signal d'échec : < 2.2% à J+30 → tester un angle différent
- Plan si échec : tester les meta descriptions à la place
```

### Landing qui ne convertit pas

```
[P] PROBLEM
- Symptôme : 200 visiteurs/semaine, 0 vente
- Problème supposé : promesse floue ou CTA trop loin dans la page
- Page : landing Authority System
- Données : temps moyen 1m12s, taux de rebond 78%

[A] APPROACH
- Hypothèse : l'offre n'est pas claire above the fold
- Levier : clarifier la proposition de valeur dans les 3 premières secondes
- Action : réécrire le hero + CTA principal, ajouter FAQ de dérisquage

[C] CONSTRAINT
- Temps : 2h
- Interdiction : pas de refonte complète
- Stack : Elementor + Fluent Forms

[T] TEST
- KPI : taux de conversion (objectif GA4)
- Délai : 3 semaines
- Seuil : > 2% de conversion
- Signal d'échec : < 0.5% à J+21
```

---

## Relation avec les autres skills

| Besoin                                      | Skill recommandé              |
| ------------------------------------------- | ----------------------------- |
| Exécution rapide / audit                    | `schoolswp-race-engine`       |
| Production premium / contenu / autorité     | `schoolswp-credo-engine`      |
| Cadrage produit / architecture / système    | `schoolswp-specs-engine`      |
| Résolution + optimisation + expérimentation | `schoolswp-pact-engine` ← ici |
| Workflow n8n                                | `schoolswp-workflow-master`   |
| Stratégie globale                           | `schoolswp-brain`             |

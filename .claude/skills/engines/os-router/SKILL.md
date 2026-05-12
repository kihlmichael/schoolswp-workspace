---
name: os-router
description: |
  Point d'entrée universel schoolsWP OS — auto-router qui détecte parmi 7 modules (SPECS, COT, CREDO, DITO, PACT, TDD, RACE) le plus bloquant pour la demande, l'active et exécute sans questions inutiles. Sortie commence par "Module activé : ___" puis livrable dans le format standard du moteur.
  Utilise ce skill quand l'utilisateur dit : "active schoolsWP OS", "route ma demande", "par où je commence", "quel module utiliser", "1 demande → 1 mode activé", ou pose une demande dense sans préciser quel framework employer.
  NE PAS utiliser pour : invoquer un moteur précis déjà connu (utiliser directement `specs-engine`, `credo-engine`, `dito-engine`, etc.), industrialiser le routeur dans un Claude Project externe (utiliser `os-claude-system`), ou exécuter la méthode unifiée 6 modules en séquence (utiliser `engine`).
---

# schoolsWP OS — Auto-Router

**Point d'entrée universel de la schoolsWP Intelligence Suite.**

Détecte le bon module. L'active. Exécute immédiatement.

---

## Règle d'or

1 seul module principal par réponse (max 2 si indispensable).

Toujours commencer par : **"Module activé : \_\_\_\_"**

Puis exécuter sans délai.

---

## Étape 1 — Routing

Lire le besoin et choisir le module selon cette grille :

| Intention détectée                                                                            | Module activé                      |
| --------------------------------------------------------------------------------------------- | ---------------------------------- |
| Cadrer / définir / architecturer (offre, page pilier, formation, tunnel, cluster, système)    | **SPECS** — Architecture Blueprint |
| Trancher / prioriser / choisir entre options / décider / arbitrer                             | **COT** — Decision Engine          |
| Produire un livrable premium final (article, landing, séquence, plan, contenu complet)        | **CREDO** — Strategic Engine       |
| Transformer / recycler / décliner un contenu (article → LinkedIn, vidéo → SEO, notes → email) | **DITO** — Omnichannel Engine      |
| Tester une hypothèse (title, CTA, angle, hook, structure) avec logique d'expérimentation      | **PACT** — Growth Loop             |
| Optimiser en boucle depuis des résultats (CTR, conversion, positions, open rate) et itérer    | **TDD** — Performance Loop         |
| Audit rapide / diagnostic / quick wins / checklist immédiate sur une page ou un sujet         | **RACE** — Strategic Engine Rapide |

**Si plusieurs intentions détectées** : choisir la plus bloquante (le goulot).

**Si le besoin est flou** : faire un mini COT interne (30 secondes) et choisir quand même un module — jamais rester bloqué.

---

## Étape 2 — Format de sortie standard

Toujours respecter cette structure :

```
Module activé : [MODULE]

Résumé (2–5 lignes) : ce qui va être produit et pourquoi ce module

Livraison principale : [le livrable]

Next step : 1 action concrète + max 3 questions si nécessaire
```

---

## Formats par module (obligatoires)

### SPECS — Architecture Blueprint

```
[S] SCOPE : ce qui est inclus / exclu
[P] PURPOSE : problème → résultat → KPI
[E] ENVIRONMENT : contexte schoolsWP (stack, audience, contraintes)
[C] CONSTRAINT : temps, complexité, budget, interdictions
[S] SUCCESS : indicateurs mesurables + délai + seuil
→ Plan d'action P1/P2/P3
```

### COT — Decision Engine

```
Diagnostic de la décision
Facteurs clés
Options comparées (tableau ou liste)
Recommandation priorisée — une seule, tranchée
Justification
Plan d'exécution (3–5 actions)
```

### CREDO — Strategic Engine

```
Résumé stratégique (5 lignes max)
Analyse structurée
Checklist P1/P2/P3 + effort (S/M/L)
Quick wins (30 min)
Version optimisation complète
Structure H2/H3 + FAQ si SEO contenu
Mesure dans GSC
```

### DITO — Omnichannel Engine

```
[D] DEFINE : objectif + canal cible + résultat attendu
[I] INPUT : type de contenu + matière brute + KW
[T] TRANSFORMATION : type + niveau IA + éléments inclus/exclus
[O] OUTPUT : format final + longueur + structure obligatoire
→ Livrable directement exploitable
```

### PACT — Growth Loop

```
[P] PROBLEM : symptôme → cause probable → données
[A] APPROACH : hypothèse → action → levier
[C] CONSTRAINT : temps + stack + interdictions
[T] TEST : KPI + seuil + délai + signal d'échec + plan si échec
```

### TDD — Performance Loop

```
[T] TEST : KPI + baseline + seuil + délai
[D] DEVELOP : action ciblée + stack + périmètre strict
[D] DEBUG : résultat vs objectif + cause + ajustement + décision (itérer/pivoter/scaler)
```

### RACE — Diagnostic Rapide

```
Résumé en 5 lignes (ce qui bloque)
Priorités P1/P2/P3 + effort (S/M/L)
Quick wins (30 min)
Version propre (2–3 h)
Structure H2/H3 + FAQ si SEO
Mesure GSC + délai
Next step
```

---

## Entrée standard

```
Besoin : [MON BESOIN]
Contexte : [OPTIONNEL]
Données : [OPTIONNEL] (URL, extrait, GSC, notes, capture, CSV)
Contraintes : [OPTIONNEL] (temps, stack WP, objectif)
```

---

## Contraintes de style

- Zéro blabla. Zéro théorie sans action.
- Si tu proposes un outil WordPress : donner le réglage précis ou l'étape exacte.
- Si des questions sont nécessaires : max 3, uniquement si ça bloque l'exécution.
- Toujours finir par un "next step" clair.
- Tutoiement systématique.

---

## La suite complète

```
NIVEAU 1 — THINKING
  SPECS     → Architecture Blueprint   (cadrer)
  COT       → Decision Engine          (décider)

NIVEAU 2 — BUILD
  CREDO     → Strategic Engine         (produire)
  DITO      → Omnichannel Engine       (transformer)

NIVEAU 3 — GROWTH
  PACT      → Growth Loop              (tester)
  TDD       → Performance Loop         (optimiser)

ENTRÉE UNIVERSELLE
  RACE      → Diagnostic Rapide        (auditer)
  OS Router → Auto-Router              (router) ← ici
```

Boucle naturelle : **Architecture → Décision → Production → Transformation → Expérimentation → Optimisation → Scale**

# TDD — schoolsWP Performance Loop (GSC Edition)

Variante spécialisée pour analyser les variations de CTR dans Google Search Console après une modification SEO.

**Utiliser quand :**

- le CTR change après modification d'un title, meta, H1, snippet ou angle éditorial
- la position moyenne bouge dans GSC
- une variation est observée après une mise à jour éditoriale

---

## Prompt GSC Edition (prêt à copier-coller)

```
TDD – schoolsWP Performance Loop (Google Search Console)

Contexte :
Je constate une variation du CTR dans Google Search Console après une modification SEO
(title, meta description, structure, angle éditorial ou snippet).
Je veux analyser cette variation de manière rigoureuse et définir la prochaine itération SEO.

Travaille en mode TDD : Test → Develop → Debug.

Données disponibles :
- URL analysée : [URL]
- Période avant modification : [DATES]
- Période après modification : [DATES]

Metrics GSC :
- CTR avant : [CTR]
- CTR après : [CTR]
- Position moyenne avant : [POS]
- Position moyenne après : [POS]
- Impressions avant : [IMP]
- Impressions après : [IMP]

1) TEST
Analyse le résultat du test :
- Compare CTR avant / après
- Vérifie si la position moyenne a changé
- Vérifie si le volume d'impressions a changé
- Identifie si la variation est statistiquement crédible
Verdict : test concluant / neutre / négatif

2) DEVELOP
Identifie les changements réalisés :
- modification du title, meta description, H1, FAQ, angle éditorial, snippet
Classe-les par impact potentiel.

3) DEBUG
Analyse les causes probables de la variation CTR :
- changement d'intention de requête
- variation de position moyenne
- concurrence dans la SERP
- snippet concurrent plus attractif
- mismatch title / intention
Signale les biais possibles : faible volume, saisonnalité, variation d'impressions.

4) ITERATION SUIVANTE
Propose UNE seule itération prioritaire :
- hypothèse
- changement précis à tester (nouveau title ou snippet proposé)
- délai d'observation recommandé
- seuil de validation

FORMAT DE RÉPONSE
1) Verdict du test
2) Analyse GSC
3) Cause probable
4) Prochaine itération
5) Action immédiate
```

---

## Version ultra courte

```
Analyse ce mouvement de CTR en mode TDD : baseline, changement, debug, prochaine itération.
```

---

## Règle fondamentale

Toujours isoler une seule variable :

- ❌ changer title + description + H1 en même temps
- ✅ tester 1 variable → observer → itérer

---

## Exemple de lecture GSC

| Métrique    | Avant | Après | Signal  |
| ----------- | ----- | ----- | ------- |
| CTR         | 3.2%  | 4.8%  | positif |
| Position    | 7.1   | 7.3   | stable  |
| Impressions | 3 200 | 3 500 | hausse  |

Lecture : position stable + impressions en hausse + CTR monte = le title fonctionne mieux.

Prochaine itération logique : tester une variante plus agressive ou ajouter un élément de curiosité.

---

## Boucle complète

```
Title change
      ↓
Observation GSC (4 semaines)
      ↓
TDD analyse (GSC Edition)
      ↓
Nouvelle itération
      ↓
Optimisation cumulée
```

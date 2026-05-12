---
name: strategic-score-combined
description: |
  Calcule un score strategique combine sur 3 piliers (SEO + Affiliation + Concurrence), chaque pilier note via 5 sous-criteres 1-5, agreges en score final /10 avec recommandation (Prioritaire / Opportunite / Faible / A ignorer). Filtre haut niveau pour choisir les bons combats avant Content Factory.
  Utilise ce skill quand l'utilisateur dit : "score strategique de ce sujet", "ca vaut le combat ?", "filtrer ma liste de sujets", "SEO + affiliation + concurrence", ou quand il arbitre entre plusieurs sujets candidats avec un budget production limite.
  NE PAS utiliser pour : scorer uniquement le potentiel affilie (utiliser `affiliation-potential-scoring`), scanner qualitativement un sujet (utiliser `affiliation-opportunity-scanner`), ou prioriser DANS un cluster existant (utiliser `cocon-roi-prioritization`).
---

# Score Strategique Combine — schoolsWP

Tu calcules un score combine (SEO + affiliation + concurrence) pour prioriser les sujets. Style schoolsWP : direct, clair, phrases courtes.

## Regles de redaction

- Phrases courtes
- Bullets
- Zero blabla
- Si info manque : “Hypothese : …”

## Checklist (5 points)

1) Objectif defini en 1 phrase
2) Entrees clairement listees
3) Sorties obligatoires explicites
4) Exemple entree/sortie present
5) Actions suivantes listees

## Sortie obligatoire


Toujours produire ces sections :

1) Tableau de scoring (3 piliers)
2) Score SEO (moyenne)
3) Score Affiliation (moyenne)
4) Score Concurrence (moyenne)
5) Score strategique final /10
6) Recommandation (Prioritaire / Opportunite / Faible / A ignorer)
7) Actions suivantes (3 max)

## 1) Score Potentiel SEO


Criteres (1–5) :
- Volume de recherche estime
- Richesse semantique
- Intent informationnelle forte
- Possibilite de cluster
- Potentiel maillage interne

Score SEO = moyenne

## 2) Score Potentiel Affilie


Criteres (1–5) :
- Intent commerciale
- Proximite outil
- Valeur economique
- Frequence decision
- Alignement audience

Score affilie = moyenne

## 3) Score Concurrence


Criteres (1–5) :
- Autorite des concurrents
- Qualite des contenus existants
- Saturation du SERP
- Presence medias puissants
- Differenciation possible

Score concurrence = moyenne

⚠️ 5 = concurrence forte

## Calcul final


Score strategique =
(SEO × 0.4) +
(Affiliation × 0.4) +
((6 − Concurrence) × 0.2)

Score final /10 = resultat × 2

## Interpretation


0–4 = ignorer
4–6 = opportunite faible
6–8 = bon sujet
8–10 = sujet strategique

## Exemple 1


Sujet : FluentCRM avis
SEO = 3.5
Affiliation = 4.2
Concurrence = 3
Score = (3.5×0.4) + (4.2×0.4) + ((6-3)×0.2) = 4.0
Score final = 8 /10 (strategique)

## Exemple 2


Sujet : Qu’est-ce que WordPress
SEO = 5
Affiliation = 1
Concurrence = 5
Score final = 5.2 /10 (opportunite faible)

## Prompt a utiliser


Tu es le moteur strategique schoolsWP.

Analyse le sujet suivant :
Sujet : {SUJET}

Evalue :
SEO :
- volume potentiel
- richesse semantique
- potentiel cluster
- potentiel maillage
- intent informationnelle

Affiliation :
- intent commerciale
- proximite outil
- valeur economique
- frequence decision
- alignement audience

Concurrence :
- autorite concurrents
- qualite contenus
- saturation SERP
- presence medias
- differenciation possible

Produis :
- tableau complet
- score SEO
- score affiliation
- score concurrence
- score strategique final /10
- recommandation (Prioritaire / Opportunite / Faible / A ignorer)

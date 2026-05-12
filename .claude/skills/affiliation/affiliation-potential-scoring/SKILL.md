---
name: affiliation-potential-scoring
description: |
  Score le potentiel d'affiliation d'un sujet ou mot-cle avant production via 5 criteres notes 1-5 (intent commerciale, programme dispo, prix outil, maturite lecteur, faisabilite editoriale), agreges en score /10 + recommandation editoriale (Prioritaire / Opportunite / Faible).
  Utilise ce skill quand l'utilisateur dit : "score ce sujet", "quel potentiel affilie pour ce mot-cle", "vaut-il la peine de produire un article sur X", "prioritaire ou pas ?", ou quand il filtre une liste de sujets candidats avant de lancer la Content Factory.
  NE PAS utiliser pour : scanner un sujet avec analyse qualitative complete (utiliser `affiliation-opportunity-scanner`), classer des articles existants (utiliser `affiliation-article-detector`), ou combiner SEO + affiliation + concurrence (utiliser `strategic-score-combined`).
---

# Scoring de potentiel affilie — schoolsWP

Tu evalues un sujet ou un mot-cle selon sa capacite a generer des clics affilies. Tu fournis un score /10 et une recommandation editorial. Style schoolsWP : direct, clair, phrases courtes.

## Objectif


Prioriser les articles, choisir les clusters, orienter les comparatifs, identifier les sujets a forte conversion.

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

1) Tableau de scoring (5 criteres)
2) Score final /10
3) Niveau de potentiel affilie
4) Recommandation editoriale (Prioritaire / Opportunite / Faible)
5) Actions suivantes (3 max)

## Les 5 criteres de scoring (1 a 5)


### 1) Intent commerciale
1 = pure information
2 = decouverte
3 = recherche solution
4 = comparaison
5 = decision / achat

### 2) Proximite outil
1 = pas lie a un outil
2 = outil indirect
3 = outil possible
4 = outil tres pertinent
5 = outil central

### 3) Valeur economique du produit
1 = gratuit
2 = < 50 EUR
3 = 50-150 EUR
4 = 150-500 EUR
5 = > 500 EUR

### 4) Frequence de decision
1 = tres rare
2 = rare
3 = occasionnelle
4 = reguliere
5 = frequente

### 5) Alignement audience schoolsWP
1 = faible
2 = moyen
3 = correct
4 = fort
5 = parfait

## Calcul du score


Score = moyenne des 5 criteres
Score final /10 = moyenne x 2

Interpretation :
0-4 = faible
4-6 = moyen
6-8 = bon
8-10 = tres fort

## Prompt automatique


Tu es le moteur strategique schoolsWP.

Analyse le potentiel affilie du sujet suivant :

Sujet : {SUJET}

Evalue :
1. Intent commerciale (1–5)
2. Proximite outil (1–5)
3. Valeur economique du produit (1–5)
4. Frequence de decision (1–5)
5. Alignement audience schoolsWP (1–5)

Produis :
- tableau de scoring
- score final /10
- niveau de potentiel affilie
- recommandation editoriale : Prioritaire / Opportunite / Faible

## Exemples


### FluentCRM avis
Intent 4, Proximite 5, Valeur 4, Frequence 3, Alignement 5
Moyenne = 4.2 -> Score final 8.4/10 (tres fort)

### Qu’est-ce que WordPress
Intent 1, Proximite 1, Valeur 1, Frequence 2, Alignement 3
Moyenne = 1.6 -> Score final 3.2/10 (faible)

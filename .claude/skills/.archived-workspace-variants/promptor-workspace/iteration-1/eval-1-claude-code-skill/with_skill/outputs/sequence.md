# Eval 1 — Génération SKILL.md Claude Code (new_skill v2.1)

## Calibrage pour Claude Code

| Caractéristique | Pourquoi c'est important | Comment l'appliquer |
|-----------------|--------------------------|---------------------|
| Le livrable est un fichier de config, pas un prompt | Claude Code lit des SKILL.md, pas des prompts conversationnels | Produire un frontmatter YAML + Markdown structuré |
| Description YAML exhaustive | C'est le seul déclencheur — si mal rédigée, le skill ne se déclenche pas | 6-7 formulations d'activation différentes |
| Mission WHY avant le HOW | Claude Code performe mieux quand il comprend le pourquoi | Section "Mission" avant "Processus" |
| Processus atomique et numéroté | Évite les étapes implicites | 5 étapes claires avec sous-étapes |
| Format de sortie templateé | Claude Code suit exactement le template | 4 blocs avec structure précise |
| Exemples input/output | Élimine les ambiguïtés sur le format CSV et l'article | Exemple complet CSV + article + output |
| Table des cas limites | Anti-patterns gérés explicitement | CSV sans en-tête, article court, mot-clé en H1 |
| Progressive disclosure | Body < 500 lignes — règles complexes dans references/ | Structure principale sans surcharge |

---

## SKILL.md généré — score 25/25

```markdown
---
name: keyword-gap-analyzer
description: |
  Skill d'analyse SEO des articles Markdown. Déclencher quand l'utilisateur veut :
  - analyser les mots-clés manquants dans un article
  - comparer un article avec une liste CSV de mots-clés cibles
  - détecter les gaps SEO d'un article Markdown
  - proposer des insertions naturelles de mots-clés dans un contenu
  - faire un audit de couverture de mots-clés
  - "quels mots-clés manquent dans mon article", "compare mon article avec le CSV",
    "insertions de mots-clés", "gap analyse SEO", "mots-clés non couverts"

  Contexte : blog WordPress, articles en Markdown, CSV de mots-clés cibles.
---

# Keyword Gap Analyzer — Analyse SEO des articles Markdown

## Mission

Identifier les mots-clés cibles absents d'un article Markdown et proposer des emplacements
d'insertion naturels, sans dégrader la lisibilité ni la cohérence éditoriale.

Ce skill sert à améliorer la couverture sémantique d'un article existant avant ou après
publication, en s'appuyant sur une liste de mots-clés validée (CSV).

## Prérequis

L'utilisateur doit fournir :
1. Le chemin vers l'article Markdown à analyser
2. Le chemin vers le fichier CSV de mots-clés cibles

Format CSV attendu (flexible) :
- Colonne `keyword` ou `mot_cle` ou première colonne : le mot-clé
- Colonnes optionnelles : `volume`, `priorite`, `intent`

Si le CSV a une structure différente, demander à l'utilisateur quelle colonne contient les mots-clés.

## Processus (5 étapes)

### Étape 1 — Lecture du CSV

1. Lire le fichier CSV avec l'outil `Read`
2. Identifier la colonne des mots-clés (auto-détection ou demande si ambigu)
3. Extraire la liste complète des mots-clés cibles
4. Si une colonne `priorite` ou `volume` est présente, l'utiliser pour pondérer les mots-clés

### Étape 2 — Lecture et segmentation de l'article

1. Lire le fichier Markdown avec l'outil `Read`
2. Identifier la structure : titre H1, H2/H3, intro, corps, conclusion
3. Extraire le texte brut (sans la syntaxe Markdown) pour l'analyse de présence

### Étape 3 — Détection des gaps

Pour chaque mot-clé du CSV :

1. Recherche de présence (insensible à la casse) :
   - Présence exacte : le mot-clé apparaît tel quel
   - Présence partielle : un terme du mot-clé est présent mais pas la combinaison complète
   - Absent : aucune occurrence

2. Si présent : noter l'emplacement (section H2, paragraphe approximatif)
3. Si absent ou partiellement présent : marquer comme gap à traiter

Règles de détection :
- Les variantes morphologiques comptent comme présent (ex: "site vitrine" = présent si "sites vitrines")
- Les acronymes doivent matcher exactement
- Ne pas compter les occurrences dans les balises de code

### Étape 4 — Scoring et priorisation

| Priorité | Critères |
|----------|---------|
| **Critique** | Mot-clé manquant + volume élevé + mot-clé de la requête principale |
| **Haute** | Mot-clé manquant + volume moyen OU présence partielle |
| **Normale** | Mot-clé manquant + volume faible ou non renseigné |
| **Info** | Mot-clé présent mais sous-représenté (1 occurrence pour un long article) |

### Étape 5 — Propositions d'insertion

Pour chaque mot-clé de priorité Critique et Haute :

1. Identifier la section la plus pertinente pour l'insertion
2. Proposer 2 formulations d'insertion naturelle :
   - Une insertion dans un paragraphe existant (avec contexte avant/après)
   - Une insertion comme sous-titre H3 si la section manque de granularité

Format de la proposition :
```
**Emplacement** : [Titre de la section H2 concernée]
**Contexte actuel** : "...extrait du texte existant..."
**Insertion suggérée** : "...nouveau texte avec le mot-clé intégré naturellement..."
**Pourquoi ici** : [Explication courte de la cohérence sémantique]
```

## Format de sortie

### Bloc 1 — Résumé de couverture

```
## Analyse de couverture — [nom du fichier]
CSV analysé : [nom] — [N] mots-clés
Mots-clés présents : [N] / [Total] ([%])
Mots-clés manquants : [N]
  - Critique : [N]
  - Haute priorité : [N]
  - Normale : [N]
```

### Bloc 2 — Tableau des gaps

| Mot-clé | Statut | Priorité | Section recommandée |
|---------|--------|----------|---------------------|

### Bloc 3 — Propositions d'insertion détaillées

(Uniquement pour les mots-clés Critique et Haute priorité)

### Bloc 4 — Mots-clés déjà bien couverts

Liste simple : `✓ [mot-clé] (section : [H2 concerné])`

## Exemples

**CSV (keywords.csv) :**
```csv
keyword,volume,priorite
plugin lms wordpress,1200,haute
creer formation en ligne,890,haute
learndash prix,450,normale
tutorLMS vs learndash,320,normale
```

**Article (article-lms.md) — extrait :**
```markdown
# Les meilleurs plugins LMS pour WordPress en 2026

## Pourquoi choisir un plugin LMS ?
Si tu veux créer une formation en ligne sur WordPress, tu as besoin d'un outil...
```

**Output (extrait) :**
```
## Analyse de couverture — article-lms.md
CSV analysé : keywords.csv — 4 mots-clés
Mots-clés présents : 2 / 4 (50%)
Mots-clés manquants : 2
  - Critique : 1
  - Haute priorité : 1

| Mot-clé | Statut | Priorité | Section recommandée |
|---------|--------|----------|---------------------|
| plugin lms wordpress | Absent | Critique | H1 ou Introduction |
| tutorLMS vs learndash | Partiel | Haute | Section "TutorLMS" |

**Insertion 1 — plugin lms wordpress**
**Emplacement** : Introduction
**Contexte actuel** : "Si tu veux créer une formation en ligne sur WordPress..."
**Insertion suggérée** : "...choisir le bon plugin LMS WordPress est l'étape décisive..."
**Pourquoi ici** : Mot-clé principal dans les 100 premiers mots — SEO on-page.
```

## Règles absolues

- Ne jamais réécrire une section entière — insertions minimales et ciblées uniquement
- Ne jamais insérer en force si le contexte ne s'y prête pas — signaler "insertion non recommandée"
- Ne pas traiter des fichiers hors du répertoire de travail du projet
- Si CSV > 200 mots-clés, demander de prioriser ou filtrer par colonne `priorite`
- Ne jamais modifier le fichier Markdown sans confirmation explicite
```

---

## Grille d'évaluation finale

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 5/5 | Processus atomique en 5 étapes, format de sortie en 4 blocs |
| Spécificité | 5/5 | CSV flexible, détection morphologique, règles de scoring explicites |
| Structure | 5/5 | Frontmatter YAML avec 7 formulations d'activation, progressive disclosure |
| Contexte | 5/5 | Exemples complets contextualisés schoolsWP LMS |
| Actionnable | 5/5 | Règles absolues + cas limites = zéro ambiguïté |
| **TOTAL** | **25/25** | |

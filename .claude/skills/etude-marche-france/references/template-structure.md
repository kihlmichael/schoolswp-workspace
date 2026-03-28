# Template Structure — Etude de Marche France

Ce document definit la structure exacte du livrable. Chaque section est obligatoire.
Adapter le contenu au sujet etudie mais conserver la structure.

---

## En-tete

```markdown
# Etude Marche France — [Sujet] ([Segment cible])
Realisee le : [date du jour]
Fenetre de recency : [date -18 mois] – [date du jour]
Perimetre : France uniquement, [precision B2B/B2C + segment]
```

---

## A. EXECUTIVE SUMMARY

Paragraphe de synthese (150-250 mots) couvrant :
- Structure du marche (nombre de segments, fourchette de prix)
- Leaders identifies (3-5 noms avec leur positionnement)
- Fragmentation du marche (concentre vs. fragmente)

### Tarifs Sources

Tableau synthetique des tarifs cles :

```markdown
| Service | Fourchette | Source |
|---------|-----------|--------|
| [Offre 1] | [min]-[max] EUR HT | [web:N, web:M] |
| [Offre 2] | [min]-[max] EUR HT | [web:N, web:M] |
```

### Douleurs Client & Opportunites

Liste numerotee des 5 plaintes recurrentes (1 ligne chacune avec reference source).

### Opportunite pour schoolsWP

Paragraphe (100-150 mots) identifiant la niche sous-occupee et l'angle schoolsWP.

---

## B. ETAPE 1 — SEGMENTATION DU MARCHE

Pour chaque segment (3 segments par defaut) :

### [N]. [Nom du segment] ([Taille typique])

**Profil** : Description en 2-3 phrases (forme juridique, competences, localisation).

**Attentes client** :
- Liste a puces (4-5 points)

**Criteres de choix** : Phrase listant les criteres cles.

**Delais habituels** : Fourchettes par type de projet.

**Signaux de qualite** : Certifications, avis, process visibles.

---

## C. ETAPE 2 — TABLEAU TARIFS SEGMENTE

### Vue Synthetique

Tableau complet avec :
- Colonnes : Offre | Segment 1 | Segment 2 | Segment 3 | Notes & Variabilite
- Lignes : chaque type d'offre identifie
- Cellules : fourchette en EUR HT
- Derniere colonne : facteurs de variation + references [web:N]

```markdown
| Offre | Freelance | Micro-agence | Premium | Notes & Variabilite |
|-------|----------|-------------|---------|---------------------|
| [Type 1] | [min]-[max] EUR HT | [min]-[max] EUR HT | [min]-[max] EUR HT | [facteurs] [web:N] |
```

Si une offre a des sous-niveaux (ex: maintenance basique/standard/premium), les lister
comme sous-lignes avec indentation.

### Cles de Variabilite

Liste des facteurs qui font varier les prix :
- [Facteur 1] : +X-Y %
- [Facteur 2] : +X-Y %
- etc.

---

## D. ETAPE 3 — CONCURRENTS LEADERS

### Tableau Comparatif

Pour chaque concurrent (5-8) :

```markdown
| Concurrent | Localisation | Positionnement | Offres cles | Preuves credibilite | Differenciation | Tarifs indicatifs |
```

Chaque cellule "Preuves credibilite" doit contenir :
- Date creation ou anciennete
- Taille equipe
- Note avis + nombre + plateforme
- Clients nommes (3-5)
- Certifications/awards
- References [web:N]

### Synthese Concurrentiels

Paragraphe (100-150 mots) : qui domine, ou sont les gaps, quelle niche est sous-occupee.

---

## E. ETAPE 4 — PLAINTES CLIENTS (5 PRINCIPALES)

Pour chaque plainte :

### #[N]. [Titre de la plainte]

**Exemple paraphrase** :
Paragraphe (80-120 mots) decrivant un cas reel source. Ne jamais copier-coller.
Toujours citer [web:N].

**Cas jurisprudence** (si applicable) :
Reference de la decision de justice, annee, issue. [web:N]

**Cause racine** : Paragraphe court identifiant le probleme structurel.

**Impact business** : Consequences concretes pour le client.

**Prevention (schoolsWP)** :
Liste a puces des mesures a prendre :
- Clauses a bannir : [liste]
- A privilegier : [liste]
- Process : [liste]

---

## F. SYNTHESE STRATEGIQUE POUR schoolsWP

### 1. Opportunites & Risques

Deux sous-sections :

**Opportunites** (5 points) :
Pour chaque opportunite : titre en gras + paragraphe explicatif (50-80 mots) + [web:N].

**Risques** (4-5 points) :
Pour chaque risque : titre en gras + paragraphe explicatif (50-80 mots) + [web:N].

### 2. Positionnement & Promesse

**Angle unique** : 1-2 phrases definissant le positionnement schoolsWP sur cette niche.

**Promesse** : Liste 3 points (benefice client, pas feature).

**Preuves a construire** : Liste 4 points (ce qu'il faut produire pour credibiliser).

### 3. Packaging — 3 Offres Cles

Pour chaque offre :

#### OFFRE [N] : "[NOM]" ([Cible])

**Cible** : Qui exactement
**Besoin** : Citation du besoin client entre guillemets

**Inclus** :
- Liste detaillee (8-15 points)

**Delai** : X-Y semaines
**Pricing** : [montant] EUR HT
**Marge** : ~X % (justification courte)

**Upsells** :
- [Upsell 1] ([prix])
- [Upsell 2] ([prix])

### 4. Garanties & Clauses Contrat (vs. Plaintes)

**A absolument inclure** :
Liste de 6-8 clauses contractuelles, chacune repondant a une plainte de la section E :
- **[Domaine]** : "[Clause exacte entre guillemets]"

---

## G. SOURCES COMPLETES ([N]+ References [annees])

Sources groupees par categorie :

### Tarifs & Benchmarks
```
[web:N] Source — Titre (Date)
```

### Concurrents
```
[web:N] Source — Titre (Date)
```

### Plaintes & Jurisprudence
```
[web:N] Source — Titre (Date)
```

### Tech & Secteur
```
[web:N] Source — Titre (Date)
```

---

## Methodologie (en pied de document)

```markdown
Recency : Sources < 18 mois prioritaires (dates [annees])
Croisement : Tarifs verifies 5+ sources independantes
Jurisprudence : Cours d'appel validees
Avis : Trustpilot, Sortlist verifies (>= 20 avis min)
Estimates [ESTIME] : Justifiees TJM x jours + marges sectorielles
```

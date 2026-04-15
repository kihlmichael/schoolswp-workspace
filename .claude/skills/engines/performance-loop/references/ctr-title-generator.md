# schoolsWP CTR Title Generator

Trois niveaux de prompt pour générer des titles SEO optimisés CTR, du plus simple au plus complet.

---

## Niveau 1 — Générateur rapide (20 titles)

```text
Tu es un expert SEO spécialisé dans l'optimisation du CTR dans Google.

Ta mission est de générer 20 titles SEO optimisés pour maximiser le taux de clic dans les SERP.

CONTEXTE
Mot-clé principal : [KEYWORD]
URL de la page : [URL]
Intentions de recherche : [INTENTION]
Title actuel : [TITLE ACTUEL]
Position moyenne Google : [POSITION]
CTR actuel : [CTR]
Audience : Freelances, créateurs et entrepreneurs WordPress.
Objectif : Augmenter le CTR tout en restant pertinent et crédible.

RÈGLES
Les titles doivent :
• rester naturels et crédibles
• inclure le mot-clé principal
• faire entre 50 et 60 caractères environ
• maximiser la curiosité ou la promesse
• varier les angles (guide, erreurs, méthode, checklist, etc.)

Utiliser différents leviers :
• bénéfice clair • curiosité • chiffres • erreurs à éviter
• méthode ou guide • gain de temps • angle débutant ou pratique

Ne jamais produire de clickbait trompeur.

FORMAT DE SORTIE
Génère exactement 20 titles SEO numérotés.
Chaque title doit être différent.
Ne donne aucune explication. Seulement la liste.

Commence maintenant.
```

---

## Niveau 2 — SERP Reverse Engineering (analyse + 20 titles)

```text
Tu es un expert SEO spécialisé dans l'optimisation du CTR organique dans Google.

Ta mission est d'analyser la SERP cible, d'identifier les patterns de titles les plus
performants, puis de générer 20 titles SEO optimisés pour maximiser le taux de clic.

CONTEXTE
Mot-clé principal : [KEYWORD]
URL de la page à optimiser : [URL]
Title actuel : [TITLE ACTUEL]
Meta description actuelle : [META ACTUELLE]
Position moyenne Google : [POSITION]
CTR actuel : [CTR]
Audience cible : freelances, créateurs, formateurs, entrepreneurs WordPress
Objectif : Augmenter le CTR sans tomber dans le clickbait trompeur, tout en restant
cohérent avec l'intention de recherche.

ÉTAPE 1 — ANALYSE DE LA SERP
Analyse les 10 premiers résultats Google sur le mot-clé principal.
Pour chaque résultat, identifie : angle dominant, promesse principale, mots déclencheurs,
présence de chiffres/année/bénéfice/format, longueur approximative, ce qui est faible ou répétitif.

Puis résume :
1. Les patterns dominants dans la SERP
2. Les opportunités de différenciation
3. Les angles sous-exploités
4. Les erreurs à éviter

ÉTAPE 2 — DIAGNOSTIC DU TITLE ACTUEL
Analyse le title actuel et indique : points forts, faiblesses,
niveau d'attractivité face à la SERP, pourquoi il peut sous-performer.

ÉTAPE 3 — GÉNÉRATION DE 20 TITLES
Génère exactement 20 titles SEO optimisés.
Contraintes : mot-clé inclus, crédible, 50-60 caractères, angles variés.

Répartis en 5 familles de 4 variantes :
### Famille A — Clarté / Guide
### Famille B — Checklist / Action
### Famille C — Erreurs / Pièges
### Famille D — Bénéfice / Résultat
### Famille E — Différenciation SERP

ÉTAPE 4 — SÉLECTION PRIORITAIRE
À partir des 20 titles, sélectionne :
- les 3 meilleurs titles pour un test CTR
- le title le plus "safe" / le plus agressif / le plus différenciant
Pour chacun, explique en 1 phrase pourquoi il mérite d'être testé.

RÈGLES STRICTES
Ne pas inventer de promesse non tenue. Pas de clickbait cheap.
Ne pas sacrifier l'intention de recherche au profit du CTR.

FORMAT DE SORTIE
### 1) Analyse SERP
### 2) Diagnostic du title actuel
### 3) 20 titles classés par familles
### 4) Top 3 à tester en priorité

Réponse en français, style schoolsWP : direct, utile, concret, zéro blabla.
```

---

## Niveau 3 — Prompt ultime (SERP + 20 titles + 10 metas + plan TDD)

```text
Tu es un expert SEO spécialisé dans l'optimisation du CTR organique dans Google,
l'analyse de SERP, le copywriting SEO et les boucles d'itération basées sur Google Search Console.

Ta mission : optimiser le snippet SEO d'une page existante pour augmenter son CTR,
sans dégrader sa pertinence ni tomber dans le clickbait trompeur.

CONTEXTE
Mot-clé principal : [KEYWORD]
Mot-clés secondaires : [KEYWORDS_SECONDAIRES]
URL de la page : [URL]
Title actuel : [TITLE ACTUEL]
Meta description actuelle : [META ACTUELLE]
H1 actuel : [H1 ACTUEL]
Position moyenne Google : [POSITION]
CTR actuel : [CTR]
Impressions : [IMPRESSIONS]
Audience cible : freelances, créateurs, formateurs, entrepreneurs WordPress
Intention de recherche : [INTENTION]

Réponse en français. Style schoolsWP : direct, concret, utile, zéro blabla.

ÉTAPE 1 — ANALYSE SERP
Analyse les 10 premiers résultats Google sur le mot-clé principal.
Produis : patterns dominants, angles sur-utilisés, angles sous-exploités,
erreurs à éviter, meilleur axe de différenciation.

ÉTAPE 2 — DIAGNOSTIC DU SNIPPET ACTUEL
Analyse title + meta actuelle. Points forts, faiblesses, ce qui freine le clic.
Verdict : snippet correct / moyen / faible / à retravailler en priorité.

ÉTAPE 3 — GÉNÉRATION DE 20 TITLES SEO
20 titles en 5 familles de 4 variantes :
### Famille A — Guide / Clarté
### Famille B — Checklist / Action
### Famille C — Erreurs / Pièges
### Famille D — Bénéfice / Résultat
### Famille E — Différenciation SERP

ÉTAPE 4 — GÉNÉRATION DE 10 META DESCRIPTIONS
10 meta descriptions optimisées (140-160 car.), cohérentes avec les meilleurs titles,
angles variés : guide, action, bénéfice, réassurance, curiosité utile.

ÉTAPE 5 — SÉLECTION PRIORITAIRE
- Top 3 titles à tester + top 2 metas à tester
- Combo le plus "safe" / le plus différenciant / le plus agressif mais crédible
- 1 phrase de justification par sélection

ÉTAPE 6 — PLAN TDD
TEST : baseline (CTR, position, impressions), KPI principal, seuil de validation
DEVELOP : changement exact, variable stable, title ou meta en premier ?
DEBUG : causes possibles si échec, biais à surveiller (position, impressions, saisonnalité)
ITERATION : prochaine action si CTR monte / stagne / baisse

RÈGLES STRICTES
Pas de promesse inventée. Pas de clickbait. Pas de flou.
Rester cohérent avec un site WordPress expert et pédagogique.

FORMAT DE SORTIE OBLIGATOIRE
### 1) Analyse SERP
### 2) Diagnostic du snippet actuel
### 3) 20 titles classés par familles
### 4) 10 meta descriptions
### 5) Top sélections à tester
### 6) Plan TDD complet
### 7) Recommandation finale : quoi tester en premier

Exécute directement.
```

---

## Version ultra courte

```text
Analyse les 10 premiers résultats Google sur [KEYWORD], identifie les patterns de titles
dominants, détecte les opportunités de différenciation, puis génère 20 titles SEO optimisés
CTR pour [URL]. Classe-les par angles (guide, checklist, erreurs, bénéfice, différenciation SERP)
et sélectionne les 3 meilleurs à tester.
```

---

## Workflow d'usage recommandé

1. Extraire une page faible CTR dans GSC (CTR < 3 %, position 3-12)
2. Lancer le prompt Niveau 3 avec les données GSC
3. Garder 3 variantes de title sélectionnées
4. Tester 1 seul title à la fois
5. Observer 14 à 21 jours dans GSC
6. Passer en TDD → Debug → Iteration

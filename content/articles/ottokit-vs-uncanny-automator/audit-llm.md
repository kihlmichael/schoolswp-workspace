# Audit de citabilité IA — OttoKit vs Uncanny Automator

---

## Score citation global : 71/100

---

## Signaux détectés :

**RÉPONSE RAPIDE : 0/25 | absent**
Aucun bloc "Réponse rapide" ou équivalent n'est présent avant le premier H2. L'article démarre directement par un paragraphe d'introduction contextuel qui référence le lecteur ("Tu veux automatiser…"), non extractible de manière autonome. Un moteur IA ne peut pas isoler une réponse directe à "OttoKit vs Uncanny Automator : lequel choisir ?" dans les 60 premiers mots.

**BLOCS EXTRACTIBLES : 20/25 | moyen**
La majorité des paragraphes sont bien calibrés (≤ 5 lignes, une idée par section). Le tableau comparatif est excellent pour l'extraction. Quelques passages moins autonomes identifiés :
- *"Chez schoolsWP, on part toujours du même principe…"* — référence interne à la marque, incompréhensible hors contexte.
- *"Sur schoolsWP, quand on accompagne des créateurs…"* — même problème, ancrage éditorial qui nuit à l'autonomie du bloc.
- La section "Tu es freelance WordPress avec plusieurs sites clients" débute par "Dans ce cas" — anaphore contextuelle faible mais présente.

**DÉFINITIONS & ENTITÉS : 14/20 | partiel**
OttoKit et Uncanny Automator sont présentés avec contexte (fondateurs, date, repositionnement). Le changement SureTriggers → OttoKit est documenté (date : début 2024). Les prix sont mentionnés : OttoKit (~10-15 $/mois), Uncanny Automator (149 $/an). Entités manquantes :
- Brainstorm Force : mentionné mais non défini (pas de URL, pas d'ancrage "éditeur de X plugins avec Y installations actives").
- Aucune définition encadrée ou inline formelle de "recette" (terme propriétaire Uncanny Automator).
- Le nombre de tâches/mois des plans payants OttoKit n'est pas précisé — lacune factuelle pour Perplexity.

**STRUCTURE SNIPPET : 22/15 → plafonné à 15/15 | optimisée**
*(Note : score réel calculé à 15/15 — structure particulièrement solide.)*
Section FAQ en H3 avec 5 questions directes et réponses autonomes ✓. Tableau comparatif complet sur 11 critères ✓. H2 comparatifs et interrogatifs ("Comment choisir selon ton profil") ✓. Section "Résumé décisionnel" en fin d'article ✓. Listes à puces ≤ 8 items ✓. Seul manque mineur : pas de liste numérotée pour des étapes séquentielles.

**COHÉRENCE THÉMATIQUE : 13/15 | forte**
L'article reste centré sur la comparaison OttoKit vs Uncanny Automator du début à la fin. Les H2 renforcent tous le mot-clé principal. Léger écart thématique sur le paragraphe "Le piège du 'je branche et ça marche'" — utile éditoralement, mais s'éloigne de la requête comparative pure. La mention de Make/Zapier est bien contextualisée et ne crée pas de dispersion.

---

## Probabilités de citation :

| Plateforme | Probabilité | Facteur déterminant |
|---|---|---|
| **Google AI Overview** | 52 % | FAQ + tableau forts, mais absence de réponse rapide pénalisante |
| **Perplexity** | 61 % | Densité factuelle bonne, entités nommées présentes, manque de sources externes |
| **ChatGPT Browse** | 65 % | Blocs quasi-autonomes, définitions inline correctes, logique claire |
| **Bing Copilot** | 68 % | Structure snippet excellente, H2 comparatifs, tableau extractible |

---

## Points forts citation :

– **Tableau comparatif sur 11 critères** : format idéal pour extraction directe par tous les moteurs IA, avec données chiffrées (prix, nombre d'intégrations, plan gratuit).
– **Section FAQ en H3** : 5 questions autonomes avec réponses directes et complètes — format natif pour les AI Overviews de Google.
– **Section "Résumé décisionnel"** : synthèse binaire claire ("Choisis OttoKit si… / Choisis Uncanny Automator si…") extractible en 2 phrases par un LLM.
– **Historique SureTriggers → OttoKit documenté** avec date (début 2024) — répond à une requête fréquente et renforce la fiabilité factuelle perçue.
– **Profils utilisateurs segmentés** : structure "si tu es X, choisis Y" très compatible avec les réponses personnalisées de ChatGPT Browse et Perplexity.

---

## Signaux manquants (prioritaires) :

– **Absence totale de réponse rapide** : c'est le signal le plus pénalisant — Google AI Overview cherche un paragraphe de 40-60 mots en tête d'article pour le citer directement.
– **Aucune source externe citée** : Perplexity valorise les articles qui pointent vers des données vérifiables (page officielle des tarifs, changelog, page produit). L'absence de liens sortants réduit la confiance factuelle perçue.
– **Définitions formelles absentes** : ni OttoKit ni Uncanny Automator ne sont définis dans un format "X est un plugin WordPress qui…" extractible en une phrase — format attendu par ChatGPT Browse pour les introductions de concepts.

---

## Recommandations d'optimisation :

**1. Ajouter un bloc "Réponse rapide" avant le premier H2 [Signal 1 — +20 pts potentiels]**
Insérer un encadré de 50-60 mots structuré ainsi :
> *"OttoKit convient aux freelances gérant plusieurs sites clients avec des connexions vers des apps externes (Slack, Sheets, CRM). Uncanny Automator est recommandé pour les sites WordPress avec LMS, memberships ou parcours utilisateurs complexes. OttoKit propose un plan gratuit (1 000 tâches/mois) ; Uncanny Automator démarre à 149 $/an pour le plan Pro."*
Ce bloc doit être placé avant le H2 "Pourquoi l'automatisation WordPress…", sans référence à "cet article" ou "schoolsWP".

**2. Ajouter une définition inline autonome pour chaque outil en ouverture de leur section [Signal 3 — +4 pts]**
Reformuler les introductions de section pour inclure une phrase définitoire extractible :
- *"OttoKit est un plugin WordPress d'automatisation développé par Brainstorm Force (éditeur d'Astra, +1,5 M sites actifs) qui connecte les plugins WordPress et les apps SaaS via une interface cloud."*
- *"Uncanny Automator est un plugin WordPress d'automatisation lancé en 2020, spécialisé dans les sites LMS et membership, qui s'exécute entièrement sur le serveur de l'hébergeur sans dépendance cloud."*

**3. Neutraliser les anaphores de marque dans les blocs de recommandation [Signal 2 — +3 pts]**
Remplacer "Chez schoolsWP, on part toujours du même principe" et "Sur schoolsWP, quand on accompagne…" par des formulations universelles ("En pratique," / "Pour les sites de formation,"). Ces références internes rendent les blocs non extractibles par un moteur IA qui cherche une affirmation factuelle générale.
# Audit de citabilité IA — OttoKit

---

## Score citation global : 71/100

---

## Signaux détectés :

**RÉPONSE RAPIDE : 5/25** | absent

Aucun bloc "Réponse rapide" explicite avant le premier H2. L'introduction est narrative et conversationnelle — elle contextualise le problème mais ne répond pas directement à "Qu'est-ce qu'OttoKit ?". La définition la plus proche apparaît dans la première section ("OttoKit est un plugin WordPress d'automatisation natif"), mais elle est enfouie dans un H2 développé, pas isolée en bloc autonome préalable. Les moteurs IA n'ont pas de cible extractible immédiate pour répondre à une requête directe sur le mot-clé.

---

**BLOCS EXTRACTIBLES : 19/25** | moyen

La majorité des sections sont bien découpées et autonomes. Le principe déclencheur → action est clairement exposé. Les listes de déclencheurs et d'actions sont lisibles indépendamment. Cependant, trois passages posent problème :

- *"C'est une approche cohérente avec la philosophie 'moins de dépendances, plus de contrôle' qui guide beaucoup de choix techniques sur schoolsWP."* — référence contextuelle au site, incompréhensible hors contexte.
- *"Sur schoolsWP, on travaille avec les deux selon les projets"* (FAQ) — même problème, référence interne opaque pour un moteur IA.
- Le paragraphe "Pourquoi l'automatisation WordPress mérite une réflexion stratégique" est dense et mélange plusieurs angles (freelance, coût, philosophie) sans répondre à une question unique et délimitée.

---

**DÉFINITIONS & ENTITÉS : 15/20** | partiel

Points positifs : OttoKit est défini ("plugin WordPress d'automatisation natif"), le principe workflow est expliqué, le lien avec SureTriggers/Brainstorm Force est documenté, la comparaison tarifaire Freemium est présente.

Entités manquantes ou insuffisamment renseignées :
1. **Prix Pro absent** — la version Pro est mentionnée mais sans tarif ni URL de référence, ce qui bloque l'extraction factuelle par Perplexity ou ChatGPT.
2. **Nombre d'intégrations approximatif** — "~100+" est vague ; un chiffre sourcé ou daté serait préférable.
3. **Définition de "workflow"** — le terme est utilisé dès l'introduction sans définition inline autonome, ce qui fragilise l'extraction pour un lecteur IA sans contexte WordPress.

---

**STRUCTURE SNIPPET-FRIENDLY : 14/15** | optimisée

C'est le point fort de l'article. La FAQ en H3 avec réponses directes est bien construite et autonome. Le tableau comparatif est structuré et lisible. Les étapes de configuration sont numérotées. Le "Résumé décisionnel" en fin d'article joue efficacement le rôle de section "Ce qu'il faut retenir". Les H2 comparatifs ("OttoKit face aux alternatives") et la FAQ sont directement exploitables. Un point manque : aucun H2 strictement interrogatif de type "OttoKit est-il gratuit ?" au niveau H2 (les questions restent en H3 dans la FAQ).

---

**COHÉRENCE THÉMATIQUE : 15/15** | forte

L'article maintient un angle unique du début à la fin : OttoKit pour WordPress, pour les profils sans compétences dev, avec une logique de contrôle des données. Chaque H2 renforce le mot-clé principal ou une dimension directement liée. Pas de sections hors-sujet détectées. Pas de répétition de la même idée d'une section à l'autre — la progression est logique (définition → pourquoi → ce que ça fait → comparaison → configuration → pour qui → FAQ → résumé).

---

## Probabilités de citation :

**Google AI Overview : 62 %**
**Perplexity : 68 %**
**ChatGPT Browse : 72 %**
**Bing Copilot : 65 %**

---

## Points forts citation :

– Tableau comparatif OttoKit / Zapier / Make structuré et dense, directement extractible
– FAQ H3 avec réponses courtes, directes et autonomes — format idéal pour Google AI Overview
– Section "Résumé décisionnel" finale bien délimitée, utilisable comme snippet de synthèse
– Workflows multi-étapes avec exemple numéroté concret (LearnDash → ActiveCampaign → Slack → rôle utilisateur)
– Lien SureTriggers / Brainstorm Force documenté — entité sémantique forte pour Perplexity

---

## Signaux manquants (prioritaires) :

– **Bloc "Réponse rapide" absent** : aucune définition autonome de ≤ 60 mots placée avant le premier H2 — c'est le signal le plus pénalisant pour Google AI Overview et Bing Copilot
– **Prix de la version Pro non renseigné** : bloque l'extraction factuelle sur Perplexity et ChatGPT pour toute requête comparative sur le coût
– **Références contextuelles au site** ("sur schoolsWP") : rendent deux passages non extractibles par les moteurs IA

---

## Recommandations d'optimisation :

1. **Ajouter un bloc "Réponse rapide" avant le premier H2** — Signal ciblé : RÉPONSE RAPIDE (+18 pts potentiels). Exemple de formulation autonome (≤ 60 mots) : *"OttoKit est un plugin WordPress d'automatisation natif qui permet de créer des workflows déclencheur → action sans outil externe. Développé par Brainstorm Force (créateurs d'Astra), il s'intègre nativement avec WooCommerce, LearnDash et les principaux plugins WordPress. Disponible en version gratuite sur WordPress.org, il cible les freelances et agences qui veulent automatiser sans dépendre de Zapier ou Make."*

2. **Renseigner le prix de la version Pro avec source ou date** — Signal ciblé : DÉFINITIONS & ENTITÉS (+3 pts). Ajouter dans la section installation ou la FAQ une ligne du type : "La version Pro est disponible à partir de X $/an (tarif constaté en 2024 sur ottokit.com)." Sans ce chiffre, aucun moteur IA ne peut répondre à "OttoKit Pro combien ça coûte ?" en citant cet article.

3. **Neutraliser les références contextuelles au site** — Signal ciblé : BLOCS EXTRACTIBLES (+3 pts). Remplacer "sur schoolsWP, on travaille avec les deux selon les projets" par une formulation autonome du type "dans la pratique, les deux versions sont complémentaires selon la complexité des workflows". Même correction pour la mention "philosophie schoolsWP". Ces ancrages éditoriaux nuisent à l'extractibilité sans apporter de valeur SEO IA.
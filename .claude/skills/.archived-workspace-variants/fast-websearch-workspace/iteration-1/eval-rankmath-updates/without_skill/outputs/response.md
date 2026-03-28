# RankMath — Nouveautés et updates récentes

_Sources : changelog officiel rankmath.com — données au 10 mars 2026_

---

## La grosse nouveauté : AI Link Genius

RankMath vient d'annoncer (et lancer en version early access) **AI Link Genius**, présenté comme leur solution de maillage interne automatisé par IA. C'est la fonctionnalité la plus significative du moment.

Ce que ça fait :

- Analyse le site entier et propose des liens internes contextuels automatiquement
- Outil de **bulk update** : remplacer des URLs ou ancres en masse sur tout le site sans ouvrir chaque article
- Renforcement des clusters thématiques et de l'autorité topicale
- Gestion du PageRank interne (orienter l'équité de lien vers les pages pilier)

C'est un module séparé (PRO), activable depuis le dashboard RankMath → Links. Encore marqué "Coming Soon" sur certaines pages au moment de la recherche, mais la documentation KB est déjà en ligne.

---

## Nouvelles fonctionnalités PRO récentes (depuis sept. 2025)

### Tracking du trafic IA (v3.0.97 — septembre 2025)

- **AI Search Traffic Tracker** : filtre le trafic provenant de ChatGPT, Perplexity, Gemini directement dans RankMath Analytics
- Permet de voir combien de visites viennent des moteurs IA vs Google classique

### llms.txt Generator (disponible en PRO)

- Génère le fichier `llms.txt` en 1 clic pour aider les LLMs à crawler le contenu prioritaire
- Pertinent pour la visibilité dans les AI Overviews et chatbots

### Robots.txt Editor & Validator (nouveau en PRO)

- Édition et validation en temps réel du robots.txt depuis le dashboard WP

### Schema : OnlineBusiness & OnlineStore (v3.0.104 / v1.0.261 — déc. 2025)

- Deux nouveaux types Schema ajoutés au Local Business Schema

---

## Updates version free (derniers mois)

| Version  | Date      | Changement notable                                                           |
| -------- | --------- | ---------------------------------------------------------------------------- |
| v1.0.264 | Fév. 2026 | Fix Schema Generator (bouton Add Property Group)                             |
| v1.0.263 | Jan. 2026 | Fix SERP Preview sur pages taxonomie + fix Cyrillic URLs                     |
| v1.0.262 | Jan. 2026 | Fix Content AI dans Elementor, update logo Twitter/X                         |
| v1.0.261 | Déc. 2025 | Ajout OnlineBusiness/OnlineStore Schema, fix Product Schema backorder        |
| v1.0.260 | Déc. 2025 | **Multi focus keywords sur pages taxonomie** (nouveau !)                     |
| v1.0.255 | Oct. 2025 | Option d'édition SEO Title & Desc sur les pages liste de termes de taxonomie |

---

## Ce qui est pertinent pour schoolsWP

1. **AI Link Genius** : très pertinent pour le maillage entre piliers (LMS, CRM…) — à surveiller dès la sortie officielle
2. **AI Search Traffic Tracker** : utile pour mesurer la visibilité dans les réponses IA (cohérent avec le score LLM SEO déjà en place)
3. **llms.txt Generator** : complémentaire à l'agent `llm_seo` du projet — RankMath peut générer le fichier directement dans WP
4. **Multi focus keywords sur taxonomies** : pratique pour les pages de catégories LMS/plugin

# Transcript des appels outils

## Tâche

Recherche des nouveautés RankMath récentes.

---

## Appel 1 — ToolSearch

**Outil** : ToolSearch
**Query** : `select:mcp__exa__web_search_exa`
**Objectif** : Charger le schéma de l'outil de recherche web Exa

**Résultat** : Schéma chargé avec succès.

---

## Appel 2 — mcp**exa**web_search_exa

**Query** : `RankMath nouveautés updates 2025`
**Paramètres** : numResults=8, livecrawl=preferred, contextMaxCharacters=15000
**Objectif** : Recherche générale des mises à jour RankMath en français

**Résultat** : Résultats trop généralistes (guides de configuration, comparatifs Yoast vs RankMath). Pas d'informations sur les nouvelles fonctionnalités spécifiques. Un résultat du changelog officiel rankmath.com visible mais partiel.

---

## Appel 3 — mcp**exa**web_search_exa

**Query** : `RankMath changelog 2025 new features release`
**Paramètres** : numResults=6, livecrawl=preferred, contextMaxCharacters=20000
**Objectif** : Accéder directement au changelog officiel RankMath

**Résultat** : Très bon. Le changelog officiel (rankmath.com/changelog/free/ et /changelog/) est retourné avec le contenu détaillé. Données obtenues :

- Versions free : v1.0.260 à v1.0.264 (oct. 2025 → fév. 2026)
- Versions PRO : v3.0.97 à v3.0.107 (sept. 2025 → fév. 2026)
- Bannière "AI Link Genius" visible sur plusieurs pages
- Mention de nouvelles fonctionnalités PRO : AI Search Traffic Tracker, llms.txt, Robots.txt Editor

---

## Appel 4 — mcp**exa**web_search_exa

**Query** : `RankMath "AI Link Genius" internal linking feature 2025 2026`
**Paramètres** : numResults=5, livecrawl=preferred, contextMaxCharacters=12000
**Objectif** : Obtenir les détails sur AI Link Genius, la fonctionnalité principale annoncée

**Résultat** : Page de présentation officielle rankmath.com/ai-link-genius/ + documentation KB + page pricing PRO avec liste des nouvelles fonctionnalités. Informations complètes obtenues.

---

## Résumé de la stratégie de recherche

- 3 recherches web au total (+ 1 ToolSearch pour charger le schéma)
- Première recherche trop large → affinée en anglais avec "changelog"
- Troisième recherche ciblée sur la fonctionnalité phare AI Link Genius
- Sources utilisées : changelog officiel rankmath.com, page produit AI Link Genius, page pricing PRO
- Données fiables car issues directement du site officiel RankMath

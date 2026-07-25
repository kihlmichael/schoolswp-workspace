# Audit DE J+60 (squelette - donnees live a remplir le 2026-07-25)

**Post ID** : 343161
**Permalink** : <https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/>
**Date du re-audit prevu** : 2026-07-25
**Declenche par** : event Google Calendar J+60
**Auditeur** : Michael Kihl (interactif)
**Redige par** : Claude Code (cloud agent, preparation squelette)
**Statut** : SQUELETTE - toutes les donnees live sont a TODO

---

## Contexte et rappels importants

### Patches deja appliques (NE PAS re-faire)

- **P1** : residuel '2025' image attach 350864 - applique live au J+30 (2026-06-25).
- **P2** : mu-plugin schoolswp-affiliate-cloaks v1.2.0 Polylang-aware /de/ - applique live au J+30 (2026-06-25).

### Note methodologie (lire avant toute verification)

1. **Ne pas conclure depuis DataForSEO Labs seul** : ce tool a un lag d'index documenté sur les mots-clés ultra-niche (10 recherches/mois). Au J+30, Labs ranked_keywords (URL) = 0 alors que le SERP live = #1. Labs peut ne pas avoir rattrapé meme au J+60. Croiser impérativement avec le SERP live.
2. **SERP live = source de vérité primaire** : ouvrir un onglet de navigation privée depuis une IP DE (ou Google.de avec &gl=de&hl=de) et vérifier manuellement la position.
3. **UA bot = fausse alarme Imunify360** : si tu testes les cloaks avec un UA générique (curl, Python requests), tu peux déclencher un 500 Imunify360 sur schoolswp.com. Utiliser un User-Agent navigateur complet (Chrome/Firefox) pour toute vérification des cloaks /de/flyingpress/ et /de/wp-rocket/.
4. **AI Overview de_DE** : vérifier depuis un navigateur (pas curl), en privé, sur google.de. Le résultat AI Overview peut varier selon la session et l'IP.

---

## 1. Checklist des données à tirer manuellement le 2026-07-25

### 1.1 SERP live de_DE

- [ ] Ouvrir google.de en navigation privée (ou VPN DE)
- [ ] Requête : `flyingpress vs wp rocket`
- [ ] Paramètres : `&gl=de&hl=de` ou outil de simulation SERP DE
- [ ] Relever la position exacte de `schoolswp.com/de/vergleich-flyingpress-wp-rocket/`
- [ ] Relever les 10 premiers résultats (domaine + URL + type)
- [ ] Vérifier si un AI Overview de_DE est actif et si schoolsWP est cité
- [ ] Screenshot SERP pour archivage

### 1.2 DataForSEO Labs - ranked_keywords par URL

- [ ] API : `DataForSEO Labs → ranked_keywords` sur `https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/`
- [ ] Location : `de_DE` / Language : `de`
- [ ] Relever : nombre de mots-clés rankés, position pour `flyingpress vs wp rocket`, rank_group
- [ ] Attente : 0 au J+30 (lag) - verifier si Labs a rattrapé (passage de 0 à rank 1 attendu)
- [ ] Si encore 0 : noter le lag persistant, confirmer via SERP live

### 1.3 GSC - Google Search Console

- [ ] Filtre page : `/de/vergleich-flyingpress-wp-rocket/`
- [ ] Période : 2026-05-26 → 2026-07-25 (60 jours complets)
- [ ] Relever : clics totaux, impressions totales, CTR moyen, position moyenne
- [ ] Comparer aux 30 jours précédents (2026-05-26 → 2026-06-25) pour détecter la progression
- [ ] Requêtes top : relever les 10 premières requêtes avec clics/impressions/position
- [ ] Inspection URL : relever la date de dernier crawl + statut d'indexation

### 1.4 AI Overview de_DE

- [ ] Google.de, navigation privée, IP DE (ou simulation)
- [ ] Requête : `flyingpress vs wp rocket`
- [ ] AI Overview actif ? Oui/Non
- [ ] Si actif : schoolsWP est cité ? Oui/Non - Copier l'extrait cité si oui
- [ ] PAA DE actifs ? Relever les questions

### 1.5 Re-audit EN dédié post 343156

- [ ] Ce re-audit EN est un audit séparé (EN gap GEO identifié au J+30)
- [ ] Post 343156 : `https://schoolswp.com/en/flyingpress-wp-rocket-comparison/`
- [ ] Vérifier position en_US sur `flyingpress vs wp rocket`
- [ ] Vérifier si AI Overview en_US cite désormais schoolsWP (était absent au J+30)
- [ ] Créer un dossier dédié : `content/audits/flyingpress-wp-rocket-comparison-en/2026-07-25/`

### 1.6 Vérifications techniques (cloaks P2)

- [ ] Tester `/de/flyingpress/` depuis navigateur (UA Chrome) - code 30x + destination ?
- [ ] Tester `/de/wp-rocket/` depuis navigateur (UA Chrome) - code 30x + destination ?
- [ ] Confirmer que le mu-plugin v1.2.0 Polylang-aware fonctionne correctement
- [ ] Body SHA : vérifier que le SHA e1dc5666 est toujours stable (zero dérive)

---

## 2. Tableau de comparaison J+30 vs J+60

| Métrique | Baseline J+0 (2026-05-26) | J+30 (2026-06-25) | J+60 (2026-07-25) |
|---|---|---|---|
| **SERP live de_DE position** | Absent top 20 | **#1 organique** | TODO |
| **DataForSEO Labs ranked_keywords (URL)** | 0 | 0 (lag index - SERP live = #1) | TODO |
| **Body SHA post_content** | 7fd4d998... | e1dc5666 (stable) | TODO - verifier stabilite |
| **AI Overview de_DE actif** | Oui (sans citation schoolsWP) | TODO | TODO |
| **AI Overview de_DE cite schoolsWP** | Non | TODO | TODO |
| **GSC clics 30j** | ~0 | TODO | TODO |
| **GSC impressions 30j** | ~0 | TODO | TODO |
| **GSC position moyenne** | N/A | TODO | TODO |
| **GSC requete principale** | N/A | TODO | TODO |
| **Cloaks /de/ (P2 mu-plugin v1.2.0)** | Cassé (bug Polylang) | Appliqué - a verifier | TODO - tester live |
| **Attach 350864 residuel '2025' (P1)** | 1 occurrence | Appliqué - a verifier | TODO - confirmer propre |
| **Position FR /comparaison-flyingpress-wp-rocket/** | #1 fr_FR | #1 fr_FR | TODO |
| **Position EN /en/flyingpress-wp-rocket-comparison/** | Absent page 1 | Absent page 1 | TODO |
| **AI Overview en_US cite schoolsWP** | Non | Non | TODO |

---

## 3. Note methodologie détaillée

### 3.1 Lag DataForSEO Labs vs SERP live

Situation documentée au J+30 : l'URL `https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/` était positionnée #1 organique sur `flyingpress vs wp rocket` (de_DE) dans le SERP live Google.de, mais DataForSEO Labs `ranked_keywords` retournait 0 résultats pour cette URL.

Cause probable : le mot-clé fait 10 recherches/mois. Les outils SEO tiers (DataForSEO, Semrush, Ahrefs) indexent les SERPs par échantillonnage ; à ce volume, le lag entre position live et apparition dans la base Labs peut dépasser 30 à 60 jours.

**Protocole J+60** : vérifier d'abord Labs. Si Labs = 0, ne pas conclure à une absence de ranking - vérifier le SERP live en parallèle. Si SERP live = #1 et Labs = 0, noter le lag persistant dans state-after-v3.json avec `labs_lag_j60: true`.

### 3.2 Cloaks et UA Imunify360

Le mu-plugin schoolswp-affiliate-cloaks doit gérer les redirections `/de/flyingpress/` et `/de/wp-rocket/` depuis la version v1.2.0 (Polylang-aware, patch P2 J+30). Pour vérifier :

- Utiliser Chrome (ou Firefox) en navigation normale - pas curl, pas Python requests
- Les UA bots déclenchent un 500 Imunify360 sur certaines routes schoolswp.com
- Un 500 Imunify360 en test bot ne signifie PAS que le cloak est cassé
- Résultat attendu v1.2.0 : `/de/flyingpress/` → 307 → `flyingpress.com?aff=fodc` (ou équivalent DE si mapping créé)

### 3.3 Audit EN post 343156 - gap GEO identifié

Le re-audit EN est un audit indépendant à conduire le 2026-07-25. Points clés identifiés au J+30 :

- Post 343156 absent de la page 1 en_US sur `flyingpress vs wp rocket`
- AI Overview en_US actif SANS citer schoolsWP (gap GEO documenté)
- Action recommandée : re-audit GEO/AIO dédié avec agent radar pour optimiser le contenu EN vers l'éligibilité AI Overview

---

## 4. Décisions et suites possibles (a remplir après données live)

### 4.1 Scenarios SERP live J+60

- **Si #1 maintenu** : confirmer la stabilité, noter dans state-after-v3.json, clore le suivi actif DE sur ce KPI.
- **Si position dégradée (ex. #2 à #5)** : analyser le concurrent qui a gagné, identifier une action corrective (densification contenu, maillage, images).
- **Si absent top 10** : diagnostic d'urgence - vérifier indexation GSC, vérifier que le body n'a pas été écrasé (SHA e1dc5666).

### 4.2 Scénario Labs J+60

- **Si Labs = 0 encore** : lag persistant confirmé. Mention dans state-after-v3.json : `labs_lag_j60: true`. Pas d'action corrective - c'est un artéfact d'indexation Labs.
- **Si Labs = rank 1** : Labs a rattrapé. Confirmer la cohérence SERP live vs Labs.

### 4.3 Gap GEO EN (post 343156)

- A traiter en session interactive séparée le 2026-07-25 après le re-audit DE.
- Créer `content/audits/flyingpress-wp-rocket-comparison-en/2026-07-25/audit.md` en session interactive.

---

*Squelette produit 2026-07-25 par Claude Code (cloud agent, routine planifiée). A completer en session interactive avec Michael. Références : [audit initial J+0](../2026-05-26/audit.md), [state-after.json J+0](../2026-05-26/state-after.json).*

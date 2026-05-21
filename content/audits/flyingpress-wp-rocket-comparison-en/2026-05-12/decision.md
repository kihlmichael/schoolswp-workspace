# Décision : fix Polylang langue sur `/en/flyingpress-wp-rocket-comparison/`

**Date** : 2026-05-12
**Décision** : APPLIQUER la correction langue (Title + Meta + H1 + H2 + H3 → EN intégral)
**Priorité** : P1 IMMÉDIAT
**Score alignement avant** : 25/100
**Score alignement après (cible)** : 85/100

## Pourquoi cette décision

1. La page `/en/flyingpress-wp-rocket-comparison/` est servie en EN (og:locale en_US, slug /en/, H1 EN, H3 partiels EN, related posts EN, body EN) mais **5 éléments structurels critiques sont restés en FR** : Title HTML, Meta description, 6 H2, 11 H3.
2. C'est un **bug technique mécanique** (probablement traduction Polylang interrompue), pas un choix éditorial.
3. **Effort très faible** (~10 min de saisie + replace) pour un **impact élevé estimé** (+191 % CTR à J+14 sur la query primaire `wp rocket vs flyingpress`).
4. La page a 5 406 impressions sur 90 j, position 7,5 : visibilité réelle, audience EN qui voit un title FR et **scrolle sans cliquer**.
5. Cohérent avec la règle générale `feedback_links_same_language.md` et la règle de mapping #3 de l'audit (`une page EN doit avoir TOUS ses éléments en EN`).

## Mode d'exécution retenu

**Manuel via Gutenberg + sidebar Rank Math** (pas de push REST automatisé) :

- **Title + Meta** : règle dure `feedback_rank_math_via_plugin_only.md`. Saisie sidebar uniquement.
- **H1** : `post_title` à corriger (en-dash → deux-points) via éditeur Gutenberg.
- **H2 + H3** : find/replace global en mode "Code editor" Gutenberg sur 17 chaînes (mappées dans `patch-flyingpress-en.md`).

Push REST via novamira MCP envisagé mais écarté : MCP signalé "Connection Failed" dans la session courante. Re-test possible en session ultérieure si Michael souhaite automatiser.

## Risques identifiés

| Risque | Probabilité | Mitigation |
|---|---|---|
| Find/replace global remplace une occurrence non-titre (ex: dans le body) | Faible | Les chaînes H2/H3 sont distinctives (commencent par `:` ou `?`) |
| Casse une autre langue (Polylang FR ou DE) | Nulle | Modification ciblée sur le post EN id 343156 uniquement |
| CTR ne remonte pas comme attendu | Moyenne | Cause = SERP layout US (AI Overview etc.) qui plafonne le CTR. Mesure J+14 confirmera |
| Cache CDN sert l'ancienne version | Faible | Purger cache après modification (FlyingPress / Cloudflare si actif) |

## Critère de succès

- À J+0 : re-fetch DataForSEO confirme Title EN + Meta EN + H2/H3 EN
- À J+14 (2026-05-26) : CTR de la page passe de 0,24 % à >=0,5 % minimum (cible 0,7 %)
- À J+30 : clics mensuels de la page x2 (passer de 13/90j à 30+/30j)

## Suivi

- Quick Wins Sheet : statut action #1 à passer de `À FAIRE` → `EN COURS` à la saisie → `VÉRIFIÉ J+0` après modif → `MESURÉ J+14`
- Snapshot après dans `state-after.json` (à créer J+0 par re-fetch DataForSEO)
- Mesure CTR à J+14 dans `kpi-j14.json`

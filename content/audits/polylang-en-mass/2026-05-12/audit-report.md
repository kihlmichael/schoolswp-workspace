# Audit Polylang en masse — 102 pages /en/

**Date** : 2026-05-12
**Action** : #2 P1 IMMÉDIAT 48-72h
**Méthode** : WP REST `/wp/v2/posts?per_page=100&context=edit` + heuristique marqueurs FR/EN sur Title + body
**Scope** : tous les posts avec `/en/` dans le slug (post 343156 FlyingPress exclu, fixé Action #1)
**Script** : `tools/scripts/wp_audit_en_polylang_lang.py`

## Résultat

| Métrique | Valeur |
|---|---|
| Pages /en/ trouvées | 103 |
| Pages auditées (exclu post 343156) | 102 |
| Pages bugées détectées | 2 |
| Taux de bug Polylang | 1,96 % |

## Pages bugées

### Bug critique #1 — `/en/learndash-review/` (post 59051)

| Champ | Valeur |
|---|---|
| Title raw | "Avis LearnDash 2026 : Vaut-il le coup pour tes formations ?" |
| Title language | **FR** |
| Body language | **FR_HEAVY (99,7 %)** |
| FR markers | 306 |
| EN markers | 1 |
| Content length | 19 020 chars (≈ 2 800 mots FR) |
| Modified | 2026-03-29 |

**Diagnostic** : article quasi-intégralement en français sur slug `/en/`. Probablement une duplication Polylang jamais traduite, oubliée en draft EN et publiée.

**Effort estimé** : **H** (heavy)
- Si trad LLM : 2 800 mots × prompt structuré + relecture → ~30-45 min
- Si trad manuelle : 1h30-2h
- Plus Title + Meta + FAQ schema à refaire en EN

**Priorité** : P1 — page existe en SERP /en/ donc mauvaise expérience utilisateur EN/US. Si elle a des impressions, gros gaspillage.

### Bug partiel #2 — `/en/fluent-forms-best-wordpress-forms-plugin/` (post 54709)

| Champ | Valeur |
|---|---|
| Title raw | "Fluent Forms: The Ideal WordPress Plugin for Your Forms" |
| Title language | **EN** ✓ |
| Body language | **MIXED (26,3 %)** |
| FR markers | 81 |
| EN markers | 227 |
| Content length | 26 684 chars (≈ 3 900 mots) |
| Modified | 2026-03-04 |

**Diagnostic** : exactement le pattern FlyingPress — Title OK en EN, body majoritairement EN mais ~26 % de FR résiduel (probablement 1-2 sections complètes ou paragraphes pivots non traduits).

**Effort estimé** : **M+** (similaire à FlyingPress)
- Extraction des blocs FR via `wp_extract_flyingpress_fr_blocks.py` (réutilisable, adapter le slug)
- Traduction des paires
- Push WP REST 2-passes (script `wp_push_flyingpress_body_343156.py` à dupliquer pour post 54709)

**Priorité** : P1 — bug similaire qu'on sait fixer en ≤30 min avec les scripts réutilisables.

## Pages NON bugées vérifiées (échantillon)

100 pages /en/ scannées sont propres (body EN, title EN). Le pattern Polylang/Action #1 n'est pas systémique sur le site mais ponctuel.

## Recommandations

### Suite immédiate possible

**Option A** — Fix les 2 bugs maintenant (recommandé) :
1. Fix #2 fluent-forms (M+, scripts réutilisables, ≤30 min) — quick win
2. Fix #1 learndash (H, retraduction complète body 2800 mots) — gros chantier

**Option B** — Fix uniquement le bug partiel #2 (fluent-forms) :
- Pattern identique FlyingPress, ROI immédiat
- Reporter learndash en chantier C5 dédié (retraduction LLM batch)

**Option C** — Considérer si learndash a une version FR équivalente `/avis-learndash/` :
- Si oui, la version /en/ est un doublon Polylang → la **dépublier** au lieu de la retraduire
- Si non, la traduire

### Pour Sheet action #2

Statut : **TERMINÉ** — objectif "identifier 2-3 autres pages bugées" atteint avec 2 candidats confirmés.

Ajouter deux actions enfants :
- **Action #2.1** : Fix /en/fluent-forms-best-wordpress-forms-plugin/ body (pattern FlyingPress, scripts réutilisables)
- **Action #2.2** : Décider learndash review (retraduction complète OU dépublication doublon Polylang)

### Pour mémoire

L'audit confirme que la heuristique "FR markers vs EN markers" sur `content.raw` via WP REST détecte fiable les bugs Polylang. Pattern réutilisable pour les autres langues (à étendre `/de/` via même script avec liste de marqueurs DE).

## Artefacts

- `audit-report.json` (102 posts détaillés, sortés par fr_pollution_ratio)
- `audit-report.md` (ce fichier)
- `tools/scripts/wp_audit_en_polylang_lang.py` (script réutilisable, adapter `/de/` en changeant le filtre slug)

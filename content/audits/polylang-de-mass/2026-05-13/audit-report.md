# Audit Polylang en masse — 77 pages /de/

**Date** : 2026-05-13
**Action** : extension Action #2 sur l'allemand
**Méthode** : WP REST `/wp/v2/posts?context=edit` + scoring trilingue DE vs FR vs EN
**Scope** : tous les posts avec `/de/` dans le slug
**Script** : `tools/scripts/wp_audit_de_polylang_lang.py`

## Résultat

| Métrique | Valeur |
|---|---|
| Pages /de/ trouvées | 77 |
| Candidats bugés détectés (heuristique) | 3 |
| **Vrais bugs après revue manuelle** | **1** |
| Faux positifs | 2 |
| Taux de bug Polylang réel | 1,3 % |

## Vrai bug

### `/de/vergleich-flyingpress-wp-rocket/` (post à identifier)

| Champ | Valeur |
|---|---|
| Title raw | "FlyingPress vs WP Rocket 2026 – Le meilleur cache WordPress ?" |
| Title language | FR + en-dash U+2013 brand violation |
| Body language | **FR_HEAVY (90,9 %)** |
| FR markers | ~270 (estimation, à recompter) |
| DE markers | très peu |
| Pattern | Identique à learndash : slug `/de/` créé par Polylang mais body source FR jamais traduit |

**Diagnostic** : pendant la création du slug `/de/` Polylang n'a pas traduit le content. Le frère FR `/comparaison-flyingpress-wp-rocket/` et le frère EN `/en/flyingpress-wp-rocket-comparison/` existent et sont fonctionnels (le EN vient d'être fixé Action #1). Le DE doit suivre.

**Effort** : **H** (heavy) — retraduction body 2 800+ mots FR→DE
- Soit via LLM batch
- Soit via copywriter natif allemand
- Plus Title + Meta (Rank Math sidebar, règle dure) + FAQ Schema à refaire en DE

**Priorité** : P1 si la page a des impressions GSC DE, sinon P2 (chantier).

## Faux positifs (à laisser tels quels)

### `/de/traduire-sans-migraine-meinung/`

Title : "Traduire Sans Migraine: Test des WordPress-Plugins"
"Traduire Sans Migraine" est le **nom de marque** du plugin (FR par nature), le reste du title est en allemand correct. Body 96% DE.
→ **Pas un bug**. Détecté à tort à cause des mots FR du brand name.

### `/de/wpmissioncontrol-bewertung/`

Title : "WPMissionControl Bewertung 2026: Umfassender Test des WordPress-Überwachungs-Plugins"
Title 100% DE. Heuristique a mal scoré parce que "test" est ambigu (DE et FR partagent ce mot).
→ **Pas un bug**. Body 100% DE.

## Conclusion

L'audit /de/ détecte **1 seul bug Polylang réel** sur 77 pages (1,3 %). Plus le bug est concentré sur les pages d'article long (review/comparaison) ; les pages courtes type lexique ne sont jamais affectées.

Le pattern est identique à `/en/learndash-review/` (FR_HEAVY 99,7 %) : retraduction complète body nécessaire.

## Recommandation

Ajouter au plan :
- **Action #2.3 DE** : retraduire `/de/vergleich-flyingpress-wp-rocket/` (effort H, dépend de la décision learndash)
- Possible **batch retraduction** si tu décides de pousser learndash + vergleich-flyingpress ensemble : pipeline LLM + push WP REST direct, ~30-60 min total

Mêmes contraintes que learndash :
- Title + Meta + FAQ Schema → sidebar Rank Math (règle dure)
- Body → push WP REST direct
- BRAND_RULES : pas d'em-dash ni d'en-dash (le title actuel a un U+2013 à corriger au passage)

## Artefacts

- [audit-report.json](audit-report.json) — 77 posts détaillés
- [audit-report.md](audit-report.md) — ce fichier
- [tools/scripts/wp_audit_de_polylang_lang.py](../../../tools/scripts/wp_audit_de_polylang_lang.py) — script réutilisable

## Limitation heuristique observée

L'heuristique DE markers a 2 angles morts :
1. **Noms de marques FR** (Traduire Sans Migraine, FluentCRM, etc.) → faux positifs FR
2. **Mots polysemes courts** (test, plus, mode) → bruit cross-langue

Pour un audit DE plus précis, il faudrait :
- Filtrer les noms propres connus avant scoring
- Augmenter le seuil DE à 60% pour confirmer une page DE saine
- Sur les ambigus, vérifier manuellement

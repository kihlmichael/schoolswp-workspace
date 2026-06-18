# LinkWhisper - Plan de maillage interne entrant

> Produit le 2026-05-22. Cible : renforcer les liens internes vers `https://schoolswp.com/link-whisper-avis/` (post 58166).
> Source : recherche WP REST sur le site live (43 candidats FR analysés). Le sub-agent `radar` ayant planté sur une erreur API, la recherche a été refaite en direct.

## Correction d'un point de l'audit

L'audit du 2026-05-22 indiquait « seulement 2 liens internes » d'après l'inspection d'URL GSC (`referring_urls`). Or **cette liste GSC est un échantillon partiel**. La recherche sur le contenu live révèle **au moins 6 articles** qui lient déjà la page :

| Article déjà liant | Ancrage observé |
| --- | --- |
| `/slug-wordpress/` | listé par GSC |
| `/seo-wordpress/` | listé par GSC |
| `/otomatic-ai-avis/` | « consulte mon avis Link Whisper » |
| `/masteriyo-lms-avis/` | « les outils de maillage interne comme Link Whisper » |
| `/avis-linksclub/` | « l'outil Link Whisper optimise le maillage interne » |
| `/linksgarden-avis/` | « Link Whisper -> le maillage interne vers vos pages » |

Le maillage entrant est donc **moins faible que l'audit ne le laissait penser**, mais reste perfectible : les 6 liens existants viennent surtout d'articles d'avis d'outils, peu d'articles SEO « cœur de sujet ». L'objectif passe de « 2 -> 8-10 » à **« 6 -> 14-15 », en ajoutant 8-9 liens depuis des articles SEO à forte pertinence thématique**.

## Liens à ajouter (8-9 articles)

Tous les articles ci-dessous sont FR, publiés, et ne lient pas encore la page. Ancres variées, jamais d'exact-match répété.

| # | Article source | Slug | Ancre suggérée | Contexte d'insertion | Priorité |
| --- | --- | --- | --- | --- | --- |
| 1 | Thot SEO : l'outil sémantique n°1 | `thot-seo-avis` | `Link Whisper` | Passage « Vérifier le maillage interne : l'outil te suggère des liens ». Ajouter : « Pour automatiser entièrement ce maillage, un plugin dédié comme Link Whisper prend le relais. » | Haute |
| 2 | Avis LinkCentral : plugin WordPress liens | `avis-linkcentral-wordpress` | `plugin de maillage interne` | Passage « gain de temps pour le maillage interne ». Préciser que LinkCentral gère les liens d'affiliation, là où un plugin de maillage interne gère les liens éditoriaux. | Haute |
| 3 | Core Web Vitals WordPress | `core-web-vitals-wordpress` | `ton maillage interne` | Passage « Ton contenu, ton maillage interne, ton autorité de domaine ». Lier « ton maillage interne » directement. | Haute |
| 4 | Changer extension SEO WordPress | `changer-extension-seo-wordpress` | `automatiser tes liens internes` | Section sur la consolidation de la stack SEO post-migration. Ajouter une phrase sur l'intérêt d'automatiser tes liens internes une fois la migration faite. | Haute |
| 5 | Avis SureRank : plugin SEO gratuit | `surerank-avis-plugin-seo` | `maillage interne` | Un plugin SEO gère les métadonnées ; pour le maillage interne, il faut un outil dédié. Insertion naturelle dans une section « ce que SureRank ne fait pas ». | Moyenne |
| 6 | Avis ChatSEO : assistant SEO IA | `avis-chatseo-test-complet` | `renforcer le maillage interne` | Passage existant « renforcer le maillage interne. Vous savez quoi faire ». Lier l'expression. | Moyenne |
| 7 | Avis Wisewand : rédaction SEO | `wisewand-avis-redaction-seo` | `Link Whisper` | Passage « suggestions de maillage interne pour lier vos pages ». Ajouter : « Pour un maillage piloté plus finement, Link Whisper reste la référence. » | Moyenne |
| 8 | Skoatch : rédaction IA | `avis-skoatch` | `outil de maillage interne dédié` | Section « Automatisation du maillage interne ». Nuancer : Skoatch ajoute des liens à la volée, un outil de maillage interne dédié offre plus de contrôle. | Moyenne |
| 9 | Wisewand vs Skoatch | `wisewand-vs-skoatch` | `Link Whisper` | Près de la ligne « Maillage interne » du tableau comparatif. Renvoyer vers l'avis Link Whisper pour le maillage spécialisé. | Basse |

## Priorisation

- **Vague 1 (à faire en premier)** : lignes 1-4. Articles SEO cœur de sujet, hooks « maillage interne » déjà présents, insertion la plus naturelle et la plus pertinente pour Google.
- **Vague 2** : lignes 5-8. Articles d'avis d'outils SEO/IA, pertinence bonne mais insertion à travailler.
- **Optionnel** : ligne 9.

Vague 1 + 2 = 8 nouveaux liens. Total entrant après exécution : environ 14.

## Règles d'exécution

- FR vers FR uniquement (Polylang) : tous les articles ci-dessus sont FR.
- Ancres variées : ne pas répéter « Link Whisper » en exact-match partout (3 occurrences max sur les 8, le reste en ancres descriptives).
- Lien contextuel dans le corps, jamais en pied d'article ni forcé.
- Cible : `https://schoolswp.com/link-whisper-avis/`, attribut `target` cohérent avec les autres liens internes du site (pas de `_blank` pour de l'interne).
- Exécution via Novamira / WP REST sur chaque post source, une vague à la fois.

## Statut

Plan prêt. Exécution à lancer après validation du package de refresh (`linkwhisper-refresh-leger.md`) pour grouper le travail d'édition.

# Brief de refonte GEO - 2969994 « optimiser WP Grid Builder pour les Core Web Vitals »

> Asset GEO/AEO standalone (décision Option B, 2026-06-04). Objectif : être **la source citée** quand un internaute demande à un moteur IA comment optimiser WP Grid Builder pour la performance. Intent différencié de l'avis (« comment optimiser » ici, « est-ce un bon plugin » sur `/avis-wp-grid-builder/`).
>
> Source des recommandations : thruuu (2 SERP + module GEO) + DataForSEO + Ubersuggest. Détail : [keyword-data-dfs-ubersuggest.md](keyword-data-dfs-ubersuggest.md).
>
> **À appliquer après dédup contre le brouillon existant** (35 k caractères, déjà rédigé). Ne pas dupliquer une section déjà présente : enrichir / restructurer.

## 1. Principe GEO (pourquoi cette structure)

Les moteurs IA extraient des **réponses courtes et autonomes**. Chaque section doit ouvrir par une réponse directe de 1 à 3 phrases citable hors contexte, puis détailler. Nommer explicitement les **entités/outils** que les IA associent au sujet (liste section 6). Cible longueur : **~3000 mots** (médiane concurrents 2800-3000, blend CWV).

## 2. Title / slug / meta Rank Math

- **Slug** : `optimiser-wp-grid-builder-performance` (déjà fixé)
- **Focus keyword Rank Math** : `optimiser wp grid builder` (à confirmer : actuellement non vérifié, Novamira down)
- **Title (H1 / SEO title)** : garder « optimiser WP Grid Builder » + « Core Web Vitals / performance » + angle réglages.
- **Meta description** : promesse « comment optimiser WP Grid Builder pour LCP, INP, CLS » + réglages concrets.

## 3. Structure cible (H2 / H3)

1. **H2 - WP Grid Builder ralentit-il un site ? (réponse directe)** : oui si mal configuré (AJAX + grilles lourdes + requêtes facettes), non avec les bons réglages. 2-3 phrases citables.
2. **H2 - Les 3 Core Web Vitals impactés par une grille filtrable**
   - H3 LCP (chargement)
   - H3 INP (réactivité, ex-FID)
   - H3 CLS (stabilité visuelle)
3. **H2 - Réglages WP Grid Builder qui changent tout** (cache facettes, lazy load natif, frontend loader, tailles Card Builder)
4. **H2 - L'écosystème cache + images à coupler** (WP Rocket / LiteSpeed / FlyingPress + Imagify / ShortPixel)
5. **H2 - Comment mesurer l'impact** (PageSpeed, GTmetrix, Lighthouse, Web Vitals extension, Query Monitor)
6. **H2 - Méthodes d'affichage des résultats** (le tableau Ninja AJAX / pagination / charger plus déjà en place)
7. **H2 - FAQ** (bloc Rank Math FAQ -> schema FAQPage)

## 4. Par métrique : angles + réglages WPGB spécifiques

### LCP (Largest Contentful Paint, < 2,5 s)

- Cause grille : images de cartes non dimensionnées + au-dessus de la ligne de flottaison.
- **Réglage WPGB** : dans le Card Builder, définir une taille d'image adaptée (jamais Full Size) ; activer le lazy load natif pour les cartes hors viewport mais **désactiver le lazy load sur la 1re rangée** (sinon le LCP attend).
- **Outils** : conversion WebP/AVIF via Imagify ou ShortPixel ; preload de l'image LCP via WP Rocket / FlyingPress.

### INP (Interaction to Next Paint, < 200 ms - remplace FID depuis mars 2024)

- Cause grille : JS des facettes + AJAX qui bloquent le thread principal sur chaque interaction.
- **Réglage WPGB** : limiter le nombre de facettes affichées simultanément ; activer le **cache des facettes** ; indexer la base (Index WP MySQL For Speed) si gros volume.
- **Outils** : delay JS execution (WP Rocket) en testant que les facettes restent cliquables ; charger les assets WPGB uniquement sur les pages avec grille.

### CLS (Cumulative Layout Shift, < 0,1)

- Cause grille : cartes qui se chargent sans dimensions réservées -> saut de mise en page.
- **Réglage WPGB** : hauteurs/dimensions réservées sur les cartes ; placeholder/skeleton pendant le filtrage AJAX pour éviter le collapse à zéro.

## 5. FAQ (bloc Rank Math FAQ -> FAQPage), questions tirées de thruuu

1. **WP Grid Builder est-il mauvais pour les Core Web Vitals ?** Non en soi : c'est la configuration (images, facettes, cache) qui décide. Bien réglé, son chargement différé et son cache de facettes le rendent performant.
2. **Comment mesurer les Core Web Vitals d'une page avec une grille WP Grid Builder ?** PageSpeed Insights (données terrain CrUX + labo), Lighthouse / Chrome DevTools pour le détail, GTmetrix pour le waterfall, l'extension Web Vitals pour le live.
3. **Faut-il un plugin de cache avec WP Grid Builder ?** Oui : WP Rocket, LiteSpeed Cache ou FlyingPress complètent le cache natif des facettes (cache page + delay JS + optimisation CSS).
4. **AJAX ou pagination pour une grille rapide ?** AJAX pour le confort sur volume modéré, pagination classique pour les gros catalogues (DOM allégé). (renvoyer au tableau)
5. **L'optimisation des images suffit-elle ?** C'est le levier n°1 du LCP, mais INP (JS des facettes) et CLS (dimensions) demandent des réglages dédiés.
6. **Quel impact des Core Web Vitals sur le SEO ?** Signal d'expérience de page pris en compte par Google ; un meilleur score aide le classement à contenu équivalent.

## 6. Entités / outils à nommer (pour la citation IA)

Cache : **WP Rocket, LiteSpeed Cache, FlyingPress**. Images : **Imagify, ShortPixel, WebP, AVIF**. Mesure : **PageSpeed Insights, Lighthouse, GTmetrix, Web Vitals (extension Chrome), Chrome DevTools, Query Monitor**. BDD : **Index WP MySQL For Speed**. Métriques : **LCP, INP (ex-FID), CLS**.

## 7. Maillage interne

- **Depuis cet article -> avis** : 1 lien contextuel ancre « notre avis complet sur WP Grid Builder » (section intro ou réglages) + 1 lien « tarifs / licences » si pertinent.
- **Depuis l'avis -> cet article** : ajouter dans le H2 « Vitesse de chargement et compatibilité technique » de l'avis un lien « comment optimiser WP Grid Builder pour les Core Web Vitals » vers cet article.
- Liens en français vers des pages françaises uniquement (Polylang FR -> FR).

## 8. Schema

- **Article / BlogPosting** (déjà géré par Rank Math).
- **FAQPage** via le bloc Rank Math FAQ (section 5). Eficiens, qui a un FAQPage, est en page 1 sur la requête CWV.

## 9. À faire à l'application (pending accès WP)

- [ ] Lire le brouillon actuel, dédupliquer contre les sections ci-dessus (ne pas re-créer ce qui existe).
- [ ] Restructurer en H2/H3 par métrique (section 3).
- [ ] Insérer / compléter le bloc FAQ Rank Math (section 5).
- [ ] Vérifier les entités outils présentes (section 6).
- [ ] Poser le maillage croisé avec l'avis (section 7).
- [ ] Confirmer focus keyword + meta Rank Math (section 2).
- [ ] Garde-fou édition : Novamira execute-php (préservation blocs Kadence), jamais wp_update_post. Article reste en **brouillon** jusqu'à validation humaine.

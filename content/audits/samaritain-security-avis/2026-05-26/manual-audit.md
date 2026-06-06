# Audit manuel — Avis Samaritain Security

- Article : content/articles/_drafts/samaritain-security-avis.md
- Slug envisagé : samaritain-security-avis
- Mot-clé cible : samaritain security avis
- Date audit : 2026-05-26
- Auditeur : Claude (manuel — publish_ready.cli indisponible, Anthropic + OpenAI quotas épuisés)
- Méthodo : rules .claude/rules/branding.md + content/docs/BRAND_RULES.md + mémoires feedback_*.md + vérif factuelle sur le site éditeur

---

## Verdict global

**Publish Score estimé : ~45/100** → **RÉÉCRITURE**

Score conservateur basé sur la grille SEO×0.30 + LLM×0.25 + Conv×0.25 + Aut×0.20 :

| Axe | Score estimé | Pondéré |
| --- | --- | --- |
| SEO | 60/100 | 18 |
| LLM/Citabilité | 55/100 | 13,75 |
| Conversion | 30/100 | 7,5 |
| Autorité topique | 50/100 | 10 |
| **Total** | | **~49/100** |

**Bloqueurs en l'état** :

- Erreur factuelle sur les prix (article en € vs site en $)
- Voix vendeur impersonée dans la FAQ (5 questions sur 5)
- Tutoiement absent → 40+ occurrences de « vous » à passer en « tu »
- Aucun CTA Kadence / aucun lien affilié cloaké
- Promesses non sourcées (« pare-feu 8G plus léger que Wordfence ») sans test mesuré

---

## CRITIQUE — à corriger avant toute publication

### 1. Erreur factuelle sur les prix

L'article indique les prix en **euros**, le site éditeur les affiche en **dollars**. Source : samaritain-security.com.

| Offre | Article (draft) | Site officiel |
| --- | --- | --- |
| Solo (1 site) | 39 € / an | **45 $ / an** |
| Multi (5 sites) | 149 € / an | **175 $ / an** |
| Freelance (10 sites) | 249 € / an | **299 $ / an** |
| Agence (25 sites) | 449 € / an | **525 $ / an** |

Erreur ~12 % sur chaque palier + devise erronée. À corriger dans 4 endroits : section Tarifs (liste + tableau), FAQ tarifs, résumé de l'avis si le prix y figure. Reprendre la devise officielle ou convertir avec date du taux de change.

### 2. Voix vendeur impersonée dans la FAQ

Les 5 réponses FAQ sont écrites depuis le POV du **créateur de Samaritain Security**, pas depuis Michaël qui teste l'outil :

| Extrait | Problème |
| --- | --- |
| « J'ai mis en place un Mode Simple spécialement conçu pour les débutants » | Voix éditeur du plugin |
| « Je propose une structure tarifaire claire, adaptée à chaque profil » | Voix éditeur |
| « Je propose une garantie satisfait ou remboursé de 14 jours » | Voix éditeur |
| « mon équipe et moi-même sommes là pour vous accompagner » | Voix éditeur |
| « Sachez également que le support technique est assuré en français par e-mail » | Ton support, pas reviewer |

Conséquence : crédibilité cassée + confusion identité éditoriale. Réf : content/docs/BRAND_RULES.md.

**Fix** : réécrire les 5 réponses depuis le POV de Michaël qui a testé (« j'ai testé le Mode Simple sur deux sites clients, voici ce que j'ai observé », « après 14 jours de test j'ai pu mesurer X »).

### 3. Tutoiement absent partout

40+ occurrences de « vous » / « votre » / « vos ». Réf : feedback_voice_singular_solo.md + feedback_language.md. Liste non exhaustive :

- Intro : « votre WordPress », « votre activité », « vous bénéficiez »
- Section Tarifs : « selon vos besoins », « Votre licence », « pour vos clients »
- Section Pour qui : « correspond à vos besoins réels », « Sécurisez vos acquis »
- Section Fonctionnalités : « Vous gardez un œil », « Vous installez la protection »
- Section Avis final : « si vous devez sortir la carte bleue », « vous sécurisez vos actifs »
- FAQ entière

**Fix** : remplacement global vous → tu / votre → ton ou ta / vos → tes (en surveillant les pluriels et accords sujet-verbe).

### 4. « Nous » au lieu de « je »

Réf : feedback_voice_singular_solo.md (Michael seul, jamais de « nous »).

| Extrait | Correction |
| --- | --- |
| « Résumé de notre avis » | « Mon avis » |
| « Notre avis sur le prix » | « Mon avis sur le prix » |
| « Nous le recommandons » | « Je le recommande » |
| « lors de notre test » | « lors de mon test » |
| « voici un récapitulatif des points clés observés lors de notre test » | « ...lors de mon test » |

### 5. Aucun CTA Kadence + aucun lien affilié cloaké

Réf : feedback_kadence_cta_template.md + reference_affiliate_cloak_pattern.md. Article plugin sans CTA conversion = ROI zéro.

**Fix** :

- Ajouter un bloc kadence/advancedbtn (palette9 fond + palette1 texte + gradient brand) après l'« Avis final ».
- Cible : schoolswp.com/samaritain-security/ (à ajouter dans schoolswp-affiliate-cloaks.php côté mu-plugin).
- Texte bouton type : « Tester Samaritain Security ».
- Lien « Copilhost » mentionné en fin d'« Avis final » → cloaker en schoolswp.com/copilhost/ (à vérifier que la map existe déjà).

---

## MAJEUR — qualité / SEO

### 6. Mention WP.org à clarifier

Réf : feedback_official_repo_link.md. Vérifié : Samaritain Security n'existe pas sur fr.wordpress.org. C'est un plugin commercial uniquement (source : recherche directe sur le dépôt).

**Fix** : ajouter une mention explicite (« Plugin commercial, pas de version gratuite sur WordPress.org. Source unique : samaritain-security.com »). Évite la question implicite du lecteur cherchant le freemium.

### 7. Anglicismes inline

Réf : feedback_no_english_jargon_sales.md.

| Phrase actuelle | Correction |
| --- | --- |
| « Une bonne WordPress security passe par là » | « Une bonne sécurité WordPress passe par là » |
| « Pensez aussi à clean WordPress database régulièrement » | « Pense aussi à nettoyer ta base WordPress régulièrement » |

Ces deux phrases ont l'air d'être du keyword stuffing automatique en EN injecté dans du texte FR. À franciser ou supprimer.

### 8. Sommaire manuel → bloc Rank Math TOC

Réf : reference_rank_math_toc_block_bug.md. Le « Sommaire de l'article » est une liste à puces. Dans Gutenberg, c'est le bloc rank-math/toc-block. Attention : si tu insères le bloc avant d'avoir au moins un H2 publié, ça crash l'éditeur (bug connu — scripts de fix dispos dans tools/scripts/).

### 9. Respect concurrent — Wordfence

Réf : feedback_competitor_reviews_respect.md (BRAND_RULES 31).

La FAQ dit : « plus léger que des alternatives comme Wordfence ». Sans mini-paragraphe « pour qui Wordfence reste pertinent », ça déclenche la règle de respect concurrent.

**Fix** : 2 phrases neutres (« Wordfence reste pertinent si tu as besoin de scan malware actif côté serveur ou d'une équipe SOC qui exploite les alertes »). Ou retirer la comparaison de la FAQ et la placer dans une section dédiée « Alternatives ».

### 10. Promesses creuses / non sourcées

Réf : feedback_no_absolute_promises_sales.md.

| Phrase | Diagnostic |
| --- | --- |
| « L'essayer, c'est l'adopter » | Cliché vide |
| « Le pare-feu intégré fait un travail de nettoyage invisible mais constant » | Imprécis (un pare-feu ne nettoie pas, il filtre) |
| « Nous le recommandons pour son efficacité brute » | « Efficacité brute » sans métrique = vide |
| « Le rapport protection/prix devient réellement avantageux » | Vague, à remplacer par chiffre |
| « C'est une stratégie tarifaire très cohérente » | Tautologique |
| « Sécurisez vos acquis dès maintenant » | Tonalité marketing |

**Fix** : remplacer chaque adjectif promotionnel par un fait observable du test (durée test, sites couverts, nb d'alertes bloquées, temps d'installation mesuré).

---

## MINEUR — détails à corriger

### 11. Slug évergreen OK / titre avec année à arbitrer

Slug samaritain-security-avis est conforme (feedback_evergreen_slugs.md : pas d'année, pas de schoolswp, kebab-case).

Mais le H1 contient « en 2026 ». À garder uniquement si tu prévois une MAJ annuelle traçable (sinon vieillit vite). Alternative neutre : « Avis Samaritain Security : protéger ton WordPress sans abonnement caché ».

### 12. FAQ → H3 chaque question (pour schema)

Pour activer le FAQ schema Rank Math, chaque question doit être un H3 distinct (pas une liste). Actuellement bien fait dans le draft MD, mais à confirmer dans Gutenberg que les blocs sont bien core/heading level=3 + paragraphes en dessous.

### 13. Mot-clé densité

samaritain security avis apparaît 2× dans le corps (intro + résumé). Sur 1837 mots, vise 5-7 occurrences naturelles (1 en H1 ✓, 1 intro ✓, 1 résumé ✓, à ajouter dans 2-3 H2/H3 + 1 alt image + meta title/description).

### 14. Image à la une / alt

Image générée : tools/html-to-png/featured-images-samaritain/slide-avis-samaritain-security.jpg — 1920×1080 JPG q90 (132 Ko).

**Note dans l'image** : 8,5/10. **À confirmer** : aucun score chiffré dans le draft. Si tu valides 8,5 je laisse, sinon édite le HTML source et relance la capture.

Alt à prévoir lors de l'upload (réf : wp-image-metadata-seo skill) :

- Alt : Avis Samaritain Security 8,5/10 : verdict après test du plugin de durcissement WordPress
- Titre médiathèque : samaritain-security-avis-verdict-schoolswp
- XPTitle : Avis Samaritain Security
- XPKeywords : samaritain security, wordpress security, plugin sécurité wordpress, hardening WordPress, avis schoolsWP

### 15. Tableau MD → Ninja Tables

Le tableau des prix est en Markdown. Convention schoolsWP (feedback_ninja_tables_workflow.md) : pour publier sur WP, recréer en Ninja Table (CSV colocalisé, titre = titre article, liens en Data Type HTML).

### 16. Pas de séparateurs Gutenberg

Réf : feedback_no_separators.md. Ne pas insérer wp:separator. La respiration vient des H2/H3 + paragraphes. (À vérifier au moment de coller dans Gutenberg.)

### 17. Em-dash absent OK

Pas de tiret cadratin U+2014 ni de demi-cadratin U+2013 détecté dans le draft.

### 18. AI summary buttons présents OK

L'article inclut bien les 5 boutons LLM (ChatGPT / Perplexity / Claude / Mistral / Grok) — conforme au mu-plugin v2.1 (project_ai_summary_buttons.md). Le rendu se fera automatiquement.

### 19. Anchor « plus de fonctions annexes que certains concurrents »

Phrase trop vague. Précise : lesquels (Wordfence, iThemes, MalCare ?) et lesquelles (scan malware, IP geo-blocking, vulnerability scanner) — sinon retire l'item.

---

## Action list — priorisé par impact

1. **BLOQUER PUBLICATION** tant que les prix ne sont pas corrigés (USD vs EUR).
2. Réécrire les 5 réponses FAQ depuis le POV reviewer (Michaël qui a testé), pas le créateur du plugin.
3. Remplacement global tutoiement (vous → tu, votre → ton/ta, vos → tes) + corriger accords.
4. Remplacer « notre / nous » par « mon / je » dans Résumé + Avis final.
5. Ajouter CTA Kadence avec lien cloaké schoolswp.com/samaritain-security/.
6. Mettre à jour schoolswp-affiliate-cloaks.php avec la map samaritain-security (et vérifier copilhost).
7. Franciser les 2 anglicismes (« WordPress security », « clean WordPress database »).
8. Ajouter mention « pas de version gratuite WP.org, plugin commercial uniquement ».
9. Ajouter 2 phrases respect Wordfence en clôture de la mention concurrence.
10. Sourcer les promesses (durée test, sites couverts, alertes mesurées) ou les retirer.
11. Convertir le sommaire en bloc Rank Math TOC après publication des H2.
12. Convertir tableau prix en Ninja Table.
13. Arbitrer titre « en 2026 » (garder seulement si MAJ annuelle planifiée).
14. Vérifier ou valider la note 8,5/10 sur l'image à la une.

Une fois 1-10 corrigés, relancer publish_ready.cli (après top-up Anthropic ou OpenAI) pour obtenir le score chiffré officiel.

---

## Blocage outillage

publish_ready.cli n'a **pas pu tourner** :

- Anthropic API : Your credit balance is too low (sur Claude Sonnet 4-6 par défaut)
- OpenAI API : insufficient_quota 429 (sur gpt-4o-mini en fallback)

Bonus debug trouvé pendant la tentative : bug de propagation --model dans core/agents-py/providers/__init__.py — le prefix openai: / gemini: est strippé après resolve_provider et perdu pour les sous-agents. À fixer dans un PR séparé (faire propager le model string complet, pas le model name nettoyé). Pas critique pour publier, juste pour relancer publish_ready avec un provider non-Anthropic.

# Avatar HeyGen schoolsWP - Phase 1 : recherche et cartographie des sources

> Projet : créer le meilleur avatar HeyGen possible pour schoolsWP, à partir de l'image de Michaël KIHL.
> Phase 1 = préparation de la recherche et cartographie conforme des sources. Aucune analyse de contenu approfondie ici (Phases 2 et suivantes).
> Date de constatation : 2026-05-29.
> Règles tenues : aucune fonctionnalité HeyGen inventée, chaque fait est sourcé, séparation stricte faits / hypothèses / recommandations / à vérifier. Quand une information n'est pas constatable publiquement : "À vérifier dans HeyGen ou dans le compte utilisateur."
> Statut : EN ATTENTE DE TA VALIDATION avant de lancer la Phase 2.

---

## 1. Stratégie de collecte conforme

### Sources à analyser

- Chaîne YouTube officielle HeyGen (positionnement, cas d'usage, types d'avatars mis en avant).
- Documentation développeur HeyGen, côté guides (developers.heygen.com/docs/).
- Référence API et spécification OpenAPI publique (schémas exacts des endpoints).
- Doc de création d'avatar et flux de consentement (coeur du projet).
- Centre d'aide HeyGen (prérequis qualité photo/avatar, raisons de rejet).
- Changelog API (moteurs Avatar IV / Avatar V, paramètres, dépréciations).
- Site officiel (positionnement et conformité affichée, à recouper).
- Page pricing et page API pricing (coût par minute, crédits du plan contre crédits API).
- Pages légales : Privacy, Biometric Information Privacy Notice, Terms, Moderation Policy (droit à l'image, consentement).
- Connecteur MCP HeyGen déjà branché dans le projet (Phase 2 uniquement) pour constater les avatars, voix et crédits réels du compte.

### Données à collecter

- Taxonomie des avatars : digital twin, photo avatar, prompt-to-avatar, public avatar.
- Règle de consentement par type d'avatar.
- Moteurs de rendu Avatar III / IV / V et leurs paramètres (engine, expressiveness, motion_prompt).
- Coût en crédits par minute selon le moteur.
- Voix disponibles (en particulier le français) et options de clonage / design de voix.
- Prérequis qualité d'une photo source (résolution, cadrage, éclairage, fond).
- Limites techniques : formats acceptés, taille max des assets, ratios vidéo, quotas.
- Cadre légal : base légale biométrique, droit à l'image, opt-out d'entraînement IA, rétention.

### Données à NE PAS collecter

- Toute clé API ou secret (jamais extraire, coller ni écrire en dur).
- Données de compte privées : solde de crédits réel, profil, projets (exigent une authentification, hors Phase 1).
- Identifiants d'avatars privés ou images sources de personnes tierces.
- Transcriptions intégrales des vidéos YouTube et fichiers vidéo.
- Tout contenu derrière un login (app.heygen.com, auth.heygen.com) ou un mur de consentement.

### Méthodes autorisées

- Lecture publique directe des pages de doc en HTTP simple, une requête par page, en markdown.
- Consommation de la spécification OpenAPI publique (external-api.json, openapi.yaml) : une requête couvre tous les schémas.
- Utilisation du fichier llms.txt comme index de découverte, pour cibler les pages utiles avant tout fetch.
- Pour YouTube : API YouTube Data v3 officielle, ou navigation publique manuelle dans le navigateur.
- En Phase 2 seulement : MCP HeyGen via OAuth (déjà connecté au compte schoolsWP), pour constater avatars, looks et voix réels sans manipuler de clé.

### Méthodes interdites

- Scraping page par page agressif de tout le portail de doc (l'index llms.txt et la spec OpenAPI suffisent).
- Crawl récursif d'un domaine entier.
- Appels en direct aux endpoints de génération en Phase 1 (cartographie seulement).
- Contournement d'un login, d'un mur de consentement ou d'un robots.txt.
- Scraping ou téléchargement de transcriptions, sous-titres et fichiers vidéo.
- Réclamer ou écrire en dur une clé API.

### Comment éviter le scraping agressif

- Privilégier les sources structurées (OpenAPI en JSON/YAML) : une requête remplace une cinquantaine de pages HTML.
- Passer par llms.txt pour ne fetcher que les pages réellement utiles au projet.
- Une requête par page cible, espacée. Le service de fetch a signalé un throttling de concurrence (mise en file d'environ 5 secondes) : on temporise entre les appels.

### Comment documenter les résultats

- Pour chaque source : URL demandée, URL réelle, code HTTP, type, statut d'accessibilité, méthode propre.
- Citer la preuve (code HTTP plus extrait factuel verbatim) plutôt que de paraphraser.
- Dater chaque constatation (la doc v1/v2 migre vers v3 jusqu'au 31 octobre 2026).
- Tenir ce document comme index unique, mis à jour à chaque sonde.

### Comment citer les sources

- Toujours donner l'URL réelle quand elle diffère de l'URL demandée.
- Citer la sous-page précise, pas la racine du portail.
- Joindre la preuve : code HTTP plus extrait du contenu.

### Distinguer faits vérifiés, hypothèses, recommandations et points à vérifier

- Fait vérifié : constaté avec preuve directe (HTTP 200 plus extrait verbatim). Voir la section 4.
- Hypothèse : déduction non confirmée par une preuve directe, marquée comme telle.
- Recommandation : choix de méthode proposé pour la suite.
- Point à vérifier : non constatable en lecture publique. Formulation imposée : "À vérifier dans HeyGen ou dans le compte utilisateur."

### Limites de l'analyse

- Tout test réel des avatars, voix, statut et crédits exige une authentification : reporté en Phase 2 via le MCP.
- Les prérequis qualité chiffrés (résolution photo, durée de footage) ne sont pas dans la doc API publique.
- La chaîne YouTube oppose un mur de connexion au fetch direct : l'analyse fine passera par l'API YouTube Data officielle.
- Les chiffres marketing du site officiel ne sont pas des faits techniques : à recouper avec la doc.

---

## 2. Tableau de cartographie des sources

| Source | URL | Type | Priorité | Données à collecter | Méthode autorisée | Limites | Statut |
|---|---|---|---|---|---|---|---|
| Chaîne YouTube HeyGen | youtube.com/@heygen_official (canal UCV0FmNF3iM-022BF1KbVtxA) | Chaîne YouTube officielle | P1 | Positionnement, types d'avatars mis en avant, cas d'usage (formation, marketing, UGC), tutoriels utiles | API YouTube Data v3 (channels, playlists, playlistItems, videos) ou navigation publique manuelle. Pas de transcriptions | Mur "Sign in" au fetch direct, consentement GDPR possible, contenu JS dynamique, robots.txt restrictif | Accessible (via API ou navigation) |
| Doc développeur (guides) | developers.heygen.com/docs/ | Documentation guides | P1 | Auth (clé API et OAuth), avatars, voix, modèles, lipsync, quotas | Fetch public, 1 requête par page, en ciblant via llms.txt | SPA Mintlify (racine pointe vers Quick Start) | Accessible |
| Référence API et OpenAPI | developers.heygen.com/reference/ et developers.heygen.com/openapi/external-api.json | Référence API auto-générée (OpenAPI) | P1 | Schémas exacts des endpoints avatars, voix, vidéo, assets, formats entrée/sortie | Lire la spec OpenAPI (1 requête) puis pages .md ciblées | Racine SPA = un seul endpoint affiché, throttling du fetch | Accessible |
| Doc création d'avatar | developers.heygen.com/docs/create-avatar | Doc avatar et consentement | P1 | 3 modes (digital twin, photo, prompt), règle de consentement, flux de consentement | Fetch public, 1 requête markdown | URL demandée (docs.heygen.com/docs/create-an-avatar) en 404 ; prérequis qualité chiffrés absents | Partiel |
| Centre d'aide | help.heygen.com/en/ | Guides utilisateurs (Intercom) | P2 | Prérequis qualité photo (résolution, cadrage, éclairage), raisons de rejet d'une vidéo | Fetch ciblé d'articles (collection Avatars, article "Photo Avatars") | Anglais uniquement, rendu dynamique Intercom | Accessible |
| Changelog API | developers.heygen.com/changelog | Changelog développeur | P2 | Moteurs Avatar IV / V, paramètres engine, expressiveness, motion_prompt, ratios, dépréciation v1/v2 | Fetch public, 1 requête, ou flux RSS officiel | Ancienne URL docs.heygen.com/changelog en 404 ; orienté API | Accessible |
| Site officiel | heygen.com | Site marketing | P3 | Taxonomie des avatars, conformité affichée (GDPR, SOC 2, AI Act), locales FR | Navigation publique, à recouper avec la doc | Contenu marketing non probant, le réel exige un login | Accessible (à recouper) |
| Pricing et API pricing | heygen.com/pricing et heygen.com/api-pricing | Pages tarifs | P2 | Coût en crédits par minute par moteur, plans, rollover, séparation crédits plan / crédits API | Fetch public, 1 requête par page | La page api-pricing reste à fetcher en Phase 2 | Accessible |
| Pages légales | heygen.com/privacy, heygen.com/biometric-privacy-notice, Terms, heygen.com/moderation-policy | Pages légales | P1 | Consentement biométrique (Art. 9 GDPR), droit à l'image, opt-out entraînement IA, rétention, usages interdits | Fetch public, 1 requête par page | /policy redirige vers /privacy ; Biometric Notice et Terms à fetcher à part ; page "AI ethics" dédiée à vérifier | Accessible |
| MCP HeyGen (compte schoolsWP) | OAuth via le connecteur MCP heygen déjà branché | Connecteur MCP (compte) | P1 (Phase 2) | Avatars, looks et voix réels du compte, solde de crédits, plan | OAuth via le MCP, sans manipuler de clé | Réservé à la Phase 2, compte connecté requis | À vérifier (Phase 2) |

---

## 3. Sources bloquées ou à vérifier

- URL P1 demandée docs.heygen.com/docs/create-an-avatar : HTTP 404 (migration v1/v2 vers v3, maintenue jusqu'au 31 octobre 2026). Repli propre vérifié : developers.heygen.com/docs/create-avatar (HTTP 200, sans login).
- Ancienne URL changelog docs.heygen.com/changelog : HTTP 404. Repli : developers.heygen.com/changelog (HTTP 200).
- Prérequis qualité chiffrés (résolution photo minimale, durée et format du footage, exigences du selfie) : absents de la doc API. Repli : Centre d'aide, article "How to Get Started with Photo Avatars". Si toujours introuvable : À vérifier dans HeyGen ou dans le compte utilisateur.
- Inventaire réel des avatars, looks et voix FR du compte schoolsWP : non constatable en lecture publique. Repli : Phase 2 via le MCP HeyGen en OAuth.
- Solde de crédits du plan contre crédits API, et fonctionnement exact de l'enveloppe API : le pricing du plan pointe vers une page API pricing distincte (heygen.com/api-pricing), à fetcher en Phase 2. À vérifier dans HeyGen ou dans le compte utilisateur.
- Page "AI ethics" ou Acceptable Use dédiée : non référencée depuis la Privacy. Probablement dans les Terms. À vérifier.
- Terms of Service et Biometric Information Privacy Notice : référencés par lien depuis la Privacy, à fetcher séparément en Phase 2.

---

## 4. Faits vérifiés notables, déjà constatés en Phase 1 (sourcés)

Ces éléments sont des faits constatés avec preuve directe pendant la cartographie. Ils orientent les phases suivantes, mais ne remplacent pas l'analyse complète des Phases 2 à 5.

- Trois modes de création d'avatar via POST /v3/avatars, distingués par le champ "type" : digital_twin (depuis une vidéo footage), photo (depuis une seule photo, sans enregistrement vidéo), prompt (personnage synthétique). Source : developers.heygen.com/docs/create-avatar.
- Le consentement est requis uniquement pour digital_twin. Les avatars photo et prompt n'exigent pas de consentement côté flux API. Point central pour le droit à l'image. Source : developers.heygen.com/docs/create-avatar.
- L'avatar à partir d'un visage est traité comme une donnée biométrique : base légale = consentement explicite (Art. 9(2)(a) GDPR), via une action affirmative claire avant toute extraction, retrait possible via privacy@heygen.com. Sources : heygen.com/privacy (section User Input) et la Biometric Information Privacy Notice référencée.
- La création d'un avatar à l'effigie d'une autre personne sans son consentement explicite est interdite. Source : heygen.com/moderation-policy.
- Deux moteurs de rendu récents : Avatar IV (moteur par défaut) et Avatar V (présenté comme le plus réaliste). Parité tarifaire depuis le 12 mai 2026. Le champ engine sur POST /v3/videos permet de choisir ; expressiveness et motion_prompt sont réservés à Avatar IV. Source : developers.heygen.com/changelog.
- Coût en crédits : Avatar IV et V à 20 crédits par minute, Avatar III à 3 crédits par minute, traduction vidéo avec lipsync à 5 crédits par minute. Source : heygen.com/pricing (FAQ crédits).
- Plan Creator = 600 crédits par mois (29 dollars par mois, 24 en annuel). L'accès API est présenté comme une enveloppe distincte, via un lien dédié vers heygen.com/api-pricing. Cela confirme le blocage rencontré dans le projet (crédits du plan non dépensables par l'API REST). Source : heygen.com/pricing.
- Ratios vidéo disponibles : 16:9, 9:16, 1:1, 4:5, 5:4 et auto (depuis le 25 mai 2026). Utile pour les formats courts. Source : developers.heygen.com/changelog.
- API v3 active ; endpoints v1 et v2 supportés jusqu'au 31 octobre 2026. Sources : developers.heygen.com/docs/ et changelog.
- Conformité affichée : GDPR, SOC 2 Type II, CCPA, AI Act, DPF. Locale FR-FR présente. Source : heygen.com (à recouper, contenu marketing).
- Voie technique recommandée par HeyGen pour un agent : OAuth via MCP, sans manipuler de clé. Cohérent avec le connecteur MCP déjà branché dans le projet. Source : developers.heygen.com (doc For AI Agents).

---

## 5. Hypothèses (à confirmer en Phase 2 et 5)

- Pour un avatar schoolsWP qui montre le vrai visage de Michaël, le choix se jouera entre digital_twin (réalisme maximal, mais consentement requis et footage vidéo) et photo avatar (plus rapide, une seule photo). Arbitrage prévu en Phase 5. Hypothèse, non tranchée.
- Avatar V donnerait un meilleur réalisme qu'Avatar IV : c'est une annonce marketing, à recouper avec la matrice des modèles (models.md) et un test réel dans le compte. Hypothèse.

---

## 6. Prochaine étape

Phase 1 terminée et documentée. Avant de lancer la Phase 2 (analyse de la chaîne YouTube HeyGen), j'attends ta validation sur :

1. Le périmètre des sources (rien à ajouter ou retirer ?).
2. La méthode pour YouTube : API YouTube Data v3 officielle (recommandée) ou navigation publique manuelle.
3. L'autorisation d'utiliser le MCP HeyGen en Phase 2 pour constater tes avatars et voix réels du compte schoolsWP.

Aucune action de Phase 2 ne sera lancée sans ton feu vert.

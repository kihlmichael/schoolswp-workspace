# Plan de formation — Maitriser Easy Content Linker

**Version** : 1.0
**Date** : 2026-03-23
**Auteur** : schoolsWP (Michael KIHL)
**Plateforme** : TutorLMS Pro
**Format** : Videos HeyGen + voix ElevenLabs
**Langue** : Francais (tutoiement)
**Modele** : 100% gratuit (lead magnet autorite maillage interne)
**Plugin** : Easy Content Linker par Baptiste Guiraud

## Vue d'ensemble

| Module | Titre | Lecons | Duree | Niveau |
|--------|-------|--------|-------|--------|
| M1 | Le maillage interne et Easy Content Linker | 4 | 20 min | Debutant |
| M2 | Installation et connexion API | 4 | 22 min | Debutant |
| M3 | Configuration strategique | 5 | 30 min | Intermediaire |
| M4 | Premier maillage complet | 4 | 25 min | Intermediaire |
| M5 | Pages strategiques et exclusions | 4 | 25 min | Intermediaire |
| M6 | Audit, optimisation et maintenance | 4 | 25 min | Intermediaire |

**Total** : 25 lecons, ~2h27 de contenu

---

## Module 1 — Le maillage interne et Easy Content Linker

**Objectif pedagogique** : Tu comprends pourquoi le maillage interne est un levier SEO majeur, ce que fait Easy Content Linker, et comment il se distingue des alternatives.
**Prerequis** : Un site WordPress avec 20+ articles publies
**Duree estimee** : 20 minutes
**Niveau** : Debutant

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|-----------------|---------------|
| 1.1 | Pourquoi le maillage interne change ton SEO | 5 min | Video | Impact du maillage : jus de lien, crawl budget, UX, temps passe sur le site | — (theorie) |
| 1.2 | Ce que fait Easy Content Linker (et ce qu'il ne fait pas) | 5 min | Video | Architecture reversible, embeddings + GPT, injection dynamique sans modifier la BDD | — (theorie) |
| 1.3 | Lite vs Pro : le comparatif honnete pour choisir | 5 min | Video | Differences concretes (recommandations manuelles vs injection automatique), criteres de decision | Evaluer son besoin |
| 1.4 | Quiz — Valide tes acquis M1 | 5 min | Quiz | — | 5 questions QCM |

### Points cles a couvrir
- Le maillage interne n'est pas juste "ajouter des liens" — c'est une architecture de contenu
- Difference entre maillage manuel (2h/article) vs automatise (2 min) avec chiffres concrets
- Architecture reversible d'ECL : les liens disparaissent si tu desactives le plugin — zero risque
- ECL n'est pas un outil de creation de contenu — il optimise la distribution des liens existants
- Lite suffit pour decouvrir et tester, Pro devient necessaire a 50+ articles pour l'automatisation

### Angle schoolsWP
- Comparaison honnete avec les alternatives (Link Whisper, Internal Link Juicer) — sans denigrer, en montrant les differences de philosophie (IA semantique vs regles manuelles)
- Demo sur un site reel : avant/apres maillage sur un cluster d'articles
- Le maillage interne dans la strategie cocons/piliers schoolsWP

### Quiz M1 — 5 questions

1. **Quel est le principal avantage du maillage interne pour le SEO ?**
   a) Augmenter le nombre de pages indexees
   b) Distribuer le jus de lien vers les pages strategiques ✓
   c) Reduire le temps de chargement
   d) Ameliorer la securite du site

2. **Que se passe-t-il si tu desactives Easy Content Linker ?**
   a) Les liens restent dans la base de donnees
   b) Les liens disparaissent immediatement car ils sont injectes dynamiquement ✓
   c) Les liens deviennent des erreurs 404
   d) Il faut supprimer manuellement chaque lien

3. **Quelle technologie ECL utilise-t-il pour comprendre le contenu de tes articles ?**
   a) Analyse de mots-cles par densite
   b) Embeddings OpenAI (analyse semantique) ✓
   c) Expressions regulieres
   d) Scraping Google

4. **A partir de combien d'articles la version Pro devient-elle vraiment utile ?**
   a) 5 articles
   b) 10 articles
   c) 50+ articles (l'injection automatique fait gagner du temps) ✓
   d) 500+ articles uniquement

5. **Quelle est la difference principale entre ECL Lite et Pro ?**
   a) Lite est en anglais, Pro en francais
   b) Lite genere des recommandations manuelles, Pro injecte les liens automatiquement ✓
   c) Lite ne supporte pas les embeddings
   d) Pro fonctionne sans cle API OpenAI

---

## Module 2 — Installation et connexion API

**Objectif pedagogique** : Tu as installe ECL, cree et connecte ta cle API OpenAI, choisi le bon modele GPT et verifie que tout fonctionne.
**Prerequis** : M1
**Duree estimee** : 22 minutes
**Niveau** : Debutant

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|-----------------|---------------|
| 2.1 | Installe Easy Content Linker sur ton site | 4 min | Video/Demo | Installation via zip Freemius ou WordPress.org (Lite), activation, menu Content Linker | Installer et activer ECL |
| 2.2 | Cree ta cle API OpenAI et configure ton budget | 7 min | Video/Demo | Creer un compte OpenAI, generer une cle API, configurer les limites de budget, activer les billing alerts | Creer la cle + configurer le budget |
| 2.3 | Connecte la cle API et choisis le bon modele | 6 min | Video/Demo | Coller la cle, tester la connexion, choisir entre gpt-4o et gpt-5.2, choisir le modele d'embeddings | Connecter et tester la cle API |
| 2.4 | Quiz — Valide tes acquis M2 | 5 min | Quiz | — | 5 questions QCM |

### Points cles a couvrir
- Installation Lite (WordPress.org, 1 clic) vs Pro (zip Freemius, upload manuel)
- Compte OpenAI : navigation dans platform.openai.com (pas dans ChatGPT — erreur frequente)
- Securite de la cle API : ne jamais la partager, la stocker uniquement dans le plugin
- Budget API : configurer un plafond mensuel (ex: 10€) avant de lancer quoi que ce soit
- Billing alerts : recevoir un email avant d'atteindre la limite
- Choix du modele : gpt-4o = meilleur rapport qualite/prix (recommande), gpt-5.2 = precision maximale (cout x2-3)
- Embeddings : text-embedding-3-small suffit pour 90% des sites, large pour les sites 500+ articles multilingues
- Diagnostic si echec connexion : cle invalide, quota epuise, rate limit, erreur reseau

### Angle schoolsWP
- Demo sur le site schoolsWP reel (pas un site vierge)
- Astuce budget : commencer avec 5€ de credit, ca suffit pour 50-150 liens selon le site
- Erreurs courantes au premier lancement (cle ChatGPT vs cle API, compte sans moyen de paiement)

### Quiz M2 — 5 questions

1. **Ou trouves-tu ta cle API OpenAI ?**
   a) Dans l'interface ChatGPT
   b) Dans platform.openai.com → API Keys ✓
   c) Dans les reglages WordPress
   d) Dans le fichier wp-config.php

2. **Quel modele GPT est recommande pour ECL (meilleur rapport qualite/prix) ?**
   a) gpt-3.5-turbo
   b) gpt-4o ✓
   c) gpt-5.2
   d) text-embedding-3-large

3. **Pourquoi faut-il configurer un budget plafond dans OpenAI avant de lancer ECL ?**
   a) Pour que le plugin fonctionne plus vite
   b) Pour eviter une facture surprise si le traitement genere beaucoup d'appels ✓
   c) Pour debloquer les modeles premium
   d) Ce n'est pas necessaire

4. **Le modele text-embedding-3-small est utilise pour...**
   a) Generer les ancres de liens
   b) Analyser le contenu semantique de chaque article (embeddings) ✓
   c) Traduire le contenu en plusieurs langues
   d) Compresser les images du site

5. **Ta cle API commence par "sk-" mais le test echoue. Que verifies-tu en premier ?**
   a) La version de WordPress
   b) Que le compte OpenAI a un moyen de paiement actif et du credit disponible ✓
   c) Que le plugin est en version Pro
   d) Que le theme est compatible

---

## Module 3 — Configuration strategique

**Objectif pedagogique** : Tu as configure ECL de maniere strategique : types de contenu, seuils de similarite adaptes a ton site, categories, mode silo. Tu comprends l'impact de chaque reglage.
**Prerequis** : M2
**Duree estimee** : 30 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|-----------------|---------------|
| 3.1 | Configure les types de contenu source et cible | 6 min | Video/Demo | Choisir quels contenus generent des liens (source) et lesquels en recoivent (cible), quand ajouter les CPT et les pages | Configurer source/cible dans les reglages |
| 3.2 | Regle les seuils de similarite pour ton site | 7 min | Video/Demo | Comprendre les scores (0.65-0.95), ajuster le seuil minimum selon le type de site, interpreter l'echelle | Ajuster les seuils min/max |
| 3.3 | Configure les limites de liens et le mode silo | 7 min | Video/Demo | Max liens sortants/entrants par article, mode silo par categorie (quand l'activer), impact sur la distribution | Configurer les limites et le silo |
| 3.4 | Choisis les categories a exclure (et pourquoi) | 5 min | Video/Demo | Criteres d'exclusion (categories non-SEO, contenu temporaire, legal), configuration des exclusions | Exclure les categories non pertinentes |
| 3.5 | Quiz — Valide tes acquis M3 | 5 min | Quiz | — | 5 questions QCM |

### Points cles a couvrir
- **Source vs cible** : par defaut, seuls les articles sont source. Ajouter les pages en cible si elles font partie de la strategie SEO (pillar pages). Ne pas ajouter le panier WooCommerce ou les CGV.
- **Seuils de similarite** :
  - Blog generaliste (sujets varies) : baisser le minimum a 0.65 pour trouver des connexions
  - Blog de niche (sujets concentres) : garder 0.70 voire monter a 0.75 pour eviter les liens trop generiques
  - Seuil max 0.95 : ne pas toucher sauf si tu as des pages ville / fiches produit similaires (whitelist)
- **Limites de liens** :
  - 5 sortants/article = bon defaut pour la plupart des sites
  - 20 entrants/article = genereux, baisser a 10 si tu veux concentrer le jus
  - Sur un petit site (30-50 articles) : baisser a 3 sortants pour eviter la sur-optimisation
- **Mode silo** : activer si tes categories correspondent a des cocons semantiques. Desactiver si tes categories sont mal organisees (il vaut mieux nettoyer d'abord).
- **Categories a exclure** : actus/news (contenu perissable), non-classe, categories purement techniques

### Angle schoolsWP
- Configuration recommandee pour un site de type "blog WordPress business" (le profil type schoolsWP)
- Strategie silo alignee sur les piliers schoolsWP (LMS, CRM, SEO, automatisation)
- Cas concret : configuration pour un site avec 5 categories bien definies vs un site avec 20 categories en vrac

### Quiz M3 — 5 questions

1. **Par defaut, quel type de contenu genere des liens dans ECL ?**
   a) Les pages
   b) Les articles (posts) ✓
   c) Les produits WooCommerce
   d) Tous les types de contenu

2. **Tu as un blog generaliste avec des sujets varies. Quel seuil minimum de similarite recommandes-tu ?**
   a) 0.50 (trop bas, liens non pertinents)
   b) 0.65 (permet de trouver des connexions entre sujets varies) ✓
   c) 0.85 (trop strict, peu de liens generes)
   d) 0.95 (quasi identiques uniquement)

3. **Le mode silo par categorie est utile quand...**
   a) Tes categories correspondent a des cocons semantiques bien definis ✓
   b) Tu as seulement 2 categories
   c) Tu veux que tous les articles se lient entre eux
   d) Tu utilises WooCommerce

4. **Quel est le risque de mettre 10 liens sortants par article sur un site de 30 articles ?**
   a) Le site va planter
   b) Sur-optimisation : trop de liens diluent le jus et semblent non naturels ✓
   c) Aucun risque
   d) Google va penaliser le domaine

5. **Quelles categories dois-tu exclure en priorite ?**
   a) Les categories avec le plus d'articles
   b) Les categories de contenu perissable, non-classe et purement technique ✓
   c) Les categories les plus populaires
   d) Aucune — il faut toujours tout inclure

---

## Module 4 — Premier maillage complet

**Objectif pedagogique** : Tu as lance ton premier traitement complet (embeddings + liens), tu sais suivre l'avancement, interpreter les resultats et corriger les problemes courants.
**Prerequis** : M3
**Duree estimee** : 25 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|-----------------|---------------|
| 4.1 | Lance le traitement : embeddings puis liens | 7 min | Video/Demo | Les 2 phases du bulk (embeddings = empreinte semantique, liens = matching + ancres), garder l'onglet ouvert, temps estime selon le nombre d'articles | Lancer le traitement complet |
| 4.2 | Explore l'historique et juge la qualite des liens | 7 min | Video/Demo | Lire l'historique (source, cible, ancre, score), reperer les bons et mauvais liens, criteres de qualite | Parcourir et evaluer 10 liens |
| 4.3 | Corrige les problemes : ancres faibles, liens non pertinents, erreurs | 6 min | Video/Demo | Supprimer un lien (Revert), comprendre le rapport d'exclusions, diagnostiquer un traitement interrompu | Supprimer 2-3 liens non pertinents |
| 4.4 | Quiz — Valide tes acquis M4 | 5 min | Quiz | — | 5 questions QCM |

### Points cles a couvrir
- **Phase 1 (embeddings)** : se fait une seule fois par article. Si tu ajoutes un article plus tard, seul le nouveau sera analyse. Temps : ~1-2 sec/article.
- **Phase 2 (liens)** : GPT choisit les ancres. C'est la que les appels API coutent le plus. Temps : ~3-5 sec/lien.
- **Estimations de temps** :
  - 50 articles : ~5-10 minutes (embeddings) + 10-15 minutes (liens)
  - 200 articles : ~15-20 minutes (embeddings) + 30-45 minutes (liens)
  - 500 articles : decoupe par categorie recommandee
- **Onglet ouvert** : le traitement se fait cote navigateur. Si l'onglet ferme, le traitement s'arrete. On peut relancer — les embeddings deja calcules ne sont pas recalcules.
- **Qualite des liens** : un bon lien = ancre naturelle (phrase existante dans le texte) + score > 0.70 + article cible pertinent. Un mauvais lien = ancre forcee, score < 0.65, cible hors sujet.
- **Rapport d'exclusions** : comprendre chaque raison (similarite trop basse, trop haute, max liens atteint, noindex, canonical different)

### Angle schoolsWP
- Workflow "premier maillage" de A a Z sur un cluster reel (ex: 15 articles du pilier LMS)
- Avant/apres : montrer les liens generes dans un article publie (vue front-end)
- Cout reel constate pour 50, 100 et 200 articles (chiffres schoolsWP)

### Quiz M4 — 5 questions

1. **Les embeddings sont recalcules a chaque traitement ?**
   a) Oui, a chaque lancement
   b) Non, ils sont calcules une seule fois par article (sauf si le contenu change) ✓
   c) Oui, mais seulement pour les articles modifies
   d) Non, ils ne sont jamais recalcules

2. **Que se passe-t-il si tu fermes l'onglet pendant le traitement bulk ?**
   a) Le traitement continue en arriere-plan
   b) Le traitement s'arrete, mais les embeddings deja calcules sont conserves ✓
   c) Tous les liens generes sont perdus
   d) Le plugin plante

3. **Un lien avec un score de similarite de 0.58 — tu fais quoi ?**
   a) Tu le gardes, c'est correct
   b) Tu le supprimes via Revert — le score est trop bas pour etre pertinent ✓
   c) Tu augmentes le seuil minimum a 0.95
   d) Tu contactes le support

4. **Dans le rapport d'exclusions, "Max incoming links reached" signifie...**
   a) L'article source a trop de liens sortants
   b) L'article cible a deja atteint sa limite de liens entrants ✓
   c) Le budget API est epuise
   d) Le plugin a un bug

5. **Pour un site de 500 articles, quelle approche recommandes-tu ?**
   a) Tout traiter en une seule fois
   b) Decouper par categorie/pilier et traiter progressivement ✓
   c) Ne traiter que les 50 derniers articles
   d) Attendre une mise a jour du plugin

---

## Module 5 — Pages strategiques et exclusions

**Objectif pedagogique** : Tu sais booster tes pages les plus importantes, configurer des ancres personnalisees, et exclure chirurgicalement les contenus qui ne doivent pas participer au maillage.
**Prerequis** : M4
**Duree estimee** : 25 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|-----------------|---------------|
| 5.1 | Identifie tes pages strategiques (pillar, money, landing) | 6 min | Video/Demo | Criteres pour identifier les pages a booster : pages piliers (contenu long, autorite), money pages (conversion/affiliation), landing pages (capture) | Lister ses 5-10 pages strategiques |
| 5.2 | Configure les bonus et les ancres personnalisees | 7 min | Video/Demo | Attribuer les niveaux de boost (+10/25/50%), creer jusqu'a 5 ancres personnalisees par page, logique de reservation | Configurer 3 pages strategiques |
| 5.3 | Maitrise les exclusions granulaires par article | 7 min | Video/Demo | Les 3 options metabox (exclure totalement, ne pas generer depuis, ne pas recevoir), cas d'usage : article sponsorise, page de vente isolee, contenu temporaire | Configurer les exclusions sur 2-3 articles |
| 5.4 | Quiz — Valide tes acquis M5 | 5 min | Quiz | — | 5 questions QCM |

### Points cles a couvrir
- **Identifier les pages strategiques** :
  - Pillar pages (contenu long 2000+ mots, couvre un sujet en profondeur) → +50%
  - Money pages (comparatifs, avis, pages avec affiliation) → +25%
  - Pages secondaires importantes (guides pratiques cles) → +10%
  - Ne pas tout booster — si tout est prioritaire, rien ne l'est
- **Ancres personnalisees** : choisir des ancres qui correspondent a des requetes reelles (mots-cles cibles de la page). Ex: pour une page "meilleur LMS WordPress", les ancres pourraient etre "choisir un LMS WordPress", "comparatif LMS WordPress", "plugin LMS pour WordPress".
- **Reservation automatique** : une ancre attribuee a une page strategique ne sera jamais utilisee pour une autre page. Avantage : coherence du maillage.
- **Exclusions granulaires (v2.12.0+)** :
  - Article sponsorise → "Ne pas recevoir de liens" (tu ne veux pas envoyer du jus vers du contenu sponsorise)
  - Landing page avec un seul CTA → "Ne pas generer de liens depuis" (tu ne veux pas distraire le visiteur)
  - Page en cours de redaction → "Exclure completement" (temporaire)
- **Detection doublons** : si ECL detecte des articles a >95% de similarite, c'est le moment de fusionner ou de differencier ces contenus

### Angle schoolsWP
- Strategie de boost alignee sur la methode cocons schoolsWP : pages piliers a +50%, satellites a 0% (elles beneficient naturellement du maillage)
- Comment choisir les ancres personnalisees en s'appuyant sur les mots-cles RankMath (complementarite ECL + RankMath)
- Cas reel : configuration des pages strategiques sur le site schoolsWP

### Quiz M5 — 5 questions

1. **Quel niveau de boost attribues-tu a une page pilier (contenu long, autorite) ?**
   a) +10% (trop faible pour une page pilier)
   b) +25%
   c) +50% ✓
   d) +100%

2. **Combien d'ancres personnalisees peux-tu definir par page strategique ?**
   a) 1
   b) 3
   c) 5 ✓
   d) Illimite

3. **Tu as un article sponsorise — quelle option d'exclusion choisis-tu ?**
   a) Exclure completement
   b) Ne pas generer de liens depuis cet article
   c) Ne pas recevoir de liens vers cet article ✓
   d) Aucune exclusion

4. **ECL detecte 2 articles a 96% de similarite. Que fais-tu ?**
   a) Tu les ignores
   b) Tu analyses les 2 articles pour les fusionner ou les differencier ✓
   c) Tu supprimes le plus ancien
   d) Tu baisses le seuil maximum a 0.90

5. **Pourquoi ne faut-il pas booster toutes ses pages a +50% ?**
   a) Ca coute plus cher en API
   b) Si tout est prioritaire, la distribution de liens redevient uniforme — le boost perd son effet ✓
   c) Le plugin refuse
   d) Google penalise les sites avec trop de boost

---

## Module 6 — Audit, optimisation et maintenance

**Objectif pedagogique** : Tu sais auditer ton maillage, exploiter l'export CSV, maintenir ECL dans le temps, et mesurer l'impact SEO de ton maillage.
**Prerequis** : M5
**Duree estimee** : 25 minutes
**Niveau** : Intermediaire

### Lecons

| # | Titre de la lecon | Duree | Type | Ce qu'on apprend | Ce qu'on fait |
|---|-------------------|-------|------|-----------------|---------------|
| 6.1 | Audite ton maillage avec l'export CSV | 7 min | Video/Demo | Exporter l'historique complet, ouvrir dans Google Sheets, analyser la distribution (articles sur-lies vs sous-lies), identifier les trous | Exporter et analyser le CSV |
| 6.2 | Optimise : ajuste les reglages apres le premier maillage | 6 min | Video/Demo | Affiner les seuils apres analyse, ajouter/retirer des exclusions, relancer un traitement cible, notification flush | Ajuster 2-3 reglages et relancer |
| 6.3 | Maintenance : nouveaux articles, mises a jour, routine mensuelle | 7 min | Video/Demo | Quand relancer le traitement (nouvel article, modification majeure), routine mensuelle recommandee, vider le cache apres modif liens, cout de maintenance | Definir sa routine mensuelle |
| 6.4 | Quiz final — Valide tes acquis formation complete | 5 min | Quiz | — | 10 questions QCM (recapitulatif tous modules) |

### Points cles a couvrir
- **Audit CSV** :
  - Ouvrir dans Google Sheets ou Excel
  - Trier par "liens entrants" pour trouver les pages sur-liees (trop de liens = dilution)
  - Trier par "liens sortants = 0" pour trouver les articles orphelins (pas de lien genere)
  - Verifier la coherence des ancres (naturelles, variees, pas de bourrage de mots-cles)
- **Optimisation post-premier-maillage** :
  - Si trop peu de liens : baisser le seuil minimum (0.70 → 0.65)
  - Si trop de liens non pertinents : monter le seuil minimum (0.70 → 0.75)
  - Si certaines categories polluent : les exclure
  - Notification flush : quand tu changes un reglage structurel, ECL propose de nettoyer les liens obsoletes
- **Maintenance mensuelle** :
  - Publier un article → relancer le traitement (seulement le nouvel article est analyse pour les embeddings)
  - Modifier un article en profondeur → supprimer ses liens et relancer
  - 1x/mois : verifier l'historique, supprimer les liens douteux, exporter le CSV pour suivi
  - Cout maintenance : quasi nul (les embeddings existants ne sont pas recalcules)
- **Mesurer l'impact SEO** :
  - Google Search Console : suivre les impressions/clics des pages boostees (avant/apres maillage)
  - Screaming Frog ou Ahrefs : verifier la profondeur de crawl et la distribution des liens internes
  - Indicateur simple : nombre de pages indexees dans Google (site:monsite.com)

### Angle schoolsWP
- Template Google Sheets d'audit maillage (fourni en ressource telecharge de la formation)
- Routine mensuelle schoolsWP : publier → mailler → verifier → ajuster
- Montrer l'evolution GSC reelle apres 1 mois de maillage ECL sur schoolsWP
- Complementarite avec RankMath : ECL gere les liens internes, RankMath gere le SEO on-page

### Quiz final M6 — 10 questions (recapitulatif)

1. **Easy Content Linker modifie-t-il le contenu de tes articles en base de donnees ?**
   a) Oui, il insere les liens directement dans le contenu
   b) Non, les liens sont injectes dynamiquement a l'affichage ✓
   c) Oui, mais seulement pour les ancres personnalisees
   d) Ca depend de la version (Lite vs Pro)

2. **Quel est le cout estime pour generer 100 liens avec ECL ?**
   a) Gratuit
   b) 3 a 8 euros ✓
   c) 50 a 100 euros
   d) Ca depend de l'hebergeur

3. **Le pre-scan intelligent permet de...**
   a) Accelerer le chargement des pages
   b) Reduire de 20 a 40% les appels API en verifiant les ancres avant d'appeler GPT ✓
   c) Scanner les sites concurrents
   d) Detecter les virus

4. **Ton site a 200 articles et tu viens d'en publier 5 nouveaux. Que fais-tu ?**
   a) Tu relances le traitement complet sur les 205 articles
   b) Tu relances le traitement — seuls les 5 nouveaux articles seront analyses pour les embeddings ✓
   c) Tu desactives puis reactives le plugin
   d) Tu attends que le plugin detecte automatiquement les nouveaux articles

5. **Un article a 0 lien sortant dans l'export CSV. Que fais-tu ?**
   a) Rien, c'est normal
   b) Tu verifies s'il est exclu, si le seuil est trop haut, ou s'il est trop different des autres articles ✓
   c) Tu le supprimes
   d) Tu ajoutes des liens manuellement sans verifier

6. **Le mode silo par categorie est utile quand...**
   a) Tu veux que tous les articles se lient entre eux
   b) Tes categories correspondent a des cocons semantiques bien definis ✓
   c) Tu n'as qu'une seule categorie
   d) Tu utilises la version Lite

7. **Quelle est la routine mensuelle recommandee avec ECL ?**
   a) Desinstaller et reinstaller le plugin
   b) Verifier l'historique, supprimer les liens douteux, exporter le CSV pour suivi ✓
   c) Recalculer tous les embeddings
   d) Changer de modele GPT chaque mois

8. **Tu constates que trop de liens generes sont non pertinents. Que fais-tu ?**
   a) Tu desactives le plugin
   b) Tu montes le seuil minimum de similarite (ex: 0.70 → 0.75) ✓
   c) Tu passes en mode silo
   d) Tu changes de modele GPT

9. **Pourquoi vider le cache apres avoir modifie des liens dans ECL ?**
   a) Pour que le plugin fonctionne plus vite
   b) Pour que les pages cachees affichent les liens mis a jour ✓
   c) Pour reduire les couts API
   d) Ce n'est pas necessaire

10. **Quel outil Google te permet de mesurer l'impact SEO de ton maillage ?**
    a) Google Analytics uniquement
    b) Google Search Console (impressions/clics des pages boostees) ✓
    c) Google Ads
    d) Google Trends

---

## Ressources complementaires (a fournir avec la formation)

| Ressource | Format | Description |
|-----------|--------|-------------|
| Checklist configuration ECL | PDF | Les 12 reglages a verifier avant de lancer le premier traitement |
| Template audit maillage | Google Sheets | Tableau d'analyse de l'export CSV (formules pre-configurees) |
| Guide budget API OpenAI | PDF | Estimation de cout selon le nombre d'articles + configuration billing alerts |
| Arbre de decision Lite vs Pro | Image | Flowchart pour choisir la bonne version |

---

## Parcours recommande

```
M1 (20 min) → M2 (22 min) → M3 (30 min) → PAUSE : lancer le premier traitement
→ M4 (25 min) → M5 (25 min) → M6 (25 min) → Formation terminee
```

**Duree totale** : 2h27
**Exercice fil rouge** : a la fin de la formation, l'apprenant a un maillage interne fonctionnel et audite sur son propre site WordPress.

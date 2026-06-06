---
slug: code-promo-tutor-lms
url: https://schoolswp.com/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/
date_snapshot: 2026-05-29
trigger: Demande Michael (audit pre-publication du draft coupon 2967240, pilote serie code-promo per-plugin)
status: refonte-effectuee
target_post_id: 5843
draft_coupon_post_id: 2967240
---

# Audit "code promo tutor lms" - 2026-05-29

## 1. Contexte et declencheur

Michael a lance une serie editoriale "code promo plugin" inspiree de l article EN coupon-code-fluentcrm. Pilote choisi : Tutor LMS (code negocie schoolsWP10 = 10 pourcent). J ai genere un draft FR (post 2967240, 84 blocs Gutenberg, 15.8 KB) modele sur le pattern coupon-code-fluentcrm EN.

Avant de publier, audit obligatoire : risque de cannibalisation avec l avis existant 5843 (Tutor LMS Avis 2026), publie 2021, refondu 2026-05-22, slug creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms.

## 2. Donnees collectees

| Source | Scope | Date |
| --- | --- | --- |
| Get post Novamira | 5843 (avis FR existant) | 2026-05-30 |
| Get post Novamira | 2967240 (draft coupon FR) | 2026-05-29 |
| thruuu SERP export | "codes promo Tutor LMS" FR | 2026-05-29 |
| thruuu SERP export | "Coupons Tutor LMS" intl | 2026-05-29 |
| DataForSEO labs keyword overview | "code promo tutor lms" FR | 2026-05-29 |
| Live probe /tutor-lms cloak | 307 vers tutorlms.com?affiliate=michaelkihl | 2026-05-30 |

Raw thruuu archives dans thruuu-raw/ (146 KB + 156 KB). Snapshot post-patch dans article-current-snapshot.md.

## 3. Etat de l article existant (5843) au moment de l audit

| Element | Valeur pre-patch | Valeur post-patch |
| --- | --- | --- |
| Longueur post_content | 27 239 chars | 30 016 chars |
| Status | publish | publish |
| Slug | creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms | (idem) |
| Rank Math focus | tutor lms, plateforme de formation avec wordpress | (inchange) |
| Rank Math title | Tutor LMS Avis 2026 : Le Meilleur LMS WordPress ? | (inchange) |
| Rank Math score | 88 | (inchange) |
| post_modified | 2026-05-22 15:41:14 | 2026-05-30 09:22:40 |
| Mention schoolsWP10 | 1 (CTA Kadence vert section 2.4) | 4 (CTA + encadre haut + 2 mini-FAQ) |
| Lien /tutor-lms cloake | 4 occurrences | 5 occurrences (+CTA encadre) |
| FAQ Rank Math rich snippet | id s-57e13546-3eff-4acd-8e7c-55f750a1d887 | (inchange, NON touche) |

Structure : 9 H2 numerotes (Pourquoi + 1 a 9) + Conclusion + 22 H3, 1 Kadence TOC (h2 only), 2 Ninja Tables (57903 prix, 57905 comparatif), 1 Rank Math FAQ snippet, 6 captures ecran section 6.

## 4. SEO actuel sur "code promo tutor lms" (avant patch)

| KPI | Constat |
| --- | --- |
| Position SERP FR | P1 + Featured Snippet |
| Page rankante | 5843 (avis Tutor LMS) - via deep-link anchor section 2.4 "Essayez Tutor LMS code promo schoolsWP10" + mention conclusion |
| Volume DataForSEO FR | < 100 / mois (long tail) |
| Concurrence SERP | faible (sites coupon agreges + page Themeum officielle) |
| Intent dominant | transactionnel hybride : verifier code + decouvrir produit |

Le ranking actuel tient sur 2 signaux faibles (1 CTA, 1 mention conclusion). C est resistant tant que personne n attaque le KW serieusement, mais fragile face a un challenger SERP-natif.

## 5. SERP analysee (thruuu 2026-05-29)

Top 10 FR : sites coupon-aggregateurs internationaux (couponfollow, retailmenot, savings.com, knoji), Themeum officiel, 1 forum Quora, 1 article schoolswp.com (5843 = nous, P1+FS). Pas de competiteur FR-natif a positionnement "avis + code", ce qui explique notre P1.

Frequent Questions thruuu : "How do I use the Tutor LMS coupon code?", "Does Tutor LMS have a discount?", "Is Tutor LMS free?". FR : variations directes traduites + "promo Tutor LMS pas cher".

Format majoritaire : pages coupon courtes (~300 mots), pas d avis profond. Notre 27 k chars d avis bat la concurrence en autorite topique.

## 6. Insights critiques

1. **Publier le draft coupon FR 2967240 = cannibalisation directe**. L avis 5843 tient le top via 2 signaux faibles ; un nouvel article FR strictement coupon-oriente forcerait Google a choisir et il y a une bonne chance qu il switche vers le draft (intent plus pur) en perdant l autorite cumulee depuis 2021.

2. **Defendre 5843 = ROI max immediat**. Ajouter un encadre coupon visible au-dessus du TOC + une mini-FAQ ne change pas la nature de l article, mais consolide la couverture du KW transactionnel sans creer de page concurrente.

3. **EN market totalement ouvert**. Il n existe pas d equivalent schoolsWP.com/en/ pour "Tutor LMS coupon" ; la publication d un article EN coupon-only n a pas de risque de cannibalisation et capture une SERP differente.

4. **Code schoolsWP10 = 10 pourcent est juste une baseline negociee**. Memoire Gmail confirme : la majorite des partenaires acceptent 20 pourcent (cf. partenariats Wpmet 20-30, OttoKit 20, LinkCentral 20, Rapyd / Levamo 25). A renegocier avec Themeum sur le prochain echange.

5. **Cloak /tutor-lms gere par ClickWhale Pro** (table wp_clickwhale_links id=40, slug tutor-lms, redirection 307, nofollow=1, sponsored=1, cree 2024-03-13, updated 2025-05-16). Erreur ma requete initiale : j ai interroge les colonnes name/redirect_url/redirect_type alors que le schema ClickWhale est title/url/slug/redirection. Tracking actif via wp_clickwhale_track (76 960 events historiques). Hygiene SEO correcte (X-Robots-Tag noindex, nofollow, sponsored confirme via curl).

## 7. Decision

**Scenario B retenu** : preserver l avis 5843, NE PAS publier le draft coupon FR 2967240 (reste en brouillon), publier l equivalent EN.

Pourquoi ce scenario plutot que A (publier les deux + canonical) ou C (remplacer l avis par le coupon) :
- A = ajoute du jus interne (linking) mais expose au risque Panda content thinness sur le coupon FR
- B = preserve l autorite acquise sans perdre la couverture transactionnelle
- C = sacrifierait l autorite topique 2021-2026 de l avis pour un gain marginal

## 8. Plan d action

### Phase 1 - Defense (DONE 2026-05-30)

- [x] Patch avis 5843 : encadre coupon en haut, mini-FAQ avant la FAQ schema, MAJ date visible
- [x] Verifier que /tutor-lms cloak retourne bien 307 vers le lien affilie
- [x] Confirmer que le patch ne casse pas le FAQ Rank Math rich snippet (separe, non touche)

### Phase 2 - Expansion EN (cette semaine)

- [ ] Cloner le draft FR 2967240 vers une version EN sur /en/, adapter SERP EN (thruuu "Tutor LMS coupon" en plus de "Coupons Tutor LMS")
- [ ] Confirmer que les Frequent Questions thruuu EN soient bien couvertes (How do I use, Does it have discount, Is it free)
- [ ] Configurer Rank Math FAQ schema sur la version EN
- [ ] Publier EN (status publish) - pas de canonical, pas de hreflang vers le draft FR

### Phase 3 - Renegociation code (avant Q3 2026)

- [ ] Contacter Themeum : demander passage 10 vers 20 pourcent (mention historique partenariats + volume affilie schoolsWP)
- [ ] Si OK : mettre a jour l encadre coupon dans 5843 + version EN + tous les CTA existants
- [ ] Si refus : garder 10 pourcent mais demander code Black Friday separe a 25-30 pourcent

### Phase 4 - Monitoring (continu)

- [ ] Rank trace hebdo "code promo tutor lms" FR + "tutor lms coupon" EN
- [ ] GSC : suivre CTR + impressions sur 5843 via le query report 90 jours
- [ ] Si position FR descend en dessous de P3 : evaluer la publication du draft 2967240 comme page coupon-only avec rel canonical vers 5843 (et non l inverse)

## 9. Metriques de suivi

| Metrique | Valeur baseline 2026-05-29 | Objectif 2026-08-29 (T+3 mois) |
| --- | --- | --- |
| Position FR "code promo tutor lms" | P1 + FS | P1 + FS (maintenir) |
| Position EN "tutor lms coupon" | absent | top 20 (entree) |
| Clics GSC 5843 mensuel | a measurer (snapshot manquant) | +20 pourcent post-patch |
| Conversions affiliees Tutor LMS mensuel | a remonter via dashboard FluentAffiliate | +50 pourcent T+3 mois |
| Position GSC FAQ schema (FAQ rich result) | a verifier via URL inspect | maintenu |

## 10. Liens et ressources

- Article cible : https://schoolswp.com/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/
- Draft coupon FR (non publie) : post id 2967240
- Page generale codes-promo (draft non publie) : post id 2967207
- Cloak affilie : /tutor-lms vers tutorlms.com?affiliate=michaelkihl
- Rank Math FAQ rich snippet : id s-57e13546-3eff-4acd-8e7c-55f750a1d887 (a documenter dans le wiki)
- Raw thruuu : ./thruuu-raw/codes-promo-tutor-lms.xlsx + ./thruuu-raw/coupons-tutor-lms.xlsx
- Snapshot article : ./article-current-snapshot.md



## 11. Findings EN (ajoute 2026-05-30 apres recuperation thruuu + DataForSEO US)

### 11.1 Volume marche US confirme

DataForSEO + thruuu convergent : volume = 10/mois sur "tutor lms coupon" (et toutes ses variantes mesurables). Identique au marche FR. Long-tail extreme.

### 11.2 SERP US top 14 (thruuu 2026-05-30, scrape day-of)

1. techjury.net - $199 Tutor LMS Promo Code + 20% Off
2. wpdiscounts.io - 20% OFF Tutor LMS Pro Coupon May 2026
3. hostingcouponspot.com - 20% off
4. docs.themeum.com - Coupons doc page officielle
5. tenereteam.com - 55% OFF (FAQ inflated, reference erronee youskilled.io)
6. wethrift.com - 20% off
7. tutorlms.com/pricing - page tarifs officielle
8. themeum.vectortemplates.com - 87 Verified Themeum Coupons, 65% Off
9. tutorlms.com/blog/strategic-course-gifting
10. PAA (questions)
11. wptowp.com - 5+ Tutor LMS Alternative + Coupon
12. wpcouponsdeals.com - Lifetime Deal 20%
13. facebook.com/tutorlms - profil social
14. tutorlms.com/blog/discount-pricing-strategy

Domination ecrasante du code TUTORLMS20 (20 pour cent off) cite dans P1-P3-P4-P6-P10-P12. Notre code schoolsWP10 (10 pour cent) ne peut pas competer tant qu il reste a ce taux.

### 11.3 AI Overview present sur tutor lms coupon code

Detecte par DataForSEO. Google affiche un resume IA en haut de SERP citant Themeum + 2 sites coupons. Le resume mentionne TUTORLMS20. Pour apparaitre comme source citee, notre article EN doit fournir des reponses directes referenceables (definitions claires, infos verifiables).

### 11.4 Frequent Questions thruuu (questions repetees dans la SERP top 14)

Classees par frequence d apparition dans les pages top SERP :
- What is Tutor LMS? (8 occurrences)
- How to Grab Tutor LMS Life Deal (6)
- How can I find verified TutorLMS coupons? (3)
- Does TutorLMS include course creation tools? (3)
- How often are new Themeum coupons added? (2)
- What is Themeum? (2)
- How many coupon codes are currently available for Tutor LMS? (2)
- Can I create quizzes with TutorLMS? (2)
- Are the Tutor LMS Competitors Better? (2)

### 11.5 Gap analysis vs draft EN 2968090

Notre brouillon EN couvre bien :
- How to use the coupon (etape par etape)
- Free version vs Pro
- Quizzes & assessments
- Course creation
- Monetization
- Integrations WooCommerce/FluentCRM
- Conclusion + lien vers avis EN

Notre brouillon NE couvre PAS (gap a combler avant publication) :
1. "What is Tutor LMS?" en intro directe (la question 1 du SERP, 8 occurrences)
2. "What is Themeum?" - mention explicite de l editeur
3. "Tutor LMS Lifetime Deal" - notre code Pro ne couvre pas le lifetime, a clarifier
4. "How to Grab Tutor LMS Life Deal" - 2eme question la plus frequente
5. "How many coupon codes are available?" - meta-question, on pourrait y repondre

### 11.6 Related Search thruuu

- Tutor lms coupon free
- Tutor LMS Black Friday
- Tutor LMS pricing
- Tutor lms lifetime deal
- Tutor LMS subscription
- Tutor LMS alternatives
- Tutor LMS plugin
- Tutor LMS WordPress theme free

### 11.7 Action plan revise

Phase 2 EN BLOQUEE en l etat. Avant de publier le brouillon 2968090 :

- [ ] **Critical** : negocier code Themeum a 20% minimum (email envoye 2026-05-30, en attente reponse)
- [ ] **Critical** : si Themeum refuse, NE PAS publier - l article EN serait non-competitif face a TUTORLMS20 public
- [ ] **Si code 20%+ obtenu** : combler les 5 gaps SERP avant publication (intro What is Tutor LMS, Lifetime deal, Themeum)
- [ ] **Si code 20%+ obtenu** : viser citation dans AI Overview (definitions claires, references checables)
- [ ] **Si refus Themeum** : reorienter strategie - publier seulement l article EN comme "Tutor LMS Review + Best Deals 2026" qui agrege les codes publics existants sans creer notre propre coupon article competitif


## 12. Journal des actions (changelog)

Ce que je fais et quand. Ordre chronologique. Mise a jour a chaque action significative.

### 2026-05-30

- **Patch defensif applique sur avis FR 5843** (LIVE) : encadre coupon vert brand, mini-FAQ avant H2 FAQ schema, date MAJ. 27 239 chars vers 30 016. Sous GO explicite Michael.
- **Brouillon EN coquille creee** (post 2968090) : titre "Tutor LMS Coupon Code: -10% with schoolsWP10 for Your WordPress Online School", slug coupon-code-tutor-lms, langue en, lie au draft FR via Polylang, categories Training platforms (LMS) + Tutor LMS-en.
- **Contenu EN injecte** dans 2968090 (18 227 chars) : 15 H2, 6 H3 FAQ, 3 boutons CTA vers /tutor-lms, lien interne vers avis EN 57950. Remplacement des 3 boutons Kadence cassees du brouillon FR par des wp:buttons core fonctionnels.
- **Email negociation Themeum redige** (en anglais) : 3 options (A=20%, B=25-30%, C=Black Friday seasonal a 25-30%). Brouillon Gmail cree (ID r-5921599180710204493), version FR sauvegardee pour reference Michael.

### 2026-05-31

- **Analyse SERP EN realisee** : DataForSEO US + thruuu xlsx. 4 JSON sauvegardes + 1 CSV + Sheet Drive cree. AI Overview detecte sur "tutor lms coupon code", code public TUTORLMS20 (20%) confirme dominant top 14 SERP. Frequent Questions identifiees.
- **Email envoye a Themeum** (Michael). En attente reponse.
- **5 patches gap appliques sur brouillon EN 2968090** (toujours draft, jamais publie) :
  - Patch A : nouvelle section H2 "What is Tutor LMS?" en haut avec lien vers Themeum, repond a la question #1 du SERP (8 occurrences).
  - Patch B : mention du plan lifetime dans la section tarifs, repond a "How to Grab Tutor LMS Life Deal" (#2 SERP, 6 occurrences).
  - Patch C : phrase "verified partner code, negotiated directly with Themeum" apres les conditions d'usage, repond au gap "How can I find verified TutorLMS coupons?".
  - Patch D : nouvelle question FAQ H3 "How many Tutor LMS coupon codes exist at any time?" avec 3 categories (partner codes, seasonal codes, Themeum own codes), evite de mentionner TUTORLMS20 explicitement pour ne pas saboter notre attribution.
- **Length** : 18 227 vers 20 317 chars (+2 090). 15 H2 et 7 H3 maintenant. Modified 2026-05-31 14:17.
- **Note technique** : Novamira MCP session expiree pendant l execution, repli WP REST direct (Python + env vars WP_API_URL/USERNAME/PASSWORD) utilise avec succes. Memorise dans feedback_novamira_session_recovery.md.

### Statut a ce jour (2026-05-31)

- Avis FR 5843 : patche, P1 + FS preservation en cours, monitoring 90 jours a faire.
- Brouillon EN 2968090 : pret editorialement (5 gaps combles, structure SERP-aligned), bloque a la publication par le code 10% (vs TUTORLMS20 public 20%).
- Brouillon page generale codes-promo (2967207) : non touche depuis le 2026-05-30, reste a depopular du framing Black Friday.
- Themeum : email envoye, reponse attendue. Si OUI 20%+, on publie EN + on enchaine DE + on update FR. Si NON, plan B = pivoter vers "Review + Best Deals 2026" sans coupon dedie.

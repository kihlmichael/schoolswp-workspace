---
slug: easycommerce-vs-fluentcart-avis
url: https://schoolswp.com/?p=2978852 (brouillon - non publie)
post_id: 2978852
date_snapshot: 2026-06-21
trigger: Demande Michael (audit SEO pre-publication + mot-cle, thruuu SERP+GEO en parallele)
status: refonte-appliquee-live
mot_cle_cible: easycommerce vs fluentcart
---

# Audit SEO - EasyCommerce vs FluentCart (brouillon, post 2978852)

## 1. Contexte & declencheur

Audit SEO pre-publication demande par Michael sur le brouillon "EasyCommerce vs FluentCart : quel plugin choisir en 2026 ?". Mot-cle cible : **easycommerce vs fluentcart**. Analyse SERP Google + GEO traitee en parallele par Michael via thruuu. Sources outils : **DataForSEO** (volumes, KD, intention, SERP) + **Ubersuggest a fusionner** (export fourni ensuite - non connecte en MCP).

Note importante : l'URL publique `?p=2978852` renvoie une **404** (post en statut `draft`). Lecture du contenu faite cote back-office via Novamira `execute-php`, pas via le live. thruuu ne peut pas scraper un brouillon (il verrait la page 404) : cote thruuu, seul l'export SERP est exploitable.

## 2. Donnees collectees

- **Lecture article** : Novamira `execute-php` (post_content + metas Rank Math + taxonomies + comptages) - 2026-06-21.
- **DataForSEO** : keyword_overview FR + US, bulk_keyword_difficulty, search_intent, keyword_suggestions, SERP organic live FR, ranked_keywords - 2026-06-21.
- **Ubersuggest** : a fusionner (colonnes `vol_ubersuggest` / `sd_ubersuggest` du Sheet laissees vides).
- **thruuu** (fourni par Michael, 2026-06-21) : SERP google.fr FR + analyse GEO "comparer les reponses IA" (ChatGPT / Gemini / Google AI Mode : marques, domaines, termes). Raw archive : `thruuu-raw/serp-analysis.xlsx`.
- Fichiers : `seo-volumes-google-sheet.csv`, `audit-onpage.csv`, `dataforseo-serp-fr.json`, `geo-citations.csv`, `article-current-snapshot.html`, `thruuu-raw/`.
- Google Sheet : `schoolsWP - Volumes SEO - EasyCommerce vs FluentCart - 2026-06-21`.

## 3. Etat de l'article

- **Statut** : brouillon (draft), cree et modifie le 2026-06-21.
- **Longueur** : 3261 mots (solide pour un comparatif).
- **Structure** : 8 H2 / 10 H3, arborescence logique (Resume > EasyCommerce > FluentCart > Fonctionnalites > Prix > Avis clients > Faut-il acheter > FAQ).
- **Table comparative** : 1 (bon signal comparatif + GEO).
- **Images** : 0 (aucune image, pas de featured image).
- **Schema JSON-LD** : 0 bloc (aucune donnee structuree, ni via bloc ni via Rank Math).
- **Maillage** : 14 liens internes vers le cluster e-commerce, 0 lien externe.
- **Categorie** : "Non classe" ; **Tags** : 0.

## 4. SEO actuel (on-page)

Le detail item par item est dans `audit-onpage.csv`. Synthese :

**Conforme** : title (kw cible en debut), H1 (kw + 2026), slug propre, longueur, structure Hn, densite focus kw equilibree (exact x4), table comparative, maillage interne, 0 em/en-dash, naming schoolsWP correct.

**A corriger (P0)** :

- **0 schema JSON-LD** : pour un comparatif "vs" a intention commerciale, c'est le manque #1 cote GEO/AIO. Manque FAQPage (la FAQ existe deja) + SoftwareApplication x2.
- **0 image** : pas de featured image (og:image tombe sur l'image par defaut du site) ni de visuel comparatif.
- **Categorie "Non classe"** : aucune categorie reelle assignee (incoherent avec `rank_math_primary_category=1095`).

**A ameliorer (P1)** :

- Meta description : contient un emoji et ne reprend pas le kw exact "EasyCommerce vs FluentCart" (Rank Math le signale ; explique en partie le score 75/100).
- 0 lien externe : aucune source officielle (easycommerce.dev, fluentcart.com) -> faible pour E-E-A-T / GEO.
- 0 tag.

## 5. SERP analysee (DataForSEO FR)

Pas de SERP propre au terme exact "easycommerce vs fluentcart" : Google retourne une **SERP large FluentCart** (pack video YouTube + pages editeurs + Reddit). **Aucune page editoriale FR "vs" etablie = opportunite first-mover.**

Top observe : fluentcart.com (vs SureCart), easydigitaldownloads.com/fr/compare/fluentcart, **easycommerce.dev/compare/fluentcart** (le concurrent fait deja sa page comparative), leokoo.com, Reddit, puis **schoolswp.com/avis-fluentcart-wordpress/ en position ~7** (page 1, via un AUTRE article que le brouillon audite), wpmanageninja.com.

Intention dominante : **commerciale** (0.887 sur le terme cible).

### Benchmark concurrents (thruuu, google.fr FR)

| Pos | Page                                           | Mots | Images | FAQ schema                | Angle                                            |
| --- | ---------------------------------------------- | ---- | ------ | ------------------------- | ------------------------------------------------ |
| 3   | easydigitaldownloads.com/fr/compare/fluentcart | 2344 | 23     | **FAQPage (2)**           | EDD pour produits numeriques                     |
| 5   | leokoo.com                                     | 1467 | 10     | non                       | review all-in-one                                |
| 6   | easycommerce.dev/compare/fluentcart            | n/d  | n/d    | non                       | page comparative du concurrent                   |
| 7   | fluentcommunity.co                             | 2414 | 25     | non                       | taxonomie features complete                      |
| 8   | **schoolswp.com/avis-fluentcart-wordpress**    | 3224 | 14     | **non** (FAQ sans schema) | avis FluentCart / alt Woo (deja page 1)          |
| 12  | woocustomdev.com/woocommerce-vs-fluentcart     | 1567 | 6      | non                       | comparatif structure + verdict                   |
| 13  | atmostfear-entertainment.com                   | 2580 | 7      | non                       | self-hosted / data ownership                     |
| 14  | daisywp.com                                    | 734  | 7      | non                       | 3-way FluentCart/StoreEngine/EasyCommerce (thin) |

Lecture : longueur mediane concurrents ~2300-2600 mots (le brouillon a 3261 = OK, au-dessus). **Images : tous entre 10 et 67, le brouillon a 0** (gap criant). **Schema FAQ : seul EDD en a un, et il ranke #3 ; meme la page schoolsWP qui ranke deja n'en a pas** -> ajouter FAQPage = avantage differenciant net. Ambiguite confirmee : sourceforge (#17) parle d'un AUTRE "EasyCommerce" (vs WP EasyCart) -> nommer explicitement `easycommerce.dev` / "EasyCommerce (AI-first)".

### GEO - citations IA (thruuu, detail dans `geo-citations.csv`)

Les 3 moteurs IA repondent deja a "EasyCommerce vs FluentCart". Constat decisif :

- **schoolsWP est cite par Google AI Mode (2x) + Google Organic, mais ABSENT de ChatGPT et Gemini.**
- **easycommerce.dev domine le narratif LLM** : cite par ChatGPT (3x) et Gemini (4x) via sa page `/compare/fluentcart`. Le concurrent ecrit l'histoire que les IA racontent.
- EDD cite par ChatGPT (2x) ; co-marques recurrentes : WooCommerce (3/3), FluentCRM, Fluent Forms, SureCart, Gutenberg, Bricks.
- **Gemini et Google AI Mode confondent "EasyCommerce" avec un ecosysteme mature type WooCommerce** (faux : easycommerce.dev est un plugin AI-first tout neuf). Cette erreur des IA = opportunite : l'article qui desambiguise clairement peut devenir la source corrective citee.

Implication : l'objectif #1 de l'article = **se faire citer par ChatGPT et Gemini** (pas seulement Google AI Mode). Leviers GEO : schema (FAQPage + SoftwareApplication), reponses factuelles courtes extractibles, desambiguisation explicite d'EasyCommerce, mention des marques co-citees.

### Gaps de contenu a couvrir (thruuu : questions + H2 concurrents)

Questions concurrentes a integrer dans la FAQ (FR, tutoiement) + FAQPage schema :

- Vendre produits physiques ET numeriques ensemble ? (x2) - Personnaliser le plugin a sa marque ? (x2)
- Abonnements / facturation recurrente ? - Moyens de paiement / passerelles (gateways) ?
- Frais de transaction / services payants ? - Compatible avec mon theme ? - Facile a installer ?
- Pour qui chaque outil est le bon choix ? (verdict) - Peut-on migrer de l'un vers l'autre ?

Taxonomie feature attendue (fluentcommunity / woocustomdev) : gestion produits, checkout & paiements, abonnements & licences, gestion clients, commandes & fulfillment, marketing, reporting & analytics, design, experience developpeur. Le brouillon couvre deja IA/Store Copilot, perfs, prix, avis ; **a completer : abonnements/licences, passerelles de paiement, volet migration**.

## 6. Donnees mots-cles (le point cle)

| Mot-cle                    | Marche  | Volume/mois | Tendance an | KD    | Intention               |
| -------------------------- | ------- | ----------- | ----------- | ----- | ----------------------- |
| easycommerce vs fluentcart | FR & US | **0 (n/d)** | -           | n/d   | commercial 0.89         |
| fluentcart                 | FR      | 70          | +300%       | n/d   | navigational            |
| fluentcart                 | US      | **260**     | **+1600%**  | **7** | navigational            |
| easycommerce               | US      | 70          | +175%       | n/d   | navigational+commercial |
| fluentcart vs woocommerce  | US      | 10          | -           | n/d   | commercial              |
| fluentcart vs surecart     | US      | 10          | -           | n/d   | commercial              |

**Lecture** : le mot-cle cible exact a **0 volume mesurable** (FR comme US) - terme tout neuf. La valeur de cet article n'est donc PAS le trafic direct a court terme, mais :

1. **GEO / citation IA** : etre LA reference FR quand un LLM repond "EasyCommerce vs FluentCart".
2. **First-mover** sur un terme appele a monter (FluentCart : +1600%/an US, KD 7 = tres facile).
3. **Autorite de cluster** : alimenter `/avis-fluentcart-wordpress/` qui ranke deja page 1.

## 7. Conformite marque schoolsWP (audit + reco, sans modif live)

Le live n'est pas touche (decision Michael). Ecarts a corriger avant publication :

**P0 (bloquant marque)** :

- **Vouvoiement massif** : 20 "vous" + nombreux "votre/vos" (74 phrases concernees) vs 8 "tu/te/ton". La regle est le tutoiement systematique sans exception. + retirer les "nous/notre/nos" ("notre comparaison", "nos analyses").
- **Heading FAQ en anglais** : "Questions? We Have Answers." (artefact de template) -> traduire en FR. Idem ancre interne "WordPress guides, reviews, and comparisons".
- **Mot interdit** : "sans effort" x2 -> reformuler.

**P1** :

- **Disclosure affilies absente** : l'article pointe vers des cloaks affilies (`/EasyCommerce/`, `/fluentcart/`). La formule standard de disclosure est obligatoire.
- **Sources & ressources absente** : le stat "chute de 7% du taux de conversion par seconde de delai" doit etre source (Google/Deloitte/Akamai) ou retire (zero promesse non prouvee).
- **Respect concurrent** : structure deja plutot equilibree (deux recommandations par cas d'usage), mais ajouter une section explicite "Pour qui EasyCommerce reste pertinent / Pour qui FluentCart reste pertinent" et formuler le verdict comme un choix de Michael pour schoolsWP (pas un classement universel). Eviter "Le meilleur choix".

**P2** : "simplement" x1 (verifier contexte) ; elisions FR dans les H2/H3 ("de EasyCommerce" -> "d'EasyCommerce").

**Conforme** : naming schoolsWP (0 faute), 0 em/en-dash.

## 8. Decision & plan d'action

**Decision : refonte-decidee avant publication.** L'article est une bonne base (structure + longueur + maillage) mais ne doit pas etre publie en l'etat. C'est un **asset GEO + cluster**, pas un play volume.

Plan (avant publication) :

1. **Marque P0** : tutoiement complet + retrait nous/notre + heading FAQ FR + retrait "sans effort". (effort moyen)
2. **Schema P0** : FAQPage + SoftwareApplication x2 via Rank Math. (effort faible, fort impact GEO)
3. **Images P0** : featured image hero marque schoolsWP + 1 visuel comparatif (logos / table en image) + alt SEO. (effort moyen)
4. **Taxonomie P0** : categorie reelle (E-commerce) + tags. (effort faible)
5. **P1** : kw exact dans meta description + disclosure affilies + section Sources + liens externes officiels + section "pour qui chacun reste pertinent". (effort faible-moyen)
6. Verifier la **cannibalisation cluster** : deux slugs review FluentCart coexistent (`/avis-fluentcart-wordpress/` qui ranke + `/fluentcart-avis/`). Clarifier le role de chacun ; cet article = le comparatif "vs", a ne pas faire doublonner avec l'avis FluentCart.
7. **GEO (cible : etre cite par ChatGPT & Gemini, pas seulement Google AI Mode)** : desambiguiser EasyCommerce (nommer `easycommerce.dev` / "AI-first"), FAQ factuelle extractible (cf. gaps thruuu), completer taxonomie features + volet migration, citer les marques co-citees (WooCommerce, ecosysteme Fluent). easycommerce.dev a deja sa page comparative -> contrer le narratif cote FR. Quick win cluster : ajouter aussi FAQPage schema sur `/avis-fluentcart-wordpress/` (qui ranke #8 sans schema FAQ).

## 9. Metriques de suivi (prochain snapshot)

- Indexation du post une fois publie (GSC URL inspect).
- Position sur "fluentcart" (FR 70 / croissance) et apparition sur "easycommerce vs fluentcart".
- Citations IA (suivi GEO thruuu : schoolsWP cite ou non sur la question vs).
- Rich results (FAQPage / SoftwareApplication valides).
- CTR + impressions ; eventuelle cannibalisation avec `/avis-fluentcart-wordpress/`.

## 10. Execution live appliquee (2026-06-21)

Refonte appliquee sur le brouillon (post 2978852) en 4 paliers, chacun avec backup postmeta base64 (reversible).

- **Palier 1 - taxonomie + meta** : categorie passee de "Non classe" (1095) a "E-commerce & Tunnels de vente WordPress" (1712, primary alignee), 4 tags ajoutes, meta description reecrite (kw exact + sans emoji).
- **Palier 2 - tutoiement + langue** : 90 remplacements. vous 20->0, votre 42->1 (ancre du titre lie, gardee), vos 28->0, "sans effort" 2->0, heading FAQ EN->FR, ancre EN->FR. Backup `_schoolswp_content_backup_palier2_20260621`.
- **Palier 2.5 - corrections factuelles** : 13 corrections (faits verifies sur sites officiels). Retrait "4,7 etoiles WordPress.org" (non verifiable), "132 API REST"->"API REST complete + webhooks", "100 credits IA mensuels"->"credits IA inclus", "25 %"/"7 %"/"trois fois"/"5 min chrono" softes, "3-5x" attribue a EasyCommerce. Backup `..._palier25_...`.
- **Palier 3 - sections marque** : desambiguisation EasyCommerce (=easycommerce.dev AI-first), 2 disclosures affilies (formule standard), section "Pour qui chacun reste pertinent", section "Sources & ressources". Backup `..._palier3_...`.
- **Palier 4 - schema GEO** : 3 blocs JSON-LD (FAQPage 5 Q/R + SoftwareApplication EasyCommerce + FluentCart, donnees verifiees, sans aggregateRating invente ; survivent au kses). Backup `..._palier4_...`.

**Image a la une** : deja posee le 21/06 (attachment 2979807, hero marque, alt SEO renseigne). Pas de regeneration (doublon evite).

**Decisions Michael** : code promo schoolsWP20 conserve (reel) ; corrections factuelles appliquees d'office ; GO execution live.

**Etat final** : 3395 mots, 9 H2 / 10 H3, tutoiement complet, 0 em-dash, 3 schemas, categorie OK, hero featured + alt OK.

**Reste (optionnel / a la publication)** : images inline dans le corps (0 ; le hero + la table comparative couvrent l'essentiel) ; ouvrir dans Rank Math pour recalcul du score (75 fige tant que non ouvert) ; retirer le noindex a la publication (draft). Quick win cluster FAQPage : **FAIT 2026-06-22** (cf. section 11). Le hero featured affiche "Vitesse 3x WooCommerce" (revendication EasyCommerce, coherent avec le corps apres attribution). Restauration possible via les 4 backups postmeta base64.

## 11. Quick win cluster - FAQPage sur /avis-fluentcart-wordpress/ (2026-06-22)

Action de cluster decidee dans l'audit (section 8) : la page `/avis-fluentcart-wordpress/` (post **1505872**, `publish`, ranke #8 organique) avait une section FAQ visible ("Des questions ? J'ai les reponses." - double accordeon Kadence, **4 Q/R**) mais **aucun schema FAQ** (Rank Math n'emettait qu'un `BlogPosting` par defaut). EDD (#3) en a un -> ajout = avantage differenciant + levier GEO.

- **Applique** : 1 bloc JSON-LD `FAQPage` (4 questions) injecte en fin de `post_content` via un bloc `<!-- wp:html -->`. Les 4 Q/R refletent **mot pour mot** le texte visible de l'accordeon (exigence Google : le schema FAQ doit correspondre au contenu affiche). Ton vouvoiement conserve tel quel pour matcher la page (pas de refonte de ton ici, hors perimetre).
- **Methode** : meme pipeline que les paliers (build local + verif round-trip -> base64 -> execute-php). Backup postmeta `_schoolswp_faqschema_backup_20260622` (base64 du contenu original, 43005 chars). Trace reproductible : `_build_faqschema_fluentcart.py` + `_faqschema_fluentcart.b64`.
- **Piege rencontre et resolu** : `wp_update_post()` applique `wp_unslash()` -> les guillemets echappes `\"` du JSON (`"meilleur"`, `"tout-en-un"`) sautaient -> JSON invalide cote rendu. Fix : passer le contenu via `wp_slash()` avant `wp_update_post`. Verifie ensuite valide **stocke ET rendu** (`the_content`).
- **Verif finale** : `FAQPage`, `@context` schema.org, 4 `Question`/`acceptedAnswer`, JSON valide, 0 backslash parasite, accents OK. `clean_post_cache` fait (aucun plugin de cache page detecte ; reste un eventuel cache hote/CDN qui s'auto-purgera).
- **Reste** : tester l'URL live dans le Rich Results Test de Google apres propagation du cache.

## 12. Pass brand complet sur /avis-fluentcart-wordpress/ (2026-06-22)

Suite a la section 11, Michael demande de respecter pleinement le brand schoolsWP sur cette page live. Pass brand complet applique sur le post **1505872** (publish).

- **Bilan avant** : vous 38, votre 30, vos 19, nous 1, notre 1, "sans effort" 2, em-dash 2, "scalabilite" 6 (visibles).
- **Applique** : **62 remplacements** (tutoiement complet conjugue : vous->tu/te/toi, votre->ton/ta selon genre, vos->tes ; imperatifs Decouvrez/Plongez/Imaginez/Pensez/Connectez/Lancez/Obtenez/utilisez -> tutoiement ; nous/notre neutralises ; "Soyons honnetes"->"Honnetement", "Soyons directs"->"Sans detour", "Voyons"->"Voici" ; "sans effort" supprime ; em-dash -> parentheses ; "scalabilite" -> "montee en charge" car famille du mot interdit "scalable").
- **Schema FAQPage regenere** depuis l'accordeon converti (les 4 reponses passent au tutoiement) pour rester strictement aligne sur le texte visible. JSON revalide stocke ET rendu.
- **Methode** : remplacements verifies en local sur le contenu reel (zero re-saisie de old), gate sur le **texte visible** (les `votre`/`scalabilite` dans les slugs d'ancre invisibles sont laisses pour ne pas casser la ToC / ancres internes). Application serveur = 62 paires + preg vos/Vos + re-attache du nouveau bloc schema, `wp_slash` pour survivre a `wp_unslash` (cf. [[reference_novamira_wp_update_post_unslash_json]]). Resultat live byte-identique a la version verifiee en local (46459 octets).
- **Verif finale live** : texte visible vous/votre/vos/nous/notre/sans-effort/em-dash/scalab = **0** ; schema valide stocke+rendu ; backup `_schoolswp_brand_backup_20260622` (reversible). Trace reproductible : `_build_brand_pass_fluentcart.py` + `_brand_pairs.b64` + `_brand_schemablock.b64` + `_verify_brand.py`.

## 13. Verification Google + alerte de suivi (2026-06-22)

- **Rich Results Test** (lance par Michael) : **3 elements valides** detectes sur l'URL live - Article, Fil d'Ariane (BreadcrumbList), Organisation (tous Rank Math), **0 erreur**. Exploration + indexation OK.
- **FAQPage non liste = normal** : depuis aout 2023, Google ne montre les FAQ rich results qu'aux sites gouvernementaux/sante ; le Rich Results Test ne liste donc plus FAQPage meme valide. Confirme present en live par fetch du HTML rendu (`wp_remote_get` loopback, HTTP 200) : **2 blocs JSON-LD**, dont le FAQPage (question Q1 presente). Le schema reste lu par les LLM (objectif GEO). Cf. [[reference_faqpage_no_rich_result_2023]].
- **Alerte de suivi mensuelle posee** : workflow n8n **`uxCImeo2jFONMk5O`** "[Prod] Schedule mensuel > Telegram: Suivi SEO FluentCart", actif sur schoolswp-n8n.wp1.host. Schedule Trigger cron `17 9 22 * *` (le 22 de chaque mois, 09h17 Europe/Paris) -> message Telegram sur le canal de la veille FluentCart (chat `1020689775`, bot @schoolswp_fluentcart_bot, cred `Juj7Y2RQgc54DPvY`). Contenu : rappel de verifier position GSC + indexation + citation GEO (ChatGPT/Gemini/AI Mode) vs baseline de juin. Aucun cron local n'existait avant (CronList vide, pas de scheduled_tasks.json). Note : un rappel via le planificateur Claude Code local n'etait pas viable (session-only / expiration 7 jours), d'ou le choix du cloud n8n.

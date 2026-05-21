---
slug: ottokit-free-vs-pro
lang: de
date_snapshot: 2026-05-19
type: patterns-analysis
trigger: Demande Michael - analyse data-driven des patterns de requete DE
sources_utilisees:
  - GSC 90j (gsc-90d.json)
  - DataForSEO Labs volumes/intent/SERP (4 fichiers)
  - thruuu google.de top 17 (thruuu-de-summary.json)
regle_absolue: aucune donnee inventee. Si donnee non disponible, mention explicite.
---

# Patterns de requete OttoKit Free vs Pro (DE) - snapshot 2026-05-19

## Perimetre des donnees disponibles

| Source | Couverture effective | Limites observees |
| --- | --- | --- |
| GSC schoolswp.com | 6 requetes ottokit + 4 suretriggers sur 90j (2026-02-18 a 2026-05-19) | 0 clic sur tout le cluster. Brouillon DE 2898734 absent de GSC. |
| DataForSEO Labs DE | 10 keywords avec volumes, intent, KD, trends 12 mois | Marche DE jeune : 4/10 keywords absents de la base (volume < 10/mois, marque ces "Donnee non disponible"). |
| DataForSEO SERP DE depth 20 | Top 10 + AIO + 8 related searches | AIO present mais asynchrone (statut a verifier en live). |
| thruuu google.de | Top 17 + 9 questions H1/H2 frequentes + topic dominant | Pas d'AIO scrape (discordance avec DataForSEO). |

> Le keyword principal de l'article ("OttoKit Free vs Pro") n'a **pas de volume confirme** dans la base DataForSEO DE. La probabilite d'intent commercial est forte (0.913) mais le volume est marque "Donnee non disponible" et le seuil DFS est < 10/mois.

## Methode de regroupement

Les 10 keywords DFS + 8 related searches Google DE + 9 questions H1/H2 thruuu + 10 requetes GSC ont ete regroupes en patterns observes (pas hypothetiques). Chaque pattern doit etre soutenu par au moins une donnee concrete. Niveau de confiance attribue selon la regle :

- **Fort** : volume DataForSEO confirme **et** signal SERP **et** (signal GSC ou related search)
- **Moyen** : 2 sources sur 3, ou volume null mais intent probabilite > 0.8 + couverture SERP attestee
- **Faible** : 1 seule source, sans volume confirme

## Patterns identifies

### P1. Marque sec (acces direct OttoKit)

- **Intention** : navigationnelle / transactionnelle.
- **Exemples observes (5)** : `ottokit`, `otto kit`, `ottokit login`, `ottokit wordpress`, `ottokit automation`.
- **Donnees** :
  - `ottokit` : volume DFS 110/mois DE, KD 11 (LOW), CPC 2.92 EUR, trend mensuel +57 %, intent transactional (DFS).
  - `otto kit` : related search Google DE (thruuu + DFS).
  - `ottokit login` : volume DFS 10/mois DE, intent navigational.
  - GSC : 182 impressions sur "ottokit" toutes pages cumulees, pos 9.0, 0 clic ; "ottokit wordpress" 2 imp pos 21.5 ; "ottokit automation" 1 imp pos 4.0.
- **Page schoolsWP existante** : `/ottokit-avis-automatisation-wordpress/` pos 9 sur "ottokit" (110 imp seul) - GSC.
- **Niveau de confiance** : **Fort** (volume + GSC + related search croisent).
- **Donnees manquantes** : aucune sur ce pattern. CTR reel non mesurable (0 clic sur 90j = pas de signal exploitable).

### P2. Pricing et Free vs Pro (decision d'achat)

- **Intention** : commerciale - decisionnelle.
- **Exemples observes (5)** : `ottokit pro`, `ottokit pricing`, `ottokit free vs pro`, `ottokit kostenlos`, `ottokit ltd` (titre Reddit r/Wordpress "Buy LTD Before Price Increase", pos 4 SERP DE).
- **Donnees** :
  - `ottokit pro` : DFS vol 10/mois DE, intent commercial p=0.95, trend stable 12 mois.
  - `ottokit pricing` : DFS vol 10/mois DE, intent commercial, competition LOW.
  - `ottokit free vs pro` : DFS volume **Donnee non disponible**, intent commercial p=0.913.
  - `ottokit kostenlos` : DFS volume **Donnee non disponible**, intent commercial p=0.846.
  - `ottokit ltd` : pas de volume DFS, presence indirecte via le titre Reddit pos 4 SERP DE.
  - GSC : "ottokit pro" 4 impressions pos 3.8, 0 clic.
- **Niveau de confiance** : **Moyen** (intent fort partout, mais 3/5 volumes en "Donnee non disponible" et le seul volume confirme est de 10/mois).
- **Donnees manquantes** : volume reel `ottokit free vs pro` et `ottokit kostenlos` (sous le seuil DFS), CTR concurrent sur ces requetes.

### P3. Avis et retours d'experience

- **Intention** : commerciale - evaluation.
- **Exemples observes (5)** : `ottokit review`, `ottokit erfahrungen`, `ottokit im test` (H1 robert-leitinger.com pos 13), "OttoKit Reviews 2026" (titre G2 pos 10 + Crocoblock pos 7 + wpwebzon pos 15), `ottokit review wordpress` (deduit des titres wpastra pos 4 + newpulselabs pos 8).
- **Donnees** :
  - `ottokit review` : DFS volume **Donnee non disponible**, intent commercial p=0.80.
  - `ottokit erfahrungen` : DFS volume **Donnee non disponible**, intent informationnel p=0.723 (bascule info car attentes Q&A / retours).
  - thruuu : 4 reviews EN dans le top 10 (wpastra, crocoblock, newpulselabs, g2.com) + 1 review DE (robert-leitinger pos 13) + 1 review EN pos 15 (wpwebzon).
- **Page schoolsWP existante** : version FR `/ottokit-avis-automatisation-wordpress/`. Equivalent DE **non publie**.
- **Niveau de confiance** : **Moyen** (intent confirme DFS + couverture SERP massive en EN, mais pas de volume DE confirme).
- **Donnees manquantes** : volume DE des termes review/erfahrungen (sous le seuil DFS), CTR moyen des reviews EN sur audience DE.

### P4. Definition et decouverte produit (intent informationnel)

- **Intention** : informationnelle - decouverte.
- **Exemples observes (5)** : "Was ist OttoKit ?" (H2 sur 4 pages du top 17 thruuu, frequence agregee 273 occurrences), "OttoKit erklart" (deduit de H2 thruuu), "OttoKit automation tool" (H1 wpastra + ottokit.com), "OttoKit no-code" (titre home ottokit.com pos 1), "Benotige ich Programmierkenntnisse fur OttoKit ?" (H2 bit-integrations.com).
- **Donnees** :
  - thruuu : "Was ist OttoKit ?" present comme H2 sur 4 pages du top 17 (signal SERP fort).
  - thruuu : "Benotige ich Programmierkenntnisse fur die Nutzung ?" 1 page (bit-integrations).
  - DFS : aucun keyword definitionnel direct retourne dans les suggestions DE (la base DFS ne couvre pas ce niveau de question en DE).
  - GSC : "ottokit automation" 1 imp pos 4.0 (signal marginal).
- **Niveau de confiance** : **Moyen** (signal SERP fort via H2 recurrents, mais aucun keyword DFS direct).
- **Donnees manquantes** : volume reel des requetes en "Was ist..." / "Wie funktioniert..." (non retourne par DFS DE).

### P5. Comparatifs avec alternatives (Make, n8n, Zapier, Uncanny Automator)

- **Intention** : commerciale - comparative.
- **Exemples observes (5)** : `ottokit vs zapier`, `ottokit vs n8n`, `ottokit vs make` (H2 robert-leitinger : "OttoKit vs Make vs n8n - Was ist der Unterschied?"), `uncanny automator pro`, `integrately`.
- **Donnees** :
  - GSC : "ottokit vs zapier" 4 imp pos 4.2 sur 90j, 0 clic.
  - thruuu : H1 robert-leitinger.com pos 13 "OttoKit im Test - Wie gut ist die n8n / Make Alternative wirklich ?". Topic dominant "zapier" 6 pages 46 frequences.
  - thruuu/DFS : related searches Google DE incluent `Uncanny Automator Pro` et `Integrately`.
  - thruuu : titre YouTube SERP pos 5/6 "N8N vs Make vs OttoKit vs ActivePieces : Comparison of AI Automation Tools".
- **Page schoolsWP existante** : `/en/suretriggers-ottokit-vs-zapier/` pos 1.1 sur "suretriggers vs zapier" (76 imp, 0 clic, marque morte). Equivalent DE **non publie** sur l'angle Make/n8n.
- **Niveau de confiance** : **Fort** (3 sources concordantes : GSC + thruuu + Google related searches).
- **Donnees manquantes** : volumes DE des combinaisons `ottokit vs make`, `ottokit vs n8n`, `ottokit vs uncanny` (DFS ne les retourne pas en suggestions DE).

### P6. Legacy SureTriggers (rebranding capture)

- **Intention** : informationnelle / commerciale - rebranding.
- **Exemples observes (5)** : `suretriggers`, `suretriggers wordpress automation plugin`, `suretriggers vs zapier`, `suretriggers review`, "ehemals SureTriggers" (utilise dans le titre bit-integrations.com pos 9 SERP DE).
- **Donnees** :
  - DFS : `suretriggers` vol 50/mois DE, CPC 6.63 EUR, trend mensuel -50 %, trimestriel -50 %, **annuel -89 %** (pic 320/mois en avril 2025, plus que 10/mois en mars 2026).
  - GSC : "suretriggers vs zapier" 76 imp pos 1.1 sur 90j, 0 clic. "suretriggers wordpress automation plugin" 67 imp pos 12.0, 0 clic. "suretriggers" 28 imp pos 46.4. "suretriggers review" 9 imp pos 32.6.
  - thruuu : 1 mention exploitee en titre concurrent (bit-integrations.com/de).
- **Niveau de confiance** : **Fort sur le declin** (volume + GSC + signal marketing concurrent).
- **Donnees manquantes** : aucune. La trajectoire est limpide : marque morte, exploitable uniquement en mention legacy (H3 unique selon CONVENTIONS audit).

### P7. Ecosysteme Sure* / produits voisins (cluster lateral)

- **Intention** : informationnelle - decouverte ecosysteme.
- **Exemples observes (5)** : `ZipWP free plan`, `Spectra Pro`, `SureRank Pro`, `Otto kit` (variante typographique), `ottokit integrations`.
- **Donnees** :
  - DFS/thruuu : tous presents dans les related searches Google DE de la SERP "OttoKit Free vs Pro".
  - DFS : `ottokit integrations` vol 10/mois DE, trend mensuel **-100 %**, trimestriel -100 % (volume ephemere).
  - DFS : pas de volumes retournes pour ZipWP free plan / Spectra Pro / SureRank Pro dans cet audit cible (audit non lance sur ces seeds).
- **Niveau de confiance** : **Faible** (1 source = related searches Google, sans volumes confirmes a part `ottokit integrations` qui s'effondre).
- **Donnees manquantes** : volumes DFS de chaque produit Sure* en DE (audit dedie a lancer si scope cluster elargi).

### P8. Affiliation et programme partenaire

- **Intention** : commerciale - B2B / agence.
- **Exemples observes (5)** : `Ottokit affiliate` (related search Google DE), "Haben Sie ein Partner-/Wiederverkauferprogramm ?" (H2 bit-integrations.com pos 9), `ottokit reseller`, `ottokit partner program`, `ottokit affiliate program` (deduit du H2 thruuu).
- **Donnees** :
  - thruuu : 1 related search Google DE + 1 H2 frequent sur 1 page du top 10 DE.
  - DFS : pas de volume retourne sur ces requetes en suggestions DE.
- **Niveau de confiance** : **Faible** (2 signaux thruuu, 0 volume confirme).
- **Donnees manquantes** : volumes DFS dedies a lancer si schoolsWP veut activer un angle agence/revendeurs.

### P9. Integrations et capacites techniques

- **Intention** : commerciale - validation technique BOFU.
- **Exemples observes (5)** : `ottokit integrations`, `ottokit vs wp fusion` (titre auto-publie ottokit.com pos 16 SERP DE thruuu), "Wo kann ich Unterstutzung erhalten ?" (H2 sur 2 pages thruuu - support), `ottokit api` (deduit du topic dominant thruuu "connect" 6 pages 49 freq + "trigger" 4 pages 55 freq), `ottokit n8n integration` (deduit du H1 robert-leitinger).
- **Donnees** :
  - DFS : `ottokit integrations` vol 10/mois DE, intent commercial, **trend -100 %** mensuel et trimestriel (donnee volatile).
  - thruuu : auto-comparatif ottokit.com publie ("OttoKit vs WP Fusion") = signal de demande sur les comparaisons d'integrations.
  - thruuu : "Wo kann ich Unterstutzung erhalten ?" 2 pages = preoccupation support.
- **Niveau de confiance** : **Moyen** (1 volume confirme + signaux SERP, mais le seul volume DFS chute a -100 %).
- **Donnees manquantes** : volumes DE des integrations specifiques (`ottokit + woocommerce`, `ottokit + fluentcrm`, etc.) non retournes par DFS.

## Tableau final recapitulatif

| # | Intention | Pattern de requete | 5 exemples concrets | Intention SEO | Niveau business | Funnel | Type de contenu a creer | Angle de conversion | Priorite SEO | Source utilisee | Donnee observee | Niveau de confiance | Donnees manquantes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Navigationnelle / transactionnelle | **Marque sec** | ottokit ; otto kit ; ottokit login ; ottokit wordpress ; ottokit automation | Acces direct produit | Fort | BOFU | Page avis pilier (existe en FR a homologuer en DE) | Capter la marque puis renvoyer vers comparatif Free vs Pro | **1** | DFS + GSC + Google related | vol 110/mois DE, KD 11, trend +57 %, GSC 182 imp pos 9.0 | Fort | CTR reel (0 clic GSC, signal inexploitable) |
| P2 | Commerciale decisionnelle | **Pricing et Free vs Pro** | ottokit pro ; ottokit pricing ; ottokit free vs pro ; ottokit kostenlos ; ottokit ltd | Comparer plans et decider achat | Fort sur intent, faible sur volume | BOFU | Comparatif Free vs Pro DE (article 2898734 - brouillon a publier) | Code promo schoolsWP20 ; cloak affilie /ottokit/ | **1** | DFS + GSC + thruuu titre Reddit | vol 10/mois confirmes (2 keywords), 3/5 volumes "Donnee non disponible", intent commercial p=0.95 a 0.913 | Moyen | Volume reel `free vs pro` et `kostenlos` (sous seuil DFS) |
| P3 | Commerciale evaluation | **Avis et retours d'experience** | ottokit review ; ottokit erfahrungen ; ottokit im test ; ottokit reviews 2026 ; ottokit review wordpress | Lire un avis tiers avant achat | Moyen | MOFU | Page avis DE (homologue `/ottokit-avis-automatisation-wordpress/`) | Avis honnete + capture ecran + CTA decouverte | **2** | DFS + thruuu | DFS volumes "Donnee non disponible" + 4 reviews EN top 10 + 1 review DE pos 13 (robert-leitinger) | Moyen | Volume DE des termes review/erfahrungen |
| P4 | Informationnelle decouverte | **Definition et decouverte produit** | Was ist OttoKit ? ; OttoKit erklart ; OttoKit automation tool ; OttoKit no-code ; Benotige ich Programmierkenntnisse fur OttoKit ? | Comprendre ce qu'est OttoKit | Moyen | TOFU | Section H2 dans pilier OttoKit DE (pas article dedie) | Educatif - lead magnet automatisations | **3** | thruuu | H2 "Was ist OttoKit ?" sur 4 pages top 17 SERP DE | Moyen | Volumes DFS sur requetes "Was ist..." (non retournes) |
| P5 | Commerciale comparative | **Comparatifs alternatives** | ottokit vs zapier ; ottokit vs n8n ; ottokit vs make ; uncanny automator pro ; integrately | Choisir entre OttoKit et un concurrent | Fort | MOFU | Article comparatif DE "OttoKit vs n8n vs Make" (angle non couvert par schoolsWP DE) | Tableau comparatif + biais avoue + CTA Free | **2** | GSC + DFS + thruuu | GSC 4 imp pos 4.2 sur "ottokit vs zapier" ; H1 robert-leitinger ; topic dominant "zapier" 6 pages | Fort | Volumes DE des combos `vs make`, `vs n8n`, `vs uncanny` |
| P6 | Informationnelle rebranding | **Legacy SureTriggers** | suretriggers ; suretriggers wordpress automation plugin ; suretriggers vs zapier ; suretriggers review ; ehemals SureTriggers | Comprendre que SureTriggers est devenu OttoKit | Faible declinant | TOFU | Mention H3 unique dans article OttoKit (`ehemals SureTriggers`) - pas d'article dedie | Capter le trafic residuel sans diluer la marque OttoKit | **4** | DFS + GSC + thruuu titre concurrent | vol 50/mois DE, trend annuel -89 %, GSC 76 imp pos 1.1 sur EN, marque legacy exploitee par bit-integrations | Fort sur le declin | Aucune (trajectoire claire) |
| P7 | Informationnelle ecosysteme | **Ecosysteme Sure* / produits voisins** | ZipWP free plan ; Spectra Pro ; SureRank Pro ; Otto kit ; ottokit integrations | Explorer la galaxie de produits voisins | Faible | TOFU | Cluster lateral (sortie du perimetre OttoKit pur) - pas d'article OttoKit dedie | Cross-sell produits BSF / Brainstorm Force | **4** | thruuu + DFS | 4 produits dans related searches Google DE, 1 seul volume DFS confirme (`ottokit integrations` 10/mois -100 %) | Faible | Volumes DFS sur ZipWP / Spectra Pro / SureRank Pro en DE |
| P8 | Commerciale B2B / agence | **Affiliation et programme partenaire** | Ottokit affiliate ; ottokit partner program ; ottokit reseller ; Haben Sie ein Partner-/Wiederverkauferprogramm ? ; ottokit affiliate program | Activer une source de revenu via OttoKit | Faible | BOFU specifique | Page propre `/de/ottokit-partnerprogramm/` (si revenu affilie schoolsWP justifie la creation) | Cloak affilie schoolsWP `/ottokit/` + valeur ajoutee setup | **4** | thruuu | 1 related search Google DE + 1 H2 concurrent (bit-integrations) | Faible | Volumes DFS dedies (non lances sur ce seed) |
| P9 | Commerciale validation technique | **Integrations et capacites** | ottokit integrations ; ottokit vs wp fusion ; Wo kann ich Unterstutzung erhalten ? ; ottokit api ; ottokit n8n integration | Verifier les capacites techniques avant achat | Moyen volatile | BOFU | Hub `/de/ottokit-integrationen/` ou section H2 dans pilier | Lister integrations cles + lien doc + CTA Free | **3** | DFS + thruuu | vol 10/mois sur `ottokit integrations` mais trend -100 % ; auto-comparatif ottokit.com (pos 16) + H2 support sur 2 pages | Moyen | Volumes DE des integrations specifiques (`+ woocommerce`, `+ fluentcrm`, etc.) |

## Donnees manquantes globales (a collecter pour fiabiliser)

1. **Volumes DE des 6 long-traines en "Donnee non disponible"** (free vs pro, erfahrungen, kostenlos, review, was ist ottokit, ottokit ltd) : seuil DFS < 10/mois - une seconde collecte via Google Ads Keyword Planner (login keyword data) ou seocharger.com (10 a 100 ranges) confirmerait l'existence d'un volume minimal.
2. **Volumes DFS de l'ecosysteme Sure* en DE** (ZipWP, Spectra Pro, SureRank Pro) : audit DFS dedie non lance (hors perimetre OttoKit pur).
3. **Volumes DFS des combinaisons "OttoKit vs n8n / Make / Uncanny / Integrately"** en DE : non retournes par DFS sur le seed OttoKit. Audit DFS dedie sur seed `automatisierung wordpress` recommande pour valider ces combos.
4. **CTR reel concurrent** sur le top 5 SERP DE : aucune source GSC tierce. Estimable uniquement par modeles CTR by position (proxy).
5. **Statut AIO en live** : DataForSEO annonce AIO asynchrone pos 1, thruuu ne le scrape pas. **A verifier en navigation manuelle** avant publication pour confirmer ou infirmer.
6. **Volume marketing affiliation** : pas de donnees FluentAffiliate ou tracker dedie integrees dans cet audit. A cross-checker si schoolsWP veut piloter P8.

## Conclusion data-driven

Les patterns soutenus par au moins **2 sources concordantes** et **volumes confirmes** sont P1 (marque sec), P5 (comparatifs alternatives) et P6 (legacy SureTriggers - confirme decroissant).

P2 (pricing/Free vs Pro), qui est le pattern cible de l'article 2898734, repose sur un intent commercial fort (p=0.913) mais sur des **volumes non disponibles dans la base DFS DE**. La justification SEO de la publication tient au cluster (P1 + P2 + P3 + P5 cumules sur 110+50+10+10+10 = 190/mois confirmes minimum sur le marche DE OttoKit), pas au volume direct du keyword `free vs pro`.

P3 (avis), P4 (definition) et P9 (integrations) sont soutenus par signaux SERP mais sans volume DFS direct - traitables en sections H2 du pilier OttoKit DE plutot qu'en articles dedies.

P7 (ecosysteme) et P8 (affiliation) restent **prospectifs** : signaux trop maigres pour justifier des actions SEO prioritaires sans audit DFS complementaire.

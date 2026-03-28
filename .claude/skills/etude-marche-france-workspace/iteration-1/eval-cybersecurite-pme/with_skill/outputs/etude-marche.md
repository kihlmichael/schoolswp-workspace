# Etude de Marche France -- Cybersecurite pour PME (TPE/PME/ETI)

**Realisee le** : 24 mars 2026
**Fenetre de recency** : septembre 2024 -- mars 2026
**Perimetre** : France uniquement, B2B
**Commanditaire** : schoolsWP OS -- veille strategique sectorielle

---

## A. EXECUTIVE SUMMARY

Le marche francais de la cybersecurite atteint **7,96 milliards EUR en 2025** (+10 % vs 2024) et devrait depasser **8 milliards EUR en 2026**, avec un TCAM de +9,3 % jusqu'en 2029 (objectif 11,36 Md EUR) [web:1][web:2]. La croissance est alimentee par trois forces convergentes : la transposition de la directive NIS2 (15 000 a 18 000 entites concernees en France) [web:5], l'explosion des cyberattaques sur les PME (77 % des incidents traites par l'ANSSI) [web:6], et l'emergence de l'assurance cyber comme nouveau standard (Stoik : 50 M EUR de primes en 2025, +200 %/an) [web:7].

**Cout moyen d'une cyberattaque pour une PME** : entre 14 720 EUR (donnees gouvernementales medianes) et 466 000 EUR (estimation incluant pertes indirectes), avec 60 % des PME victimes qui ferment dans les 18 mois [web:6]. Le ratio cout d'un audit (8 000 EUR) vs cout d'un incident (50 000 EUR minimum) rend l'investissement en cybersecurite economiquement rationnel.

**Opportunite strategique** : le segment TPE/PME (< 250 salaries) reste massivement sous-equipe. Seulement une minorite dispose d'un prestataire cybersecurite dedie. Le marche est fragmente entre freelances (800-1 200 EUR/j), MSSP mid-market (1 500-8 000 EUR/mois) et ESN premium (TJM > 1 500 EUR). NIS2 cree une demande forcee d'audits de conformite avec une hausse tarifaire de 10-15 % sur ce segment [web:2].

---

## B. SEGMENTATION DU MARCHE

### Segment 1 -- Consultant independant / Micro-cabinet (1-10 personnes)

| Critere | Detail |
|---|---|
| **Profil type** | Freelance OSCP/CEH, ex-RSSI, micro-SARL specialisee |
| **Cible** | TPE, PME < 50 salaries, associations |
| **TJM moyen** | 600-1 200 EUR HT (junior-senior) ; 1 200-1 800 EUR HT (expert PASSI) [web:2][web:4] |
| **Services** | Pentest ponctuel, audit flash, sensibilisation, mise en conformite RGPD/NIS2 |
| **Forces** | Prix accessible, proximite, reactivite |
| **Faiblesses** | Pas de SOC, pas de couverture 24/7, capacite limitee en gestion de crise |
| **Part de marche estimee** | ~20 % du segment PME [ESTIME] |

### Segment 2 -- MSSP / Prestataire intermediaire (10-200 personnes)

| Critere | Detail |
|---|---|
| **Profil type** | MSSP regional, pure-player cyber mid-market (Advens, ITrust, Cyna, Guardis) |
| **Cible** | PME 50-500 salaries, ETI |
| **Forfait mensuel** | SOC manage : 1 500-4 000 EUR/mois ; MSSP complet : 3 000-8 000 EUR/mois [web:3] |
| **Services** | SOC manage 24/7, MDR/XDR, audit PASSI, conformite NIS2, CSIRT |
| **Forces** | Couverture continue, expertise sectorielle, tarifs mutualises |
| **Faiblesses** | SLA parfois flous, dependance a un outil unique (SIEM/EDR vendor lock-in) |
| **Part de marche estimee** | ~35 % du segment PME [ESTIME] |

### Segment 3 -- ESN / Pure player premium (200+ personnes)

| Critere | Detail |
|---|---|
| **Profil type** | Orange Cyberdefense, Capgemini, Thales, Atos/Eviden, Wavestone |
| **Cible** | ETI, grands comptes, administrations, OIV/OSE |
| **TJM moyen** | 1 500-2 500 EUR HT (consultant senior/manager) [ESTIME] |
| **Services** | SOC/CSIRT interne, red team, GRC, conformite NIS2/LPM, conseil strategique |
| **Forces** | Certifications ANSSI (PASSI, PRIS, PDIS), capacite industrielle, couverture internationale |
| **Faiblesses** | Ticket d'entree eleve (> 100 K EUR/an), rigidite contractuelle, sous-traitance frequente |
| **Part de marche estimee** | ~45 % du marche total (mais < 15 % du segment pure PME) [ESTIME] |

---

## C. TABLEAU TARIFS SEGMENTE

### C.1 Pentest / Test d'intrusion

| Prestation | Fourchette HT | Duree type | Commentaire |
|---|---|---|---|
| Pentest web app (1 application) | 3 000 - 8 000 EUR | 3-5 jours | Methodologie OWASP Top 10 |
| Pentest reseau externe | 4 000 - 10 000 EUR | 4-7 jours | Scope : IP publiques, DNS, VPN |
| Pentest reseau interne + AD | 6 000 - 15 000 EUR | 6-10 jours | Active Directory, lateral movement [web:4] |
| Pentest complet (web + reseau + social eng.) | 15 000 - 30 000 EUR | 10-20 jours | Red team light |
| Pentest automatise / IA (ex: Egide) | 500 - 3 000 EUR | 1-2 jours | Scan + rapport, sans intervention humaine [web:4] |

*Source principale : [web:4] -- TJM pentester confirme : 800-1 800 EUR/jour*

### C.2 Audit de securite / Conformite

| Prestation | Fourchette HT | Duree type | Commentaire |
|---|---|---|---|
| Audit flash / diagnostic cyber | 1 500 - 5 000 EUR | 1-3 jours | 80 % des failles critiques identifiees [web:2][web:4] |
| Audit complet PME (< 100 postes) | 5 000 - 15 000 EUR | 5-10 jours | Technique + organisationnel |
| Audit conformite NIS2 | 8 000 - 25 000 EUR | 5-15 jours | +10-15 % vs audit standard (effet NIS2) [web:2] |
| Audit PASSI qualifie ANSSI | 15 000 - 50 000 EUR | 10-25 jours | Obligatoire pour OIV/OSE [web:8] |
| Audit RGPD + cyber croise | 3 000 - 10 000 EUR | 3-7 jours | DPO externalisable en complement |

### C.3 SOC manage / Supervision continue

| Prestation | Fourchette HT/mois | Perimetre | Commentaire |
|---|---|---|---|
| EDR manage seul | 500 - 1 500 EUR | Endpoints uniquement | SentinelOne, CrowdStrike, MS Defender |
| SOC manage mid-market | 1 500 - 4 000 EUR | Endpoints + logs reseau | Monitoring 24/7, SLA 4h [web:3] |
| MSSP complet | 3 000 - 8 000 EUR | Full stack (FW, EDR, SIEM, vuln scan) | Inclut conformite et reporting [web:3] |
| SOC + CSIRT (reponse a incident) | 5 000 - 12 000 EUR | Full stack + astreinte incident | Intervention sur site incluse |

### C.4 Formation / Sensibilisation

| Prestation | Fourchette HT | Format | Commentaire |
|---|---|---|---|
| Sensibilisation phishing (campagne) | 500 - 3 000 EUR | En ligne, 1-3 mois | Simulation + rapport |
| Formation cybersecurite dirigeants | 1 500 - 4 000 EUR | 1 journee presentiel | NIS2 impose la formation des dirigeants |
| Formation technique equipe IT | 2 000 - 6 000 EUR | 2-3 jours | Securisation AD, hardening, incident response |
| Programme annuel sensibilisation | 3 000 - 10 000 EUR | 12 mois, modules mensuels | E-learning + phishing simule |

### C.5 Assurance cyber

| Assureur | Prime annuelle HT | CA couvert | Garanties cles |
|---|---|---|---|
| Stoik | 1 000 - 8 000 EUR | < 50 M EUR CA | Prevention tech + detection + gestion de crise + indemnisation [web:7] |
| Dattak | 800 - 6 000 EUR | < 50 M EUR CA | Audit de vulnerabilites inclus + couverture sinistre [web:7] |
| Onlynnov | 1 200 - 10 000 EUR | < 100 M EUR CA | Specialise tech/startups [web:7] |
| Hiscox / AXA (traditionnels) | 1 500 - 15 000 EUR | Variable | Couverture large, franchise elevee |

*Marche en forte croissance : +15-20 %/an, primes mondiales vers 44 Md$ d'ici 2032 [web:7]*

---

## D. CONCURRENTS LEADERS

### D.1 Orange Cyberdefense

| Critere | Detail |
|---|---|
| **CA cybersecurite** | ~1 Md EUR (monde), leader France [web:10] |
| **Effectif** | 3 000+ experts cyber |
| **Positionnement** | Leader ISG 2025 dans 6 quadrants France [web:10] |
| **Offre PME** | Cyber Protection a partir de 10 EUR/mois/poste (12 mois) [web:10] |
| **Certifications** | PASSI, PRIS, PDIS qualifie ANSSI |
| **Force** | Marque Orange = confiance ; capacite industrielle ; SOC 24/7 mondial |
| **Faiblesse** | Perception "trop grand pour les PME" ; rigidite contractuelle |

### D.2 Advens

| Critere | Detail |
|---|---|
| **CA** | ~100 M EUR [ESTIME] |
| **Effectif** | 600+ personnes |
| **Positionnement** | Leader ISG 2025 dans 3 quadrants ; pure-player cyber FR [web:10] |
| **Offre** | SOC manage mySOC, consulting, audit PASSI, GRC |
| **Modele** | Entreprise a mission (reversement de dividendes a des causes sociales) |
| **Force** | SOC souverain francais ; positionnement ethique differenciant |
| **Faiblesse** | Notoriete inferieure a Orange ; tarifs mid-market, peu accessible aux TPE |

### D.3 Almond (ex-Amossys + Almond)

| Critere | Detail |
|---|---|
| **CA** | ~50 M EUR [ESTIME] |
| **Effectif** | 350+ personnes |
| **Positionnement** | Rising Star ISG 2025 dans 2 quadrants [web:10] |
| **Offre** | Audit/pentest, SOC manage, conseil GRC, formation |
| **Force** | Forte expertise technique (pentest, red team) ; croissance rapide |
| **Faiblesse** | Taille intermediaire ; couverture geographique limitee vs ESN nationales |

### D.4 ITrust

| Critere | Detail |
|---|---|
| **Siege** | Toulouse |
| **Positionnement** | Editeur + MSSP souverain, technologie SIEM/XDR proprietaire (Reveelium) |
| **Offre PME** | SOC manage adapte PME, scanner de vulnerabilites IKare |
| **Force** | Solution souveraine francaise ; tarifs competitifs vs leaders ; label ExpertCyber |
| **Faiblesse** | Taille limitee ; ecosysteme partenaires restreint |

### D.5 Stoik (InsurTech + CyberSec)

| Critere | Detail |
|---|---|
| **Levees** | 70 M EUR total (Series C : 20 M EUR, janvier 2026) [web:7] |
| **Clients** | 10 000+ entreprises assurees en Europe, +600/mois [web:7] |
| **Primes** | ~50 M EUR bruts en 2025, croissance +200 %/an [web:7] |
| **Modele** | Assurance cyber + prevention technique + detection + gestion de crise |
| **Force** | Modele integre unique (assurance + cyber) ; croissance explosive ; backed by a16z |
| **Faiblesse** | Rentabilite non prouvee ; dependance au marche de la reassurance |

### D.6 Dattak (InsurTech cyber)

| Critere | Detail |
|---|---|
| **Levees** | 25 M EUR total (seed 7 M EUR + 18 M EUR) [web:7] |
| **Fondateurs** | Benoit Grouchko, Charlotte Couallier (dec. 2021) |
| **Modele** | Assurance cyber pour TPE/PME via courtiers + audit vulnerabilites integre |
| **Cible** | TPE/PME et startups tech |
| **Force** | Approche auditee (scoring de risque avant souscription) ; distribution via courtiers |
| **Faiblesse** | Plus petit que Stoik ; notoriete en construction |

### D.7 Autres acteurs notables

| Acteur | Segment | Specifite |
|---|---|---|
| **Wavestone** | Conseil GRC premium | Cabinet de conseil, TJM eleve, ETI/grands comptes |
| **Thales / Atos-Eviden** | Defense / OIV | Souverainete, cloud de confiance, tres grands comptes |
| **Capgemini** | ESN globale | Cyber integre dans offre SI globale |
| **Cyna** | MSSP pour MSP/revendeurs | SOC manage en marque blanche pour infogerants |
| **Guardis** | MSSP mid-market | Focus PME/ETI, offres packagées |
| **Deefense** | Micro-cabinet conseil | Audits accessibles PME, contenu pedagogique |

---

## E. PLAINTES CLIENTS (5 PRINCIPALES)

### E.1 Opacite tarifaire et surfacturation

**Frequence** : Tres elevee
**Description** : Les PME decrivent regulierement une difficulte a obtenir des devis clairs et comparables. Les tarifs varient du simple au quintuple pour des prestations similaires (pentest : 3 000 a 30 000 EUR). Certains prestataires facturent des "audits" qui se limitent a un scan automatise revendu 5-10x son cout reel.
**Verbatim type** : "On nous a facture 12 000 EUR pour un rapport de 15 pages genere par un outil automatique." [ESTIME d'apres forums et retours terrain]

### E.2 Incomprehension du livrable / jargon technique

**Frequence** : Elevee
**Description** : Les rapports d'audit sont rediges dans un jargon technique incomprehensible pour les dirigeants de PME. Le client paie mais ne sait pas quoi faire du livrable. Absence quasi systematique de plan d'action priorise et actionnable.
**Impact** : Le client ne corrige pas les failles identifiees, rendant l'audit inutile.

### E.3 Arnaque au faux support technique

**Frequence** : Tres elevee (signalements massifs sur cybermalveillance.gouv.fr) [web:9]
**Description** : Escroquerie par message d'alerte anxiogene bloquant l'ecran, poussant a appeler un faux support et payer un pseudo-depannage. Sophistication croissante des montants preleves. Microsoft, Cybermalveillance.gouv.fr et le Parquet de Paris ont lance un appel conjoint a la mobilisation en juillet 2025 [web:9].
**Impact PME** : Perte financiere directe + compromission potentielle du SI.

### E.4 Engagement contractuel disproportionne

**Frequence** : Moderee a elevee
**Description** : Les MSSP et infogerants imposent des engagements de 24-36 mois avec des clauses de sortie penalisantes. Le perimetre est flou. Les SLA ne sont pas mesures ni reportes au client.
**Verbatim type** : "On a signe pour 3 ans, on ne sait toujours pas ce qu'ils surveillent exactement." [ESTIME]

### E.5 Absence de suivi post-audit

**Frequence** : Elevee
**Description** : Le prestataire livre le rapport d'audit puis disparait. Pas d'accompagnement a la remediation, pas de retest, pas de suivi de la mise en conformite. Le client se retrouve seul avec une liste de 47 vulnerabilites et aucune idee de par ou commencer.
**Impact** : Le client percoit la cybersecurite comme un cout sans valeur, ce qui freine les investissements futurs.

---

## F. SYNTHESE STRATEGIQUE POUR schoolsWP

### F.1 Opportunites identifiees

1. **NIS2 comme levier de demande forcee** : 15 000-18 000 entites francaises doivent se mettre en conformite d'ici 2029. Les PME de 50+ salaries dans les 18 secteurs couverts cherchent activement des prestataires accessibles. C'est un marche de contenu SEO massif (mots-cles : "conformite NIS2 PME", "audit NIS2 prix", "obligation NIS2 France").

2. **Gap editorial sur le segment PME** : Les contenus existants sont soit trop techniques (orientes RSSI/DSI), soit trop commerciaux (pages vendeurs). Il manque un contenu pedagogique, neutre et actionnable pour les dirigeants de PME qui decouvrent le sujet.

3. **Assurance cyber = nouveau pilier thematique** : Stoik et Dattak creent une categorie. Les mots-cles "assurance cyber PME", "Stoik avis", "Dattak vs Stoik" sont en croissance avec une concurrence editoriale encore faible [ESTIME].

4. **Contenu comparatif a forte valeur** : Les PME cherchent des comparatifs neutres ("MSSP vs SOC interne", "quel prestataire cybersecurite PME", "pentest prix 2026"). Ces requetes a intent decisive/comparative sont le coeur de competence de schoolsWP.

5. **Affiliation et lead generation** : Les assureurs cyber (Stoik, Dattak) et les MSSP mid-market ont des programmes partenaires. Le contenu schoolsWP peut generer des leads qualifies via des comparatifs et des guides.

### F.2 Risques

1. **Complexite technique du domaine** : La cybersecurite exige une precision factuelle elevee. Une erreur de conseil peut engager la responsabilite editoriale (ex: recommander un outil non adapte).

2. **Vitesse d'obsolescence** : Les menaces, les outils et les reglementations evoluent tres vite. Un contenu de mars 2026 peut etre obsolete en septembre 2026.

3. **Concurrence editoriale croissante** : Les acteurs du marche (Stoik, ITrust, Orange) investissent massivement dans le content marketing. Le SEO devient competitif sur les mots-cles transactionnels.

4. **Risque reputationnel** : Recommander un prestataire qui fait ensuite l'objet de plaintes peut nuire a la credibilite de schoolsWP.

### F.3 Trois offres de contenu recommandees

**Offre 1 -- Pilier "Cybersecurite PME" (SEO editorial)**

- Pillar page : "Cybersecurite PME France : le guide complet [2026]"
- Cluster de 15-20 articles : comparatifs MSSP, guide NIS2, tarifs pentest, assurance cyber, sensibilisation employes
- Intent cible : informationnelle + decisive
- Monetisation : affiliation assurance cyber (Stoik/Dattak), lead gen prestataires
- **Garantie schoolsWP** : chaque article audite par le pipeline publish_ready (score >= 85), sources verifiees, mise a jour trimestrielle

**Offre 2 -- Guide "Conformite NIS2 pour PME" (lead magnet)**

- Format : PDF 25-30 pages, telechargeable contre email
- Contenu : checklist des 15 objectifs "entites importantes", auto-diagnostic, budget type, annuaire prestataires PASSI
- Distribution : SEO + LinkedIn + partenariat courtiers en assurance cyber
- **Garantie schoolsWP** : contenu verifie vs texte officiel de transposition, tutoiement systematique, zero jargon non explique

**Offre 3 -- Comparateur interactif "Prestataire Cybersecurite PME"**

- Format : outil web (formulaire -> recommandation personnalisee)
- Criteres : taille entreprise, budget, secteur, niveau de maturite, obligations reglementaires
- Sortie : 3 prestataires recommandes + estimation budgetaire + checklist questions a poser
- Monetisation : leads qualifies vers MSSP partenaires (CPL)
- **Garantie schoolsWP** : selection neutre basee sur criteres objectifs (certifications, SLA, tarifs publics), pas de placement paye non declare

### F.4 Garanties editoriales schoolsWP

Conformement aux principes de la marque :

- **Transparence tarifaire** : tous les prix mentionnes sont HT, sources, et dates. Les estimations sont marquees [ESTIME].
- **Neutralite** : aucun placement produit non declare. Les liens d'affiliation sont identifies comme tels.
- **Tutoiement systematique** : le contenu s'adresse au dirigeant de PME en le tutoyant, sans condescendance.
- **Mots interdits** : jamais de "revolutionnaire", "game changer", "en un clic", "sans effort" dans les contenus cybersecurite.
- **Mise a jour** : engagement de revision trimestrielle des donnees tarifaires et reglementaires.
- **Scoring qualite** : chaque article passe par le pipeline publish_ready avec un seuil minimum de 85/100 (SEO x 0.30 + LLM x 0.25 + Conversion x 0.25 + Autorite x 0.20).

---

## G. SOURCES COMPLETES

| Ref | Source | URL |
|---|---|---|
| [web:1] | Jedha -- Chiffres marche cybersecurite 2026 | https://www.jedha.co/formation-cybersecurite/chiffres-sur-le-marche-de-la-cybersecurite-en-2025 |
| [web:2] | Deefense -- Prix audit cybersecurite PME 2025 | https://deefense.fr/cyber-et-it/prix-audit-cybersecurite-pme-budget-et-tarifs-detailles-2025 |
| [web:3] | Guardis -- MSSP France 2025 fournisseurs | https://www.guardis.fr/cybersecurite-et-mssp/mssps-france-2025-fournisseurs/ |
| [web:4] | Invictis -- Tarif pentest 2026 | https://invictis.fr/quel-tarif-pour-un-pentest/ |
| [web:5] | Orange Cyberdefense -- NIS2 obligations et echeances | https://www.orangecyberdefense.com/fr/insights/blog/nis-2-obligations-echeances-sanctions-et-mise-en-conformite |
| [web:6] | Cybermalveillance.gouv.fr -- Barometre maturite cyber TPE-PME 2025 | https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/etude-maturite-cyber-tpe-pme-2025 |
| [web:7] | Plateya -- Assurance cyber Stoik Onlynnov Dattak comparaison 2026 | https://www.plateya.fr/blog/detail/assurance-cyber-comparaison-stoik-onlynnov-et-dattak-2026 |
| [web:8] | ANSSI -- Prestataires labellises MesServicesCyber | https://messervices.cyber.gouv.fr/prestataires-labellises |
| [web:9] | Cybermalveillance.gouv.fr -- Arnaque faux support technique | https://www.cybermalveillance.gouv.fr/tous-nos-contenus/fiches-reflexes/arnaques-au-faux-support-technique |
| [web:10] | Orange Cyberdefense -- Temoignages clients et positionnement ISG 2025 | https://www.orangecyberdefense.com/fr/temoignages-clients |
| [web:11] | ChannelNews -- Marche francais cybersecurite +10 % en 2025 | https://www.channelnews.fr/le-marche-francais-de-la-cybersecurite-va-encore-progresser-de-10-en-2025-145191 |
| [web:12] | Copla -- NIS2 France implementation timeline 2026 | https://copla.com/blog/compliance-regulations/nis2-directive-regulations-and-implementation-in-france/ |
| [web:13] | Rehackt -- Cybersecurite France grand decalage 2025 perspectives 2026 | https://rehackt.fr/cybersecurite-en-france-le-grand-decalage-de-2025-et-les-perspectives-2026/ |
| [web:14] | Sekost -- Cout moyen cyberattaque chiffres 2025 | https://sekost.fr/blog/securite/cout-moyen-cyberattaque/ |
| [web:15] | Malt -- Barometre tarifs experts cybersecurite freelances 2026 | https://www.malt.fr/t/barometre-tarifs/tech/expert-cybersecurite |
| [web:16] | Copwell -- Cybersecurite TPE/PME 2026 solutions souveraines budget | https://copwell.fr/cybersecurite-tpe-pme-2026-solutions-souveraines-budget/ |
| [web:17] | SkillX -- Cout cybersecurite PME | https://skillx.fr/cout-cybersecurite-pme/ |
| [web:18] | Codeur.com -- Tarif consultant cybersecurite fevrier 2026 | https://www.codeur.com/consultant/securite/tarif |
| [web:19] | Keyrus/Opsky -- SOC manage vs MSSP pour PME | https://web.keyrus.com/opsky-blog/partenaire-cybersecurite-pme-guide-de-selection |
| [web:20] | Exaegis -- Blueprint SOC manages mid-market 2024-2025 | https://research.exaegis.com/blueprint-soc-manages-mid-market-2024-2025 |
| [web:21] | Laucked -- Prix pentest PME 2025 | https://www.laucked.com/blog/prix-pentest-pme |
| [web:22] | Usine Digitale -- Stoik leve 20 M EUR | https://www.usine-digitale.fr/cybersecurite/assurance-cyber-stoik-leve-20-millions-deuros.html |
| [web:23] | FrenchWeb -- Dattak startup assurance cyber PME | https://www.frenchweb.fr/connaissez-vous-dattak-la-startup-qui-veut-assurer-les-pme-en-cas-de-cyberattaque/436425 |
| [web:24] | SFR Business -- Cout reel cyberattaque PME | https://www.sfrbusiness.fr/room/securite/cout-reel-cyberattaque-pme.html |
| [web:25] | BNP Paribas Entreprises -- Cyberattaque combien ca coute | https://banqueentreprise.bnpparibas/post/anticiper-les-risques/article/cyberattaque-combien-ca-coute.html |

---

*Etude realisee pour schoolsWP OS -- usage interne, veille strategique et planification editoriale.*
*Les donnees marquees [ESTIME] sont des estimations basees sur le croisement de sources partielles et l'expertise sectorielle.*
*Derniere mise a jour : 24 mars 2026.*

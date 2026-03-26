---
name: schoolswp-email-engine
description: Agent schoolsWP: schoolswp-email-engine
model: sonnet
---

# schoolsWP Email Engine

Role
- Sequences email conversion (7 jours, nurturing, offres).

Quand l'utiliser
- Toute demande email / sequence / automation.

---

## STRUCTURE 7 JOURS (LOGIQUE)

J1 Declic
J2 Probleme reel
J3 Methode
J4 Preuve
J5 Autorite
J6 Opportunite
J7 Decision

Regles
- Emails courts
- 1 idee = 1 email
- CTA clair

## SEQUENCE 7 JOURS — VERSION COMPLETE

JOUR 1 — Objet : Pourquoi ton site ne genere rien
La majorite des sites WordPress ont un probleme simple :
ils sont jolis, mais inutiles.
Un site devient un levier quand il sert un systeme.
Demain, je t'explique pourquoi le trafic ne suffit pas.

JOUR 2 — Objet : Le mythe du trafic
Le trafic sans structure ne vaut rien.
Pas de capture email, pas de sequence, pas d'offre claire.
Demain, je te detaille le modele.

JOUR 3 — Objet : Le modele en 3 piliers
1 Trafic strategique
2 Capture intelligente
3 Offre claire
Lien : [Article pilier]
Demain : cas reel.

JOUR 4 — Objet : 2 000 visiteurs -> 3 500 EUR
Cas concret, meme trafic, structure differente.
Si tu veux appliquer ce modele, je peux t'aider.

JOUR 5 — Objet : L'erreur des freelances WP
Trop de plugins, pas de funnel, pas de positionnement.
Demain : plan 30 jours.

JOUR 6 — Objet : Ton plan en 30 jours
S1 offre + cible
S2 page pilier + lead magnet
S3 sequence email
S4 CTA + offre
CTA : [Offre]

JOUR 7 — Objet : Dernier rappel
Resume, decision, CTA final.

## KPI CIBLES

- Open rate 35-50%
- CTR 8-15%
- Conversion offre 2-5%

## SEGMENTATION SIMPLE

- Clic article SEO -> formation SEO
- Clic audit -> consulting
- Clic stack outils -> affiliation

## SEQUENCE BOFU — CONVERSION DIRECTE (5 EMAILS)

Email 1 — Confrontation
Objet : Ton site ne manque pas de trafic. Il manque de structure.
Pre-header : Et ca te coute chaque semaine.
Texte :
Tu n'as pas un probleme de plugin ni de theme. Tu as un probleme d'architecture.
Un site sans tunnel clair = trafic perdu, leads perdus, revenu instable.
Tu peux optimiser des details ou structurer le systeme.
CTA : [Audit / Formation]

Email 2 — Cout de l'inaction
Objet : Ce que ton site te fait perdre (calcul simple)
Pre-header : Les chiffres ne mentent pas.
Exemple : 1 000 visiteurs, 0,5% = 5 leads. A 2% = 20 leads. 15 opportunites / mois.
Tu ne manques pas de trafic. Tu manques de conversion.
CTA : [Audit]

Email 3 — Autorite + preuve
Objet : Ce que je fais differemment
Pre-header : Pas du bricolage.
Je revois offre, tunnel, stack, maillage. Resultat : clarte, coherence, conversion.
Ce n'est pas une formation de plus. C'est une architecture complete.
CTA : [Details]

Email 4 — Urgence maitrisee
Objet : J'ouvre 5 creneaux ce mois-ci
Pre-header : Pas plus.
Je limite volontairement. 5 audits strategiques ce mois-ci.
Si trafic existe et tu veux passer un cap, c'est maintenant.
CTA : [Calendrier]

Email 5 — Dernier rappel
Objet : Je ferme les creneaux ce soir
Pre-header : Apres, mois prochain.
Soit tu continues. Soit tu structures. Pas d'entre-deux.
WordPress peut etre un centre de cout ou un actif strategique.
CTA : [Reserve]

KPI cibles
- Open rate > 40%
- CTR > 12%
- Conversion audit 3-8%
- Conversion formation premium 2-5%

## AUTOMATION FLUENTCRM + FLUENTCART + TUTORLMS (RESUME)

Triggers
- FluentCart: Order Created / Checkout Completed (abandon)
- FluentCart: Order Paid / Completed (client)
- TutorLMS: Course Enrolled (activation)

Tags produits
- BUY:Paid
- BUY:Training:<nom>
- BUY:Audit
- LMS:Enrolled:<cours>

Flows
FC1 Abandon checkout
- Tag BOFU:Visited:Checkout
- Email abandon 1h / 24h / 48h

FC2 Paiement confirme
- Apply BUY:Paid + STAGE:CUSTOMER
- Stop onboarding/BOFU/reengage
- Start SEQ:Customer:Audit:Prep ou SEQ:Customer:Training

TL1 Enrollement cours
- Apply LMS:Enrolled:<cours>
- Start SEQ:LMS:Activation:7d

BOFU Audit (3 emails)
- A1 Diagnostic clair + CTA audit
- A2 3 erreurs + CTA audit
- A3 Trancher + CTA audit

BOFU Formation (3 emails)
- F1 Methode + CTA formation
- F2 Systeme + CTA formation
- F3 Decision + CTA formation

## SEQUENCE UPSELL 30 JOURS (RESUME)

Phases
1) Activation J1-7
2) Autorite avancee J8-14
3) Tension business J15-21
4) Conversion premium J22-30

Emails (18)
J1 Diagnostic rapide (5 questions) + checklist avancee
J2 Erreur invisible + micro-optimisation
J3 Resultat rapide + test
J4 Stack avancee + tunnel segmente
J5 Positionnement (outil vs levier)
J8 Framework complet (Attraction -> Conversion)
J9 Erreur strategique (trafic != conversion)
J10 Etude de cas detaillee + CTA soft
J11 Objection "je peux le faire seul"
J15 Cout cache + calcul simple
J16 Comparaison freelance structure vs disperse
J17 Vision 12 mois
J18 Story perso (arreter de tester)
J22 Presentation audit
J23 FAQ audit
J24 Bonus semaine
J26 Rappel creneaux
J28 Dernier appel

CTA finaux
- Audit strategique
- Programme premium
- Diagnostic personnalise


## SEQUENCE LANCEMENT LOW-TICKET (5 JOURS)

Email 1 — Annonce
Objet : J'ai cree quelque chose de simple
Pre-header : Pour arreter de bricoler ton WordPress.
Texte :
Lancement formation courte "WordPress Rentable en 7 Jours".
Systeme simple : structure, premiers leads, stack coherente.
CTA : [Acces]

Email 2 — Probleme
Objet : Pourquoi ton site ne genere rien
Pre-header : Ce n'est pas ton theme.
Probleme = structure manquante (pilier, aimant, sequence, offre).
CTA : [Acces]

Email 3 — Solution
Objet : Ce que tu vas reellement obtenir
Pre-header : 2-3h. Pas 40.
- Architecture claire
- Stack optimisee
- Template pilier
- Tunnel pret
- Scripts email
CTA : [Acces]

Email 4 — Preuve + bonus
Objet : +120% trafic apres structuration
Pre-header : Pas grace au design.
Cas concret + bonus (checklist stack 2026 + template pilier)
CTA : [Acces]

Email 5 — Urgence
Objet : Dernieres heures
Pre-header : Le bonus disparait.
Rappel + decision + CTA.

KPI cible
- Open 35-45%
- CTR 8-15%
- Conversion 8-12% leads chauds

## SEQUENCE LOW-TICKET SEGMENTEE (DEBUTANT / FREELANCE)

Segment Debutant (J0-J4)
J0 Objet : Tu peux creer ton site (meme sans technique)
- Rassurance + plan simple
J1 Objet : L'erreur n1 des debutants
- Theme/plugins vs structure
J2 Objet : Le plan WordPress en 4 etapes
- Theme propre + 4 plugins + page claire + formulaire
CTA : [Lien]
J3 Objet : "Et si je ne suis pas pret ?"
- 2-3h, checklist, rythme, garantie
J4 Objet : Soit tu demarres. Soit tu procrastines.
CTA : [Lien]

Segment Freelance (J0-J4)
J0 Objet : Ton site doit generer des leads
- Tunnel + lead magnet + sequence
J1 Objet : Combien de leads tu perds ?
- Calcul conversion
J2 Objet : Stack trafic -> clients
- Pilier + aimant + email 5 jours + offre
CTA : [Lien]
J3 Objet : 10 leads de plus / mois = ?
- ROI simple vs prix
J4 Objet : 37 EUR pour structurer ton tunnel
CTA : [Lien]

Implementation tags (FluentCRM)
- Lead magnet "Creer son site" -> SEG:Beginner
- Lead magnet "Audit trafic" -> SEG:Freelance
- Page SEO visitee 2x -> SEG:Freelance

## SEQUENCE EVERGREEN 30 JOURS (SCHOOLS WP)

Structure
Phase 1 J1-5 : activation + low-ticket
Phase 2 J6-12 : autorite + affiliation
Phase 3 J13-21 : conversion offre principale
Phase 4 J22-30 : positionnement premium

Phase 1 (J1-5)
- Sequence low-ticket 5 jours (voir section)

Phase 2 (J6-12)
J6 Objet : Ma stack WordPress complete (CTA comparatif)
J8 Objet : Les 5 erreurs WordPress invisibles (cluster SEO)
J10 Objet : De 0 a 3k/mois avec WordPress (cas)
J12 Objet : Si tu veux aller plus loin (upsell 97)

Phase 3 (J13-21)
J13 Positionnement fort (pourquoi stagnent)
J15 Framework schoolsWP (cocon/tunnel/stack) + CTA offre principale
J17 ROI chiffre
J19 Objections (prix/temps/niveau)
J21 Offre limitee (bonus 72h + garantie)

Phase 4 (J22-30)
J22 Mini audit 5 questions
J24 Cas audit 90 jours (avant/apres)
J26 Appel a candidature (3 projets)
J28 Vision long terme (WP levier)
J30 Recadrage final (appliquer seul vs accompagnement)

Logique
- Monétise J1-5
- Affiliation J6-12
- Vends offre coeur J13-21
- Filtre premium J22-30

Optimisations
- Scoring comportemental
- Sortie auto si achat premium
- Relance non-ouvreurs
- Reengage J45

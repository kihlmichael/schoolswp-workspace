---
name: schoolswp-automation
description: Agent schoolsWP: schoolswp-automation
model: sonnet
---

# schoolsWP Automation (FluentCRM + FluentCart + TutorLMS)

Role
- Automations, tags, triggers, sequences, stop rules.

Quand l'utiliser
- Toute demande d'automatisation CRM/LMS/paiement.

---

## TAXONOMIE TAGS

Sources
- SRC:LeadMagnet:Stack
- SRC:LeadMagnet:SEOChecklist
- SRC:Organic:Blog
- SRC:Organic:YouTube
- SRC:Organic:LinkedIn

Persona
- PERS:Beginner
- PERS:Freelance
- PERS:Agency

Niveau
- LVL:Beginner
- LVL:Intermediate
- LVL:Advanced

Intent
- INT:SEO
- INT:Performance
- INT:CRM
- INT:LMS
- INT:Funnel

Funnel
- STAGE:TOFU
- STAGE:MOFU
- STAGE:BOFU
- STAGE:CUSTOMER

Engagement
- ENG:Click
- ENG:Click
- ENG:Click
- ENG:Inactive14
- ENG:Inactive30

Achat
- BUY:Paid
- BUY:Training:<nom>
- BUY:Audit
- BUY:Sub:Active
- BUY:Sub:Cancelled
- BUY:Refunded

LMS
- LMS:Enrolled:<cours>
- LMS:Completed:<cours>

## TRIGGERS (STACK FLUENT)

FluentCart
- Order Created / Checkout Completed (abandon)
- Payment Succeeded / Order Paid / Completed (client)
- Subscription Created / Renewed / Cancelled
- Refunded

TutorLMS
- Course Enrolled
- Course Completed

## STOP RULES

Des que STAGE:CUSTOMER est applique :
- Stop SEQ:Onboarding:*
- Stop SEQ:BOFU:*
- Stop SEQ:Reengage:*

## FLOW FC1 — ABANDON CHECKOUT

Trigger : Checkout Completed
- Tag BOFU:Visited:Checkout
- Delay 1h -> Email abandon 1
- Delay 23h -> Email abandon 2
- Delay 48h -> Email abandon 3 (soft)
Condition : stop si BUY:Paid

## FLOW FC2 — PAIEMENT CONFIRME

Trigger : Order Paid
- Apply BUY:Paid + STAGE:CUSTOMER
- Add list Clients
- Remove Inactive tags
- Start SEQ:Customer:Audit:Prep OU SEQ:Customer:Training

## FLOW TL1 — ENROLLEMENT COURS

Trigger : Course Enrolled
- Apply LMS:Enrolled:<cours>
- Start SEQ:LMS:Activation:7d

## SEQUENCES (RESUME)

SEQ:Onboarding:Freelance:7d
- J1 bienvenue
- J2 erreur
- J3 framework
- J4 stack
- J5 cas
- J6 vision
- J7 offre

SEQ:BOFU:Audit:3
- A1 diagnostic clair
- A2 3 erreurs
- A3 trancher

SEQ:BOFU:Training:3
- F1 methode
- F2 systeme
- F3 decision

SEQ:Customer:Training:Onboarding:5
- Acces cours
- Quick win
- Rappel progression
- Proof
- Upsell soft

SEQ:LMS:Activation:7d
- Jour 1 activation
- Jour 3 progression
- Jour 5 blocages
- Jour 7 completion

## LEAD SCORING (CHAUD / TIEDE / FROID)

Points
- Open email +1
- Click email +3
- Download lead magnet +5
- Visite page formation +8
- Visite page audit +10
- Retour 2x page offre +12
- Repond email +15

Seuils
- 0-10 : Froid
- 11-25 : Tiede
- 26-50 : Chaud
- 50+ : Ultra chaud

Actions
- Froid : nurturing educatif
- Tiede : preuves / cas
- Chaud : sequence conversion + RDV
- Ultra chaud : email perso + calendrier direct

## WORKFLOW VISUEL (TEXTE)

Trafic -> Lead Magnet -> Tag Segment -> Sequence 7 jours
-> Scoring -> Froid/Tiede/Chaud/Ultra
-> Sequence adaptee -> Offre (Formation/Audit)
-> Achat -> Onboarding client -> Upsell

## ARCHITECTURE MARKETING AUTOMATION (SCHOOLS WP)

Schema logique
Trafic -> Lead Magnet -> Tag auto -> Sequence segmentee
-> Scoring comportemental -> Declencheur BOFU -> Offre adaptee

Triggers d'entree
- Guide debutant -> SEG:Beginner
- Checklist SEO -> SEG:Freelance
- Guide agence -> SEG:Agency
- Newsletter generique -> SEG:Unknown

Triggers comportementaux
- Clic formation +10
- Clic audit +20
- Visite page formation 2x / 7j +25
- Ouvre 3 emails / 7j +10
- Video 70% +15

Scoring intention
- Inscription newsletter +5
- Lead magnet +10
- Clic affilie +15
- Visite page offre +20
- Reponse email +25
- RDV Calendly +50

Classes
- 0-20 Froid -> nurturing
- 21-50 Tiede -> sequence approfondie
- 51-80 Chaud -> sequence conversion
- 81+ Ultra chaud -> notif manuelle + offre perso

Sequences conditionnelles
- Freelance : score >= 40 + clic audit -> seq audit 3 emails
- Agence : visite page retainer + score >= 60 -> seq agence 3 emails

Conditions avancees
- Inactif 30j -> tag inactif + reactivation 3 emails
- Achat formation SEO -> J+14 proposer Funnel WP
- Clic affilie Fluent Forms -> email bonus integration FluentCRM

Retargeting
- Pixels Meta/Google sur pages formation
- Audiences : visiteurs formation, emails actifs, score >= 40
- Ads : masterclass, cas, offre limitee
- Retargeting organique : newsletter + article cluster + video liee

Implémentation FluentCRM (resume)
- Tags segments + tags scoring
- Automations : lien clique, page visitee, tag ajoute
- 3 pipelines : Formation / Audit / Agence

Exemple workflow
Checklist SEO -> SEG:Freelance -> seq 7j
Clic audit -> +20
Score total 45 -> seq conversion
RDV -> +50 -> notif admin

## CHECKLIST IMPLEMENTATION FLUENTCRM (PAS A PAS)

1) Creer listes
- L - Newsletter
- L - Clients

2) Creer tags segments
- SEG:Beginner
- SEG:Freelance
- SEG:Agency
- SEG:Unknown

3) Creer tags stages
- STAGE:TOFU / MOFU / BOFU / CUSTOMER

4) Creer tags engagement
- ENG:Click
- ENG:Inactive14 / ENG:Inactive30

5) Creer tags achat
- BUY:Training:<nom>
- BUY:Audit
- BUY:Paid

6) Creer champs custom
- cf_level
- cf_primary_goal
- cf_business_type
- cf_stack_interest
- cf_lead_score

7) Connecter formulaires (Fluent Forms)
- Map champs -> cf_*
- Tag segment selon lead magnet
- Ajouter liste Newsletter

8) Creer sequences
- Onboarding segment (7j)
- BOFU Audit (3)
- BOFU Formation (3)
- Reengage (2-3)
- Customer Training (5)
- LMS Activation (7)

9) Automations principales
- Entry -> sequence segmentee
- Link click -> scoring + BOFU
- Inactivite 14/30j -> reengage
- FluentCart Paid -> client + stop autres sequences
- TutorLMS Enrolled -> activation

10) Scoring
- Regles points
- Tags STAGE:HOT / STAGE:ULTRA selon seuil

11) Retargeting
- Pixels sur pages formation/audit
- Audiences : visiteurs + leads score >= 40

12) Tests
- Test inscription
- Test clic lien
- Test achat
- Test stop rules

## SCORING AUTOMATIQUE FLUENTCRM (RESUME)

Champs custom
- lead_score_total (number)
- lead_temperature (select)
- segment_type (select)

Regles de scoring
- Open email +1
- Click lien +3
- Lead magnet +5
- Visite /audit +10
- Visite /formation +8
- Page offre 2x / 7j +12
- Form audit +20

Seuils
- >50 STAGE:ULTRA
- 26-50 chaud
- 11-25 tiede
- 0-10 froid

Actions par temperature
- Froid : nurture evergreen
- Tiede : preuves / cas
- Chaud : sequence conversion
- Ultra : notif admin + email perso + Calendly

Segmentation avancee
- Si segment = agence + page audit agence -> +20
- Si segment = debutant + page formation debutant -> +15

Dashboard
- Leads totaux / froid / tiede / chaud / ultra / closing

## PLAN AUTOMATIONS FLUENTCRM (ETAPE PAR ETAPE)

Automation 1 — Entry Segment
Trigger : Form submit (Lead Magnet)
Actions :
- Add list Newsletter
- Apply tag segment_* (selon form)
- Update score +5
- Start sequence Onboarding segmentee

Automation 2 — Email Engagement
Trigger : Email opened
Action : Update score +1

Trigger : Link clicked
Action : Update score +3 + apply ENG:Click si pertinent

Automation 3 — Page Visit Scoring
Trigger : Page visited contains /audit
Action : Update score +10
Trigger : Page visited contains /formation
Action : Update score +8
Trigger : Page visited 2x / 7j
Action : Update score +12

Automation 4 — Form Audit Submitted
Trigger : Form submit (Audit)
Actions :
- Update score +20
- Apply tag intent_audit

Automation 5 — Temperature Update
Trigger : score updated
Conditions :
- score > 50 -> tag STAGE:ULTRA + lead_temperature = STAGE:ULTRA
- score 26-50 -> tag chaud
- score 11-25 -> tag tiede
- score 0-10 -> tag froid

Automation 6 — Conversion Sequences
Trigger : tag chaud added
Actions : start SEQ:BOFU:Audit (ou Formation selon lien clique)

Trigger : tag STAGE:ULTRA added
Actions :
- Notify admin
- Send personal email
- Send Calendly

Automation 7 — Inactivity
Trigger : added to list Newsletter
Delay 14j -> if no open/click -> tag Inactive:14d + reengage seq
Delay 30j -> if no open/click -> tag Inactive:30d + low freq

Automation 8 — Purchase (FluentCart)
Trigger : Order Paid
Actions :
- Apply BUY:Paid
- Apply STAGE:CUSTOMER
- Stop onboarding/BOFU/reengage
- Start SEQ:Customer:Training or SEQ:Customer:Audit:Prep

Automation 9 — LMS Activation (TutorLMS)
Trigger : Course Enrolled
Actions :
- Apply LMS:Enrolled:<cours>
- Start SEQ:LMS:Activation:7d

## NOMENCLATURE SIMPLE (STANDARD)

Tags
- SEG:Beginner / SEG:Freelance / SEG:Agency / SEG:Unknown
- STAGE:TOFU / MOFU / BOFU / CUSTOMER
- ENG:Open / ENG:Click / ENG:Inactive14 / ENG:Inactive30
- BUY:Training:<nom> / BUY:Audit / BUY:Paid
- LMS:Enrolled:<cours>

Sequences
- SEQ:Onboarding:Beginner:7d
- SEQ:Onboarding:Freelance:7d
- SEQ:Onboarding:Agency:7d
- SEQ:BOFU:Audit:3
- SEQ:BOFU:Training:3
- SEQ:Reengage:2
- SEQ:Customer:Training:5
- SEQ:LMS:Activation:7d

Automations
- AUT:Entry:Segment
- AUT:Scoring:Email
- AUT:Scoring:Pages
- AUT:Temperature:Update
- AUT:Conversion:BOFU
- AUT:Inactivity
- AUT:Purchase:FluentCart
- AUT:LMS:Enroll




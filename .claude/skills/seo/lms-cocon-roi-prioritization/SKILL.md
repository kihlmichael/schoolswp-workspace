---
name: lms-cocon-roi-prioritization
description: Prioriser le cocon LMS WordPress selon un score ROI (SEO + Business + Autorite - Effort) et produire un plan d'exécution 4 semaines. Utiliser quand l'utilisateur veut classer les articles LMS par ROI, décider quoi produire en premier dans le cluster LMS, ou planifier une exécution concrète semaine par semaine.
---

# Priorisation ROI - Cocon LMS WordPress (schoolsWP)

Tu priorises les pages du cocon LMS WordPress avec un score ROI simple.
Style schoolsWP : direct, decisionnel, sans blabla.

## Formule

Score ROI = (SEO x 0.35) + (Business x 0.35) + (Autorite x 0.2) - (Effort x 0.1)

## Sorties obligatoires

1) Priorite A (publier en premier)
2) Priorite B (phase 2)
3) Priorite C (backlog)
4) Plan d execution 4 semaines
5) Notes d impact (autorite + cluster)

## Donnees d entree

- Liste de pages LMS
- Notes : SEO / Business / Autorite / Effort (1-10)

## Prompt principal


Tu es le moteur de priorisation ROI de schoolsWP.

Applique le score ROI :
(SEO x 0.35) + (Business x 0.35) + (Autorite x 0.2) - (Effort x 0.1)

Classe les pages en :
- Priorite A (publier en premier)
- Priorite B (phase 2)
- Priorite C (backlog)

Puis propose un plan d execution sur 4 semaines.

## Exemple entree / sortie


Entree (exemple):
- Architecture complete d un LMS WordPress rentable | SEO 8 | Business 9 | Autorite 10 | Effort 7
- Connecter Tutor LMS a FluentCRM | SEO 7 | Business 9 | Autorite 8 | Effort 5
- Tutor LMS vs LearnDash (decision business) | SEO 9 | Business 7 | Autorite 8 | Effort 6

Sortie (exemple):
Priorite A:
- Architecture complete d un LMS WordPress rentable (ROI ~ 7.75)
- Connecter Tutor LMS a FluentCRM (ROI ~ 7.6)
- Tutor LMS vs LearnDash (ROI ~ 7.55)
Plan 4 semaines:
S1: Article signature
S2: Comparatif + automatisation
S3: LMS gratuit vs premium
S4: Tunnel de vente LMS

## Exemple (reference)


Priorite A
1) Architecture complete d un LMS WordPress rentable
SEO 8, Business 9, Autorite 10, Effort 7
Score ROI ~ 7.75

2) Connecter Tutor LMS a FluentCRM
SEO 7, Business 9, Autorite 8, Effort 5
Score ROI ~ 7.6

3) Tutor LMS vs LearnDash (decision business)
SEO 9, Business 7, Autorite 8, Effort 6
Score ROI ~ 7.55

Priorite B
4) LMS gratuit vs premium (ROI)
5) Tunnel de vente formation WordPress
6) Optimiser la vitesse d un LMS WordPress

Priorite C
- Gamification LMS
- LMS multisite
- RGPD LMS
- Gestion 1000+ eleves
- Tableau de bord eleve optimise

Plan 4 semaines
S1: Article signature (architecture LMS rentable)
S2: Tutor LMS vs LearnDash + Tutor LMS -> FluentCRM
S3: LMS gratuit vs premium
S4: Tunnel de vente LMS

## Regles

- Phrases courtes
- Chiffres explicites
- Toujours donner un plan 4 semaines
- Si info manque : "Hypothese : ..."

## Checklist (5 points)

1) Notes SEO/Business/Autorite/Effort remplies
2) Score ROI calcule pour chaque page
3) Priorites A/B/C tranchees
4) Plan 4 semaines coherent
5) Maillage interne prevu

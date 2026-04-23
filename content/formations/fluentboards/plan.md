# Formation FluentBoards de zéro à pro — Plan de production

Tableau de bord de la production de la 1re formation payante schoolsWP.

**Spec :** [docs/superpowers/specs/2026-04-21-formation-fluentboards-design.md](../../../docs/superpowers/specs/2026-04-21-formation-fluentboards-design.md)
**Plan d'implémentation :** [docs/superpowers/plans/2026-04-21-formation-fluentboards.md](../../../docs/superpowers/plans/2026-04-21-formation-fluentboards.md)

**Cadrage validé (2026-04-21) :**

- Audience : **D — Bâtisseur d'écosystème Fluent** (déjà équipé FluentCRM/Forms/Support/Bundle)
- Angle : **A — Maîtrise standalone** ("FluentBoards de zéro à pro")
- Format de livraison : **B — Hybride texte + démos screen** (sans voix off AI, sans face cam obligatoire)
- Hébergement cours : **TutorLMS** sur schoolswp.com
- Checkout : **FluentCart** (early bird 67 € × 30 places, puis 97 €, order bump 27 €)
- Email / bridge : **FluentCRM** (welcome automation + enrollment TutorLMS)
- Durée planning : **9 semaines** (S1 setup → S9 bilan)

---

## Prérequis vérifiés (Task 0.2)

Date de vérif : **2026-04-23**

- [x] **TutorLMS Pro** actif (Tutor LMS 3.9.9 + Tutor LMS Pro 3.9.9, licence active)
- [x] **FluentCart Pro** actif, licence active, flow "créer produit" OK
- [x] **FluentCRM Pro** actif, licence active, ≥ 1 liste + ≥ 1 tag existants
- [x] **FluentBoards Pro** actif, licence active, features Pro accessibles (recurring tasks, custom fields, webhooks)
- [x] **FluentRoadmap** présent et actif — **GATE DÉCISIF PASSÉ** : Module 6 reste à 5 leçons complètes (Roadmap inclus)
- [x] **n8n** instance accessible — ⚠️ aucun credential FluentBoards configuré → à créer en **Task 0.3** (non bloquant)

**Conclusion :** stack complète, aucun prérequis bloquant. On peut enchaîner Task 0.3 (bridge FluentCart ↔ TutorLMS) sans retard.

---

## Bridge FluentCart ↔ TutorLMS choisi (Task 0.3)

Date décision : **2026-04-23**

- **Plan retenu : Plan B — FluentCRM comme pont**
- **Plan A écarté** : FluentCart n'expose que 3 intégrations globales (WP User Create/Update, Webhook, FluentCRM). Aucune intégration native TutorLMS côté FluentCart, ni option "Grant access to course" dans la conception d'un produit FluentCart.
- **Plan B validé** : FluentCRM expose nativement les triggers TutorLMS (`Course Enrolled`, `Course Completed`, `Lesson Completed`) + les triggers FluentCart. On chaîne donc :
  - Trigger : `FluentCart → Product Purchased` (filtré sur l'ID produit formation)
  - Action 1 : Apply tag `formation-fluentboards`
  - Action 2 : Add to list `Formation FluentBoards acheteurs`
  - Action 3 : **Enroll in TutorLMS Course** (à confirmer : action native FluentCRM dispo ? sinon fallback HTTP Call vers API REST TutorLMS)
  - Action 4 : Send welcome email
  - Wait 7 days → follow-up email (construit en Task 7.2)
- **n8n credential FluentBoards** : à créer en parallèle (non bloquant, utile pour les workflows téléchargeables de Task 5.6-5.7)
- Captures de la config : `assets/captures/bridge/` (à remplir pendant Task 0.6)

**Prochaines tâches liées** (S1 seconde moitié) :
- Task 0.4 : créer le cours TutorLMS → donne le course_id nécessaire pour l'action enroll
- Task 0.5 : créer le produit FluentCart → donne le product_id nécessaire pour le filtre trigger
- Task 0.6 : construire l'automation FluentCRM qui lie les deux
- Task 0.7 : test end-to-end du tunnel complet

---

## Cours TutorLMS créé (Task 0.4 shell via API)

Date création shell : **2026-04-23**

Confirmé en base :

- course_id : **2670141**
- slug : formations-fluentboards-de-zero-a-pro
- URL publique : schoolswp.com/formation/formations-fluentboards-de-zero-a-pro
- URL admin : schoolswp.com/wp-admin/admin.php?page=create-course&course_id=2670141
- Statut : private
- Titre : FluentBoards de zéro à pro
- Author : Michaël KIHL (user ID 2)
- Catégorie : Formations schoolsWP (term ID 2410)
- Description : Placeholder (remplacée en S6 avec la copy sales page)

Reste à compléter manuellement dans le builder Tutor LMS (les champs sont des composants React non-exposés REST, donc pas automatisables via API) :

- [ ] Tab Basics : Difficulty Level Intermediate + Pricing Model Payé 97 €
- [ ] Tab Additional : Public ciblé + Durée 8h / 0min + Prérequis
- [ ] Tab Programme : créer les 7 sections dans l'ordre (Setup, Structurer, Piloter, Collaborer, Automatiser, Mesurer, Industrialiser) avec description courte
- [ ] Certificate : activer le module + activer le certificat sur le cours + conditions 100% completion + quiz ≥ 70 %

Estimé 5-8 min de clics dans le builder. Non bloquant pour Task 0.5 (produit FluentCart) qui peut être attaquée en parallèle.

---

## Leçons détaillées (Task 1.1)

*Sera rempli pendant Task 1.1 — liste des 40 leçons avec objectif pédagogique par leçon. Cf. plan d'implémentation section correspondante.*

---

## Progression des 55 tasks

Cocher au fur et à mesure. Voir le plan d'implémentation pour le détail.

### Phase 0 — Setup technique (S1)

- [ ] Task 0.1 Scaffold repo
- [ ] Task 0.2 Vérifs stack
- [ ] Task 0.3 Bridge FluentCart ↔ TutorLMS
- [ ] Task 0.4 Cours TutorLMS squelette
- [ ] Task 0.5 Produit FluentCart + checkout
- [ ] Task 0.6 Automation FluentCRM welcome
- [ ] Task 0.7 Test E2E 12 checkpoints
- [ ] Task 0.8 Template OBS démos screen
- [ ] Task 0.9 Board fil rouge v0

### Phase 1 — Module 1 Setup (S1)

- [ ] Task 1.1 Plan 40 leçons
- [ ] Task 1.2 Les 5 leçons Module 1
- [ ] Task 1.3 Quiz Module 1
- [ ] Task 1.4 Snapshot v-M1 + tag

### Phase 2 — Modules 2 + 3 (S2)

- [ ] Task 2.1 Les 6 leçons Module 2
- [ ] Task 2.2 Quiz Module 2
- [ ] Task 2.3 Snapshot v-M2 + tag
- [ ] Task 2.4 Les 6 leçons Module 3
- [ ] Task 2.5 Quiz Module 3
- [ ] Task 2.6 Snapshot v-M3 + tag

### Phase 3 — Module 4 + début Module 5 (S3)

- [ ] Task 3.1 Les 6 leçons Module 4
- [ ] Task 3.2 Quiz Module 4
- [ ] Task 3.3 Snapshot v-M4 + tag
- [ ] Task 3.4 Les 3 premières leçons Module 5

### Phase 4 — Fin Module 5 + Module 6 (S4)

- [ ] Task 4.1 Les 3 dernières leçons Module 5
- [ ] Task 4.2 Quiz Module 5
- [ ] Task 4.3 Les 4-5 leçons Module 6
- [ ] Task 4.4 Quiz Module 6
- [ ] Task 4.5 Snapshots v-M5 + v-M6 + tags

### Phase 5 — Module 7 + livrables annexes (S5)

- [ ] Task 5.1 Les 6 leçons Module 7
- [ ] Task 5.2 Quiz Module 7
- [ ] Task 5.3 Export + sanitize Board Agence Template final + tag
- [ ] Task 5.4 Checklist setup PDF
- [ ] Task 5.5 Tableau routage webhooks
- [ ] Task 5.6 3 workflows n8n formation base
- [ ] Task 5.7 7 workflows n8n order bump

### Phase 6 — Sales + videos + tunnel (S6)

- [ ] Task 6.1 Copy sales page
- [ ] Task 6.2 Sales page HTML cc-design
- [ ] Task 6.3 Publication sales page schoolswp.com
- [ ] Task 6.4 Video pitch 90 s
- [ ] Task 6.5 Video welcome 2 min + section 0 TutorLMS
- [ ] Task 6.6 Thank-you page FluentCart
- [ ] Task 6.7 QA E2E 16 checkpoints + tag `formation-fb-ready-for-launch`

### Phase 7 — Pré-lancement (S7)

- [ ] Task 7.1 Article "FluentBoards avis"
- [ ] Task 7.2 Séquence email lancement (4 emails)
- [ ] Task 7.3 3 posts LinkedIn + planification Blotato
- [ ] Task 7.4 Automation tag "early-bird"
- [ ] Task 7.5 Gate pré-lancement + tag `formation-fb-rc1`

### Phase 8 — Lancement (S8)

- [ ] Task 8.1 J-3 teaser email + LinkedIn
- [ ] Task 8.2 J0 lancement officiel
- [ ] Task 8.3 J+3 rappel social proof
- [ ] Task 8.4 J+7 last call + bascule prix 97 €

### Phase 9 — Bilan (S9)

- [ ] Task 9.1 Feedback apprenants
- [ ] Task 9.2 Bilan métriques
- [ ] Task 9.3 Backlog v1.1
- [ ] Task 9.4 Décision v2 + tag `formation-fb-v1-shipped`

---

## QA blockers S1

*Tickets à fixer si Tasks 0.7/QA remontent des problèmes. À remplir au fur et à mesure.*

---

## Launch day log (S8)

*Journal d'incidents / frictions / insights pendant le lancement. À remplir le J0 et les jours suivants.*

---

## Backlog v1.1 (S9+)

*Ajustements identifiés après lancement. À remplir en Task 9.3.*

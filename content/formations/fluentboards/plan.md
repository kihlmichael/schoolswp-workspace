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

*À remplir à l'issue de Task 0.2. Date de vérif : _TODO_*

- [ ] TutorLMS actif + licence Pro active
- [ ] FluentCart actif + licence active + flow "créer produit" opérationnel
- [ ] FluentCRM actif + licence active (au moins 1 liste + 1 tag)
- [ ] FluentBoards Pro actif + licence active (recurring tasks + custom fields + webhooks accessibles)
- [ ] FluentRoadmap — **GATE DÉCISIF** : si absent, Module 6 passe de 5 à 4 leçons
- [ ] n8n instance accessible + credentials FluentBoards configurés

---

## Bridge FluentCart ↔ TutorLMS choisi (Task 0.3)

*À remplir à l'issue de Task 0.3*

- Plan retenu : **_TODO_** (Plan A natif / Plan B fallback FluentCRM)
- Procédure exacte : _TODO_
- Captures de la config : `assets/captures/bridge/`

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

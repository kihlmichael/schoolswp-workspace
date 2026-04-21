# Design — Formation "FluentBoards de zéro à pro"

**Date :** 2026-04-21
**Statut :** Design validé, prêt pour plan d'implémentation
**Produit :** 1re formation payante schoolsWP (mini-formation, angle standalone, format hybride LMS)
**Owner :** Michael KIHL

---

## 1. Objectif

Produire et lancer la **première formation payante schoolsWP** — "FluentBoards de zéro à pro" — en 9 semaines, à destination des pros déjà équipés Fluent Suite (audience D = bâtisseur écosystème Fluent).

C'est la **première brique d'un catalogue de mini-formations standalones** sur l'écosystème Fluent Suite (FluentBoards → FluentCRM → FluentCart → …). Chaque formation tient debout seule, avec un angle de maîtrise standalone plutôt que cross-plugin.

### Pourquoi maintenant

- Aucun cocon FluentBoards n'existe sur schoolswp.com (thématique neuve côté schoolsWP, créneau ouvert)
- 148 pages de doc officielle + 27 vidéos WPManageNinja scrapées le 2026-04-21 = matière première prête
- Audience déjà acquise via les piliers `crm-fluentcrm`, `lms`, `flyingpress`, `hebergement`
- Stack livraison complet en place : TutorLMS + FluentCart + FluentCRM

### Hors scope (explicitement)

- Formation cross-plugin "intégration Fluent Suite complète" (reportée après le catalogue standalone)
- Cible audience A/B/C (solopreneur, agence, manager classique) — approchée dans un 2e temps
- Drip content / cohort-based learning (evergreen auto-rythmé uniquement)
- Communauté Discord / forum intégré (MVP = email direct)
- Upsell OTO "Agency Review Loom" (reporté v2)

---

## 2. Cadrage produit (validé étape par étape)

| Dimension | Choix validé |
|---|---|
| **Format livrable** | Mini-formation payante (puis cluster SEO + lead magnet + LMS module en follow-up) |
| **Audience cible (MVP)** | **D — Bâtisseur d'écosystème Fluent** (équipe qui a déjà FluentCRM/Forms/Support ou Bundle) |
| **Audiences futures** | A (solopreneur WP), B (agence WP), C (manager cherchant alternative Trello) |
| **Angle / promesse** | **A — Maîtrise standalone** : "FluentBoards de zéro à pro" (pas intégration cross-plugin) |
| **Format de livraison** | **B — Hybride texte + démos screen** (sans voix off AI, sans face cam obligatoire) |
| **Hébergement cours** | **TutorLMS** (installé sur schoolswp.com) |
| **Checkout / paiement** | **FluentCart** (pas SureCart pour produits propres) |
| **Email / CRM** | **FluentCRM** (welcome automation + bridge inscription TutorLMS) |

---

## 3. Architecture pédagogique

### Fil rouge

> **"Construis le board agence FluentBoards que tu réutiliseras pour chaque nouveau client."**

Chaque module ajoute une pièce concrète au board de démonstration. À la fin du module 7, l'apprenant exporte un JSON importable qu'il garde comme template réutilisable.

### Structure TutorLMS

**1 cours unique** "FluentBoards de zéro à pro" :

- **7 sections** (= les 7 modules)
- **40 leçons** au total (5-7 par module)
- **7 quiz de validation** (5-8 QCM chacun, non bloquants, seuil 70%)
- **1 certificat** à 100% complétion + tous les quiz ≥ 70%
- **Zone ressources** accessible dès la connexion (4 livrables téléchargeables)

### Les 7 modules

| # | Module | Promesse | Durée | Livrable module |
|---|---|---|---|---|
| 1 | **Setup** | Installer, activer, positionner proprement | ~45 min | Premier board créé |
| 2 | **Structurer** | Poser un squelette réutilisable (stages, templates, custom fields) | ~60 min | Board avec stages + template de task |
| 3 | **Piloter** | Animer les tasks au quotidien (dates, priorités, récurrences, filtres) | ~60 min | Board peuplé de tasks pilotables |
| 4 | **Collaborer** | Faire entrer équipe + clients dans le board | ~60 min | Frontend Portal client configuré |
| 5 | **Automatiser** | Entrées/sorties (webhooks, Fluent Forms/CRM/Support, S3) | ~75 min | 2 webhooks opérationnels + 1 intégration Fluent Forms |
| 6 | **Mesurer** | Time tracking, reports, roadmap publique (FluentRoadmap) | ~45 min | Dashboard + roadmap active |
| 7 | **Industrialiser** | Folders, bulk, import/export, migration Trello/Asana, **export template final** | ~60 min | **Board Agence Template exporté (JSON)** |

**Total temps de contenu : ~6h45** (45+60+60+60+75+45+60 min). Temps réel apprenant estimé : **8-12 h sur 1-3 semaines**.

### Format standard d'une leçon

Chaque leçon suit le même pattern (prédictibilité = UX formation) :

1. **Objectif en 1 phrase** ("À la fin de cette leçon tu sauras…")
2. **Contexte** (pourquoi cette fonctionnalité compte dans le fil rouge — 2-3 phrases)
3. **Démo screen** (clip MP4 30-90 s — OBS ou Loom. Sans voix off AI ; voix humaine optionnelle selon leçon ; face cam optionnelle ; fallback acceptable = clip muet avec callouts texte annotés)
4. **Texte structuré** (étapes numérotées + captures annotées fixes pour les points précis)
5. **Pièges à éviter** (1-3 encadrés : erreurs fréquentes remontées de la doc/FAQ)
6. **Checklist de fin** (3-5 cases à cocher — validation avant la leçon suivante)

Les démos screen s'enregistrent dans le **même board fil rouge** d'une leçon à l'autre — l'apprenant voit le board grandir visuellement.

### Mapping source ↔ module

Chaque module s'appuie sur une combinaison de :

- **Docs officielles** archivées dans `content/docs/fluentboards/docs/` (38 pages)
- **Vidéos YouTube** archivées dans `content/docs/fluentboards/youtube/` (27 vidéos, transcripts EN)
- **Captures + démos screen** produites par Michael dans son board fil rouge

Les mappings précis source → leçon seront détaillés dans le plan d'implémentation (writing-plans).

### Bonus / annexes (après module 7)

- **Cas d'usage alternatifs** : freelance WP, agence WP, studio créatif, association/nonprofit (adaptations du template)
- **FAQ + dépannage** (extraits condensés du blog fluentboards)
- **Changelog FluentBoards** (référence versions)

### Livrables téléchargeables inclus dans la formation

1. **Board Agence Template schoolsWP** — export JSON importable directement dans FluentBoards (stages + custom fields + task templates + webhooks d'exemple)
2. **Checklist setup FluentBoards** — PDF 2 pages, étape par étape
3. **Tableau de routage webhooks** — matrice "événement source → task FluentBoards" (Fluent Forms, FluentCRM, FluentSupport, Google Form, Typeform, n8n)
4. **3 workflows n8n d'exemple** — JSON importables utilisant l'incoming webhook FluentBoards

---

## 4. Parcours apprenant

### Rythme

**Evergreen auto-rythmé** (pas de drip content). Audience D est autonome, veut accéder au module dont elle a besoin. Drip générerait du support pour "pourquoi le module 3 n'est pas débloqué ?".

### Support MVP

**Email direct** (pas de Discord/forum) avec promesse "réponse sous 48 h en semaine" affichée sur la sales page. Les questions remontées alimentent la FAQ v2.

### Bridge FluentCart ↔ TutorLMS

**Plan A (si natif)** : add-on FluentCart officiel TutorLMS.
**Plan B (fallback garanti)** : automation FluentCRM déclenchée à l'achat → API TutorLMS pour inscrire l'utilisateur au cours + email welcome.

À valider en S1 pendant le setup technique.

### Parcours end-to-end

1. Arrive sur sales page via LinkedIn / newsletter / article schoolswp.com
2. Clique "Acheter" au prix affiché (67 € early bird ou 97 € public)
3. Checkout FluentCart 1 page (CB/SEPA)
4. Redirigé vers thank-you page + email welcome FluentCRM (< 60 s)
5. Email welcome → lien espace TutorLMS connecté
6. Zone "Démarrer ici" → video accueil 2 min + pack ressources téléchargeable
7. Module 1 → progression visible + quiz fin de module
8. Fin module 7 → export Board Template + certificat
9. Email J+7 : feedback "tu as avancé jusqu'où ?" + bonus utilisation template
10. Email J+30 : upsell future formation Fluent Suite (FluentCRM prochain du catalogue)

---

## 5. Tunnel de vente + pricing

### Prix

| Offre | Prix TTC | Conditions |
|---|---|---|
| **Early bird** | **67 €** | Les 30 premiers acheteurs (FOMO par nombre, pas par date) |
| **Prix public** | **97 €** | Après early bird |
| **Order bump** | **+27 €** | "Pack Workflows n8n Avancés" (7 workflows additionnels, coché par défaut) |

**Panier moyen avec order bump (taux estimé 30-40%) : ~110 €**

### Justification du prix (arguments sales page)

- Audience D dépense déjà 249-499 $/an sur FluentBoards Pro + souvent ≥ 500 $/an Bundle Fluent
- Gain temps estimé : 10-20 h de setup/essais-erreurs évités
- Le Board Template JSON exporté vaut le prix seul (asset réutilisable infiniment)

### Garantie

**Satisfait ou remboursé 14 jours sans justification**, géré manuellement via FluentCart (taux attendu < 5 %).

### Sales page

- **URL :** `schoolswp.com/formations/fluentboards/`
- **Build :** skill `cc-design` (pas aidesigner — on est en prod finale brand-strict, pas exploration)
- **Structure :** Headline + sub → Video pitch 90 s → Ce qui est inclus → Résultats concrets → Pour qui → Pas pour toi si → Preuve sociale → Démo board template → Bio → Pricing → Garantie → FAQ → CTA final FOMO

### Upsell v2 (pas MVP)

**"FluentBoards Agency Review" — +47 €** : review asynchrone Loom 15-20 min du board de l'apprenant. À tester une fois la formation validée en vente.

---

## 6. Acquisition (tunnel de trafic)

### MVP (semaine de lancement S8)

- **Email FluentCRM à la liste existante** — séquence 4 emails sur 7 jours (teaser → annonce → témoignage/démo → last call)
- **Post LinkedIn × 3** — J-3 teaser, J0 lancement, J+7 bilan
- **Article schoolswp.com "FluentBoards avis complet"** — publication avant lancement (SEO long terme + CTA formation)

### Après lancement (M+1 et après)

- Article "Migrer Trello → FluentBoards" (SEO long-tail, cible audience C qui peut se convertir en D)
- Lead magnet gratuit "extrait Board Agence Template" (capture emails FluentCRM → séquence 5 emails → pitch formation)
- Intégration dans cocon `/crm-fluentcrm/` existant (liens depuis articles sur automation)

---

## 7. Production & planning (9 semaines)

### Volume à produire

- **40 leçons** × (~1 000-1 500 mots + 1 clip screen 30-90 s + 5-10 captures annotées)
- **7 quiz** (~45 questions QCM)
- **4 livrables téléchargeables** (board JSON + PDF checklist + tableau webhooks + 3 workflows n8n)
- **7 workflows n8n additionnels** pour order bump
- **Sales page** + thank-you page + FluentCart produit + FluentCRM automation
- **Video pitch 90 s** (sales page) + **video welcome 2 min** (TutorLMS)
- **Séquence email lancement 4 emails** + **3 posts LinkedIn** + **article SEO "FluentBoards avis"**

### Planning

| Sem | Phase | Livrables de fin de phase |
|---|---|---|
| **S1** | Setup technique + Module 1 | TutorLMS cours squelette, FluentCart produit test, bridge testé, Module 1 en ligne |
| **S2** | Modules 2 + 3 | Modules 2 et 3 en ligne, board fil rouge peuplé jusqu'au module 3 |
| **S3** | Module 4 + 50 % Module 5 | Module 4 en ligne (Frontend Portal), Module 5 à 50 % |
| **S4** | Fin Module 5 + Module 6 | Modules 5 et 6 en ligne (webhooks + intégrations + reports) |
| **S5** | Module 7 + livrables annexes | Module 7 en ligne, Board Template JSON exporté, checklist PDF, tableau webhooks, 10 workflows n8n |
| **S6** | Sales page + videos + tunnel | Sales page cc-design en ligne, videos, FluentCart tunnel testé end-to-end, FluentCRM automation active |
| **S7** | Pré-lancement SEO + contenu | Article "FluentBoards avis" publié, séquence email rédigée, 3 posts LinkedIn écrits |
| **S8** | **Lancement early bird** | J0 email+LinkedIn, J+3 rappel, J+5 témoignage, J+7 last call |
| **S9** | Transition prix public + bilan | Prix → 97 €, sales page ajustée, bilan ventes/conversion/retours, TODO v2 |

**Charge estimée : ~180-220 h sur 9 semaines = ~20-25 h/semaine.**

### Délégation aux agents schoolsWP

| Livrable | Agent / skill | Rôle Michael |
|---|---|---|
| Drafts texte des 40 leçons | `studio` / `schoolswp-content-studio` | Plan + captures + démo, agent rédige draft 1, relecture finale |
| 7 quiz (45 QCM) | `studio` | Rédaction QCM depuis transcripts YT + docs |
| Article "FluentBoards avis" | `brain-lite` | Pipeline 5 étapes standard |
| Brief SEO préalable | `radar` | Si article pas encore brief-é |
| Séquence email lancement (4) | `flow` + `studio` | Flow setup FluentCRM, studio rédige |
| 3 posts LinkedIn | `pulse` | Repurpose depuis formation |
| Sales page HTML | `cc-design` (skill) | Spec + copy → HTML brand-strict |
| Checklist PDF + tableau webhooks | `cc-design` | Spec → HTML/PDF brand-strict |

### Non déléguable (100 % Michael)

- 40 démos screen (enregistrées dans son compte FluentBoards réel)
- Captures annotées
- Board fil rouge (workflows réels sur sa machine)
- 10 workflows n8n (credentials chez lui)
- Video pitch 90 s + video welcome 2 min
- Relectures finales de tout le contenu

### Risques & mitigations

| Risque | Mitigation |
|---|---|
| Bridge FluentCart ↔ TutorLMS non documenté | Test dès S1, fallback FluentCRM validé |
| Démos screen inconsistantes | Template OBS fixé dès S1 (résolution, overlay, curseur, intro/outro) |
| Board fil rouge qui dérive | Tag version JSON à chaque fin de module (M1, M2, …) |
| Qualité quiz (trop basique/hard) | Beta-test externe S4-S5 avec 2-3 testeurs liste FluentCRM |
| Retard cumulé S4-S5 | Buffer 0.5 sem intégré, S9 en absorption si besoin |
| Early bird ne part pas | Plan B : +7 j early bird, activer top 50 contacts FluentCRM, accepter lancement mou |

---

## 8. QA + métriques

### QA technique end-to-end (S6)

Tests obligatoires sur compte test avant ouverture publique :

1. Achat FluentCart (CB + SEPA)
2. Order bump 27 € (panier mis à jour)
3. Email post-achat FluentCRM envoyé < 60 s
4. Bridge inscription TutorLMS (user inscrit au cours)
5. Accès cours (sections + leçons + zone ressources visibles)
6. Progression TutorLMS (pourcentage avance)
7. Quiz module (score calculé, seuil 70 % tracké)
8. Certificat généré à 100 % + quiz ≥ 70 %
9. Import Board Template JSON dans FluentBoards Pro réel
10. Import workflows n8n (connexion credentials → tourne)
11. Remboursement simulé (FluentCart OK, désinscription user)
12. Désinscription newsletter (RGPD)

### QA contenu (S4-S5)

- 2-3 beta-testeurs externes (liste FluentCRM, pros Fluent Suite)
- Accès gratuit contre feedback structuré
- Grille : compréhension / clarté démo / utilité pratique (1-5) + "manque quoi ?"
- Beta-test sur 2 modules au choix (pas toute la formation)
- Retours intégrés avant lancement public, en priorité sur les quiz

### Métriques cibles

**Sales page**
- Conversion visites → achats : **2-4 %**
- Taux adoption order bump : **30-40 %**

**Formation**
- Taux démarrage (inscrits → leçon 1 ouverte) : **> 80 %**
- Taux complétion (inscrits → fin module 7) : **> 30 %**
- Score moyen quiz : **> 75 %**

**Business**
- CA early bird S8 : **~2 010 € (30 × 67 €)**
- CA rythme de croisière S10+ : **485-1 455 €/mois (5-15 ventes × 97 €)**
- Taux remboursement 14 j : **< 5 %**
- NPS à J+30 : **> 40**

**SEO & acquisition**
- Trafic article "FluentBoards avis" (GSC)
- CTR emails lancement
- Clics LinkedIn (UTM tracking)

### Loop d'itération post-lancement

- **S10** : review complète métriques + feedback → ajustements immédiats (FAQ, leçons faibles, sales page)
- **M+1** : bilan mensuel. Si < 5 ventes, diagnostiquer. Si > 15 ventes, préparer upsell Agency Review v2.
- **M+3** : décision enchaîner formation FluentCRM (2e du catalogue) avec même pattern

---

## 9. Structure fichiers dans le repo

```
content/
  formations/
    fluentboards/
      plan.md                           # plan détaillé des 40 leçons
      modules/
        01-setup/
          01-pourquoi-fluentboards.md   # 1 fichier par leçon
          02-installation.md
          ...
        02-structurer/
        03-piloter/
        04-collaborer/
        05-automatiser/
        06-mesurer/
        07-industrialiser/
      livrables/
        board-template-agence.json      # export final FluentBoards
        checklist-setup.md              # source Markdown
        checklist-setup.pdf             # export PDF via cc-design
        webhook-routing-table.md
        workflows-n8n/
          01-bug-github-to-task.json
          02-lead-form-to-task-crm.json
          03-support-ticket-to-task.json
          ...                            # +7 pour order bump
      assets/
        captures/                       # screenshots annotés (PNG)
        demos/                          # clips MP4 screen
      sales/
        sales-page.html                 # cc-design output
        thank-you-page.html
        email-sequence.md
        linkedin-posts.md
        video-pitch-90s-script.md
        video-welcome-2min-script.md
```

---

## 10. Dépendances externes

- **TutorLMS installé + fonctionnel sur schoolswp.com** (confirmé par Michael 2026-04-21)
- **FluentCart installé + licence active** (confirmé par Michael 2026-04-21)
- **FluentCRM installé + licence active** (pilier déjà actif dans l'écosystème schoolsWP)
- **FluentBoards Pro licence active** (besoin pour enregistrer démos avec toutes les features)
- **FluentRoadmap** — à vérifier en S1 : intégré à FluentBoards Pro ou licence séparée. Si séparée, soit l'inclure dans les prérequis de la formation ("FluentBoards Pro + FluentRoadmap"), soit retirer le volet Roadmap du Module 6 (remplaçable par focus Reports + Time Tracking seul).
- **n8n instance accessible** (schoolswp-n8n.wp1.host — déjà en place)
- **OBS ou Loom pour démos screen** (OBS gratuit, Loom free plan suffisant si clips < 5 min)

---

## 11. Scope v2 (pas MVP)

Backlog pour après le lancement, si la traction justifie :

- Upsell OTO "FluentBoards Agency Review" 47 € (Loom asynchrone)
- Canal Discord privé formation + Q&A live trimestrielle
- Bundle "Fluent Suite Mastery" (formation FluentBoards + FluentCRM + FluentCart à prix bundle)
- Version anglaise de la formation (audience anglophone via LinkedIn)
- Formations suivantes du catalogue standalone : FluentCRM, FluentCart, FluentForms, FluentSupport
- Ouverture aux audiences A/B/C avec positionnement ajusté (migration Trello/Asana, solopreneur, manager classique)

---

## 12. Définition de "done" pour cette formation (MVP)

La formation est **done** quand :

- [ ] Les 7 modules + 40 leçons + 7 quiz sont en ligne dans TutorLMS
- [ ] Les 4 livrables téléchargeables sont fonctionnels et testés (import réel OK pour JSON + workflows)
- [ ] Le tunnel FluentCart → FluentCRM → TutorLMS fonctionne end-to-end (12 tests QA passés)
- [ ] La sales page est en ligne à schoolswp.com/formations/fluentboards/
- [ ] Les vidéos pitch (90 s) et welcome (2 min) sont publiées
- [ ] La séquence email de lancement (4 emails) est configurée dans FluentCRM et testée
- [ ] L'article "FluentBoards avis complet" est publié sur schoolswp.com
- [ ] La formation est accessible en early bird à 67 € pour les 30 premiers acheteurs
- [ ] Le certificat TutorLMS se génère correctement en fin de cours

---

## Annexes

### A. Sources scrapées (2026-04-21)

- 38 docs officielles (`content/docs/fluentboards/docs/`)
- 19 pages marketing (`content/docs/fluentboards/pages/`)
- 91 articles blog (`content/docs/fluentboards/blog/`)
- 27 vidéos YouTube WPManageNinja (`content/docs/fluentboards/youtube/` — 2h44m total, transcripts EN auto-générés)

### B. Vidéos YouTube clés pour référence benchmark

- **#22** "Running a Client Project from Start to Finish" (18m30) → benchmark fil rouge
- **#21** "How to Automate Your Agency Project Management" (17m15) → Module 5 + 7
- **#26** "Create a Personalized Project Management Board" (9m46) → Module 2
- **#25** "No-Chaos Project Dashboard for Client-Focused Agency" (6m33) → Module 6
- **#6 + #19** Frontend Portal (2 vidéos) → Module 4
- **#4 + #23** FluentRoadmap → Module 6
- **#7, #9, #24** Migration Trello/Asana → Module 7 bonus

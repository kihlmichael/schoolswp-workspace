---
title: Déploiement FAQ Kadence Accordion sur la home (FR/EN/DE)
date: 2026-05-24
status: TODO
owner: Michael
priority: P1 (rich snippet Google)
companion_to:
  - tools/wp-mu-plugins/schoolswp-home-schema.php (v1.0.1)
audit_ref: content/audits/schoolswp-30pts/2026-05-24/audit.md
---

# FAQ home — coller dans les 3 pages

Le mu-plugin schoolswp-home-schema.php est en prod et injecte déjà le bloc FAQPage JSON-LD sur les 3 homes FR/EN/DE. **Pour que Google affiche le rich snippet FAQ**, le contenu visible dans la home doit être **pixel-perfect identique** au JSON-LD — sinon pénalité et aucun résultat enrichi.

Action : coller dans chaque home un bloc **Kadence Accordion** avec exactement ces 6 Q/A par langue.

## Procédure (par page)

1. wp-admin → Pages → **Home** (ou la version EN/DE selon Polylang)
2. Éditeur Gutenberg → bas de page (juste avant le footer ou sous le dernier H2)
3. Ajouter un bloc : taper /accordion → choisir **Kadence Accordion**
4. Régler : 6 panes, premier ouvert, design cohérent avec la home
5. Coller titre + réponse pour chaque pane (cf. listes ci-dessous)
6. **Vérifier** : le texte des questions et réponses doit être **strictement identique** (ponctuation, accents, apostrophes typographiques) à la version JSON-LD
7. Mettre à jour → vider FlyingPress (déjà fait pour les 3 homes mais re-purger après modif)

## Q/A version FR (page Home)

### Q1
**Question** : Qu'est-ce que schoolsWP ?
**Réponse** : schoolsWP est une plateforme de formations WordPress concrètes pour freelances, créateurs et solopreneurs. Michaël KIHL y partage des tutoriels, audits et méthodes pour créer des sites WordPress performants, automatisés et rentables.

### Q2
**Question** : À qui s'adressent les formations schoolsWP ?
**Réponse** : Aux freelances qui veulent vivre du web, aux solopreneurs qui automatisent leur business WordPress, et aux créateurs de contenu qui cherchent une stack pro sans tomber dans la dette technique.

### Q3
**Question** : Quels piliers WordPress couvre schoolsWP ?
**Réponse** : Six piliers : automatisation (Fluent stack, n8n, SureTriggers), SEO et GEO/AIO, performance et UX, monétisation (FluentCart, affiliations), formations en ligne (TutorLMS), sécurité et hébergement.

### Q4
**Question** : Les formations schoolsWP sont-elles gratuites ?
**Réponse** : Les articles, tutoriels et la newsletter sont gratuits. Les formations approfondies (modules vidéo, accompagnement, certifications) sont payantes via FluentCart et TutorLMS.

### Q5
**Question** : Comment contacter Michaël KIHL ?
**Réponse** : Par email à contact@michaelkihl.fr, sur LinkedIn (linkedin.com/in/michaelkihl/) ou via les boutons sociaux en bas de chaque article.

### Q6
**Question** : Comment recevoir les nouveaux contenus schoolsWP ?
**Réponse** : En t'abonnant à la newsletter via le bouton présent sur la home : tu reçois chaque semaine les nouveaux articles, audits et méthodes testées sur WordPress.

## Q/A version EN (page Home traduction EN)

### Q1
**Question** : What is schoolsWP?
**Answer** : schoolsWP is a practical WordPress training platform for freelancers, creators and solopreneurs. Michaël KIHL shares tutorials, audits and methods to build WordPress sites that are fast, automated and profitable.

### Q2
**Question** : Who are schoolsWP trainings for?
**Answer** : For freelancers who want to make a living from the web, solopreneurs automating their WordPress business, and content creators looking for a pro stack without falling into technical debt.

### Q3
**Question** : Which WordPress pillars does schoolsWP cover?
**Answer** : Six pillars: automation (Fluent stack, n8n, SureTriggers), SEO and GEO/AIO, performance and UX, monetization (FluentCart, affiliates), online training (TutorLMS), security and hosting.

### Q4
**Question** : Are schoolsWP trainings free?
**Answer** : Articles, tutorials and the newsletter are free. In-depth trainings (video modules, coaching, certifications) are paid via FluentCart and TutorLMS.

### Q5
**Question** : How to contact Michaël KIHL?
**Answer** : By email at contact@michaelkihl.fr, on LinkedIn (linkedin.com/in/michaelkihl/) or via the social buttons at the bottom of each article.

### Q6
**Question** : How to receive new schoolsWP content?
**Answer** : By subscribing to the newsletter via the button on the home page: you receive each week the new articles, audits and tested methods on WordPress.

## Q/A version DE (page Home traduction DE)

### Q1
**Frage** : Was ist schoolsWP?
**Antwort** : schoolsWP ist eine praktische WordPress-Trainingsplattform für Freelancer, Kreative und Solopreneure. Michaël KIHL teilt Tutorials, Audits und Methoden, um schnelle, automatisierte und profitable WordPress-Seiten zu erstellen.

### Q2
**Frage** : Für wen sind die schoolsWP-Trainings gedacht?
**Antwort** : Für Freelancer, die vom Web leben möchten, Solopreneure, die ihr WordPress-Geschäft automatisieren, und Content-Ersteller, die einen professionellen Stack ohne technische Schulden suchen.

### Q3
**Frage** : Welche WordPress-Säulen deckt schoolsWP ab?
**Antwort** : Sechs Säulen: Automatisierung (Fluent stack, n8n, SureTriggers), SEO und GEO/AIO, Performance und UX, Monetarisierung (FluentCart, Affiliates), Online-Training (TutorLMS), Sicherheit und Hosting.

### Q4
**Frage** : Sind die schoolsWP-Trainings kostenlos?
**Antwort** : Artikel, Tutorials und der Newsletter sind kostenlos. Tiefgehende Trainings (Video-Module, Coaching, Zertifizierungen) sind kostenpflichtig über FluentCart und TutorLMS.

### Q5
**Frage** : Wie kann man Michaël KIHL kontaktieren?
**Antwort** : Per E-Mail an contact@michaelkihl.fr, auf LinkedIn (linkedin.com/in/michaelkihl/) oder über die Social-Buttons am Ende jedes Artikels.

### Q6
**Frage** : Wie erhält man neue schoolsWP-Inhalte?
**Antwort** : Durch Abonnieren des Newsletters über den Button auf der Startseite: Du erhältst wöchentlich die neuen Artikel, Audits und getesteten Methoden zu WordPress.

## Validation post-pose

Pour chaque langue, après pose et update :

1. Vider FlyingPress (purge URL = home concernée)
2. Ouvrir la home en navigation privée → ouvrir un pane → vérifier que le texte du pane = texte du JSON-LD (Ctrl+F dans view-source pour le script schoolswp-home-schema)
3. Passer la home à **Google Rich Results Test** : https://search.google.com/test/rich-results
   - Coller https://schoolswp.com/ (puis /en/, puis /de/)
   - Attendu : 4 entités détectées (Organization, WebSite, BreadcrumbList, FAQPage avec 6 questions)
   - Si "FAQ détectée mais texte ne correspond pas" → corriger l'accordéon visible
4. Soumettre les 3 URLs dans **GSC URL inspection** → "Demander une indexation"

## Sources de vérité (ne pas diverger)

- JSON-LD : tools/wp-mu-plugins/schoolswp-home-schema.php v1.0.1 (commit 0751aa0)
- Audit : content/audits/schoolswp-30pts/2026-05-24/audit.md (Action 2.C)
- BRAND_RULES : tutoiement, schoolsWP toujours, jamais SchoolsWP, jamais d'em-dash dans les réponses

# Gap Analysis FluentCRM — Videos YouTube vs Documentation officielle

**Date** : 2026-03-21
**Objectif** : Identifier les ecarts entre les videos YouTube officielles FluentCRM et la documentation scrapee, pour alimenter le plan de formation schoolsWP.

---

## Sources analysees

### Videos YouTube (5 fichiers)

| Video | Duree | Date | Vues | Fichier |
|-------|-------|------|------|---------|
| FluentCRM 101 Mastery — Ultimate Tutorial | 85:59 | 2023-03-14 | 23 842 | `fluentcrm-101-mastery-ultimate-tutorial.md` |
| Quickstart Guide to Configure | 5:15 | 2022-08-08 | 16 738 | `fluentcrm-quickstart-guide-configure.md` |
| Free WordPress CRM Plugin | 11:22 | 2021-03-11 | 44 550 | `fluentcrm-free-wordpress-crm-plugin.md` |
| What's Inside FluentCRM | 3:35 | 2024-01-19 | 13 106 | `fluentcrm-whats-inside.md` |
| FluentCRM 3.0 — New CRM Experience | 0:57 | 2025-11-10 | 1 872 | `fluentcrm-3-0-new-crm-experience.md` |

### Documentation officielle (51 fichiers `.firecrawl/fluentcrm-*.md`)

Repartis en categories : Getting Started, Global Settings, Contacts, Emails, Automations, Event Tracking, Reports, Integrations, Advanced Features, FAQ.

---

## 1. Matrice de couverture

### Getting Started (Installation, configuration, SMTP)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| Installation free (WordPress.org) | Oui — Quickstart (0:16), 101 Mastery (01:44), Free Plugin (0:30) | Oui — `fluentcrm-install-upgrade.md` | Basique |
| Upgrade vers Pro (zip + licence) | Oui — Quickstart (02:24), 101 Mastery (01:44) | Oui — `fluentcrm-install-upgrade.md` | Basique |
| Activation licence | Oui — Quickstart (02:24), 101 Mastery | Oui — `fluentcrm-install-upgrade.md` | Basique |
| Configuration SMTP (FluentSMTP) | Oui — Quickstart (03:37), 101 Mastery | Oui — `fluentcrm-smtp-bounce.md`, `fluentcrm-deliverability.md` | Intermediaire |
| Business settings (nom, adresse, logo) | Oui — Quickstart, 101 Mastery | Oui — `fluentcrm-business-settings.md` | Basique |
| Email deliverability (providers, cron, multi-threading) | Non | Oui — `fluentcrm-deliverability.md` | Avance |
| Bounce handlers | Non | Oui — `fluentcrm-smtp-bounce.md` | Intermediaire |
| Requirements (PHP, WP versions) | Non | Oui — `fluentcrm-install-upgrade.md` | Basique |

### Contacts (dashboard, gestion, import/export, statuts, segmentation, filtres)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| Contacts dashboard (vue globale, filtres basiques) | Oui — 101 Mastery (32:52), Free Plugin (1:40) | Oui — `fluentcrm-contacts-dashboard.md` | Intermediaire |
| Contact overview (details individuels) | Oui — 101 Mastery (32:52), Free Plugin (1:40) | Oui — `fluentcrm-contact-overview.md` | Intermediaire |
| Ajout manuel de contacts | Oui — 101 Mastery (06:54) | Oui — `fluentcrm-manage-contacts.md` | Basique |
| Import CSV | Oui — 101 Mastery (06:54), Free Plugin (1:11) | Oui — `fluentcrm-import-contacts.md` | Intermediaire |
| Import depuis autres CRM (MailChimp, etc.) | Oui — 101 Mastery (06:54) | Non (la doc couvre l'import depuis plugins WP, pas migration CRM externe) | Basique |
| Import depuis WooCommerce/EDD/LMS | Oui — 101 Mastery (10:44) | Oui — `fluentcrm-import-contacts.md` | Intermediaire |
| Export contacts | Non | Oui — `fluentcrm-export-contacts.md` (Pro only) | Intermediaire |
| Contact statuses (subscribed, pending, bounced, complained) | Oui — 101 Mastery (28:24) | Oui — `fluentcrm-contact-statuses.md` | Intermediaire |
| Contact status "Transactional" | Non | Oui — `fluentcrm-contact-statuses.md` | Intermediaire |
| Segmentation par listes | Oui — 101 Mastery (14:52), Free Plugin (3:25) | Oui — `fluentcrm-contacts-dashboard.md` | Basique |
| Segmentation par tags | Oui — 101 Mastery (14:52), Free Plugin (3:25) | Oui — `fluentcrm-contacts-dashboard.md` | Basique |
| Dynamic segments (Pro) | Oui — 101 Mastery (14:52) | Oui — `fluentcrm-contacts-dashboard.md` | Intermediaire |
| Advanced filter (filtres combines) | Oui — 101 Mastery (32:52) | Oui — `fluentcrm-advanced-filter.md` | Avance |
| Bulk actions | Oui — 101 Mastery (32:52) | Oui — `fluentcrm-manage-contacts.md` | Intermediaire |
| Custom contact fields | Oui — 101 Mastery (32:52, mentionne) | Oui — `fluentcrm-custom-fields.md` | Intermediaire |
| Flexible segmentation (role WP, WooCommerce, LearnDash) | Oui — 101 Mastery (45:22) | Oui — `fluentcrm-general-settings.md`, `fluentcrm-learndash.md` | Avance |
| Company module | Non | Oui — `fluentcrm-company-module.md` | Avance |

### Emails (campagnes, templates, sequences, recurrentes, composition)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| Email templates (creation, styles, blocs) | Oui — 101 Mastery (19:04), Free Plugin (4:05) | Oui — `fluentcrm-email-templates.md`, `fluentcrm-compose-email.md` | Intermediaire |
| Email campaigns (creation, envoi, planification) | Oui — 101 Mastery (24:02), Free Plugin (4:05) | Oui — `fluentcrm-email-campaigns.md` | Intermediaire |
| A/B testing (sujets) | Oui — 101 Mastery (24:02), Free Plugin (mentionne) | Oui — `fluentcrm-email-campaigns.md`, `fluentcrm-campaign-summary.md` | Intermediaire |
| UTM parameters | Oui — 101 Mastery (24:02) | Oui — `fluentcrm-email-campaigns.md` | Basique |
| Post-campaign actions (tags par activite) | Oui — 101 Mastery (24:02) | Oui — `fluentcrm-campaign-summary.md` | Intermediaire |
| Email sequences | Oui — 101 Mastery (49:28) | Oui — `fluentcrm-email-sequence.md` | Intermediaire |
| Recurring campaigns (newsletter automatique) | Non | Oui — `fluentcrm-recurring-campaign.md` | Avance |
| Compose email (editeur, blocs, smart codes) | Oui — 101 Mastery (19:04) | Oui — `fluentcrm-compose-email.md` | Intermediaire |
| Conditional sections (emails) | Oui — 101 Mastery (01:19:34) | Oui — `fluentcrm-conditional-sections.md` | Intermediaire |
| Conditional sections (pages WP) | Oui — 101 Mastery (01:19:34) | Oui — `fluentcrm-conditional-sections.md` | Intermediaire |
| Campaign labels | Non | Oui — `fluentcrm-campaign-labels.md` | Basique |
| Email overview (vue globale emails envoyes) | Non | Oui — `fluentcrm-emails-overview.md` | Basique |
| Campaign summary & analytics | Oui — 101 Mastery (mentionne) | Oui — `fluentcrm-campaign-summary.md` | Intermediaire |
| Merge codes / Smart codes | Oui — 101 Mastery (19:04, contact properties) | Oui — `fluentcrm-merge-codes.md` | Avance |
| RSS block / Latest Post block | Non | Oui — `fluentcrm-recurring-campaign.md` | Intermediaire |
| Gutenberg email editor (v3.0) | Oui — 3.0 teaser (mentionne) | Non (doc pas encore mise a jour pour 3.0) | Basique |

### Automation (editeur, triggers, actions, conditionnels, goals, rapports)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| Introduction automations (concept, glossaire) | Oui — 101 Mastery (58:00), Free Plugin (8:22), What's Inside | Oui — `fluentcrm-automation-intro.md` | Intermediaire |
| Automation editor (interface) | Oui — 101 Mastery (58:00) | Oui — `fluentcrm-automation-editor.md` | Intermediaire |
| Triggers (CRM, WP, WooCommerce, LMS, membership) | Oui — 101 Mastery (01:02:24) | Oui — `fluentcrm-automation-triggers.md` | Avance |
| Actions (send email, apply list/tag, delay, create user, etc.) | Oui — 101 Mastery (01:06:34) | Oui — `fluentcrm-automation-actions.md` | Avance |
| WordPress automation actions (create WP user, change role, etc.) | Oui — 101 Mastery (01:06:34, mentionne) | Oui — `fluentcrm-wp-automation-actions.md` | Intermediaire |
| Goals / Benchmark actions | Oui — 101 Mastery (01:12:42) | Oui — `fluentcrm-automation-goals.md` | Avance |
| Conditionals (yes/no paths) | Oui — 101 Mastery (01:16:54) | Oui — `fluentcrm-automation-conditionals.md` | Intermediaire |
| Split test dans automations | Oui — 101 Mastery (01:06:34, use case upsell) | Non (pas de doc dediee) | Intermediaire |
| Automation reports (chart, step, email analytics, individuel) | Oui — 101 Mastery (58:00, breve mention) | Oui — `fluentcrm-automation-reports.md` | Intermediaire |
| Automation labels | Non | Oui — `fluentcrm-automation-labels.md` | Basique |
| Import/Export automations | Non | Oui — `fluentcrm-automation-intro.md` | Basique |

### Integrations (WooCommerce, Fluent Forms, TutorLMS, LearnDash, webhooks)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| WooCommerce (sync, checkout checkbox, import par produit) | Oui — 101 Mastery (10:44, 45:22) | Oui — `fluentcrm-woocommerce.md`, `fluentcrm-integration-settings.md` | Intermediaire |
| WooCommerce segmentation par produit (tags produit) | Oui — 101 Mastery (45:22) | Oui — `fluentcrm-woocommerce.md` | Avance |
| Fluent Forms (creation form, integration feed, dynamic tags) | Oui — 101 Mastery (37:37), Free Plugin (6:45) | Oui — `fluentcrm-fluent-forms.md`, `fluentcrm-optin-forms.md` | Avance |
| LearnDash (tag par cours, segmentation, triggers) | Oui — 101 Mastery (45:22, 01:02:24) | Oui — `fluentcrm-learndash.md` | Avance |
| TutorLMS | Non (uniquement mentionne dans la liste d'import) | Oui — `fluentcrm-tutorlms.md` | Avance |
| Integration settings (global — WooCommerce, EDD, LifterLMS, LearnDash) | Oui — 101 Mastery (10:44) | Oui — `fluentcrm-integration-settings.md` | Basique |
| Incoming webhooks | Oui — 101 Mastery (01:21:34) | Oui — `fluentcrm-incoming-webhooks.md`, `fluentcrm-webhook.md` | Intermediaire |
| Outgoing webhooks (Zapier) | Oui — 101 Mastery (01:21:34) | Oui — `fluentcrm-webhook.md` | Intermediaire |
| LifterLMS | Oui — 101 Mastery (49:28, mentionne trigger) | Non (pas de doc dediee scrapee) | Basique |
| EDD (Easy Digital Downloads) | Non (mentionne seulement) | Oui — `fluentcrm-advanced-reports.md` (rapports EDD) | Basique |
| Paid Membership Pro / MemberPress / Restrict Content | Oui — 101 Mastery (01:02:24, mentionne trigger membership) | Oui — `fluentcrm-import-contacts.md` (import only) | Basique |

### Settings (general, business, email, compliance, smart links, double opt-in)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| General settings (sync WP, signup, comment form, WooCommerce checkout) | Oui — 101 Mastery (42:10, 10:44) | Oui — `fluentcrm-general-settings.md` | Intermediaire |
| Business settings | Oui — Quickstart, 101 Mastery | Oui — `fluentcrm-business-settings.md` | Basique |
| Email settings (from, reply-to, footer, preferences) | Oui — 101 Mastery (mentionne) | Oui — `fluentcrm-email-settings.md` | Intermediaire |
| Compliance settings (anonymize IP, GDPR, one-click unsub) | Non | Oui — `fluentcrm-compliance-settings.md` | Intermediaire |
| Smart links | Oui — 101 Mastery (53:57) | Oui — `fluentcrm-smartlinks.md` | Intermediaire |
| Double opt-in | Oui — 101 Mastery (28:24) | Oui — `fluentcrm-double-optin.md` | Intermediaire |
| Global settings overview (index) | Non | Oui — `fluentcrm-global-settings.md` | Basique |
| Managers settings | Non | Oui — `fluentcrm-global-settings.md` (mentionne) | Basique |
| REST API settings | Non | Oui — `fluentcrm-global-settings.md` (mentionne) | Avance |

### Advanced (rapports avances, event tracking, merge codes, company module, abandoned cart)

| Sujet / Fonctionnalite | Videos | Doc | Profondeur |
|------------------------|--------|-----|------------|
| Advanced reports (contact growth, email stats, WooCommerce, LMS reports) | Non | Oui — `fluentcrm-advanced-reports.md` | Avance |
| Event tracking | Non | Oui — `fluentcrm-event-tracking.md` | Avance |
| Merge codes / Smart codes (structure, data transformers) | Oui — 101 Mastery (contact properties, mentionne) | Oui — `fluentcrm-merge-codes.md` | Avance |
| Company module | Non | Oui — `fluentcrm-company-module.md` | Avance |
| Abandoned cart (WooCommerce) | Non | Oui — `fluentcrm-abandoned-cart.md` | Avance |
| Advanced features config (quick nav, campaign archives, multi-threading, AI, system log) | Non | Oui — `fluentcrm-advanced-features.md` | Avance |
| FAQ (cron, double opt-in forms vs CRM, custom fields, form plugins) | Non | Oui — `fluentcrm-faq.md` | Intermediaire |
| SMS Marketing (v3.0) | Oui — 3.0 teaser | Non (doc pas encore mise a jour) | Basique |
| Nouvelle UI v3.0 | Oui — 3.0 teaser | Non | Basique |

---

## 2. Gaps identifies

### A. Dans la doc mais PAS dans les videos — opportunites de contenu original

Ces sujets ne sont pas couverts dans les 5 videos analysees. Ce sont des opportunites directes pour la formation schoolsWP :

1. **Recurring campaigns / Newsletter automatique** (`fluentcrm-recurring-campaign.md`) — Envoyer des newsletters recurrentes avec le bloc "Latest Post". Aucune video ne couvre ce sujet.
2. **Abandoned cart WooCommerce** (`fluentcrm-abandoned-cart.md`) — Configuration et automatisation des paniers abandonnes. Question posee dans les commentaires YouTube ("How to create Abandoned cart discount email in fluentcrm?").
3. **Event tracking** (`fluentcrm-event-tracking.md`) — Module avance de suivi comportemental utilisateur. Pas mentionne dans les videos.
4. **Company module** (`fluentcrm-company-module.md`) — Organisation des contacts par entreprise, logo automatique. Fonctionnalite absente des videos.
5. **Advanced reports** (`fluentcrm-advanced-reports.md`) — Rapports avances : croissance contacts, stats emails, rapports WooCommerce/LMS. Brievement mentionne dans le tutorial 101 mais pas detaille.
6. **Compliance settings / GDPR** (`fluentcrm-compliance-settings.md`) — Anonymisation IP, suppression contacts, export donnees personnelles, one-click unsubscribe.
7. **Export contacts** (`fluentcrm-export-contacts.md`) — Fonctionnalite Pro pour exporter les contacts. Jamais demontree en video.
8. **Email deliverability en profondeur** (`fluentcrm-deliverability.md`) — Cron jobs, multi-threading, providers multiples. Crucial mais non couvert en video.
9. **REST API** — Mentionnee dans les settings mais aucune demo en video. Sujet pour utilisateurs avances.
10. **Campaign labels / Automation labels** (`fluentcrm-campaign-labels.md`, `fluentcrm-automation-labels.md`) — Organisation de l'espace de travail.
11. **TutorLMS integration detaillee** (`fluentcrm-tutorlms.md`) — Triggers, actions, goals, filtres, rapports avances specifiques TutorLMS. Crucial pour la stack schoolsWP.
12. **Merge codes avances** (`fluentcrm-merge-codes.md`) — Structure complete, data transformers, fallback values. Les videos ne montrent que l'insertion basique.
13. **Advanced features config** (`fluentcrm-advanced-features.md`) — Quick nav, campaign archives, multi-threading, disable AI, system log.

### B. Dans les videos mais PAS dans la doc — tips pratiques a integrer

1. **Migration depuis MailChimp/ConvertKit/ActiveCampaign via API** — Le tutorial 101 (06:54) montre le processus d'import depuis un CRM externe avec cle API. La doc ne couvre que l'import depuis plugins WordPress installes.
2. **Split test dans les automations** — Le tutorial 101 (01:06:34) montre un split test A/B dans un funnel d'automation (upsell email). Pas de doc dediee a cette fonctionnalite.
3. **Export vers Google Sheets via Zapier** — Le tutorial 101 (01:21:34) montre comment transferer des donnees FluentCRM vers Google Sheets via Zapier/outgoing webhook. La doc webhook reste technique et ne donne pas ce use case concret.
4. **Commentaires de blog comme source de leads** — Le tutorial 101 montre la conversion des commentaires en abonnes. La doc le mentionne dans general settings mais sans mise en contexte strategique.
5. **WooCommerce checkout subscription checkbox** — Montre en video comme tactique de generation de leads. La doc est factuelle sans angle marketing.
6. **SMS Marketing et Gutenberg email editor (v3.0)** — Annonces dans le teaser 3.0 mais doc pas encore mise a jour.

### C. Dans les deux mais superficiel — besoin d'approfondir

1. **Email sequences** — Le tutorial 101 (49:28) montre la creation basique, la doc aussi. Manque : strategies avancees de nurturing, exemples concrets de sequences (onboarding, upsell, re-engagement), bonnes pratiques de timing.
2. **Advanced filter** — Montre en video (filtres basiques), doc tres detaillee (11 min de lecture). Le gap est cote video : pas de cas d'usage avances.
3. **Automation triggers** — Le tutorial 101 montre form submission, WooCommerce order, LearnDash enrollment. La doc liste beaucoup plus de triggers (birthday, tag applied, company applied, etc.). Besoin de couvrir les triggers moins evidents.
4. **Smart links** — Le tutorial 101 (53:57) et la doc couvrent le sujet, mais la fonctionnalite "Auto Login with Smart Links" n'est abordee que dans la doc.
5. **Double opt-in** — Les deux sources couvrent la configuration, mais ni l'une ni l'autre n'explique quand utiliser vs ne pas utiliser le double opt-in, ni l'impact sur les taux de conversion.
6. **WooCommerce automation** — Les videos montrent l'integration basique et l'import. La doc couvre plus de profondeur (opt-in checkbox, segmentation, marketing automation specifique WooCommerce). Besoin d'un module dedie avec cas d'usage reels.
7. **Merge codes** — Les videos mentionnent les "contact properties" pour personnaliser les emails. La doc detaille les data transformers et fallback values — fonctionnalites puissantes non explorees en video.

---

## 3. Questions frequentes des commentaires YouTube

### Questions recurrentes revelant des besoins non couverts

| Question | Source | Frequence / Indicateur |
|----------|--------|----------------------|
| **Free vs Pro : quelles differences exactes ?** | @yxcvmk, @mohsinworld, @helloapple556 (Free Plugin) | 3+ questions directes |
| **Peut-on envoyer un email individuel (pas campagne) ?** | @naomipaine7101, @YourLocalHandyman (Free Plugin, 101 Mastery) | 2 questions |
| **Les clients WooCommerce sont-ils sync automatiquement ?** | @ryansills509 (101 Mastery) | 1 question detaillee |
| **Comment creer un email de panier abandonne ?** | @BioCodeServices (What's Inside) | 1 question |
| **Peut-on recevoir des emails dans FluentCRM ?** | @YourLocalHandyman (101 Mastery) | 1 question (malentendu sur le role CRM vs inbox) |
| **Pricing : combien d'utilisateurs par plan ?** | @midathanadevi5338 (101 Mastery) | 1 question |
| **Comment fonctionne l'A/B testing ?** | @Blutezeit678 (101 Mastery) | 1 question |
| **Le lien FluentCRM en footer est-il retirable en Pro ?** | @TiempoTotal (101 Mastery) | 1 question |
| **Smart links pour tracker les visiteurs non-contacts ?** | @smilewithroshni2494 (101 Mastery) | 1 question |
| **Faut-il encore un service email (Sendinblue, etc.) avec FluentCRM ?** | @izakniemann5734 (Free Plugin) | 1 question |
| **Tutorials sur des cas d'usage concrets (funnels, sequences, recovery)** | @nickslab3589 (What's Inside) | 1 demande explicite |
| **Ajout de providers SMS custom (pas juste Twilio/AWS)** | @sisouhzl5645, @dennislube5772 (3.0 teaser) | 2 demandes |
| **Correction des traductions (i18n)** | @tomasnovy2065 (3.0 teaser) | 1 demande |
| **Creation automatique d'un WP user a la souscription (free)** | @BenZan7181 (Free Plugin) | 1 question |
| **Integration video YouTube dans les newsletters** | @mihailmanole (Free Plugin) | 1 question |

### Synthese des themes recurrents

- **Clarification free vs pro** : besoin majeur, aucune video ne fait un comparatif clair
- **Emails individuels** : les gens ne comprennent pas que FluentCRM est un outil de marketing, pas un client email
- **Cas d'usage concrets** : la demande la plus forte est pour des tutorials pratiques (funnels de vente, sequences de nurturing, recovery panier)
- **WooCommerce** : synchronisation et automatisation = premiere preoccupation des e-commercants
- **Pricing et limites** : questions non-techniques mais strategiques pour la decision d'achat

---

## 4. Recommandations pour le plan de formation schoolsWP

### Modules gratuits (M1-M3) — Sujets prioritaires

Ces sujets correspondent au parcours debutant et repondent aux questions les plus frequentes :

**M1 — Decouverte et installation**
- Installation free + upgrade Pro (couvert en video, a adapter en francais avec angle schoolsWP)
- Configuration business settings + SMTP (FluentSMTP)
- **Free vs Pro : comparatif clair** (gap identifie — contenu original)
- Comprendre le role de FluentCRM : CRM + email marketing, PAS un client email (repondre au malentendu frequent)
- Faut-il un service email externe ? (repondre a la question recurrente)

**M2 — Premiers contacts et segmentation**
- Ajout manuel + import CSV + import WordPress users
- Listes, tags, segments dynamiques — explication et strategie de nommage
- Les 6 statuts de contacts (dont Transactional, pas couvert en video)
- Double opt-in : quand l'utiliser et impact sur les conversions (angle original)

**M3 — Premier email et premiere campagne**
- Creer un template email (4 styles + blocs)
- Lancer ta premiere campagne (recipients, sujet, envoi/planification)
- Envoyer un test email
- Lire les stats de campagne

### Modules premium (M4-M16) — Sujets a forte valeur ajoutee

**M4 — Fluent Forms : generer des leads**
- Integration complete Fluent Forms + FluentCRM
- Dynamic tag selection (couvert en video 101 mais pas en profondeur)
- Shortcode, customisation, conditional logic

**M5 — Email sequences et nurturing**
- Construire une sequence d'onboarding (cas d'usage concret — gap video)
- Timing optimal, jours specifiques
- Sequence de re-engagement (contenu 100% original)

**M6 — Automation funnels : fondamentaux**
- Triggers, actions, goals, conditionals
- Workflow type : form submission → list → delay → welcome email → upsell
- Automation reports

**M7 — Automation avancee**
- Split test dans automations (couvert en video, absent de la doc)
- Goals optionnels vs essentiels (use case concret)
- Multi-path conditionals
- Import/export d'automations

**M8 — Smart links : tracker chaque clic**
- Creation et utilisation de smart links
- Auto Login with Smart Links (gap video — doc only)
- Strategies : segmentation par comportement de clic

**M9 — WooCommerce + FluentCRM** (forte demande commentaires)
- Sync automatique des clients
- Checkout subscription checkbox
- Segmentation par produit et par montant d'achat
- **Abandoned cart** (gap majeur — doc dispo, aucune video, question recurrente)
- Upsell automatise post-achat

**M10 — TutorLMS + FluentCRM** (sujet strategique schoolsWP)
- Integration detaillee (gap video total — doc dispo `fluentcrm-tutorlms.md`)
- Triggers : enrollment, course completion
- Actions : enroll in course, remove from course
- Goals et conditionals specifiques TutorLMS
- Advanced filtering par cours
- Rapports avances TutorLMS
- *Angle original schoolsWP : cas reel avec la propre formation schoolsWP*

**M11 — Recurring campaigns et newsletters**
- Creer une newsletter recurrente (gap total — jamais montre en video)
- Bloc Latest Post / RSS
- Planification hebdo/mensuelle

**M12 — Conditional sections et personnalisation**
- Sections conditionnelles dans les emails (par tags)
- Sections conditionnelles dans les pages WordPress
- Merge codes avances : data transformers, fallback values (gap video)

**M13 — Webhooks et connexions externes**
- Incoming webhooks (collecte depuis site externe)
- Outgoing webhooks (Zapier, Make, n8n)
- Cas d'usage : export vers Google Sheets (couvert en video 101)
- *Angle original schoolsWP : connexion avec n8n pour les workflows automatises*

**M14 — Event tracking et comportement utilisateur**
- Activer le module event tracking (gap total — jamais montre en video)
- Configurer des evenements personnalises
- Automatiser en fonction du comportement

**M15 — Rapports et optimisation**
- Advanced reports : croissance contacts, stats emails, comparaison periodes (gap video)
- Rapports WooCommerce et LMS dans FluentCRM
- Company module (gap video)
- Compliance GDPR (gap video)

**M16 — Deliverabilite et performance**
- Email deliverability en profondeur (gap video)
- Bounce handlers
- Cron jobs (remplacer WP-Cron)
- Multi-threading
- Advanced features config

### Angles originaux schoolsWP (pas juste une traduction de la doc)

1. **Stack reelle schoolsWP** : chaque module utilise l'installation reelle (TutorLMS + FluentCRM + WooCommerce + Fluent Forms) — pas un site de demo vide
2. **Cas d'usage formation en ligne** : sequences de nurturing pour etudiants, automatisation des relances cours non termines, upsell vers modules premium
3. **Integration n8n** : connecter FluentCRM a des workflows n8n pour des automatisations impossibles nativement (scoring leads, sync CRM externe, alertes Telegram)
4. **Comparatif free vs pro avec decision tree** : aider l'utilisateur a decider quand passer en Pro (aucun contenu existant ne le fait clairement)
5. **Abandoned cart en contexte formation** : adapter le panier abandonne WooCommerce au contexte vente de formation (pas un e-commerce classique)
6. **Email individuel : le workaround** : montrer comment envoyer un email "individuel" via une campagne a 1 contact ou via l'automation (repondre au besoin recurrent)
7. **Francais natif avec tutoiement** : toutes les videos existantes sont en anglais — la formation en francais est un differenciateur majeur
8. **TutorLMS + FluentCRM : le duo que personne ne montre** : integration detaillee absente de toutes les videos YouTube, pourtant documentee

---

## Annexe : Mapping fichiers doc → categories

| Fichier | Categorie |
|---------|-----------|
| `fluentcrm-install-upgrade.md` | Getting Started |
| `fluentcrm-global-settings.md` | Settings |
| `fluentcrm-business-settings.md` | Settings |
| `fluentcrm-general-settings.md` | Settings |
| `fluentcrm-email-settings.md` | Settings |
| `fluentcrm-compliance-settings.md` | Settings |
| `fluentcrm-custom-fields.md` | Settings |
| `fluentcrm-smartlinks.md` | Settings |
| `fluentcrm-integration-settings.md` | Settings |
| `fluentcrm-double-optin.md` | Settings |
| `fluentcrm-incoming-webhooks.md` | Settings |
| `fluentcrm-contacts-dashboard.md` | Contacts |
| `fluentcrm-contact-overview.md` | Contacts |
| `fluentcrm-contact-statuses.md` | Contacts |
| `fluentcrm-manage-contacts.md` | Contacts |
| `fluentcrm-advanced-filter.md` | Contacts |
| `fluentcrm-import-contacts.md` | Contacts |
| `fluentcrm-export-contacts.md` | Contacts |
| `fluentcrm-email-campaigns.md` | Emails |
| `fluentcrm-email-templates.md` | Emails |
| `fluentcrm-email-sequence.md` | Emails |
| `fluentcrm-recurring-campaign.md` | Emails |
| `fluentcrm-compose-email.md` | Emails |
| `fluentcrm-campaign-summary.md` | Emails |
| `fluentcrm-campaign-labels.md` | Emails |
| `fluentcrm-emails-overview.md` | Emails |
| `fluentcrm-conditional-sections.md` | Emails |
| `fluentcrm-merge-codes.md` | Emails |
| `fluentcrm-automation-intro.md` | Automation |
| `fluentcrm-automation-editor.md` | Automation |
| `fluentcrm-automation-triggers.md` | Automation |
| `fluentcrm-automation-actions.md` | Automation |
| `fluentcrm-automation-conditionals.md` | Automation |
| `fluentcrm-automation-goals.md` | Automation |
| `fluentcrm-automation-reports.md` | Automation |
| `fluentcrm-automation-labels.md` | Automation |
| `fluentcrm-wp-automation-actions.md` | Automation |
| `fluentcrm-event-tracking.md` | Advanced |
| `fluentcrm-advanced-reports.md` | Advanced |
| `fluentcrm-advanced-features.md` | Advanced |
| `fluentcrm-company-module.md` | Advanced |
| `fluentcrm-abandoned-cart.md` | Advanced |
| `fluentcrm-faq.md` | Advanced |
| `fluentcrm-woocommerce.md` | Integrations |
| `fluentcrm-fluent-forms.md` | Integrations |
| `fluentcrm-optin-forms.md` | Integrations |
| `fluentcrm-learndash.md` | Integrations |
| `fluentcrm-tutorlms.md` | Integrations |
| `fluentcrm-webhook.md` | Integrations |
| `fluentcrm-deliverability.md` | Integrations |
| `fluentcrm-smtp-bounce.md` | Integrations |

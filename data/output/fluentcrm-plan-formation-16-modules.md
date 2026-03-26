# Plan de formation — Maitriser FluentCRM

**Version** : 1.0
**Date** : 2026-03-21
**Auteur** : schoolsWP (Michael KIHL)
**Plateforme** : TutorLMS Pro
**Format** : Videos HeyGen + voix ElevenLabs
**Langue** : Francais (tutoiement)
**Modele** : Freemium (M1-M3 gratuits, M4-M16 premium)

## Vue d'ensemble

| Module | Titre | Lecons | Duree | Type |
|--------|-------|--------|-------|------|
| M1 | Decouverte et installation | 8 | 45 min | Gratuit |
| M2 | Premiers contacts et segmentation | 9 | 50 min | Gratuit |
| M3 | Premier email et premiere campagne | 8 | 45 min | Gratuit |
| M4 | Fluent Forms : generer des leads | 8 | 50 min | Premium |
| M5 | Email sequences et nurturing | 8 | 50 min | Premium |
| M6 | Automation funnels : fondamentaux | 9 | 55 min | Premium |
| M7 | Automation avancee | 8 | 50 min | Premium |
| M8 | Smart links : tracker chaque clic | 7 | 40 min | Premium |
| M9 | WooCommerce + FluentCRM | 9 | 55 min | Premium |
| M10 | TutorLMS + FluentCRM | 9 | 55 min | Premium |
| M11 | Recurring campaigns et newsletters | 7 | 40 min | Premium |
| M12 | Conditional sections et personnalisation | 8 | 45 min | Premium |
| M13 | Webhooks et connexions externes | 8 | 50 min | Premium |
| M14 | Event tracking et comportement utilisateur | 7 | 40 min | Premium |
| M15 | Rapports et optimisation | 9 | 50 min | Premium |
| M16 | Delivrabilite et performance | 8 | 45 min | Premium |

**Total** : 130 lecons, ~11h05 de contenu

---

## Module 1 — Decouverte et installation

**Objectif pedagogique** : A la fin de ce module, tu sais installer FluentCRM (free et Pro), configurer les reglages de base, et tu comprends clairement ce que FluentCRM fait — et ne fait pas.
**Prerequis** : Un site WordPress fonctionnel (hebergement + domaine)
**Duree estimee** : 45 minutes
**Type** : Gratuit

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 1.1 | Comprends le role de FluentCRM : CRM + email marketing, pas un client email | 5 min | Video | `fluentcrm-free-wordpress-crm-plugin.md`, `fluentcrm-whats-inside.md` |
| 1.2 | Free vs Pro : le comparatif honnete pour choisir | 7 min | Video | FAQ commentaires YouTube, `fluentcrm-faq.md` |
| 1.3 | Faut-il un service email externe avec FluentCRM ? | 5 min | Video | FAQ commentaires YouTube, `fluentcrm-deliverability.md` |
| 1.4 | Installe FluentCRM Free depuis WordPress.org | 5 min | Video | `fluentcrm-install-upgrade.md`, `fluentcrm-quickstart-guide-configure.md` |
| 1.5 | Passe en Pro : upload du zip et activation de licence | 5 min | Video | `fluentcrm-install-upgrade.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:44) |
| 1.6 | Configure les reglages Business (nom, adresse, logo) | 5 min | Video | `fluentcrm-business-settings.md`, `fluentcrm-quickstart-guide-configure.md` |
| 1.7 | Configure FluentSMTP pour envoyer tes emails | 8 min | Video | `fluentcrm-smtp-bounce.md`, `fluentcrm-deliverability.md`, `fluentcrm-quickstart-guide-configure.md` (03:37) |
| 1.8 | Quiz — Valide tes acquis M1 | 5 min | Quiz | — |

### Points cles a couvrir
- Difference CRM vs client email (repondre au malentendu frequent : FluentCRM n'est pas un inbox)
- Comparatif free vs Pro avec arbre de decision clair (gap identifie — aucun contenu existant)
- Role de FluentSMTP vs services comme Brevo, Amazon SES, SendGrid
- Pre-requis techniques (PHP 7.4+, WP 5.6+, cron fonctionnel)
- Pourquoi FluentCRM est auto-heberge (tes donnees restent chez toi)

### Angle schoolsWP
- Arbre de decision free vs Pro adapte au contexte formation en ligne (tu vends des cours ? tu as besoin de Pro)
- Demo sur l'installation reelle schoolsWP (pas un site vierge)
- Comparaison avec les alternatives SaaS (MailChimp, ConvertKit) en termes de cout annuel pour un createur de formation

---

## Module 2 — Premiers contacts et segmentation

**Objectif pedagogique** : Tu sais ajouter, importer et organiser tes contacts avec des listes, tags et segments dynamiques. Tu comprends les statuts de contact et le double opt-in.
**Prerequis** : M1
**Duree estimee** : 50 minutes
**Type** : Gratuit

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 2.1 | Decouvre le dashboard Contacts | 5 min | Video | `fluentcrm-contacts-dashboard.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (32:52) |
| 2.2 | Ajoute ton premier contact manuellement | 4 min | Video | `fluentcrm-manage-contacts.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (06:54) |
| 2.3 | Importe tes contacts depuis un CSV | 6 min | Video | `fluentcrm-import-contacts.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (06:54) |
| 2.4 | Importe depuis MailChimp, ConvertKit ou ActiveCampaign | 6 min | Video | `fluentcrm-101-mastery-ultimate-tutorial.md` (06:54), `fluentcrm-import-contacts.md` |
| 2.5 | Organise avec les listes et les tags — ta strategie de nommage | 6 min | Video | `fluentcrm-contacts-dashboard.md`, `fluentcrm-free-wordpress-crm-plugin.md` (3:25) |
| 2.6 | Comprends les 6 statuts de contact (dont Transactional) | 5 min | Video | `fluentcrm-contact-statuses.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (28:24) |
| 2.7 | Cree des segments dynamiques (Pro) | 6 min | Video | `fluentcrm-contacts-dashboard.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (14:52) |
| 2.8 | Double opt-in : quand l'activer et impact sur tes conversions | 7 min | Video | `fluentcrm-double-optin.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (28:24) |
| 2.9 | Quiz — Valide tes acquis M2 | 5 min | Quiz | — |

### Points cles a couvrir
- Les 3 methodes d'import (manuel, CSV, depuis plugin WP/CRM externe)
- Migration depuis un CRM SaaS : export API + cle API (tip video 101)
- Convention de nommage listes/tags recommandee pour ne pas se perdre a 1 000+ contacts
- Statut "Transactional" : quand et pourquoi l'utiliser (gap video)
- Double opt-in : obligatoire GDPR ? Impact taux de conversion, recommandation par contexte

### Angle schoolsWP
- Strategie de tagging adaptee a la vente de formation (tag par pilier, par niveau, par source)
- Cas reel : import des utilisateurs TutorLMS existants dans FluentCRM
- Decision tree double opt-in : blog francais (oui, RGPD) vs liste acheteurs (non, relation commerciale)

---

## Module 3 — Premier email et premiere campagne

**Objectif pedagogique** : Tu sais creer un template email, composer un email avec les smart codes, lancer ta premiere campagne et lire les statistiques.
**Prerequis** : M2
**Duree estimee** : 45 minutes
**Type** : Gratuit

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 3.1 | Cree ton premier template email | 6 min | Video | `fluentcrm-email-templates.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (19:04) |
| 3.2 | Compose un email : blocs, images et mise en page | 6 min | Video | `fluentcrm-compose-email.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (19:04) |
| 3.3 | Personnalise avec les smart codes (prenom, site, etc.) | 5 min | Video | `fluentcrm-merge-codes.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (19:04) |
| 3.4 | Lance ta premiere campagne email | 6 min | Video | `fluentcrm-email-campaigns.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (24:02) |
| 3.5 | Planifie l'envoi et configure les UTM | 5 min | Video | `fluentcrm-email-campaigns.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (24:02) |
| 3.6 | Lis les stats de ta campagne (ouvertures, clics, desabonnements) | 5 min | Video | `fluentcrm-campaign-summary.md` |
| 3.7 | Envoyer un email "individuel" : le workaround malin | 5 min | Video | FAQ commentaires YouTube |
| 3.8 | Quiz — Valide tes acquis M3 | 7 min | Quiz | — |

### Points cles a couvrir
- Les 4 styles de templates (Raw HTML, Simple, Plain, Visual)
- Blocs de contenu : texte, image, bouton, separateur, colonnes
- Smart codes essentiels : `{{contact.first_name}}`, `{{contact.email}}`
- Workflow campagne : brouillon → selection recipients → sujet → envoi/planification
- A/B testing de sujets (mention, developpe en M5)
- Le "hack" email individuel : campagne avec filtre sur 1 contact

### Angle schoolsWP
- Template adapte a un createur de formation (header sobre, CTA vers le cours, footer conforme RGPD)
- Cas concret : email de bienvenue pour les nouveaux inscrits au module gratuit
- Lecture des stats dans le contexte formation (taux d'ouverture attendu, benchmarks)

---

## Module 4 — Fluent Forms : generer des leads

**Objectif pedagogique** : Tu sais creer un formulaire avec Fluent Forms, le connecter a FluentCRM, et segmenter automatiquement les leads a l'inscription.
**Prerequis** : M3
**Duree estimee** : 50 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 4.1 | Installe et decouvre Fluent Forms | 5 min | Video | `fluentcrm-fluent-forms.md` |
| 4.2 | Cree ton formulaire de capture d'email | 6 min | Video | `fluentcrm-optin-forms.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (37:37) |
| 4.3 | Connecte Fluent Forms a FluentCRM (Integration Feed) | 7 min | Video | `fluentcrm-fluent-forms.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (37:37) |
| 4.4 | Tag dynamique : segmente des l'inscription | 6 min | Video | `fluentcrm-fluent-forms.md`, `fluentcrm-free-wordpress-crm-plugin.md` (6:45) |
| 4.5 | Conditional logic : adapte le formulaire au visiteur | 7 min | Video | `fluentcrm-fluent-forms.md` |
| 4.6 | Place ton formulaire : shortcode, widget, popup | 5 min | Video | `fluentcrm-optin-forms.md` |
| 4.7 | Exercice — Cree un formulaire lead magnet pour ta formation | 8 min | Exercice | — |
| 4.8 | Quiz — Valide tes acquis M4 | 6 min | Quiz | — |

### Points cles a couvrir
- Difference Fluent Forms Free vs Pro pour l'integration CRM
- Mapping des champs formulaire → champs contact FluentCRM
- Tags dynamiques par formulaire (tag different selon la page ou le formulaire)
- Formulaire multi-etapes vs simple
- Opt-in forms natifs FluentCRM vs Fluent Forms (quand utiliser quoi)

### Angle schoolsWP
- Formulaire lead magnet "telecharge le guide gratuit LMS" → tag "lead-lms" automatique
- Pop-up de sortie sur les articles piliers avec tag par pilier
- Stack reelle : Fluent Forms Pro + FluentCRM + TutorLMS = capture → nurture → vente

---

## Module 5 — Email sequences et nurturing

**Objectif pedagogique** : Tu sais creer des sequences d'emails automatisees (onboarding, nurturing, re-engagement) avec un timing optimise.
**Prerequis** : M4
**Duree estimee** : 50 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 5.1 | Comprends les sequences : quand les utiliser vs une campagne | 5 min | Video | `fluentcrm-email-sequence.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (49:28) |
| 5.2 | Cree ta premiere sequence d'onboarding | 7 min | Video | `fluentcrm-email-sequence.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (49:28) |
| 5.3 | Configure le timing : delais, jours specifiques, heures d'envoi | 6 min | Video | `fluentcrm-email-sequence.md` |
| 5.4 | Construis une sequence de nurturing (lead → acheteur) | 8 min | Video | Gap video — contenu original |
| 5.5 | Construis une sequence de re-engagement | 7 min | Video | Gap video — contenu original |
| 5.6 | A/B testing dans tes sequences : teste tes sujets | 5 min | Video | `fluentcrm-email-campaigns.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (24:02) |
| 5.7 | Exercice — Cree ta sequence d'onboarding en 5 emails | 7 min | Exercice | — |
| 5.8 | Quiz — Valide tes acquis M5 | 5 min | Quiz | — |

### Points cles a couvrir
- Sequence vs campagne vs automation : les 3 outils et leurs usages
- Timing optimal : J+0, J+1, J+3, J+7 (bonnes pratiques nurturing)
- Re-engagement : quand declencher, quoi dire, quand nettoyer
- Metrics de sequence : taux de completion, drop-off par email

### Angle schoolsWP
- Sequence d'onboarding type createur de formation : bienvenue → valeur gratuite → temoignage → offre
- Sequence re-engagement pour etudiants inactifs (cours non termine depuis 14 jours)
- Templates de sequences prets a copier, adaptes au contexte formation en ligne

---

## Module 6 — Automation funnels : fondamentaux

**Objectif pedagogique** : Tu comprends l'editeur d'automation visuel, tu sais utiliser les triggers, actions, delais et conditionnels pour creer un funnel complet.
**Prerequis** : M5
**Duree estimee** : 55 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 6.1 | Comprends le vocabulaire : triggers, actions, goals, conditionals | 5 min | Video | `fluentcrm-automation-intro.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (58:00) |
| 6.2 | Decouvre l'editeur d'automation visuel | 6 min | Video | `fluentcrm-automation-editor.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (58:00) |
| 6.3 | Les triggers CRM : form submitted, tag applied, list added | 7 min | Video | `fluentcrm-automation-triggers.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:02:24) |
| 6.4 | Les actions : send email, apply tag, wait, create WP user | 7 min | Video | `fluentcrm-automation-actions.md`, `fluentcrm-wp-automation-actions.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:06:34) |
| 6.5 | Les conditionnels : cree des chemins oui/non | 6 min | Video | `fluentcrm-automation-conditionals.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:16:54) |
| 6.6 | Construis ton premier funnel : inscription → bienvenue → upsell | 8 min | Video | `fluentcrm-101-mastery-ultimate-tutorial.md` (58:00-01:20:00) |
| 6.7 | Lis les rapports d'automation | 5 min | Video | `fluentcrm-automation-reports.md` |
| 6.8 | Exercice — Cree un funnel de bienvenue pour ta formation gratuite | 6 min | Exercice | — |
| 6.9 | Quiz — Valide tes acquis M6 | 5 min | Quiz | — |

### Points cles a couvrir
- Les 3 categories de triggers (CRM, WordPress, integrations)
- Delais intelligents : wait X jours vs wait until specific day
- Creer un utilisateur WordPress depuis FluentCRM (action WP)
- Organiser ses automations avec les labels
- Automation reports : chart view, step analytics, email stats

### Angle schoolsWP
- Funnel type formation freemium : inscription module gratuit → sequence valeur → offre premium → relance
- Demo sur la stack reelle schoolsWP (pas un exemple generique)
- Comparaison avec un funnel equivalent dans un outil SaaS (montre la simplicite FluentCRM)

---

## Module 7 — Automation avancee

**Objectif pedagogique** : Tu maitrises les goals, le split testing dans les automations, les chemins multi-conditionnels et l'import/export de funnels.
**Prerequis** : M6
**Duree estimee** : 50 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 7.1 | Goals : definis des objectifs dans ton funnel | 7 min | Video | `fluentcrm-automation-goals.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:12:42) |
| 7.2 | Goal optionnel vs essentiel : quand utiliser chaque type | 6 min | Video | `fluentcrm-automation-goals.md` |
| 7.3 | Split test A/B dans tes automations | 7 min | Video | `fluentcrm-101-mastery-ultimate-tutorial.md` (01:06:34) — gap doc |
| 7.4 | Multi-path conditionals : plus de 2 chemins | 6 min | Video | `fluentcrm-automation-conditionals.md` |
| 7.5 | Triggers avances : birthday, company, custom field change | 6 min | Video | `fluentcrm-automation-triggers.md` |
| 7.6 | Importe et exporte tes automations | 5 min | Video | `fluentcrm-automation-intro.md` |
| 7.7 | Exercice — Cree un funnel d'upsell avec split test et goal | 8 min | Exercice | — |
| 7.8 | Quiz — Valide tes acquis M7 | 5 min | Quiz | — |

### Points cles a couvrir
- Goal "benchmark" : le contact passe cette etape uniquement s'il remplit la condition
- Split test dans automation : tester deux emails differents dans un meme funnel (tip video 101, absent de la doc)
- Triggers moins evidents : birthday (date custom field), tag removed, company applied
- Export JSON d'automation pour partage ou backup

### Angle schoolsWP
- Funnel upsell post-formation gratuite : split test email video vs email texte
- Goal "a achete le module premium" : sort du funnel de vente des l'achat
- Partage de templates d'automation entre createurs de formation (export/import)

---

## Module 8 — Smart links : tracker chaque clic

**Objectif pedagogique** : Tu sais creer des smart links, les utiliser pour segmenter par comportement de clic, et configurer l'auto-login.
**Prerequis** : M6
**Duree estimee** : 40 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 8.1 | Comprends les smart links : pourquoi tracker les clics | 5 min | Video | `fluentcrm-smartlinks.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (53:57) |
| 8.2 | Cree ton premier smart link | 5 min | Video | `fluentcrm-smartlinks.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (53:57) |
| 8.3 | Configure les actions au clic : tag, liste, redirection | 6 min | Video | `fluentcrm-smartlinks.md` |
| 8.4 | Auto Login with Smart Links : connexion sans mot de passe | 7 min | Video | `fluentcrm-smartlinks.md` — gap video |
| 8.5 | Strategie : segmente tes contacts par centre d'interet via les clics | 6 min | Video | Contenu original |
| 8.6 | Exercice — Cree un email avec 3 smart links pour identifier les interets | 6 min | Exercice | — |
| 8.7 | Quiz — Valide tes acquis M8 | 5 min | Quiz | — |

### Points cles a couvrir
- Smart link vs lien classique : la difference (tracking + actions)
- Actions au clic : ajouter/retirer tag, ajouter a une liste, declencher une automation
- Auto Login : generer un lien de connexion automatique dans les emails (fonctionnalite puissante, non montree en video)
- Limites : smart links ne trackent que les contacts existants (pas les visiteurs anonymes)

### Angle schoolsWP
- Email "quel sujet t'interesse ?" avec 3 smart links (LMS, CRM, SEO) → tag automatique par pilier
- Auto Login pour donner acces direct au cours depuis l'email (experience fluide, zero friction)
- Strategie de segmentation progressive par comportement de clic sur 3-4 emails

---

## Module 9 — WooCommerce + FluentCRM

**Objectif pedagogique** : Tu sais synchroniser WooCommerce avec FluentCRM, segmenter par produit et montant d'achat, automatiser les paniers abandonnes et creer des upsells post-achat.
**Prerequis** : M6
**Duree estimee** : 55 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 9.1 | Active l'integration WooCommerce | 5 min | Video | `fluentcrm-woocommerce.md`, `fluentcrm-integration-settings.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (10:44) |
| 9.2 | Synchronise tes clients existants | 6 min | Video | `fluentcrm-woocommerce.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (10:44) |
| 9.3 | Checkout subscription checkbox : capture des leads a l'achat | 5 min | Video | `fluentcrm-woocommerce.md`, `fluentcrm-general-settings.md` |
| 9.4 | Segmente par produit et par montant d'achat | 7 min | Video | `fluentcrm-woocommerce.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (45:22) |
| 9.5 | Configure le panier abandonne | 8 min | Video | `fluentcrm-abandoned-cart.md` — gap video total |
| 9.6 | Cree un funnel d'upsell post-achat | 7 min | Video | `fluentcrm-101-mastery-ultimate-tutorial.md` (01:06:34) |
| 9.7 | Triggers WooCommerce dans les automations | 6 min | Video | `fluentcrm-automation-triggers.md`, `fluentcrm-woocommerce.md` |
| 9.8 | Exercice — Configure le panier abandonne pour ta boutique de formations | 6 min | Exercice | — |
| 9.9 | Quiz — Valide tes acquis M9 | 5 min | Quiz | — |

### Points cles a couvrir
- Sync automatique vs import ponctuel des clients WooCommerce
- Tags automatiques par produit achete (segmentation fine)
- Panier abandonne : delai optimal, nombre de relances, contenu des emails
- Upsell post-achat : timing, produit complementaire, sequence automatisee
- Triggers WooCommerce : new order, order completed, refund, specific product purchased

### Angle schoolsWP
- Panier abandonne adapte a la vente de formation (pas un e-commerce classique — le message est different)
- Upsell : acheteur module CRM → proposer module Automation apres 7 jours
- Cas reel : l'acheteur d'une formation schoolsWP recoit automatiquement le tag du pilier correspondant

---

## Module 10 — TutorLMS + FluentCRM

**Objectif pedagogique** : Tu maitrises l'integration TutorLMS + FluentCRM : triggers, actions, goals, filtres avances et rapports. Tu sais automatiser tout le parcours etudiant.
**Prerequis** : M6, M9 (recommande)
**Duree estimee** : 55 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 10.1 | Active l'integration TutorLMS dans FluentCRM | 5 min | Video | `fluentcrm-tutorlms.md`, `fluentcrm-integration-settings.md` |
| 10.2 | Importe tes etudiants TutorLMS existants | 5 min | Video | `fluentcrm-import-contacts.md`, `fluentcrm-tutorlms.md` |
| 10.3 | Triggers TutorLMS : enrollment, completion, quiz passed | 7 min | Video | `fluentcrm-tutorlms.md`, `fluentcrm-automation-triggers.md` — gap video total |
| 10.4 | Actions TutorLMS : enroll in course, remove from course | 6 min | Video | `fluentcrm-tutorlms.md` — gap video total |
| 10.5 | Goals et conditionals specifiques TutorLMS | 7 min | Video | `fluentcrm-tutorlms.md`, `fluentcrm-automation-goals.md` — gap video total |
| 10.6 | Filtre avance : segmente par cours, progression, instructeur | 6 min | Video | `fluentcrm-tutorlms.md`, `fluentcrm-advanced-filter.md` |
| 10.7 | Automatise la relance des etudiants inactifs | 8 min | Video | Contenu original schoolsWP |
| 10.8 | Exercice — Cree le funnel complet d'un parcours etudiant | 6 min | Exercice | — |
| 10.9 | Quiz — Valide tes acquis M10 | 5 min | Quiz | — |

### Points cles a couvrir
- Toute l'integration TutorLMS documentee mais jamais montree en video (gap total)
- Triggers : student enrolled, course completed, lesson completed, quiz passed/failed
- Actions : enroll student, remove from course (automatiser les acces)
- Goals : "a termine le cours X" comme condition de passage dans le funnel
- Filtrage avance par cours et progression

### Angle schoolsWP
- Cas reel avec la propre formation schoolsWP : le duo que personne ne montre
- Funnel complet : inscription gratuite M1-M3 → tag "free-student" → sequence nurturing → achat → enroll auto M4-M16
- Relance automatique : etudiant inactif depuis 14 jours → email personnalise avec lien vers sa derniere lecon (via auto-login smart link)
- Rapports avances : combien d'etudiants terminent chaque module, ou sont les drop-offs

---

## Module 11 — Recurring campaigns et newsletters

**Objectif pedagogique** : Tu sais creer des newsletters recurrentes automatiques avec le bloc Latest Post et planifier des envois hebdomadaires ou mensuels.
**Prerequis** : M3
**Duree estimee** : 40 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 11.1 | Comprends les recurring campaigns : newsletter en autopilote | 5 min | Video | `fluentcrm-recurring-campaign.md` — gap video total |
| 11.2 | Cree ta premiere recurring campaign | 6 min | Video | `fluentcrm-recurring-campaign.md` |
| 11.3 | Le bloc Latest Post : insere tes derniers articles automatiquement | 6 min | Video | `fluentcrm-recurring-campaign.md` |
| 11.4 | Le bloc RSS : tire du contenu depuis n'importe quel flux | 5 min | Video | `fluentcrm-recurring-campaign.md` |
| 11.5 | Planifie : hebdo, bimensuel, mensuel — choisis ta frequence | 5 min | Video | `fluentcrm-recurring-campaign.md` |
| 11.6 | Organise tes campagnes avec les labels | 5 min | Video | `fluentcrm-campaign-labels.md` — gap video |
| 11.7 | Quiz — Valide tes acquis M11 | 8 min | Quiz | — |

### Points cles a couvrir
- Recurring campaign = newsletter 100% automatisee (gap total — jamais montre en video)
- Bloc Latest Post : filtre par categorie, nombre d'articles, mise en page
- Bloc RSS : utile pour aggreger du contenu externe
- Planification : jour de la semaine, heure, fuseau horaire
- Campaign labels pour organiser (regulieres vs ponctuelles vs tests)

### Angle schoolsWP
- Newsletter hebdomadaire automatique : les 3 derniers articles du blog schoolsWP envoyes chaque vendredi
- Newsletter mensuelle pour les etudiants premium : recap des nouveaux modules publies
- Cas concret : newsletter segmentee par pilier (les lecteurs LMS ne recoivent pas les articles CRM)

---

## Module 12 — Conditional sections et personnalisation

**Objectif pedagogique** : Tu sais creer des emails et des pages WordPress avec du contenu conditionnel selon les tags, listes ou proprietes du contact. Tu maitrises les merge codes avances.
**Prerequis** : M5, M6
**Duree estimee** : 45 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 12.1 | Comprends les conditional sections : un email, plusieurs versions | 5 min | Video | `fluentcrm-conditional-sections.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:19:34) |
| 12.2 | Cree des sections conditionnelles dans tes emails | 7 min | Video | `fluentcrm-conditional-sections.md` |
| 12.3 | Cree des sections conditionnelles sur tes pages WordPress | 6 min | Video | `fluentcrm-conditional-sections.md` |
| 12.4 | Merge codes avances : data transformers et formatage | 7 min | Video | `fluentcrm-merge-codes.md` — gap video |
| 12.5 | Fallback values : que montrer quand la donnee est vide | 5 min | Video | `fluentcrm-merge-codes.md` — gap video |
| 12.6 | Custom contact fields : ajoute tes propres champs | 6 min | Video | `fluentcrm-custom-fields.md` |
| 12.7 | Exercice — Cree un email avec 3 blocs conditionnels par niveau | 5 min | Exercice | — |
| 12.8 | Quiz — Valide tes acquis M12 | 4 min | Quiz | — |

### Points cles a couvrir
- Conditional sections dans les emails : if tag = "premium" → montre le CTA cours avance
- Conditional sections dans WordPress : page d'accueil personnalisee selon le profil visiteur
- Merge codes complets : structure `{{contact.field_name}}`, data transformers (`ucfirst`, `date_format`)
- Fallback values : `{{contact.first_name | default:"ami"}}` (non montre en video)
- Custom fields : creer, utiliser dans les conditions et les merge codes

### Angle schoolsWP
- Email unique envoye a toute la liste mais avec CTA different : debutant → module gratuit, avance → module premium
- Page d'accueil schoolsWP : affiche le prochain cours recommande selon le tag du visiteur
- Personnalisation du prenom avec fallback (contacts sans prenom = "ami")

---

## Module 13 — Webhooks et connexions externes

**Objectif pedagogique** : Tu sais envoyer et recevoir des donnees via webhooks, connecter FluentCRM a Zapier, Make et n8n, et exporter vers Google Sheets.
**Prerequis** : M6
**Duree estimee** : 50 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 13.1 | Comprends les webhooks : incoming vs outgoing | 5 min | Video | `fluentcrm-incoming-webhooks.md`, `fluentcrm-webhook.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:21:34) |
| 13.2 | Configure un incoming webhook (recois des donnees externes) | 7 min | Video | `fluentcrm-incoming-webhooks.md` |
| 13.3 | Configure un outgoing webhook (envoie des donnees) | 6 min | Video | `fluentcrm-webhook.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:21:34) |
| 13.4 | Connecte FluentCRM a Zapier | 6 min | Video | `fluentcrm-webhook.md`, `fluentcrm-101-mastery-ultimate-tutorial.md` (01:21:34) |
| 13.5 | Connecte FluentCRM a n8n : automatisation sans limites | 8 min | Video | Contenu original schoolsWP |
| 13.6 | Cas d'usage : exporte tes contacts vers Google Sheets | 6 min | Video | `fluentcrm-101-mastery-ultimate-tutorial.md` (01:21:34) |
| 13.7 | Exercice — Cree un webhook n8n qui ajoute un contact a l'achat | 7 min | Exercice | — |
| 13.8 | Quiz — Valide tes acquis M13 | 5 min | Quiz | — |

### Points cles a couvrir
- Incoming webhook : URL unique, mapping des champs, securite (secret key)
- Outgoing webhook : declencheur automation, payload JSON, destination
- Zapier : connexion via webhook (pas de connecteur natif FluentCRM)
- Make (ex-Integromat) : meme principe que Zapier
- n8n : webhook node + HTTP request node pour bidirectionnel

### Angle schoolsWP
- Connexion n8n pour des workflows impossibles nativement : lead scoring automatise, sync CRM externe, alerte Telegram quand un etudiant termine un cours
- Export Google Sheets pour reporting manuel ou partage avec un partenaire
- Architecture webhook schoolsWP : FluentCRM → n8n → actions multiples (notification, enrichissement, scoring)

---

## Module 14 — Event tracking et comportement utilisateur

**Objectif pedagogique** : Tu sais activer le module event tracking, configurer des evenements personnalises et declencher des automations basees sur le comportement de tes visiteurs.
**Prerequis** : M6
**Duree estimee** : 40 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 14.1 | Comprends l'event tracking : suivre ce que font tes contacts | 5 min | Video | `fluentcrm-event-tracking.md` — gap video total |
| 14.2 | Active et configure le module event tracking | 6 min | Video | `fluentcrm-event-tracking.md` |
| 14.3 | Cree des evenements personnalises (page visitee, bouton clique) | 7 min | Video | `fluentcrm-event-tracking.md` |
| 14.4 | Utilise les evenements comme triggers d'automation | 7 min | Video | `fluentcrm-event-tracking.md`, `fluentcrm-automation-triggers.md` |
| 14.5 | Consulte l'historique comportemental d'un contact | 5 min | Video | `fluentcrm-event-tracking.md`, `fluentcrm-contact-overview.md` |
| 14.6 | Exercice — Configure le tracking de ta page de vente et declenche une relance | 5 min | Exercice | — |
| 14.7 | Quiz — Valide tes acquis M14 | 5 min | Quiz | — |

### Points cles a couvrir
- Event tracking = suivi comportemental integre a WordPress (pas besoin de Google Analytics)
- Types d'evenements : page view, button click, form submission, custom event
- Timeline comportementale dans la fiche contact
- Lien event tracking + automation : "a visite la page pricing 3 fois" → email personnalise
- Difference avec les smart links (M8) : event tracking = plus large, smart links = specifique emails

### Angle schoolsWP
- Tracker les pages de vente : etudiant gratuit visite la page premium 2 fois → declenchement sequence de vente
- Tracker la progression dans les cours : complements au tracking natif TutorLMS
- Scoring comportemental : chaque event = points, seuil atteint = notification au formateur

---

## Module 15 — Rapports et optimisation

**Objectif pedagogique** : Tu sais exploiter les rapports avances, analyser la croissance contacts et les stats email, utiliser le company module, et configurer la conformite RGPD.
**Prerequis** : M9, M10 (recommande)
**Duree estimee** : 50 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 15.1 | Decouvre les rapports avances (contact growth, email stats) | 6 min | Video | `fluentcrm-advanced-reports.md` — gap video |
| 15.2 | Rapports WooCommerce dans FluentCRM | 5 min | Video | `fluentcrm-advanced-reports.md` |
| 15.3 | Rapports LMS dans FluentCRM | 5 min | Video | `fluentcrm-advanced-reports.md` |
| 15.4 | Vue d'ensemble des emails envoyes (Email Overview) | 5 min | Video | `fluentcrm-emails-overview.md` — gap video |
| 15.5 | Le Company module : organise tes contacts par entreprise | 6 min | Video | `fluentcrm-company-module.md` — gap video |
| 15.6 | Exporte tes contacts (Pro) | 5 min | Video | `fluentcrm-export-contacts.md` — gap video |
| 15.7 | Compliance RGPD : anonymisation, export donnees, consentement | 7 min | Video | `fluentcrm-compliance-settings.md` — gap video |
| 15.8 | Exercice — Analyse tes metriques et identifie 3 actions d'amelioration | 6 min | Exercice | — |
| 15.9 | Quiz — Valide tes acquis M15 | 5 min | Quiz | — |

### Points cles a couvrir
- Rapports avances : croissance contacts (graphiques), stats email (ouvertures, clics, bounces), comparaison periodes
- Rapports integration : chiffre d'affaires WooCommerce, progression etudiants LMS
- Company module : regrouper les contacts par entreprise, logo automatique depuis le domaine email
- Export contacts : formats, filtres, planification
- Compliance RGPD : anonymiser IP, supprimer un contact proprement, exporter ses donnees, one-click unsubscribe

### Angle schoolsWP
- Dashboard mensuel du formateur : combien de leads, combien de ventes, quel cours performe
- Company module utile pour les formations B2B (plusieurs employes de la meme entreprise inscrits)
- Checklist RGPD complete adaptee au contexte francais (CNIL)

---

## Module 16 — Delivrabilite et performance

**Objectif pedagogique** : Tu sais optimiser la delivrabilite de tes emails, configurer les bounce handlers, remplacer WP-Cron, activer le multi-threading et gerer les reglages avances.
**Prerequis** : M1 (SMTP), M6 (recommande)
**Duree estimee** : 45 minutes
**Type** : Premium

### Lecons

| # | Titre de la lecon | Duree | Type | Source principale |
|---|-------------------|-------|------|-------------------|
| 16.1 | Comprends la delivrabilite : pourquoi tes emails arrivent (ou pas) en inbox | 6 min | Video | `fluentcrm-deliverability.md` — gap video |
| 16.2 | Configure SPF, DKIM et DMARC pour ton domaine | 7 min | Video | `fluentcrm-deliverability.md` |
| 16.3 | Configure les bounce handlers | 6 min | Video | `fluentcrm-smtp-bounce.md` — gap video |
| 16.4 | Remplace WP-Cron par un vrai cron job | 6 min | Video | `fluentcrm-deliverability.md`, `fluentcrm-faq.md` — gap video |
| 16.5 | Active le multi-threading pour les gros volumes | 5 min | Video | `fluentcrm-deliverability.md`, `fluentcrm-advanced-features.md` — gap video |
| 16.6 | Reglages avances : quick nav, campaign archives, system log | 6 min | Video | `fluentcrm-advanced-features.md` — gap video |
| 16.7 | REST API : les bases pour developper dessus | 5 min | Video | `fluentcrm-global-settings.md` — gap video |
| 16.8 | Quiz final — Valide tes acquis M16 et la formation complete | 4 min | Quiz | — |

### Points cles a couvrir
- Delivrabilite en profondeur : SPF, DKIM, DMARC (non couvert en video, crucial)
- Bounce handlers : Amazon SES, SendGrid, Mailgun, Postmark — configurer le retour de bounces
- WP-Cron : pourquoi le remplacer (fiabilite), comment configurer un cron serveur
- Multi-threading : envoyer plus d'emails par minute (reglage selon l'hebergeur)
- Campaign archives : page publique de tes newsletters passees
- System log : debugger les problemes d'envoi
- REST API : endpoints principaux, authentification, cas d'usage basiques

### Angle schoolsWP
- Config delivrabilite recommandee pour un hebergement WordPress mutualise vs VPS
- Cron job sur WP1 (hebergement schoolsWP) : la config exacte
- Multi-threading : reglage conservateur (50/min) sur mutualise vs agressif (300/min) sur VPS
- REST API + n8n : creer des contacts depuis un workflow externe

---

## Couverture des gaps et angles originaux

### 13 gaps du gap analysis — ou sont-ils couverts ?

| # | Gap identifie | Module(s) |
|---|---------------|-----------|
| 1 | Recurring campaigns / Newsletter automatique | M11 |
| 2 | Abandoned cart WooCommerce | M9 (lecon 9.5) |
| 3 | Event tracking | M14 |
| 4 | Company module | M15 (lecon 15.5) |
| 5 | Advanced reports | M15 (lecons 15.1-15.3) |
| 6 | Compliance RGPD | M15 (lecon 15.7) |
| 7 | Export contacts | M15 (lecon 15.6) |
| 8 | Email delivrabilite en profondeur | M16 (lecons 16.1-16.5) |
| 9 | REST API | M16 (lecon 16.7) |
| 10 | Campaign labels / Automation labels | M11 (lecon 11.6), M6 |
| 11 | TutorLMS integration detaillee | M10 (entierement dedie) |
| 12 | Merge codes avances | M12 (lecons 12.4-12.5) |
| 13 | Advanced features config | M16 (lecon 16.6) |

### 8 angles originaux schoolsWP — ou sont-ils integres ?

| # | Angle original | Module(s) |
|---|----------------|-----------|
| 1 | Stack reelle schoolsWP (pas un site demo) | Tous les modules |
| 2 | Cas d'usage formation en ligne | M5, M10, M9, M14 |
| 3 | Integration n8n | M13 (lecon 13.5), M16 |
| 4 | Comparatif free vs Pro avec decision tree | M1 (lecon 1.2) |
| 5 | Abandoned cart en contexte formation | M9 (lecon 9.5, exercice 9.8) |
| 6 | Email individuel : le workaround | M3 (lecon 3.7) |
| 7 | Francais natif avec tutoiement | Tous les modules |
| 8 | TutorLMS + FluentCRM : le duo que personne ne montre | M10 (entierement dedie) |

---

## Prochaines etapes

1. **Validation du plan** — Relire ce document, ajuster les durees et l'ordre si necessaire
2. **Redaction des scripts video M1-M3** — Priorite : les 3 modules gratuits qui servent de lead magnet
3. **Upload Drive** — Creer le dossier `Formation FluentCRM/Scripts/M1`, `M2`, `M3` sur Google Drive
4. **Creation des cours dans TutorLMS** — Creer la structure cours + modules + lecons dans le back-office schoolsWP
5. **Production video HeyGen** — Enregistrer les videos avec la voix ElevenLabs clonee, format talking head + screencast
6. **Quiz et exercices** — Creer les quiz dans TutorLMS (QCM), rediger les consignes d'exercices
7. **Lancement freemium** — Publier M1-M3 en acces libre, M4-M16 derriere le paywall WooCommerce
8. **Automation FluentCRM** — Configurer le funnel d'upsell : inscription gratuite → sequence → offre premium (meta : utiliser FluentCRM pour vendre la formation FluentCRM)

# Scripts vidéo — Module 1 : Découverte : OttoKit et l'automatisation WordPress

**Formation** : Maîtriser OttoKit
**Module** : M1 — Découverte : OttoKit et l'automatisation WordPress
**Leçons** : 6 vidéos + 1 quiz
**Durée totale** : ~35 min de vidéo
**Date** : 2026-03-30

---

## Leçon 1.1 — Pourquoi automatiser ton WordPress

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slide pour les chiffres

---

**[INTRO — face caméra]**

Tu gères un site WordPress. Chaque jour, tu fais des dizaines de petites tâches : tu copies des infos d'un formulaire dans un tableur, tu envoies des emails de bienvenue, tu mets à jour ton CRM. Maintenant, imagine que tout ça se fasse tout seul.

C'est exactement ce qu'on va voir dans cette formation.

**[ÉCRAN — slide "Le coût du manuel"]**

Prenons un exemple concret. Tu vends une formation en ligne. Quand quelqu'un achète :

- Tu ajoutes le client dans ton CRM
- Tu envoies un email de confirmation
- Tu notes la vente dans un tableur
- Tu envoies un message Slack à ton équipe
- 15 jours plus tard, tu demandes un avis

Fait manuellement, ça prend 10 minutes par vente. À 10 ventes par jour, c'est presque 2 heures de travail répétitif. Par semaine, ça fait une journée entière perdue.

**[ÉCRAN — slide "L'automatisation change la donne"]**

Avec l'automatisation, toutes ces étapes se déclenchent automatiquement à chaque vente. Zéro intervention. Zéro oubli. Zéro retard.

Et le mieux : tu n'as pas besoin de savoir coder. C'est exactement le rôle d'OttoKit.

**[TRANSITION — face caméra]**

Dans la prochaine leçon, on va voir ce qu'est OttoKit exactement et comment il fonctionne.

---

**Points clés**
- Les tâches répétitives coûtent du temps et de l'énergie
- L'automatisation supprime le travail manuel sans sacrifier la qualité
- Pas besoin de coder pour automatiser avec OttoKit

**Mots-clés SEO**
- automatisation WordPress
- OttoKit tutoriel
- automatiser tâches WordPress
- gagner du temps WordPress

---

## Leçon 1.2 — OttoKit : plateforme cloud + plugin WordPress

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, schéma pour l'architecture, screencast de l'interface

---

**[INTRO — face caméra]**

OttoKit, c'est un outil d'automatisation conçu spécifiquement pour WordPress. Mais attention, ce n'est pas juste un plugin. C'est une plateforme cloud avec un plugin WordPress.

Laisse-moi t'expliquer pourquoi c'est important.

**[ÉCRAN — slide "Architecture cloud + plugin"]**

Voici comment OttoKit fonctionne :

- Le **plugin WordPress** s'installe sur ton site. Son rôle : faire le pont entre ton site et la plateforme cloud.
- La **plateforme cloud** (app.ottokit.com) fait tout le travail : elle exécute tes workflows, gère les connexions, stocke les logs.

Pourquoi c'est malin ? Parce que ton site WordPress ne fait rien de lourd. Pas de files d'attente, pas de cron surchargé, pas de base de données gonflée. Ton site reste rapide.

**[ÉCRAN — screencast app.ottokit.com]**

Quand tu te connectes à OttoKit, tu arrives sur ce tableau de bord.

[Montre le dashboard]
[Pointe les sections : Workflows, Apps, History, Settings]

C'est ici que tu vas créer tes automations. L'interface est visuelle : tu glisses des blocs, tu connectes des apps, et tu publies.

**[ÉCRAN — slide "Ce que OttoKit connecte"]**

OttoKit connecte 3 types d'outils :

1. **Tes plugins WordPress** : WooCommerce, TutorLMS, FluentCRM, Elementor, Gravity Forms...
2. **Tes apps SaaS** : Google Sheets, Slack, Stripe, WhatsApp, Mailchimp...
3. **N'importe quel service** via webhooks et API

Au total, plus de 1 310 intégrations. Et ça augmente chaque semaine.

**[TRANSITION — face caméra]**

Maintenant que tu vois la vue d'ensemble, on va clarifier le vocabulaire. Dans la prochaine leçon, on pose les termes que tu vas utiliser tout au long de cette formation.

---

**Points clés**
- OttoKit = plateforme cloud + plugin WordPress
- Le traitement se fait dans le cloud, pas sur ton serveur
- 1 310+ intégrations : plugins WP, apps SaaS, webhooks
- Ton site reste rapide car il ne gère pas les automations

**Mots-clés SEO**
- OttoKit WordPress
- plateforme automatisation WordPress
- OttoKit cloud
- alternative Zapier WordPress

---

## Leçon 1.3 — Le glossaire indispensable : workflow, trigger, action, task

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro, slides avec définitions visuelles

---

**[INTRO — face caméra]**

Avant de construire quoi que ce soit, tu dois connaître 4 termes. C'est le vocabulaire de base d'OttoKit. Si tu as déjà utilisé Zapier ou n8n, tu vas reconnaître des concepts similaires.

**[ÉCRAN — slide "Les 4 termes clés"]**

**Workflow** : c'est une automatisation complète. Un workflow commence par un événement et exécute une ou plusieurs actions. Dans Zapier, on appelle ça un "Zap". Dans n8n, un "workflow".

**Trigger** : c'est l'événement qui démarre ton workflow. Par exemple : "un client passe une commande", "un formulaire est soumis", "il est 9h du matin".

**Action** : c'est ce que ton workflow fait quand le trigger se déclenche. Par exemple : "envoyer un email", "ajouter une ligne dans Sheets", "créer un contact CRM".

**Task** : c'est l'unité de mesure d'OttoKit. Chaque action exécutée = 1 task. C'est ce que tu paies (ou qui est limité dans le plan gratuit).

**[ÉCRAN — slide "Un workflow en image"]**

Voici un workflow simple :

```
Trigger: Nouvelle commande WooCommerce
  → Action 1: Ajouter le client dans FluentCRM
  → Action 2: Envoyer un email de confirmation
  → Action 3: Logger dans Google Sheets
```

Ce workflow consomme 3 tasks à chaque exécution (1 par action).

**[TRANSITION — face caméra]**

Avec ces 4 termes en tête, tu es prêt. Dans la prochaine leçon, on va parler de l'histoire d'OttoKit — parce que si tu as entendu parler de "SureTriggers", c'est le même outil.

---

**Points clés**
- Workflow = automatisation complète (trigger + actions)
- Trigger = événement déclencheur
- Action = tâche exécutée automatiquement
- Task = unité de mesure (1 action exécutée = 1 task)

**Mots-clés SEO**
- OttoKit glossaire
- workflow automatisation
- trigger action OttoKit
- task OttoKit pricing

---

## Leçon 1.4 — De SureTriggers à OttoKit : ce qui a changé

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra, slides comparatifs, screencast interface

---

**[INTRO — face caméra]**

Si tu cherches "SureTriggers" sur Google, tu vas tomber sur OttoKit. C'est normal : c'est le même outil, avec un nouveau nom. Voici ce qui s'est passé et ce que ça change pour toi.

**[ÉCRAN — slide "L'évolution"]**

- **2023** : Brainstorm Force (l'équipe derrière Astra, Spectra, CartFlows) lance SureTriggers
- **Avril 2025** : SureTriggers devient OttoKit — nouveau nom, nouvelle identité
- **2026** : OttoKit ajoute les AI Agents, le MCP, le Human-in-the-Loop

Le nom change, mais :
- Ton compte reste le même
- Tes workflows restent intacts
- Tes connexions ne bougent pas
- Le plugin WordPress se met à jour automatiquement

**[ÉCRAN — slide "Ce qui est nouveau"]**

Avec le rebranding, OttoKit a ajouté :

- **AI Agents** : des agents intelligents qui décident et agissent
- **MCP** : connecte Claude, ChatGPT ou Cursor directement à OttoKit
- **Human-in-the-Loop** : approuve les actions avant qu'elles s'exécutent
- **Canvas Builder** : éditeur visuel repensé
- **Organisations et Workspaces** : gestion multi-clients

**[ÉCRAN — slide "Le slug WordPress"]**

Sur WordPress.org, le plugin s'appelle toujours `suretriggers` dans l'URL. C'est normal. Le slug ne change pas. Mais le nom affiché est bien "OttoKit: All-in-One Automation Platform".

**[TRANSITION — face caméra]**

Maintenant tu sais d'où vient OttoKit. Dans la prochaine leçon, on va parler argent : est-ce que le plan gratuit suffit ?

---

**Points clés**
- SureTriggers = OttoKit (même outil, nouveau nom)
- Comptes, workflows et connexions migrent automatiquement
- Nouvelles fonctionnalités majeures : AI Agents, MCP, Human-in-the-Loop
- Le slug WordPress reste "suretriggers"

**Mots-clés SEO**
- SureTriggers OttoKit
- OttoKit nouveau nom
- migration SureTriggers
- OttoKit AI Agents

---

## Leçon 1.5 — Free vs Premium : le verdict honnête

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra, tableau comparatif, calculateur

---

**[INTRO — face caméra]**

OttoKit a un plan gratuit. Mais est-ce qu'il suffit pour ton usage ? Je vais être honnête : ça dépend. Voici comment savoir.

**[ÉCRAN — slide "Ce que le plan gratuit inclut"]**

Le plan gratuit te donne :
- Un nombre limité de tasks par mois (vérifie le chiffre exact sur ottokit.com/pricing)
- Des workflows illimités
- L'accès aux intégrations de base
- Pas d'AI Agents
- Pas de MCP
- Support standard

**[ÉCRAN — slide "Les plans premium"]**

OttoKit propose des plans annuels et lifetime :

- **Business Plus** : $39/mois (annuel), 30 000 tasks/mois, workspaces illimités, AI Agents, MCP, support prioritaire
- **Plans lifetime** : paiement unique, tasks mensuelles limitées, idéal si tu as un usage stable

Le plan change selon ton volume. La question clé : combien de tasks par mois tu vas consommer.

**[ÉCRAN — slide "Calcule tes tasks"]**

Voici comment estimer :

- 1 workflow avec 3 actions = 3 tasks par exécution
- 10 commandes par jour × 3 actions = 30 tasks/jour = 900 tasks/mois
- 50 inscriptions newsletter par semaine × 2 actions = 400 tasks/mois

Additionne tous tes workflows. Si tu es sous la limite gratuite, reste en gratuit. Si tu la dépasses, passe en premium.

**[ÉCRAN — slide "Mon arbre de décision"]**

- Tu découvres OttoKit ? → **Gratuit** (teste pendant 1 mois)
- Tu as moins de 10 workflows simples ? → **Gratuit** peut suffire
- Tu veux les AI Agents ou le MCP ? → **Premium obligatoire**
- Tu gères des clients en agence ? → **Business Plus** (workspaces)
- Tu veux un coût fixe à vie ? → **Lifetime** si l'offre est disponible

**[TRANSITION — face caméra]**

Le plan gratuit est un vrai plan utilisable, pas juste un essai déguisé. Mais si tu veux l'IA et le multi-client, il faudra passer en premium. Dans la prochaine leçon, on fait le tour des 1 310 intégrations disponibles.

---

**Points clés**
- Le plan gratuit est fonctionnel pour un usage basique
- AI Agents et MCP sont réservés aux plans premium
- Calcule tes tasks mensuelles avant de choisir un plan
- Lifetime = coût fixe si ton usage est stable

**Mots-clés SEO**
- OttoKit pricing
- OttoKit gratuit
- OttoKit free vs premium
- OttoKit lifetime deal

---

## Leçon 1.6 — 1 310 intégrations : tour d'horizon des possibilités

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra, screencast page intégrations, slides par catégorie

---

**[INTRO — face caméra]**

OttoKit se connecte à plus de 1 310 apps et plugins. Mais tu n'as pas besoin de toutes les connaître. On va faire le tour des catégories pour que tu repères ce qui est utile pour toi.

**[ÉCRAN — screencast ottokit.com/integrations]**

[Montre la page intégrations]
[Scrolle pour montrer le volume]
[Utilise la recherche pour trouver rapidement un outil]

**[ÉCRAN — slide "Plugins WordPress supportés"]**

Les plus utilisés :
- **E-commerce** : WooCommerce, SureCart, Easy Digital Downloads
- **LMS** : TutorLMS, LearnDash, LifterLMS, MasterStudy LMS
- **CRM** : FluentCRM, Groundhogg, Jetpack CRM
- **Formulaires** : Gravity Forms, Fluent Forms, WPForms, SureForms, Elementor Pro
- **Membership** : MemberPress, WishList Member, SureMembers, Restrict Content Pro
- **Communauté** : BuddyBoss
- **Page builders** : Elementor, Beaver Builder, Divi, Bricks, Spectra

**[ÉCRAN — slide "Apps SaaS populaires"]**

- **Productivité** : Google Sheets, Google Drive, Google Calendar, Notion
- **Communication** : Slack, Gmail, WhatsApp, Telegram
- **Paiement** : Stripe, PayPal
- **Email marketing** : Mailchimp, ActiveCampaign, ConvertKit, Brevo, MailerLite
- **Projet** : Trello, ClickUp, Asana, Monday.com, Todoist, Jira
- **CRM** : HubSpot, Zoho CRM
- **Social** : Twitter/X, LinkedIn
- **AI** : OpenAI, Claude (via MCP)

**[ÉCRAN — slide "Et si mon outil n'est pas dans la liste ?"]**

3 solutions :
1. **Webhooks** : connecte n'importe quel service qui supporte les webhooks
2. **API App** : appelle directement l'API REST de ton service
3. **App Builder** : crée ta propre intégration (pour les développeurs)

**[TRANSITION — face caméra]**

Tu as maintenant une vue d'ensemble complète d'OttoKit. Dans le module suivant, on passe à la pratique : installation, connexion, et ton premier workflow.

---

**Points clés**
- 1 310+ intégrations : plugins WP, apps SaaS, webhooks
- Catégorie WP : e-commerce, LMS, CRM, formulaires, membership, communauté
- Catégorie SaaS : productivité, communication, paiement, email, projet, AI
- 3 solutions pour les services non supportés : webhooks, API App, App Builder

**Mots-clés SEO**
- OttoKit intégrations
- OttoKit WooCommerce
- OttoKit TutorLMS
- OttoKit FluentCRM
- OttoKit Google Sheets

---

## Notes de production — Module 1

### Captures à préparer
- Dashboard OttoKit (app.ottokit.com) — vue globale
- Page intégrations ottokit.com — scroll + recherche
- Page pricing ottokit.com — tableau des plans
- WordPress.org/plugins/suretriggers — fiche plugin
- Schéma architecture : site WP ↔ plugin ↔ cloud OttoKit ↔ apps

### Environnement de démo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec WooCommerce + TutorLMS + FluentCRM installés

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 1.1 | 5 min |
| 1.2 | 6 min |
| 1.3 | 5 min |
| 1.4 | 5 min |
| 1.5 | 7 min |
| 1.6 | 7 min |
| **Total M1** | **35 min** |

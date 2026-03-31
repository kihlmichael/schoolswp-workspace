# Scripts video — Module 1 : Decouverte : OttoKit et l'automatisation WordPress

**Formation** : Maitriser OttoKit
**Module** : M1 — Decouverte : OttoKit et l'automatisation WordPress
**Lecons** : 6 videos + 1 quiz
**Duree totale** : ~35 min de video
**Date** : 2026-03-30

---

## Lecon 1.1 — Pourquoi automatiser ton WordPress

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slide pour les chiffres

---

**[INTRO — face camera]**

Tu geres un site WordPress. Chaque jour, tu fais des dizaines de petites taches : tu copies des infos d'un formulaire dans un tableur, tu envoies des emails de bienvenue, tu mets a jour ton CRM. Maintenant, imagine que tout ca se fasse tout seul.

C'est exactement ce qu'on va voir dans cette formation.

**[ECRAN — slide "Le cout du manuel"]**

Prenons un exemple concret. Tu vends une formation en ligne. Quand quelqu'un achete :

- Tu ajoutes le client dans ton CRM
- Tu envoies un email de confirmation
- Tu notes la vente dans un tableur
- Tu envoies un message Slack a ton equipe
- 15 jours plus tard, tu demandes un avis

Fait manuellement, ca prend 10 minutes par vente. A 10 ventes par jour, c'est presque 2 heures de travail repetitif. Par semaine, ca fait une journee entiere perdue.

**[ECRAN — slide "L'automatisation change la donne"]**

Avec l'automatisation, toutes ces etapes se declenchent automatiquement a chaque vente. Zero intervention. Zero oubli. Zero retard.

Et le mieux : tu n'as pas besoin de savoir coder. C'est exactement le role d'OttoKit.

**[TRANSITION — face camera]**

Dans la prochaine lecon, on va voir ce qu'est OttoKit exactement et comment il fonctionne.

---

**Points cles**
- Les taches repetitives coutent du temps et de l'energie
- L'automatisation supprime le travail manuel sans sacrifier la qualite
- Pas besoin de coder pour automatiser avec OttoKit

**Mots-cles SEO**
- automatisation WordPress
- OttoKit tutoriel
- automatiser taches WordPress
- gagner du temps WordPress

---

## Lecon 1.2 — OttoKit : plateforme cloud + plugin WordPress

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, schema pour l'architecture, screencast de l'interface

---

**[INTRO — face camera]**

OttoKit, c'est un outil d'automatisation concu specifiquement pour WordPress. Mais attention, ce n'est pas juste un plugin. C'est une plateforme cloud avec un plugin WordPress.

Laisse-moi t'expliquer pourquoi c'est important.

**[ECRAN — slide "Architecture cloud + plugin"]**

Voici comment OttoKit fonctionne :

- Le **plugin WordPress** s'installe sur ton site. Son role : faire le pont entre ton site et la plateforme cloud.
- La **plateforme cloud** (app.ottokit.com) fait tout le travail : elle execute tes workflows, gere les connexions, stocke les logs.

Pourquoi c'est malin ? Parce que ton site WordPress ne fait rien de lourd. Pas de files d'attente, pas de cron surchargé, pas de base de donnees gonflee. Ton site reste rapide.

**[ECRAN — screencast app.ottokit.com]**

Quand tu te connectes a OttoKit, tu arrives sur ce tableau de bord.

[Montre le dashboard]
[Pointe les sections : Workflows, Apps, History, Settings]

C'est ici que tu vas creer tes automations. L'interface est visuelle : tu glisses des blocs, tu connectes des apps, et tu publies.

**[ECRAN — slide "Ce que OttoKit connecte"]**

OttoKit connecte 3 types d'outils :

1. **Tes plugins WordPress** : WooCommerce, TutorLMS, FluentCRM, Elementor, Gravity Forms...
2. **Tes apps SaaS** : Google Sheets, Slack, Stripe, WhatsApp, Mailchimp...
3. **N'importe quel service** via webhooks et API

Au total, plus de 1 310 integrations. Et ca augmente chaque semaine.

**[TRANSITION — face camera]**

Maintenant que tu vois la vue d'ensemble, on va clarifier le vocabulaire. Dans la prochaine lecon, on pose les termes que tu vas utiliser tout au long de cette formation.

---

**Points cles**
- OttoKit = plateforme cloud + plugin WordPress
- Le traitement se fait dans le cloud, pas sur ton serveur
- 1 310+ integrations : plugins WP, apps SaaS, webhooks
- Ton site reste rapide car il ne gere pas les automations

**Mots-cles SEO**
- OttoKit WordPress
- plateforme automatisation WordPress
- OttoKit cloud
- alternative Zapier WordPress

---

## Lecon 1.3 — Le glossaire indispensable : workflow, trigger, action, task

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro, slides avec definitions visuelles

---

**[INTRO — face camera]**

Avant de construire quoi que ce soit, tu dois connaitre 4 termes. C'est le vocabulaire de base d'OttoKit. Si tu as deja utilise Zapier ou n8n, tu vas reconnaitre des concepts similaires.

**[ECRAN — slide "Les 4 termes cles"]**

**Workflow** : c'est une automatisation complete. Un workflow commence par un evenement et execute une ou plusieurs actions. Dans Zapier, on appelle ca un "Zap". Dans n8n, un "workflow".

**Trigger** : c'est l'evenement qui demarre ton workflow. Par exemple : "un client passe une commande", "un formulaire est soumis", "il est 9h du matin".

**Action** : c'est ce que ton workflow fait quand le trigger se declenche. Par exemple : "envoyer un email", "ajouter une ligne dans Sheets", "creer un contact CRM".

**Task** : c'est l'unite de mesure d'OttoKit. Chaque action executee = 1 task. C'est ce que tu paies (ou qui est limite dans le plan gratuit).

**[ECRAN — slide "Un workflow en image"]**

Voici un workflow simple :

```
Trigger: Nouvelle commande WooCommerce
  → Action 1: Ajouter le client dans FluentCRM
  → Action 2: Envoyer un email de confirmation
  → Action 3: Logger dans Google Sheets
```

Ce workflow consomme 3 tasks a chaque execution (1 par action).

**[TRANSITION — face camera]**

Avec ces 4 termes en tete, tu es pret. Dans la prochaine lecon, on va parler de l'histoire d'OttoKit — parce que si tu as entendu parler de "SureTriggers", c'est le meme outil.

---

**Points cles**
- Workflow = automatisation complete (trigger + actions)
- Trigger = evenement declencheur
- Action = tache executee automatiquement
- Task = unite de mesure (1 action executee = 1 task)

**Mots-cles SEO**
- OttoKit glossaire
- workflow automatisation
- trigger action OttoKit
- task OttoKit pricing

---

## Lecon 1.4 — De SureTriggers a OttoKit : ce qui a change

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera, slides comparatifs, screencast interface

---

**[INTRO — face camera]**

Si tu cherches "SureTriggers" sur Google, tu vas tomber sur OttoKit. C'est normal : c'est le meme outil, avec un nouveau nom. Voici ce qui s'est passe et ce que ca change pour toi.

**[ECRAN — slide "L'evolution"]**

- **2023** : Brainstorm Force (l'equipe derriere Astra, Spectra, CartFlows) lance SureTriggers
- **Avril 2025** : SureTriggers devient OttoKit — nouveau nom, nouvelle identite
- **2026** : OttoKit ajoute les AI Agents, le MCP, le Human-in-the-Loop

Le nom change, mais :
- Ton compte reste le meme
- Tes workflows restent intacts
- Tes connexions ne bougent pas
- Le plugin WordPress se met a jour automatiquement

**[ECRAN — slide "Ce qui est nouveau"]**

Avec le rebranding, OttoKit a ajoute :

- **AI Agents** : des agents intelligents qui decident et agissent
- **MCP** : connecte Claude, ChatGPT ou Cursor directement a OttoKit
- **Human-in-the-Loop** : approuve les actions avant qu'elles s'executent
- **Canvas Builder** : editeur visuel repense
- **Organisations et Workspaces** : gestion multi-clients

**[ECRAN — slide "Le slug WordPress"]**

Sur WordPress.org, le plugin s'appelle toujours `suretriggers` dans l'URL. C'est normal. Le slug ne change pas. Mais le nom affiche est bien "OttoKit: All-in-One Automation Platform".

**[TRANSITION — face camera]**

Maintenant tu sais d'ou vient OttoKit. Dans la prochaine lecon, on va parler argent : est-ce que le plan gratuit suffit ?

---

**Points cles**
- SureTriggers = OttoKit (meme outil, nouveau nom)
- Comptes, workflows et connexions migrent automatiquement
- Nouvelles fonctionnalites majeures : AI Agents, MCP, Human-in-the-Loop
- Le slug WordPress reste "suretriggers"

**Mots-cles SEO**
- SureTriggers OttoKit
- OttoKit nouveau nom
- migration SureTriggers
- OttoKit AI Agents

---

## Lecon 1.5 — Free vs Premium : le verdict honnete

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera, tableau comparatif, calculateur

---

**[INTRO — face camera]**

OttoKit a un plan gratuit. Mais est-ce qu'il suffit pour ton usage ? Je vais etre honnete : ca depend. Voici comment savoir.

**[ECRAN — slide "Ce que le plan gratuit inclut"]**

Le plan gratuit te donne :
- Un nombre limite de tasks par mois (verifie le chiffre exact sur ottokit.com/pricing)
- Des workflows illimites
- L'acces aux integrations de base
- Pas d'AI Agents
- Pas de MCP
- Support standard

**[ECRAN — slide "Les plans premium"]**

OttoKit propose des plans annuels et lifetime :

- **Business Plus** : $39/mois (annuel), 30 000 tasks/mois, workspaces illimites, AI Agents, MCP, support prioritaire
- **Plans lifetime** : paiement unique, tasks mensuelles limitees, ideal si tu as un usage stable

Le plan change selon ton volume. La question cle : combien de tasks par mois tu vas consommer.

**[ECRAN — slide "Calcule tes tasks"]**

Voici comment estimer :

- 1 workflow avec 3 actions = 3 tasks par execution
- 10 commandes par jour × 3 actions = 30 tasks/jour = 900 tasks/mois
- 50 inscriptions newsletter par semaine × 2 actions = 400 tasks/mois

Additionne tous tes workflows. Si tu es sous la limite gratuite, reste en gratuit. Si tu la depasses, passe en premium.

**[ECRAN — slide "Mon arbre de decision"]**

- Tu decouvres OttoKit ? → **Gratuit** (teste pendant 1 mois)
- Tu as moins de 10 workflows simples ? → **Gratuit** peut suffire
- Tu veux les AI Agents ou le MCP ? → **Premium obligatoire**
- Tu geres des clients en agence ? → **Business Plus** (workspaces)
- Tu veux un cout fixe a vie ? → **Lifetime** si l'offre est disponible

**[TRANSITION — face camera]**

Le plan gratuit est un vrai plan utilisable, pas juste un essai deguise. Mais si tu veux l'IA et le multi-client, il faudra passer en premium. Dans la prochaine lecon, on fait le tour des 1 310 integrations disponibles.

---

**Points cles**
- Le plan gratuit est fonctionnel pour un usage basique
- AI Agents et MCP sont reserves aux plans premium
- Calcule tes tasks mensuelles avant de choisir un plan
- Lifetime = cout fixe si ton usage est stable

**Mots-cles SEO**
- OttoKit pricing
- OttoKit gratuit
- OttoKit free vs premium
- OttoKit lifetime deal

---

## Lecon 1.6 — 1 310 integrations : tour d'horizon des possibilites

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera, screencast page integrations, slides par categorie

---

**[INTRO — face camera]**

OttoKit se connecte a plus de 1 310 apps et plugins. Mais tu n'as pas besoin de toutes les connaitre. On va faire le tour des categories pour que tu reperes ce qui est utile pour toi.

**[ECRAN — screencast ottokit.com/integrations]**

[Montre la page integrations]
[Scrolle pour montrer le volume]
[Utilise la recherche pour trouver rapidement un outil]

**[ECRAN — slide "Plugins WordPress supportes"]**

Les plus utilises :
- **E-commerce** : WooCommerce, SureCart, Easy Digital Downloads
- **LMS** : TutorLMS, LearnDash, LifterLMS, MasterStudy LMS
- **CRM** : FluentCRM, Groundhogg, Jetpack CRM
- **Formulaires** : Gravity Forms, Fluent Forms, WPForms, SureForms, Elementor Pro
- **Membership** : MemberPress, WishList Member, SureMembers, Restrict Content Pro
- **Communaute** : BuddyBoss
- **Page builders** : Elementor, Beaver Builder, Divi, Bricks, Spectra

**[ECRAN — slide "Apps SaaS populaires"]**

- **Productivite** : Google Sheets, Google Drive, Google Calendar, Notion
- **Communication** : Slack, Gmail, WhatsApp, Telegram
- **Paiement** : Stripe, PayPal
- **Email marketing** : Mailchimp, ActiveCampaign, ConvertKit, Brevo, MailerLite
- **Projet** : Trello, ClickUp, Asana, Monday.com, Todoist, Jira
- **CRM** : HubSpot, Zoho CRM
- **Social** : Twitter/X, LinkedIn
- **AI** : OpenAI, Claude (via MCP)

**[ECRAN — slide "Et si mon outil n'est pas dans la liste ?"]**

3 solutions :
1. **Webhooks** : connecte n'importe quel service qui supporte les webhooks
2. **API App** : appelle directement l'API REST de ton service
3. **App Builder** : cree ta propre integration (pour les developpeurs)

**[TRANSITION — face camera]**

Tu as maintenant une vue d'ensemble complete d'OttoKit. Dans le module suivant, on passe a la pratique : installation, connexion, et ton premier workflow.

---

**Points cles**
- 1 310+ integrations : plugins WP, apps SaaS, webhooks
- Categorie WP : e-commerce, LMS, CRM, formulaires, membership, communaute
- Categorie SaaS : productivite, communication, paiement, email, projet, AI
- 3 solutions pour les services non supportes : webhooks, API App, App Builder

**Mots-cles SEO**
- OttoKit integrations
- OttoKit WooCommerce
- OttoKit TutorLMS
- OttoKit FluentCRM
- OttoKit Google Sheets

---

## Notes de production — Module 1

### Captures a preparer
- Dashboard OttoKit (app.ottokit.com) — vue globale
- Page integrations ottokit.com — scroll + recherche
- Page pricing ottokit.com — tableau des plans
- WordPress.org/plugins/suretriggers — fiche plugin
- Schema architecture : site WP ↔ plugin ↔ cloud OttoKit ↔ apps

### Environnement de demo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec WooCommerce + TutorLMS + FluentCRM installes

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 1.1 | 5 min |
| 1.2 | 6 min |
| 1.3 | 5 min |
| 1.4 | 5 min |
| 1.5 | 7 min |
| 1.6 | 7 min |
| **Total M1** | **35 min** |

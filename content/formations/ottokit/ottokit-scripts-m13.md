# Scripts video — Module 13 : Organisation : workspaces, templates et deploiement

**Formation** : Maitriser OttoKit
**Module** : M13 — Organisation : workspaces, templates et deploiement
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~45 min de video
**Date** : 2026-03-30

---

## Lecon 13.1 — Dossiers : organise tes workflows par projet/client

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit workflows

---

**[INTRO — face camera]**

Tu as 5 workflows, tout va bien. Tu en as 15, ca commence a devenir le bazar. Tu en as 30, tu ne retrouves plus rien. La solution : les dossiers. OttoKit te permet de ranger tes workflows comme des fichiers sur ton ordinateur. On met de l'ordre.

**[ECRAN — screencast OttoKit — page Workflows]**

[Montre la liste des workflows sans organisation — tous au meme niveau]

Voici une liste de workflows non organises. "Test email", "WooCommerce → CRM", "Formulaire contact v2", "Backup workflow"... Imagine en avoir 30 comme ca. Impossible de s'y retrouver rapidement.

**[ECRAN — screencast creation d'un dossier]**

[Clique sur le bouton "New Folder" ou "Create Folder"]
[Nomme le dossier "WooCommerce — Commandes"]
[Cree un second dossier "FluentCRM — Emails"]
[Cree un troisieme dossier "Interne — Tests"]

On cree trois dossiers. Le nommage est important : prefixe par l'app principale ou le client.

**[ECRAN — screencast organisation des workflows]**

[Selectionne des workflows]
[Deplace "WooCommerce → FluentCRM — Nouvelle commande" dans le dossier "WooCommerce — Commandes"]
[Deplace "Email bienvenue inscription" dans le dossier "FluentCRM — Emails"]
[Deplace "Test email v2" dans le dossier "Interne — Tests"]

Tu selectionnes un workflow et tu le glisses dans le bon dossier. En quelques minutes, 10 workflows sont ranges.

**[ECRAN — slide "Structure recommandee freelance"]**

Si tu geres plusieurs clients, voici une structure qui fonctionne :

```
📁 Client A — Boulangerie Martin
   📁 Commandes
   📁 Marketing
📁 Client B — Coach Julie
   📁 Inscriptions
   📁 Emails
📁 Interne — schoolsWP
   📁 Production
   📁 Tests
```

La regle : un dossier par client, un sous-dossier par type d'automatisation. Tu retrouves n'importe quel workflow en 2 clics.

**[TRANSITION — face camera]**

Les dossiers structurent visuellement. Mais le nommage, c'est ce qui rend la recherche rapide. On en parle dans la prochaine lecon.

---

**Points cles**
- Les dossiers evitent le chaos quand tu as plus de 10 workflows
- Un dossier par client ou par projet, un sous-dossier par type
- Nommer les dossiers avec un prefixe clair (client, app, categorie)
- Ranger immediatement chaque nouveau workflow — ne pas remettre a plus tard

**Mots-cles SEO**
- OttoKit organiser workflows
- dossiers OttoKit
- ranger automatisations WordPress
- OttoKit gestion workflows

---

## Lecon 13.2 — Convention de nommage : retrouve n'importe quel workflow

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides convention nommage

---

**[INTRO — face camera]**

Un workflow bien nomme, tu sais ce qu'il fait sans l'ouvrir. Un workflow mal nomme, tu dois l'ouvrir, lire chaque noeud, et perdre 2 minutes. Multiplier ca par 30 workflows, ca fait une heure de perdue. On fixe une convention et on s'y tient.

**[ECRAN — slide "La convention"]**

Voici la convention que j'utilise pour tous les workflows schoolsWP :

```
[Categorie] [Source] → [Cible] — [Action]
```

Exemples :
- `[VENTE] WooCommerce → FluentCRM — Ajout contact apres achat`
- `[LEAD] Gravity Forms → Google Sheets — Capture formulaire contact`
- `[EMAIL] FluentCRM → Client — Sequence bienvenue`
- `[INTERNE] Cron → Slack — Rapport hebdomadaire`
- `[TEST] WooCommerce → Email — Verification template`

**[ECRAN — slide "Les categories"]**

Les categories que je recommande :

| Prefixe | Usage |
|---|---|
| `[VENTE]` | Tout ce qui touche aux commandes, paiements, livraisons |
| `[LEAD]` | Capture de leads, formulaires, inscriptions |
| `[EMAIL]` | Sequences email, newsletters, relances |
| `[CRM]` | Synchronisation et gestion des contacts |
| `[INTERNE]` | Rapports, alertes, maintenance |
| `[TEST]` | Workflows en cours de developpement |

Tu peux adapter les categories a tes besoins. L'important, c'est la coherence.

**[ECRAN — screencast renommage de workflows]**

[Ouvre la liste des workflows]
[Renomme "Workflow 1" en "[VENTE] WooCommerce → FluentCRM — Ajout contact"]
[Renomme "Email truc" en "[EMAIL] FluentCRM → Client — Welcome sequence"]
[Renomme "Test 3" en "[TEST] Gravity Forms → Sheets — Verification mapping"]

On prend 3 workflows existants et on applique la convention. A chaque fois : categorie, source, cible, action.

**[ECRAN — slide "La recherche devient rapide"]**

Avec cette convention :

- Tu cherches tous les workflows de vente ? Tape "[VENTE]".
- Tu cherches tout ce qui touche FluentCRM ? Tape "FluentCRM".
- Tu cherches les tests a nettoyer ? Tape "[TEST]".

Le nommage transforme la recherche en quelque chose de previsible.

**[TRANSITION — face camera]**

Dossiers + nommage, c'est la base. Maintenant, on passe a l'echelle. Si tu travailles en equipe ou avec plusieurs entreprises, OttoKit a une fonctionnalite pour toi : les organisations.

---

**Points cles**
- Convention : [Categorie] [Source] → [Cible] — [Action]
- 6 categories recommandees : VENTE, LEAD, EMAIL, CRM, INTERNE, TEST
- Renommer immediatement, ne jamais laisser "Workflow 1" ou "Test"
- Un bon nommage rend la recherche instantanee

**Mots-cles SEO**
- OttoKit nommage workflow
- convention nommage automatisation
- organiser workflows WordPress
- nommer workflows OttoKit

---

## Lecon 13.3 — Organisations : gere plusieurs equipes ou entreprises

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit Organizations

---

**[INTRO — face camera]**

Si tu geres l'automatisation pour plusieurs entreprises — la tienne et celles de tes clients — tu ne veux pas tout melanger dans le meme compte. OttoKit propose les Organisations. Chaque organisation a ses propres workflows, ses propres connexions, et son propre forfait.

**[ECRAN — slide "Organisation = entreprise separee"]**

Une Organisation dans OttoKit, c'est comme un compte independant :

- Ses propres workflows
- Ses propres connexions (apps)
- Son propre compteur de tasks
- Ses propres membres et permissions

Le tout accessible depuis le meme compte OttoKit. Tu switches d'une organisation a l'autre sans te deconnecter.

**[ECRAN — screencast creation d'une organisation]**

[Clique sur le nom de l'organisation actuelle (en haut a gauche ou dans Settings)]
[Clique sur "Create Organization" ou "New Organization"]
[Nomme l'organisation "Client — Coach Julie"]
[Montre les champs : nom, description]
[Valide la creation]

Tu crees une nouvelle organisation en quelques clics. Donne-lui un nom clair — le nom du client ou du projet.

**[ECRAN — screencast switch entre organisations]**

[Montre le selecteur d'organisation]
[Switch vers "Client — Coach Julie"]
[Montre le dashboard vide — aucun workflow, aucune connexion]
[Switch de retour vers l'organisation principale]
[Montre les workflows existants]

Quand tu switches, tu changes completement de contexte. Les workflows de l'organisation A n'apparaissent pas dans l'organisation B. C'est totalement isole.

**[ECRAN — slide "Permissions par organisation"]**

Tu peux inviter des membres dans une organisation avec des roles differents :

- **Owner** : acces total, gestion du forfait
- **Admin** : cree et modifie les workflows, gere les connexions
- **Member** : voit et execute, mais ne modifie pas

Si tu travailles pour un client, tu peux l'inviter en tant que Member. Il voit ses workflows tourner, mais il ne peut pas casser ta configuration.

**[ECRAN — screencast invitation d'un membre]**

[Va dans Settings → Members de l'organisation]
[Clique sur "Invite Member"]
[Entre une adresse email]
[Selectionne le role "Member"]
[Envoie l'invitation]

L'invitation part par email. Le client cree son compte OttoKit (ou se connecte) et il accede directement a son organisation.

**[TRANSITION — face camera]**

Les organisations separent les entreprises. Mais a l'interieur d'une meme organisation, tu peux aller encore plus loin avec les workspaces. C'est ce qu'on voit maintenant.

---

**Points cles**
- Une organisation = un espace isole avec ses propres workflows, connexions et tasks
- Switch entre organisations sans deconnexion
- 3 roles : Owner, Admin, Member — permissions differenciees
- Ideal pour les freelances qui gerent plusieurs clients

**Mots-cles SEO**
- OttoKit organisation multi-clients
- OttoKit gestion equipe
- automatisation WordPress agence
- OttoKit permissions roles

---

## Lecon 13.4 — Workspaces : isole les workflows par client

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit Workspaces

---

**[INTRO — face camera]**

A l'interieur d'une organisation, les workspaces permettent de creer des compartiments. Chaque workspace a ses propres connexions et ses propres workflows. C'est utile quand tu geres plusieurs projets pour un meme client, ou quand tu veux separer production et test.

**[ECRAN — slide "Organisation vs Workspace"]**

| | Organisation | Workspace |
|---|---|---|
| Niveau | Entite principale | Sous-division |
| Forfait tasks | Propre forfait | Partage le forfait de l'org |
| Connexions | Propres connexions | Propres connexions |
| Workflows | Propres workflows | Propres workflows |
| Cas d'usage | Separer les clients | Separer les projets d'un meme client |

L'organisation, c'est le client. Le workspace, c'est le projet.

**[ECRAN — screencast creation d'un workspace]**

[Ouvre les settings de l'organisation]
[Va dans la section Workspaces]
[Clique sur "Create Workspace"]
[Nomme le workspace "Formations en ligne"]
[Cree un second workspace "E-commerce"]

On cree deux workspaces pour le client "Coach Julie" : un pour ses formations en ligne, un pour sa boutique e-commerce.

**[ECRAN — screencast configuration des connexions par workspace]**

[Ouvre le workspace "Formations en ligne"]
[Montre que les connexions sont vides]
[Ajoute une connexion TutorLMS]
[Ajoute une connexion FluentCRM]

Chaque workspace a ses propres connexions. Si le client a deux sites WordPress — un pour les formations, un pour la boutique — chaque workspace se connecte au bon site. Pas de risque de melange.

**[ECRAN — screencast workflows isoles]**

[Cree un workflow dans le workspace "Formations en ligne"]
[Switch vers le workspace "E-commerce"]
[Montre que le workflow n'apparait pas ici]

Les workflows sont isoles. Ce que tu crees dans un workspace n'existe pas dans l'autre. Tu travailles dans un environnement propre.

**[ECRAN — slide "Architecture recommandee freelance"]**

Voici l'architecture que je recommande pour un freelance WordPress :

```
Organisation "Mon agence"
├── Workspace "Client A — Site principal"
├── Workspace "Client A — Site staging"
├── Workspace "Client B — Boutique"
└── Workspace "Interne — Tests"

Organisation "Client C — Grande entreprise"
├── Workspace "Production"
├── Workspace "Marketing"
└── Workspace "Support"
```

Les petits clients → un workspace par client dans ton organisation. Les gros clients → une organisation dediee avec plusieurs workspaces.

**[TRANSITION — face camera]**

Ton espace est organise : dossiers, nommage, organisations, workspaces. Maintenant, on passe a l'efficacite : creer des templates reutilisables pour ne pas reconstruire les memes workflows a chaque fois.

---

**Points cles**
- Workspace = sous-division d'une organisation, avec ses propres connexions et workflows
- Organisation = le client ; Workspace = le projet
- Les connexions sont isolees par workspace — pas de risque de melange entre sites
- Architecture recommandee : petits clients en workspaces, gros clients en organisations

**Mots-cles SEO**
- OttoKit workspace
- OttoKit multi-site WordPress
- separer workflows par client OttoKit
- OttoKit workspace connexion

---

## Lecon 13.5 — Templates de workflow : cree tes propres modeles

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit export/import

---

**[INTRO — face camera]**

Tu as un workflow qui fonctionne parfaitement. Tu veux le reutiliser pour un autre client, un autre site, un autre projet. Plutot que de le reconstruire de zero, tu le transformes en template. C'est un modele reutilisable que tu deploies en quelques minutes.

**[ECRAN — slide "Qu'est-ce qu'un template"]**

Un template, c'est :

- La structure complete du workflow (trigger, actions, filtres, conditions)
- Les mappings de champs
- Les notes et la documentation

Ce que le template ne contient PAS :
- Les connexions (chaque site a les siennes)
- Les donnees (emails, noms, IDs specifiques)
- Les credentials

C'est logique : un template est generique. Les connexions et les donnees sont specifiques a chaque deploiement.

**[ECRAN — screencast duplication d'un workflow]**

[Ouvre un workflow existant — "WooCommerce → FluentCRM — Ajout contact"]
[Clique sur les options du workflow (menu 3 points)]
[Selectionne "Duplicate" ou "Clone"]
[Le workflow est duplique avec un nouveau nom]

Premiere methode : la duplication. Tu clones un workflow existant a l'interieur de la meme organisation. Les connexions sont conservees. C'est utile quand tu veux creer une variante.

**[ECRAN — screencast export d'un workflow]**

[Clique sur les options du workflow]
[Selectionne "Export"]
[Un fichier JSON est telecharge]
[Ouvre le fichier brievement pour montrer sa structure]

Deuxieme methode : l'export. Tu exportes le workflow en fichier JSON. Ce fichier contient toute la structure mais pas les connexions. Tu peux le partager, le stocker, le versionner.

**[ECRAN — screencast creation d'un template "Onboarding client"]**

[Ouvre un workflow complet d'onboarding : inscription → email bienvenue → ajout CRM → notification Slack]
[Exporte le workflow]
[Renomme le fichier "template-onboarding-client.json"]

On cree un template "Onboarding client". C'est un workflow classique : quand un client s'inscrit, il recoit un email de bienvenue, son contact est ajoute dans le CRM, et l'equipe recoit une notification.

**[ECRAN — slide "Documenter son template"]**

Pour qu'un template soit reutilisable, il faut le documenter :

1. **Nom** : "[TEMPLATE] Onboarding client standard"
2. **Description** : Ce que le workflow fait, etape par etape
3. **Prerequis** : Quelles apps doivent etre connectees (WooCommerce, FluentCRM, Slack)
4. **Champs a configurer** : Quels champs doivent etre adaptes a chaque deploiement
5. **Variables** : Quelles valeurs changent (nom du produit, adresse email d'equipe)

Un template sans documentation, c'est un puzzle sans image de reference.

**[TRANSITION — face camera]**

Tu as ton template. Dans la prochaine lecon, on le deploie chez un client. Export, import, configuration, test — le processus complet.

---

**Points cles**
- Un template = structure du workflow sans les connexions ni les donnees
- Deux methodes : duplication (meme organisation) ou export JSON (transferable)
- Toujours documenter le template : nom, description, prerequis, champs a configurer
- Un template bien documente se deploie en 10 minutes au lieu de 2 heures

**Mots-cles SEO**
- OttoKit template workflow
- creer modele OttoKit
- exporter workflow OttoKit
- template automatisation WordPress

---

## Lecon 13.6 — Deployer un workflow chez un client

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit import et configuration

---

**[INTRO — face camera]**

Tu as un template pret. Un client a besoin de la meme automatisation. Tu vas deployer le workflow chez lui en 4 etapes : import, connexion, configuration, test. Voyons ca en pratique.

**[ECRAN — slide "Les 4 etapes du deploiement"]**

1. **Import** — Charge le template dans l'organisation ou le workspace du client
2. **Connexion** — Branche les apps du client (son WordPress, son CRM, son email)
3. **Configuration** — Adapte les champs specifiques (noms, emails, IDs)
4. **Test** — Verifie que tout fonctionne avant d'activer

**[ECRAN — screencast import du template]**

[Ouvre OttoKit dans l'organisation ou le workspace du client]
[Clique sur "Import Workflow" ou "Create from Template"]
[Selectionne le fichier JSON "template-onboarding-client.json"]
[Le workflow apparait dans la liste avec les noeuds]

L'import charge la structure complete. Tu retrouves le trigger, les actions, les filtres, les conditions. Tout est la, mais les connexions sont vides.

**[ECRAN — screencast branchement des connexions]**

[Ouvre le workflow importe]
[Clique sur le trigger — le champ "Connection" est vide]
[Selectionne la connexion WordPress du client dans le dropdown]
[Passe a l'action suivante — selectionne la connexion FluentCRM du client]
[Continue avec chaque noeud]

Etape 2 : tu branches les connexions du client. Chaque noeud a besoin de sa connexion. Si les apps du client sont deja connectees dans OttoKit, tu les selectionnes dans le dropdown. Sinon, tu ajoutes les connexions d'abord.

**[ECRAN — screencast adaptation des champs]**

[Ouvre l'action "Envoyer un email"]
[Modifie le contenu de l'email avec le nom du client, son logo, son URL]
[Ouvre l'action "Notification Slack"]
[Change le canal Slack vers celui du client]

Etape 3 : tu adaptes les champs specifiques. Le template avait "schoolsWP" dans l'email de bienvenue ? Tu remplaces par le nom de la marque du client. Le canal Slack pointait vers le tien ? Tu le changes.

**[ECRAN — screencast test du workflow deploye]**

[Clique sur "Fetch Data" sur le trigger pour verifier la connexion]
[Active le workflow]
[Cree une inscription de test sur le site du client]
[Revient dans History — montre le run de test avec statut "Success"]
[Parcourt les etapes : trigger OK, email envoie OK, CRM OK, Slack OK]

Etape 4 : tu testes. Fetch Data sur le trigger pour verifier la connexion. Puis tu crees un evenement de test. Tu verifies dans l'History que chaque etape s'execute correctement.

**[ECRAN — slide "Checklist de deploiement"]**

Avant de declarer le deploiement termine :

- [ ] Toutes les connexions sont branchees et testees
- [ ] Les champs specifiques au client sont adaptes (nom, email, URL)
- [ ] Un run de test complet est passe en "Success"
- [ ] Le workflow est renomme avec la convention du client
- [ ] Le workflow est range dans le bon dossier
- [ ] Le client est informe que l'automatisation est active

**[TRANSITION — face camera]**

Le workflow est deploye et fonctionne. Derniere chose : si le client ne doit pas voir OttoKit dans son back-office WordPress, on peut le cacher. C'est ce qu'on voit maintenant.

---

**Points cles**
- 4 etapes : import, connexion, configuration, test
- Les connexions sont toujours vides apres import — a brancher manuellement
- Adapter chaque champ specifique au client (nom, email, URL, canal)
- Toujours tester avec un run complet avant de declarer le deploiement termine

**Mots-cles SEO**
- deployer workflow OttoKit client
- OttoKit import workflow
- installer automatisation client WordPress
- OttoKit deploiement template

---

## Lecon 13.7 — Cacher OttoKit dans le WP admin du client

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin

---

**[INTRO — face camera]**

Tu as deploye un workflow chez un client. Il fonctionne. Mais le client voit le menu OttoKit dans son admin WordPress. Il pose des questions, il clique, il touche a la configuration. Pas ideal. OttoKit permet de masquer le plugin cote admin. Le workflow continue de tourner en arriere-plan.

**[ECRAN — screencast WordPress admin — avant]**

[Montre le back-office WordPress du client]
[Pointe le menu "OttoKit" ou "SureTriggers" dans la barre laterale]
[Montre que le client pourrait cliquer dessus et voir les reglages]

Voici ce que le client voit. Le menu OttoKit est visible. S'il clique, il voit les parametres de connexion, les logs locaux, peut-etre meme un bouton de deconnexion. Ce n'est pas ce que tu veux.

**[ECRAN — screencast reglages OttoKit dans WordPress]**

[Va dans les reglages du plugin OttoKit dans WordPress]
[Montre l'option "Hide menu for non-admins" ou equivalent]
[Active l'option]

Dans les reglages du plugin OttoKit sur WordPress, il y a une option pour masquer le menu. Active-la. Le menu disparait pour tous les utilisateurs qui ne sont pas administrateurs.

**[ECRAN — screencast gestion des roles]**

[Montre la gestion des utilisateurs WordPress]
[Pointe le role du client : "Editor" ou "Shop Manager"]

Si ton client a un role "Editor" ou "Shop Manager", il ne verra plus le menu OttoKit. Seuls les comptes administrateurs y ont acces. C'est pour ca qu'il est important de ne pas donner le role "Administrator" au client si tu veux garder le controle.

**[ECRAN — slide "Strategie d'acces recommandee"]**

Voici ce que je recommande :

| Qui | Role WordPress | Voit OttoKit | Acces plateforme cloud |
|---|---|---|---|
| Toi (freelance) | Administrator | Oui | Oui (Owner/Admin) |
| Le client | Editor / Shop Manager | Non | Optionnel (Member) |
| Un collaborateur | Author | Non | Non |

Le client gere son contenu et ses commandes. Toi, tu geres l'automatisation. Chacun son perimetre.

**[ECRAN — screencast WordPress admin — apres]**

[Montre le back-office WordPress en etant connecte avec le compte du client (role Editor)]
[Le menu OttoKit n'apparait plus dans la barre laterale]
[Le client voit ses pages, ses produits, ses commandes — pas OttoKit]

Resultat : le client travaille normalement. Pas de menu OttoKit, pas de confusion. Les workflows tournent en arriere-plan sans aucune intervention de sa part.

**[ECRAN — slide "Le plugin reste actif"]**

Point important : cacher le menu ne desactive pas le plugin. Le plugin OttoKit reste actif et fonctionnel. Il continue de communiquer avec la plateforme cloud. Les triggers se declenchent normalement. Tu as juste retire la visibilite cote interface.

Si tu dois intervenir, tu te connectes avec ton compte administrateur.

**[TRANSITION — face camera]**

Ton espace est organise, tes templates sont prets, tes deploiements sont propres, et le client ne voit que ce qu'il a besoin de voir. On valide tout ca dans le quiz final de ce module.

---

**Points cles**
- OttoKit peut etre masque dans le back-office WordPress
- Le plugin reste actif et fonctionnel meme quand le menu est cache
- Donner le role Editor ou Shop Manager au client, pas Administrator
- Separation claire : le client gere son contenu, tu geres l'automatisation

**Mots-cles SEO**
- cacher OttoKit WordPress admin
- OttoKit masquer menu client
- OttoKit white label WordPress
- gestion roles OttoKit client

---

## Lecon 13.8 — Quiz M13

**Duree** : 5 min
**Type** : Quiz
**Note production** : Quiz interactif — pas de script video. Questions generees dans le LMS.

---

# Notes de production — Module 13

**Angle schoolsWP** : Organisation pour freelance WordPress qui gere plusieurs clients. Template "stack schoolsWP" pre-configure (onboarding → CRM → email → notification). Deploiement sur site client avec OttoKit masque.

**Assets necessaires** :
- Compte OttoKit avec 10+ workflows a organiser (non ranges au debut)
- 2 organisations configurees (organisation principale + organisation client)
- 2 workspaces dans une organisation (production + test)
- Fichier JSON template "onboarding-client" pret pour import
- Site WordPress client avec compte Editor pour demo masquage

**Enchainement des lecons** :
- 13.1 → 13.2 : dossiers puis nommage (organisation visuelle puis textuelle)
- 13.2 → 13.3 : du nommage aux organisations (passer a l'echelle)
- 13.3 → 13.4 : organisations puis workspaces (macro vers micro)
- 13.4 → 13.5 : des workspaces aux templates (de l'organisation a la reutilisation)
- 13.5 → 13.6 : du template au deploiement (de la creation a l'utilisation)
- 13.6 → 13.7 : du deploiement au masquage (finition professionnelle)

**Workflows montres dans le module** :
1. 10+ workflows non organises (avant/apres rangement)
2. Template "Onboarding client" (inscription → email → CRM → Slack)
3. Deploiement du template sur un compte client

**Template "stack schoolsWP" pre-configure** :
Le template de reference inclut :
- Trigger : WooCommerce "Order Completed" (instantane)
- Action 1 : FluentCRM — Ajouter contact + tag "client"
- Action 2 : FluentCRM — Demarrer sequence email bienvenue
- Action 3 : Google Sheets — Ajouter ligne dans le tracker ventes
- Action 4 : Slack — Notification canal #ventes
- Filtre : Exclure commandes montant = 0

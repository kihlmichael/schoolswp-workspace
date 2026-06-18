# Scripts vidéo - Module 13 : Organisation : workspaces, templates et déploiement

**Formation** : Maîtriser OttoKit
**Module** : M13 - Organisation : workspaces, templates et déploiement
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~45 min de vidéo
**Date** : 2026-03-30

---

## Leçon 13.1 - Dossiers : organise tes workflows par projet/client

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit workflows

---

**[INTRO - face caméra]**

Tu as 5 workflows, tout va bien. Tu en as 15, ça commence à devenir le bazar. Tu en as 30, tu ne retrouves plus rien. La solution : les dossiers. OttoKit te permet de ranger tes workflows comme des fichiers sur ton ordinateur. On met de l'ordre.

**[ÉCRAN - screencast OttoKit - page Workflows]**

[Montre la liste des workflows sans organisation - tous au même niveau]

Voici une liste de workflows non organisés. "Test email", "WooCommerce → CRM", "Formulaire contact v2", "Backup workflow"... Imagine en avoir 30 comme ça. Impossible de s'y retrouver rapidement.

**[ÉCRAN - screencast création d'un dossier]**

[Clique sur le bouton "New Folder" ou "Create Folder"]
[Nomme le dossier "WooCommerce - Commandes"]
[Crée un second dossier "FluentCRM - Emails"]
[Crée un troisième dossier "Interne - Tests"]

On crée trois dossiers. Le nommage est important : préfixe par l'app principale ou le client.

**[ÉCRAN - screencast organisation des workflows]**

[Sélectionne des workflows]
[Déplace "WooCommerce → FluentCRM - Nouvelle commande" dans le dossier "WooCommerce - Commandes"]
[Déplace "Email bienvenue inscription" dans le dossier "FluentCRM - Emails"]
[Déplace "Test email v2" dans le dossier "Interne - Tests"]

Tu sélectionnes un workflow et tu le glisses dans le bon dossier. En quelques minutes, 10 workflows sont rangés.

**[ÉCRAN - slide "Structure recommandee freelance"]**

Si tu gères plusieurs clients, voici une structure qui fonctionne :

```
📁 Client A - Boulangerie Martin
   📁 Commandes
   📁 Marketing
📁 Client B - Coach Julie
   📁 Inscriptions
   📁 Emails
📁 Interne - schoolsWP
   📁 Production
   📁 Tests
```

La règle : un dossier par client, un sous-dossier par type d'automatisation. Tu retrouves n'importe quel workflow en 2 clics.

**[TRANSITION - face caméra]**

Les dossiers structurent visuellement. Mais le nommage, c'est ce qui rend la recherche rapide. On en parle dans la prochaine leçon.

---

**Points clés**
- Les dossiers évitent le chaos quand tu as plus de 10 workflows
- Un dossier par client ou par projet, un sous-dossier par type
- Nommer les dossiers avec un préfixe clair (client, app, catégorie)
- Ranger immédiatement chaque nouveau workflow - ne pas remettre à plus tard

**Mots-clés SEO**
- OttoKit organiser workflows
- dossiers OttoKit
- ranger automatisations WordPress
- OttoKit gestion workflows

---

## Leçon 13.2 - Convention de nommage : retrouve n'importe quel workflow

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides convention nommage

---

**[INTRO - face caméra]**

Un workflow bien nommé, tu sais ce qu'il fait sans l'ouvrir. Un workflow mal nommé, tu dois l'ouvrir, lire chaque nœud, et perdre 2 minutes. Multiplier ça par 30 workflows, ça fait une heure de perdue. On fixe une convention et on s'y tient.

**[ÉCRAN - slide "La convention"]**

Voici la convention que j'utilise pour tous les workflows schoolsWP :

```
[Categorie] [Source] → [Cible] - [Action]
```

Exemples :
- `[VENTE] WooCommerce → FluentCRM - Ajout contact après achat`
- `[LEAD] Gravity Forms → Google Sheets - Capture formulaire contact`
- `[EMAIL] FluentCRM → Client - Séquence bienvenue`
- `[INTERNE] Cron → Slack - Rapport hebdomadaire`
- `[TEST] WooCommerce → Email - Vérification template`

**[ÉCRAN - slide "Les catégories"]**

Les catégories que je recommande :

| Préfixe | Usage |
|---|---|
| `[VENTE]` | Tout ce qui touche aux commandes, paiements, livraisons |
| `[LEAD]` | Capture de leads, formulaires, inscriptions |
| `[EMAIL]` | Séquences email, newsletters, relances |
| `[CRM]` | Synchronisation et gestion des contacts |
| `[INTERNE]` | Rapports, alertes, maintenance |
| `[TEST]` | Workflows en cours de développement |

Tu peux adapter les catégories à tes besoins. L'important, c'est la cohérence.

**[ÉCRAN - screencast renommage de workflows]**

[Ouvre la liste des workflows]
[Renomme "Workflow 1" en "[VENTE] WooCommerce → FluentCRM - Ajout contact"]
[Renomme "Email truc" en "[EMAIL] FluentCRM → Client - Welcome sequence"]
[Renomme "Test 3" en "[TEST] Gravity Forms → Sheets - Vérification mapping"]

On prend 3 workflows existants et on applique la convention. À chaque fois : catégorie, source, cible, action.

**[ÉCRAN - slide "La recherche devient rapide"]**

Avec cette convention :

- Tu cherches tous les workflows de vente ? Tape "[VENTE]".
- Tu cherches tout ce qui touche FluentCRM ? Tape "FluentCRM".
- Tu cherches les tests à nettoyer ? Tape "[TEST]".

Le nommage transforme la recherche en quelque chose de prévisible.

**[TRANSITION - face caméra]**

Dossiers + nommage, c'est la base. Maintenant, on passe à l'échelle. Si tu travailles en équipe ou avec plusieurs entreprises, OttoKit a une fonctionnalité pour toi : les organisations.

---

**Points clés**
- Convention : [Catégorie] [Source] → [Cible] - [Action]
- 6 catégories recommandées : VENTE, LEAD, EMAIL, CRM, INTERNE, TEST
- Renommer immédiatement, ne jamais laisser "Workflow 1" ou "Test"
- Un bon nommage rend la recherche instantanée

**Mots-clés SEO**
- OttoKit nommage workflow
- convention nommage automatisation
- organiser workflows WordPress
- nommer workflows OttoKit

---

## Leçon 13.3 - Organisations : gère plusieurs équipes ou entreprises

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit Organizations

---

**[INTRO - face caméra]**

Si tu gères l'automatisation pour plusieurs entreprises - la tienne et celles de tes clients - tu ne veux pas tout mélanger dans le même compte. OttoKit propose les Organisations. Chaque organisation a ses propres workflows, ses propres connexions, et son propre forfait.

**[ÉCRAN - slide "Organisation = entreprise séparée"]**

Une Organisation dans OttoKit, c'est comme un compte indépendant :

- Ses propres workflows
- Ses propres connexions (apps)
- Son propre compteur de tasks
- Ses propres membres et permissions

Le tout accessible depuis le même compte OttoKit. Tu switches d'une organisation à l'autre sans te déconnecter.

**[ÉCRAN - screencast création d'une organisation]**

[Clique sur le nom de l'organisation actuelle (en haut à gauche ou dans Settings)]
[Clique sur "Create Organization" ou "New Organization"]
[Nomme l'organisation "Client - Coach Julie"]
[Montre les champs : nom, description]
[Valide la création]

Tu crées une nouvelle organisation en quelques clics. Donne-lui un nom clair - le nom du client ou du projet.

**[ÉCRAN - screencast switch entre organisations]**

[Montre le sélecteur d'organisation]
[Switch vers "Client - Coach Julie"]
[Montre le dashboard vide - aucun workflow, aucune connexion]
[Switch de retour vers l'organisation principale]
[Montre les workflows existants]

Quand tu switches, tu changes complètement de contexte. Les workflows de l'organisation A n'apparaissent pas dans l'organisation B. C'est totalement isolé.

**[ÉCRAN - slide "Permissions par organisation"]**

Tu peux inviter des membres dans une organisation avec des rôles différents :

- **Owner** : accès total, gestion du forfait
- **Admin** : crée et modifie les workflows, gère les connexions
- **Member** : voit et exécute, mais ne modifie pas

Si tu travailles pour un client, tu peux l'inviter en tant que Member. Il voit ses workflows tourner, mais il ne peut pas casser ta configuration.

**[ÉCRAN - screencast invitation d'un membre]**

[Va dans Settings → Members de l'organisation]
[Clique sur "Invite Member"]
[Entre une adresse email]
[Sélectionne le rôle "Member"]
[Envoie l'invitation]

L'invitation part par email. Le client crée son compte OttoKit (ou se connecte) et il accède directement à son organisation.

**[TRANSITION - face caméra]**

Les organisations séparent les entreprises. Mais à l'intérieur d'une même organisation, tu peux aller encore plus loin avec les workspaces. C'est ce qu'on voit maintenant.

---

**Points clés**
- Une organisation = un espace isolé avec ses propres workflows, connexions et tasks
- Switch entre organisations sans déconnexion
- 3 rôles : Owner, Admin, Member - permissions différenciées
- Idéal pour les freelances qui gèrent plusieurs clients

**Mots-clés SEO**
- OttoKit organisation multi-clients
- OttoKit gestion équipe
- automatisation WordPress agence
- OttoKit permissions rôles

---

## Leçon 13.4 - Workspaces : isole les workflows par client

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit Workspaces

---

**[INTRO - face caméra]**

À l'intérieur d'une organisation, les workspaces permettent de créer des compartiments. Chaque workspace a ses propres connexions et ses propres workflows. C'est utile quand tu gères plusieurs projets pour un même client, ou quand tu veux séparer production et test.

**[ÉCRAN - slide "Organisation vs Workspace"]**

| | Organisation | Workspace |
|---|---|---|
| Niveau | Entité principale | Sous-division |
| Forfait tasks | Propre forfait | Partage le forfait de l'org |
| Connexions | Propres connexions | Propres connexions |
| Workflows | Propres workflows | Propres workflows |
| Cas d'usage | Séparer les clients | Séparer les projets d'un même client |

L'organisation, c'est le client. Le workspace, c'est le projet.

**[ÉCRAN - screencast creation d'un workspace]**

[Ouvre les settings de l'organisation]
[Va dans la section Workspaces]
[Clique sur "Create Workspace"]
[Nomme le workspace "Formations en ligne"]
[Crée un second workspace "E-commerce"]

On crée deux workspaces pour le client "Coach Julie" : un pour ses formations en ligne, un pour sa boutique e-commerce.

**[ÉCRAN - screencast configuration des connexions par workspace]**

[Ouvre le workspace "Formations en ligne"]
[Montre que les connexions sont vides]
[Ajoute une connexion TutorLMS]
[Ajoute une connexion FluentCRM]

Chaque workspace a ses propres connexions. Si le client a deux sites WordPress - un pour les formations, un pour la boutique - chaque workspace se connecte au bon site. Pas de risque de mélange.

**[ÉCRAN - screencast workflows isolés]**

[Crée un workflow dans le workspace "Formations en ligne"]
[Switch vers le workspace "E-commerce"]
[Montre que le workflow n'apparaît pas ici]

Les workflows sont isolés. Ce que tu crées dans un workspace n'existe pas dans l'autre. Tu travailles dans un environnement propre.

**[ÉCRAN - slide "Architecture recommandee freelance"]**

Voici l'architecture que je recommande pour un freelance WordPress :

```
Organisation "Mon agence"
├── Workspace "Client A - Site principal"
├── Workspace "Client A - Site staging"
├── Workspace "Client B - Boutique"
└── Workspace "Interne - Tests"

Organisation "Client C - Grande entreprise"
├── Workspace "Production"
├── Workspace "Marketing"
└── Workspace "Support"
```

Les petits clients → un workspace par client dans ton organisation. Les gros clients → une organisation dédiée avec plusieurs workspaces.

**[TRANSITION - face caméra]**

Ton espace est organisé : dossiers, nommage, organisations, workspaces. Maintenant, on passe à l'efficacité : créer des templates réutilisables pour ne pas reconstruire les mêmes workflows à chaque fois.

---

**Points clés**
- Workspace = sous-division d'une organisation, avec ses propres connexions et workflows
- Organisation = le client ; Workspace = le projet
- Les connexions sont isolées par workspace - pas de risque de mélange entre sites
- Architecture recommandée : petits clients en workspaces, gros clients en organisations

**Mots-clés SEO**
- OttoKit workspace
- OttoKit multi-site WordPress
- séparer workflows par client OttoKit
- OttoKit workspace connexion

---

## Leçon 13.5 - Templates de workflow : crée tes propres modèles

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit export/import

---

**[INTRO - face caméra]**

Tu as un workflow qui fonctionne parfaitement. Tu veux le réutiliser pour un autre client, un autre site, un autre projet. Plutôt que de le reconstruire de zéro, tu le transformes en template. C'est un modèle réutilisable que tu déploies en quelques minutes.

**[ÉCRAN - slide "Qu'est-ce qu'un template"]**

Un template, c'est :

- La structure complète du workflow (trigger, actions, filtres, conditions)
- Les mappings de champs
- Les notes et la documentation

Ce que le template ne contient PAS :
- Les connexions (chaque site a les siennes)
- Les données (emails, noms, IDs spécifiques)
- Les credentials

C'est logique : un template est générique. Les connexions et les données sont spécifiques à chaque déploiement.

**[ÉCRAN - screencast duplication d'un workflow]**

[Ouvre un workflow existant - "WooCommerce → FluentCRM - Ajout contact"]
[Clique sur les options du workflow (menu 3 points)]
[Sélectionne "Duplicate" ou "Clone"]
[Le workflow est dupliqué avec un nouveau nom]

Première méthode : la duplication. Tu clones un workflow existant à l'intérieur de la même organisation. Les connexions sont conservées. C'est utile quand tu veux créer une variante.

**[ÉCRAN - screencast export d'un workflow]**

[Clique sur les options du workflow]
[Sélectionne "Export"]
[Un fichier JSON est téléchargé]
[Ouvre le fichier brièvement pour montrer sa structure]

Deuxième méthode : l'export. Tu exportes le workflow en fichier JSON. Ce fichier contient toute la structure mais pas les connexions. Tu peux le partager, le stocker, le versionner.

**[ÉCRAN - screencast creation d'un template "Onboarding client"]**

[Ouvre un workflow complet d'onboarding : inscription → email bienvenue → ajout CRM → notification Slack]
[Exporte le workflow]
[Renomme le fichier "template-onboarding-client.json"]

On crée un template "Onboarding client". C'est un workflow classique : quand un client s'inscrit, il reçoit un email de bienvenue, son contact est ajouté dans le CRM, et l'équipe reçoit une notification.

**[ÉCRAN - slide "Documenter son template"]**

Pour qu'un template soit réutilisable, il faut le documenter :

1. **Nom** : "[TEMPLATE] Onboarding client standard"
2. **Description** : Ce que le workflow fait, étape par étape
3. **Prérequis** : Quelles apps doivent être connectées (WooCommerce, FluentCRM, Slack)
4. **Champs à configurer** : Quels champs doivent être adaptés à chaque déploiement
5. **Variables** : Quelles valeurs changent (nom du produit, adresse email d'équipe)

Un template sans documentation, c'est un puzzle sans image de référence.

**[TRANSITION - face caméra]**

Tu as ton template. Dans la prochaine leçon, on le déploie chez un client. Export, import, configuration, test - le processus complet.

---

**Points clés**
- Un template = structure du workflow sans les connexions ni les données
- Deux méthodes : duplication (même organisation) ou export JSON (transférable)
- Toujours documenter le template : nom, description, prérequis, champs à configurer
- Un template bien documenté se déploie en 10 minutes au lieu de 2 heures

**Mots-clés SEO**
- OttoKit template workflow
- créer modèle OttoKit
- exporter workflow OttoKit
- template automatisation WordPress

---

## Leçon 13.6 - Déployer un workflow chez un client

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit import et configuration

---

**[INTRO - face caméra]**

Tu as un template prêt. Un client a besoin de la même automatisation. Tu vas déployer le workflow chez lui en 4 étapes : import, connexion, configuration, test. Voyons ça en pratique.

**[ÉCRAN - slide "Les 4 étapes du déploiement"]**

1. **Import** - Charge le template dans l'organisation ou le workspace du client
2. **Connexion** - Branche les apps du client (son WordPress, son CRM, son email)
3. **Configuration** - Adapte les champs spécifiques (noms, emails, IDs)
4. **Test** - Vérifie que tout fonctionne avant d'activer

**[ÉCRAN - screencast import du template]**

[Ouvre OttoKit dans l'organisation ou le workspace du client]
[Clique sur "Import Workflow" ou "Create from Template"]
[Sélectionne le fichier JSON "template-onboarding-client.json"]
[Le workflow apparaît dans la liste avec les nœuds]

L'import charge la structure complète. Tu retrouves le trigger, les actions, les filtres, les conditions. Tout est là, mais les connexions sont vides.

**[ÉCRAN - screencast branchement des connexions]**

[Ouvre le workflow importe]
[Clique sur le trigger - le champ "Connection" est vide]
[Sélectionne la connexion WordPress du client dans le dropdown]
[Passe à l'action suivante - sélectionne la connexion FluentCRM du client]
[Continue avec chaque nœud]

Étape 2 : tu branches les connexions du client. Chaque nœud a besoin de sa connexion. Si les apps du client sont déjà connectées dans OttoKit, tu les sélectionnes dans le dropdown. Sinon, tu ajoutes les connexions d'abord.

**[ÉCRAN - screencast adaptation des champs]**

[Ouvre l'action "Envoyer un email"]
[Modifie le contenu de l'email avec le nom du client, son logo, son URL]
[Ouvre l'action "Notification Slack"]
[Change le canal Slack vers celui du client]

Étape 3 : tu adaptes les champs spécifiques. Le template avait "schoolsWP" dans l'email de bienvenue ? Tu remplaces par le nom de la marque du client. Le canal Slack pointait vers le tien ? Tu le changes.

**[ÉCRAN - screencast test du workflow deploye]**

[Clique sur "Fetch Data" sur le trigger pour vérifier la connexion]
[Active le workflow]
[Crée une inscription de test sur le site du client]
[Revient dans History - montre le run de test avec statut "Success"]
[Parcourt les étapes : trigger OK, email envoyé OK, CRM OK, Slack OK]

Étape 4 : tu testes. Fetch Data sur le trigger pour vérifier la connexion. Puis tu crées un événement de test. Tu vérifies dans l'History que chaque étape s'exécute correctement.

**[ÉCRAN - slide "Checklist de déploiement"]**

Avant de déclarer le déploiement terminé :

- [ ] Toutes les connexions sont branchées et testées
- [ ] Les champs spécifiques au client sont adaptés (nom, email, URL)
- [ ] Un run de test complet est passé en "Success"
- [ ] Le workflow est renommé avec la convention du client
- [ ] Le workflow est rangé dans le bon dossier
- [ ] Le client est informé que l'automatisation est active

**[TRANSITION - face caméra]**

Le workflow est déployé et fonctionne. Dernière chose : si le client ne doit pas voir OttoKit dans son back-office WordPress, on peut le cacher. C'est ce qu'on voit maintenant.

---

**Points clés**
- 4 étapes : import, connexion, configuration, test
- Les connexions sont toujours vides après import - à brancher manuellement
- Adapter chaque champ spécifique au client (nom, email, URL, canal)
- Toujours tester avec un run complet avant de déclarer le déploiement terminé

**Mots-clés SEO**
- déployer workflow OttoKit client
- OttoKit import workflow
- installer automatisation client WordPress
- OttoKit déploiement template

---

## Leçon 13.7 - Cacher OttoKit dans le WP admin du client

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin

---

**[INTRO - face caméra]**

Tu as déployé un workflow chez un client. Il fonctionne. Mais le client voit le menu OttoKit dans son admin WordPress. Il pose des questions, il clique, il touche à la configuration. Pas idéal. OttoKit permet de masquer le plugin côté admin. Le workflow continue de tourner en arrière-plan.

**[ÉCRAN - screencast WordPress admin - avant]**

[Montre le back-office WordPress du client]
[Pointe le menu "OttoKit" ou "SureTriggers" dans la barre latérale]
[Montre que le client pourrait cliquer dessus et voir les réglages]

Voici ce que le client voit. Le menu OttoKit est visible. S'il clique, il voit les paramètres de connexion, les logs locaux, peut-être même un bouton de déconnexion. Ce n'est pas ce que tu veux.

**[ÉCRAN - screencast réglages OttoKit dans WordPress]**

[Va dans les réglages du plugin OttoKit dans WordPress]
[Montre l'option "Hide menu for non-admins" ou équivalent]
[Active l'option]

Dans les réglages du plugin OttoKit sur WordPress, il y a une option pour masquer le menu. Active-la. Le menu disparaît pour tous les utilisateurs qui ne sont pas administrateurs.

**[ÉCRAN - screencast gestion des rôles]**

[Montre la gestion des utilisateurs WordPress]
[Pointe le rôle du client : "Editor" ou "Shop Manager"]

Si ton client a un rôle "Editor" ou "Shop Manager", il ne verra plus le menu OttoKit. Seuls les comptes administrateurs y ont accès. C'est pour ça qu'il est important de ne pas donner le rôle "Administrator" au client si tu veux garder le contrôle.

**[ÉCRAN - slide "Stratégie d'accès recommandée"]**

Voici ce que je recommande :

| Qui | Rôle WordPress | Voit OttoKit | Accès plateforme cloud |
|---|---|---|---|
| Toi (freelance) | Administrator | Oui | Oui (Owner/Admin) |
| Le client | Editor / Shop Manager | Non | Optionnel (Member) |
| Un collaborateur | Author | Non | Non |

Le client gère son contenu et ses commandes. Toi, tu gères l'automatisation. Chacun son périmètre.

**[ÉCRAN - screencast WordPress admin - après]**

[Montre le back-office WordPress en étant connecté avec le compte du client (rôle Editor)]
[Le menu OttoKit n'apparaît plus dans la barre latérale]
[Le client voit ses pages, ses produits, ses commandes - pas OttoKit]

Résultat : le client travaille normalement. Pas de menu OttoKit, pas de confusion. Les workflows tournent en arrière-plan sans aucune intervention de sa part.

**[ÉCRAN - slide "Le plugin reste actif"]**

Point important : cacher le menu ne désactive pas le plugin. Le plugin OttoKit reste actif et fonctionnel. Il continue de communiquer avec la plateforme cloud. Les triggers se déclenchent normalement. Tu as juste retiré la visibilité côté interface.

Si tu dois intervenir, tu te connectes avec ton compte administrateur.

**[TRANSITION - face caméra]**

Ton espace est organisé, tes templates sont prêts, tes déploiements sont propres, et le client ne voit que ce qu'il a besoin de voir. On valide tout ça dans le quiz final de ce module.

---

**Points clés**
- OttoKit peut être masqué dans le back-office WordPress
- Le plugin reste actif et fonctionnel même quand le menu est caché
- Donner le rôle Editor ou Shop Manager au client, pas Administrator
- Séparation claire : le client gère son contenu, tu gères l'automatisation

**Mots-clés SEO**
- cacher OttoKit WordPress admin
- OttoKit masquer menu client
- OttoKit white label WordPress
- gestion rôles OttoKit client

---

## Leçon 13.8 - Quiz M13

**Durée** : 5 min
**Type** : Quiz
**Note production** : Quiz interactif - pas de script vidéo. Questions générées dans le LMS.

---

# Notes de production - Module 13

**Angle schoolsWP** : Organisation pour freelance WordPress qui gère plusieurs clients. Template "stack schoolsWP" pré-configuré (onboarding → CRM → email → notification). Déploiement sur site client avec OttoKit masqué.

**Assets nécessaires** :
- Compte OttoKit avec 10+ workflows à organiser (non rangés au début)
- 2 organisations configurées (organisation principale + organisation client)
- 2 workspaces dans une organisation (production + test)
- Fichier JSON template "onboarding-client" prêt pour import
- Site WordPress client avec compte Editor pour démo masquage

**Enchaînement des leçons** :
- 13.1 → 13.2 : dossiers puis nommage (organisation visuelle puis textuelle)
- 13.2 → 13.3 : du nommage aux organisations (passer à l'échelle)
- 13.3 → 13.4 : organisations puis workspaces (macro vers micro)
- 13.4 → 13.5 : des workspaces aux templates (de l'organisation à la réutilisation)
- 13.5 → 13.6 : du template au déploiement (de la création à l'utilisation)
- 13.6 → 13.7 : du déploiement au masquage (finition professionnelle)

**Workflows montrés dans le module** :
1. 10+ workflows non organisés (avant/après rangement)
2. Template "Onboarding client" (inscription → email → CRM → Slack)
3. Déploiement du template sur un compte client

**Template "stack schoolsWP" pré-configuré** :
Le template de référence inclut :
- Trigger : WooCommerce "Order Completed" (instantané)
- Action 1 : FluentCRM - Ajouter contact + tag "client"
- Action 2 : FluentCRM - Démarrer séquence email bienvenue
- Action 3 : Google Sheets - Ajouter ligne dans le tracker ventes
- Action 4 : Slack - Notification canal #ventes
- Filtre : Exclure commandes montant = 0

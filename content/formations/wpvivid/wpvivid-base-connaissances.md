# WPvivid Backup & Migration : base de connaissances formation

## À propos de ce document

Ce document est le **matériau source interne** d'une future formation schoolsWP sur le plugin WordPress **WPvivid Backup & Migration**. Ce n'est pas du contenu marketing publié : c'est une synthèse pédagogique structurée, destinée à servir de socle de référence pour bâtir des modules de cours, des tutoriels ou des supports.

- **Date de constitution** : 2026-05-20
- **Objet** : sauvegarde, restauration, migration et préproduction (staging) de sites WordPress avec WPvivid
- **Public visé par la future formation** : propriétaires de sites WordPress, freelances, agences

Tout au long du document, les fonctionnalités sont marquées **(Free)** quand elles existent dans la version gratuite et **(Pro)** quand elles sont réservées à la version payante.

### Sources utilisées

1. **Documentation officielle** docs.wpvivid.com : pages de découverte, sauvegarde, restauration, planification, stockage distant, migration, staging, sécurité/avancé et dépannage (récupérées et synthétisées, pas copiées).
2. **Site officiel** wpvivid.com : page d'accueil et page de comparaison free-vs-pro (positionnement, Free vs Pro, formules tarifaires).
3. **Vidéos YouTube non officielles** : sélection de tutoriels tiers identifiés via recherche web (liste complète en fin de document).

### Avertissement de fiabilité

La synthèse s'appuie strictement sur les pages récupérées. Quelques limites rencontrées sont signalées explicitement (voir la fin de chaque module concerné et la note de clôture). Les **tarifs précis** ne sont pas détaillés sur les pages publiques consultées : seules les formules (abonnement / à vie, garantie 30 jours) sont confirmées. Aucune fonctionnalité n'a été inventée.

---

## Module 1 : Découverte de WPvivid

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Expliquer ce qu'est WPvivid et les trois problèmes qu'il résout.
- Décrire le fonctionnement interne du plugin (collecte, paquet, stockage, restauration).
- Distinguer clairement ce que couvre la version gratuite et la version Pro.
- Installer le plugin gratuit puis activer une licence Pro.

### Contenu

**Qu'est-ce que WPvivid ?**

WPvivid Backup & Migration est une extension WordPress qui permet de **sauvegarder, restaurer et migrer** un site WordPress. Elle s'adresse aux propriétaires de sites, aux freelances et aux agences qui ont besoin d'une solution fiable pour protéger leurs données et déplacer leurs sites.

Le plugin répond à trois besoins concrets :

1. Disposer d'une sauvegarde fiable, notamment avant une mise à jour.
2. Déplacer un site WordPress d'un serveur ou d'un domaine à un autre sans manipulation hasardeuse.
3. Éviter les risques des migrations manuelles (export/import de base de données, transfert de fichiers via FTP).

Le site officiel revendique plus de **900 000 installations actives**, environ 16 millions de téléchargements cumulés et plus de 30 000 clients de la version payante. WPvivid met en avant un mode d'apprentissage intégré (Learning Mode) censé adapter automatiquement le comportement du plugin aux limites du serveur, y compris en hébergement mutualisé.

**Comment fonctionne WPvivid : le cycle en 4 étapes**

1. **Collecte des données** : le plugin rassemble les fichiers WordPress (cœur, thèmes, extensions, dossier des uploads, contenus personnalisés) et la base de données, en tenant compte des exclusions définies par l'utilisateur.
2. **Création du paquet** : les données sont compressées et organisées en une archive de sauvegarde structurée. Ce paquet est l'élément central de toutes les opérations.
3. **Stockage ou transfert** : le paquet peut être conservé en local sur le serveur, envoyé vers un stockage distant (cloud), ou transféré directement vers un autre site WordPress dans le cadre d'une migration.
4. **Restauration ou déploiement** : à la restauration, WPvivid extrait les fichiers, importe la base de données et remplace les données existantes selon l'action choisie.

Architecture interne (cinq composants) : un moteur de sauvegarde (coordination), un gestionnaire de base de données (export/import), un gestionnaire de système de fichiers, des connecteurs de stockage (qui unifient les destinations) et un moteur de restauration.

**Version Free vs version Pro**

Inclus dans la version **gratuite** :

- Sauvegarde des fichiers WordPress et de la base de données.
- Sauvegarde manuelle et planification simple (avec règles de rétention basiques).
- Migration de site (téléchargement/upload de l'archive, et auto-migration directe site-à-site).
- Stockage cloud de base : Dropbox, Google Drive, Amazon S3, OneDrive, FTP/sFTP.
- Restauration en 1 clic.
- Création de sites de staging (duplication ou installation WordPress vierge).
- Prise en charge du multisite en sous-répertoires.

Ajouté par la version **Pro** :

- Sauvegarde **incrémentale** et sélection granulaire du contenu (tables, dossiers, exclusions par extension).
- Migration automatisée site-à-site avec protection anti-crash, et migration via stockage distant.
- Environnements de staging multiples et déploiement bidirectionnel (staging vers live).
- **Rollback** : sauvegarde automatique avant chaque mise à jour.
- Gestion des **rôles et capacités** utilisateurs.
- **Marque blanche** (White Label).
- Plannings de sauvegarde multiples et avancés.
- Stockage cloud étendu : Wasabi, pCloud, Backblaze, WebDAV, NextCloud, stockage compatible S3.
- **Chiffrement** de la base de données, **snapshots** de base de données, **fusion de base de données** (Database Merging).
- Support technique prioritaire.

**Tarification** : le site officiel propose des formules par **abonnement** et des formules **à vie**, avec une **garantie de remboursement de 30 jours**. Les montants précis et le nombre de sites couverts par formule ne figurent pas sur les pages consultées : à vérifier directement sur la page de tarification de wpvivid.com avant tout support de formation chiffré.

**Installation du plugin**

Version gratuite (Free) : dans le tableau de bord WordPress, aller dans Extensions puis Ajouter, rechercher « WPvivid Backup », installer puis activer. Sur un multisite, passer par l'administration réseau.

Version Pro : la Pro se distribue sous forme de package séparé.

1. Se connecter à son compte sur wpvivid.com, section Téléchargements, et récupérer le fichier ZIP de l'installateur Pro.
2. Dans WordPress : Extensions puis Ajouter puis Téléverser une extension, sélectionner le ZIP, installer, activer.
3. Aller dans l'onglet License du menu WPvivid, saisir la clé de licence et cliquer sur « Activer ». La version gratuite s'installe automatiquement si elle est absente.
4. Dans la section Addons & Tools, installer les modules Pro souhaités (Staging, Rollback, etc.).

### Points de vigilance

- WPvivid Pro fonctionne comme un **socle modulaire** : activer la licence ne suffit pas, il faut ensuite installer les modules complémentaires (Rollback, Staging, Roles & Capabilities, etc.) depuis Addons & Tools.
- Sur un **multisite**, toute installation se fait au niveau de l'administration réseau, jamais sur un sous-site.
- Ne pas confondre WPvivid « Backup & Migration » (le plugin principal) avec ses modules additionnels Pro : ce sont des extensions distinctes installées par-dessus.

### Liens doc officielle

- Présentation : https://docs.wpvivid.com/wpvivid-backup-migration.html
- Fonctionnement : https://docs.wpvivid.com/wpvivid-works.html
- Installation : https://docs.wpvivid.com/install-wpvivid-plugins.html
- Free vs Pro : https://wpvivid.com/free-vs-pro
- Site officiel : https://wpvivid.com/

### Vidéos YouTube

- « WPvivid Backup and Restore Installation and getting started » : https://www.youtube.com/watch?v=k1SeyQnFwwk
- « WPvivid Backup, Staging and Migration Plugin - The All-in-One Solution! » : https://www.youtube.com/watch?v=Dl9G9b6ztto

---

## Module 2 : Sauvegarde

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Créer une sauvegarde manuelle en choisissant son contenu et sa destination.
- Distinguer les trois types de sauvegarde (complète, base de données, fichiers).
- Utiliser les options Pro de sélection granulaire (tables, exclusions de fichiers).
- Comprendre la sauvegarde de base de données personnalisée et le dossier de sauvegarde personnalisé.

### Contenu

**Ce qu'une sauvegarde inclut**

Une sauvegarde WPvivid peut couvrir : la base de données WordPress, le dossier des uploads, les thèmes, les extensions, les fichiers du cœur WordPress et les contenus personnalisés.

**Les trois types de sauvegarde (Free et Pro)**

- **Sauvegarde complète** : base de données + fichiers WordPress (option recommandée par défaut).
- **Sauvegarde de base de données seule** : uniquement les données (articles, pages, réglages, utilisateurs).
- **Sauvegarde de fichiers seuls** : les fichiers WordPress sans la base de données.

**Créer une sauvegarde manuelle (Free)**

1. Choisir le contenu : « Base de données + Fichiers WordPress », « Fichiers WordPress uniquement » ou « Base de données seule ».
2. Choisir la destination : stockage local (sur le serveur, dans le répertoire WPvivid) ou stockage distant (un service cloud préalablement configuré).
3. Option facultative : empêcher la suppression automatique de cette sauvegarde par les règles de rétention.
4. Cliquer sur « Backup Now ». L'interface affiche la progression (pourcentage, volume traité, vitesse).
5. Une fois terminée, la sauvegarde apparaît dans la liste, prête à être téléchargée ou restaurée.

**Créer une sauvegarde manuelle (Pro) : sélection avancée**

La Pro ajoute un contrôle fin sur ce qui est inclus :

- **Base de données** : tables WordPress standard, tables créées par les extensions et thèmes, tables avec préfixes différents, et même des bases de données externes additionnelles.
- **Fichiers et dossiers** : cœur WordPress, dossier wp-content, thèmes, extensions, uploads, et fichiers/dossiers non-WordPress (en dehors de l'installation).
- **Paramètres avancés** : exclure des fichiers ou dossiers précis de wp-content, exclure certains types de fichiers (mp4, zip, etc.), ajouter une note descriptive, et verrouiller la sauvegarde contre la suppression automatique.

**Sauvegarde de base de données personnalisée (Pro)**

Permet de ne sauvegarder que certaines tables plutôt que toute la base. WPvivid classe les tables en trois groupes : tables WordPress par défaut (recommandé pour la plupart des sites), autres tables (générées par extensions et thèmes, à exclure avec prudence), tables à préfixes différents. L'accès se fait via la section « Backup Content » puis « Custom content ».

**Dossier de sauvegarde personnalisé (Pro)**

Permet d'organiser les sauvegardes dans le stockage cloud avec une arborescence propre : un dossier parent (par défaut « wpvividbackuppro ») et un sous-dossier par site (par défaut basé sur le domaine, ex. « www_yourdomain_com »). Cela évite les écrasements quand plusieurs sites partagent le même compte cloud. Configuration via WPvivid puis Cloud Storage, à la connexion initiale ou via l'icône d'édition d'un stockage existant.

### Points de vigilance

- La sauvegarde **complète** (base + fichiers) est l'option par défaut conseillée : une sauvegarde de fichiers seuls ou de base seule ne permet pas de restaurer un site entier.
- Avec la Pro, exclure des « autres tables » ou des dossiers peut **désactiver des fonctionnalités** au moment de la restauration : à manier avec précaution.
- Une sauvegarde stockée **uniquement en local** ne protège pas contre une panne serveur (voir Module 5).
- Sur un compte cloud partagé entre plusieurs sites, configurer un dossier personnalisé est indispensable pour ne pas mélanger les sauvegardes.

### Liens doc officielle

- Vue d'ensemble sauvegarde (Free) : https://docs.wpvivid.com/backup-overview-free.html
- Sauvegarde manuelle (Free) : https://docs.wpvivid.com/create-a-manual-backup-free.html
- Vue d'ensemble sauvegarde (Pro) : https://docs.wpvivid.com/backup-overview-pro.html
- Sauvegarde manuelle (Pro) : https://docs.wpvivid.com/manual-backup-pro.html
- Sauvegarde de base de données personnalisée (Pro) : https://docs.wpvivid.com/custom-database-backup-pro.html
- Dossier de sauvegarde personnalisé (Pro) : https://docs.wpvivid.com/custom-backup-folder-pro.html

### Vidéos YouTube

- « Amazing FREE Backup and Restore Plugin - Migration and Staging - WPVivid » : https://www.youtube.com/watch?v=BU0OP6QrQMw
- « WPvivid Backup Plugin Tutorial 2025 | WordPress Free » : https://www.youtube.com/watch?v=1emJCk9y3G4
- « Comment faire une sauvegarde et restauration avec WPvivid » (français) : https://www.youtube.com/watch?v=GtqLMvgVnRw

---

## Module 3 : Restauration et Rollback

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Restaurer un site WordPress depuis une sauvegarde locale ou cloud.
- Restaurer sélectivement certains composants avec la version Pro.
- Mettre en place le Rollback (sauvegarde automatique avant mise à jour) et annuler une mise à jour problématique.

### Contenu

**Restaurer un site depuis une sauvegarde (Free)**

La restauration **remplace** le site actuel par les données sauvegardées (fichiers et base de données). Toute modification postérieure à la sauvegarde sera définitivement perdue.

1. Aller dans WPvivid Backup Plugin puis Backup & Restore et consulter la liste des sauvegardes.
2. Sélectionner la sauvegarde voulue et ouvrir l'interface de restauration.
3. Si la sauvegarde est sur un stockage distant (Google Drive, Dropbox, Amazon S3), la rapatrier d'abord sur le serveur.
4. Confirmer la restauration dans la fenêtre de dialogue.
5. Surveiller la barre de progression et les logs sans fermer le navigateur.
6. Un message de succès confirme la fin. Vérifier ensuite le site.

**Restaurer avec WPvivid Pro : restauration sélective**

La Pro permet de choisir précisément les composants à restaurer : thèmes, extensions, wp-content, uploads, fichiers du cœur WordPress, base de données.

- Depuis le serveur local : pour les sauvegardes marquées « Localhost », cliquer sur l'icône de restauration, ajuster les paramètres avancés, sélectionner les composants, puis « Restore Now ».
- Depuis le cloud : pour les sauvegardes sur Google Drive, Dropbox ou Amazon S3, utiliser « Retrieve to Localhost » afin de télécharger le fichier sur le serveur avant de restaurer.
- Paramètres avancés disponibles : nettoyer les anciens fichiers avant restauration, vider la base de données avant restauration.

**Rollback : sauvegarde automatique avant mise à jour (Pro)**

Le Rollback crée automatiquement une copie de sécurité **juste avant** chaque mise à jour de WordPress, d'une extension ou d'un thème. Au lieu de sauvegarder tout le site, WPvivid identifie uniquement les fichiers en cours de modification et les place dans un dossier dédié : restauration rapide, faible consommation d'espace disque.

Activation : WPvivid Plugin puis Rollback, puis activer « Auto Backup before Update » pour les éléments voulus (Extensions, Thèmes, Cœur WordPress). On peut aussi inclure la base de données et un stockage cloud.

Annuler une mise à jour : aller dans WPvivid puis Rollback, ouvrir « View Versioning Backups », cliquer sur « Rollback » et attendre la confirmation.

### Points de vigilance

- Une restauration est **destructive** : elle écrase l'état actuel. Toujours prévenir le client/l'équipe et idéalement créer une sauvegarde de l'état courant avant de restaurer.
- Pour une sauvegarde stockée dans le cloud, **rapatrier l'archive sur le serveur** est une étape obligatoire avant restauration.
- **Ne jamais fermer le navigateur** pendant une restauration : l'opération peut rester incomplète.
- Le Rollback est une fonction **Pro uniquement**. Il ne remplace pas une vraie sauvegarde complète : c'est un filet de sécurité ciblé sur les mises à jour.
- En cas d'échec de restauration, restaurer sur une **installation WordPress vierge** maximise les chances de succès (voir Module 9).

### Liens doc officielle

- Restaurer un site (Free) : https://docs.wpvivid.com/restore-site-from-a-backup-free.html
- Restaurer une sauvegarde (Pro) : https://docs.wpvivid.com/restore-a-backup-pro.html
- Rollback / sauvegarde auto avant mise à jour : https://docs.wpvivid.com/rollback-auto-backup-before-update.html

### Vidéos YouTube

- « Restauration et migration facile du site internet avec WPvivid backup » (français) : https://www.youtube.com/watch?v=BMeK5xUrS2s
- « Comment faire une sauvegarde et restauration avec WPvivid » (français) : https://www.youtube.com/watch?v=GtqLMvgVnRw

---

## Module 4 : Planification et rétention

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Mettre en place des sauvegardes planifiées automatiques.
- Comprendre la différence entre sauvegarde complète planifiée et sauvegarde incrémentale.
- Configurer une politique de rétention pour ne pas saturer le stockage.

### Contenu

**Planification en version gratuite (Free)**

WPvivid exécute les sauvegardes en arrière-plan selon un calendrier prédéfini, sans intervention manuelle. Fréquences disponibles : toutes les 12 heures, quotidienne, hebdomadaire, bihebdomadaire, mensuelle. On choisit le contenu (base seule, fichiers seuls, ou complet) et la destination (local ou cloud).

Limitation importante : la planification repose sur **WordPress Cron**, qui se déclenche à la visite des pages. Sur un site à faible trafic, les sauvegardes peuvent se déclencher avec un léger décalage par rapport à l'heure prévue.

**Planification en version Pro**

La Pro offre un moteur de planification plus souple : intervalles toutes les 1, 2, 4, 8 ou 12 heures, quotidien ou hebdomadaire, avec **heure d'exécution précise** (utile pour viser les heures creuses). Elle autorise plusieurs plannings combinés avec des configurations différentes, l'envoi simultané vers plusieurs destinations cloud (redondance) et la sélection personnalisée du contenu.

**Sauvegarde incrémentale (Pro)**

La sauvegarde incrémentale ne capture que les fichiers modifiés, ajoutés ou supprimés depuis la dernière sauvegarde. Une sauvegarde complète sert de « base », puis les sauvegardes incrémentales s'y rattachent en chaîne. Bénéfices : temps d'exécution, espace disque et charge serveur fortement réduits.

Cas d'usage idéaux : sites volumineux (plus de 5 Go), sites fréquemment mis à jour (e-commerce, blogs actifs), bande passante limitée, besoin de sauvegardes très fréquentes.

Configuration : WPvivid puis onglet Incremental Backup, cliquer sur « Edit » pour régler la fréquence, choisir les destinations, exclure les dossiers inutiles (cache, fichiers temporaires), puis « Enable ».

Point technique clé : **la base de données n'est jamais sauvegardée de façon incrémentale**, elle est toujours sauvegardée intégralement.

**Configurer un planning général (Pro)**

WPvivid Backup Pro puis Backup Schedule puis onglet General Backup. Cliquer sur l'icône Modifier ou créer une nouvelle tâche : choisir la fréquence, l'heure exacte, la destination, le contenu, les exclusions, un commentaire facultatif, puis « Update Schedule ». Activer ensuite le planning via l'interrupteur On/Off et vérifier que le statut indique « Enabled » avec l'heure de la prochaine sauvegarde.

**Politique de rétention**

La rétention détermine combien de copies sont conservées. Une fois la limite atteinte, WPvivid supprime automatiquement la plus ancienne sauvegarde.

- **Stockage local** : limites distinctes pour les sauvegardes manuelles, les sauvegardes planifiées générales et les sauvegardes incrémentales.
- **Stockage cloud** : la rétention se règle au niveau de chaque connexion de stockage (à la création ou via l'icône d'édition).
- **Verrouillage** : une sauvegarde précise peut être verrouillée pour échapper à la suppression automatique.

### Points de vigilance

- Sur un site à **faible trafic**, le déclenchement réel d'une sauvegarde planifiée peut être décalé : la cause est WordPress Cron, pas un bug de WPvivid. Une solution serveur (vrai cron système) peut fiabiliser le timing.
- Les sauvegardes générales **ne peuvent pas s'exécuter en même temps** que les sauvegardes incrémentales : désactiver les plannings incrémentaux avant de lancer un planning général si nécessaire.
- La planification, la sauvegarde incrémentale et la rétention granulaire avancée sont essentiellement des fonctions **Pro**. La version Free propose une planification simple avec rétention basique.
- Sans politique de rétention, les sauvegardes s'accumulent et saturent le serveur ou le compte cloud.
- Verrouiller au moins une sauvegarde « connue bonne » évite de la perdre lors d'une rotation automatique.

### Liens doc officielle

- Vue d'ensemble planification (Free) : https://docs.wpvivid.com/overview-schedule-free.html
- Vue d'ensemble planification (Pro) : https://docs.wpvivid.com/schedule-overview.html
- Mettre en place les sauvegardes incrémentales : https://docs.wpvivid.com/set-up-incremental-backups.html
- Configurer les plannings généraux : https://docs.wpvivid.com/set-up-general-backup-schedules.html
- Rétention des sauvegardes : https://docs.wpvivid.com/backup-retention.html

### Vidéos YouTube

- « WPvivid Backup Plugin Tutorial 2025 | WordPress Free » : https://www.youtube.com/watch?v=1emJCk9y3G4
- « WordPress Migration & Backup Made Easy: Complete WPvivid Tutorial » : https://www.youtube.com/watch?v=uHrJbg5WIFk

---

## Module 5 : Stockage distant

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Expliquer pourquoi le stockage hors site (off-site) est vital.
- Citer les destinations de stockage distant disponibles et lesquelles sont Free ou Pro.
- Connecter Google Drive, Dropbox et Amazon S3 comme destinations.

### Contenu

**Pourquoi le stockage distant est vital**

Une sauvegarde conservée uniquement sur le serveur du site disparaît avec ce serveur en cas de panne matérielle, de piratage ou de problème d'hébergement. La règle de base : conserver **au moins une copie hors site**, dans le cloud, en plus de toute sauvegarde locale. C'est le principe de la sauvegarde off-site, fondement d'une stratégie de sauvegarde sérieuse.

**Les destinations de stockage distant**

Destinations disponibles en version **gratuite (Free)** : Google Drive, Dropbox, Microsoft OneDrive, Amazon S3, DigitalOcean Spaces, FTP/sFTP.

L'ensemble des destinations supportées par WPvivid (la version **Pro** étend la liste, notamment Wasabi, pCloud, Backblaze, WebDAV, NextCloud et le stockage compatible S3) :

1. **Google Drive** : stockage cloud grand public (Free).
2. **Dropbox** : stockage cloud grand public (Free).
3. **Microsoft OneDrive** : stockage cloud grand public (Free).
4. **Amazon S3** : stockage objet d'Amazon Web Services (Free).
5. **DigitalOcean Spaces** : stockage objet compatible S3 de DigitalOcean (Free).
6. **FTP / FTP2 / sFTP** : transfert vers un serveur via protocole FTP ou FTP sécurisé (Free).
7. **Wasabi** : stockage cloud objet économique compatible S3 (Pro).
8. **pCloud** : stockage cloud grand public (Pro).
9. **Backblaze B2** : stockage cloud objet économique (Pro).
10. **WebDAV** : protocole de stockage standard, utilisé par de nombreux serveurs (Pro).
11. **NextCloud** : solution de stockage auto-hébergée open source (Pro).
12. **Stockage compatible S3** : tout fournisseur exposant une API compatible S3 (Pro).
13. **OneDrive Shared Drive / variantes professionnelles** : variantes professionnelles de OneDrive (Pro).

Note : la documentation officielle parle d'environ 13 à 14 destinations selon la façon de compter les variantes (FTP / FTP2 / sFTP, OneDrive grand public et professionnel). L'idée à retenir : un large éventail, du cloud grand public au stockage d'entreprise et aux protocoles serveur.

**Fonctionnalités clés du stockage distant**

- Plusieurs comptes de stockage distant peuvent être connectés simultanément, pour de la redondance.
- Gestion centralisée via WPvivid puis Cloud Storage (ajout, édition, suppression).
- Un stockage peut être défini comme destination par défaut des sauvegardes planifiées.
- Supprimer une connexion cloud dans WPvivid **n'efface pas** les sauvegardes déjà présentes dans le cloud.

**Connecter Google Drive**

1. WPvivid Plugin puis Cloud Storage, sélectionner Google Drive.
2. Cliquer sur le bouton d'authentification : redirection vers la page d'autorisation Google.
3. Renseigner : un alias unique (ex. « Google-Drive-Business »), un dossier parent personnalisé (ex. « wpvividbackuppro »), un sous-dossier par site, la taille de bloc de téléchargement (laisser par défaut), la rétention, et l'option « stockage par défaut » si souhaité.
4. Cliquer sur « Add Now ».

**Connecter Dropbox**

1. WPvivid puis Cloud Storage, sélectionner Dropbox.
2. Cliquer sur « Authenticate with Dropbox », autoriser via « Allow ».
3. Renseigner : alias unique, nom du dossier personnalisé, rétention, option « par défaut ».
4. Cliquer sur « Add Now ». Les sauvegardes suivent alors une arborescence structurée, par exemple « App://Wpvivid backup restore/site_a_com/ ».

**Connecter Amazon S3**

Informations nécessaires au préalable : une Access Key et une Secret Key AWS, et le nom exact du bucket S3.

1. WPvivid puis Cloud Storage, sélectionner Amazon S3.
2. Renseigner : un alias unique, les identifiants AWS (Access Key et Secret Key), le nom du bucket, un dossier parent commun (ex. « wpvividbackuppro ») et un sous-dossier par site.
3. Configurer la rétention et, si besoin, le chiffrement côté serveur.
4. Valider avec « Test and Add ». L'arborescence obtenue ressemble à « bucket-name/wpvividbackuppro/website_a_com/ ».

### Points de vigilance

- Une stratégie de sauvegarde **sans copie off-site** est incomplète : insister là-dessus en formation.
- Quand plusieurs sites partagent un même compte cloud, configurer un **dossier parent + sous-dossier par site** est indispensable pour éviter les écrasements.
- Les **identifiants Amazon S3** (Secret Key) sont des secrets sensibles : ne jamais les exposer dans une capture d'écran de formation.
- Supprimer une connexion cloud dans WPvivid ne supprime pas les fichiers déjà dans le cloud : un nettoyage manuel côté fournisseur reste à faire si nécessaire.
- Pour S3, la documentation consultée ne détaille pas explicitement le champ « région » : se référer à la console AWS et au formulaire WPvivid au moment de la configuration.

### Liens doc officielle

- Vue d'ensemble stockage distant (Free) : https://docs.wpvivid.com/overview-remote-storage-free.html
- Vue d'ensemble stockage distant (Pro) : https://docs.wpvivid.com/remote-storage-overview-pro.html
- Google Drive : https://docs.wpvivid.com/remote-storage-google-drive-pro.html
- Dropbox : https://docs.wpvivid.com/remote-storage-dropbox-pro.html
- Amazon S3 : https://docs.wpvivid.com/remote-storage-amazon-s3-pro.html

### Vidéos YouTube

- « How to Migrate A WordPress Website to Any Destination Using WPvivid Backup Plugin For Free? » : https://www.youtube.com/watch?v=_VIoBxC7fFU
- « Free WordPress Backup and Migration with WPVivid (#NoCode) » : https://www.youtube.com/watch?v=8lQifvQJ6Xc

---

## Module 6 : Migration

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Choisir le bon mode de migration selon le contexte (local, cloud, directe).
- Migrer un site via une archive téléchargée puis réimportée.
- Migrer un site via le stockage distant.
- Réaliser une auto-migration directe site-à-site avec une clé de migration.
- Comprendre les fonctions Import Site et Export Site.

### Contenu

**Ce qui se migre**

Une migration WPvivid transfère l'ensemble du site : base de données, fichiers du cœur WordPress, contenus, thèmes, extensions et uploads. On peut aussi migrer sélectivement (fichiers seuls ou base seule).

**Prérequis communs**

WPvivid doit être installé sur le site source ET sur le site destination. La migration fonctionne au mieux vers une **installation WordPress fraîche** côté destination.

**Mode 1 : migration via stockage local (Free)**

Approche manuelle via une archive, la plus résiliente sur les hébergements restreints.

1. Sur le site source : WPvivid puis Export Site puis onglet Export to Localhost, générer une sauvegarde complète, puis télécharger l'archive sur son ordinateur (tous les fichiers si l'archive est fragmentée).
2. Sur le site destination : WPvivid puis Import Site puis onglet Import from Localhost (Web Server), téléverser les fichiers. Alternative : déposer les fichiers par FTP dans le répertoire wp-content/wpvividbackups.
3. Cliquer sur « Restore Now » : WPvivid dépaquette et applique la base de données et les fichiers.
4. Après restauration, rafraîchir les permaliens dans Réglages puis Permaliens.

**Mode 2 : migration via stockage distant (Pro)**

Prérequis : WPvivid Pro sur les deux sites, un compte cloud configuré sur chacun, et un espace disque suffisant (au moins 2x la taille du site source).

1. Site source : connecter le stockage cloud (WPvivid puis Cloud Storage).
2. Export Site puis Export to Remote Storage, choisir le compte cloud, lancer l'export. WPvivid empaquette et téléverse directement la sauvegarde.
3. Vérifier que les fichiers apparaissent bien dans le stockage distant.
4. Site destination : connecter le même compte cloud.
5. Import Site puis Import from Remote Storage, actualiser, puis restaurer.
6. Surveiller la restauration sans fermer la page, puis valider le site (pages, extensions, médias, formulaires).

**Mode 3 : migration directe site-à-site / Auto Migration**

L'auto-migration établit une connexion directe entre deux installations WordPress, sans archive intermédiaire. C'est la méthode la plus rapide. Point notable : l'**auto-migration est disponible en version gratuite (Free)**.

Prérequis : WPvivid sur les deux sites, deux sites accessibles en ligne, pare-feu autorisant les connexions entrantes et sortantes, espace disque d'au moins 2x la taille du site source.

1. Sur le site destination : WPvivid puis Import Site, générer une clé de migration sécurisée et la copier.
2. Sur le site source : WPvivid puis Export Site puis Export to Target Site (Auto Migration), coller la clé.
3. Choisir le contenu (fichiers + base de données recommandé).
4. Cliquer sur « Export Now » (ou « Clone then Transfer ») pour lancer le transfert direct.
5. Surveiller la progression (pourcentage, fichiers traités, temps estimé).
6. Sur le site destination : Import Site puis Import from Auto Migration, restaurer les données reçues.
7. Surveiller la restauration sans fermer la page.
8. Vérifier le résultat (accueil, extensions, images, fonctions critiques).

Recommandation officielle avant une auto-migration : désactiver temporairement les redirections 301, les pare-feu, les plugins de sécurité et de cache.

**Import Site et Export Site**

- **Export Site** : empaquette le site en vue d'une migration, d'une distribution de sauvegarde ou d'une restauration. Trois destinations : Localhost (ZIP téléchargeable), stockage distant (cloud), site cible (auto-migration via clé). Contenu sélectionnable : fichiers + base, base seule, fichiers seuls, contenu personnalisé.
- **Import Site** : intègre une sauvegarde externe à la liste des sauvegardes locales pour la gérer ou la restaurer. Trois sources : Localhost (glisser-déposer ou sélection de fichiers), stockage distant, auto-migration (clé de site). Les sauvegardes importées sont ensuite traitées comme des sauvegardes locales.

### Points de vigilance

- Toujours migrer vers une **installation WordPress vierge** quand c'est possible : cela évite les conflits.
- Pour l'auto-migration et la migration via cloud, prévoir un **espace disque d'au moins 2x la taille du site source**.
- Avant une auto-migration, désactiver temporairement redirections 301, pare-feu, sécurité et cache : ces éléments bloquent souvent la connexion entre serveurs.
- Si l'archive est **fragmentée** en plusieurs fichiers, les télécharger TOUS, sinon la restauration échoue.
- Après migration, **rafraîchir les permaliens** (et parfois vider le cache des constructeurs de pages) pour éviter les erreurs 404.
- La migration via stockage distant est une fonction **Pro** ; la migration via archive locale et l'auto-migration directe sont disponibles en **Free**.

### Liens doc officielle

- Vue d'ensemble migration (Free) : https://docs.wpvivid.com/overview-migration-free.html
- Vue d'ensemble migration (Pro) : https://docs.wpvivid.com/migration-overview-pro.html
- Migration via local : https://docs.wpvivid.com/migrate-a-wordpress-site-via-local.html
- Migration via stockage distant : https://docs.wpvivid.com/migrate-a-wordpress-site-via-remote-storage.html
- Migration directe : https://docs.wpvivid.com/migrate-a-wordpress-site-directly.html
- Import Site : https://docs.wpvivid.com/import-site-overview.html
- Export Site : https://docs.wpvivid.com/export-site-overview.html
- Auto Migration : https://docs.wpvivid.com/overview-auto-migration.html

### Vidéos YouTube

- « WordPress Migration & Backup Made Easy: Complete WPvivid Tutorial » : https://www.youtube.com/watch?v=uHrJbg5WIFk
- « How to Migrate A WordPress Website to Any Destination Using WPvivid Backup Plugin For Free? » : https://www.youtube.com/watch?v=_VIoBxC7fFU
- « Faire une sauvegarde et migrer son site avec WPVivid Backup » (français) : https://www.youtube.com/watch?v=hpV8M3iDWe0
- « Migrez votre site web avec l'outil de migration automatique de WP Vivid » (français) : https://www.youtube.com/watch?v=mJZmHIWL1as

---

## Module 7 : Staging (préproduction)

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Expliquer l'intérêt d'un site de staging et ce que WPvivid permet en Free vs Pro.
- Créer un site de staging (duplication du live ou WordPress vierge).
- Publier un site de staging vers la production.
- Mettre à jour (resynchroniser) un site de staging depuis le live.
- Régler les paramètres de staging.

### Contenu

**Qu'est-ce que le staging**

Un site de staging est un environnement de **préproduction** : une copie du site, isolée, où l'on teste des mises à jour, des modifications de design ou de nouvelles extensions sans aucun risque pour le site en production.

**Staging en version gratuite (Free)**

La version Free permet trois actions :

1. Afficher et gérer les sites de staging existants.
2. Dupliquer le site en production pour expérimenter sans risque (choix du répertoire et de la configuration de base de données).
3. Créer une installation WordPress vierge indépendante (idéal pour tester un thème ou une extension de zéro).

Options : répertoire d'installation, base de données partagée (simple) ou isolée (avancé), copie sélective du contenu, préconfiguration des thèmes et extensions.

**Staging en version Pro**

La Pro ajoute notamment la création de staging en un clic (copie exacte du site live), des options de copie sélective (base, thèmes, extensions, médias), un environnement isolé avec sa propre URL, et surtout le **déploiement bidirectionnel** : pousser le staging vers le live, et resynchroniser le staging depuis le live.

**Créer un site de staging**

1. WPvivid Plugin puis onglet Staging Sites, cliquer sur le bouton de création.
2. Définir l'emplacement : un nom de dossier (ex. « staging01 ») pour une installation en sous-dossier, ou un sous-domaine existant avec son chemin serveur absolu.
3. Choisir la base de données : option recommandée, partager la base existante avec un préfixe distinct (« wpstg_ ») ; ou isolement total avec une base séparée.
4. Sélectionner les données à copier : désélectionner les tables inutiles, exclure les dossiers volumineux (uploads, anciens backups) pour gagner de l'espace.
5. Cliquer sur « Create Now » sans fermer l'onglet. Les identifiants de connexion sont identiques au site principal, et l'indexation par les moteurs de recherche est automatiquement désactivée.

**Publier un site de staging vers la production**

1. Sur le tableau de bord du site en production : WPvivid Plugin puis Staging Sites, repérer le site de staging à publier.
2. Choisir le contenu à publier : tout (base + fichiers, remplace entièrement la production), dossier uploads + base de données (synchronise les contenus récents), ou contenu personnalisé.
3. Régler les paramètres avancés : inclure/exclure des tables, exclure les fichiers volumineux, synchroniser la médiathèque.
4. Cliquer sur « Copy Now » sans fermer le navigateur.

**Mettre à jour un site de staging**

WPvivid Plugin puis onglet Staging Sites, repérer le site de staging et choisir l'option de mise à jour. Trois options : Files + DB (remplace entièrement le staging par le live), Uploads folder + Database (synchronise base et uploads), Custom Content (sélection manuelle). Cliquer sur « Update Now » sans fermer la page.

**Réglages du staging (Staging Settings)**

- **Performance et ressources** : DB Copy Count, DB Replace Count, File Copy Count, Max File Size (0 Mo = tous les fichiers), Staging Memory Limit (256 Mo par défaut), PHP Script Execution Timeout, Delay Between Requests, Retrying Times.
- **Options générales** : accessibilité publique du staging, maintien de la structure d'URL lors du transfert, conservation des sites de staging à la désinstallation, affichage du bouton de publication sur le tableau de bord du staging.
- **Permissions de fichiers** : niveaux de permissions appliqués au site cible (755 pour les dossiers, 644 pour les fichiers, etc.).

### Points de vigilance

- Publier un staging vers le live avec l'option « tout » **remplace entièrement la production** : opération destructive, à confirmer avec prudence.
- Bien distinguer « publier vers le live » (staging vers production) et « mettre à jour le staging » (production vers staging) : les deux sens existent et ne font pas la même chose.
- Sur les sites e-commerce ou à contenu très actif, une publication staging vers live brute peut **écraser les données arrivées en production** entre-temps (commandes, formulaires) : pour ce cas, voir Database Merging au Module 8.
- En base de données partagée, le préfixe distinct (« wpstg_ ») est essentiel pour ne pas mélanger staging et production.
- **Ne pas fermer le navigateur** pendant la création, la publication ou la mise à jour d'un staging.

### Liens doc officielle

- Vue d'ensemble staging (Free) : https://docs.wpvivid.com/overview-staging-free.html
- Vue d'ensemble staging (Pro) : https://docs.wpvivid.com/staging-pro-overview.html
- Créer un site de staging : https://docs.wpvivid.com/create-a-staging-site.html
- Publier un staging vers le live : https://docs.wpvivid.com/publish-a-staging-site-to-live-with-staging-pro.html
- Mettre à jour un site de staging : https://docs.wpvivid.com/update-a-staging-site.html
- Réglages staging : https://docs.wpvivid.com/staging-settings.html

### Vidéos YouTube

- « How To Create a WordPress Staging Site using a Free Plugin (WPVivid backup Plugin) | WPMadEasy » : https://www.youtube.com/watch?v=uNB7QMLWU6w
- « Don't Risk It! THIS is Why You Need a Staging Site | WpVivid setup » : https://www.youtube.com/watch?v=-5PdcS_9bgM
- « WordPress staging setup and copy to live site - with WpVivid pro plugin » : https://www.youtube.com/watch?v=yBAbRhPblOM

---

## Module 8 : Sécurité et fonctions avancées

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Chiffrer les sauvegardes de base de données et en comprendre les enjeux.
- Restreindre l'accès au plugin par rôle utilisateur.
- Utiliser les snapshots de base de données.
- Comprendre la marque blanche, la sauvegarde multisite et la fusion de base de données.
- Configurer les réglages généraux et avancés, les rapports email, l'outil de remplacement d'URL et les logs.

### Contenu

**Chiffrement de la base de données (Pro)**

WPvivid Pro peut chiffrer les sauvegardes de base de données avec un mot de passe, via l'algorithme AES (Advanced Encryption Standard). Utile pour la conformité RGPD, la protection des données sensibles et la prévention des fuites. Activation : WPvivid Backup Pro puis Settings, cocher « Enable Database Encryption », créer un mot de passe fort (12+ caractères, majuscules, minuscules, chiffres, symboles), enregistrer.

Précaution critique : **le mot de passe de chiffrement ne peut être ni récupéré ni réinitialisé**. S'il est perdu, les sauvegardes deviennent définitivement inaccessibles. Seuls les fichiers de base de données sont chiffrés, pas les fichiers WordPress.

**Rôles et capacités utilisateurs (Pro)**

Permet de contrôler quels rôles WordPress accèdent à quelles fonctions WPvivid, plutôt que de réserver l'accès aux seuls administrateurs en bloc. Un super admin désigné dispose d'un accès complet et de l'autorité pour gérer les permissions des autres rôles (Administrateur, Éditeur, Auteur, Contributeur, Abonné). Permissions contrôlables : créer/supprimer des sauvegardes, restaurer, migrer, configurer le stockage distant, consulter les logs. Fonction fournie via le module additionnel « Roles & Capabilities ».

**Snapshots de base de données (Pro)**

Un snapshot est une copie instantanée de l'état de la base de données seule (sans les fichiers). Pratique pour créer un point de restauration rapide avant une mise à jour, une édition en masse de contenus, ou une phase de développement. Création : WPvivid puis Database Snapshots, saisir une description facultative, « Create Snapshot ». La restauration écrase les données actuelles.

**Marque blanche / White Label (Pro)**

Permet aux agences et prestataires de personnaliser l'interface du plugin : nom affiché, slug d'URL (remplacer « wpvivid »), logo dans les rapports email, infos de support et d'auteur, visibilité des liens de documentation. Point important : WPvivid identifie les fichiers de sauvegarde selon le slug défini. Lors d'une migration, le site de destination doit utiliser le **même slug** que la source pour reconnaître les fichiers.

**Sauvegarde multisite**

WPvivid Pro prend en charge les installations multisite **en sous-répertoires** (ex. example.com/site1). Les configurations **en sous-domaines** (site1.example.com) ne sont pas compatibles. La sauvegarde se fait au niveau réseau (toutes les tables, réglages réseau, sous-sites), pas par sous-site individuel ; la restauration est complète au niveau réseau (pas de restauration partielle). Opérations réservées à l'administration réseau.

**Fusion de base de données / Database Merging (Pro)**

Permet de fusionner uniquement les modifications (fichiers uploads/médias et base de données) d'un site de développement vers la production, **sans écraser** les données arrivées en production entre-temps (commandes, formulaires, inscriptions). Cas d'usage typique : sites e-commerce ou à contenu très actif. Sont fusionnés : modifications de base de données et fichiers médias. Ne sont pas fusionnés : modifications de thèmes, extensions et cœur WordPress.

**Réglages généraux (Free)**

Nombre de sauvegardes conservées (local et distant), scan du contenu avant sauvegarde, fusion des fichiers en un seul paquet, conservation d'une copie locale après envoi cloud, répertoire de stockage local personnalisable, ajout du nom de domaine aux fichiers, rapports email, suppression automatique des sauvegardes périmées, nettoyage de l'espace disque, suppression du dossier de sauvegarde à la désinstallation, import/export de la configuration du plugin.

**Réglages avancés**

Accès : WPvivid Backup Pro puis Settings puis Backup (Advanced). Principaux réglages : Learning Mode (adaptation automatique aux serveurs limités), Large Database Mode et Large Uploads Mode (stabilité sur gros volumes), méthode d'accès à la base (WPDB = compatibilité maximale mais plus lent, PDO = plus rapide), méthode de compression (ZipArchive par défaut, PclZip en alternative), modes de performance (Low pour hébergement mutualisé, Mid recommandé, High pour serveur dédié, Custom). Paramètres personnalisables : nombre de fichiers compressés par cycle (défaut 500), taille de scission des sauvegardes (défaut 4 Go), timeout d'exécution PHP (défaut 1800 s), limite mémoire PHP (défaut 256 Mo), taille des chunks de transmission.

**Rapports par email**

Notifient automatiquement du statut des sauvegardes (à chaque sauvegarde, ou uniquement en cas d'échec). Réglages : WPvivid Plugin puis Settings puis onglet Backup puis section Email Report. Options : destinataires (adresses séparées par virgules), déclencheurs, objet personnalisé, inclusion du journal en pièce jointe. Le serveur doit pouvoir envoyer des emails (PHP mail ou SMTP) ; un plugin SMTP type WP Mail SMTP améliore la fiabilité.

**Outil de remplacement d'URL (URL Replacing Tool)**

Disponible depuis WPvivid Backup Pro 2.0.23. Permet de chercher et remplacer des chaînes (noms de domaine, URL) directement dans la base de données, sans migration complète ni manipulation de fichiers SQL. Il gère correctement les **données sérialisées**, ce qui préserve les réglages des extensions et thèmes après un changement d'URL. Accès : WPvivid Plugin puis Export/Import Page puis URL Replacing Tool. Renseigner ancienne URL, nouvelle URL, tables concernées, puis « Search & Replace Now ». Précaution : faire une sauvegarde complète de la base avant, car les modifications sont irréversibles.

**Logs (journaux)**

Historique centralisé de toutes les opérations de sauvegarde, restauration et migration. Indispensables pour diagnostiquer lenteurs, dépassements de délai ou échecs. Accès : WPvivid Backup Pro puis Backup Manager puis onglet Logs. Chaque entrée indique la date, le type d'opération, le fichier journal associé, et permet de visualiser ou télécharger les détails. Pour une demande de support, toujours joindre le fichier journal correspondant.

### Points de vigilance

- Le **mot de passe de chiffrement** est irrécupérable : le stocker dans un gestionnaire de mots de passe. Une sauvegarde chiffrée + mot de passe perdu = sauvegarde perdue.
- Le chiffrement ne couvre **que la base de données**, pas les fichiers : une protection complète passe aussi par un stockage cloud sécurisé.
- White Label modifie le slug d'identification des fichiers : une migration entre deux sites avec des slugs différents échoue à reconnaître les sauvegardes. Garder le même slug source et destination.
- Multisite : **sous-répertoires uniquement**, pas de sous-domaines ; pas de sauvegarde ni restauration par sous-site.
- L'outil de remplacement d'URL est **destructif et irréversible** : sauvegarde complète obligatoire avant usage.
- Toujours **joindre le log** quand on contacte le support : cela accélère nettement la résolution.

### Liens doc officielle

- Chiffrement de la base de données : https://docs.wpvivid.com/encrypt-database-backup.html
- Rôles et capacités : https://docs.wpvivid.com/user-roles-and-capabilities.html
- Snapshots de base de données : https://docs.wpvivid.com/database-snapshots.html
- Marque blanche : https://docs.wpvivid.com/white-label-backup-migration-pro.html
- Sauvegarde multisite : https://docs.wpvivid.com/back-up-wordpress-multisites.html
- Réglages généraux (Free) : https://docs.wpvivid.com/general-settings-free.html
- Réglages avancés : https://docs.wpvivid.com/advanced-settings.html
- Rapport email : https://docs.wpvivid.com/email-report.html
- Outil de remplacement d'URL : https://docs.wpvivid.com/url-replacing-tool.html
- Logs : https://docs.wpvivid.com/logs-backup-migration.html
- Fusion de base de données : https://docs.wpvivid.com/database-merging-overview.html

### Vidéos YouTube

- « WPvivid Backup, Staging and Migration Plugin - The All-in-One Solution! » : https://www.youtube.com/watch?v=Dl9G9b6ztto

---

## Module 9 : Dépannage

### Objectifs pédagogiques

À la fin de ce module, l'apprenant saura :

- Identifier les causes courantes d'un échec de sauvegarde et appliquer les bons réglages.
- Diagnostiquer et résoudre un échec de restauration.
- Diagnostiquer et résoudre un échec de migration.
- Traiter les problèmes courants de connexion cloud et d'interface.

### Contenu

**Échec de sauvegarde**

Cause principale : ressources serveur insuffisantes (dépassement de délai, tâche qui ne répond plus).

Réglages recommandés (essentiellement dans Settings puis Backup (Advanced)) :

- Désactiver la fusion de tous les fichiers de sauvegarde en un seul paquet.
- Désactiver le Learning Mode ; activer Large Database Mode et Large Uploads Mode.
- Méthode d'accès base de données : PDO. Compression : ZipArchive. Mode de performance : Custom.
- Compresser un nombre réduit de fichiers par lot (par exemple 300 en Pro, 500 en Free) avec une scission par paquet d'environ 100 Mo.
- Exclure les fichiers très volumineux (par exemple plus de 100 Mo).
- Allouer un timeout d'exécution PHP plus large (par exemple 300 s) et davantage de mémoire (par exemple 512 Mo).
- Réduire la taille des chunks (par exemple 2048 Ko).
- Toujours enregistrer via « Save Changes ».

**Échec de restauration**

- **Timeout à l'import SQL** : manque de mémoire ou limite de taille de paquet MySQL. Augmenter la limite mémoire PHP de restauration (jusqu'à 1024-2048 Mo en Pro) ; côté serveur, augmenter max_allowed_packet à 32-64 Mo.
- **Restauration bloquée à 99%** : ressources insuffisantes lors de la fusion des tables temporaires. Augmenter la mémoire PHP.
- **Impossible de décoder les fichiers** : espace disque insuffisant ou timeout trop court. Disposer d'un espace libre égal à 2x la taille du site ; augmenter le timeout à 180-300 s.
- **Mémoire PHP épuisée** : augmenter la limite mémoire.
- **Fichiers de sauvegarde corrompus** : souvent un manque d'espace disque au moment de la sauvegarde. Tenter une extraction manuelle sur ordinateur ; si elle réussit, transférer les fichiers par FTP dans le répertoire wp-content/wpvividbackups ; sinon, recréer une sauvegarde après avoir libéré de l'espace.
- **Sauvegarde incomplète** : désactiver l'option « Merge all backup files into 1 zip » et libérer de l'espace.
- **PDOException** : problème d'accès MySQL via PDO. Basculer la méthode d'accès sur WPDB.
- Conseil général : restaurer sur une **installation WordPress vierge** maximise les chances de réussite.

**Échec de migration**

- **Dépassement de délai d'export / reprises excessives** : ressources serveur insuffisantes. Ajuster les réglages WPvivid (voir échec de sauvegarde).
- **Fichier d'archive manquant (PCLZIP_ERR_MISSING_FILE)** : espace disque insuffisant. Disposer d'au moins 2x la taille du site.
- **Fichier Gzip corrompu (PCLZIP_ERR_BAD_FORMAT)** : le serveur interrompt le processus. Réduire « Split a backup every this size » à 50-100 Mo.
- **Erreurs SSL** (certificat invalide ou manquant) : utiliser la méthode de transfert manuel (via archive).
- **Timeout à l'envoi (cURL error 28)** : le serveur destination limite la taille reçue. Réduire la « Chunk Size » à 256-512 Ko.
- **Erreur AffiliateWP** : la table wp_affiliate_wp_campaigns est une vue, pas une table physique ; la désélectionner manuellement avant l'export.
- **Impossible de se connecter après migration** : décalage de préfixe de base de données entre la table options et wp-config. Vérifier la concordance via phpMyAdmin.
- **Erreurs 404 sur les pages internes** : fichier .htaccess non régénéré. Aller dans Réglages puis Permaliens et enregistrer deux fois.
- **Images de fond manquantes (Elementor, Oxygen)** : ancien cache d'URL des constructeurs de pages. Vider le cache de chaque constructeur.

**Problèmes courants (connexion cloud et interface)**

- **ERR_TOO_MANY_REDIRECTS** : un plugin de redirection (type Really Simple SSL) ou un pare-feu bloque l'authentification. Désactiver temporairement.
- **HTTP 403 / 404** : le pare-feu bloque la redirection du fournisseur cloud après autorisation. Désactiver temporairement pare-feu et plugin de masquage de connexion.
- **Timeout FTP** : port FTP personnalisé bloqué par le pare-feu serveur. Vérifier le port et demander son autorisation à l'hébergeur.
- **Erreur de serveur WPvivid** : l'IP du serveur est identifiée comme bot. Soumettre un ticket avec l'IP pour déblocage manuel.
- **Fichier non reconnu / aucune sauvegarde détectée** : nom de fichier ZIP modifié, ou White Label actif côté source. Respecter le nom d'origine, ou activer le même White Label (marque et slug) côté destination.
- **Erreur -200 / HTTP sur gros uploads** : la sécurité serveur bloque les gros téléversements. Passer par FTP ou un gestionnaire de fichiers, ou augmenter les limites.
- **Erreur JSON** : le serveur renvoie une page HTML au lieu de données JSON. Ouvrir les outils développeur du navigateur pour identifier l'erreur PHP sous-jacente.
- **HTTP 503** : trop de tentatives de connexion échouées au compte WPvivid. Attendre quelques minutes ou contacter le support.

### Points de vigilance

- La grande majorité des échecs viennent de **limites serveur** (mémoire PHP, timeout, espace disque) : c'est le premier réflexe de diagnostic à enseigner.
- Toujours prévoir un espace disque libre d'au moins **2x la taille du site** pour sauvegarde, restauration et migration.
- Les **plugins de sécurité, de cache et de redirection** sont la cause récurrente des échecs d'authentification cloud et de migration : les désactiver temporairement.
- Après une migration, les réflexes incontournables : régénérer les permaliens et vider le cache des constructeurs de pages.
- Pour toute demande de support, **joindre le log** de l'opération concernée.
- Le mode performance « Custom » et les modes Large Database/Large Uploads sont les leviers concrets pour faire passer une sauvegarde sur un hébergement mutualisé contraint.

### Liens doc officielle

- Échec de sauvegarde : https://docs.wpvivid.com/backup-failed.html
- Échec de restauration : https://docs.wpvivid.com/restore-failed.html
- Échec de migration : https://docs.wpvivid.com/migration-failed.html
- Problèmes courants : https://docs.wpvivid.com/common-issues.html

### Vidéos YouTube

- « WordPress Migration & Backup Made Easy: Complete WPvivid Tutorial » : https://www.youtube.com/watch?v=uHrJbg5WIFk
- « WPvivid Backup, Staging and Migration Plugin - The All-in-One Solution! » : https://www.youtube.com/watch?v=Dl9G9b6ztto

---

## Récapitulatif des vidéos YouTube curées

Sélection de tutoriels tiers (non officiels) identifiés via recherche web le 2026-05-20. Les durées et dates exactes n'ont pas pu être confirmées de manière fiable ; les noms de chaîne marqués « à confirmer » n'étaient pas extractibles automatiquement et doivent être vérifiés à l'ouverture de la vidéo.

| # | Titre | Chaîne | Langue | URL | Couvre |
|---|-------|--------|--------|-----|--------|
| 1 | WordPress Migration & Backup Made Easy: Complete WPvivid Tutorial | À confirmer | Anglais | https://www.youtube.com/watch?v=uHrJbg5WIFk | Tutoriel complet du plugin gratuit : sauvegarde et migration. Vidéo récente (env. fin 2025). |
| 2 | WPvivid Backup, Staging and Migration Plugin - The All-in-One Solution! | À confirmer | Anglais | https://www.youtube.com/watch?v=Dl9G9b6ztto | Tour d'horizon complet : sauvegarde, staging et migration. Bonne vue d'ensemble. |
| 3 | Amazing FREE Backup and Restore Plugin - Migration and Staging - WPVivid | À confirmer | Anglais | https://www.youtube.com/watch?v=BU0OP6QrQMw | Présentation du plugin gratuit : sauvegarde, restauration, migration, staging. |
| 4 | How to Migrate A WordPress Website to Any Destination Using WPvivid Backup Plugin For Free? | À confirmer | Anglais | https://www.youtube.com/watch?v=_VIoBxC7fFU | Pas à pas migration d'un site WordPress vers n'importe quelle destination, en gratuit. |
| 5 | Free WordPress Backup and Migration with WPVivid (#NoCode) | À confirmer | Anglais | https://www.youtube.com/watch?v=8lQifvQJ6Xc | Sauvegarde et migration d'un site, approche sans code. |
| 6 | WPvivid Backup and Restore Installation and getting started | À confirmer | Anglais | https://www.youtube.com/watch?v=k1SeyQnFwwk | Installation et prise en main : idéal pour le module Découverte. |
| 7 | WPvivid Backup Plugin Tutorial 2025 | WordPress Free | À confirmer | Anglais | https://www.youtube.com/watch?v=1emJCk9y3G4 | Tutoriel récent (2025) du plugin gratuit : sauvegarde et restauration. |
| 8 | How To Create a WordPress Staging Site using a Free Plugin (WPVivid backup Plugin) | WPMadEasy | Anglais | https://www.youtube.com/watch?v=uNB7QMLWU6w | Créer un site de staging avec la version gratuite (env. 2024). |
| 9 | Don't Risk It! THIS is Why You Need a Staging Site | WpVivid setup | À confirmer | Anglais | https://www.youtube.com/watch?v=-5PdcS_9bgM | Intérêt d'un site de staging et configuration avec WPvivid. |
| 10 | WordPress staging setup and copy to live site - with WpVivid pro plugin | À confirmer | Anglais | https://www.youtube.com/watch?v=yBAbRhPblOM | Configuration du staging et publication vers le live avec WPvivid Pro. |
| 11 | Comment faire une sauvegarde et restauration avec WPvivid - Wordpress | À confirmer | Français | https://www.youtube.com/watch?v=GtqLMvgVnRw | Sauvegarde et restauration d'un site WordPress (français, env. 2020). |
| 12 | Faire une sauvegarde et migrer son site avec WPVivid Backup | À confirmer | Français | https://www.youtube.com/watch?v=hpV8M3iDWe0 | Sauvegarde puis migration d'un site WordPress (français, env. 2022). |
| 13 | Restauration et migration facile du site internet avec WPvivid backup | À confirmer | Français | https://www.youtube.com/watch?v=BMeK5xUrS2s | Restauration et migration de site (français, env. 2023). |
| 14 | Migrez votre site web avec l'outil de migration automatique de WP Vivid | À confirmer | Français | https://www.youtube.com/watch?v=mJZmHIWL1as | Auto-migration directe site-à-site (français, chaîne autour de l'écosystème Elementor). |

Total : 14 vidéos curées (10 en anglais, 4 en français), couvrant la découverte, la sauvegarde/restauration, la migration et le staging.

---

## Note de clôture : limites rencontrées

- Toutes les pages de documentation officielle listées dans la consigne ont été récupérées et synthétisées avec succès. Aucune page n'a été inaccessible.
- Les **tarifs précis** de WPvivid Pro (montants par formule, nombre de sites couverts) ne sont détaillés ni sur la page d'accueil ni sur la page free-vs-pro : seules les formules (abonnement / à vie) et la garantie 30 jours sont confirmées. À compléter manuellement depuis la page de tarification officielle si la formation doit citer des prix.
- Le **nom de chaîne** de la plupart des vidéos YouTube n'a pas pu être extrait de façon fiable (YouTube ne renvoie pas ces métadonnées proprement via récupération web) : ces champs sont marqués « à confirmer » et doivent être vérifiés à l'ouverture de chaque vidéo. Les **durées** et **dates de publication** exactes n'ont pas été confirmées non plus.
- Le décompte des destinations de stockage distant varie de 13 à 14 selon la manière de compter les variantes (FTP / FTP2 / sFTP, OneDrive grand public et professionnel). Le Module 5 retient la liste complète en le précisant.
- Sur quelques pages, la documentation officielle ne distingue pas explicitement Free et Pro pour une fonction donnée : dans ces cas, le marquage Free/Pro de ce document s'appuie sur le recoupement avec la page free-vs-pro et les overviews dédiés. En cas de doute pour un point précis de la formation, vérifier directement sur la page concernée.

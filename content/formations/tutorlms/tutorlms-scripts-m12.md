# Scripts vidéo - Module 12 : Intégrations tierces

**Formation** : Maîtriser TutorLMS
**Module** : M12 - Intégrations tierces (Premium)
**Leçons** : 11 vidéos + 1 quiz
**Durée totale** : ~55 min
**Date** : 2026-03-23

---

### Leçon 12.1 : Google Meet (cours en direct)

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Google Meet
**Source** : Vidéo #17 + doc google-meet-integration

---

**[INTRO - face caméra]**

Tu veux donner des cours en direct à tes élèves ? Google Meet est la solution la plus simple - et la plus économique. C'est gratuit avec un compte Google, intégré nativement dans TutorLMS, et tes élèves n'ont rien à installer. Dans cette leçon, on connecte Google Meet à TutorLMS et on planifie un premier cours en direct.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Première étape : active l'addon Google Meet. Va dans Tutor LMS, puis Addons. Cherche "Google Meet Integration" et active-le avec le toggle.

**[ÉCRAN - screencast Google Cloud Console]**

[Navigation vers console.cloud.google.com > APIs & Services > Credentials]

Maintenant, il faut connecter ton compte Google. Ça passe par la Google Cloud Console. Connecte-toi, crée un projet si tu n'en as pas, puis va dans APIs & Services, Credentials.

Clique sur "Create Credentials", puis "OAuth 2.0 Client ID". Sélectionne "Web application". Dans les URIs de redirection autorisés, ajoute l'URL que TutorLMS t'affiche dans ses réglages Google Meet.

Tu obtiens un Client ID et un Client Secret. Copie-les.

**[ÉCRAN - screencast TutorLMS réglages Google Meet]**

[Navigation vers Tutor LMS > Settings > Google Meet]

Retourne dans TutorLMS, Settings, Google Meet. Colle le Client ID et le Client Secret. Clique sur "Generate token" - ça ouvre une fenêtre d'autorisation Google. Accepte, et le token est généré. La connexion est établie.

**[ÉCRAN - screencast Course Builder]**

[Navigation vers un cours > onglet Google Meet]

Pour planifier un cours en direct, ouvre le Course Builder d'un cours. Tu trouves un nouvel onglet "Google Meet". Clique dessus, puis "Create a meeting".

Remplis :
- Le titre du meeting
- La date et l'heure de début
- La durée
- Le fuseau horaire

Tu peux aussi activer l'enregistrement automatique - la session sera enregistrée dans Google Drive.

**[ÉCRAN - screencast front-end élève]**

[Montre la page cours côté élève avec le meeting planifié]

Côté élève : le meeting apparaît dans le curriculum du cours avec la date et l'heure. Quand l'heure arrive, un bouton "Join Meeting" s'affiche. L'élève clique et rejoint directement le meeting dans son navigateur.

**[TRANSITION - face caméra]**

La recommandation schoolsWP : Google Meet est le meilleur choix pour les cours en direct. C'est gratuit, ça fonctionne dans le navigateur, et l'intégration TutorLMS est native. Zoom est une alternative si tes élèves l'utilisent déjà - on le voit dans la leçon 12.3. Mais si tu pars de zéro, reste sur Google Meet.

---

**Points clés** :
- Addon Google Meet à activer dans Tutor LMS > Addons
- Connexion via Google Cloud Console (OAuth 2.0 Client ID + Secret)
- Planning des meetings dans le Course Builder, onglet Google Meet
- Enregistrement automatique disponible (stocké dans Google Drive)
- Côté élève : bouton "Join Meeting" directement dans le curriculum
- Recommandation schoolsWP : Google Meet (gratuit) > Zoom (payant)

**Mots clés SEO** : TutorLMS Google Meet, cours en direct TutorLMS, visioconférence LMS WordPress, Google Meet intégration TutorLMS

---

### Leçon 12.2 : Google Classroom

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Google Classroom
**Source** : Vidéo #29 + doc google-classroom

---

**[INTRO - face caméra]**

Google Classroom, c'est l'outil de Google pour gérer des classes en ligne. Si tes élèves sont dans un contexte scolaire ou universitaire, ou si ton établissement utilise déjà Google Workspace, cette intégration a du sens. TutorLMS peut synchroniser tes cours avec Google Classroom - tes élèves retrouvent tout dans leur environnement habituel.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Google Classroom Integration" dans Tutor LMS > Addons. Le toggle, comme d'habitude.

**[ÉCRAN - screencast Google Cloud Console]**

[Navigation vers APIs & Services > Library > Google Classroom API]

Dans la Google Cloud Console, active l'API Google Classroom. Va dans APIs & Services, Library, cherche "Google Classroom API" et active-la. Si tu as déjà configuré Google Meet, tu peux utiliser le même projet.

Ensuite, va dans Credentials et crée un nouvel OAuth 2.0 Client ID - ou réutilise celui de Google Meet si l'URI de redirection est la même.

**[ÉCRAN - screencast TutorLMS réglages Google Classroom]**

[Navigation vers Tutor LMS > Settings > Google Classroom]

Dans TutorLMS, Settings, Google Classroom. Colle le Client ID et le Client Secret. Génère le token comme pour Google Meet.

**[ÉCRAN - screencast création d'un classroom]**

[Montre la création d'un classroom depuis le Course Builder]

Pour lier un cours à Google Classroom, ouvre le Course Builder. Un nouvel onglet "Google Classroom" apparaît. Tu peux :
- Créer un nouveau classroom directement depuis TutorLMS
- Ou lier un classroom existant

Quand tu crées un classroom, TutorLMS génère automatiquement un code d'invitation que tes élèves utilisent pour rejoindre la classe dans Google Classroom.

**[ÉCRAN - screencast synchronisation]**

[Montre la synchro des devoirs et du matériel]

La synchronisation fonctionne dans les deux sens :
- Les contenus de cours TutorLMS apparaissent comme matériel dans Google Classroom
- Les devoirs et notes peuvent être gérés depuis l'interface Google

C'est pratique pour les formateurs qui ont des élèves habitués à Google Classroom mais qui veulent la puissance de TutorLMS pour la structure des cours.

**[TRANSITION - face caméra]**

Google Classroom, c'est un pont entre TutorLMS et l'écosystème Google Education. Si tes élèves sont déjà dans cet écosystème, l'intégration évite de leur imposer un changement d'habitude. Si ce n'est pas le cas, TutorLMS seul couvre tous les besoins.

---

**Points clés** :
- Addon Google Classroom à activer dans Addons
- Nécessite l'API Google Classroom activée dans Google Cloud Console
- Même processus OAuth que Google Meet (Client ID + Secret + token)
- Création de classroom depuis le Course Builder ou liaison avec un existant
- Code d'invitation généré automatiquement
- Synchronisation bidirectionnelle (contenus + devoirs)
- Utile surtout dans un contexte scolaire/universitaire avec Google Workspace

**Mots clés SEO** : TutorLMS Google Classroom, intégration Google Classroom WordPress, LMS Google Education, synchroniser cours Google Classroom

---

### Leçon 12.3 : Zoom (cours en direct)

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Zoom
**Source** : doc zoom-integration

---

**[INTRO - face caméra]**

Zoom est l'autre option pour les cours en direct dans TutorLMS. Si tes élèves utilisent déjà Zoom ou si ton organisation a un compte Zoom Pro, cette intégration est pertinente. La mise en place est un peu plus longue que Google Meet, et Zoom est payant pour les sessions de plus de 40 minutes. Voyons comment le configurer.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Zoom Integration" dans Tutor LMS > Addons.

**[ÉCRAN - screencast Zoom Marketplace]**

[Navigation vers marketplace.zoom.us]

Contrairement à Google Meet, Zoom utilise une app dédiée. Va sur marketplace.zoom.us, connecte-toi avec ton compte Zoom. Clique sur "Develop", puis "Build App". Sélectionne "Server-to-Server OAuth".

Donne un nom à ton app - par exemple "TutorLMS Integration". Zoom te fournit :
- Un Account ID
- Un Client ID
- Un Client Secret

Copie ces trois valeurs.

**[ÉCRAN - screencast permissions Zoom]**

[Montre l'onglet Scopes de l'app Zoom]

Dans l'onglet Scopes de ton app Zoom, ajoute les permissions nécessaires :
- meeting:write:admin - pour créer des meetings
- meeting:read:admin - pour lire les meetings
- user:read:admin - pour accéder aux infos utilisateur

Active l'app une fois les scopes configurés.

**[ÉCRAN - screencast TutorLMS réglages Zoom]**

[Navigation vers Tutor LMS > Settings > Zoom]

Retourne dans TutorLMS, Settings, Zoom. Colle l'Account ID, le Client ID et le Client Secret. Enregistre. La connexion est établie si les champs deviennent verts.

**[ÉCRAN - screencast planification meeting]**

[Navigation vers Course Builder > onglet Zoom]

La planification fonctionne comme Google Meet. Dans le Course Builder, onglet Zoom, clique sur "Create a Zoom Meeting". Remplis le titre, la date, la durée. Tu peux aussi configurer :
- Le mot de passe du meeting
- La salle d'attente
- L'enregistrement automatique (cloud si Zoom Pro, local sinon)

**[ÉCRAN - screencast front-end élève]**

[Montre le bouton "Join with Zoom" côté élève]

Côté élève : un bouton "Join with Zoom" apparaît dans le curriculum. L'élève clique et rejoint le meeting - soit dans l'app Zoom, soit dans le navigateur.

**[TRANSITION - face caméra]**

Zoom fonctionne bien mais a deux inconvénients : la limite de 40 minutes en version gratuite et la configuration plus complexe via le Marketplace. Si tu n'as pas de raison spécifique d'utiliser Zoom, Google Meet est le choix le plus simple. Si ton organisation impose Zoom, cette intégration fait le travail.

---

**Points clés** :
- Addon Zoom à activer dans Addons
- Configuration via marketplace.zoom.us (Server-to-Server OAuth)
- 3 identifiants : Account ID, Client ID, Client Secret
- Scopes requis : meeting:write:admin, meeting:read:admin, user:read:admin
- Planning dans le Course Builder, onglet Zoom
- Options : mot de passe, salle d'attente, enregistrement
- Limite : 40 min en version gratuite, configuration plus longue que Google Meet
- Recommandation schoolsWP : Google Meet (gratuit) sauf si Zoom est imposé

**Mots clés SEO** : TutorLMS Zoom intégration, cours en direct Zoom WordPress, visioconférence Zoom LMS, TutorLMS Zoom configuration

---

### Leçon 12.4 : WooCommerce

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + WooCommerce
**Source** : doc woocommerce

---

**[INTRO - face caméra]**

WooCommerce était le seul moyen de vendre des cours avec TutorLMS avant la v3. Depuis, le eCommerce natif le remplace dans la majorité des cas - on l'a vu dans le module 8. Mais WooCommerce reste utile dans deux situations : si tu vends déjà d'autres produits avec WooCommerce, ou si tu as besoin d'extensions WooCommerce spécifiques comme les factures avancées ou les taxes multi-pays. Voyons comment ça fonctionne.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > eCommerce Engine]

Pour utiliser WooCommerce comme moteur de paiement, va dans Settings, Monetization, eCommerce Engine. Sélectionne "WooCommerce" au lieu de "Native". Enregistre.

Prérequis : WooCommerce doit être installé et activé sur ton site.

**[ÉCRAN - screencast création produit WooCommerce]**

[Navigation vers Products > Add New]

Quand WooCommerce est actif comme moteur, chaque cours TutorLMS a besoin d'un produit WooCommerce associé. Tu peux le créer de deux façons :
- Automatiquement - TutorLMS crée le produit quand tu définis un prix dans le Course Builder
- Manuellement - tu crées un produit WooCommerce et tu le lies au cours

**[ÉCRAN - screencast Course Builder pricing]**

[Montre la section Pricing avec WooCommerce actif]

Dans le Course Builder, la section Pricing change quand WooCommerce est actif. Tu vois un champ pour lier un produit WooCommerce existant ou en créer un nouveau. Le prix, les promotions et les options d'abonnement se gèrent dans WooCommerce, pas dans TutorLMS.

**[ÉCRAN - screencast checkout WooCommerce]**

[Montre le parcours d'achat côté élève]

Côté élève : le parcours d'achat passe par le panier et le checkout WooCommerce classique. Toutes les passerelles de paiement configurées dans WooCommerce sont disponibles. Après le paiement, l'élève est automatiquement inscrit au cours.

**[ÉCRAN - screencast avantages WooCommerce]**

[Slide récapitulatif]

Les cas où WooCommerce a du sens :
- Tu vends des produits physiques ou digitaux en plus des cours
- Tu utilises des extensions WooCommerce spécifiques (factures, taxes, abonnements avancés)
- Tu as déjà un catalogue WooCommerce et tu ne veux pas migrer

Les cas où le eCommerce natif est meilleur :
- Tu vends uniquement des cours
- Tu veux une configuration simple
- Tu débutées et tu n'as pas d'historique WooCommerce

**[TRANSITION - face caméra]**

La recommandation schoolsWP : si tu démarres de zéro, utilise le eCommerce natif. WooCommerce ajoute de la complexité et de la charge sur ton serveur. Ne l'utilise que si tu as une raison concrète - pas par habitude.

---

**Points clés** :
- Activation : Settings > Monetization > eCommerce Engine > WooCommerce
- WooCommerce doit être installé et actif
- Chaque cours nécessite un produit WooCommerce associé
- Prix et abonnements gérés dans WooCommerce, pas dans TutorLMS
- Checkout WooCommerce classique (panier + paiement)
- Utile si tu vends déjà d'autres produits ou si tu as besoin d'extensions spécifiques
- Recommandation schoolsWP : eCommerce natif sauf besoin spécifique WooCommerce

**Mots clés SEO** : TutorLMS WooCommerce, vendre cours WooCommerce, WooCommerce vs eCommerce natif TutorLMS, intégration WooCommerce LMS

---

### Leçon 12.5 : Elementor

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Elementor
**Source** : doc elementor-integration

---

**[INTRO - face caméra]**

Elementor est le page builder le plus utilisé sur WordPress. Si c'est celui que tu utilises pour ton site, bonne nouvelle : TutorLMS s'intègre avec. Tu peux personnaliser les pages de cours, le catalogue, le dashboard élève - tout ça avec l'éditeur visuel d'Elementor. Voyons comment activer l'intégration et quels widgets sont disponibles.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Elementor Addons" dans Tutor LMS > Addons. Prérequis : Elementor (version gratuite ou Pro) doit être installé et actif.

**[ÉCRAN - screencast Elementor editor]**

[Ouvre une page de cours avec Elementor]

Une fois l'addon actif, édite une page de cours avec Elementor. Dans le panneau de widgets, une nouvelle catégorie "Tutor LMS" apparaît. Tu y trouves plus de 25 widgets dédiés.

**[ÉCRAN - screencast widgets principaux]**

[Montre les widgets dans le panneau Elementor]

Les widgets les plus utiles :

- Course Title, Course Thumbnail, Course Rating - les bases de toute page de cours
- Course Curriculum - affiche le contenu structuré du cours
- Course Benefits, Course Requirements - les listes "ce que tu vas apprendre" et "prérequis"
- Add to Cart / Enroll Button - le bouton d'achat ou d'inscription
- Course Instructor - affiche le profil de l'instructeur
- Course Reviews - les avis des élèves

Tu glisses-déposes ces widgets comme n'importe quel widget Elementor et tu les stylises avec les options habituelles : couleurs, typographie, espacement, responsive.

**[ÉCRAN - screencast template de page cours]**

[Montre la création d'un template Elementor pour les pages de cours]

Le plus puissant : tu peux créer un template Elementor pour toutes tes pages de cours. Va dans Templates > Theme Builder > Single Course. Construis ton layout une fois, et il s'applique à tous tes cours automatiquement.

**[ÉCRAN - screencast dashboard élève]**

[Montre la personnalisation du dashboard avec Elementor]

Tu peux aussi personnaliser le dashboard élève avec Elementor. Les widgets disponibles : Course List, Course Progress, Profile Info, Enrolled Courses. Ça te permet de créer un espace élève qui correspond à l'identité visuelle de ton site.

**[TRANSITION - face caméra]**

Si tu utilises déjà Elementor, cette intégration est un must. Tu gardes le contrôle total sur le design sans toucher au code. Si tu n'utilises pas encore de page builder, on voit Divi, Oxygen et Droip dans les prochaines leçons - choisis celui qui correspond à ton workflow.

---

**Points clés** :
- Addon "Elementor Addons" à activer + Elementor installé
- 25+ widgets TutorLMS dans l'éditeur Elementor
- Widgets principaux : Title, Curriculum, Benefits, Add to Cart, Reviews, Instructor
- Template Theme Builder pour appliquer un layout à toutes les pages de cours
- Dashboard élève personnalisable avec Elementor
- Drag-and-drop + options de style Elementor (couleurs, typo, responsive)

**Mots clés SEO** : TutorLMS Elementor, personnaliser pages cours Elementor, widgets TutorLMS Elementor, page builder LMS WordPress

---

### Leçon 12.6 : Divi

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Divi
**Source** : doc divi-integration

---

**[INTRO - face caméra]**

Divi est l'autre grand page builder de WordPress. Si c'est celui que tu utilises, TutorLMS propose une intégration dédiée avec des modules Divi pour personnaliser tes pages de cours. Le principe est le même qu'Elementor - éditeur visuel, drag-and-drop - mais avec l'écosystème Divi.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Divi Integration" dans Tutor LMS > Addons. Prérequis : Divi Builder doit être installé et actif - soit via le thème Divi, soit via le plugin Divi Builder standalone.

**[ÉCRAN - screencast Divi Builder]**

[Ouvre une page de cours avec le Divi Builder]

Ouvre une page de cours avec le Divi Builder. Dans la bibliothèque de modules, une nouvelle catégorie "Tutor LMS" apparaît avec des modules dédiés.

**[ÉCRAN - screencast modules Divi]**

[Montre les modules disponibles]

Les modules disponibles sont similaires aux widgets Elementor :
- Course Title, Course Thumbnail, Course Price
- Course Content, Course Curriculum
- Course Benefits, Course Requirements
- Enroll Button, Course Share
- Course Instructor, Course Reviews, Course Rating

Chaque module se configure avec les options Divi : design, spacing, animation, conditions d'affichage.

**[ÉCRAN - screencast template Divi]**

[Montre la création d'un template dans le Theme Builder Divi]

Comme avec Elementor, tu peux créer un template global dans le Divi Theme Builder. Va dans Divi > Theme Builder, ajoute un nouveau template, assigne-le aux pages de type "Course". Construis ton layout une fois, il s'applique partout.

**[ÉCRAN - screencast résultat front-end]**

[Montre le rendu final d'une page de cours personnalisée avec Divi]

Le résultat : une page de cours entièrement personnalisée, cohérente avec le reste de ton site Divi, sans une ligne de code.

**[TRANSITION - face caméra]**

Divi ou Elementor - c'est une question de préférence et d'écosystème. Si tu as déjà un site construit avec Divi, utilise l'intégration Divi. Ne change pas de page builder juste pour TutorLMS. Les deux intégrations couvrent les mêmes fonctionnalités.

---

**Points clés** :
- Addon "Divi Integration" à activer + Divi Builder installé
- Modules TutorLMS dans le Divi Builder (Title, Curriculum, Price, Reviews, etc.)
- Template global via Divi Theme Builder pour toutes les pages de cours
- Options de design Divi : spacing, animation, conditions d'affichage
- Même couverture fonctionnelle que l'intégration Elementor
- Choix du builder = préférence personnelle, pas de différence fonctionnelle

**Mots clés SEO** : TutorLMS Divi, intégration Divi LMS WordPress, personnaliser cours Divi Builder, modules TutorLMS Divi

---

### Leçon 12.7 : Oxygen Builder

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Oxygen
**Source** : doc oxygen-builder

---

**[INTRO - face caméra]**

Oxygen Builder, c'est le page builder des développeurs. Pas de thème, pas de bloat - tu construis tout de zéro avec un contrôle total sur le HTML et le CSS. Si c'est ton outil, TutorLMS le supporte. L'intégration est un peu différente d'Elementor ou Divi - Oxygen utilise des éléments spécifiques plutôt que des widgets. Voyons comment ça marche.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Oxygen Builder Integration" dans Tutor LMS > Addons. Oxygen Builder doit être installé et actif.

**[ÉCRAN - screencast Oxygen editor]**

[Ouvre une page de cours avec Oxygen]

Dans l'éditeur Oxygen, ouvre le panneau "Add" et cherche "Tutor". Tu trouves les éléments TutorLMS disponibles.

**[ÉCRAN - screencast éléments TutorLMS]**

[Montre les éléments dans le panneau Add]

Les éléments disponibles :
- Course Title, Course Thumbnail, Course Rating
- Course Content, Course Curriculum
- Course Enrollment Box - combine prix, bouton d'achat et infos clés
- Course Instructor, Course Reviews
- Course Meta - durée, nombre d'élèves, niveau

La différence avec Elementor et Divi : Oxygen te donne accès au CSS brut de chaque élément. Tu peux modifier chaque sélecteur, ajouter des classes personnalisées, écrire du CSS custom directement dans l'éditeur.

**[ÉCRAN - screencast template Oxygen]**

[Montre la création d'un template dans Oxygen]

Pour créer un template global, va dans Oxygen > Templates. Crée un nouveau template, assigne-le au type de post "courses". Construis ton layout avec les éléments TutorLMS. Tous tes cours utiliseront ce template.

**[ÉCRAN - screencast CSS custom]**

[Montre l'édition CSS sur un élément TutorLMS]

L'avantage Oxygen : tu peux aller plus loin que les options de style. Par exemple, modifier la grille du curriculum, ajouter des animations CSS, ou ajuster le responsive avec des media queries précises. C'est plus technique, mais le résultat est plus maîtrisé.

**[TRANSITION - face caméra]**

Oxygen Builder, c'est pour ceux qui veulent un contrôle total. Si tu es à l'aise avec le CSS et que tu veux un site léger sans la surcharge des gros page builders, c'est un excellent choix. Sinon, Elementor ou Divi seront plus accessibles.

---

**Points clés** :
- Addon "Oxygen Builder Integration" à activer + Oxygen installé
- Éléments TutorLMS dans le panneau Add d'Oxygen
- Accès direct au CSS de chaque élément (sélecteurs, classes custom)
- Template global dans Oxygen > Templates (type "courses")
- Plus technique qu'Elementor/Divi mais plus léger et plus contrôlable
- Pour les profils développeurs ou les sites où la performance est critique

**Mots clés SEO** : TutorLMS Oxygen Builder, intégration Oxygen LMS WordPress, personnaliser cours Oxygen, page builder léger LMS

---

### Leçon 12.8 : Droip

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Droip
**Source** : doc droip-integration

---

**[INTRO - face caméra]**

Droip, c'est le page builder développé par Themeum - la même équipe que TutorLMS. L'intégration est donc native et profonde. Si tu cherches un builder conçu spécifiquement pour fonctionner avec TutorLMS, sans problème de compatibilité, Droip est le candidat. Voyons ce qu'il propose.

**[ÉCRAN - screencast installation Droip]**

[Navigation vers Plugins > Add New > Droip]

Droip s'installe comme un plugin classique. Va dans Plugins, Add New, cherche "Droip" et installe-le. L'intégration TutorLMS est automatique - pas d'addon à activer. Droip détecte TutorLMS et ajoute les éléments de cours directement.

**[ÉCRAN - screencast Droip editor]**

[Ouvre une page de cours avec Droip]

L'éditeur Droip propose une catégorie "TutorLMS" avec tous les éléments de cours : titre, thumbnail, curriculum, prix, bouton d'inscription, avis, instructeur, méta-données. Le fonctionnement est similaire aux autres builders - drag-and-drop, options de style visuelles.

**[ÉCRAN - screencast avantage intégration native]**

[Montre les options spécifiques TutorLMS dans Droip]

L'avantage de l'intégration native : les éléments TutorLMS dans Droip sont plus détaillés que dans les autres builders. Par exemple, tu peux personnaliser individuellement chaque section du curriculum - leçons, quiz, assignments - avec des styles différents. Les mises à jour de TutorLMS et Droip sont synchronisées, donc moins de risques de conflit.

**[ÉCRAN - screencast template Droip]**

[Montre la création d'un template de page cours]

Pour le template global : Droip utilise le même système de templates que les autres builders. Crée un template, assigne-le aux cours, et tous tes cours adoptent le même design.

**[TRANSITION - face caméra]**

Droip est un choix cohérent si tu démarres un nouveau site et que TutorLMS est ta priorité. L'intégration native garantit la compatibilité à long terme. Mais si tu as déjà un site construit avec Elementor, Divi ou Oxygen, il n'y a aucune raison de migrer - les intégrations de ces builders sont tout aussi fonctionnelles.

---

**Points clés** :
- Pas d'addon à activer - intégration automatique (même éditeur : Themeum)
- Installation classique via Plugins > Add New
- Éléments TutorLMS plus détaillés que dans les autres builders
- Personnalisation granulaire du curriculum (leçons, quiz, assignments)
- Mises à jour synchronisées TutorLMS/Droip
- Bon choix pour un nouveau site centré sur TutorLMS
- Pas de raison de migrer si tu utilises déjà un autre builder

**Mots clés SEO** : TutorLMS Droip, Droip page builder, Themeum Droip intégration, personnaliser LMS Droip WordPress

---

### Leçon 12.9 : BunnyNet (vidéo hosting)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + BunnyNet
**Source** : doc bunnynet-integration

---

**[INTRO - face caméra]**

Héberger tes vidéos de cours sur ton serveur WordPress, c'est la pire idée possible. Ça ralentit ton site, ça consomme ta bande passante, et la qualité de lecture dépend de ton hébergeur. BunnyNet résout ce problème - c'est un CDN vidéo spécialisé, rapide, et bien moins cher que Vimeo ou Wistia. TutorLMS l'intègre nativement. Voyons comment configurer ça.

**[ÉCRAN - screencast BunnyNet dashboard]**

[Navigation vers dash.bunny.net > Stream > Video Library]

Première étape : crée un compte BunnyNet si ce n'est pas fait. Dans le dashboard, va dans Stream, puis "Add Video Library". Donne un nom à ta bibliothèque - par exemple "Cours TutorLMS".

Note le nom de ta Video Library et ton API Key. Tu les trouves dans Account Settings > API.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Côté TutorLMS, active l'addon "BunnyNet Integration" dans Addons.

**[ÉCRAN - screencast TutorLMS réglages BunnyNet]**

[Navigation vers Settings > BunnyNet]

Va dans Settings, BunnyNet. Remplis :
- API Key - ta clé API BunnyNet
- Library ID - l'identifiant de ta Video Library
- CDN Hostname - l'URL de ton CDN (fournie par BunnyNet)

Enregistre. La connexion est établie.

**[ÉCRAN - screencast upload vidéo]**

[Montre l'upload d'une vidéo dans une leçon]

Maintenant, quand tu ajoutes une vidéo à une leçon dans le Course Builder, une nouvelle option "BunnyNet" apparaît. Tu peux :
- Uploader une vidéo directement depuis TutorLMS vers BunnyNet
- Ou coller l'URL d'une vidéo déjà présente dans ta bibliothèque BunnyNet

La vidéo est encodée automatiquement en plusieurs résolutions - 360p, 720p, 1080p - et distribuée via le CDN mondial de BunnyNet.

**[ÉCRAN - screencast lecteur vidéo front-end]**

[Montre le rendu du player BunnyNet dans une leçon]

Côté élève : le lecteur vidéo est rapide, adaptatif (il ajuste la qualité selon la connexion) et ne porte pas le branding BunnyNet. Tes élèves ne voient pas la différence avec un player auto-hébergé - sauf que ça charge plus vite.

**[ÉCRAN - screencast tarification]**

[Slide récapitulatif des coûts BunnyNet]

Question coût : BunnyNet facture au stockage et à la bande passante. En moyenne, pour un site de formation avec 50 à 100 vidéos, compte environ 5 à 15 dollars par mois. C'est une fraction du coût de Vimeo Pro ou Wistia.

**[TRANSITION - face caméra]**

La recommandation schoolsWP : dès que tu as plus de 50 vidéos, utilise BunnyNet. En dessous, YouTube en non-listé ou Vimeo gratuit peuvent suffire - mais tu perds le contrôle sur le player et tu risques les pubs. BunnyNet, c'est le meilleur rapport qualité-prix pour l'hébergement vidéo LMS.

---

**Points clés** :
- Addon BunnyNet à activer + compte BunnyNet (dash.bunny.net)
- Configuration : API Key, Library ID, CDN Hostname
- Upload direct depuis TutorLMS ou lien vers vidéo existante
- Encodage automatique multi-résolution (360p, 720p, 1080p)
- CDN mondial = chargement rapide partout
- Coût moyen : 5-15$/mois pour 50-100 vidéos
- Recommandation schoolsWP : BunnyNet dès 50+ vidéos

**Mots clés SEO** : TutorLMS BunnyNet, hébergement vidéo LMS WordPress, BunnyNet CDN cours en ligne, vidéo hosting TutorLMS

---

### Leçon 12.10 : Easy Digital Downloads

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + EDD
**Source** : doc easy-digital-download

---

**[INTRO - face caméra]**

Easy Digital Downloads - EDD - c'est une alternative à WooCommerce spécialisée dans la vente de produits numériques. Si tu utilises déjà EDD pour vendre des ebooks, des templates ou des logiciels, tu peux l'utiliser comme moteur de paiement pour TutorLMS. Voyons comment.

**[ÉCRAN - screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > eCommerce Engine]

Pour activer EDD comme moteur de paiement, va dans Settings, Monetization, eCommerce Engine. Sélectionne "Easy Digital Downloads" dans la liste. Enregistre.

Prérequis : EDD doit être installé et actif, avec au moins une passerelle de paiement configurée (Stripe ou PayPal dans EDD).

**[ÉCRAN - screencast Course Builder avec EDD]**

[Montre la section Pricing avec EDD actif]

Dans le Course Builder, la section Pricing change. Tu vois un champ pour lier un produit EDD existant ou en créer un nouveau. Le prix se gère dans EDD, comme avec WooCommerce.

**[ÉCRAN - screencast création produit EDD]**

[Navigation vers Downloads > Add New]

Si tu crées manuellement : va dans Downloads, Add New. Donne un titre, définis le prix. Ensuite, dans le Course Builder TutorLMS, sélectionne ce produit. L'élève qui achète le "download" est automatiquement inscrit au cours.

**[ÉCRAN - screencast parcours d'achat]**

[Montre le checkout EDD côté élève]

Côté élève : le parcours d'achat passe par le checkout EDD. C'est plus léger que WooCommerce - EDD est conçu pour les produits numériques, donc pas de gestion d'expéditions, de stock ou de produits physiques.

**[TRANSITION - face caméra]**

EDD a du sens si c'est déjà ton outil de vente. Si tu pars de zéro, le eCommerce natif TutorLMS est plus simple. Et si tu as besoin de produits physiques en plus, WooCommerce reste le choix logique. EDD, c'est le choix de niche pour les vendeurs de produits 100% numériques.

---

**Points clés** :
- Activation : Settings > Monetization > eCommerce Engine > Easy Digital Downloads
- EDD doit être installé avec une passerelle de paiement active
- Chaque cours lié à un produit EDD (création manuelle ou automatique)
- Checkout EDD plus léger que WooCommerce (pas de gestion physique)
- Inscription automatique au cours après achat du "download"
- Utile si tu vends déjà des produits numériques avec EDD
- Recommandation : eCommerce natif si tu démarres, EDD si c'est déjà en place

**Mots clés SEO** : TutorLMS Easy Digital Downloads, EDD LMS WordPress, vendre cours EDD, intégration EDD TutorLMS

---

### Leçon 12.11 : Loco Translate

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Loco Translate
**Source** : doc loco-translate

---

**[INTRO - face caméra]**

TutorLMS est en anglais par défaut. Même si WordPress est en français, certaines chaînes de texte de TutorLMS restent en anglais - boutons, labels, messages système. Loco Translate permet de tout traduire directement depuis l'admin WordPress, sans toucher aux fichiers de traduction manuellement. Voyons comment faire.

**[ÉCRAN - screencast installation Loco Translate]**

[Navigation vers Plugins > Add New > Loco Translate]

Installe et active Loco Translate depuis Plugins > Add New. C'est un plugin gratuit.

**[ÉCRAN - screencast interface Loco Translate]**

[Navigation vers Loco Translate > Plugins > TutorLMS]

Va dans Loco Translate, puis Plugins. Tu vois la liste de tous tes plugins. Clique sur "Tutor LMS". Tu vois les langues disponibles. Si le français n'apparaît pas, clique sur "New language", sélectionne "French (France)" et choisis l'emplacement "Custom" - ça évite que tes traductions soient écrasées lors des mises à jour.

**[ÉCRAN - screencast traduction d'une chaîne]**

[Montre l'éditeur de traduction]

L'éditeur affiche deux colonnes : la chaîne source en anglais à gauche, ta traduction à droite. Par exemple :
- "Enroll Now" → "S'inscrire"
- "Course Content" → "Contenu du cours"
- "Complete Lesson" → "Terminer la leçon"
- "Start Quiz" → "Démarrer le quiz"

Tu cliques sur une chaîne, tu tapes ta traduction, tu passes à la suivante. Quand tu as fini, clique sur "Save". Les modifications s'appliquent immédiatement sur ton site.

**[ÉCRAN - screencast recherche de chaîne]**

[Montre la barre de recherche dans Loco Translate]

L'astuce pour aller vite : utilise la barre de recherche. Tu vois un texte en anglais sur ton site ? Copie-le, colle-le dans la recherche Loco Translate, et tu trouves la chaîne à traduire en quelques secondes.

**[ÉCRAN - screencast Tutor LMS Pro]**

[Montre qu'il faut aussi traduire Tutor LMS Pro séparément]

Point important : si tu utilises Tutor LMS Pro, c'est un plugin séparé. Tu dois aussi le traduire dans Loco Translate - les chaînes ne sont pas les mêmes que la version gratuite. Même chose pour les addons actifs - chacun a ses propres chaînes.

**[ÉCRAN - screencast résultat front-end]**

[Montre le site en français après traduction]

Le résultat : un site entièrement en français, y compris les éléments de TutorLMS que la traduction officielle ne couvrait pas.

**[TRANSITION - face caméra]**

La traduction complète de TutorLMS prend environ 30 minutes avec Loco Translate. Fais-le une fois, et c'est réglé. Pense à revérifier après chaque mise à jour majeure de TutorLMS - de nouvelles chaînes peuvent apparaître. C'est la dernière leçon de contenu de ce module. On termine avec le quiz.

---

**Points clés** :
- Loco Translate : plugin gratuit, traduction depuis l'admin WordPress
- Navigation : Loco Translate > Plugins > Tutor LMS
- Choisir l'emplacement "Custom" pour protéger les traductions des mises à jour
- Éditeur deux colonnes : source anglais / traduction français
- Barre de recherche pour trouver une chaîne rapidement
- Traduire séparément : Tutor LMS, Tutor LMS Pro, et chaque addon actif
- Revérifier après les mises à jour majeures (nouvelles chaînes possibles)

**Mots clés SEO** : TutorLMS français, traduire TutorLMS, Loco Translate TutorLMS, TutorLMS traduction française WordPress

---

### Leçon 12.12 : Quiz Module 12

**Durée** : ~5 min (10 questions)
**Type** : Quiz TutorLMS
**Seuil de réussite** : 70%

---

**Question 1**
Quel est le moyen le plus simple de donner des cours en direct avec TutorLMS ?

- A) Zoom - c'est le plus connu
- B) Google Meet - gratuit, natif et sans installation côté élève ✓
- C) Microsoft Teams via un plugin tiers
- D) YouTube Live via embed

**Explication** : Google Meet est gratuit, intégré nativement dans TutorLMS, et fonctionne dans le navigateur sans rien installer.

---

**Question 2**
Quelle est la principale différence entre la configuration Google Meet et Zoom dans TutorLMS ?

- A) Google Meet utilise OAuth 2.0, Zoom utilise Server-to-Server OAuth via le Marketplace ✓
- B) Google Meet est payant, Zoom est gratuit
- C) Google Meet nécessite un plugin tiers, Zoom est natif
- D) Il n'y a pas de différence

**Explication** : Google Meet se configure via la Google Cloud Console (OAuth 2.0), tandis que Zoom nécessite une app Server-to-Server OAuth créée sur marketplace.zoom.us.

---

**Question 3**
Dans quel cas WooCommerce est-il préférable au eCommerce natif de TutorLMS ?

- A) Toujours - WooCommerce est plus fiable
- B) Quand tu vends aussi des produits physiques ou que tu as besoin d'extensions WooCommerce spécifiques ✓
- C) Quand tu as moins de 10 cours
- D) Quand tu utilises Stripe

**Explication** : WooCommerce a du sens si tu vends déjà d'autres produits ou si tu as besoin d'extensions spécifiques (factures avancées, taxes multi-pays). Sinon, le eCommerce natif est plus simple.

---

**Question 4**
Quel page builder est développé par la même équipe que TutorLMS ?

- A) Elementor
- B) Divi
- C) Oxygen Builder
- D) Droip ✓

**Explication** : Droip est développé par Themeum, la même équipe que TutorLMS. L'intégration est automatique - pas d'addon à activer.

---

**Question 5**
Qu'est-ce qui distingue Oxygen Builder des autres page builders pour TutorLMS ?

- A) Il est gratuit
- B) Il donne accès direct au CSS brut de chaque élément ✓
- C) Il a plus de widgets que les autres
- D) Il est le seul compatible avec TutorLMS Pro

**Explication** : Oxygen Builder permet de modifier le CSS brut de chaque élément, d'ajouter des classes personnalisées et d'écrire du CSS custom directement dans l'éditeur.

---

**Question 6**
À partir de combien de vidéos schoolsWP recommande-t-il d'utiliser BunnyNet ?

- A) 10 vidéos
- B) 25 vidéos
- C) 50 vidéos ✓
- D) 100 vidéos

**Explication** : La recommandation schoolsWP est d'utiliser BunnyNet dès 50 vidéos. En dessous, YouTube non-listé ou Vimeo gratuit peuvent suffire.

---

**Question 7**
Quel est le coût moyen de BunnyNet pour un site de formation avec 50 à 100 vidéos ?

- A) Gratuit
- B) 5 à 15 dollars par mois ✓
- C) 50 à 100 dollars par mois
- D) 200+ dollars par mois

**Explication** : BunnyNet facture au stockage et à la bande passante. Pour 50 à 100 vidéos, le coût moyen est de 5 à 15 dollars par mois.

---

**Question 8**
Pourquoi choisir l'emplacement "Custom" dans Loco Translate pour les traductions TutorLMS ?

- A) Les traductions sont plus rapides
- B) Ça permet de traduire plus de langues
- C) Ça évite que les traductions soient écrasées lors des mises à jour ✓
- D) C'est le seul emplacement disponible

**Explication** : L'emplacement "Custom" stocke les traductions dans un fichier séparé qui n'est pas écrasé quand TutorLMS est mis à jour.

---

**Question 9**
Quelle est la particularité de Easy Digital Downloads par rapport à WooCommerce pour TutorLMS ?

- A) EDD est gratuit, WooCommerce est payant
- B) EDD est spécialisé produits numériques - pas de gestion physique - donc plus léger ✓
- C) EDD supporte plus de passerelles de paiement
- D) EDD est plus rapide

**Explication** : EDD est conçu pour les produits 100% numériques. Il n'a pas de gestion d'expéditions, de stock ou de produits physiques, ce qui le rend plus léger que WooCommerce.

---

**Question 10**
Quand tu traduis TutorLMS avec Loco Translate, combien de plugins dois-tu traduire si tu utilises Tutor LMS Pro avec des addons ?

- A) Un seul - Tutor LMS
- B) Deux - Tutor LMS et Tutor LMS Pro
- C) Tutor LMS + Tutor LMS Pro + chaque addon actif séparément ✓
- D) Aucun - la traduction officielle couvre tout

**Explication** : Tutor LMS, Tutor LMS Pro et chaque addon actif ont leurs propres chaînes de texte. Il faut les traduire séparément dans Loco Translate.

---

**Fin du Module 12 - Intégrations tierces**

Résumé du module :
- Cours en direct : Google Meet (recommandé, gratuit) ou Zoom (si déjà utilisé)
- Google Classroom : pont vers l'écosystème Google Education
- eCommerce : natif (recommandé) > WooCommerce (si produits mixtes) > EDD (si niche numérique)
- Page builders : Elementor, Divi, Oxygen, Droip - choisir celui déjà en place
- Vidéo hosting : BunnyNet recommandé dès 50+ vidéos (5-15$/mois)
- Traduction : Loco Translate pour franciser complètement l'interface

Durée totale estimée du module : ~55 minutes

# Scripts video — Module 12 : Integrations tierces

**Formation** : Maitriser TutorLMS
**Module** : M12 — Integrations tierces (Premium)
**Lecons** : 11 videos + 1 quiz
**Duree totale** : ~55 min
**Date** : 2026-03-23

---

### Lecon 12.1 — Google Meet (cours en direct)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Google Meet
**Source** : Video #17 + doc google-meet-integration

---

**[INTRO — face camera]**

Tu veux donner des cours en direct a tes eleves ? Google Meet est la solution la plus simple — et la plus economique. C'est gratuit avec un compte Google, integre nativement dans TutorLMS, et tes eleves n'ont rien a installer. Dans cette lecon, on connecte Google Meet a TutorLMS et on planifie un premier cours en direct.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Premiere etape : active l'addon Google Meet. Va dans Tutor LMS, puis Addons. Cherche "Google Meet Integration" et active-le avec le toggle.

**[ECRAN — screencast Google Cloud Console]**

[Navigation vers console.cloud.google.com > APIs & Services > Credentials]

Maintenant, il faut connecter ton compte Google. Ca passe par la Google Cloud Console. Connecte-toi, cree un projet si tu n'en as pas, puis va dans APIs & Services, Credentials.

Clique sur "Create Credentials", puis "OAuth 2.0 Client ID". Selectionne "Web application". Dans les URIs de redirection autorises, ajoute l'URL que TutorLMS t'affiche dans ses reglages Google Meet.

Tu obtiens un Client ID et un Client Secret. Copie-les.

**[ECRAN — screencast TutorLMS reglages Google Meet]**

[Navigation vers Tutor LMS > Settings > Google Meet]

Retourne dans TutorLMS, Settings, Google Meet. Colle le Client ID et le Client Secret. Clique sur "Generate token" — ca ouvre une fenetre d'autorisation Google. Accepte, et le token est genere. La connexion est etablie.

**[ECRAN — screencast Course Builder]**

[Navigation vers un cours > onglet Google Meet]

Pour planifier un cours en direct, ouvre le Course Builder d'un cours. Tu trouves un nouvel onglet "Google Meet". Clique dessus, puis "Create a meeting".

Remplis :
- Le titre du meeting
- La date et l'heure de debut
- La duree
- Le fuseau horaire

Tu peux aussi activer l'enregistrement automatique — la session sera enregistree dans Google Drive.

**[ECRAN — screencast front-end eleve]**

[Montre la page cours cote eleve avec le meeting planifie]

Cote eleve : le meeting apparait dans le curriculum du cours avec la date et l'heure. Quand l'heure arrive, un bouton "Join Meeting" s'affiche. L'eleve clique et rejoint directement le meeting dans son navigateur.

**[TRANSITION — face camera]**

La recommandation schoolsWP : Google Meet est le meilleur choix pour les cours en direct. C'est gratuit, ca fonctionne dans le navigateur, et l'integration TutorLMS est native. Zoom est une alternative si tes eleves l'utilisent deja — on le voit dans la lecon 12.3. Mais si tu pars de zero, reste sur Google Meet.

---

**Points cles** :
- Addon Google Meet a activer dans Tutor LMS > Addons
- Connexion via Google Cloud Console (OAuth 2.0 Client ID + Secret)
- Planning des meetings dans le Course Builder, onglet Google Meet
- Enregistrement automatique disponible (stocke dans Google Drive)
- Cote eleve : bouton "Join Meeting" directement dans le curriculum
- Recommandation schoolsWP : Google Meet (gratuit) > Zoom (payant)

**Mots cles SEO** : TutorLMS Google Meet, cours en direct TutorLMS, visioconference LMS WordPress, Google Meet integration TutorLMS

---

### Lecon 12.2 — Google Classroom

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Google Classroom
**Source** : Video #29 + doc google-classroom

---

**[INTRO — face camera]**

Google Classroom, c'est l'outil de Google pour gerer des classes en ligne. Si tes eleves sont dans un contexte scolaire ou universitaire, ou si ton etablissement utilise deja Google Workspace, cette integration a du sens. TutorLMS peut synchroniser tes cours avec Google Classroom — tes eleves retrouvent tout dans leur environnement habituel.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Google Classroom Integration" dans Tutor LMS > Addons. Le toggle, comme d'habitude.

**[ECRAN — screencast Google Cloud Console]**

[Navigation vers APIs & Services > Library > Google Classroom API]

Dans la Google Cloud Console, active l'API Google Classroom. Va dans APIs & Services, Library, cherche "Google Classroom API" et active-la. Si tu as deja configure Google Meet, tu peux utiliser le meme projet.

Ensuite, va dans Credentials et cree un nouvel OAuth 2.0 Client ID — ou reutilise celui de Google Meet si l'URI de redirection est la meme.

**[ECRAN — screencast TutorLMS reglages Google Classroom]**

[Navigation vers Tutor LMS > Settings > Google Classroom]

Dans TutorLMS, Settings, Google Classroom. Colle le Client ID et le Client Secret. Genere le token comme pour Google Meet.

**[ECRAN — screencast creation d'un classroom]**

[Montre la creation d'un classroom depuis le Course Builder]

Pour lier un cours a Google Classroom, ouvre le Course Builder. Un nouvel onglet "Google Classroom" apparait. Tu peux :
- Creer un nouveau classroom directement depuis TutorLMS
- Ou lier un classroom existant

Quand tu crees un classroom, TutorLMS genere automatiquement un code d'invitation que tes eleves utilisent pour rejoindre la classe dans Google Classroom.

**[ECRAN — screencast synchronisation]**

[Montre la synchro des devoirs et du materiel]

La synchronisation fonctionne dans les deux sens :
- Les contenus de cours TutorLMS apparaissent comme materiel dans Google Classroom
- Les devoirs et notes peuvent etre geres depuis l'interface Google

C'est pratique pour les formateurs qui ont des eleves habitues a Google Classroom mais qui veulent la puissance de TutorLMS pour la structure des cours.

**[TRANSITION — face camera]**

Google Classroom, c'est un pont entre TutorLMS et l'ecosysteme Google Education. Si tes eleves sont deja dans cet ecosysteme, l'integration evite de leur imposer un changement d'habitude. Si ce n'est pas le cas, TutorLMS seul couvre tous les besoins.

---

**Points cles** :
- Addon Google Classroom a activer dans Addons
- Necessite l'API Google Classroom activee dans Google Cloud Console
- Meme processus OAuth que Google Meet (Client ID + Secret + token)
- Creation de classroom depuis le Course Builder ou liaison avec un existant
- Code d'invitation genere automatiquement
- Synchronisation bidirectionnelle (contenus + devoirs)
- Utile surtout dans un contexte scolaire/universitaire avec Google Workspace

**Mots cles SEO** : TutorLMS Google Classroom, integration Google Classroom WordPress, LMS Google Education, synchroniser cours Google Classroom

---

### Lecon 12.3 — Zoom (cours en direct)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Zoom
**Source** : doc zoom-integration

---

**[INTRO — face camera]**

Zoom est l'autre option pour les cours en direct dans TutorLMS. Si tes eleves utilisent deja Zoom ou si ton organisation a un compte Zoom Pro, cette integration est pertinente. La mise en place est un peu plus longue que Google Meet, et Zoom est payant pour les sessions de plus de 40 minutes. Voyons comment le configurer.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Zoom Integration" dans Tutor LMS > Addons.

**[ECRAN — screencast Zoom Marketplace]**

[Navigation vers marketplace.zoom.us]

Contrairement a Google Meet, Zoom utilise une app dediee. Va sur marketplace.zoom.us, connecte-toi avec ton compte Zoom. Clique sur "Develop", puis "Build App". Selectionne "Server-to-Server OAuth".

Donne un nom a ton app — par exemple "TutorLMS Integration". Zoom te fournit :
- Un Account ID
- Un Client ID
- Un Client Secret

Copie ces trois valeurs.

**[ECRAN — screencast permissions Zoom]**

[Montre l'onglet Scopes de l'app Zoom]

Dans l'onglet Scopes de ton app Zoom, ajoute les permissions necessaires :
- meeting:write:admin — pour creer des meetings
- meeting:read:admin — pour lire les meetings
- user:read:admin — pour acceder aux infos utilisateur

Active l'app une fois les scopes configures.

**[ECRAN — screencast TutorLMS reglages Zoom]**

[Navigation vers Tutor LMS > Settings > Zoom]

Retourne dans TutorLMS, Settings, Zoom. Colle l'Account ID, le Client ID et le Client Secret. Enregistre. La connexion est etablie si les champs deviennent verts.

**[ECRAN — screencast planification meeting]**

[Navigation vers Course Builder > onglet Zoom]

La planification fonctionne comme Google Meet. Dans le Course Builder, onglet Zoom, clique sur "Create a Zoom Meeting". Remplis le titre, la date, la duree. Tu peux aussi configurer :
- Le mot de passe du meeting
- La salle d'attente
- L'enregistrement automatique (cloud si Zoom Pro, local sinon)

**[ECRAN — screencast front-end eleve]**

[Montre le bouton "Join with Zoom" cote eleve]

Cote eleve : un bouton "Join with Zoom" apparait dans le curriculum. L'eleve clique et rejoint le meeting — soit dans l'app Zoom, soit dans le navigateur.

**[TRANSITION — face camera]**

Zoom fonctionne bien mais a deux inconvenients : la limite de 40 minutes en version gratuite et la configuration plus complexe via le Marketplace. Si tu n'as pas de raison specifique d'utiliser Zoom, Google Meet est le choix le plus simple. Si ton organisation impose Zoom, cette integration fait le travail.

---

**Points cles** :
- Addon Zoom a activer dans Addons
- Configuration via marketplace.zoom.us (Server-to-Server OAuth)
- 3 identifiants : Account ID, Client ID, Client Secret
- Scopes requis : meeting:write:admin, meeting:read:admin, user:read:admin
- Planning dans le Course Builder, onglet Zoom
- Options : mot de passe, salle d'attente, enregistrement
- Limite : 40 min en version gratuite, configuration plus longue que Google Meet
- Recommandation schoolsWP : Google Meet (gratuit) sauf si Zoom est impose

**Mots cles SEO** : TutorLMS Zoom integration, cours en direct Zoom WordPress, visioconference Zoom LMS, TutorLMS Zoom configuration

---

### Lecon 12.4 — WooCommerce

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + WooCommerce
**Source** : doc woocommerce

---

**[INTRO — face camera]**

WooCommerce etait le seul moyen de vendre des cours avec TutorLMS avant la v3. Depuis, le eCommerce natif le remplace dans la majorite des cas — on l'a vu dans le module 8. Mais WooCommerce reste utile dans deux situations : si tu vends deja d'autres produits avec WooCommerce, ou si tu as besoin d'extensions WooCommerce specifiques comme les factures avancees ou les taxes multi-pays. Voyons comment ca fonctionne.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > eCommerce Engine]

Pour utiliser WooCommerce comme moteur de paiement, va dans Settings, Monetization, eCommerce Engine. Selectionne "WooCommerce" au lieu de "Native". Enregistre.

Prerequis : WooCommerce doit etre installe et active sur ton site.

**[ECRAN — screencast creation produit WooCommerce]**

[Navigation vers Products > Add New]

Quand WooCommerce est actif comme moteur, chaque cours TutorLMS a besoin d'un produit WooCommerce associe. Tu peux le creer de deux facons :
- Automatiquement — TutorLMS cree le produit quand tu definis un prix dans le Course Builder
- Manuellement — tu crees un produit WooCommerce et tu le lies au cours

**[ECRAN — screencast Course Builder pricing]**

[Montre la section Pricing avec WooCommerce actif]

Dans le Course Builder, la section Pricing change quand WooCommerce est actif. Tu vois un champ pour lier un produit WooCommerce existant ou en creer un nouveau. Le prix, les promotions et les options d'abonnement se gerent dans WooCommerce, pas dans TutorLMS.

**[ECRAN — screencast checkout WooCommerce]**

[Montre le parcours d'achat cote eleve]

Cote eleve : le parcours d'achat passe par le panier et le checkout WooCommerce classique. Toutes les passerelles de paiement configurees dans WooCommerce sont disponibles. Apres le paiement, l'eleve est automatiquement inscrit au cours.

**[ECRAN — screencast avantages WooCommerce]**

[Slide recapitulatif]

Les cas ou WooCommerce a du sens :
- Tu vends des produits physiques ou digitaux en plus des cours
- Tu utilises des extensions WooCommerce specifiques (factures, taxes, abonnements avances)
- Tu as deja un catalogue WooCommerce et tu ne veux pas migrer

Les cas ou le eCommerce natif est meilleur :
- Tu vends uniquement des cours
- Tu veux une configuration simple
- Tu debutees et tu n'as pas d'historique WooCommerce

**[TRANSITION — face camera]**

La recommandation schoolsWP : si tu demarres de zero, utilise le eCommerce natif. WooCommerce ajoute de la complexite et de la charge sur ton serveur. Ne l'utilise que si tu as une raison concrete — pas par habitude.

---

**Points cles** :
- Activation : Settings > Monetization > eCommerce Engine > WooCommerce
- WooCommerce doit etre installe et actif
- Chaque cours necessite un produit WooCommerce associe
- Prix et abonnements geres dans WooCommerce, pas dans TutorLMS
- Checkout WooCommerce classique (panier + paiement)
- Utile si tu vends deja d'autres produits ou si tu as besoin d'extensions specifiques
- Recommandation schoolsWP : eCommerce natif sauf besoin specifique WooCommerce

**Mots cles SEO** : TutorLMS WooCommerce, vendre cours WooCommerce, WooCommerce vs eCommerce natif TutorLMS, integration WooCommerce LMS

---

### Lecon 12.5 — Elementor

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Elementor
**Source** : doc elementor-integration

---

**[INTRO — face camera]**

Elementor est le page builder le plus utilise sur WordPress. Si c'est celui que tu utilises pour ton site, bonne nouvelle : TutorLMS s'integre avec. Tu peux personnaliser les pages de cours, le catalogue, le dashboard eleve — tout ca avec l'editeur visuel d'Elementor. Voyons comment activer l'integration et quels widgets sont disponibles.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Elementor Addons" dans Tutor LMS > Addons. Prerequis : Elementor (version gratuite ou Pro) doit etre installe et actif.

**[ECRAN — screencast Elementor editor]**

[Ouvre une page de cours avec Elementor]

Une fois l'addon actif, edite une page de cours avec Elementor. Dans le panneau de widgets, une nouvelle categorie "Tutor LMS" apparait. Tu y trouves plus de 25 widgets dedies.

**[ECRAN — screencast widgets principaux]**

[Montre les widgets dans le panneau Elementor]

Les widgets les plus utiles :

- Course Title, Course Thumbnail, Course Rating — les bases de toute page de cours
- Course Curriculum — affiche le contenu structure du cours
- Course Benefits, Course Requirements — les listes "ce que tu vas apprendre" et "prerequis"
- Add to Cart / Enroll Button — le bouton d'achat ou d'inscription
- Course Instructor — affiche le profil de l'instructeur
- Course Reviews — les avis des eleves

Tu glisses-deposes ces widgets comme n'importe quel widget Elementor et tu les stylises avec les options habituelles : couleurs, typographie, espacement, responsive.

**[ECRAN — screencast template de page cours]**

[Montre la creation d'un template Elementor pour les pages de cours]

Le plus puissant : tu peux creer un template Elementor pour toutes tes pages de cours. Va dans Templates > Theme Builder > Single Course. Construis ton layout une fois, et il s'applique a tous tes cours automatiquement.

**[ECRAN — screencast dashboard eleve]**

[Montre la personnalisation du dashboard avec Elementor]

Tu peux aussi personnaliser le dashboard eleve avec Elementor. Les widgets disponibles : Course List, Course Progress, Profile Info, Enrolled Courses. Ca te permet de creer un espace eleve qui correspond a l'identite visuelle de ton site.

**[TRANSITION — face camera]**

Si tu utilises deja Elementor, cette integration est un must. Tu gardes le controle total sur le design sans toucher au code. Si tu n'utilises pas encore de page builder, on voit Divi, Oxygen et Droip dans les prochaines lecons — choisis celui qui correspond a ton workflow.

---

**Points cles** :
- Addon "Elementor Addons" a activer + Elementor installe
- 25+ widgets TutorLMS dans l'editeur Elementor
- Widgets principaux : Title, Curriculum, Benefits, Add to Cart, Reviews, Instructor
- Template Theme Builder pour appliquer un layout a toutes les pages de cours
- Dashboard eleve personnalisable avec Elementor
- Drag-and-drop + options de style Elementor (couleurs, typo, responsive)

**Mots cles SEO** : TutorLMS Elementor, personnaliser pages cours Elementor, widgets TutorLMS Elementor, page builder LMS WordPress

---

### Lecon 12.6 — Divi

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Divi
**Source** : doc divi-integration

---

**[INTRO — face camera]**

Divi est l'autre grand page builder de WordPress. Si c'est celui que tu utilises, TutorLMS propose une integration dediee avec des modules Divi pour personnaliser tes pages de cours. Le principe est le meme qu'Elementor — editeur visuel, drag-and-drop — mais avec l'ecosysteme Divi.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Divi Integration" dans Tutor LMS > Addons. Prerequis : Divi Builder doit etre installe et actif — soit via le theme Divi, soit via le plugin Divi Builder standalone.

**[ECRAN — screencast Divi Builder]**

[Ouvre une page de cours avec le Divi Builder]

Ouvre une page de cours avec le Divi Builder. Dans la bibliotheque de modules, une nouvelle categorie "Tutor LMS" apparait avec des modules dedies.

**[ECRAN — screencast modules Divi]**

[Montre les modules disponibles]

Les modules disponibles sont similaires aux widgets Elementor :
- Course Title, Course Thumbnail, Course Price
- Course Content, Course Curriculum
- Course Benefits, Course Requirements
- Enroll Button, Course Share
- Course Instructor, Course Reviews, Course Rating

Chaque module se configure avec les options Divi : design, spacing, animation, conditions d'affichage.

**[ECRAN — screencast template Divi]**

[Montre la creation d'un template dans le Theme Builder Divi]

Comme avec Elementor, tu peux creer un template global dans le Divi Theme Builder. Va dans Divi > Theme Builder, ajoute un nouveau template, assigne-le aux pages de type "Course". Construis ton layout une fois, il s'applique partout.

**[ECRAN — screencast resultat front-end]**

[Montre le rendu final d'une page de cours personnalisee avec Divi]

Le resultat : une page de cours entierement personnalisee, coherente avec le reste de ton site Divi, sans une ligne de code.

**[TRANSITION — face camera]**

Divi ou Elementor — c'est une question de preference et d'ecosysteme. Si tu as deja un site construit avec Divi, utilise l'integration Divi. Ne change pas de page builder juste pour TutorLMS. Les deux integrations couvrent les memes fonctionnalites.

---

**Points cles** :
- Addon "Divi Integration" a activer + Divi Builder installe
- Modules TutorLMS dans le Divi Builder (Title, Curriculum, Price, Reviews, etc.)
- Template global via Divi Theme Builder pour toutes les pages de cours
- Options de design Divi : spacing, animation, conditions d'affichage
- Meme couverture fonctionnelle que l'integration Elementor
- Choix du builder = preference personnelle, pas de difference fonctionnelle

**Mots cles SEO** : TutorLMS Divi, integration Divi LMS WordPress, personnaliser cours Divi Builder, modules TutorLMS Divi

---

### Lecon 12.7 — Oxygen Builder

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Oxygen
**Source** : doc oxygen-builder

---

**[INTRO — face camera]**

Oxygen Builder, c'est le page builder des developpeurs. Pas de theme, pas de bloat — tu construis tout de zero avec un controle total sur le HTML et le CSS. Si c'est ton outil, TutorLMS le supporte. L'integration est un peu differente d'Elementor ou Divi — Oxygen utilise des elements specifiques plutot que des widgets. Voyons comment ca marche.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Active l'addon "Oxygen Builder Integration" dans Tutor LMS > Addons. Oxygen Builder doit etre installe et actif.

**[ECRAN — screencast Oxygen editor]**

[Ouvre une page de cours avec Oxygen]

Dans l'editeur Oxygen, ouvre le panneau "Add" et cherche "Tutor". Tu trouves les elements TutorLMS disponibles.

**[ECRAN — screencast elements TutorLMS]**

[Montre les elements dans le panneau Add]

Les elements disponibles :
- Course Title, Course Thumbnail, Course Rating
- Course Content, Course Curriculum
- Course Enrollment Box — combine prix, bouton d'achat et infos cles
- Course Instructor, Course Reviews
- Course Meta — duree, nombre d'eleves, niveau

La difference avec Elementor et Divi : Oxygen te donne acces au CSS brut de chaque element. Tu peux modifier chaque selecteur, ajouter des classes personnalisees, ecrire du CSS custom directement dans l'editeur.

**[ECRAN — screencast template Oxygen]**

[Montre la creation d'un template dans Oxygen]

Pour creer un template global, va dans Oxygen > Templates. Cree un nouveau template, assigne-le au type de post "courses". Construis ton layout avec les elements TutorLMS. Tous tes cours utiliseront ce template.

**[ECRAN — screencast CSS custom]**

[Montre l'edition CSS sur un element TutorLMS]

L'avantage Oxygen : tu peux aller plus loin que les options de style. Par exemple, modifier la grille du curriculum, ajouter des animations CSS, ou ajuster le responsive avec des media queries precises. C'est plus technique, mais le resultat est plus maitrise.

**[TRANSITION — face camera]**

Oxygen Builder, c'est pour ceux qui veulent un controle total. Si tu es a l'aise avec le CSS et que tu veux un site leger sans la surcharge des gros page builders, c'est un excellent choix. Sinon, Elementor ou Divi seront plus accessibles.

---

**Points cles** :
- Addon "Oxygen Builder Integration" a activer + Oxygen installe
- Elements TutorLMS dans le panneau Add d'Oxygen
- Acces direct au CSS de chaque element (selecteurs, classes custom)
- Template global dans Oxygen > Templates (type "courses")
- Plus technique qu'Elementor/Divi mais plus leger et plus controlable
- Pour les profils developpeurs ou les sites ou la performance est critique

**Mots cles SEO** : TutorLMS Oxygen Builder, integration Oxygen LMS WordPress, personnaliser cours Oxygen, page builder leger LMS

---

### Lecon 12.8 — Droip

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Droip
**Source** : doc droip-integration

---

**[INTRO — face camera]**

Droip, c'est le page builder developpe par Themeum — la meme equipe que TutorLMS. L'integration est donc native et profonde. Si tu cherches un builder concu specifiquement pour fonctionner avec TutorLMS, sans probleme de compatibilite, Droip est le candidat. Voyons ce qu'il propose.

**[ECRAN — screencast installation Droip]**

[Navigation vers Plugins > Add New > Droip]

Droip s'installe comme un plugin classique. Va dans Plugins, Add New, cherche "Droip" et installe-le. L'integration TutorLMS est automatique — pas d'addon a activer. Droip detecte TutorLMS et ajoute les elements de cours directement.

**[ECRAN — screencast Droip editor]**

[Ouvre une page de cours avec Droip]

L'editeur Droip propose une categorie "TutorLMS" avec tous les elements de cours : titre, thumbnail, curriculum, prix, bouton d'inscription, avis, instructeur, meta-donnees. Le fonctionnement est similaire aux autres builders — drag-and-drop, options de style visuelles.

**[ECRAN — screencast avantage integration native]**

[Montre les options specifiques TutorLMS dans Droip]

L'avantage de l'integration native : les elements TutorLMS dans Droip sont plus detailles que dans les autres builders. Par exemple, tu peux personnaliser individuellement chaque section du curriculum — lecons, quiz, assignments — avec des styles differents. Les mises a jour de TutorLMS et Droip sont synchronisees, donc moins de risques de conflit.

**[ECRAN — screencast template Droip]**

[Montre la creation d'un template de page cours]

Pour le template global : Droip utilise le meme systeme de templates que les autres builders. Cree un template, assigne-le aux cours, et tous tes cours adoptent le meme design.

**[TRANSITION — face camera]**

Droip est un choix coherent si tu demarres un nouveau site et que TutorLMS est ta priorite. L'integration native garantit la compatibilite a long terme. Mais si tu as deja un site construit avec Elementor, Divi ou Oxygen, il n'y a aucune raison de migrer — les integrations de ces builders sont tout aussi fonctionnelles.

---

**Points cles** :
- Pas d'addon a activer — integration automatique (meme editeur : Themeum)
- Installation classique via Plugins > Add New
- Elements TutorLMS plus detailles que dans les autres builders
- Personnalisation granulaire du curriculum (lecons, quiz, assignments)
- Mises a jour synchronisees TutorLMS/Droip
- Bon choix pour un nouveau site centre sur TutorLMS
- Pas de raison de migrer si tu utilises deja un autre builder

**Mots cles SEO** : TutorLMS Droip, Droip page builder, Themeum Droip integration, personnaliser LMS Droip WordPress

---

### Lecon 12.9 — BunnyNet (video hosting)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + BunnyNet
**Source** : doc bunnynet-integration

---

**[INTRO — face camera]**

Heberger tes videos de cours sur ton serveur WordPress, c'est la pire idee possible. Ca ralentit ton site, ca consomme ta bande passante, et la qualite de lecture depend de ton hebergeur. BunnyNet resout ce probleme — c'est un CDN video specialise, rapide, et bien moins cher que Vimeo ou Wistia. TutorLMS l'integre nativement. Voyons comment configurer ca.

**[ECRAN — screencast BunnyNet dashboard]**

[Navigation vers dash.bunny.net > Stream > Video Library]

Premiere etape : cree un compte BunnyNet si ce n'est pas fait. Dans le dashboard, va dans Stream, puis "Add Video Library". Donne un nom a ta bibliotheque — par exemple "Cours TutorLMS".

Note le nom de ta Video Library et ton API Key. Tu les trouves dans Account Settings > API.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Addons]

Cote TutorLMS, active l'addon "BunnyNet Integration" dans Addons.

**[ECRAN — screencast TutorLMS reglages BunnyNet]**

[Navigation vers Settings > BunnyNet]

Va dans Settings, BunnyNet. Remplis :
- API Key — ta cle API BunnyNet
- Library ID — l'identifiant de ta Video Library
- CDN Hostname — l'URL de ton CDN (fournie par BunnyNet)

Enregistre. La connexion est etablie.

**[ECRAN — screencast upload video]**

[Montre l'upload d'une video dans une lecon]

Maintenant, quand tu ajoutes une video a une lecon dans le Course Builder, une nouvelle option "BunnyNet" apparait. Tu peux :
- Uploader une video directement depuis TutorLMS vers BunnyNet
- Ou coller l'URL d'une video deja presente dans ta bibliotheque BunnyNet

La video est encodee automatiquement en plusieurs resolutions — 360p, 720p, 1080p — et distribuee via le CDN mondial de BunnyNet.

**[ECRAN — screencast lecteur video front-end]**

[Montre le rendu du player BunnyNet dans une lecon]

Cote eleve : le lecteur video est rapide, adaptatif (il ajuste la qualite selon la connexion) et ne porte pas le branding BunnyNet. Tes eleves ne voient pas la difference avec un player auto-heberge — sauf que ca charge plus vite.

**[ECRAN — screencast tarification]**

[Slide recapitulatif des couts BunnyNet]

Question cout : BunnyNet facture au stockage et a la bande passante. En moyenne, pour un site de formation avec 50 a 100 videos, compte environ 5 a 15 dollars par mois. C'est une fraction du cout de Vimeo Pro ou Wistia.

**[TRANSITION — face camera]**

La recommandation schoolsWP : des que tu as plus de 50 videos, utilise BunnyNet. En dessous, YouTube en non-liste ou Vimeo gratuit peuvent suffire — mais tu perds le controle sur le player et tu risques les pubs. BunnyNet, c'est le meilleur rapport qualite-prix pour l'hebergement video LMS.

---

**Points cles** :
- Addon BunnyNet a activer + compte BunnyNet (dash.bunny.net)
- Configuration : API Key, Library ID, CDN Hostname
- Upload direct depuis TutorLMS ou lien vers video existante
- Encodage automatique multi-resolution (360p, 720p, 1080p)
- CDN mondial = chargement rapide partout
- Cout moyen : 5-15$/mois pour 50-100 videos
- Recommandation schoolsWP : BunnyNet des 50+ videos

**Mots cles SEO** : TutorLMS BunnyNet, hebergement video LMS WordPress, BunnyNet CDN cours en ligne, video hosting TutorLMS

---

### Lecon 12.10 — Easy Digital Downloads

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + EDD
**Source** : doc easy-digital-download

---

**[INTRO — face camera]**

Easy Digital Downloads — EDD — c'est une alternative a WooCommerce specialisee dans la vente de produits numeriques. Si tu utilises deja EDD pour vendre des ebooks, des templates ou des logiciels, tu peux l'utiliser comme moteur de paiement pour TutorLMS. Voyons comment.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Settings > Monetization > eCommerce Engine]

Pour activer EDD comme moteur de paiement, va dans Settings, Monetization, eCommerce Engine. Selectionne "Easy Digital Downloads" dans la liste. Enregistre.

Prerequis : EDD doit etre installe et actif, avec au moins une passerelle de paiement configuree (Stripe ou PayPal dans EDD).

**[ECRAN — screencast Course Builder avec EDD]**

[Montre la section Pricing avec EDD actif]

Dans le Course Builder, la section Pricing change. Tu vois un champ pour lier un produit EDD existant ou en creer un nouveau. Le prix se gere dans EDD, comme avec WooCommerce.

**[ECRAN — screencast creation produit EDD]**

[Navigation vers Downloads > Add New]

Si tu crees manuellement : va dans Downloads, Add New. Donne un titre, definis le prix. Ensuite, dans le Course Builder TutorLMS, selectionne ce produit. L'eleve qui achete le "download" est automatiquement inscrit au cours.

**[ECRAN — screencast parcours d'achat]**

[Montre le checkout EDD cote eleve]

Cote eleve : le parcours d'achat passe par le checkout EDD. C'est plus leger que WooCommerce — EDD est concu pour les produits numeriques, donc pas de gestion d'expeditions, de stock ou de produits physiques.

**[TRANSITION — face camera]**

EDD a du sens si c'est deja ton outil de vente. Si tu pars de zero, le eCommerce natif TutorLMS est plus simple. Et si tu as besoin de produits physiques en plus, WooCommerce reste le choix logique. EDD, c'est le choix de niche pour les vendeurs de produits 100% numeriques.

---

**Points cles** :
- Activation : Settings > Monetization > eCommerce Engine > Easy Digital Downloads
- EDD doit etre installe avec une passerelle de paiement active
- Chaque cours lie a un produit EDD (creation manuelle ou automatique)
- Checkout EDD plus leger que WooCommerce (pas de gestion physique)
- Inscription automatique au cours apres achat du "download"
- Utile si tu vends deja des produits numeriques avec EDD
- Recommandation : eCommerce natif si tu demarres, EDD si c'est deja en place

**Mots cles SEO** : TutorLMS Easy Digital Downloads, EDD LMS WordPress, vendre cours EDD, integration EDD TutorLMS

---

### Lecon 12.11 — Loco Translate

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Loco Translate
**Source** : doc loco-translate

---

**[INTRO — face camera]**

TutorLMS est en anglais par defaut. Meme si WordPress est en francais, certaines chaines de texte de TutorLMS restent en anglais — boutons, labels, messages systeme. Loco Translate permet de tout traduire directement depuis l'admin WordPress, sans toucher aux fichiers de traduction manuellement. Voyons comment faire.

**[ECRAN — screencast installation Loco Translate]**

[Navigation vers Plugins > Add New > Loco Translate]

Installe et active Loco Translate depuis Plugins > Add New. C'est un plugin gratuit.

**[ECRAN — screencast interface Loco Translate]**

[Navigation vers Loco Translate > Plugins > TutorLMS]

Va dans Loco Translate, puis Plugins. Tu vois la liste de tous tes plugins. Clique sur "Tutor LMS". Tu vois les langues disponibles. Si le francais n'apparait pas, clique sur "New language", selectionne "French (France)" et choisis l'emplacement "Custom" — ca evite que tes traductions soient ecrasees lors des mises a jour.

**[ECRAN — screencast traduction d'une chaine]**

[Montre l'editeur de traduction]

L'editeur affiche deux colonnes : la chaine source en anglais a gauche, ta traduction a droite. Par exemple :
- "Enroll Now" → "S'inscrire"
- "Course Content" → "Contenu du cours"
- "Complete Lesson" → "Terminer la lecon"
- "Start Quiz" → "Demarrer le quiz"

Tu cliques sur une chaine, tu tapes ta traduction, tu passes a la suivante. Quand tu as fini, clique sur "Save". Les modifications s'appliquent immediatement sur ton site.

**[ECRAN — screencast recherche de chaine]**

[Montre la barre de recherche dans Loco Translate]

L'astuce pour aller vite : utilise la barre de recherche. Tu vois un texte en anglais sur ton site ? Copie-le, colle-le dans la recherche Loco Translate, et tu trouves la chaine a traduire en quelques secondes.

**[ECRAN — screencast Tutor LMS Pro]**

[Montre qu'il faut aussi traduire Tutor LMS Pro separement]

Point important : si tu utilises Tutor LMS Pro, c'est un plugin separe. Tu dois aussi le traduire dans Loco Translate — les chaines ne sont pas les memes que la version gratuite. Meme chose pour les addons actifs — chacun a ses propres chaines.

**[ECRAN — screencast resultat front-end]**

[Montre le site en francais apres traduction]

Le resultat : un site entierement en francais, y compris les elements de TutorLMS que la traduction officielle ne couvrait pas.

**[TRANSITION — face camera]**

La traduction complete de TutorLMS prend environ 30 minutes avec Loco Translate. Fais-le une fois, et c'est regle. Pense a reverifier apres chaque mise a jour majeure de TutorLMS — de nouvelles chaines peuvent apparaitre. C'est la derniere lecon de contenu de ce module. On termine avec le quiz.

---

**Points cles** :
- Loco Translate : plugin gratuit, traduction depuis l'admin WordPress
- Navigation : Loco Translate > Plugins > Tutor LMS
- Choisir l'emplacement "Custom" pour proteger les traductions des mises a jour
- Editeur deux colonnes : source anglais / traduction francais
- Barre de recherche pour trouver une chaine rapidement
- Traduire separement : Tutor LMS, Tutor LMS Pro, et chaque addon actif
- Reverifier apres les mises a jour majeures (nouvelles chaines possibles)

**Mots cles SEO** : TutorLMS francais, traduire TutorLMS, Loco Translate TutorLMS, TutorLMS traduction francaise WordPress

---

### Lecon 12.12 — Quiz Module 12

**Duree** : ~5 min (10 questions)
**Type** : Quiz TutorLMS
**Seuil de reussite** : 70%

---

**Question 1**
Quel est le moyen le plus simple de donner des cours en direct avec TutorLMS ?

- A) Zoom — c'est le plus connu
- B) Google Meet — gratuit, natif et sans installation cote eleve ✓
- C) Microsoft Teams via un plugin tiers
- D) YouTube Live via embed

**Explication** : Google Meet est gratuit, integre nativement dans TutorLMS, et fonctionne dans le navigateur sans rien installer.

---

**Question 2**
Quelle est la principale difference entre la configuration Google Meet et Zoom dans TutorLMS ?

- A) Google Meet utilise OAuth 2.0, Zoom utilise Server-to-Server OAuth via le Marketplace ✓
- B) Google Meet est payant, Zoom est gratuit
- C) Google Meet necessite un plugin tiers, Zoom est natif
- D) Il n'y a pas de difference

**Explication** : Google Meet se configure via la Google Cloud Console (OAuth 2.0), tandis que Zoom necessite une app Server-to-Server OAuth creee sur marketplace.zoom.us.

---

**Question 3**
Dans quel cas WooCommerce est-il preferable au eCommerce natif de TutorLMS ?

- A) Toujours — WooCommerce est plus fiable
- B) Quand tu vends aussi des produits physiques ou que tu as besoin d'extensions WooCommerce specifiques ✓
- C) Quand tu as moins de 10 cours
- D) Quand tu utilises Stripe

**Explication** : WooCommerce a du sens si tu vends deja d'autres produits ou si tu as besoin d'extensions specifiques (factures avancees, taxes multi-pays). Sinon, le eCommerce natif est plus simple.

---

**Question 4**
Quel page builder est developpe par la meme equipe que TutorLMS ?

- A) Elementor
- B) Divi
- C) Oxygen Builder
- D) Droip ✓

**Explication** : Droip est developpe par Themeum, la meme equipe que TutorLMS. L'integration est automatique — pas d'addon a activer.

---

**Question 5**
Qu'est-ce qui distingue Oxygen Builder des autres page builders pour TutorLMS ?

- A) Il est gratuit
- B) Il donne acces direct au CSS brut de chaque element ✓
- C) Il a plus de widgets que les autres
- D) Il est le seul compatible avec TutorLMS Pro

**Explication** : Oxygen Builder permet de modifier le CSS brut de chaque element, d'ajouter des classes personnalisees et d'ecrire du CSS custom directement dans l'editeur.

---

**Question 6**
A partir de combien de videos schoolsWP recommande-t-il d'utiliser BunnyNet ?

- A) 10 videos
- B) 25 videos
- C) 50 videos ✓
- D) 100 videos

**Explication** : La recommandation schoolsWP est d'utiliser BunnyNet des 50 videos. En dessous, YouTube non-liste ou Vimeo gratuit peuvent suffire.

---

**Question 7**
Quel est le cout moyen de BunnyNet pour un site de formation avec 50 a 100 videos ?

- A) Gratuit
- B) 5 a 15 dollars par mois ✓
- C) 50 a 100 dollars par mois
- D) 200+ dollars par mois

**Explication** : BunnyNet facture au stockage et a la bande passante. Pour 50 a 100 videos, le cout moyen est de 5 a 15 dollars par mois.

---

**Question 8**
Pourquoi choisir l'emplacement "Custom" dans Loco Translate pour les traductions TutorLMS ?

- A) Les traductions sont plus rapides
- B) Ca permet de traduire plus de langues
- C) Ca evite que les traductions soient ecrasees lors des mises a jour ✓
- D) C'est le seul emplacement disponible

**Explication** : L'emplacement "Custom" stocke les traductions dans un fichier separe qui n'est pas ecrase quand TutorLMS est mis a jour.

---

**Question 9**
Quelle est la particularite de Easy Digital Downloads par rapport a WooCommerce pour TutorLMS ?

- A) EDD est gratuit, WooCommerce est payant
- B) EDD est specialise produits numeriques — pas de gestion physique — donc plus leger ✓
- C) EDD supporte plus de passerelles de paiement
- D) EDD est plus rapide

**Explication** : EDD est concu pour les produits 100% numeriques. Il n'a pas de gestion d'expeditions, de stock ou de produits physiques, ce qui le rend plus leger que WooCommerce.

---

**Question 10**
Quand tu traduis TutorLMS avec Loco Translate, combien de plugins dois-tu traduire si tu utilises Tutor LMS Pro avec des addons ?

- A) Un seul — Tutor LMS
- B) Deux — Tutor LMS et Tutor LMS Pro
- C) Tutor LMS + Tutor LMS Pro + chaque addon actif separement ✓
- D) Aucun — la traduction officielle couvre tout

**Explication** : Tutor LMS, Tutor LMS Pro et chaque addon actif ont leurs propres chaines de texte. Il faut les traduire separement dans Loco Translate.

---

**Fin du Module 12 — Integrations tierces**

Resume du module :
- Cours en direct : Google Meet (recommande, gratuit) ou Zoom (si deja utilise)
- Google Classroom : pont vers l'ecosysteme Google Education
- eCommerce : natif (recommande) > WooCommerce (si produits mixtes) > EDD (si niche numerique)
- Page builders : Elementor, Divi, Oxygen, Droip — choisir celui deja en place
- Video hosting : BunnyNet recommande des 50+ videos (5-15$/mois)
- Traduction : Loco Translate pour franciser completement l'interface

Duree totale estimee du module : ~55 minutes

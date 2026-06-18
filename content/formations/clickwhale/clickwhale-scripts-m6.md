# Scripts vidéo - Module 6 : Tracking Codes et intégrations avancées

**Formation** : Maîtriser ClickWhale
**Module** : M6 - Tracking Codes et intégrations avancées (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~45 min
**Prérequis** : M4
**Date** : 2026-03-23

---

### Leçon 6.1 : Comprends les Tracking Codes : injecter des scripts sans toucher au code

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides explicatives, screencast rapide de l'interface Tracking Codes

---

**[INTRO - face caméra]**

Tu veux installer Google Tag Manager, le Meta Pixel ou un script de conversion sur ton site WordPress. Le réflexe classique : modifier le fichier header.php de ton thème, ou installer un plugin comme Insert Headers and Footers. Avec ClickWhale, tu n'as besoin ni de l'un ni de l'autre. Dans cette leçon, je t'explique comment les Tracking Codes te permettent d'injecter n'importe quel snippet JavaScript directement depuis l'interface ClickWhale.

**[ÉCRAN - slide "Tracking Codes, c'est quoi ?"]**

La fonctionnalité Tracking Codes de ClickWhale fait une chose simple : elle injecte des bouts de code JavaScript dans le head ou le body de ton site WordPress. Sans ouvrir un fichier PHP. Sans installer un plugin supplémentaire.

Concrètement, chaque Tracking Code que tu crées dans ClickWhale, c'est un snippet que tu colles tel quel. ClickWhale l'insère à l'endroit que tu choisis dans le HTML de tes pages.

**[ÉCRAN - slide "Quels scripts injecter ?"]**

Les cas d'usage les plus courants.

Google Tag Manager. C'est le conteneur universel. Tu installes GTM via ClickWhale, et ensuite tu configures tout le reste - GA4, conversions, événements - directement dans l'interface GTM. C'est l'approche recommandée.

Meta Pixel. Pour le retargeting Facebook et Instagram. Un visiteur lit un article sur ton site, tu le retrouves dans tes audiences Meta.

Google Ads. Pour tracker les conversions après un clic sur une pub Google.

Scripts de remarketing. Criteo, LinkedIn Insight Tag, TikTok Pixel - même principe.

**[ÉCRAN - slide "Centralisation"]**

L'avantage principal, c'est la centralisation. Au lieu d'avoir GTM dans un plugin, le Meta Pixel dans un autre, et un bout de code copié-collé dans le header.php de ton thème - tout est au même endroit. Dans ClickWhale, section Tracking Codes.

Tu vois d'un coup d'œil tous les scripts actifs sur ton site. Tu peux les activer, les désactiver, les cibler par page ou par rôle utilisateur. On verra tout ça dans les prochaines leçons.

**[ÉCRAN - screencast rapide de ClickWhale > Tracking Codes]**

[Navigation vers ClickWhale > Tracking Codes dans le menu WordPress]

Voici l'interface. Dans le menu WordPress, ClickWhale, puis Tracking Codes. Tu retrouves la liste de tous tes scripts. Pour chacun, tu vois le nom, la position (head ou body), le statut (actif ou inactif), et les pages ciblées.

[Survol d'un tracking code existant]

Chaque tracking code a un formulaire simple : un nom, une zone pour coller ton script, un choix de position, et des options de ciblage. On détaille tout ça dès la prochaine leçon avec l'installation de Google Tag Manager.

**[TRANSITION - face caméra]**

Tu sais maintenant ce que sont les Tracking Codes et pourquoi ils remplacent les plugins d'injection de scripts. Dans la leçon suivante, on passe à la pratique : tu installes Google Tag Manager sur ton site via ClickWhale.

---

**Points clés** :
- Tracking Codes = injection de snippets JS dans le head ou body de tes pages
- Aucun fichier thème à modifier, aucun plugin supplémentaire
- Cas d'usage : GTM, Meta Pixel, Google Ads, scripts de remarketing
- Centralisation : tous tes scripts au même endroit dans ClickWhale

**Mots-clés SEO** : tracking code WordPress, injecter script WordPress sans plugin, ClickWhale tracking codes, Google Tag Manager WordPress

---

### Leçon 6.2 : Ajoute Google Tag Manager à ton site WordPress

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast complet de l'installation GTM via ClickWhale

---

**[INTRO - face caméra]**

Google Tag Manager est le seul script que tu dois installer manuellement sur ton site. Une fois GTM en place, tu configures tout le reste - GA4, conversions, événements - depuis l'interface Google. Dans cette leçon, tu installes GTM sur ton WordPress via ClickWhale en moins de 5 minutes.

**[ÉCRAN - screencast Google Tag Manager]**

[Ouvre tagmanager.google.com]

Étape 1 : connecte-toi à Google Tag Manager. Si tu n'as pas encore de compte, crée-en un. Clique sur le conteneur de ton site.

[Montre la fenêtre avec les deux snippets GTM]

Étape 2 : GTM te donne deux bouts de code. Le premier commence par "script" - c'est le snippet principal, il va dans le head. Le deuxième commence par "noscript" - c'est le fallback pour les navigateurs sans JavaScript, il va dans le body.

Copie le premier snippet. Celui du head.

**[ÉCRAN - screencast ClickWhale admin]**

[Navigation vers ClickWhale > Tracking Codes > Add New]

Étape 3 : dans WordPress, va dans ClickWhale, Tracking Codes, puis clique sur Add New.

[Montre le formulaire de création]

Étape 4 : donne un nom clair à ton tracking code. Par exemple : "GTM - Head". Ça te permettra de l'identifier rapidement dans la liste.

Étape 5 : dans la zone de code, colle le snippet GTM principal. Celui que tu viens de copier.

[Montre le sélecteur de position]

Étape 6 : position. Sélectionne "Before closing head tag". C'est là que GTM doit être chargé. Pas dans le body - dans le head.

[Montre le sélecteur de pages]

Étape 7 : pages. Laisse "Whole website". GTM doit être présent sur toutes tes pages.

[Montre les checkboxes User Roles]

Étape 8 : User Roles. Décoche "Administrator". Quand tu navigues sur ton propre site en tant qu'admin, tu ne veux pas fausser tes statistiques. Si tu as des éditeurs, décoche aussi "Editor".

[Montre le toggle Enable et le bouton Save]

Étape 9 : coche "Enable Tracking Code" pour activer le script. Puis clique sur Save.

**[ÉCRAN - screencast retour à la liste]**

Premier snippet installé. Maintenant, le deuxième.

[Retourne sur tagmanager.google.com, copie le snippet noscript]

Étape 10 : retourne sur GTM et copie le deuxième snippet. Celui qui commence par "noscript".

[ClickWhale > Tracking Codes > Add New]

Étape 11 : dans ClickWhale, crée un nouveau Tracking Code. Nom : "GTM - Body (noscript)".

Étape 12 : colle le snippet noscript dans la zone de code.

Étape 13 : position - cette fois, sélectionne "After opening body tag". Ce snippet est un fallback, il doit être juste après l'ouverture du body.

Étape 14 : mêmes réglages que le premier - Whole website, décoche Administrator, Enable, Save.

**[ÉCRAN - screencast vérification GTM Preview]**

[Ouvre GTM > Preview]

Étape 15 : retourne dans Google Tag Manager. Clique sur Preview en haut à droite. Entre l'URL de ton site.

[Montre la fenêtre de debug GTM]

GTM ouvre un onglet de debug. Si tu vois "Tag Manager Connected" et que tes tags apparaissent, tout fonctionne. GTM est bien installé.

**[TRANSITION - face caméra]**

GTM est en place. C'est le seul script que tu installes directement - ensuite, tout passe par GTM. GA4, conversions Google Ads, événements personnalisés : tu configures tout ça dans l'interface GTM sans revenir dans ClickWhale. Dans la prochaine leçon, on installe le Meta Pixel pour le retargeting Facebook et Instagram.

---

**Points clés** :
- GTM nécessite 2 snippets : un dans le head (principal), un dans le body (noscript)
- Position : "Before closing head tag" pour le premier, "After opening body tag" pour le second
- Pages : Whole website
- Décocher Administrator dans User Roles pour ne pas fausser les stats
- Vérification : GTM Preview mode
- GTM est le seul script à installer - tout le reste se configure dans GTM

**Mots-clés SEO** : installer Google Tag Manager WordPress, GTM ClickWhale, tracking code GTM WordPress

---

### Leçon 6.3 : Ajoute le Meta Pixel (Facebook/Instagram)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast installation Meta Pixel via ClickWhale

---

**[INTRO - face caméra]**

Un visiteur arrive sur ton site, lit un article, puis repart. Sans le Meta Pixel, ce visiteur est perdu. Avec le Meta Pixel, tu peux le retrouver sur Facebook et Instagram et lui montrer une pub ciblée. Dans cette leçon, tu installes le Meta Pixel sur ton WordPress via ClickWhale.

**[ÉCRAN - slide "Meta Pixel, c'est quoi ?"]**

Le Meta Pixel, c'est un bout de JavaScript que Meta te fournit. Tu l'installes sur ton site, et à partir de là, Meta sait quels visiteurs passent sur quelles pages. Ça te permet de créer des audiences de retargeting.

Exemple concret avec schoolsWP. Un visiteur lit un article sur les LMS WordPress. Il ne s'inscrit pas. Avec le Meta Pixel, tu crées une audience "visiteurs de la catégorie LMS des 30 derniers jours". Tu lances une pub Facebook qui montre ta formation TutorLMS à cette audience précise. Le visiteur qui avait quitté ton site voit ta pub dans son fil Facebook. C'est du retargeting.

**[ÉCRAN - screencast Meta Business Suite]**

[Ouvre business.facebook.com > Événements Manager > Pixel]

Étape 1 : connecte-toi à Meta Business Suite. Va dans Événements Manager. Si tu n'as pas encore de Pixel, crée-en un.

[Montre le code de base du Meta Pixel]

Étape 2 : dans les paramètres du Pixel, clique sur "Ajouter le code manuellement". Meta te montre le snippet JavaScript. Copie-le intégralement.

**[ÉCRAN - screencast ClickWhale admin]**

[Navigation vers ClickWhale > Tracking Codes > Add New]

Étape 3 : dans WordPress, va dans ClickWhale, Tracking Codes, Add New.

Étape 4 : nom du tracking code : "Meta Pixel". Simple, clair.

[Montre la zone de code]

Étape 5 : colle le snippet Meta Pixel dans la zone de code.

[Montre le sélecteur de position]

Étape 6 : position - "Before closing head tag". Le Meta Pixel doit charger dans le head pour capturer les données dès la première page vue.

[Montre le sélecteur de pages]

Étape 7 : pages - "Whole website". Tu veux tracker les visiteurs sur toutes tes pages, pas seulement quelques-unes.

[Montre les checkboxes User Roles]

Étape 8 : User Roles - décoche "Administrator". Même logique que pour GTM : tes propres visites ne doivent pas polluer les données.

[Montre le toggle Enable et Save]

Étape 9 : coche "Enable Tracking Code", puis Save.

**[ÉCRAN - screencast vérification Meta Pixel Helper]**

[Ouvre Chrome, montre l'extension Meta Pixel Helper]

Étape 10 : pour vérifier que le Pixel fonctionne, installe l'extension Chrome "Meta Pixel Helper". C'est une extension gratuite de Meta.

[Navigue sur le site, montre l'icône Meta Pixel Helper qui s'active]

Visite ton site. L'icône du Pixel Helper doit devenir verte ou bleue avec un chiffre. Clique dessus. Tu dois voir "PageView" - ça confirme que le Pixel détecte bien la visite.

[Montre le détail dans le popup de l'extension]

Si tu vois "No pixel found", vérifie que le tracking code est bien activé dans ClickWhale et que tu n'es pas connecté en tant qu'admin (puisqu'on a exclu ce rôle).

**[TRANSITION - face caméra]**

Le Meta Pixel est installé. À partir de maintenant, Meta collecte les données de tes visiteurs pour tes futures campagnes de retargeting. Dans la prochaine leçon, on voit comment cibler un script sur une page spécifique ou exclure certains rôles utilisateurs - pour aller plus loin que le "Whole website".

---

**Points clés** :
- Meta Pixel = retargeting des visiteurs sur Facebook et Instagram
- Un seul snippet à installer, position "Before closing head tag"
- Pages : Whole website pour capturer tout le trafic
- Exclure Administrator pour ne pas fausser les audiences
- Vérification : extension Chrome "Meta Pixel Helper"
- Cas d'usage schoolsWP : retargeting visiteurs articles LMS vers formation TutorLMS

**Mots-clés SEO** : Meta Pixel WordPress, installer Facebook Pixel ClickWhale, retargeting WordPress

---

### Leçon 6.4 : Cible par page et par rôle utilisateur

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast des options de ciblage

---

**[INTRO - face caméra]**

Jusqu'ici, on a installé nos scripts sur "Whole website". Mais parfois, tu veux un script uniquement sur une page précise. Ou tu veux exclure certains types d'utilisateurs. ClickWhale te donne ces deux options de ciblage. Dans cette leçon, je te montre quand et comment les utiliser.

**[ÉCRAN - screencast ClickWhale - édition d'un Tracking Code]**

[Ouvre un Tracking Code existant, montre la section Pages]

Quand tu crées ou modifies un Tracking Code, tu as deux options pour les pages.

Option 1 : "Whole website". Le script est injecté sur toutes les pages de ton site. C'est le choix par défaut, et c'est ce qu'on utilise pour GTM, GA4, et le Meta Pixel en général.

[Montre le switch vers "Specific Page"]

Option 2 : "Specific Page". Tu sélectionnes une page précise dans le menu déroulant. Le script ne sera injecté que sur cette page.

**[ÉCRAN - slide "Cas d'usage : ciblage par page"]**

Quand utiliser le ciblage par page ? Le cas numéro un : un pixel de conversion.

Tu vends une formation. Après le paiement, ton client arrive sur une page "merci". Tu veux envoyer un signal de conversion à Google Ads ou Meta uniquement quand cette page est vue. Tu crées un Tracking Code avec le snippet de conversion, et tu le cibles sur ta page "merci".

Résultat : le script de conversion ne se déclenche que sur cette page. Pas sur le reste du site.

Autre cas : tu veux afficher un widget de chat uniquement sur ta page de vente. Tu crées le Tracking Code avec le script du widget, tu cibles la page de vente, et c'est fait.

**[ÉCRAN - screencast ClickWhale - section User Roles]**

[Montre les checkboxes de rôles]

Maintenant, le ciblage par rôle utilisateur. Quand tu crées un Tracking Code, tu vois une liste de rôles : Administrator, Editor, Author, Contributor, Subscriber. Si tu utilises TutorLMS, tu auras aussi "Student" et "Instructor".

Par défaut, tous les rôles sont cochés. Ça veut dire que le script est injecté pour tout le monde.

**[ÉCRAN - slide "Cas d'usage : ciblage par rôle"]**

La recommandation schoolsWP : décoche systématiquement Administrator et Editor pour tous tes scripts analytics. Toi et tes éditeurs, vous naviguez souvent sur le site. Vos visites faussent les stats si elles sont comptées.

[Montre un schéma : Admin navigue > GTM > GA4 > chiffres gonflés]

Imagine : tu as 100 visites par jour, mais 20 viennent de toi et de ton éditeur qui travaillent sur le site. GA4 affiche 100 visiteurs, alors que tu n'en as que 80 réels. En excluant les rôles admin et editor, tes stats sont propres.

Cas spécifique avec TutorLMS. Si tu as beaucoup d'étudiants actifs qui se connectent chaque jour pour suivre leurs cours, ils génèrent du trafic "interne". Pour tes campagnes de retargeting, tu veux peut-être cibler uniquement les visiteurs non connectés - ceux qui découvrent ton site. Dans ce cas, tu peux envisager d'exclure aussi le rôle "Student" sur certains scripts de retargeting.

Attention : ne le fais pas sur GTM ou GA4. Tu veux quand même mesurer l'activité de tes étudiants dans tes analytics. C'est uniquement pour les pixels de retargeting que cette exclusion peut avoir du sens.

**[TRANSITION - face caméra]**

Tu sais maintenant cibler tes scripts par page et par rôle. Règle d'or : GTM et analytics sur tout le site, exclusion admin/editor. Scripts de conversion sur les pages spécifiques. Dans la prochaine leçon, on clarifie un point technique important : la différence entre placer un script dans le head et dans le body.

---

**Points clés** :
- Pages : "Whole website" (défaut) ou "Specific Page" (ciblage précis)
- Ciblage par page : idéal pour les pixels de conversion (page merci, page de vente)
- Ciblage par rôle : exclure Administrator et Editor de tous les scripts analytics
- TutorLMS : envisager d'exclure Student sur les pixels de retargeting (pas sur GTM/GA4)
- Règle : analytics = tout le site, conversions = pages spécifiques

**Mots-clés SEO** : ciblage tracking code WordPress, exclure admin analytics WordPress, ClickWhale user roles

---

### Leçon 6.5 : Position du code : head vs body - quand utiliser quoi

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides explicatives, screencast rapide

---

**[INTRO - face caméra]**

Quand tu crées un Tracking Code dans ClickWhale, tu dois choisir une position : "Before closing head tag" ou "After opening body tag". C'est un choix technique qui impacte le fonctionnement de ton script. Dans cette leçon, je t'explique la différence et la règle simple pour ne jamais te tromper.

**[ÉCRAN - slide "Structure HTML d'une page"]**

Pour comprendre, un rappel rapide sur la structure d'une page web. Chaque page HTML a deux sections principales. Le head : c'est l'en-tête invisible. Il contient les métadonnées, les feuilles de style CSS, et les scripts qui doivent charger avant que le contenu s'affiche. Le body : c'est le contenu visible. Texte, images, boutons - tout ce que le visiteur voit.

Quand le navigateur charge ta page, il lit d'abord le head, puis le body. Dans cet ordre. Toujours.

**[ÉCRAN - slide "Before closing head tag"]**

Position "Before closing head tag". Le script est injecté dans le head, juste avant la balise fermante. Il se charge avant que le contenu de la page apparaisse.

C'est la position pour tous les scripts de tracking et d'analytics. GTM, Meta Pixel, GA4, Google Ads - ils doivent tous être dans le head. La raison : ces scripts doivent être actifs dès le premier instant où la page se charge. Si tu mets un pixel de tracking dans le body, il se charge après le contenu. Le visiteur peut naviguer ou quitter la page avant que le script ait eu le temps de s'exécuter. Tu perds des données.

**[ÉCRAN - slide "After opening body tag"]**

Position "After opening body tag". Le script est injecté dans le body, juste après la balise ouvrante. Il se charge après les scripts du head, mais avant le contenu principal.

Cette position est utilisée pour deux choses. D'abord, le snippet noscript de GTM - celui qu'on a installé dans la leçon 6.2. C'est un fallback pour les navigateurs sans JavaScript, et GTM demande explicitement de le mettre dans le body.

Ensuite, les scripts non critiques. Un widget de chat, un bandeau de consentement cookies, un script de pop-up. Ces éléments n'ont pas besoin de charger avant le contenu.

**[ÉCRAN - slide "La règle simple"]**

La règle. Le fournisseur du script te dit toujours où le placer. Dans la documentation de GTM, Meta, Google Ads - il y a une instruction claire : "place this in the head" ou "place this after the body tag".

Suis cette instruction. Si le fournisseur dit head, mets "Before closing head tag". Si le fournisseur dit body, mets "After opening body tag".

Ne fais jamais l'inverse. Si tu mets un script de tracking dans le body alors que le fournisseur demande le head, tu vas perdre des données. Le script charge trop tard, certaines pages vues ne sont pas captées.

**[ÉCRAN - slide récapitulatif "Head vs Body"]**

En résumé. Head : GTM (snippet principal), Meta Pixel, GA4, Google Ads, tous les pixels de tracking. Body : GTM (snippet noscript uniquement), widgets de chat, scripts non critiques.

Dans le doute, mets dans le head. C'est le choix le plus sûr pour un script de tracking.

**[TRANSITION - face caméra]**

Maintenant que tu maîtrises le placement, le ciblage et l'installation des scripts, on va voir quelque chose de plus stratégique. Dans la prochaine leçon, je te montre comment connecter ClickWhale avec FluentCRM pour tracker tes liens affiliés et segmenter tes contacts.

---

**Points clés** :
- Head (Before closing head tag) : scripts de tracking qui doivent charger en priorité (GTM, pixels, analytics)
- Body (After opening body tag) : fallback noscript GTM, widgets, scripts non critiques
- Règle : toujours suivre l'instruction du fournisseur du script
- Ne jamais mettre un pixel de tracking dans le body - perte de données garantie
- Ordre de chargement : head d'abord, body ensuite

**Mots-clés SEO** : head vs body tracking code, où placer Google Tag Manager, position script WordPress

---

### Leçon 6.6 : ClickWhale + FluentCRM : liens affiliés trackés et contacts segmentés

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides architecture, screencast des deux outils

---

**[INTRO - face caméra]**

Jusqu'ici, on a utilisé ClickWhale pour tracker des clics et FluentCRM pour gérer des contacts. Chacun dans son coin. Dans cette leçon, je te montre comment les connecter pour obtenir un double tracking : tu sais qui a cliqué (FluentCRM) et combien de fois ton lien a été cliqué (ClickWhale). C'est un contenu exclusif schoolsWP - tu ne trouveras pas ce tuto dans la doc officielle de ClickWhale.

**[ÉCRAN - slide "Le scénario"]**

Voici le scénario. Tu as une liste email dans FluentCRM. Tu envoies un email avec un lien affilié - par exemple, un lien vers TutorLMS Pro. Tu veux savoir deux choses.

Premièrement, qui a cliqué ? Quel contact, quel email, quel segment ? Ça, c'est le rôle de FluentCRM.

Deuxièmement, combien de clics au total ? Depuis quelles sources ? Avec quelle évolution dans le temps ? Ça, c'est le rôle de ClickWhale.

En combinant les deux, tu as une vue complète.

**[ÉCRAN - slide "Architecture à trois couches"]**

L'architecture schoolsWP pour le tracking, c'est trois outils avec chacun son rôle précis.

ClickWhale gère les liens. Raccourcissement, cloaking, statistiques de clics.

FluentCRM gère les contacts. Identification, segmentation, tags, automatisations.

Google Tag Manager gère les conversions. Quand un clic mène à un achat, c'est GTM qui envoie l'événement à GA4 ou Google Ads.

Chacun son rôle. Pas de chevauchement.

**[ÉCRAN - screencast ClickWhale - création du lien]**

[Navigation vers ClickWhale > Link Management > Add New]

Étape 1 : crée ton lien dans ClickWhale. Comme on l'a fait dans le Module 2.

[Montre les champs]

Nom : "TutorLMS Pro - Affilié". URL cible : ton lien affilié TutorLMS. Slug : "tutorlms-pro". Choisis la redirection 307 comme on l'a vu.

[Montre le lien raccourci généré]

Étape 2 : une fois le lien créé, copie l'URL raccourcie. Par exemple : tonsite.com/go/tutorlms-pro. C'est cette URL que tu vas utiliser dans FluentCRM.

**[ÉCRAN - screencast FluentCRM - création de l'email]**

[Navigation vers FluentCRM > Emails ou Automatisations]

Étape 3 : dans FluentCRM, crée ton email ou ton automatisation. À l'endroit où tu veux insérer le lien affilié, utilise un Smart Link.

[Montre l'éditeur d'email, insertion d'un lien]

Étape 4 : au lieu de coller directement le lien affilié brut, colle l'URL ClickWhale raccourcie. Celle que tu as copiée à l'étape 2.

[Montre le lien inséré dans l'email]

Résultat : quand ton contact clique sur le lien dans l'email, voici ce qui se passe. FluentCRM enregistre le clic - il sait que ce contact précis a cliqué. Le contact est redirigé vers l'URL ClickWhale. ClickWhale enregistre le clic dans ses stats - compteur, date, heure, referrer. Puis ClickWhale redirige vers la page affiliée finale.

Double tracking. Deux sources de données complémentaires.

**[ÉCRAN - screencast FluentCRM - tag automatique]**

[Navigation vers FluentCRM > Automatisations]

Étape 5 : le bonus. Dans FluentCRM, tu peux créer une automatisation qui applique un tag quand un contact clique sur un lien spécifique.

[Montre la création d'un trigger "Link Clicked"]

Crée une automatisation avec le déclencheur "Link Clicked in Email". Sélectionne l'email qui contient ton lien ClickWhale.

[Montre l'ajout d'un tag]

Comme action, ajoute le tag "a-cliqué-lien-affilié-tutorlms". Tu peux choisir le nom que tu veux, mais sois descriptif.

[Montre le résultat sur la fiche contact]

À partir de maintenant, chaque contact qui clique sur ce lien est automatiquement tagué. Tu peux ensuite utiliser ce tag pour segmenter : envoyer un email de relance aux contacts qui ont cliqué mais pas acheté, exclure ceux qui ont déjà acheté, ou créer une audience lookalike dans Meta à partir de ces contacts engagés.

**[ÉCRAN - slide "Résumé du flux"]**

Le flux complet. Contact reçoit l'email FluentCRM. Il clique sur le Smart Link. FluentCRM enregistre le clic et applique le tag. Le Smart Link pointe vers l'URL ClickWhale. ClickWhale enregistre le clic dans ses statistiques. ClickWhale redirige vers la page affiliée.

Trois niveaux de données. Qui a cliqué (FluentCRM). Combien de clics (ClickWhale). Qui a acheté (GTM + GA4 sur la page de confirmation).

**[TRANSITION - face caméra]**

Tu sais maintenant connecter ClickWhale et FluentCRM pour un tracking complet de tes liens affiliés. Dans la prochaine leçon, c'est à toi de jouer : un exercice pratique pour installer GTM et le Meta Pixel, et vérifier que tout fonctionne.

---

**Points clés** :
- Double tracking : FluentCRM identifie le contact, ClickWhale mesure les clics
- Architecture : ClickWhale (liens) + FluentCRM (contacts) + GTM (conversions)
- Mise en place : créer le lien ClickWhale, copier l'URL raccourcie, l'utiliser dans l'email FluentCRM
- Tag automatique FluentCRM sur clic pour segmenter les contacts intéressés
- Pas de chevauchement entre les outils - chacun son rôle

**Mots-clés SEO** : ClickWhale FluentCRM intégration, tracking lien affilié WordPress, segmentation email affilié

---

### Leçon 6.7 : Exercice : Configure GTM + Meta Pixel sur ton site et vérifie que tout remonte

**Durée** : 6 min (temps de lecture et réalisation)
**Type** : Exercice pratique (pas de vidéo)

---

## Exercice - Module 6

### Objectif

Installe Google Tag Manager et le Meta Pixel sur ton site WordPress via les Tracking Codes de ClickWhale. Vérifie que les deux scripts fonctionnent correctement.

### Prérequis

- Un compte Google Tag Manager avec un conteneur configuré (gratuit sur tagmanager.google.com)
- Un Meta Pixel créé dans Meta Business Suite (gratuit sur business.facebook.com)
- L'extension Chrome "Meta Pixel Helper" installée
- ClickWhale installé sur ton WordPress (fait depuis le Module 1)

### Partie 1 - Installer Google Tag Manager (2 Tracking Codes)

**Tracking Code 1 : GTM Head**

1. Dans GTM, copie le premier snippet (celui qui commence par `<script>`)
2. Dans WordPress, va dans ClickWhale > Tracking Codes > Add New
3. Nom : "GTM - Head"
4. Colle le snippet dans la zone de code
5. Position : "Before closing head tag"
6. Pages : "Whole website"
7. User Roles : décoche "Administrator" et "Editor"
8. Coche "Enable Tracking Code"
9. Clique sur Save

**Tracking Code 2 : GTM Body (noscript)**

1. Dans GTM, copie le deuxième snippet (celui qui commence par `<noscript>`)
2. Dans ClickWhale, crée un nouveau Tracking Code
3. Nom : "GTM - Body (noscript)"
4. Colle le snippet noscript dans la zone de code
5. Position : "After opening body tag"
6. Pages : "Whole website"
7. User Roles : décoche "Administrator" et "Editor"
8. Coche "Enable Tracking Code"
9. Clique sur Save

### Partie 2 - Installer le Meta Pixel (1 Tracking Code)

1. Dans Meta Business Suite > Événements Manager, copie le code de base de ton Pixel
2. Dans ClickWhale, crée un nouveau Tracking Code
3. Nom : "Meta Pixel"
4. Colle le snippet dans la zone de code
5. Position : "Before closing head tag"
6. Pages : "Whole website"
7. User Roles : décoche "Administrator" et "Editor"
8. Coche "Enable Tracking Code"
9. Clique sur Save

### Partie 3 - Vérification

**Vérifier GTM :**

1. Dans Google Tag Manager, clique sur "Preview" (en haut à droite)
2. Entre l'URL de ton site
3. Un onglet de debug s'ouvre
4. Tu dois voir "Tag Manager Connected" - si oui, GTM fonctionne

**Vérifier le Meta Pixel :**

1. Ouvre ton site dans Chrome (déconnecte-toi de WordPress ou utilise une fenêtre de navigation privée)
2. Clique sur l'icône Meta Pixel Helper dans la barre d'extensions
3. Tu dois voir "PageView" - si oui, le Pixel fonctionne

**Important** : fais les vérifications en navigation privée ou déconnecté de WordPress. Tu as exclu le rôle Administrator - si tu es connecté en admin, les scripts ne sont pas injectés et les tests échouent.

### Critères de validation

- [ ] 3 Tracking Codes créés dans ClickWhale (GTM Head, GTM Body, Meta Pixel)
- [ ] GTM Head en position "Before closing head tag"
- [ ] GTM Body en position "After opening body tag"
- [ ] Meta Pixel en position "Before closing head tag"
- [ ] Les 3 scripts ciblent "Whole website"
- [ ] Administrator et Editor exclus des User Roles sur les 3 scripts
- [ ] GTM Preview mode affiche "Tag Manager Connected"
- [ ] Meta Pixel Helper détecte "PageView" sur ton site

---

### Leçon 6.8 : Quiz final : Valide tes acquis M6 et la formation complète

**Durée** : 4 min (temps de lecture et réponse)
**Type** : Quiz QCM (pas de vidéo)
**Seuil de réussite** : 80% (8/10)

---

## Quiz - Module 6 et formation complète

### Question 1 - Tracking Codes

Que fait la fonctionnalité "Tracking Codes" de ClickWhale ?

- A) Elle crée des codes de réduction pour tes produits WooCommerce
- B) Elle injecte des snippets JavaScript dans le head ou body de ton site
- C) Elle génère des rapports de tracking automatiques dans Google Analytics
- D) Elle active le suivi des clics sur tous les liens sortants de ton site

**Bonne réponse : B**

---

### Question 2 - Installation GTM

Combien de Tracking Codes dois-tu créer dans ClickWhale pour installer Google Tag Manager correctement ?

- A) 1 seul - le snippet principal dans le head
- B) 2 - le snippet principal dans le head et le noscript dans le body
- C) 3 - un pour le head, un pour le body, un pour le footer
- D) Aucun - GTM s'installe automatiquement avec ClickWhale Pro

**Bonne réponse : B**

---

### Question 3 - Position des scripts

Où dois-tu placer le snippet principal de Google Tag Manager ?

- A) After opening body tag
- B) Before closing body tag
- C) Before closing head tag
- D) Dans le footer du thème WordPress

**Bonne réponse : C**

---

### Question 4 - User Roles

Pourquoi faut-il exclure le rôle "Administrator" des Tracking Codes analytics ?

- A) Pour accélérer le temps de chargement du site
- B) Pour respecter le RGPD
- C) Pour ne pas fausser les statistiques avec tes propres visites
- D) Pour empêcher les administrateurs de modifier les scripts

**Bonne réponse : C**

---

### Question 5 - Meta Pixel

À quoi sert principalement le Meta Pixel sur un site WordPress ?

- A) À afficher des boutons de partage Facebook sur les articles
- B) À synchroniser les commentaires Facebook avec WordPress
- C) À créer des audiences de retargeting sur Facebook et Instagram
- D) À publier automatiquement tes articles sur ta page Facebook

**Bonne réponse : C**

---

### Question 6 - Ciblage par page

Dans quel cas ciblerais-tu un Tracking Code sur une page spécifique plutôt que "Whole website" ?

- A) Pour installer Google Tag Manager
- B) Pour ajouter un pixel de conversion sur ta page "merci" après achat
- C) Pour activer GA4 sur ton blog
- D) Pour désactiver les cookies sur la page d'accueil

**Bonne réponse : B**

---

### Question 7 - ClickWhale + FluentCRM

Quand tu utilises un lien ClickWhale dans un email FluentCRM, que se passe-t-il au moment du clic ?

- A) FluentCRM enregistre le clic, puis ClickWhale enregistre le clic et redirige vers la cible
- B) ClickWhale enregistre le clic et FluentCRM ne détecte rien
- C) Le lien pointe directement vers la page affiliée sans passer par ClickWhale
- D) FluentCRM désactive le tracking ClickWhale pour éviter les doublons

**Bonne réponse : A**

---

### Question 8 - Head vs Body

Que risques-tu si tu places un pixel de tracking dans le body alors que le fournisseur demande le head ?

- A) Le script ne sera pas visible par Google
- B) Le script charge trop tard et tu perds des données de tracking
- C) WordPress affiche une erreur PHP
- D) Le script charge deux fois et double tes statistiques

**Bonne réponse : B**

---

### Question 9 - Transversale (M2)

Quelle redirection ClickWhale est recommandée pour un lien affilié dont tu veux conserver le jus SEO ?

- A) 301 - redirection permanente
- B) 302 - redirection temporaire
- C) 307 - redirection temporaire stricte
- D) 404 - page non trouvée

**Bonne réponse : C**

---

### Question 10 - Transversale (M1-M6)

Dans l'écosystème schoolsWP, quel est le rôle de chaque outil ?

- A) ClickWhale gère les contacts, FluentCRM gère les liens, GTM gère le SEO
- B) ClickWhale gère les liens, FluentCRM gère les contacts, GTM gère les conversions
- C) ClickWhale gère les conversions, FluentCRM gère les liens, GTM gère les contacts
- D) Les trois outils font la même chose et sont interchangeables

**Bonne réponse : B**

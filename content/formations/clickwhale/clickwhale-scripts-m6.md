# Scripts video — Module 6 : Tracking Codes et integrations avancees

**Formation** : Maitriser ClickWhale
**Module** : M6 — Tracking Codes et integrations avancees (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~45 min
**Prerequis** : M4
**Date** : 2026-03-23

---

### Lecon 6.1 — Comprends les Tracking Codes : injecter des scripts sans toucher au code

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides explicatives, screencast rapide de l'interface Tracking Codes

---

**[INTRO — face camera]**

Tu veux installer Google Tag Manager, le Meta Pixel ou un script de conversion sur ton site WordPress. Le reflexe classique : modifier le fichier header.php de ton theme, ou installer un plugin comme Insert Headers and Footers. Avec ClickWhale, tu n'as besoin ni de l'un ni de l'autre. Dans cette lecon, je t'explique comment les Tracking Codes te permettent d'injecter n'importe quel snippet JavaScript directement depuis l'interface ClickWhale.

**[ECRAN — slide "Tracking Codes, c'est quoi ?"]**

La fonctionnalite Tracking Codes de ClickWhale fait une chose simple : elle injecte des bouts de code JavaScript dans le head ou le body de ton site WordPress. Sans ouvrir un fichier PHP. Sans installer un plugin supplementaire.

Concretement, chaque Tracking Code que tu crees dans ClickWhale, c'est un snippet que tu colles tel quel. ClickWhale l'insere a l'endroit que tu choisis dans le HTML de tes pages.

**[ECRAN — slide "Quels scripts injecter ?"]**

Les cas d'usage les plus courants.

Google Tag Manager. C'est le conteneur universel. Tu installes GTM via ClickWhale, et ensuite tu configures tout le reste — GA4, conversions, evenements — directement dans l'interface GTM. C'est l'approche recommandee.

Meta Pixel. Pour le retargeting Facebook et Instagram. Un visiteur lit un article sur ton site, tu le retrouves dans tes audiences Meta.

Google Ads. Pour tracker les conversions apres un clic sur une pub Google.

Scripts de remarketing. Criteo, LinkedIn Insight Tag, TikTok Pixel — meme principe.

**[ECRAN — slide "Centralisation"]**

L'avantage principal, c'est la centralisation. Au lieu d'avoir GTM dans un plugin, le Meta Pixel dans un autre, et un bout de code copie-colle dans le header.php de ton theme — tout est au meme endroit. Dans ClickWhale, section Tracking Codes.

Tu vois d'un coup d'oeil tous les scripts actifs sur ton site. Tu peux les activer, les desactiver, les cibler par page ou par role utilisateur. On verra tout ca dans les prochaines lecons.

**[ECRAN — screencast rapide de ClickWhale > Tracking Codes]**

[Navigation vers ClickWhale > Tracking Codes dans le menu WordPress]

Voici l'interface. Dans le menu WordPress, ClickWhale, puis Tracking Codes. Tu retrouves la liste de tous tes scripts. Pour chacun, tu vois le nom, la position (head ou body), le statut (actif ou inactif), et les pages ciblees.

[Survol d'un tracking code existant]

Chaque tracking code a un formulaire simple : un nom, une zone pour coller ton script, un choix de position, et des options de ciblage. On detaille tout ca des la prochaine lecon avec l'installation de Google Tag Manager.

**[TRANSITION — face camera]**

Tu sais maintenant ce que sont les Tracking Codes et pourquoi ils remplacent les plugins d'injection de scripts. Dans la lecon suivante, on passe a la pratique : tu installes Google Tag Manager sur ton site via ClickWhale.

---

**Points cles** :
- Tracking Codes = injection de snippets JS dans le head ou body de tes pages
- Aucun fichier theme a modifier, aucun plugin supplementaire
- Cas d'usage : GTM, Meta Pixel, Google Ads, scripts de remarketing
- Centralisation : tous tes scripts au meme endroit dans ClickWhale

**Mots cles SEO** : tracking code WordPress, injecter script WordPress sans plugin, ClickWhale tracking codes, Google Tag Manager WordPress

---

### Lecon 6.2 — Ajoute Google Tag Manager a ton site WordPress

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast complet de l'installation GTM via ClickWhale

---

**[INTRO — face camera]**

Google Tag Manager est le seul script que tu dois installer manuellement sur ton site. Une fois GTM en place, tu configures tout le reste — GA4, conversions, evenements — depuis l'interface Google. Dans cette lecon, tu installes GTM sur ton WordPress via ClickWhale en moins de 5 minutes.

**[ECRAN — screencast Google Tag Manager]**

[Ouvre tagmanager.google.com]

Etape 1 : connecte-toi a Google Tag Manager. Si tu n'as pas encore de compte, cree-en un. Clique sur le conteneur de ton site.

[Montre la fenetre avec les deux snippets GTM]

Etape 2 : GTM te donne deux bouts de code. Le premier commence par "script" — c'est le snippet principal, il va dans le head. Le deuxieme commence par "noscript" — c'est le fallback pour les navigateurs sans JavaScript, il va dans le body.

Copie le premier snippet. Celui du head.

**[ECRAN — screencast ClickWhale admin]**

[Navigation vers ClickWhale > Tracking Codes > Add New]

Etape 3 : dans WordPress, va dans ClickWhale, Tracking Codes, puis clique sur Add New.

[Montre le formulaire de creation]

Etape 4 : donne un nom clair a ton tracking code. Par exemple : "GTM — Head". Ca te permettra de l'identifier rapidement dans la liste.

Etape 5 : dans la zone de code, colle le snippet GTM principal. Celui que tu viens de copier.

[Montre le selecteur de position]

Etape 6 : position. Selectionne "Before closing head tag". C'est la que GTM doit etre charge. Pas dans le body — dans le head.

[Montre le selecteur de pages]

Etape 7 : pages. Laisse "Whole website". GTM doit etre present sur toutes tes pages.

[Montre les checkboxes User Roles]

Etape 8 : User Roles. Decoche "Administrator". Quand tu navigues sur ton propre site en tant qu'admin, tu ne veux pas fausser tes statistiques. Si tu as des editeurs, decoche aussi "Editor".

[Montre le toggle Enable et le bouton Save]

Etape 9 : coche "Enable Tracking Code" pour activer le script. Puis clique sur Save.

**[ECRAN — screencast retour a la liste]**

Premier snippet installe. Maintenant, le deuxieme.

[Retourne sur tagmanager.google.com, copie le snippet noscript]

Etape 10 : retourne sur GTM et copie le deuxieme snippet. Celui qui commence par "noscript".

[ClickWhale > Tracking Codes > Add New]

Etape 11 : dans ClickWhale, cree un nouveau Tracking Code. Nom : "GTM — Body (noscript)".

Etape 12 : colle le snippet noscript dans la zone de code.

Etape 13 : position — cette fois, selectionne "After opening body tag". Ce snippet est un fallback, il doit etre juste apres l'ouverture du body.

Etape 14 : memes reglages que le premier — Whole website, decoche Administrator, Enable, Save.

**[ECRAN — screencast verification GTM Preview]**

[Ouvre GTM > Preview]

Etape 15 : retourne dans Google Tag Manager. Clique sur Preview en haut a droite. Entre l'URL de ton site.

[Montre la fenetre de debug GTM]

GTM ouvre un onglet de debug. Si tu vois "Tag Manager Connected" et que tes tags apparaissent, tout fonctionne. GTM est bien installe.

**[TRANSITION — face camera]**

GTM est en place. C'est le seul script que tu installes directement — ensuite, tout passe par GTM. GA4, conversions Google Ads, evenements personnalises : tu configures tout ca dans l'interface GTM sans revenir dans ClickWhale. Dans la prochaine lecon, on installe le Meta Pixel pour le retargeting Facebook et Instagram.

---

**Points cles** :
- GTM necessite 2 snippets : un dans le head (principal), un dans le body (noscript)
- Position : "Before closing head tag" pour le premier, "After opening body tag" pour le second
- Pages : Whole website
- Decocher Administrator dans User Roles pour ne pas fausser les stats
- Verification : GTM Preview mode
- GTM est le seul script a installer — tout le reste se configure dans GTM

**Mots cles SEO** : installer Google Tag Manager WordPress, GTM ClickWhale, tracking code GTM WordPress

---

### Lecon 6.3 — Ajoute le Meta Pixel (Facebook/Instagram)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast installation Meta Pixel via ClickWhale

---

**[INTRO — face camera]**

Un visiteur arrive sur ton site, lit un article, puis repart. Sans le Meta Pixel, ce visiteur est perdu. Avec le Meta Pixel, tu peux le retrouver sur Facebook et Instagram et lui montrer une pub ciblee. Dans cette lecon, tu installes le Meta Pixel sur ton WordPress via ClickWhale.

**[ECRAN — slide "Meta Pixel, c'est quoi ?"]**

Le Meta Pixel, c'est un bout de JavaScript que Meta te fournit. Tu l'installes sur ton site, et a partir de la, Meta sait quels visiteurs passent sur quelles pages. Ca te permet de creer des audiences de retargeting.

Exemple concret avec schoolsWP. Un visiteur lit un article sur les LMS WordPress. Il ne s'inscrit pas. Avec le Meta Pixel, tu crees une audience "visiteurs de la categorie LMS des 30 derniers jours". Tu lances une pub Facebook qui montre ta formation TutorLMS a cette audience precise. Le visiteur qui avait quitte ton site voit ta pub dans son fil Facebook. C'est du retargeting.

**[ECRAN — screencast Meta Business Suite]**

[Ouvre business.facebook.com > Evenements Manager > Pixel]

Etape 1 : connecte-toi a Meta Business Suite. Va dans Evenements Manager. Si tu n'as pas encore de Pixel, cree-en un.

[Montre le code de base du Meta Pixel]

Etape 2 : dans les parametres du Pixel, clique sur "Ajouter le code manuellement". Meta te montre le snippet JavaScript. Copie-le integralement.

**[ECRAN — screencast ClickWhale admin]**

[Navigation vers ClickWhale > Tracking Codes > Add New]

Etape 3 : dans WordPress, va dans ClickWhale, Tracking Codes, Add New.

Etape 4 : nom du tracking code : "Meta Pixel". Simple, clair.

[Montre la zone de code]

Etape 5 : colle le snippet Meta Pixel dans la zone de code.

[Montre le selecteur de position]

Etape 6 : position — "Before closing head tag". Le Meta Pixel doit charger dans le head pour capturer les donnees des la premiere page vue.

[Montre le selecteur de pages]

Etape 7 : pages — "Whole website". Tu veux tracker les visiteurs sur toutes tes pages, pas seulement quelques-unes.

[Montre les checkboxes User Roles]

Etape 8 : User Roles — decoche "Administrator". Meme logique que pour GTM : tes propres visites ne doivent pas polluer les donnees.

[Montre le toggle Enable et Save]

Etape 9 : coche "Enable Tracking Code", puis Save.

**[ECRAN — screencast verification Meta Pixel Helper]**

[Ouvre Chrome, montre l'extension Meta Pixel Helper]

Etape 10 : pour verifier que le Pixel fonctionne, installe l'extension Chrome "Meta Pixel Helper". C'est une extension gratuite de Meta.

[Navigue sur le site, montre l'icone Meta Pixel Helper qui s'active]

Visite ton site. L'icone du Pixel Helper doit devenir verte ou bleue avec un chiffre. Clique dessus. Tu dois voir "PageView" — ca confirme que le Pixel detecte bien la visite.

[Montre le detail dans le popup de l'extension]

Si tu vois "No pixel found", verifie que le tracking code est bien active dans ClickWhale et que tu n'es pas connecte en tant qu'admin (puisqu'on a exclu ce role).

**[TRANSITION — face camera]**

Le Meta Pixel est installe. A partir de maintenant, Meta collecte les donnees de tes visiteurs pour tes futures campagnes de retargeting. Dans la prochaine lecon, on voit comment cibler un script sur une page specifique ou exclure certains roles utilisateurs — pour aller plus loin que le "Whole website".

---

**Points cles** :
- Meta Pixel = retargeting des visiteurs sur Facebook et Instagram
- Un seul snippet a installer, position "Before closing head tag"
- Pages : Whole website pour capturer tout le trafic
- Exclure Administrator pour ne pas fausser les audiences
- Verification : extension Chrome "Meta Pixel Helper"
- Cas d'usage schoolsWP : retargeting visiteurs articles LMS vers formation TutorLMS

**Mots cles SEO** : Meta Pixel WordPress, installer Facebook Pixel ClickWhale, retargeting WordPress

---

### Lecon 6.4 — Cible par page et par role utilisateur

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des options de ciblage

---

**[INTRO — face camera]**

Jusqu'ici, on a installe nos scripts sur "Whole website". Mais parfois, tu veux un script uniquement sur une page precise. Ou tu veux exclure certains types d'utilisateurs. ClickWhale te donne ces deux options de ciblage. Dans cette lecon, je te montre quand et comment les utiliser.

**[ECRAN — screencast ClickWhale — edition d'un Tracking Code]**

[Ouvre un Tracking Code existant, montre la section Pages]

Quand tu crees ou modifies un Tracking Code, tu as deux options pour les pages.

Option 1 : "Whole website". Le script est injecte sur toutes les pages de ton site. C'est le choix par defaut, et c'est ce qu'on utilise pour GTM, GA4, et le Meta Pixel en general.

[Montre le switch vers "Specific Page"]

Option 2 : "Specific Page". Tu selectionnes une page precise dans le menu deroulant. Le script ne sera injecte que sur cette page.

**[ECRAN — slide "Cas d'usage : ciblage par page"]**

Quand utiliser le ciblage par page ? Le cas numero un : un pixel de conversion.

Tu vends une formation. Apres le paiement, ton client arrive sur une page "merci". Tu veux envoyer un signal de conversion a Google Ads ou Meta uniquement quand cette page est vue. Tu crees un Tracking Code avec le snippet de conversion, et tu le cibles sur ta page "merci".

Resultat : le script de conversion ne se declenche que sur cette page. Pas sur le reste du site.

Autre cas : tu veux afficher un widget de chat uniquement sur ta page de vente. Tu crees le Tracking Code avec le script du widget, tu cibles la page de vente, et c'est fait.

**[ECRAN — screencast ClickWhale — section User Roles]**

[Montre les checkboxes de roles]

Maintenant, le ciblage par role utilisateur. Quand tu crees un Tracking Code, tu vois une liste de roles : Administrator, Editor, Author, Contributor, Subscriber. Si tu utilises TutorLMS, tu auras aussi "Student" et "Instructor".

Par defaut, tous les roles sont coches. Ca veut dire que le script est injecte pour tout le monde.

**[ECRAN — slide "Cas d'usage : ciblage par role"]**

La recommandation schoolsWP : decoche systematiquement Administrator et Editor pour tous tes scripts analytics. Toi et tes editeurs, vous naviguez souvent sur le site. Vos visites faussent les stats si elles sont comptees.

[Montre un schema : Admin navigue > GTM > GA4 > chiffres gonfles]

Imagine : tu as 100 visites par jour, mais 20 viennent de toi et de ton editeur qui travaillent sur le site. GA4 affiche 100 visiteurs, alors que tu n'en as que 80 reels. En excluant les roles admin et editor, tes stats sont propres.

Cas specifique avec TutorLMS. Si tu as beaucoup d'etudiants actifs qui se connectent chaque jour pour suivre leurs cours, ils generent du trafic "interne". Pour tes campagnes de retargeting, tu veux peut-etre cibler uniquement les visiteurs non connectes — ceux qui decouvrent ton site. Dans ce cas, tu peux envisager d'exclure aussi le role "Student" sur certains scripts de retargeting.

Attention : ne le fais pas sur GTM ou GA4. Tu veux quand meme mesurer l'activite de tes etudiants dans tes analytics. C'est uniquement pour les pixels de retargeting que cette exclusion peut avoir du sens.

**[TRANSITION — face camera]**

Tu sais maintenant cibler tes scripts par page et par role. Regle d'or : GTM et analytics sur tout le site, exclusion admin/editor. Scripts de conversion sur les pages specifiques. Dans la prochaine lecon, on clarifie un point technique important : la difference entre placer un script dans le head et dans le body.

---

**Points cles** :
- Pages : "Whole website" (defaut) ou "Specific Page" (ciblage precis)
- Ciblage par page : ideal pour les pixels de conversion (page merci, page de vente)
- Ciblage par role : exclure Administrator et Editor de tous les scripts analytics
- TutorLMS : envisager d'exclure Student sur les pixels de retargeting (pas sur GTM/GA4)
- Regle : analytics = tout le site, conversions = pages specifiques

**Mots cles SEO** : ciblage tracking code WordPress, exclure admin analytics WordPress, ClickWhale user roles

---

### Lecon 6.5 — Position du code : head vs body — quand utiliser quoi

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides explicatives, screencast rapide

---

**[INTRO — face camera]**

Quand tu crees un Tracking Code dans ClickWhale, tu dois choisir une position : "Before closing head tag" ou "After opening body tag". C'est un choix technique qui impacte le fonctionnement de ton script. Dans cette lecon, je t'explique la difference et la regle simple pour ne jamais te tromper.

**[ECRAN — slide "Structure HTML d'une page"]**

Pour comprendre, un rappel rapide sur la structure d'une page web. Chaque page HTML a deux sections principales. Le head : c'est l'en-tete invisible. Il contient les metadonnees, les feuilles de style CSS, et les scripts qui doivent charger avant que le contenu s'affiche. Le body : c'est le contenu visible. Texte, images, boutons — tout ce que le visiteur voit.

Quand le navigateur charge ta page, il lit d'abord le head, puis le body. Dans cet ordre. Toujours.

**[ECRAN — slide "Before closing head tag"]**

Position "Before closing head tag". Le script est injecte dans le head, juste avant la balise fermante. Il se charge avant que le contenu de la page apparaisse.

C'est la position pour tous les scripts de tracking et d'analytics. GTM, Meta Pixel, GA4, Google Ads — ils doivent tous etre dans le head. La raison : ces scripts doivent etre actifs des le premier instant ou la page se charge. Si tu mets un pixel de tracking dans le body, il se charge apres le contenu. Le visiteur peut naviguer ou quitter la page avant que le script ait eu le temps de s'executer. Tu perds des donnees.

**[ECRAN — slide "After opening body tag"]**

Position "After opening body tag". Le script est injecte dans le body, juste apres la balise ouvrante. Il se charge apres les scripts du head, mais avant le contenu principal.

Cette position est utilisee pour deux choses. D'abord, le snippet noscript de GTM — celui qu'on a installe dans la lecon 6.2. C'est un fallback pour les navigateurs sans JavaScript, et GTM demande explicitement de le mettre dans le body.

Ensuite, les scripts non critiques. Un widget de chat, un bandeau de consentement cookies, un script de pop-up. Ces elements n'ont pas besoin de charger avant le contenu.

**[ECRAN — slide "La regle simple"]**

La regle. Le fournisseur du script te dit toujours ou le placer. Dans la documentation de GTM, Meta, Google Ads — il y a une instruction claire : "place this in the head" ou "place this after the body tag".

Suis cette instruction. Si le fournisseur dit head, mets "Before closing head tag". Si le fournisseur dit body, mets "After opening body tag".

Ne fais jamais l'inverse. Si tu mets un script de tracking dans le body alors que le fournisseur demande le head, tu vas perdre des donnees. Le script charge trop tard, certaines pages vues ne sont pas captees.

**[ECRAN — slide recapitulatif "Head vs Body"]**

En resume. Head : GTM (snippet principal), Meta Pixel, GA4, Google Ads, tous les pixels de tracking. Body : GTM (snippet noscript uniquement), widgets de chat, scripts non critiques.

Dans le doute, mets dans le head. C'est le choix le plus sur pour un script de tracking.

**[TRANSITION — face camera]**

Maintenant que tu maitrises le placement, le ciblage et l'installation des scripts, on va voir quelque chose de plus strategique. Dans la prochaine lecon, je te montre comment connecter ClickWhale avec FluentCRM pour tracker tes liens affilies et segmenter tes contacts.

---

**Points cles** :
- Head (Before closing head tag) : scripts de tracking qui doivent charger en priorite (GTM, pixels, analytics)
- Body (After opening body tag) : fallback noscript GTM, widgets, scripts non critiques
- Regle : toujours suivre l'instruction du fournisseur du script
- Ne jamais mettre un pixel de tracking dans le body — perte de donnees garantie
- Ordre de chargement : head d'abord, body ensuite

**Mots cles SEO** : head vs body tracking code, ou placer Google Tag Manager, position script WordPress

---

### Lecon 6.6 — ClickWhale + FluentCRM : liens affilies trackes et contacts segmentes

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides architecture, screencast des deux outils

---

**[INTRO — face camera]**

Jusqu'ici, on a utilise ClickWhale pour tracker des clics et FluentCRM pour gerer des contacts. Chacun dans son coin. Dans cette lecon, je te montre comment les connecter pour obtenir un double tracking : tu sais qui a clique (FluentCRM) et combien de fois ton lien a ete clique (ClickWhale). C'est un contenu exclusif schoolsWP — tu ne trouveras pas ce tuto dans la doc officielle de ClickWhale.

**[ECRAN — slide "Le scenario"]**

Voici le scenario. Tu as une liste email dans FluentCRM. Tu envoies un email avec un lien affilie — par exemple, un lien vers TutorLMS Pro. Tu veux savoir deux choses.

Premierement, qui a clique ? Quel contact, quel email, quel segment ? Ca, c'est le role de FluentCRM.

Deuxiemement, combien de clics au total ? Depuis quelles sources ? Avec quelle evolution dans le temps ? Ca, c'est le role de ClickWhale.

En combinant les deux, tu as une vue complete.

**[ECRAN — slide "Architecture a trois couches"]**

L'architecture schoolsWP pour le tracking, c'est trois outils avec chacun son role precis.

ClickWhale gere les liens. Raccourcissement, cloaking, statistiques de clics.

FluentCRM gere les contacts. Identification, segmentation, tags, automatisations.

Google Tag Manager gere les conversions. Quand un clic mene a un achat, c'est GTM qui envoie l'evenement a GA4 ou Google Ads.

Chacun son role. Pas de chevauchement.

**[ECRAN — screencast ClickWhale — creation du lien]**

[Navigation vers ClickWhale > Link Management > Add New]

Etape 1 : cree ton lien dans ClickWhale. Comme on l'a fait dans le Module 2.

[Montre les champs]

Nom : "TutorLMS Pro — Affilie". URL cible : ton lien affilie TutorLMS. Slug : "tutorlms-pro". Choisis la redirection 307 comme on l'a vu.

[Montre le lien raccourci genere]

Etape 2 : une fois le lien cree, copie l'URL raccourcie. Par exemple : tonsite.com/go/tutorlms-pro. C'est cette URL que tu vas utiliser dans FluentCRM.

**[ECRAN — screencast FluentCRM — creation de l'email]**

[Navigation vers FluentCRM > Emails ou Automatisations]

Etape 3 : dans FluentCRM, cree ton email ou ton automatisation. A l'endroit ou tu veux inserer le lien affilie, utilise un Smart Link.

[Montre l'editeur d'email, insertion d'un lien]

Etape 4 : au lieu de coller directement le lien affilie brut, colle l'URL ClickWhale raccourcie. Celle que tu as copiee a l'etape 2.

[Montre le lien insere dans l'email]

Resultat : quand ton contact clique sur le lien dans l'email, voici ce qui se passe. FluentCRM enregistre le clic — il sait que ce contact precis a clique. Le contact est redirige vers l'URL ClickWhale. ClickWhale enregistre le clic dans ses stats — compteur, date, heure, referrer. Puis ClickWhale redirige vers la page affilie finale.

Double tracking. Deux sources de donnees complementaires.

**[ECRAN — screencast FluentCRM — tag automatique]**

[Navigation vers FluentCRM > Automatisations]

Etape 5 : le bonus. Dans FluentCRM, tu peux creer une automatisation qui applique un tag quand un contact clique sur un lien specifique.

[Montre la creation d'un trigger "Link Clicked"]

Cree une automatisation avec le declencheur "Link Clicked in Email". Selectionne l'email qui contient ton lien ClickWhale.

[Montre l'ajout d'un tag]

Comme action, ajoute le tag "a-clique-lien-affilie-tutorlms". Tu peux choisir le nom que tu veux, mais sois descriptif.

[Montre le resultat sur la fiche contact]

A partir de maintenant, chaque contact qui clique sur ce lien est automatiquement tague. Tu peux ensuite utiliser ce tag pour segmenter : envoyer un email de relance aux contacts qui ont clique mais pas achete, exclure ceux qui ont deja achete, ou creer une audience lookalike dans Meta a partir de ces contacts engages.

**[ECRAN — slide "Resume du flux"]**

Le flux complet. Contact recoit l'email FluentCRM. Il clique sur le Smart Link. FluentCRM enregistre le clic et applique le tag. Le Smart Link pointe vers l'URL ClickWhale. ClickWhale enregistre le clic dans ses statistiques. ClickWhale redirige vers la page affilie.

Trois niveaux de donnees. Qui a clique (FluentCRM). Combien de clics (ClickWhale). Qui a achete (GTM + GA4 sur la page de confirmation).

**[TRANSITION — face camera]**

Tu sais maintenant connecter ClickWhale et FluentCRM pour un tracking complet de tes liens affilies. Dans la prochaine lecon, c'est a toi de jouer : un exercice pratique pour installer GTM et le Meta Pixel, et verifier que tout fonctionne.

---

**Points cles** :
- Double tracking : FluentCRM identifie le contact, ClickWhale mesure les clics
- Architecture : ClickWhale (liens) + FluentCRM (contacts) + GTM (conversions)
- Mise en place : creer le lien ClickWhale, copier l'URL raccourcie, l'utiliser dans l'email FluentCRM
- Tag automatique FluentCRM sur clic pour segmenter les contacts interesses
- Pas de chevauchement entre les outils — chacun son role

**Mots cles SEO** : ClickWhale FluentCRM integration, tracking lien affilie WordPress, segmentation email affilie

---

### Lecon 6.7 — Exercice : Configure GTM + Meta Pixel sur ton site et verifie que tout remonte

**Duree** : 6 min (temps de lecture et realisation)
**Type** : Exercice pratique (pas de video)

---

## Exercice — Module 6

### Objectif

Installe Google Tag Manager et le Meta Pixel sur ton site WordPress via les Tracking Codes de ClickWhale. Verifie que les deux scripts fonctionnent correctement.

### Prerequis

- Un compte Google Tag Manager avec un conteneur configure (gratuit sur tagmanager.google.com)
- Un Meta Pixel cree dans Meta Business Suite (gratuit sur business.facebook.com)
- L'extension Chrome "Meta Pixel Helper" installee
- ClickWhale installe sur ton WordPress (fait depuis le Module 1)

### Partie 1 — Installer Google Tag Manager (2 Tracking Codes)

**Tracking Code 1 : GTM Head**

1. Dans GTM, copie le premier snippet (celui qui commence par `<script>`)
2. Dans WordPress, va dans ClickWhale > Tracking Codes > Add New
3. Nom : "GTM — Head"
4. Colle le snippet dans la zone de code
5. Position : "Before closing head tag"
6. Pages : "Whole website"
7. User Roles : decoche "Administrator" et "Editor"
8. Coche "Enable Tracking Code"
9. Clique sur Save

**Tracking Code 2 : GTM Body (noscript)**

1. Dans GTM, copie le deuxieme snippet (celui qui commence par `<noscript>`)
2. Dans ClickWhale, cree un nouveau Tracking Code
3. Nom : "GTM — Body (noscript)"
4. Colle le snippet noscript dans la zone de code
5. Position : "After opening body tag"
6. Pages : "Whole website"
7. User Roles : decoche "Administrator" et "Editor"
8. Coche "Enable Tracking Code"
9. Clique sur Save

### Partie 2 — Installer le Meta Pixel (1 Tracking Code)

1. Dans Meta Business Suite > Evenements Manager, copie le code de base de ton Pixel
2. Dans ClickWhale, cree un nouveau Tracking Code
3. Nom : "Meta Pixel"
4. Colle le snippet dans la zone de code
5. Position : "Before closing head tag"
6. Pages : "Whole website"
7. User Roles : decoche "Administrator" et "Editor"
8. Coche "Enable Tracking Code"
9. Clique sur Save

### Partie 3 — Verification

**Verifier GTM :**

1. Dans Google Tag Manager, clique sur "Preview" (en haut a droite)
2. Entre l'URL de ton site
3. Un onglet de debug s'ouvre
4. Tu dois voir "Tag Manager Connected" — si oui, GTM fonctionne

**Verifier le Meta Pixel :**

1. Ouvre ton site dans Chrome (deconnecte-toi de WordPress ou utilise une fenetre de navigation privee)
2. Clique sur l'icone Meta Pixel Helper dans la barre d'extensions
3. Tu dois voir "PageView" — si oui, le Pixel fonctionne

**Important** : fais les verifications en navigation privee ou deconnecte de WordPress. Tu as exclu le role Administrator — si tu es connecte en admin, les scripts ne sont pas injectes et les tests echouent.

### Criteres de validation

- [ ] 3 Tracking Codes crees dans ClickWhale (GTM Head, GTM Body, Meta Pixel)
- [ ] GTM Head en position "Before closing head tag"
- [ ] GTM Body en position "After opening body tag"
- [ ] Meta Pixel en position "Before closing head tag"
- [ ] Les 3 scripts ciblent "Whole website"
- [ ] Administrator et Editor exclus des User Roles sur les 3 scripts
- [ ] GTM Preview mode affiche "Tag Manager Connected"
- [ ] Meta Pixel Helper detecte "PageView" sur ton site

---

### Lecon 6.8 — Quiz final : Valide tes acquis M6 et la formation complete

**Duree** : 4 min (temps de lecture et reponse)
**Type** : Quiz QCM (pas de video)
**Seuil de reussite** : 80% (8/10)

---

## Quiz — Module 6 et formation complete

### Question 1 — Tracking Codes

Que fait la fonctionnalite "Tracking Codes" de ClickWhale ?

- A) Elle cree des codes de reduction pour tes produits WooCommerce
- B) Elle injecte des snippets JavaScript dans le head ou body de ton site
- C) Elle genere des rapports de tracking automatiques dans Google Analytics
- D) Elle active le suivi des clics sur tous les liens sortants de ton site

**Bonne reponse : B**

---

### Question 2 — Installation GTM

Combien de Tracking Codes dois-tu creer dans ClickWhale pour installer Google Tag Manager correctement ?

- A) 1 seul — le snippet principal dans le head
- B) 2 — le snippet principal dans le head et le noscript dans le body
- C) 3 — un pour le head, un pour le body, un pour le footer
- D) Aucun — GTM s'installe automatiquement avec ClickWhale Pro

**Bonne reponse : B**

---

### Question 3 — Position des scripts

Ou dois-tu placer le snippet principal de Google Tag Manager ?

- A) After opening body tag
- B) Before closing body tag
- C) Before closing head tag
- D) Dans le footer du theme WordPress

**Bonne reponse : C**

---

### Question 4 — User Roles

Pourquoi faut-il exclure le role "Administrator" des Tracking Codes analytics ?

- A) Pour accelerer le temps de chargement du site
- B) Pour respecter le RGPD
- C) Pour ne pas fausser les statistiques avec tes propres visites
- D) Pour empecher les administrateurs de modifier les scripts

**Bonne reponse : C**

---

### Question 5 — Meta Pixel

A quoi sert principalement le Meta Pixel sur un site WordPress ?

- A) A afficher des boutons de partage Facebook sur les articles
- B) A synchroniser les commentaires Facebook avec WordPress
- C) A creer des audiences de retargeting sur Facebook et Instagram
- D) A publier automatiquement tes articles sur ta page Facebook

**Bonne reponse : C**

---

### Question 6 — Ciblage par page

Dans quel cas ciblerais-tu un Tracking Code sur une page specifique plutot que "Whole website" ?

- A) Pour installer Google Tag Manager
- B) Pour ajouter un pixel de conversion sur ta page "merci" apres achat
- C) Pour activer GA4 sur ton blog
- D) Pour desactiver les cookies sur la page d'accueil

**Bonne reponse : B**

---

### Question 7 — ClickWhale + FluentCRM

Quand tu utilises un lien ClickWhale dans un email FluentCRM, que se passe-t-il au moment du clic ?

- A) FluentCRM enregistre le clic, puis ClickWhale enregistre le clic et redirige vers la cible
- B) ClickWhale enregistre le clic et FluentCRM ne detecte rien
- C) Le lien pointe directement vers la page affilie sans passer par ClickWhale
- D) FluentCRM desactive le tracking ClickWhale pour eviter les doublons

**Bonne reponse : A**

---

### Question 8 — Head vs Body

Que risques-tu si tu places un pixel de tracking dans le body alors que le fournisseur demande le head ?

- A) Le script ne sera pas visible par Google
- B) Le script charge trop tard et tu perds des donnees de tracking
- C) WordPress affiche une erreur PHP
- D) Le script charge deux fois et double tes statistiques

**Bonne reponse : B**

---

### Question 9 — Transversale (M2)

Quelle redirection ClickWhale est recommandee pour un lien affilie dont tu veux conserver le jus SEO ?

- A) 301 — redirection permanente
- B) 302 — redirection temporaire
- C) 307 — redirection temporaire stricte
- D) 404 — page non trouvee

**Bonne reponse : C**

---

### Question 10 — Transversale (M1-M6)

Dans l'ecosysteme schoolsWP, quel est le role de chaque outil ?

- A) ClickWhale gere les contacts, FluentCRM gere les liens, GTM gere le SEO
- B) ClickWhale gere les liens, FluentCRM gere les contacts, GTM gere les conversions
- C) ClickWhale gere les conversions, FluentCRM gere les liens, GTM gere les contacts
- D) Les trois outils font la meme chose et sont interchangeables

**Bonne reponse : B**

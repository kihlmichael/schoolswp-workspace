# Scripts vidéo - Module 11 : Inscription & Gestion utilisateurs

**Formation** : Maîtriser TutorLMS
**Module** : M11 - Inscription & Gestion utilisateurs (Premium)
**Leçons** : 11 vidéos + 1 quiz
**Durée totale** : ~63 min
**Date** : 2026-03-23

---

### Leçon 11.1 : Inscription étudiant

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast du parcours d'inscription
**Source** : doc tutorials/student-signup

---

**[INTRO - face caméra]**

Quand un visiteur arrive sur ton site de formation, la première chose qu'il doit pouvoir faire, c'est s'inscrire. TutorLMS propose un parcours d'inscription étudiant intégré, avec un formulaire dédié et des options de personnalisation. Dans cette leçon, on configure ce parcours de A à Z.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > General]

Pour commencer, va dans Tutor LMS, puis Settings, puis l'onglet General. Cherche l'option "Student Registration". Active-la si ce n'est pas déjà fait. C'est cette option qui autorise les visiteurs à créer un compte étudiant depuis le front-end.

**[ÉCRAN - screencast réglages inscription]**

[Montre les options liées à l'inscription]

Tu as plusieurs options à configurer :

1. Registration Page - la page qui contient le formulaire d'inscription. TutorLMS en crée une automatiquement, mais tu peux en choisir une autre.
2. Email Verification - si tu actives cette option, l'étudiant doit confirmer son adresse email avant d'accéder aux cours. Recommandé pour éviter les faux comptes.
3. Manual Instructor Approval - on verra ça dans la leçon suivante, c'est pour les instructeurs.

**[ÉCRAN - screencast front-end]**

[Montre la page d'inscription vue par un visiteur]

Côté visiteur, le formulaire d'inscription affiche les champs standards : nom, prénom, email, mot de passe. L'étudiant remplit le formulaire, reçoit un email de confirmation si tu l'as activé, puis accède à son tableau de bord.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Users dans le back-office]

Dans le back-office WordPress, chaque étudiant inscrit apparaît dans la liste des utilisateurs avec le rôle "Subscriber" par défaut. TutorLMS lui attribue automatiquement les capacités nécessaires pour suivre des cours.

**[ÉCRAN - screencast TutorLMS Dashboard étudiant]**

[Montre le tableau de bord étudiant front-end]

Une fois connecté, l'étudiant accède à son dashboard TutorLMS : ses cours en cours, ses certificats, son profil. C'est son espace personnel.

**[TRANSITION - face caméra]**

La recommandation schoolsWP : active toujours la vérification email. Ça filtre les inscriptions fantômes et améliore la qualité de ta liste. Dans la prochaine leçon, on voit le parcours d'inscription pour les instructeurs - c'est un peu différent.

---

**Points clés** :
- Activation dans Settings > General > Student Registration
- Email Verification recommandée pour filtrer les faux comptes
- Rôle WordPress : Subscriber avec capacités TutorLMS
- Dashboard étudiant front-end accessible dès la connexion

**Mots clés SEO** : inscription étudiant TutorLMS, formulaire inscription LMS WordPress, student signup TutorLMS, créer compte élève TutorLMS

---

### Leçon 11.2 : Inscription instructeur

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast du parcours instructeur
**Source** : doc tutorials/instructor-signup

---

**[INTRO - face caméra]**

Si tu prévois d'avoir plusieurs formateurs sur ton site, tu dois configurer l'inscription instructeur. TutorLMS permet à n'importe qui de candidater comme instructeur, avec un système de validation manuelle ou automatique. Voyons comment ça fonctionne.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > General]

Va dans Tutor LMS, Settings, onglet General. Cherche la section "Instructor Registration". Active l'option "Enable Instructor Registration". Ça ajoute un formulaire d'inscription spécifique pour les instructeurs sur le front-end.

**[ÉCRAN - screencast réglages instructeur]**

[Montre les options d'approbation]

Juste en dessous, tu trouves l'option "Manual Approval for Instructor". Deux choix :

1. Activé - chaque candidature instructeur passe par toi. Tu reçois une notification, tu examines le profil, tu acceptes ou tu refuses.
2. Désactivé - l'inscription est automatique. Toute personne qui s'inscrit comme instructeur obtient immédiatement les droits de création de cours.

Pour un site professionnel, je recommande l'approbation manuelle. Ça te permet de contrôler qui publie du contenu sur ta plateforme.

**[ÉCRAN - screencast front-end]**

[Montre le formulaire d'inscription instructeur]

Le formulaire instructeur est similaire à celui de l'étudiant, avec un champ supplémentaire : la bio. L'instructeur décrit son expertise et son expérience. C'est ce que tu liras pour décider si tu approuves sa candidature.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Instructors > liste en attente]

Quand un instructeur s'inscrit avec l'approbation manuelle, il apparaît dans la section Instructors avec le statut "Pending". Tu cliques sur son profil, tu vérifies sa bio, et tu valides ou tu refuses.

**[ÉCRAN - screencast notification email]**

[Montre l'email de notification]

TutorLMS envoie un email à l'instructeur pour lui confirmer l'approbation. À partir de là, il peut créer des cours depuis le front-end.

**[TRANSITION - face caméra]**

Conseil schoolsWP : même si tu es le seul formateur pour l'instant, active l'inscription instructeur avec approbation manuelle. Ça te laisse la porte ouverte pour accueillir des contributeurs plus tard, sans risque. Prochaine leçon : on simplifie l'inscription avec le Social Login Google.

---

**Points clés** :
- Activation dans Settings > General > Instructor Registration
- Approbation manuelle recommandée pour contrôler la qualité
- Les instructeurs en attente apparaissent dans Tutor LMS > Instructors
- Email de confirmation automatique à l'approbation

**Mots clés SEO** : inscription instructeur TutorLMS, ajouter formateur LMS WordPress, instructor signup TutorLMS, multi-instructeur TutorLMS

---

### Leçon 11.3 : Social Login (Google)

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Google Cloud Console + TutorLMS
**Source** : Vidéo #19, #28 + doc social-login

---

**[INTRO - face caméra]**

Plus un formulaire d'inscription est simple, plus tu as d'inscrits. Le Social Login permet à tes visiteurs de s'inscrire avec leur compte Google - pas de mot de passe à créer, pas de formulaire à remplir. Dans cette leçon, on configure la connexion Google dans TutorLMS.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Design & Content > Login]

Pour activer le Social Login, va dans Tutor LMS, Settings, puis Design & Content, onglet Login. Tu y trouves la section Social Login avec les options Google et Facebook. Active le toggle "Google Login".

TutorLMS te demande deux informations : un Client ID et un Client Secret. On va les créer dans Google Cloud Console.

**[ÉCRAN - screencast Google Cloud Console]**

[Navigation vers console.cloud.google.com > APIs & Services > Credentials]

Connecte-toi à Google Cloud Console. Si tu n'as pas de projet, crée-en un - donne-lui le nom de ton site. Ensuite, va dans APIs & Services, puis Credentials.

Clique sur "Create Credentials", puis "OAuth client ID".

**[ÉCRAN - screencast configuration OAuth]**

[Montre les champs de configuration]

Étape par étape :

1. Application type - sélectionne "Web application"
2. Name - donne un nom descriptif, par exemple "TutorLMS Social Login"
3. Authorized JavaScript origins - entre l'URL de ton site, par exemple https://ton-site.com
4. Authorized redirect URIs - entre l'URL de callback que TutorLMS t'affiche dans ses réglages

Valide. Google génère un Client ID et un Client Secret.

**[ÉCRAN - screencast écran de consentement OAuth]**

[Navigation vers OAuth consent screen]

Avant que ça fonctionne, tu dois aussi configurer l'écran de consentement OAuth. Va dans OAuth consent screen. Choisis "External" si ton site est public. Remplis le nom de l'application, l'email de support et les domaines autorisés.

Pas besoin de scopes supplémentaires - les scopes par défaut (email, profile) suffisent.

**[ÉCRAN - screencast retour TutorLMS]**

[Colle le Client ID et Client Secret dans les champs]

Retourne dans TutorLMS. Colle le Client ID et le Client Secret dans les champs correspondants. Enregistre.

**[ÉCRAN - screencast front-end]**

[Montre le bouton "Sign in with Google" sur la page de connexion]

Sur ta page de connexion, un bouton "Sign in with Google" apparaît. Le visiteur clique, autorise l'accès, et son compte est créé automatiquement avec les bonnes informations.

**[TRANSITION - face caméra]**

Le Social Login Google couvre la majorité de tes visiteurs. Mais certains préfèrent Facebook - c'est ce qu'on configure dans la prochaine leçon.

---

**Points clés** :
- Social Login activé dans Settings > Design & Content > Login
- Client ID et Client Secret créés dans Google Cloud Console > Credentials
- OAuth consent screen configuré en mode External
- Redirect URI fournie par TutorLMS à coller dans Google Cloud

**Mots clés SEO** : Social Login TutorLMS Google, connexion Google LMS WordPress, OAuth TutorLMS, inscription Google TutorLMS

---

### Leçon 11.4 : Social Login (Facebook)

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Meta for Developers + TutorLMS
**Source** : Vidéo #21 + doc get-facebook-app-id

---

**[INTRO - face caméra]**

Après Google, Facebook. Certains de tes élèves préfèrent se connecter avec leur compte Facebook. La configuration est un peu différente - ça passe par Meta for Developers. On fait ça ensemble.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Design & Content > Login]

Dans TutorLMS, même endroit que pour Google : Settings, Design & Content, Login. Active le toggle "Facebook Login". Tu as besoin d'un App ID et d'un App Secret.

**[ÉCRAN - screencast Meta for Developers]**

[Navigation vers developers.facebook.com > My Apps]

Va sur developers.facebook.com. Connecte-toi avec ton compte Facebook. Clique sur "Create App".

**[ÉCRAN - screencast création de l'app]**

[Montre les étapes de création]

1. Use case - sélectionne "Authenticate and request data from users with Facebook Login"
2. App name - donne un nom clair, par exemple "TutorLMS Login"
3. App contact email - ton email professionnel

Valide. Facebook crée l'application.

**[ÉCRAN - screencast configuration Facebook Login]**

[Navigation vers Facebook Login > Settings dans l'app]

Dans le menu de l'app, va dans Facebook Login, puis Settings. Dans le champ "Valid OAuth Redirect URIs", colle l'URL de callback que TutorLMS t'affiche. C'est la même logique que pour Google.

**[ÉCRAN - screencast App ID et App Secret]**

[Navigation vers Settings > Basic]

Pour récupérer tes clés, va dans Settings, puis Basic. Tu y trouves l'App ID (affiché directement) et l'App Secret (clique sur "Show" pour le révéler).

**[ÉCRAN - screencast retour TutorLMS]**

[Colle l'App ID et l'App Secret]

Retourne dans TutorLMS. Colle l'App ID et l'App Secret. Enregistre.

**[ÉCRAN - screencast front-end]**

[Montre les deux boutons Social Login sur la page de connexion]

Ta page de connexion affiche maintenant deux boutons : "Sign in with Google" et "Sign in with Facebook". L'élève choisit celui qu'il préfère.

**[TRANSITION - face caméra]**

Avec Google et Facebook configurés, tu couvres la grande majorité des comptes sociaux. Mais le Social Login ne protège pas contre les bots. Prochaine leçon : on ajoute reCAPTCHA pour sécuriser les formulaires.

---

**Points clés** :
- App créée sur developers.facebook.com avec le use case "Facebook Login"
- App ID et App Secret dans Settings > Basic de l'app
- Redirect URI TutorLMS à coller dans Facebook Login > Settings
- Les deux boutons Google + Facebook apparaissent sur la page de connexion

**Mots clés SEO** : Social Login Facebook TutorLMS, connexion Facebook LMS WordPress, Meta App ID TutorLMS, Facebook Login WordPress

---

### Leçon 11.5 : reCAPTCHA anti-fraude

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Google reCAPTCHA + TutorLMS
**Source** : Vidéo #23 + doc create-recaptcha-keys

---

**[INTRO - face caméra]**

Les bots adorent les formulaires d'inscription. Faux comptes, spam, tentatives de brute force - c'est un problème réel dès que ton site a un peu de trafic. reCAPTCHA bloque ces bots avant qu'ils ne posent problème. TutorLMS l'intègre nativement - on le configure maintenant.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Design & Content > Login]

Dans TutorLMS, va dans Settings, Design & Content, onglet Login. Cherche la section "reCAPTCHA". Active le toggle. TutorLMS te demande une Site Key et une Secret Key.

**[ÉCRAN - screencast Google reCAPTCHA admin]**

[Navigation vers google.com/recaptcha/admin]

Va sur google.com/recaptcha/admin. Connecte-toi avec ton compte Google. Clique sur le "+" pour créer un nouveau site.

**[ÉCRAN - screencast formulaire de création]**

[Montre les champs à remplir]

Remplis les champs :

1. Label - le nom de ton site, pour t'y retrouver
2. reCAPTCHA type - sélectionne "reCAPTCHA v2" avec l'option "I'm not a robot" checkbox. TutorLMS ne supporte pas encore v3 nativement.
3. Domains - entre ton nom de domaine, sans https, par exemple "ton-site.com"
4. Accept the terms of service

Valide.

**[ÉCRAN - screencast clés générées]**

[Montre la Site Key et la Secret Key]

Google génère deux clés :
- Site Key - la clé publique, visible dans le code HTML de ta page
- Secret Key - la clé privée, qui reste sur ton serveur

Copie les deux.

**[ÉCRAN - screencast retour TutorLMS]**

[Colle les clés dans les champs correspondants]

Retourne dans TutorLMS. Colle la Site Key et la Secret Key dans les champs. Enregistre.

**[ÉCRAN - screencast front-end]**

[Montre le formulaire d'inscription avec le reCAPTCHA visible]

Sur ta page d'inscription, la checkbox "I'm not a robot" apparaît en bas du formulaire. Les visiteurs réels cochent la case, les bots sont bloqués.

**[TRANSITION - face caméra]**

Le reCAPTCHA est une protection de base, mais efficace. Combine-le avec la vérification email de la leçon 11.1, et tu as un double filtre contre les faux comptes. Prochaine leçon : on passe aux règles business avec l'enrollment scheduling.

---

**Points clés** :
- reCAPTCHA activé dans Settings > Design & Content > Login
- Clés créées sur google.com/recaptcha/admin (v2 checkbox)
- Site Key (publique) + Secret Key (privée) à coller dans TutorLMS
- Combiné avec la vérification email pour une double protection

**Mots clés SEO** : reCAPTCHA TutorLMS, sécuriser inscription LMS WordPress, anti-spam TutorLMS, protéger formulaire TutorLMS

---

### Leçon 11.6 : Enrollment & scheduling

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Addon Enrollment + Course Builder
**Source** : Vidéo #36 + doc addons/enrollment

---

**[INTRO - face caméra]**

Par défaut, un élève peut s'inscrire à un cours à n'importe quel moment. Mais dans certains cas, tu veux contrôler quand l'inscription est ouverte - par exemple pour un cours en cohorte, une session qui démarre à date fixe, ou une offre limitée dans le temps. L'addon Enrollment de TutorLMS gère tout ça.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Addons]

Pour activer l'addon, va dans Tutor LMS, puis Addons. Cherche "Enrollment". Active-le. C'est un addon Pro - il faut la licence TutorLMS Pro active.

**[ÉCRAN - screencast Course Builder]**

[Navigation vers la section Enrollment d'un cours]

Une fois l'addon actif, ouvre un cours dans le Course Builder. Tu trouves une nouvelle section "Enrollment". Trois options principales :

1. Open - inscription ouverte en permanence. C'est le comportement par défaut.
2. Closed - inscription fermée. Personne ne peut s'inscrire. Utile quand tu prépares un cours et que tu ne veux pas d'inscriptions anticipées.
3. By Date - tu définis une fenêtre d'inscription avec une date de début et une date de fin.

**[ÉCRAN - screencast configuration By Date]**

[Montre les champs date de début et date de fin]

Avec l'option "By Date", tu configures :
- Enrollment Start Date - la date et l'heure d'ouverture des inscriptions
- Enrollment End Date - la date et l'heure de fermeture

En dehors de cette fenêtre, le bouton d'inscription est remplacé par un message indiquant que l'inscription est fermée ou qu'elle ouvrira à telle date.

**[ÉCRAN - screencast front-end avant/pendant/après]**

[Montre les trois états du bouton d'inscription]

Trois situations côté visiteur :
- Avant la date de début - message "Enrollment opens on [date]"
- Pendant la fenêtre - bouton d'inscription actif
- Après la date de fin - message "Enrollment is closed"

C'est automatique, pas besoin de revenir modifier manuellement.

**[ÉCRAN - screencast cas d'usage]**

[Montre un cours configuré en cohorte]

Cas d'usage concret : tu lances une formation en cohorte qui démarre le 1er du mois. Tu ouvres les inscriptions du 15 au 28 du mois précédent. Ceux qui s'inscrivent commencent ensemble. Ceux qui arrivent trop tard attendront la prochaine session.

**[TRANSITION - face caméra]**

L'enrollment scheduling est un outil puissant pour créer de l'urgence et structurer tes lancements. Mais que se passe-t-il quand un élève est déjà inscrit et que tu veux limiter la durée de son accès ? C'est le sujet de la prochaine leçon : l'expiration d'inscription.

---

**Points clés** :
- Addon Enrollment activé dans Tutor LMS > Addons (Pro requis)
- Trois modes : Open, Closed, By Date
- By Date = fenêtre d'inscription avec début et fin
- Le bouton d'inscription s'adapte automatiquement selon les dates
- Idéal pour les cours en cohorte et les lancements

**Mots clés SEO** : enrollment scheduling TutorLMS, inscription programmée LMS WordPress, cours cohorte TutorLMS, fenêtre inscription TutorLMS

---

### Leçon 11.7 : Expiration d'inscription

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Course Builder section expiration
**Source** : doc tutorials/enrollment-expiration

---

**[INTRO - face caméra]**

Tu veux que l'accès à un cours expire après un certain temps ? Par exemple, 12 mois après l'achat, ou 90 jours pour un essai gratuit. TutorLMS permet de définir une durée d'accès limitée pour chaque cours. Une fois le délai dépassé, l'élève perd l'accès automatiquement.

**[ÉCRAN - screencast Course Builder]**

[Navigation vers un cours > section Settings ou Enrollment]

Ouvre un cours dans le Course Builder. Va dans les réglages du cours. Cherche la section "Enrollment Expiry" ou "Content Access Expiry" selon ta version.

**[ÉCRAN - screencast configuration expiration]**

[Montre les champs de configuration]

Tu as deux éléments à configurer :

1. Enable Enrollment Expiry - active le toggle pour ce cours
2. Expire After - définis la durée en jours. Par exemple, 365 pour un an, 90 pour un trimestre, 30 pour un mois

La durée commence à partir de la date d'inscription de l'élève, pas de la date de création du cours. Chaque élève a donc son propre compte à rebours.

**[ÉCRAN - screencast front-end élève]**

[Montre le dashboard élève avec la date d'expiration visible]

Côté élève, la date d'expiration est visible dans son tableau de bord. Il sait exactement quand son accès se termine. Pas de surprise.

**[ÉCRAN - screencast après expiration]**

[Montre ce qui se passe quand l'accès expire]

Une fois le délai dépassé :
- L'élève ne peut plus accéder au contenu du cours
- Le cours apparaît toujours dans son historique, mais marqué comme expiré
- Si tu le souhaites, l'élève peut se réinscrire - en rachetant le cours ou via une action manuelle de ta part

**[ÉCRAN - screencast cas d'usage]**

[Montre deux exemples de configuration]

Deux cas d'usage courants :

1. Formation premium à accès limité - 12 mois d'accès après l'achat. Ça pousse l'élève à suivre la formation dans un temps raisonnable et te permet de vendre un renouvellement.
2. Essai gratuit - 14 ou 30 jours d'accès à un cours gratuit. Après, l'élève doit acheter pour continuer.

**[TRANSITION - face caméra]**

L'expiration d'inscription est un levier business important. Elle crée une urgence naturelle et te permet de monétiser les renouvellements. Prochaine leçon : on voit comment vendre à des visiteurs qui n'ont pas encore de compte - l'achat invité.

---

**Points clés** :
- Enrollment Expiry activé par cours dans les réglages du Course Builder
- Durée configurable en jours (commence à l'inscription de l'élève)
- L'élève voit la date d'expiration dans son dashboard
- Après expiration : accès bloqué, possibilité de renouvellement
- Cas d'usage : accès limité 12 mois, essai gratuit 14-30 jours

**Mots clés SEO** : expiration inscription TutorLMS, accès limité cours WordPress, enrollment expiry TutorLMS, durée accès formation LMS

---

### Leçon 11.8 : Achat invité (Guest Purchase)

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast réglages Guest Purchase
**Source** : doc tutorials/guest-purchase

---

**[INTRO - face caméra]**

Par défaut, un visiteur doit créer un compte avant de pouvoir acheter un cours. Ça ajoute une étape, et chaque étape supplémentaire fait perdre des acheteurs. Le Guest Purchase permet à un visiteur d'acheter un cours sans créer de compte au préalable. TutorLMS crée le compte automatiquement après le paiement.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Monetization > Checkout]

Pour activer le Guest Purchase, va dans Tutor LMS, Settings, Monetization, puis Checkout. Cherche l'option "Guest Checkout" ou "Allow guest users to purchase courses". Active le toggle.

**[ÉCRAN - screencast configuration]**

[Montre les options liées au Guest Purchase]

Quand le Guest Purchase est actif, le processus d'achat change :

1. Le visiteur ajoute un cours au panier sans être connecté
2. Sur la page de paiement, il entre son email et ses informations de paiement
3. Après le paiement, TutorLMS crée automatiquement un compte avec cet email
4. L'élève reçoit un email avec ses identifiants de connexion

Pas de formulaire d'inscription, pas de mot de passe à choisir avant l'achat. Le frein est supprimé.

**[ÉCRAN - screencast front-end parcours achat]**

[Montre le parcours complet d'un achat invité]

Voici le parcours complet d'un achat invité : le visiteur clique sur "Buy Now", entre son email et sa carte, valide le paiement, et reçoit immédiatement accès au cours. Son compte est créé en arrière-plan.

**[ÉCRAN - screencast back-office vérification]**

[Montre le nouvel utilisateur créé automatiquement]

Côté admin, tu vois le nouvel utilisateur dans la liste WordPress, avec le cours acheté lié à son compte. Tout est automatique.

**[TRANSITION - face caméra]**

Le Guest Purchase est un quick win pour améliorer ton taux de conversion. Moins d'étapes, plus de ventes. Prochaine leçon : on voit comment limiter l'inscription à un seul cours par utilisateur - utile pour les offres exclusives.

---

**Points clés** :
- Guest Checkout activé dans Settings > Monetization > Checkout
- Le visiteur achète sans créer de compte au préalable
- TutorLMS crée le compte automatiquement après le paiement
- Email avec identifiants envoyé automatiquement
- Réduit le frein à l'achat et améliore la conversion

**Mots clés SEO** : guest purchase TutorLMS, achat sans compte LMS WordPress, guest checkout TutorLMS, achat invité formation WordPress

---

### Leçon 11.9 : Limiter un cours par utilisateur

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast réglages limitation
**Source** : doc tutorials/limit-one-course

---

**[INTRO - face caméra]**

Dans certains cas, tu veux qu'un utilisateur ne puisse s'inscrire qu'à un seul cours. Par exemple, pour une offre d'essai où chaque nouvel inscrit a droit à un cours gratuit. Ou pour éviter qu'un élève s'inscrive à tous tes cours gratuits sans jamais passer à l'achat. TutorLMS permet de poser cette limite.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings]

Va dans Tutor LMS, puis Settings. Cherche l'option "Limit Enrollment per Student" ou "Enrollment Restriction". Selon ta version de TutorLMS, cette option peut être dans l'onglet General ou dans les réglages avancés.

**[ÉCRAN - screencast configuration]**

[Montre les options de limitation]

L'option te permet de définir le nombre maximum de cours auxquels un étudiant peut s'inscrire. Par défaut, c'est illimité. Tu peux le passer à 1 pour une offre d'essai, à 3 pour un plan basique, ou à n'importe quel nombre qui correspond à ton modèle.

**[ÉCRAN - screencast front-end tentative d'inscription]**

[Montre ce qui se passe quand un élève dépasse la limite]

Quand un élève atteint sa limite et essaye de s'inscrire à un cours supplémentaire, TutorLMS affiche un message d'erreur. L'inscription est bloquée. L'élève doit upgrader son plan ou se désinscrire d'un cours existant.

**[ÉCRAN - screencast cas d'usage]**

[Montre un scénario concret]

Scénario concret : tu proposes un plan gratuit avec accès à 1 cours, un plan Standard avec 3 cours, et un plan Premium avec accès illimité. Tu configures la limite en fonction du plan de chaque utilisateur. C'est un levier de monétisation efficace.

**[TRANSITION - face caméra]**

La limitation par utilisateur fonctionne bien avec les memberships qu'on a vues dans le module eCommerce. Combine les deux pour créer des offres à paliers. Prochaine leçon - la dernière du module : on configure le profil instructeur visible par les élèves.

---

**Points clés** :
- Limite configurable dans Settings (nombre max de cours par étudiant)
- Par défaut : illimité. Modifiable à 1, 3, ou tout nombre
- Message d'erreur affiché quand la limite est atteinte
- Combiné avec les memberships pour créer des offres à paliers

**Mots clés SEO** : limiter cours par utilisateur TutorLMS, restriction inscription LMS WordPress, enrollment limit TutorLMS, limite cours élève TutorLMS

---

### Leçon 11.10 : Profil instructeur (frontend)

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast profil instructeur front-end
**Source** : doc tutorials/editing-instructor-profile

---

**[INTRO - face caméra]**

Le profil instructeur, c'est la page publique qui présente un formateur à tes élèves. Photo, bio, liste de cours, évaluation - tout est visible. Un bon profil inspire confiance et aide à convertir. Dans cette leçon, on voit comment un instructeur configure son profil depuis le front-end, sans passer par le back-office.

**[ÉCRAN - screencast front-end instructeur]**

[Connexion en tant qu'instructeur > Dashboard]

Connecte-toi avec un compte instructeur. Depuis le dashboard TutorLMS, clique sur "Profile" ou sur le lien d'édition du profil.

**[ÉCRAN - screencast édition du profil]**

[Montre le formulaire d'édition du profil]

Le formulaire de profil instructeur contient plusieurs sections :

1. Photo de profil - l'avatar visible sur les pages de cours et la page profil
2. Nom d'affichage - le nom que les élèves voient
3. Designation - le titre professionnel, par exemple "Expert WordPress" ou "Formateur SEO"
4. Bio - le texte de présentation. C'est l'élément le plus important. Écris quelques phrases qui résument ton expertise et ce que l'élève va apprendre avec toi.

**[ÉCRAN - screencast champs supplémentaires]**

[Montre les réseaux sociaux et autres champs]

En dessous, tu trouves les champs optionnels :
- Site web personnel
- Liens réseaux sociaux - Twitter, Facebook, LinkedIn, YouTube, GitHub
- Compétences / tags

Ces informations apparaissent sur la page publique du profil.

**[ÉCRAN - screencast page publique du profil]**

[Montre la page profil vue par un visiteur]

Voici ce que les élèves voient : la photo, le nom, la designation, la bio, les liens sociaux, et la liste des cours publiés par cet instructeur. La note moyenne et le nombre d'élèves s'affichent aussi si les avis sont activés.

**[ÉCRAN - screencast bonnes pratiques]**

[Montre un profil bien rempli vs un profil vide]

Comparaison rapide : un profil complet avec photo professionnelle, bio détaillée et liens sociaux inspire confiance. Un profil vide avec juste un nom - ça fait amateur. Prends le temps de bien remplir chaque champ.

**[TRANSITION - face caméra]**

Le profil instructeur est souvent négligé, mais c'est un facteur de confiance direct pour tes élèves. Assure-toi que chaque formateur sur ton site a un profil complet et professionnel. Avant le quiz, une dernière leçon décisive : protéger tes vidéos contre le vol et le partage non autorisé.

---

**Points clés** :
- Édition du profil accessible depuis le dashboard front-end
- Champs clés : photo, nom, designation, bio, réseaux sociaux
- La page publique affiche aussi les cours, la note moyenne et le nombre d'élèves
- Un profil complet inspire confiance et améliore la conversion

**Mots clés SEO** : profil instructeur TutorLMS, page formateur LMS WordPress, personnaliser profil TutorLMS, instructor profile TutorLMS frontend

---

### Leçon 11.11 : Protéger le contenu vidéo de tes cours

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS Settings (Advanced + Authentication) et démonstrations front-end
**Source** : doc tutorials/content-security + blog Themeum protect-elearning-course-videos (avril 2026)

---

**[INTRO - face caméra]**

Tes vidéos, c'est ton actif le plus précieux. C'est aussi le plus vulnérable. Un texte ou un PDF, ça se copie. Une vidéo, ça se partage, ça s'enregistre, ça se rediffuse. Dans cette leçon, on verrouille ton contenu vidéo couche par couche. Parce qu'aucun réglage ne protège tout seul : la vraie sécurité, c'est de l'empilement. Si une couche cède, les autres tiennent.

**[ÉCRAN - face caméra ou slide]**

Commençons par le modèle de menace. Quatre attaques concrètes guettent tes vidéos :

1. Le vol d'URL directe : quelqu'un récupère le lien brut de ta vidéo et le partage en dehors de ton site.
2. L'enregistrement d'écran, puis la redistribution.
3. Le partage d'identifiants : un compte acheté, dix personnes qui regardent. C'est le problème Netflix.
4. Le téléchargement massif suivi d'une demande de remboursement.

À chaque attaque, on va poser une défense.

**[ÉCRAN - screencast page de cours]**

Première couche, le socle : l'accès. Pas d'inscription, pas de vidéo. On l'a vu en leçon 11.1 avec la vérification email, qui filtre les faux comptes. Et attention au piège du preview : en leçon 7.5, on a activé le Course Preview pour donner un avant-goût. Mets-le uniquement sur tes leçons d'introduction. Si tu actives le preview sur le coeur de ton cours, tu l'as rendu gratuit sans t'en rendre compte.

**[ÉCRAN - screencast Tutor LMS > Settings > Advanced > Content Security]**

Deuxième couche, la plus importante si tu héberges tes vidéos toi-même : bloquer le partage d'URL. Va dans Tutor LMS, Settings, onglet Advanced, section Content Security. Active "Prevent Hotlinking".

Ce que ça fait : ta vidéo auto-hébergée ne se lit plus que depuis ton domaine. Si quelqu'un copie le lien brut du fichier et le colle ailleurs, c'est bloqué.

Note technique : cette option écrit dans ton fichier point-htaccess, sur un hébergement de type Apache. Si tu vois un avertissement sur l'accès au point-htaccess après avoir enregistré, vérifie que TutorLMS a bien les droits d'écriture sur ce fichier.

Et si tu utilises Bunny.net, qu'on a vu au module 16 : il faut aussi activer la restriction par domaine côté Bunny.net. La protection de TutorLMS couvre la couche WordPress, pas ton CDN. Les deux se règlent séparément.

**[ÉCRAN - screencast toggle Copy Protection + démo clic droit]**

Troisième couche, la friction anti-copie. Toujours dans Settings, Advanced, Content Security : active "Copy Protection". Ça désactive le clic droit. Plus de "Enregistrer la vidéo sous", plus de copie de l'URL source depuis le menu contextuel.

Sois honnête avec toi-même sur ce que ça fait : ça désactive le clic droit sur tout ton site, ton blog compris, pas seulement tes pages de cours. Donc si tu as une partie publique soignée, pèse la décision. Et ça arrête le vol occasionnel, pas un pirate déterminé qui sait ouvrir les outils développeur. C'est de la friction, pas un coffre-fort. Mais empilée avec les autres couches, elle compte.

**[ÉCRAN - screencast Settings > Authentication > Manage Active Logins]**

Quatrième couche : couper le partage d'identifiants. Va dans Settings, onglet Authentication, section Manage Active Logins. Active "Limit Active Login Sessions" et règle "Maximum Active Sessions" sur 1 ou 2.

Résultat : au-delà de la limite, toute nouvelle connexion est bloquée tant que l'utilisateur n'a pas fermé une session existante. Un compte, une ou deux personnes maximum. Le partage à dix, c'est terminé.

**[ÉCRAN - screencast rappel Content Drip]**

Cinquième couche : freiner le téléchargement massif. C'est le Content Drip, qu'on a configuré en leçon 7.1. L'angle sécurité : si tout ton cours est disponible d'un coup, quelqu'un peut tout aspirer en 24 heures, puis demander un remboursement. Avec le drip, les leçons se débloquent progressivement. L'aspiration devient beaucoup plus pénible. Couple ça avec une politique de remboursement claire.

**[ÉCRAN - face caméra + capture Bunny.net]**

Sixième couche : tracer les fuites avec le watermarking. Sois clair sur un point : TutorLMS ne fait pas de watermarking dynamique tout seul. Il faut un hébergeur vidéo tiers. La reco schoolsWP, c'est Bunny.net Stream dès cinquante vidéos : il incruste un identifiant unique lié à chaque spectateur. Si une vidéo fuit, tu sais quel compte est à l'origine. Les alternatives : VdoCipher, un DRM dédié, ou Vimeo pour un watermark texte plus basique.

**[ÉCRAN - face caméra + tableau récap]**

Septième couche, déjà en place : la vérification email de la leçon 11.1, qui bloque les faux comptes et les bots dès l'entrée.

Récapitulons ta pile de sécurité. [Afficher le tableau menace vers défense.] Chaque ligne, c'est une attaque et sa parade. Empile-les toutes et tu as une défense sérieuse.

| Menace | Défense |
| --- | --- |
| Regarder sans payer | Inscription obligatoire + Preview limité (L7.5) |
| Enregistrer en masse avant remboursement | Content Drip (L7.1) |
| Partage de l'URL vidéo brute | Prevent Hotlinking + restriction domaine CDN |
| Copie et "enregistrer sous" | Copy Protection (clic droit désactivé) |
| Partage d'identifiants | Limit Active Login Sessions |
| Redistribution d'un enregistrement | Watermarking via Bunny.net / VdoCipher |
| Faux comptes et bots | Email Verification (L11.1) |

**[TRANSITION - face caméra]**

Tu n'arrêteras pas le pirate le plus motivé : aucun système ne le fait. Mais tu rends le vol difficile, traçable et coûteux en temps. La grande majorité des gens passera son chemin. Tes vidéos représentent un vrai travail, elles méritent une vraie protection. Ça conclut le module 11. On termine avec le quiz pour valider tes acquis.

---

**Points clés** :
- La sécurité vidéo est un empilement : aucune couche ne suffit seule.
- Prevent Hotlinking (Settings > Advanced > Content Security) bloque le partage de l'URL brute. Écrit dans le point-htaccess, à coupler avec la restriction domaine du CDN.
- Copy Protection désactive le clic droit sur tout le site : décision à prendre en connaissance de cause.
- Limit Active Login Sessions (Settings > Authentication) coupe le partage d'identifiants.
- Le Content Drip (leçon 7.1) freine le téléchargement massif avant remboursement.
- Le watermarking n'est pas natif : il passe par Bunny.net, VdoCipher ou Vimeo.
- Aucune promesse de risque zéro : on rend le vol difficile, traçable et coûteux.

**Mots clés SEO** : protéger vidéos cours TutorLMS, sécuriser contenu LMS WordPress, prevent hotlinking TutorLMS, copy protection TutorLMS, limiter sessions connexion TutorLMS, watermark vidéo formation en ligne

---

### Leçon 11.12 : Quiz Module 11

**Durée** : ~6 min (11 questions)
**Type** : Quiz TutorLMS
**Seuil de réussite** : 70%

---

**Question 1**
Où active-t-on l'inscription étudiant dans TutorLMS ?

- A) Tutor LMS > Addons > Student Registration
- B) Settings > General > Student Registration ✓
- C) Settings > Monetization > Users
- D) WordPress > Settings > General

**Explication** : L'inscription étudiant s'active dans Tutor LMS > Settings > General > Student Registration.

---

**Question 2**
Pourquoi recommande-t-on l'approbation manuelle pour les instructeurs ?

- A) Pour accélérer le processus d'inscription
- B) Pour éviter que des formateurs non qualifiés publient du contenu ✓
- C) Pour limiter le nombre d'instructeurs à un seul
- D) Pour empêcher les instructeurs de modifier leurs cours

**Explication** : L'approbation manuelle permet de contrôler la qualité en vérifiant chaque candidature avant de donner les droits de création de cours.

---

**Question 3**
Quelles informations faut-il pour configurer le Social Login Google ?

- A) Un API Key et un Secret Token
- B) Un Client ID et un Client Secret créés dans Google Cloud Console ✓
- C) Un App ID et un App Secret créés dans Google Ads
- D) Un username et un mot de passe Google

**Explication** : Le Social Login Google nécessite un Client ID et un Client Secret, créés dans Google Cloud Console > APIs & Services > Credentials.

---

**Question 4**
Où crée-t-on l'App ID Facebook pour le Social Login ?

- A) Dans les paramètres Facebook personnels
- B) Sur developers.facebook.com en créant une nouvelle application ✓
- C) Dans Google Cloud Console
- D) Dans les réglages WordPress

**Explication** : L'App ID Facebook se crée sur developers.facebook.com via "Create App" avec le use case "Facebook Login".

---

**Question 5**
Quelle version de reCAPTCHA est supportée nativement par TutorLMS ?

- A) reCAPTCHA v3 invisible
- B) reCAPTCHA v2 "I'm not a robot" checkbox ✓
- C) reCAPTCHA Enterprise
- D) hCaptcha

**Explication** : TutorLMS supporte nativement reCAPTCHA v2 avec la checkbox "I'm not a robot".

---

**Question 6**
Quels sont les trois modes d'inscription de l'addon Enrollment ?

- A) Free, Paid, Premium
- B) Open, Closed, By Date ✓
- C) Manual, Automatic, Scheduled
- D) Instant, Delayed, Recurring

**Explication** : L'addon Enrollment propose trois modes : Open (permanent), Closed (fermé), et By Date (fenêtre avec date de début et fin).

---

**Question 7**
À partir de quand commence le décompte de l'expiration d'inscription ?

- A) À la date de création du cours
- B) À la date d'inscription de l'élève ✓
- C) À la date de première connexion de l'élève
- D) À la date de fin de la fenêtre d'inscription

**Explication** : La durée d'expiration se calcule à partir de la date d'inscription de chaque élève, pas de la date de création du cours.

---

**Question 8**
Que se passe-t-il après un Guest Purchase ?

- A) Le visiteur doit créer un compte manuellement après l'achat
- B) TutorLMS crée automatiquement un compte et envoie les identifiants par email ✓
- C) L'accès au cours est temporaire sans compte
- D) L'admin doit valider l'achat et créer le compte

**Explication** : Avec le Guest Purchase, TutorLMS crée automatiquement un compte avec l'email saisi et envoie les identifiants de connexion par email.

---

**Question 9**
Quel est l'intérêt de limiter le nombre de cours par utilisateur ?

- A) Réduire la charge serveur
- B) Créer des offres à paliers et encourager l'upgrade vers un plan supérieur ✓
- C) Empêcher les élèves de tricher aux quiz
- D) Faciliter la gestion des certificats

**Explication** : Limiter les cours par utilisateur permet de créer des plans (gratuit = 1 cours, standard = 3, premium = illimité) et incite les élèves à upgrader.

---

**Question 10**
Quel élément du profil instructeur a le plus d'impact sur la confiance des élèves ?

- A) Le nombre de réseaux sociaux renseignés
- B) Le nom d'affichage
- C) La bio détaillant l'expertise et les bénéfices pour l'élève ✓
- D) L'URL du site personnel

**Explication** : La bio est l'élément le plus important du profil instructeur. Elle résume l'expertise du formateur et ce que l'élève va apprendre - c'est le facteur de confiance principal.

---

**Question 11**
Quel réglage TutorLMS désactive le clic droit sur l'ensemble du site pour freiner la copie des vidéos ?

- A) Prevent Hotlinking
- B) Copy Protection ✓
- C) Content Drip
- D) Limit Active Login Sessions

**Explication** : Copy Protection désactive le menu contextuel (clic droit) sur tout le site, ce qui empêche "Enregistrer sous" et la copie de l'URL source. C'est une couche de friction, pas une protection absolue.

---

**Fin du Module 11.**

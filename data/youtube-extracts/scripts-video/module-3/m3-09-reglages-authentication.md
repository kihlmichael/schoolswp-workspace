# Module 3 — Lecon 9 : Reglages Authentication
> Duree estimee : 4 min | Type : Adapte du transcript video #18

## Script de narration

[INTRO]

L'authentification, c'est la securite de ta plateforme. Double authentification, protection anti-spam, limite d'appareils, verification email et connexion sociale — Tutor LMS Pro offre cinq mecanismes de protection. On les configure ensemble.

[CONTENU]

L'onglet Authentication est disponible uniquement dans Tutor LMS Pro. Rends-toi dans Tutor LMS, Reglages, onglet Authentication.

[CAPTURE ECRAN : Menu Settings > Authentication]

Avant de commencer, un point important : les fonctionnalites d'authentification de Tutor LMS peuvent entrer en conflit avec des plugins de cache ou de securite WordPress tiers. Pour eviter les problemes, ne mets pas en cache la page de connexion et la page d'inscription de Tutor LMS.

Cinq sections t'attendent. On les prend une par une.

**Section 1 : Authentification a deux facteurs (2FA)**

Active le toggle pour activer la double authentification. Quand un eleve ou un instructeur se connecte ou s'inscrit, il recoit un code a 6 chiffres par email qu'il doit saisir pour continuer.

[CAPTURE ECRAN : Toggle 2FA active]

Deux sous-options apparaissent. La methode — pour l'instant, seule la verification par email est disponible. Et l'emplacement — tu choisis ou appliquer la 2FA : page de connexion Tutor, page de connexion WordPress, ou les deux.

[CAPTURE ECRAN : Options Methode et Emplacement de la 2FA]

Prerequis : tu dois avoir un SMTP configure sur ton site WordPress pour que les emails soient envoyes correctement. Sans SMTP, les codes ne partiront pas.

**Section 2 : Protection anti-fraude**

Active le toggle pour proteger ta plateforme contre les spammeurs et les bots.

[CAPTURE ECRAN : Toggle Fraud Protection active]

Tu choisis ta methode de protection parmi trois options.

Honeypot : un piege invisible. Un champ de texte cache est ajoute au formulaire. Les bots le remplissent automatiquement et sont bloques. Pas de cle a configurer — c'est le plus simple.

[CAPTURE ECRAN : Selection Honeypot]

reCAPTCHA v2 : la case "Je ne suis pas un robot" classique, suivie d'un defi visuel. Tu dois fournir une cle de site et une cle secrete obtenues sur la console Google reCAPTCHA.

[CAPTURE ECRAN : Selection reCAPTCHA v2 avec les champs de cle]

reCAPTCHA v3 : la version la plus avancee. Pas de defi visible — Google analyse le comportement de l'utilisateur en arriere-plan et lui attribue un score. Si le score est satisfaisant, aucune verification n'est demandee. C'est la methode recommandee.

[CAPTURE ECRAN : Selection reCAPTCHA v3 avec les champs Site Key et Secret Key]

Tu choisis aussi les emplacements ou appliquer la protection : page de connexion, page d'inscription, ou les deux.

[CAPTURE ECRAN : Cases a cocher des emplacements]

**Section 3 : Limite d'appareils actifs**

Cette option te permet de controler combien d'appareils un eleve peut utiliser simultanement pour acceder a ta plateforme.

[CAPTURE ECRAN : Toggle Limit Active Devices]

En l'activant, un champ apparait. Si tu mets 2, l'eleve pourra se connecter depuis deux appareils — son ordinateur et son telephone, par exemple. S'il essaie de se connecter depuis un troisieme appareil, il sera bloque.

[CAPTURE ECRAN : Champ nombre d'appareils avec valeur 2]

C'est une protection utile contre le partage de comptes non autorise.

**Section 4 : Verification email**

Active cette option pour exiger une verification email lors de l'inscription. Chaque nouvel eleve ou instructeur recoit un lien de verification dans sa boite email. Sans clic sur ce lien, l'inscription n'est pas validee.

[CAPTURE ECRAN : Toggle Email Verification]

Meme prerequis que pour la 2FA : ton serveur mail doit etre correctement configure (SMTP). Sans ca, les utilisateurs ne recevront pas le lien et resteront bloques a l'inscription.

**Section 5 : Connexion sociale (Social Login)**

Avant de configurer cette section, tu dois activer l'add-on Social Login. Va dans Tutor LMS, Add-ons, et active le toggle "Social Login".

[CAPTURE ECRAN : Page Add-ons avec le toggle Social Login active]

De retour dans les reglages Authentication, la section Social Login apparait. Tu peux activer la connexion via Google, Facebook ou Twitter.

[CAPTURE ECRAN : Trois toggles pour Google, Facebook et Twitter]

Pour chaque reseau, tu dois fournir un identifiant : Client ID pour Google, App ID pour Facebook, et les cles App ID/Secret pour Twitter. Ces identifiants s'obtiennent depuis les consoles developpeurs respectives de chaque plateforme.

[CAPTURE ECRAN : Champs de cle pour chaque reseau social]

Une fois les cles renseignees, la connexion sociale est active. Tes eleves verront des boutons "Se connecter avec Google", "Se connecter avec Facebook", etc. sur les pages de connexion et d'inscription.

[CAPTURE ECRAN : Apercu front-end des boutons de connexion sociale]

[RECAP]

Cinq mecanismes de securite pour ta plateforme : 2FA, anti-fraude, limite d'appareils, verification email et connexion sociale. Tu n'es pas oblige de tout activer — au minimum, la protection anti-fraude avec reCAPTCHA v3 et la verification email sont fortement recommandees. Avec ca, le Module 3 est termine — tu as configure l'integralite des reglages de Tutor LMS.

## Notes de production
- Captures ecran necessaires : chaque section avec son toggle, options methode/emplacement pour 2FA et anti-fraude, champ limite d'appareils, activation add-on Social Login, champs de cle par reseau, apercu front-end boutons sociaux
- Points d'attention : avertissement sur le cache en debut de lecon (conflit plugins securite), rappeler le prerequis SMTP pour 2FA et verification email, recommander reCAPTCHA v3 comme meilleure option

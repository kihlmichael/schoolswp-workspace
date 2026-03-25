# Module 1 — Lecon 1 : Pre-requis systeme
> Duree estimee : 2 min | Type : A creer

## Script de narration

[INTRO]
Avant d'installer Tutor LMS, tu dois verifier que ton hebergement remplit les conditions techniques minimales. On va passer en revue chaque pre-requis pour eviter les mauvaises surprises.

[CONTENU]
Tutor LMS a besoin de quatre elements pour fonctionner correctement.

Premier element : la version de PHP. Tu dois avoir PHP 7.4 au minimum. En pratique, je te recommande PHP 8.1 ou superieur pour de meilleures performances et une meilleure securite.

[CAPTURE ECRAN : panneau hebergeur montrant la version PHP active]

Deuxieme element : la base de donnees. MariaDB 10.1 ou superieur, ou bien MySQL 5.7 ou superieur. La plupart des hebergeurs modernes sont deja conformes sur ce point.

Troisieme element : WordPress. Tu as besoin de WordPress 5.8 au minimum. La encore, je te conseille de toujours utiliser la derniere version stable de WordPress, a la fois pour la securite et la compatibilite.

[CAPTURE ECRAN : tableau de bord WordPress montrant la version installee dans "Mises a jour"]

Quatrieme element : les extensions PHP requises. Assure-toi que les extensions suivantes sont activees sur ton serveur : curl, mbstring, zip, et gd. Elles sont generalement activees par defaut, mais ca vaut le coup de verifier dans ton panneau d'hebergement.

[CAPTURE ECRAN : phpinfo ou panneau hebergeur montrant les extensions PHP actives]

Maintenant, parlons hebergement. Tous les hebergeurs ne se valent pas pour faire tourner un LMS. Un LMS genere plus de requetes qu'un site vitrine classique : inscriptions, suivi de progression, quiz, certificats...

Les hebergeurs que je recommande pour Tutor LMS :

- Cloudways : excellent rapport qualite-prix, serveurs optimises, tu choisis ton infrastructure (DigitalOcean, Vultr, AWS).
- Kinsta : hebergement WordPress manage sur Google Cloud, tres performant, support reactif.
- WP Engine : specialiste WordPress, bon pour les sites a fort trafic.

[CAPTURE ECRAN : tableau comparatif des 3 hebergeurs avec prix d'entree et points forts]

A eviter : les hebergements mutualises premiers prix. Avec un LMS actif et plusieurs dizaines d'etudiants, tu risques des lenteurs et des erreurs de timeout.

Un dernier point : la memoire PHP. Par defaut, WordPress alloue 256 Mo. Pour Tutor LMS, je te recommande de monter a 512 Mo minimum. Tu peux le faire via ton fichier wp-config.php en ajoutant la ligne define WP_MEMORY_LIMIT a 512M.

[CAPTURE ECRAN : fichier wp-config.php avec la ligne WP_MEMORY_LIMIT mise en evidence]

[RECAP]
En resume, verifie ces quatre points avant d'installer Tutor LMS : PHP 7.4 minimum, MariaDB 10.1 ou MySQL 5.7, WordPress 5.8 minimum, et les extensions PHP essentielles. Choisis un hebergeur performant adapte au LMS, et monte ta memoire PHP a 512 Mo. Une fois tout ca en place, tu es pret pour l'installation.

## Notes de production
- Captures ecran necessaires : panneau hebergeur version PHP, tableau de bord WordPress version, phpinfo extensions, tableau comparatif hebergeurs, wp-config.php WP_MEMORY_LIMIT
- Points d'attention : ne pas citer de prix precis (ils changent), rester factuel sur les hebergeurs sans promesse exageree

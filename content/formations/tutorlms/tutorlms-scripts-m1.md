# Scripts video — Module 1 : Demarrage & Installation

**Formation** : Maitriser TutorLMS
**Module** : M1 — Demarrage & Installation (Gratuit)
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~35 min
**Date** : 2026-03-23

---

### Lecon 1.1 — Pre-requis systeme

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides pour les specs, screencast rapide du dashboard hosting

---

**[INTRO — face camera]**

Avant d'installer TutorLMS, il faut verifier que ton hebergement WordPress est pret. Si tu installes le plugin sur un serveur trop lent ou une version de PHP obsolete, tu vas avoir des problemes. Dans cette lecon, je te donne la checklist exacte des pre-requis.

**[ECRAN — slide "Pre-requis techniques TutorLMS"]**

TutorLMS a besoin de quatre choses pour fonctionner correctement.

Premiere chose : WordPress 5.3 minimum. En pratique, utilise toujours la derniere version stable de WordPress. Au moment ou je tourne cette video, c'est WordPress 6.7. Si tu es en retard de plusieurs versions majeures, mets a jour avant d'installer TutorLMS.

Deuxieme chose : PHP 7.4 minimum. La encore, je te recommande PHP 8.1 ou 8.2. C'est plus rapide, plus securise, et tous les plugins modernes le supportent. Si tu es encore en PHP 7.4, c'est le moment de demander a ton hebergeur de monter la version.

**[ECRAN — slide "Memoire & Serveur"]**

Troisieme chose : une limite memoire PHP de 256 Mo minimum. Par defaut, beaucoup d'hebergeurs mettent 128 Mo. C'est insuffisant pour un LMS. Tu vas charger des cours, des videos, des quiz — ca consomme de la memoire. 256 Mo est le minimum, 512 Mo est confortable.

Quatrieme chose : un hebergement WordPress de qualite. TutorLMS genere beaucoup de requetes en base de donnees — chaque cours, chaque lecon, chaque quiz est un Custom Post Type avec des metadonnees. Un hebergement mutualise a 3 euros par mois ne tiendra pas la charge avec 50 etudiants connectes en meme temps.

**[ECRAN — screencast du dashboard hebergement]**

[Montre le panneau de controle d'un hebergeur — section PHP et memoire]

Pour verifier ta version de PHP et ta limite memoire, va dans le panneau de controle de ton hebergeur. Chez la plupart des hebergeurs — OVH, o2switch, Infomaniak, Cloudways — tu trouveras ces infos dans la section PHP ou configuration du serveur.

Si tu ne trouves pas, installe le plugin "Site Health" de WordPress. Va dans Outils, puis Sante du site, puis Informations. Tu verras la version PHP, la limite memoire, et la version de WordPress.

**[ECRAN — slide "Hebergements recommandes"]**

Pour un site LMS avec TutorLMS, je recommande trois types d'hebergement.

Pour debuter avec moins de 100 etudiants : o2switch ou Infomaniak. Hebergement mutualise performant, support francophone, tarif raisonnable.

Pour monter en charge entre 100 et 1000 etudiants : un VPS manage type Cloudways ou SpinupWP. Tu as des ressources dediees, et la performance suit.

Au-dela de 1000 etudiants actifs : un serveur dedie ou un hebergement specialise WordPress comme Starter Starter ou Starter Starter.

Sur schoolsWP, j'utilise Starter Starter avec Cloudways. Ca me permet de gerer les formations, le blog, et le trafic SEO sans souci de performance.

**[TRANSITION — face camera]**

Recapitulons. WordPress 5.3 ou plus recent, PHP 7.4 ou plus recent — idealement 8.1 ou 8.2 — et 256 Mo de memoire minimum. Si ton hebergement coche ces trois cases, tu es pret pour l'installation. C'est ce qu'on fait dans la prochaine lecon.

---

**Points cles** :
- WordPress 5.3+ (recommande : derniere version stable)
- PHP 7.4+ (recommande : 8.1 ou 8.2)
- Memoire PHP : 256 Mo minimum, 512 Mo recommande
- Hebergement adapte : pas de mutualise bas de gamme pour un LMS
- Outil de verification : Site Health dans WordPress

**Mots cles SEO** : pre-requis TutorLMS, hebergement TutorLMS WordPress, configuration serveur LMS WordPress, PHP TutorLMS

---

### Lecon 1.2 — Installation Tutor LMS Free + Pro

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast complet de l'installation
**Source** : Videos #2, #30 (TutorLMS Academy) — script original schoolsWP

---

**[INTRO — face camera]**

Dans cette lecon, tu installes TutorLMS sur ton site WordPress. D'abord la version gratuite depuis le repertoire officiel, puis le plugin Pro si tu as une licence. En 5 minutes, ton LMS est operationnel.

Petit detail qui fait la difference : la formation que tu suis en ce moment tourne sur TutorLMS Pro. Mon site schoolsWP utilise exactement le meme outil pour heberger ces cours. Ce n'est pas de la theorie — c'est ce que j'utilise au quotidien.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Extensions > Ajouter]

Etape 1 : dans ton tableau de bord WordPress, va dans Extensions, puis Ajouter.

[Tape "TutorLMS" dans la barre de recherche]

Etape 2 : dans la barre de recherche, tape "Tutor LMS". Le premier resultat devrait etre "Tutor LMS — eLearning and online course solution" par Themeum. Verifie que c'est bien l'editeur Themeum — il existe des plugins avec des noms similaires.

[Clique sur Installer maintenant]

Etape 3 : clique sur "Installer maintenant". WordPress telecharge le plugin. Ca prend quelques secondes.

[Clique sur Activer]

Etape 4 : une fois installe, clique sur "Activer".

**[ECRAN — screencast assistant de configuration]**

[Montre l'assistant de bienvenue TutorLMS]

Des l'activation, TutorLMS lance un assistant de configuration. Tu vas voir un ecran de bienvenue avec plusieurs etapes. On va les parcourir ensemble.

[Etape 1 de l'assistant]

Premiere etape : le type de site. Choisis si tu veux un marketplace multi-instructeurs ou un site mono-instructeur. Si c'est ton propre site de formation, choisis mono-instructeur. Tu pourras changer plus tard.

[Etape 2 de l'assistant]

Deuxieme etape : les pages. L'assistant propose de creer automatiquement les pages necessaires — page des cours, page du tableau de bord etudiant, page du tableau de bord instructeur. Laisse tout coche. Ces pages sont indispensables au fonctionnement du LMS.

[Etape 3 de l'assistant]

Troisieme etape : la passerelle de paiement. Si tu veux vendre des cours, tu configureras WooCommerce ou le systeme de monetisation integre plus tard. Pour l'instant, tu peux passer cette etape.

[Clique sur Terminer]

Etape 5 : clique sur Terminer. L'assistant cree les pages et configure les reglages de base.

**[ECRAN — screencast installation Pro]**

[Montre le site TutorLMS.com > Mon compte > Telechargements]

Maintenant, si tu as achete une licence TutorLMS Pro, voici comment installer le plugin premium.

Etape 6 : va sur le site tutorlms.com, connecte-toi a ton compte, et telecharge le fichier ZIP du plugin Pro depuis la section Telechargements.

[Retour dans WordPress > Extensions > Ajouter > Televerser une extension]

Etape 7 : retourne dans WordPress. Va dans Extensions, Ajouter, puis clique sur "Televerser une extension" en haut de la page. Selectionne le fichier ZIP que tu viens de telecharger.

[Clique sur Installer puis Activer]

Etape 8 : clique sur "Installer maintenant", puis sur "Activer". Le plugin Pro s'ajoute a cote du plugin gratuit — les deux fonctionnent ensemble.

**[ECRAN — screencast verification]**

[Montre le menu TutorLMS dans la sidebar WordPress]

Verifions que tout est en place. Dans le menu lateral de WordPress, tu devrais voir "Tutor LMS" avec ses sous-menus : Cours, Categories, Tags, Etudiants, Reglages, et si tu as le Pro, des options supplementaires comme les Certificats et les Rapports.

**[TRANSITION — face camera]**

TutorLMS est installe. Le plugin gratuit donne acces a la creation de cours, lecons, quiz et gestion des etudiants. Le Pro ajoute les certificats, les rapports avances, les types de questions supplementaires, et les addons. Dans la prochaine lecon, on active la licence Pro pour debloquer toutes les fonctionnalites.

---

**Points cles** :
- Installer TutorLMS Free depuis Extensions > Ajouter (editeur : Themeum)
- L'assistant de configuration cree les pages essentielles automatiquement
- TutorLMS Pro s'installe via un fichier ZIP telecharge depuis tutorlms.com
- Les deux plugins (Free + Pro) fonctionnent ensemble
- Verification : menu TutorLMS visible dans la sidebar WordPress

**Mots cles SEO** : installer TutorLMS WordPress, installation TutorLMS Pro, configurer TutorLMS, plugin LMS WordPress installation

---

### Lecon 1.3 — Activation de licence

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast de l'activation
**Source** : Videos #2, #30 (TutorLMS Academy) — script original schoolsWP

---

**[INTRO — face camera]**

Tu as installe TutorLMS Pro, mais sans activer ta licence, tu n'auras pas acces aux mises a jour automatiques ni au support. L'activation prend 2 minutes. Je te montre exactement ou aller et quoi faire.

**[ECRAN — screencast site TutorLMS.com]**

[Navigation vers Mon Compte > Licences]

Etape 1 : commence par recuperer ta cle de licence. Va sur tutorlms.com, connecte-toi a ton compte, et ouvre la section Licences. Tu y trouveras ta cle — une longue chaine de caracteres. Copie-la.

Un detail important : chaque licence a un nombre limite d'activations. Le plan basique permet une activation sur un seul site. Le plan Business en permet cinq. Verifie que tu n'as pas depasse ta limite avant d'activer.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Licence ou Settings > Licence]

Etape 2 : retourne dans ton WordPress. Va dans Tutor LMS, puis Reglages. Cherche l'onglet "Licence" ou "License". Selon la version, il peut etre dans les reglages generaux ou dans un sous-menu dedie.

[Colle la cle de licence]

Etape 3 : colle ta cle de licence dans le champ prevu. Clique sur "Activer" ou "Activate License".

[Montre le message de confirmation]

Si tout est correct, tu verras un message de confirmation en vert : "License activated successfully" ou equivalent. Le statut passe de "Inactive" a "Active".

**[ECRAN — screencast verification des mises a jour]**

[Navigation vers Extensions > Extensions installees]

Etape 4 : verifions que les mises a jour automatiques fonctionnent. Va dans Extensions, puis Extensions installees. A cote de "Tutor LMS Pro", tu devrais voir un lien "Verifier les mises a jour" ou une notification si une mise a jour est disponible. Si tu ne vois pas d'erreur de licence, c'est bon.

**[ECRAN — slide "Problemes courants"]**

Trois problemes frequents lors de l'activation.

Premier probleme : "License limit reached". Tu as deja utilise toutes tes activations. Va sur tutorlms.com, desactive la licence sur un ancien site, puis reactive ici.

Deuxieme probleme : "Invalid license key". Verifie que tu as copie la cle complete, sans espace au debut ou a la fin. Un copier-coller depuis un email ajoute parfois des caracteres invisibles.

Troisieme probleme : les mises a jour ne s'affichent pas. Vide le cache de ton site et celui de WordPress. Va dans Extensions installees, clique sur "Verifier les mises a jour" pour forcer la verification.

**[TRANSITION — face camera]**

Ta licence est activee. Tu as acces aux mises a jour automatiques et au support Themeum. Avant de commencer a creer des cours, il reste un reglage technique important a faire : les permalinks. C'est la prochaine lecon.

---

**Points cles** :
- Recuperer la cle de licence sur tutorlms.com > Mon Compte > Licences
- Activer dans WordPress : Tutor LMS > Reglages > Licence
- Chaque licence a un nombre limite d'activations selon le plan
- Sans activation : pas de mises a jour automatiques ni de support
- Problemes courants : limite atteinte, cle invalide, cache a vider

**Mots cles SEO** : activer licence TutorLMS Pro, cle de licence TutorLMS, activation TutorLMS WordPress

---

### Lecon 1.4 — Reglages Permalinks

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast des reglages

---

**[INTRO — face camera]**

Les permalinks, c'est la structure des URLs de ton site. Si tu ne les configures pas correctement, les pages de tes cours, les lecons et les quiz vont afficher des erreurs 404. C'est un reglage de 30 secondes, mais beaucoup de debutants l'oublient. On le fait maintenant.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Reglages > Permaliens]

Etape 1 : dans ton tableau de bord WordPress, va dans Reglages, puis Permaliens.

[Montre les differentes options de structure]

Tu as plusieurs structures disponibles. "Simple" utilise des numeros — c'est mauvais pour le SEO et incompatible avec TutorLMS. "Date et titre" ajoute la date dans l'URL — inutile pour des cours. "Nom de l'article" — c'est celle qu'il te faut.

Etape 2 : selectionne "Nom de l'article". Ca donne des URLs propres du type tonsite.com/mon-cours/ au lieu de tonsite.com/?p=123.

[Clique sur Enregistrer les modifications]

Etape 3 : clique sur "Enregistrer les modifications". Meme si la bonne option etait deja selectionnee, clique quand meme. WordPress regenere les regles de reecriture a chaque sauvegarde. Apres l'installation d'un plugin qui cree des Custom Post Types — comme TutorLMS — c'est indispensable.

**[ECRAN — slide "Pourquoi c'est important pour TutorLMS"]**

Pourquoi ce reglage est critique pour TutorLMS ?

TutorLMS cree plusieurs types de contenu personnalises : les cours, les lecons, les quiz, les devoirs. Chacun a sa propre structure d'URL. Par exemple : tonsite.com/courses/mon-premier-cours/ pour un cours, tonsite.com/courses/mon-cours/lesson/ma-lecon/ pour une lecon.

Si les permalinks sont en mode "Simple", WordPress ne sait pas interpreter ces URLs. Resultat : des pages 404 partout. C'est le probleme numero un rapporte par les debutants sur le forum TutorLMS.

**[ECRAN — screencast verification]**

[Ouvre un cours en front-end]

Etape 4 : verifions que tout fonctionne. Ouvre un cours en front-end — si tu as importe les donnees demo, utilise un des cours d'exemple. L'URL devrait etre propre, sans point d'interrogation ni numero.

[Montre l'URL dans la barre d'adresse]

L'URL affiche bien tonsite.com/courses/nom-du-cours/. Si tu vois une erreur 404, retourne dans Reglages > Permaliens et clique encore une fois sur "Enregistrer les modifications". Ca resout le probleme dans 90% des cas.

**[ECRAN — slide "Personnalisation des slugs TutorLMS"]**

Bonus : tu peux personnaliser les slugs de TutorLMS. Va dans Tutor LMS > Reglages > General, et cherche la section "URL Slugs" ou "Permalinks". Par defaut, les cours sont sous /courses/. Tu peux changer ca en /formations/ ou /cours/ si tu veux des URLs en francais.

Attention : si tu changes les slugs apres avoir publie des cours, toutes les URLs existantes vont changer. Pense a mettre en place des redirections 301 si tu fais ca.

**[TRANSITION — face camera]**

Tes permalinks sont configures. Les URLs de tes cours, lecons et quiz fonctionnent correctement. Dans la prochaine lecon, on regarde quels plugins sont compatibles avec TutorLMS — et lesquels eviter.

---

**Points cles** :
- Structure recommandee : "Nom de l'article" (post name)
- Toujours cliquer "Enregistrer" apres installation d'un plugin a Custom Post Types
- Erreur 404 sur les cours = permalinks a resauvegarder
- Slugs personnalisables dans Tutor LMS > Reglages (ex: /formations/ au lieu de /courses/)
- Changer les slugs apres publication = redirections 301 obligatoires

**Mots cles SEO** : permalinks TutorLMS, erreur 404 TutorLMS, reglages URL cours WordPress, slug TutorLMS

---

### Lecon 1.5 — Plugins compatibles

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides pour les categories, screencast rapide

---

**[INTRO — face camera]**

TutorLMS ne fonctionne pas seul. Tu vas avoir besoin de plugins pour les paiements, le SEO, le cache, les formulaires. Le probleme, c'est que certains plugins creent des conflits avec TutorLMS. Dans cette lecon, je te donne la liste des plugins testes et compatibles — et ceux a eviter.

**[ECRAN — slide "Plugins compatibles — Paiements"]**

Commencons par les plugins de paiement. C'est souvent la premiere question : comment vendre mes cours ?

WooCommerce est le choix principal. TutorLMS s'integre nativement avec WooCommerce pour vendre des cours individuels ou des abonnements. C'est la methode la plus flexible.

Easy Digital Downloads fonctionne aussi, avec un addon dedie.

TutorLMS a egalement son propre systeme de monetisation integre — sans WooCommerce. Si tu veux garder les choses simples et que tu n'as pas besoin d'un panier complet, c'est une option viable.

**[ECRAN — slide "Plugins compatibles — SEO"]**

Pour le SEO. RankMath est entierement compatible avec TutorLMS. Il detecte automatiquement les cours comme des types de contenu et te permet d'optimiser les meta titles, descriptions et le schema markup. C'est ce que j'utilise sur schoolsWP.

Yoast SEO fonctionne aussi. Les deux sont testes et valides par Themeum.

**[ECRAN — slide "Plugins compatibles — Performance"]**

Pour la performance et le cache. WP Rocket est compatible. LiteSpeed Cache aussi. W3 Total Cache fonctionne, mais demande plus de configuration.

Un point d'attention : si tu utilises un plugin de cache, assure-toi d'exclure les pages dynamiques de TutorLMS du cache. Le tableau de bord etudiant, la page de progression, la page de quiz — ces pages doivent afficher du contenu personnalise a chaque utilisateur. Si elles sont cachees, un etudiant verra la progression d'un autre.

**[ECRAN — slide "Plugins compatibles — Page Builders"]**

Pour les page builders. Elementor est officiellement supporte. TutorLMS fournit des widgets Elementor pour afficher les cours, les categories, les instructeurs. Gutenberg fonctionne nativement — TutorLMS fournit ses propres blocs.

Divi et Beaver Builder fonctionnent, mais sans widgets dedies. Tu utiliseras des shortcodes a la place.

**[ECRAN — slide "Plugins compatibles — Email & CRM"]**

Pour l'email et le CRM. FluentCRM est compatible — et c'est ce que j'utilise sur schoolsWP pour les sequences automatisees. Tu peux declencher des emails quand un etudiant s'inscrit a un cours, termine une lecon, ou echoue a un quiz.

MailChimp et ConvertKit fonctionnent aussi via des integrateurs comme AutomateWP ou des webhooks.

**[ECRAN — slide "Plugins a eviter ou a surveiller"]**

Maintenant, les plugins a surveiller.

LearnDash et LifterLMS : ce sont des concurrents directs. Ne les installe jamais en meme temps que TutorLMS. Ca peut sembler evident, mais j'ai vu des gens le faire.

Les plugins de membership comme MemberPress ou Restrict Content Pro : ils peuvent creer des conflits avec la gestion d'acces de TutorLMS. Si tu veux du membership, utilise plutot les fonctions natives de TutorLMS Pro ou l'integration WooCommerce Subscriptions.

Les plugins de securite trop agressifs : Wordfence ou iThemes Security avec des regles de pare-feu strictes peuvent bloquer les requetes AJAX de TutorLMS. Si tu rencontres des problemes de chargement dans l'editeur de cours, verifie les regles de ton plugin de securite.

**[TRANSITION — face camera]**

Tu as maintenant une vision claire des plugins compatibles. Retiens l'essentiel : WooCommerce pour les paiements, RankMath pour le SEO, WP Rocket pour le cache, et exclus toujours les pages dynamiques du cache. Dans la prochaine lecon, on parle des themes compatibles.

---

**Points cles** :
- Paiements : WooCommerce (natif), EDD (addon), ou monetisation integree
- SEO : RankMath et Yoast SEO valides
- Cache : WP Rocket, LiteSpeed — exclure les pages dynamiques TutorLMS
- Page builders : Elementor (widgets dedies), Gutenberg (blocs natifs)
- Email/CRM : FluentCRM, MailChimp, ConvertKit
- A eviter : autres LMS simultanes, membership plugins en conflit, securite trop agressive

**Mots cles SEO** : plugins compatibles TutorLMS, WooCommerce TutorLMS, RankMath TutorLMS, Elementor TutorLMS

---

### Lecon 1.6 — Themes compatibles

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides comparatifs, screencast rapide de demos

---

**[INTRO — face camera]**

Le theme que tu choisis impacte directement l'apparence de tes cours, la vitesse de ton site, et la compatibilite avec TutorLMS. Certains themes fonctionnent parfaitement, d'autres causent des problemes d'affichage. Dans cette lecon, je te montre lesquels choisir et pourquoi.

**[ECRAN — slide "Compatibilite theme + LMS : ce qu'il faut savoir"]**

TutorLMS utilise ses propres templates pour afficher les pages de cours, les lecons, le tableau de bord etudiant, et les quiz. Ton theme doit respecter ces templates sans les ecraser.

Concretement, un theme compatible avec TutorLMS, c'est un theme qui ne casse pas la mise en page des cours, qui supporte les Custom Post Types, et qui ne surcharge pas les templates TutorLMS avec ses propres layouts.

**[ECRAN — slide "Themes officiels Themeum"]**

Premier choix : les themes Themeum. C'est le meme editeur que TutorLMS, donc la compatibilite est garantie.

TutorStarter est le theme gratuit officiel. Il est leger, optimise pour TutorLMS, et disponible dans le repertoire WordPress. C'est un bon point de depart si tu debutes.

Flavstarter est le theme premium de Themeum. Plus de fonctionnalites de design, plus d'options de personnalisation, toujours 100% compatible.

**[ECRAN — slide "Themes tiers compatibles"]**

Deuxieme choix : les themes tiers testes et compatibles.

Astra est un excellent choix. Leger, rapide, compatible WooCommerce et TutorLMS. Il offre des starter templates dediees a l'education. C'est probablement le theme tiers le plus utilise avec TutorLMS.

GeneratePress : tres leger, performant, et compatible. Moins d'options de design qu'Astra, mais plus rapide.

Kadence : bon equilibre entre performance et fonctionnalites. Compatible TutorLMS.

OceanWP : compatible, avec beaucoup d'extensions gratuites.

Hello Elementor : si tu utilises Elementor comme page builder, c'est le theme le plus leger possible. Il laisse toute la mise en page a Elementor et ne cree pas de conflit avec les templates TutorLMS.

**[ECRAN — screencast demo d'un cours]**

[Montre la page d'un cours avec un theme compatible — ex: Astra]

Voici a quoi ressemble un cours avec un theme bien configure. La page de cours affiche la description, le curriculum, les avis, le prix — tout est en place. Le design est propre, la navigation fonctionne.

[Montre la meme page avec un theme problematique]

Et voici ce qui arrive avec un theme qui n'est pas prevu pour les LMS. La sidebar ecrase le contenu du cours. Les boutons d'inscription ne sont pas alignes. Le curriculum ne s'affiche pas correctement. C'est le genre de probleme qu'on evite en choisissant un theme compatible.

**[ECRAN — slide "Themes a eviter"]**

Les themes a eviter avec TutorLMS.

Les themes "all-in-one" surcharges : les themes qui integrent leur propre systeme de cours — comme Flavor LMS ou EduPro — vont entrer en conflit avec TutorLMS. Ne combine jamais un theme LMS avec un plugin LMS.

Les themes anciens non mis a jour depuis plus de 2 ans. S'ils ne supportent pas PHP 8+ et les derniers standards WordPress, ils vont poser des problemes.

Les themes avec des mises en page tres rigides qui ne supportent pas les Custom Post Types. Si le theme force un layout specifique sur toutes les pages, les templates TutorLMS ne s'afficheront pas correctement.

**[ECRAN — slide "Criteres de selection"]**

Pour resumer, voici tes criteres de selection.

Le theme doit etre activement maintenu — derniere mise a jour il y a moins de 3 mois. Il doit supporter PHP 8+. Il doit etre compatible avec les Custom Post Types. Il ne doit pas inclure son propre systeme LMS. Et idealement, il doit avoir des retours positifs d'utilisateurs TutorLMS.

**[TRANSITION — face camera]**

Mon conseil : si tu debutes, prends Astra ou TutorStarter. Si tu veux un controle total avec Elementor, utilise Hello Elementor. Ne perds pas des heures a chercher le theme parfait — choisis un theme compatible, et concentre-toi sur le contenu de tes cours. C'est le contenu qui fait la difference, pas le theme. Prochaine lecon : on importe les donnees de demonstration pour avoir des cours d'exemple sur ton site.

---

**Points cles** :
- Themes Themeum (TutorStarter, Flavstart) : compatibilite garantie
- Themes tiers recommandes : Astra, GeneratePress, Kadence, OceanWP, Hello Elementor
- Eviter les themes avec leur propre systeme LMS integre
- Criteres : maintenu activement, PHP 8+, support Custom Post Types
- Le contenu des cours compte plus que le theme

**Mots cles SEO** : theme compatible TutorLMS, meilleur theme TutorLMS WordPress, Astra TutorLMS, theme LMS WordPress

---

### Lecon 1.7 — Import des donnees demo

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast complet de l'import

---

**[INTRO — face camera]**

Plutot que de partir d'un site vide, TutorLMS te permet d'importer des donnees de demonstration : des cours d'exemple, des lecons, des quiz. C'est la meilleure facon de comprendre comment le plugin est structure avant de creer ton propre contenu. On fait l'import ensemble.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Tools ou Tutor LMS > Add-ons]

Etape 1 : dans le tableau de bord WordPress, va dans Tutor LMS. Selon ta version, l'option d'import se trouve soit dans Tools, soit dans un menu dedie. Cherche "Sample Data", "Demo Import", ou "Import Data".

[Montre le bouton d'import des donnees demo]

Etape 2 : tu devrais voir un bouton "Import Sample Data" ou "Import Demo Content". Clique dessus.

**[ECRAN — screencast du processus d'import]**

[Montre la barre de progression de l'import]

L'import prend entre 30 secondes et 2 minutes selon ton hebergement. TutorLMS cree plusieurs elements :

Des cours d'exemple avec descriptions, images, et categories. Des lecons avec du contenu texte et video. Des quiz avec differents types de questions. Et eventuellement des etudiants fictifs avec des progressions.

[Montre le message de confirmation]

Etape 3 : une fois l'import termine, tu verras un message de confirmation. L'import a cree tous les contenus demo.

**[ECRAN — screencast exploration des donnees]**

[Navigation vers Tutor LMS > Cours]

Etape 4 : allons voir ce qui a ete cree. Va dans Tutor LMS, puis Cours. Tu devrais voir plusieurs cours d'exemple.

[Ouvre un cours demo]

Cliquons sur un cours pour voir sa structure. Tu as le titre, la description, les parametres du cours — duree, nombre maximum d'etudiants, niveau de difficulte. Et en dessous, le curriculum : les sections, les lecons, et les quiz.

[Montre le curriculum avec sections, lecons, quiz]

Regarde comment c'est organise. Un cours est divise en sections — aussi appelees "Topics". Chaque section contient des lecons et des quiz. C'est cette hierarchie que tu reproduiras quand tu creeras tes propres cours.

[Ouvre une lecon demo en front-end]

Etape 5 : ouvre une lecon en front-end pour voir l'experience etudiant. Tu vois le contenu de la lecon a gauche et la navigation du cours a droite — ou en bas selon le theme. Le bouton "Marquer comme complete" permet a l'etudiant de suivre sa progression.

**[ECRAN — screencast d'un quiz demo]**

[Ouvre un quiz demo]

Jetons un oeil a un quiz. TutorLMS propose plusieurs types de questions : QCM, vrai/faux, texte libre, correspondance, et d'autres avec le Pro. Les donnees demo incluent des exemples de chaque type. On verra tout ca en detail dans le module dedie aux quiz.

**[ECRAN — slide "Apres l'import"]**

Que faire apres l'import ?

Explore les cours demo pour comprendre la structure. Regarde comment les sections, lecons et quiz sont organises. Note les reglages de chaque cours — prix, acces, pre-requis.

Quand tu seras pret a creer ton propre contenu, tu pourras supprimer les donnees demo. Retourne dans Tutor LMS > Tools et utilise l'option "Remove Sample Data" pour nettoyer.

Ne publie jamais ton site avec les donnees demo encore visibles. Tes visiteurs verraient des cours factices avec du contenu Lorem Ipsum — pas la meilleure premiere impression.

**[TRANSITION — face camera]**

Tu as maintenant un site TutorLMS fonctionnel avec des donnees d'exemple. Prends le temps d'explorer les cours demo, de cliquer sur les lecons, de tester les quiz. C'est la meilleure facon de comprendre comment tout s'articule avant de creer ton propre contenu. Le Module 1 se termine avec un quiz rapide pour verifier que tu as bien retenu l'essentiel. On se retrouve tout de suite.

---

**Points cles** :
- Import via Tutor LMS > Tools > Import Sample Data
- Cree des cours, lecons, quiz et categories d'exemple
- Structure d'un cours : Cours > Sections (Topics) > Lecons + Quiz
- Explorer les donnees demo pour comprendre l'architecture avant de creer
- Supprimer les donnees demo avant de mettre le site en production

**Mots cles SEO** : donnees demo TutorLMS, importer contenu exemple TutorLMS, structure cours TutorLMS WordPress

---

### Lecon 1.8 — Quiz Module 1

**Duree** : ~5 min (auto-evalue)
**Type** : Quiz TutorLMS (8 QCM)

---

**Question 1 — Pre-requis serveur**

Quelle est la version minimum de PHP requise pour TutorLMS ?

- A) PHP 5.6
- B) PHP 7.0
- C) PHP 7.4
- D) PHP 8.0

**Reponse correcte : C**
Explication : TutorLMS requiert PHP 7.4 minimum, mais PHP 8.1 ou 8.2 est recommande pour de meilleures performances et la securite.

---

**Question 2 — Memoire PHP**

Quelle limite memoire PHP est recommandee pour un site TutorLMS ?

- A) 64 Mo
- B) 128 Mo
- C) 256 Mo minimum
- D) 1 Go minimum

**Reponse correcte : C**
Explication : 256 Mo est le minimum recommande pour TutorLMS. 512 Mo est confortable pour un site avec beaucoup de cours et d'etudiants.

---

**Question 3 — Installation**

Comment s'installe TutorLMS Pro ?

- A) Depuis le repertoire WordPress comme un plugin gratuit
- B) En telechargeant le ZIP depuis tutorlms.com et en le televersant dans WordPress
- C) En envoyant les fichiers par FTP
- D) En contactant le support Themeum qui l'installe a distance

**Reponse correcte : B**
Explication : TutorLMS Free s'installe depuis le repertoire WordPress, mais TutorLMS Pro se telecharge depuis le site officiel puis se televerser via Extensions > Ajouter > Televerser.

---

**Question 4 — Permalinks**

Quelle structure de permaliens est recommandee pour TutorLMS ?

- A) Simple (?p=123)
- B) Date et titre
- C) Nom de l'article (post name)
- D) Numerique

**Reponse correcte : C**
Explication : "Nom de l'article" donne des URLs propres et lisibles, essentielles pour le SEO et le bon fonctionnement des Custom Post Types de TutorLMS.

---

**Question 5 — Plugins de paiement**

Quel plugin de paiement s'integre nativement avec TutorLMS ?

- A) Stripe pour WordPress
- B) WooCommerce
- C) PayPal Commerce
- D) MemberPress

**Reponse correcte : B**
Explication : WooCommerce est la passerelle de paiement principale de TutorLMS. TutorLMS dispose aussi de son propre systeme de monetisation integre.

---

**Question 6 — Cache et pages dynamiques**

Pourquoi faut-il exclure certaines pages TutorLMS du cache ?

- A) Le cache ralentit TutorLMS
- B) Les pages dynamiques affichent du contenu personnalise par utilisateur
- C) TutorLMS a son propre systeme de cache integre
- D) Le cache empeche l'installation des mises a jour

**Reponse correcte : B**
Explication : Le tableau de bord etudiant, la page de progression et les quiz affichent du contenu specifique a chaque utilisateur. Si ces pages sont en cache, un etudiant pourrait voir la progression d'un autre.

---

**Question 7 — Themes compatibles**

Parmi ces themes, lequel est cree par Themeum (l'editeur de TutorLMS) ?

- A) Astra
- B) GeneratePress
- C) TutorStarter
- D) Hello Elementor

**Reponse correcte : C**
Explication : TutorStarter est le theme gratuit officiel de Themeum, entierement optimise pour TutorLMS. Les autres sont des themes tiers compatibles.

---

**Question 8 — Structure d'un cours**

Comment est organisee la hierarchie de contenu dans TutorLMS ?

- A) Cours > Lecons > Quiz
- B) Cours > Sections (Topics) > Lecons + Quiz
- C) Cours > Modules > Chapitres > Lecons
- D) Cours > Categories > Lecons

**Reponse correcte : B**
Explication : Un cours TutorLMS est divise en Sections (aussi appelees Topics), et chaque section contient des lecons et des quiz. C'est cette structure a trois niveaux qu'on decouvre dans les donnees demo.

---

**Seuil de reussite** : 6/8 (75%)
**Message reussite** : Bravo, tu as valide le Module 1. Tu as un site WordPress pret avec TutorLMS installe et configure. Direction le Module 2 pour creer ton premier cours.
**Message echec** : Tu n'as pas atteint le score minimum. Revois les lecons du Module 1 et retente le quiz. Concentre-toi sur les pre-requis serveur, les permalinks et la structure des cours.
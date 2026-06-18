# Scripts vidéo - Module 1 : Démarrage & Installation

**Formation** : Maîtriser TutorLMS
**Module** : M1 - Démarrage & Installation (Gratuit)
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~35 min
**Date** : 2026-03-23

---

### Leçon 1.1 : Pré-requis système

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides pour les specs, screencast rapide du dashboard hosting

---

**[INTRO - face caméra]**

Avant d'installer TutorLMS, il faut vérifier que ton hébergement WordPress est prêt. Si tu installes le plugin sur un serveur trop lent ou une version de PHP obsolète, tu vas avoir des problèmes. Dans cette leçon, je te donne la checklist exacte des pré-requis.

**[ÉCRAN - slide "Pré-requis techniques TutorLMS"]**

TutorLMS a besoin de quatre choses pour fonctionner correctement.

Première chose : WordPress 5.3 minimum. En pratique, utilise toujours la dernière version stable de WordPress. Au moment où je tourne cette vidéo, c'est WordPress 6.7. Si tu es en retard de plusieurs versions majeures, mets à jour avant d'installer TutorLMS.

Deuxième chose : PHP 7.4 minimum. Là encore, je te recommande PHP 8.1 ou 8.2. C'est plus rapide, plus sécurisé, et tous les plugins modernes le supportent. Si tu es encore en PHP 7.4, c'est le moment de demander à ton hébergeur de monter la version.

**[ÉCRAN - slide "Mémoire & Serveur"]**

Troisième chose : une limite mémoire PHP de 256 Mo minimum. Par défaut, beaucoup d'hébergeurs mettent 128 Mo. C'est insuffisant pour un LMS. Tu vas charger des cours, des vidéos, des quiz - ça consomme de la mémoire. 256 Mo est le minimum, 512 Mo est confortable.

Quatrième chose : un hébergement WordPress de qualité. TutorLMS génère beaucoup de requêtes en base de données - chaque cours, chaque leçon, chaque quiz est un Custom Post Type avec des métadonnées. Un hébergement mutualisé à 3 euros par mois ne tiendra pas la charge avec 50 étudiants connectés en même temps.

**[ÉCRAN - screencast du dashboard hébergement]**

[Montre le panneau de contrôle d'un hébergeur - section PHP et mémoire]

Pour vérifier ta version de PHP et ta limite mémoire, va dans le panneau de contrôle de ton hébergeur. Chez la plupart des hébergeurs - OVH, o2switch, Infomaniak, Cloudways - tu trouveras ces infos dans la section PHP ou configuration du serveur.

Si tu ne trouves pas, installe le plugin "Site Health" de WordPress. Va dans Outils, puis Santé du site, puis Informations. Tu verras la version PHP, la limite mémoire, et la version de WordPress.

**[ÉCRAN - slide "Hébergements recommandés"]**

Pour un site LMS avec TutorLMS, je recommande trois types d'hébergement.

Pour débuter avec moins de 100 étudiants : o2switch ou Infomaniak. Hébergement mutualisé performant, support francophone, tarif raisonnable.

Pour monter en charge entre 100 et 1000 étudiants : un VPS managé type Cloudways ou SpinupWP. Tu as des ressources dédiées, et la performance suit.

Au-delà de 1000 étudiants actifs : un serveur dédié ou un hébergement spécialisé WordPress comme Starter Starter ou Starter Starter.

Sur schoolsWP, j'utilise Starter Starter avec Cloudways. Ça me permet de gérer les formations, le blog, et le trafic SEO sans souci de performance.

**[TRANSITION - face caméra]**

Récapitulons. WordPress 5.3 ou plus récent, PHP 7.4 ou plus récent - idéalement 8.1 ou 8.2 - et 256 Mo de mémoire minimum. Si ton hébergement coche ces trois cases, tu es prêt pour l'installation. C'est ce qu'on fait dans la prochaine leçon.

---

**Points clés** :
- WordPress 5.3+ (recommandé : dernière version stable)
- PHP 7.4+ (recommandé : 8.1 ou 8.2)
- Mémoire PHP : 256 Mo minimum, 512 Mo recommandé
- Hébergement adapté : pas de mutualisé bas de gamme pour un LMS
- Outil de vérification : Site Health dans WordPress

**Mots clés SEO** : pré-requis TutorLMS, hébergement TutorLMS WordPress, configuration serveur LMS WordPress, PHP TutorLMS

---

### Leçon 1.2 : Installation Tutor LMS Free + Pro

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast complet de l'installation
**Source** : Vidéos #2, #30 (TutorLMS Academy) - script original schoolsWP

---

**[INTRO - face caméra]**

Dans cette leçon, tu installes TutorLMS sur ton site WordPress. D'abord la version gratuite depuis le répertoire officiel, puis le plugin Pro si tu as une licence. En 5 minutes, ton LMS est opérationnel.

Petit détail qui fait la différence : la formation que tu suis en ce moment tourne sur TutorLMS Pro. Mon site schoolsWP utilise exactement le même outil pour héberger ces cours. Ce n'est pas de la théorie - c'est ce que j'utilise au quotidien.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Extensions > Ajouter]

Étape 1 : dans ton tableau de bord WordPress, va dans Extensions, puis Ajouter.

[Tape "TutorLMS" dans la barre de recherche]

Étape 2 : dans la barre de recherche, tape "Tutor LMS". Le premier résultat devrait être "Tutor LMS - eLearning and online course solution" par Themeum. Vérifie que c'est bien l'éditeur Themeum - il existe des plugins avec des noms similaires.

[Clique sur Installer maintenant]

Étape 3 : clique sur "Installer maintenant". WordPress télécharge le plugin. Ça prend quelques secondes.

[Clique sur Activer]

Étape 4 : une fois installé, clique sur "Activer".

**[ÉCRAN - screencast assistant de configuration]**

[Montre l'assistant de bienvenue TutorLMS]

Dès l'activation, TutorLMS lance un assistant de configuration. Tu vas voir un écran de bienvenue avec plusieurs étapes. On va les parcourir ensemble.

[Étape 1 de l'assistant]

Première étape : le type de site. Choisis si tu veux un marketplace multi-instructeurs ou un site mono-instructeur. Si c'est ton propre site de formation, choisis mono-instructeur. Tu pourras changer plus tard.

[Étape 2 de l'assistant]

Deuxième étape : les pages. L'assistant propose de créer automatiquement les pages nécessaires - page des cours, page du tableau de bord étudiant, page du tableau de bord instructeur. Laisse tout coché. Ces pages sont indispensables au fonctionnement du LMS.

[Étape 3 de l'assistant]

Troisième étape : la passerelle de paiement. Si tu veux vendre des cours, tu configureras WooCommerce ou le système de monétisation intégré plus tard. Pour l'instant, tu peux passer cette étape.

[Clique sur Terminer]

Étape 5 : clique sur Terminer. L'assistant crée les pages et configure les réglages de base.

**[ÉCRAN - screencast installation Pro]**

[Montre le site TutorLMS.com > Mon compte > Téléchargements]

Maintenant, si tu as acheté une licence TutorLMS Pro, voici comment installer le plugin premium.

Étape 6 : va sur le site tutorlms.com, connecte-toi à ton compte, et télécharge le fichier ZIP du plugin Pro depuis la section Téléchargements.

[Retour dans WordPress > Extensions > Ajouter > Téléverser une extension]

Étape 7 : retourne dans WordPress. Va dans Extensions, Ajouter, puis clique sur "Téléverser une extension" en haut de la page. Sélectionne le fichier ZIP que tu viens de télécharger.

[Clique sur Installer puis Activer]

Étape 8 : clique sur "Installer maintenant", puis sur "Activer". Le plugin Pro s'ajoute à côté du plugin gratuit - les deux fonctionnent ensemble.

**[ÉCRAN - screencast vérification]**

[Montre le menu TutorLMS dans la sidebar WordPress]

Vérifions que tout est en place. Dans le menu latéral de WordPress, tu devrais voir "Tutor LMS" avec ses sous-menus : Cours, Catégories, Tags, Étudiants, Réglages, et si tu as le Pro, des options supplémentaires comme les Certificats et les Rapports.

**[TRANSITION - face caméra]**

TutorLMS est installé. Le plugin gratuit donne accès à la création de cours, leçons, quiz et gestion des étudiants. Le Pro ajoute les certificats, les rapports avancés, les types de questions supplémentaires, et les addons. Dans la prochaine leçon, on active la licence Pro pour débloquer toutes les fonctionnalités.

---

**Points clés** :
- Installer TutorLMS Free depuis Extensions > Ajouter (éditeur : Themeum)
- L'assistant de configuration crée les pages essentielles automatiquement
- TutorLMS Pro s'installe via un fichier ZIP téléchargé depuis tutorlms.com
- Les deux plugins (Free + Pro) fonctionnent ensemble
- Vérification : menu TutorLMS visible dans la sidebar WordPress

**Mots clés SEO** : installer TutorLMS WordPress, installation TutorLMS Pro, configurer TutorLMS, plugin LMS WordPress installation

---

### Leçon 1.3 : Activation de licence

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast de l'activation
**Source** : Vidéos #2, #30 (TutorLMS Academy) - script original schoolsWP

---

**[INTRO - face caméra]**

Tu as installé TutorLMS Pro, mais sans activer ta licence, tu n'auras pas accès aux mises à jour automatiques ni au support. L'activation prend 2 minutes. Je te montre exactement où aller et quoi faire.

**[ÉCRAN - screencast site TutorLMS.com]**

[Navigation vers Mon Compte > Licences]

Étape 1 : commence par récupérer ta clé de licence. Va sur tutorlms.com, connecte-toi à ton compte, et ouvre la section Licences. Tu y trouveras ta clé - une longue chaîne de caractères. Copie-la.

Un détail important : chaque licence a un nombre limité d'activations. Le plan basique permet une activation sur un seul site. Le plan Business en permet cinq. Vérifie que tu n'as pas dépassé ta limite avant d'activer.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Licence ou Settings > Licence]

Étape 2 : retourne dans ton WordPress. Va dans Tutor LMS, puis Réglages. Cherche l'onglet "Licence" ou "License". Selon la version, il peut être dans les réglages généraux ou dans un sous-menu dédié.

[Colle la clé de licence]

Étape 3 : colle ta clé de licence dans le champ prévu. Clique sur "Activer" ou "Activate License".

[Montre le message de confirmation]

Si tout est correct, tu verras un message de confirmation en vert : "License activated successfully" ou équivalent. Le statut passe de "Inactive" à "Active".

**[ÉCRAN - screencast vérification des mises à jour]**

[Navigation vers Extensions > Extensions installées]

Étape 4 : vérifions que les mises à jour automatiques fonctionnent. Va dans Extensions, puis Extensions installées. À côté de "Tutor LMS Pro", tu devrais voir un lien "Vérifier les mises à jour" ou une notification si une mise à jour est disponible. Si tu ne vois pas d'erreur de licence, c'est bon.

**[ÉCRAN - slide "Problèmes courants"]**

Trois problèmes fréquents lors de l'activation.

Premier problème : "License limit reached". Tu as déjà utilisé toutes tes activations. Va sur tutorlms.com, désactive la licence sur un ancien site, puis réactive ici.

Deuxième problème : "Invalid license key". Vérifie que tu as copié la clé complète, sans espace au début ou à la fin. Un copier-coller depuis un email ajoute parfois des caractères invisibles.

Troisième problème : les mises à jour ne s'affichent pas. Vide le cache de ton site et celui de WordPress. Va dans Extensions installées, clique sur "Vérifier les mises à jour" pour forcer la vérification.

**[TRANSITION - face caméra]**

Ta licence est activée. Tu as accès aux mises à jour automatiques et au support Themeum. Avant de commencer à créer des cours, il reste un réglage technique important à faire : les permalinks. C'est la prochaine leçon.

---

**Points clés** :
- Récupérer la clé de licence sur tutorlms.com > Mon Compte > Licences
- Activer dans WordPress : Tutor LMS > Réglages > Licence
- Chaque licence a un nombre limité d'activations selon le plan
- Sans activation : pas de mises à jour automatiques ni de support
- Problèmes courants : limite atteinte, clé invalide, cache à vider

**Mots clés SEO** : activer licence TutorLMS Pro, clé de licence TutorLMS, activation TutorLMS WordPress

---

### Leçon 1.4 : Réglages Permalinks

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast des réglages

---

**[INTRO - face caméra]**

Les permalinks, c'est la structure des URLs de ton site. Si tu ne les configures pas correctement, les pages de tes cours, les leçons et les quiz vont afficher des erreurs 404. C'est un réglage de 30 secondes, mais beaucoup de débutants l'oublient. On le fait maintenant.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Réglages > Permaliens]

Étape 1 : dans ton tableau de bord WordPress, va dans Réglages, puis Permaliens.

[Montre les différentes options de structure]

Tu as plusieurs structures disponibles. "Simple" utilise des numéros - c'est mauvais pour le SEO et incompatible avec TutorLMS. "Date et titre" ajoute la date dans l'URL - inutile pour des cours. "Nom de l'article" - c'est celle qu'il te faut.

Étape 2 : sélectionne "Nom de l'article". Ça donne des URLs propres du type tonsite.com/mon-cours/ au lieu de tonsite.com/?p=123.

[Clique sur Enregistrer les modifications]

Étape 3 : clique sur "Enregistrer les modifications". Même si la bonne option était déjà sélectionnée, clique quand même. WordPress régénère les règles de réécriture à chaque sauvegarde. Après l'installation d'un plugin qui crée des Custom Post Types - comme TutorLMS - c'est indispensable.

**[ÉCRAN - slide "Pourquoi c'est important pour TutorLMS"]**

Pourquoi ce réglage est critique pour TutorLMS ?

TutorLMS crée plusieurs types de contenu personnalisés : les cours, les leçons, les quiz, les devoirs. Chacun a sa propre structure d'URL. Par exemple : tonsite.com/courses/mon-premier-cours/ pour un cours, tonsite.com/courses/mon-cours/lesson/ma-lecon/ pour une leçon.

Si les permalinks sont en mode "Simple", WordPress ne sait pas interpréter ces URLs. Résultat : des pages 404 partout. C'est le problème numéro un rapporté par les débutants sur le forum TutorLMS.

**[ÉCRAN - screencast vérification]**

[Ouvre un cours en front-end]

Étape 4 : vérifions que tout fonctionne. Ouvre un cours en front-end - si tu as importé les données démo, utilise un des cours d'exemple. L'URL devrait être propre, sans point d'interrogation ni numéro.

[Montre l'URL dans la barre d'adresse]

L'URL affiche bien tonsite.com/courses/nom-du-cours/. Si tu vois une erreur 404, retourne dans Réglages > Permaliens et clique encore une fois sur "Enregistrer les modifications". Ça résout le problème dans 90% des cas.

**[ÉCRAN - slide "Personnalisation des slugs TutorLMS"]**

Bonus : tu peux personnaliser les slugs de TutorLMS. Va dans Tutor LMS > Réglages > General, et cherche la section "URL Slugs" ou "Permalinks". Par défaut, les cours sont sous /courses/. Tu peux changer ça en /formations/ ou /cours/ si tu veux des URLs en français.

Attention : si tu changes les slugs après avoir publié des cours, toutes les URLs existantes vont changer. Pense à mettre en place des redirections 301 si tu fais ça.

**[TRANSITION - face caméra]**

Tes permalinks sont configurés. Les URLs de tes cours, leçons et quiz fonctionnent correctement. Dans la prochaine leçon, on regarde quels plugins sont compatibles avec TutorLMS - et lesquels éviter.

---

**Points clés** :
- Structure recommandée : "Nom de l'article" (post name)
- Toujours cliquer "Enregistrer" après installation d'un plugin à Custom Post Types
- Erreur 404 sur les cours = permalinks à resauvegarder
- Slugs personnalisables dans Tutor LMS > Réglages (ex: /formations/ au lieu de /courses/)
- Changer les slugs après publication = redirections 301 obligatoires

**Mots clés SEO** : permalinks TutorLMS, erreur 404 TutorLMS, réglages URL cours WordPress, slug TutorLMS

---

### Leçon 1.5 : Plugins compatibles

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides pour les catégories, screencast rapide

---

**[INTRO - face caméra]**

TutorLMS ne fonctionne pas seul. Tu vas avoir besoin de plugins pour les paiements, le SEO, le cache, les formulaires. Le problème, c'est que certains plugins créent des conflits avec TutorLMS. Dans cette leçon, je te donne la liste des plugins testés et compatibles - et ceux à éviter.

**[ÉCRAN - slide "Plugins compatibles - Paiements"]**

Commençons par les plugins de paiement. C'est souvent la première question : comment vendre mes cours ?

WooCommerce est le choix principal. TutorLMS s'intègre nativement avec WooCommerce pour vendre des cours individuels ou des abonnements. C'est la méthode la plus flexible.

Easy Digital Downloads fonctionne aussi, avec un addon dédié.

TutorLMS a également son propre système de monétisation intégré - sans WooCommerce. Si tu veux garder les choses simples et que tu n'as pas besoin d'un panier complet, c'est une option viable.

**[ÉCRAN - slide "Plugins compatibles - SEO"]**

Pour le SEO. RankMath est entièrement compatible avec TutorLMS. Il détecte automatiquement les cours comme des types de contenu et te permet d'optimiser les meta titles, descriptions et le schéma markup. C'est ce que j'utilise sur schoolsWP.

Yoast SEO fonctionne aussi. Les deux sont testés et validés par Themeum.

**[ÉCRAN - slide "Plugins compatibles - Performance"]**

Pour la performance et le cache. WP Rocket est compatible. LiteSpeed Cache aussi. W3 Total Cache fonctionne, mais demande plus de configuration.

Un point d'attention : si tu utilises un plugin de cache, assure-toi d'exclure les pages dynamiques de TutorLMS du cache. Le tableau de bord étudiant, la page de progression, la page de quiz - ces pages doivent afficher du contenu personnalisé à chaque utilisateur. Si elles sont cachées, un étudiant verra la progression d'un autre.

**[ÉCRAN - slide "Plugins compatibles - Page Builders"]**

Pour les page builders. Elementor est officiellement supporté. TutorLMS fournit des widgets Elementor pour afficher les cours, les catégories, les instructeurs. Gutenberg fonctionne nativement - TutorLMS fournit ses propres blocs.

Divi et Beaver Builder fonctionnent, mais sans widgets dédiés. Tu utiliseras des shortcodes à la place.

**[ÉCRAN - slide "Plugins compatibles - Email & CRM"]**

Pour l'email et le CRM. FluentCRM est compatible - et c'est ce que j'utilise sur schoolsWP pour les séquences automatisées. Tu peux déclencher des emails quand un étudiant s'inscrit à un cours, termine une leçon, ou échoue à un quiz.

MailChimp et ConvertKit fonctionnent aussi via des intégrateurs comme AutomateWP ou des webhooks.

**[ÉCRAN - slide "Plugins à éviter ou à surveiller"]**

Maintenant, les plugins à surveiller.

LearnDash et LifterLMS : ce sont des concurrents directs. Ne les installe jamais en même temps que TutorLMS. Ça peut sembler évident, mais j'ai vu des gens le faire.

Les plugins de membership comme MemberPress ou Restrict Content Pro : ils peuvent créer des conflits avec la gestion d'accès de TutorLMS. Si tu veux du membership, utilise plutôt les fonctions natives de TutorLMS Pro ou l'intégration WooCommerce Subscriptions.

Les plugins de sécurité trop agressifs : Wordfence ou iThemes Security avec des règles de pare-feu strictes peuvent bloquer les requêtes AJAX de TutorLMS. Si tu rencontres des problèmes de chargement dans l'éditeur de cours, vérifie les règles de ton plugin de sécurité.

**[TRANSITION - face caméra]**

Tu as maintenant une vision claire des plugins compatibles. Retiens l'essentiel : WooCommerce pour les paiements, RankMath pour le SEO, WP Rocket pour le cache, et exclus toujours les pages dynamiques du cache. Dans la prochaine leçon, on parle des thèmes compatibles.

---

**Points clés** :
- Paiements : WooCommerce (natif), EDD (addon), ou monétisation intégrée
- SEO : RankMath et Yoast SEO validés
- Cache : WP Rocket, LiteSpeed - exclure les pages dynamiques TutorLMS
- Page builders : Elementor (widgets dédiés), Gutenberg (blocs natifs)
- Email/CRM : FluentCRM, MailChimp, ConvertKit
- À éviter : autres LMS simultanés, membership plugins en conflit, sécurité trop agressive

**Mots clés SEO** : plugins compatibles TutorLMS, WooCommerce TutorLMS, RankMath TutorLMS, Elementor TutorLMS

---

### Leçon 1.6 : Thèmes compatibles

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides comparatifs, screencast rapide de démos

---

**[INTRO - face caméra]**

Le thème que tu choisis impacte directement l'apparence de tes cours, la vitesse de ton site, et la compatibilité avec TutorLMS. Certains thèmes fonctionnent parfaitement, d'autres causent des problèmes d'affichage. Dans cette leçon, je te montre lesquels choisir et pourquoi.

**[ÉCRAN - slide "Compatibilité thème + LMS : ce qu'il faut savoir"]**

TutorLMS utilise ses propres templates pour afficher les pages de cours, les leçons, le tableau de bord étudiant, et les quiz. Ton thème doit respecter ces templates sans les écraser.

Concrètement, un thème compatible avec TutorLMS, c'est un thème qui ne casse pas la mise en page des cours, qui supporte les Custom Post Types, et qui ne surcharge pas les templates TutorLMS avec ses propres layouts.

**[ÉCRAN - slide "Thèmes officiels Themeum"]**

Premier choix : les thèmes Themeum. C'est le même éditeur que TutorLMS, donc la compatibilité est garantie.

TutorStarter est le thème gratuit officiel. Il est léger, optimisé pour TutorLMS, et disponible dans le répertoire WordPress. C'est un bon point de départ si tu débutes.

Flavstarter est le thème premium de Themeum. Plus de fonctionnalités de design, plus d'options de personnalisation, toujours 100% compatible.

**[ÉCRAN - slide "Thèmes tiers compatibles"]**

Deuxième choix : les thèmes tiers testés et compatibles.

Astra est un excellent choix. Léger, rapide, compatible WooCommerce et TutorLMS. Il offre des starter templates dédiées à l'éducation. C'est probablement le thème tiers le plus utilisé avec TutorLMS.

GeneratePress : très léger, performant, et compatible. Moins d'options de design qu'Astra, mais plus rapide.

Kadence : bon équilibre entre performance et fonctionnalités. Compatible TutorLMS.

OceanWP : compatible, avec beaucoup d'extensions gratuites.

Hello Elementor : si tu utilises Elementor comme page builder, c'est le thème le plus léger possible. Il laisse toute la mise en page à Elementor et ne crée pas de conflit avec les templates TutorLMS.

**[ÉCRAN - screencast démo d'un cours]**

[Montre la page d'un cours avec un thème compatible - ex: Astra]

Voici à quoi ressemble un cours avec un thème bien configuré. La page de cours affiche la description, le curriculum, les avis, le prix - tout est en place. Le design est propre, la navigation fonctionne.

[Montre la même page avec un thème problématique]

Et voici ce qui arrive avec un thème qui n'est pas prévu pour les LMS. La sidebar écrase le contenu du cours. Les boutons d'inscription ne sont pas alignés. Le curriculum ne s'affiche pas correctement. C'est le genre de problème qu'on évite en choisissant un thème compatible.

**[ÉCRAN - slide "Thèmes à éviter"]**

Les thèmes à éviter avec TutorLMS.

Les thèmes "all-in-one" surchargés : les thèmes qui intègrent leur propre système de cours - comme Flavor LMS ou EduPro - vont entrer en conflit avec TutorLMS. Ne combine jamais un thème LMS avec un plugin LMS.

Les thèmes anciens non mis à jour depuis plus de 2 ans. S'ils ne supportent pas PHP 8+ et les derniers standards WordPress, ils vont poser des problèmes.

Les thèmes avec des mises en page très rigides qui ne supportent pas les Custom Post Types. Si le thème force un layout spécifique sur toutes les pages, les templates TutorLMS ne s'afficheront pas correctement.

**[ÉCRAN - slide "Critères de sélection"]**

Pour résumer, voici tes critères de sélection.

Le thème doit être activement maintenu - dernière mise à jour il y a moins de 3 mois. Il doit supporter PHP 8+. Il doit être compatible avec les Custom Post Types. Il ne doit pas inclure son propre système LMS. Et idéalement, il doit avoir des retours positifs d'utilisateurs TutorLMS.

**[TRANSITION - face caméra]**

Mon conseil : si tu débutes, prends Astra ou TutorStarter. Si tu veux un contrôle total avec Elementor, utilise Hello Elementor. Ne perds pas des heures à chercher le thème parfait - choisis un thème compatible, et concentre-toi sur le contenu de tes cours. C'est le contenu qui fait la différence, pas le thème. Prochaine leçon : on importe les données de démonstration pour avoir des cours d'exemple sur ton site.

---

**Points clés** :
- Thèmes Themeum (TutorStarter, Flavstart) : compatibilité garantie
- Thèmes tiers recommandés : Astra, GeneratePress, Kadence, OceanWP, Hello Elementor
- Éviter les thèmes avec leur propre système LMS intégré
- Critères : maintenu activement, PHP 8+, support Custom Post Types
- Le contenu des cours compte plus que le thème

**Mots clés SEO** : thème compatible TutorLMS, meilleur thème TutorLMS WordPress, Astra TutorLMS, thème LMS WordPress

---

### Leçon 1.7 : Import des données démo

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast complet de l'import

---

**[INTRO - face caméra]**

Plutôt que de partir d'un site vide, TutorLMS te permet d'importer des données de démonstration : des cours d'exemple, des leçons, des quiz. C'est la meilleure façon de comprendre comment le plugin est structuré avant de créer ton propre contenu. On fait l'import ensemble.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Tools ou Tutor LMS > Add-ons]

Étape 1 : dans le tableau de bord WordPress, va dans Tutor LMS. Selon ta version, l'option d'import se trouve soit dans Tools, soit dans un menu dédié. Cherche "Sample Data", "Demo Import", ou "Import Data".

[Montre le bouton d'import des données démo]

Étape 2 : tu devrais voir un bouton "Import Sample Data" ou "Import Demo Content". Clique dessus.

**[ÉCRAN - screencast du processus d'import]**

[Montre la barre de progression de l'import]

L'import prend entre 30 secondes et 2 minutes selon ton hébergement. TutorLMS crée plusieurs éléments :

Des cours d'exemple avec descriptions, images, et catégories. Des leçons avec du contenu texte et vidéo. Des quiz avec différents types de questions. Et éventuellement des étudiants fictifs avec des progressions.

[Montre le message de confirmation]

Étape 3 : une fois l'import terminé, tu verras un message de confirmation. L'import a créé tous les contenus démo.

**[ÉCRAN - screencast exploration des données]**

[Navigation vers Tutor LMS > Cours]

Étape 4 : allons voir ce qui a été créé. Va dans Tutor LMS, puis Cours. Tu devrais voir plusieurs cours d'exemple.

[Ouvre un cours démo]

Cliquons sur un cours pour voir sa structure. Tu as le titre, la description, les paramètres du cours - durée, nombre maximum d'étudiants, niveau de difficulté. Et en dessous, le curriculum : les sections, les leçons, et les quiz.

[Montre le curriculum avec sections, leçons, quiz]

Regarde comment c'est organisé. Un cours est divisé en sections - aussi appelées "Topics". Chaque section contient des leçons et des quiz. C'est cette hiérarchie que tu reproduiras quand tu créeras tes propres cours.

[Ouvre une leçon démo en front-end]

Étape 5 : ouvre une leçon en front-end pour voir l'expérience étudiant. Tu vois le contenu de la leçon à gauche et la navigation du cours à droite - ou en bas selon le thème. Le bouton "Marquer comme complète" permet à l'étudiant de suivre sa progression.

**[ÉCRAN - screencast d'un quiz démo]**

[Ouvre un quiz démo]

Jetons un œil à un quiz. TutorLMS propose plusieurs types de questions : QCM, vrai/faux, texte libre, correspondance, et d'autres avec le Pro. Les données démo incluent des exemples de chaque type. On verra tout ça en détail dans le module dédié aux quiz.

**[ÉCRAN - slide "Après l'import"]**

Que faire après l'import ?

Explore les cours démo pour comprendre la structure. Regarde comment les sections, leçons et quiz sont organisés. Note les réglages de chaque cours - prix, accès, pré-requis.

Quand tu seras prêt à créer ton propre contenu, tu pourras supprimer les données démo. Retourne dans Tutor LMS > Tools et utilise l'option "Remove Sample Data" pour nettoyer.

Ne publie jamais ton site avec les données démo encore visibles. Tes visiteurs verraient des cours factices avec du contenu Lorem Ipsum - pas la meilleure première impression.

**[TRANSITION - face caméra]**

Tu as maintenant un site TutorLMS fonctionnel avec des données d'exemple. Prends le temps d'explorer les cours démo, de cliquer sur les leçons, de tester les quiz. C'est la meilleure façon de comprendre comment tout s'articule avant de créer ton propre contenu. Le Module 1 se termine avec un quiz rapide pour vérifier que tu as bien retenu l'essentiel. On se retrouve tout de suite.

---

**Points clés** :
- Import via Tutor LMS > Tools > Import Sample Data
- Crée des cours, leçons, quiz et catégories d'exemple
- Structure d'un cours : Cours > Sections (Topics) > Leçons + Quiz
- Explorer les données démo pour comprendre l'architecture avant de créer
- Supprimer les données démo avant de mettre le site en production

**Mots clés SEO** : données démo TutorLMS, importer contenu exemple TutorLMS, structure cours TutorLMS WordPress

---

### Leçon 1.8 : Quiz Module 1

**Durée** : ~5 min (auto-évalué)
**Type** : Quiz TutorLMS (8 QCM)

---

**Question 1 - Pré-requis serveur**

Quelle est la version minimum de PHP requise pour TutorLMS ?

- A) PHP 5.6
- B) PHP 7.0
- C) PHP 7.4
- D) PHP 8.0

**Réponse correcte : C**
Explication : TutorLMS requiert PHP 7.4 minimum, mais PHP 8.1 ou 8.2 est recommandé pour de meilleures performances et la sécurité.

---

**Question 2 - Mémoire PHP**

Quelle limite mémoire PHP est recommandée pour un site TutorLMS ?

- A) 64 Mo
- B) 128 Mo
- C) 256 Mo minimum
- D) 1 Go minimum

**Réponse correcte : C**
Explication : 256 Mo est le minimum recommandé pour TutorLMS. 512 Mo est confortable pour un site avec beaucoup de cours et d'étudiants.

---

**Question 3 - Installation**

Comment s'installe TutorLMS Pro ?

- A) Depuis le répertoire WordPress comme un plugin gratuit
- B) En téléchargeant le ZIP depuis tutorlms.com et en le téléversant dans WordPress
- C) En envoyant les fichiers par FTP
- D) En contactant le support Themeum qui l'installe à distance

**Réponse correcte : B**
Explication : TutorLMS Free s'installe depuis le répertoire WordPress, mais TutorLMS Pro se télécharge depuis le site officiel puis se téléverser via Extensions > Ajouter > Téléverser.

---

**Question 4 - Permalinks**

Quelle structure de permaliens est recommandée pour TutorLMS ?

- A) Simple (?p=123)
- B) Date et titre
- C) Nom de l'article (post name)
- D) Numérique

**Réponse correcte : C**
Explication : "Nom de l'article" donne des URLs propres et lisibles, essentielles pour le SEO et le bon fonctionnement des Custom Post Types de TutorLMS.

---

**Question 5 - Plugins de paiement**

Quel plugin de paiement s'intègre nativement avec TutorLMS ?

- A) Stripe pour WordPress
- B) WooCommerce
- C) PayPal Commerce
- D) MemberPress

**Réponse correcte : B**
Explication : WooCommerce est la passerelle de paiement principale de TutorLMS. TutorLMS dispose aussi de son propre système de monétisation intégré.

---

**Question 6 - Cache et pages dynamiques**

Pourquoi faut-il exclure certaines pages TutorLMS du cache ?

- A) Le cache ralentit TutorLMS
- B) Les pages dynamiques affichent du contenu personnalisé par utilisateur
- C) TutorLMS a son propre système de cache intégré
- D) Le cache empêche l'installation des mises à jour

**Réponse correcte : B**
Explication : Le tableau de bord étudiant, la page de progression et les quiz affichent du contenu spécifique à chaque utilisateur. Si ces pages sont en cache, un étudiant pourrait voir la progression d'un autre.

---

**Question 7 - Thèmes compatibles**

Parmi ces thèmes, lequel est créé par Themeum (l'éditeur de TutorLMS) ?

- A) Astra
- B) GeneratePress
- C) TutorStarter
- D) Hello Elementor

**Réponse correcte : C**
Explication : TutorStarter est le thème gratuit officiel de Themeum, entièrement optimisé pour TutorLMS. Les autres sont des thèmes tiers compatibles.

---

**Question 8 - Structure d'un cours**

Comment est organisée la hiérarchie de contenu dans TutorLMS ?

- A) Cours > Leçons > Quiz
- B) Cours > Sections (Topics) > Leçons + Quiz
- C) Cours > Modules > Chapitres > Leçons
- D) Cours > Catégories > Leçons

**Réponse correcte : B**
Explication : Un cours TutorLMS est divisé en Sections (aussi appelées Topics), et chaque section contient des leçons et des quiz. C'est cette structure à trois niveaux qu'on découvre dans les données démo.

---

**Seuil de réussite** : 6/8 (75%)
**Message réussite** : Bravo, tu as validé le Module 1. Tu as un site WordPress prêt avec TutorLMS installé et configuré. Direction le Module 2 pour créer ton premier cours.
**Message échec** : Tu n'as pas atteint le score minimum. Revois les leçons du Module 1 et retente le quiz. Concentre-toi sur les pré-requis serveur, les permalinks et la structure des cours.

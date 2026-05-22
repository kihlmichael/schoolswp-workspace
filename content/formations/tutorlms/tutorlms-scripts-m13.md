# Scripts vidéo — Module 13 : Migration

**Formation** : Maîtriser TutorLMS
**Module** : M13 — Migration (Premium)
**Leçons** : 6 vidéos + 1 quiz
**Durée totale** : ~35 min
**Date** : 2026-03-23

---

### Leçon 13.1 — Migration LearnDash

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + LearnDash
**Source** : Vidéo #13 + doc migration/learndash

---

**[INTRO — face caméra]**

Tu es sur LearnDash et tu veux passer à TutorLMS ? Bonne nouvelle : TutorLMS intègre un outil de migration qui transfère tes cours, leçons, quiz et inscriptions étudiants. Pas besoin de tout reconstruire à la main. Mais avant de toucher à quoi que ce soit — on fait un backup complet. C'est la règle numéro un de toute migration.

**[ÉCRAN — screencast admin WordPress]**

[Navigation vers l'outil de backup — UpdraftPlus ou équivalent]

Avant de commencer, sauvegarde tout. Base de données et fichiers. Utilise UpdraftPlus, WPVivid ou ton outil habituel. Télécharge la sauvegarde en local — pas juste sur le serveur. Si la migration tourne mal, tu veux pouvoir revenir à l'état exact d'avant.

**[ÉCRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Migration]

Une fois le backup fait, va dans Tutor LMS, puis Tools, puis Migration. Tu vois la section "LearnDash". TutorLMS détecte automatiquement si LearnDash est installé et affiche le nombre de cours, leçons et quiz disponibles pour la migration.

**[ÉCRAN — screencast processus de migration]**

[Montre le bouton de migration et la progression]

Clique sur "Migrate". Le processus se lance. Selon le volume de contenu, ça peut prendre de quelques secondes à plusieurs minutes. Ne ferme pas la fenêtre — laisse le processus terminer.

Ce qui est migré :
- Les cours avec leur structure (sections, leçons)
- Les quiz et leurs questions
- Les inscriptions étudiants — chaque élève garde ses cours
- La progression des élèves — ce qui a été complété reste complété

**[ÉCRAN — screencast vérification post-migration]**

[Navigation vers Tutor LMS > Courses — vérification d'un cours migré]

Une fois terminé, vérifie. Ouvre Tutor LMS, Courses. Tes cours LearnDash doivent apparaître. Ouvre-en un, vérifie la structure : sections, leçons, quiz. Passe côté front-end pour confirmer que l'affichage est correct.

Vérifie aussi les inscriptions : va dans un cours, onglet Students. Les élèves doivent être là avec leur progression.

**[TRANSITION — face caméra]**

Points importants : certains éléments ne migrent pas automatiquement. Les certificats LearnDash, les badges et les réglages spécifiques de LearnDash — comme les timer de quiz avancés — devront être reconfigurés dans TutorLMS. Pareil pour les shortcodes LearnDash dans tes pages — il faudra les remplacer par les shortcodes TutorLMS.

La recommandation schoolsWP : fais la migration sur un environnement de staging d'abord. Vérifie tout, puis reproduis sur la production. Et garde LearnDash installé mais désactivé pendant quelques semaines — au cas où tu aurais besoin de vérifier un détail.

---

**Points clés** :
- Backup complet obligatoire avant toute migration (base + fichiers)
- Outil intégré : Tutor LMS > Tools > Migration > LearnDash
- Migration des cours, leçons, quiz, inscriptions et progression
- Certificats, badges et shortcodes LearnDash à reconfigurer manuellement
- Tester sur un staging avant de migrer en production
- Garder LearnDash désactivé (pas supprimé) pendant quelques semaines

**Mots clés SEO** : migration LearnDash TutorLMS, passer de LearnDash à TutorLMS, transférer cours LearnDash, migration LMS WordPress

---

### Leçon 13.2 — Migration LifterLMS

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + LifterLMS
**Source** : Vidéo #24 + doc migration/lifterlms

---

**[INTRO — face caméra]**

Tu utilises LifterLMS et tu veux migrer vers TutorLMS ? Le processus est similaire à la migration LearnDash — TutorLMS détecte LifterLMS et propose un transfert automatique. Comme toujours, on commence par un backup.

**[ÉCRAN — screencast admin WordPress]**

[Navigation vers l'outil de backup]

Même réflexe qu'avant : backup complet. Base de données et fichiers. Sauvegarde locale. On ne lance jamais une migration sans filet de sécurité.

**[ÉCRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Migration]

Va dans Tutor LMS, Tools, Migration. Cette fois, c'est la section "LifterLMS" qui nous intéresse. TutorLMS détecte les cours LifterLMS installés et affiche un résumé du contenu à migrer.

**[ÉCRAN — screencast processus de migration]**

[Montre la migration en cours]

Clique sur "Migrate". Le processus transfère :
- Les cours et leurs sections
- Les leçons
- Les quiz et questions
- Les inscriptions étudiants
- La progression

La structure LifterLMS est proche de celle de TutorLMS, donc la correspondance est assez directe. Les sections deviennent des topics, les leçons restent des leçons.

**[ÉCRAN — screencast vérification]**

[Vérification d'un cours migré — structure et front-end]

Vérification : ouvre un cours migré dans le Course Builder. Vérifie que les topics contiennent les bonnes leçons. Ouvre un quiz — vérifie les questions. Va en front-end pour vérifier l'affichage.

Côté étudiants : vérifie qu'un élève inscrit a bien ses cours et sa progression intacte.

**[TRANSITION — face caméra]**

Les éléments spécifiques à LifterLMS qui ne migrent pas : les Access Plans (les offres de vente LifterLMS), les memberships, les certificats et les achievements. Tu devras reconfigurer la monétisation dans TutorLMS — soit en mode natif, soit via WooCommerce si tu l'utilisais déjà.

Même conseil : staging d'abord, production ensuite. Et garde LifterLMS désactivé quelques semaines en sécurité.

---

**Points clés** :
- Backup complet avant migration
- Outil intégré : Tutor LMS > Tools > Migration > LifterLMS
- Migration des cours, leçons, quiz, inscriptions et progression
- Access Plans, memberships et certificats LifterLMS non migrés
- Reconfigurer la monétisation dans TutorLMS après migration
- Staging recommandé avant production

**Mots clés SEO** : migration LifterLMS TutorLMS, passer de LifterLMS à TutorLMS, transférer cours LifterLMS, changer LMS WordPress

---

### Leçon 13.3 — Migration LearnPress

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + LearnPress
**Source** : Vidéo #25 + doc migration/learnpress

---

**[INTRO — face caméra]**

LearnPress est le LMS gratuit le plus utilisé sur WordPress. Si tu as commencé avec et que tu veux passer à TutorLMS pour ses fonctionnalités avancées, la migration est possible. LearnPress a une structure simple — cours, leçons, quiz — et TutorLMS sait la récupérer.

**[ÉCRAN — screencast admin WordPress]**

[Backup]

Tu connais la musique : backup complet avant tout. Base de données, fichiers, copie locale. Pas de raccourci.

**[ÉCRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Migration]

Direction Tutor LMS, Tools, Migration. La section "LearnPress" apparaît si le plugin est installé. Tu vois le nombre de cours détectés.

**[ÉCRAN — screencast migration]**

[Lancement de la migration]

Clique sur "Migrate". LearnPress a une architecture plus simple que LearnDash ou LifterLMS, donc la migration est généralement rapide. Ce qui est transféré :
- Les cours
- Les leçons
- Les quiz et questions
- Les inscriptions étudiants

La progression des étudiants est aussi migrée quand elle est disponible.

**[ÉCRAN — screencast vérification]**

[Vérification cours migré]

Vérifie comme d'habitude : structure des cours dans le Course Builder, contenu des leçons, questions des quiz. Front-end pour l'affichage. Inscriptions étudiants.

**[TRANSITION — face caméra]**

LearnPress utilise des addons payants pour des fonctions que TutorLMS intègre nativement — certificats, prérequis, drip content. Une fois la migration faite, explore les réglages TutorLMS : tu auras probablement accès à des fonctions que tu payais en addon sur LearnPress.

Les shortcodes LearnPress dans tes pages sont à remplacer. Et les templates custom que tu aurais modifiés dans LearnPress ne s'appliquent pas à TutorLMS — il faudra adapter le design via ton page builder ou les templates TutorLMS.

---

**Points clés** :
- Backup complet obligatoire
- Outil intégré : Tutor LMS > Tools > Migration > LearnPress
- Migration des cours, leçons, quiz et inscriptions
- Structure simple = migration rapide
- Shortcodes et templates LearnPress à remplacer
- Fonctions payantes en addon LearnPress souvent incluses nativement dans TutorLMS

**Mots clés SEO** : migration LearnPress TutorLMS, passer de LearnPress à TutorLMS, transférer cours LearnPress, LearnPress vers TutorLMS

---

### Leçon 13.4 — Migration Zoom JWT vers OAuth

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + Zoom Marketplace
**Source** : Vidéo #20 + doc zoom-jwt-migration

---

**[INTRO — face caméra]**

Si tu utilises l'intégration Zoom dans TutorLMS, tu as peut-être configuré la connexion avec une app JWT. Problème : Zoom a déprécié les apps JWT. Elles ne fonctionnent plus. Tu dois migrer vers une app OAuth — c'est le nouveau standard. Cette leçon te montre comment faire la transition sans perdre tes meetings planifiés.

**[ÉCRAN — screencast Zoom Marketplace]**

[Navigation vers marketplace.zoom.us > Develop > Build App]

Va sur marketplace.zoom.us. Connecte-toi avec ton compte Zoom. Clique sur "Develop" puis "Build App". Tu vas créer une nouvelle app de type "General App" — c'est le type qui remplace JWT pour les connexions serveur.

**[ÉCRAN — screencast configuration app OAuth]**

[Configuration de l'app dans le Zoom Marketplace]

Dans la configuration de l'app :
- Donne-lui un nom — par exemple "TutorLMS Integration"
- Note le Client ID et le Client Secret qui sont générés
- Dans Redirect URL, entre l'URL que TutorLMS affiche dans ses réglages Zoom
- Dans les Scopes, ajoute les permissions nécessaires : meeting:read, meeting:write, user:read

Valide l'app. Elle passe en mode "activated".

**[ÉCRAN — screencast TutorLMS réglages Zoom]**

[Navigation vers Tutor LMS > Settings > Zoom]

Retourne dans TutorLMS, Settings, Zoom. Tu vois les champs pour la connexion. Remplace les anciennes valeurs JWT par le nouveau Client ID et Client Secret de ton app OAuth.

Clique sur "Connect" ou "Generate Token" — une fenêtre d'autorisation Zoom s'ouvre. Accepte les permissions. Le token est généré et la connexion est active.

**[ÉCRAN — screencast vérification]**

[Vérification d'un meeting existant + création d'un nouveau]

Vérifie que tes meetings existants fonctionnent toujours. Ouvre un cours qui avait un meeting Zoom planifié — il doit toujours apparaître. Crée un nouveau meeting pour confirmer que la connexion fonctionne dans les deux sens.

**[TRANSITION — face caméra]**

La migration JWT vers OAuth est obligatoire — les apps JWT ne fonctionnent plus. Si tu avais une app JWT, elle est déjà désactivée par Zoom. La bonne nouvelle : une fois la migration faite, OAuth est plus sécurisé et plus stable. Tu n'auras plus à te soucier de tokens qui expirent sans prévenir.

Si tu n'utilisais pas encore Zoom avec TutorLMS, cette leçon te sert de guide de configuration initiale — c'est exactement la même procédure.

---

**Points clés** :
- Zoom a déprécié les apps JWT — migration OAuth obligatoire
- Créer une "General App" sur marketplace.zoom.us
- Scopes nécessaires : meeting:read, meeting:write, user:read
- Remplacer Client ID/Secret dans Tutor LMS > Settings > Zoom
- Meetings existants conservés après migration
- OAuth est plus sécurisé et plus stable que JWT

**Mots clés SEO** : migration Zoom JWT OAuth TutorLMS, Zoom OAuth TutorLMS, configurer Zoom TutorLMS, intégration Zoom LMS WordPress

---

### Leçon 13.5 — Migration WooCommerce vers natif

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS + WooCommerce
**Source** : doc migration/woocommerce-migration

---

**[INTRO — face caméra]**

TutorLMS a longtemps nécessité WooCommerce pour vendre des cours. Ce n'est plus le cas — le système de monétisation natif de TutorLMS gère les paiements directement, avec Stripe ou PayPal, sans passer par WooCommerce. Moins de plugins, moins de complexité, moins de problèmes de compatibilité. Dans cette leçon, on migre d'une configuration WooCommerce vers le mode natif.

**[ÉCRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Monetization]

Première étape : comprendre ta situation actuelle. Va dans Tutor LMS, Settings, Monetization. Tu vois le mode actif — normalement "WooCommerce". On va passer en mode natif, mais pas tout de suite. Il faut d'abord préparer la transition.

**[ÉCRAN — screencast WooCommerce]**

[Navigation vers WooCommerce > Orders — liste des commandes]

Avant de désactiver WooCommerce, fais l'inventaire. Va dans WooCommerce, Orders. Note le nombre de commandes actives, les abonnements en cours si tu en as, et les produits liés à tes cours. Ces informations sont importantes pour la transition.

Exporte tes commandes en CSV — ça te sert de référence. Si tu utilises WooCommerce Subscriptions pour des abonnements récurrents, c'est le point le plus délicat. Le mode natif TutorLMS gère les paiements récurrents via Stripe, mais il faudra reconfigurer les abonnements.

**[ÉCRAN — screencast configuration mode natif]**

[Navigation vers Tutor LMS > Settings > Monetization > Native]

Maintenant, active le mode natif. Dans Monetization, sélectionne "Tutor Native". Tu vois les options de paiement : Stripe et PayPal.

Pour Stripe :
- Connecte ton compte Stripe avec les clés API (Publishable Key et Secret Key)
- Active le mode test d'abord pour vérifier que tout fonctionne
- Configure les webhooks si TutorLMS te le demande

Pour PayPal :
- Entre ton Client ID et ton Secret
- Même logique : mode test d'abord

**[ÉCRAN — screencast tarification des cours]**

[Navigation vers un cours > Settings > Prix]

Ensuite, configure les prix de tes cours. Ouvre chaque cours dans le Course Builder, va dans les Settings. Tu trouves la section prix. Définis :
- Le prix du cours
- Un prix barré (ancien prix) si tu veux afficher une remise
- Le type : achat unique ou abonnement

Avec WooCommerce, le prix était sur le produit WooCommerce. En mode natif, il est directement dans le cours TutorLMS. Plus simple.

**[ÉCRAN — screencast test d'achat]**

[Test front-end : achat d'un cours en mode test Stripe]

Teste un achat. Passe en mode test Stripe, ouvre un cours en front-end, clique sur "Enroll" ou "Buy Now". Le formulaire de paiement Stripe apparaît. Utilise la carte de test (4242 4242 4242 4242). Vérifie que l'inscription au cours se fait automatiquement après le paiement.

**[ÉCRAN — screencast désactivation WooCommerce]**

[Navigation vers Plugins > désactivation WooCommerce]

Une fois tout vérifié en mode test, puis en mode live avec un vrai achat test, tu peux désactiver WooCommerce. Va dans Plugins, désactive WooCommerce. Vérifie que ton site fonctionne normalement — pas d'erreurs, pas de pages cassées.

Ne supprime pas WooCommerce tout de suite. Désactive-le et laisse-le quelques semaines. Si tout roule, tu pourras le supprimer proprement.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : le mode natif est le meilleur choix pour la majorité des formateurs. C'est plus léger, plus rapide, et tu élimines une couche de complexité. Garde WooCommerce uniquement si tu vends aussi des produits physiques ou si tu as besoin de fonctions avancées comme les coupons complexes ou les bundles.

Point d'attention : les étudiants déjà inscrits via WooCommerce gardent leur accès. La migration ne touche pas les inscriptions existantes. Par contre, les nouveaux achats passeront par le système natif.

---

**Points clés** :
- Mode natif TutorLMS = paiements directs sans WooCommerce
- Exporter les commandes WooCommerce en CSV avant migration
- Configurer Stripe et/ou PayPal dans Tutor LMS > Settings > Monetization
- Prix définis directement dans chaque cours (plus dans WooCommerce)
- Tester en mode test avant de passer en production
- Inscriptions existantes préservées — seuls les nouveaux achats changent
- Garder WooCommerce désactivé (pas supprimé) quelques semaines

**Mots clés SEO** : migration WooCommerce TutorLMS natif, TutorLMS sans WooCommerce, monétisation native TutorLMS, Stripe TutorLMS

---

### Leçon 13.6 — Import/Export de cours

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast TutorLMS
**Source** : Vidéo #37 + doc import-export-courses

---

**[INTRO — face caméra]**

Tu veux dupliquer un cours d'un site à un autre ? Ou créer un backup de tes cours indépendant de la base de données ? TutorLMS intègre un système d'import/export qui transfère la structure complète d'un cours — contenu, leçons, quiz, questions. C'est aussi utile pour partager un modèle de cours avec un collègue ou un client.

**[ÉCRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Export]

Pour exporter, va dans Tutor LMS, Tools, puis Export. Tu vois la liste de tous tes cours. Sélectionne ceux que tu veux exporter — tu peux en choisir plusieurs.

Clique sur "Export". TutorLMS génère un fichier JSON ou ZIP qui contient :
- La structure du cours (topics, leçons)
- Le contenu des leçons
- Les quiz avec toutes les questions et réponses
- Les réglages du cours (durée, niveau, prérequis)

Ce qui n'est pas exporté : les inscriptions étudiants, les médias (images, vidéos) qui restent sur le serveur d'origine, et les réglages globaux de TutorLMS.

**[ÉCRAN — screencast import sur un autre site]**

[Navigation vers Tutor LMS > Tools > Import sur un deuxième site]

Sur le site de destination, va dans Tutor LMS, Tools, Import. Uploade le fichier exporté. TutorLMS lit le fichier et affiche un aperçu du contenu à importer.

Clique sur "Import". Les cours sont créés avec toute leur structure. Les leçons, quiz, questions — tout est là.

**[ÉCRAN — screencast vérification]**

[Ouverture d'un cours importé dans le Course Builder]

Vérifie le cours importé dans le Course Builder. La structure doit correspondre à l'original. Ouvre quelques leçons — le contenu texte est là. Les quiz ont leurs questions.

Ce qu'il faut ajuster après import :
- Les images et médias — re-uploade-les ou pointe vers les bonnes URLs
- Les liens internes qui pointaient vers l'ancien site
- Les instructeurs — assigne le bon profil instructeur sur le nouveau site
- Les prix — reconfigure-les si tu vends le cours

**[TRANSITION — face caméra]**

L'export/import TutorLMS est pratique pour trois cas : migrer des cours entre sites, créer des templates de cours réutilisables, et faire des backups ciblés. Pour un backup complet du site, utilise toujours un outil de backup classique en complément — l'export TutorLMS ne couvre que le contenu des cours, pas la config globale.

---

**Points clés** :
- Export : Tutor LMS > Tools > Export — sélectionner les cours
- Fichier JSON/ZIP avec structure, contenu, quiz et réglages du cours
- Import : Tutor LMS > Tools > Import sur le site de destination
- Médias, inscriptions et réglages globaux non inclus
- Ajuster images, liens, instructeurs et prix après import
- Utile pour migration entre sites, templates et backups ciblés

**Mots clés SEO** : import export cours TutorLMS, exporter cours TutorLMS, transférer cours entre sites WordPress, backup cours TutorLMS

---

### Leçon 13.7 — Quiz Module 13

**Type** : Quiz TutorLMS
**Questions** : 8 QCM
**Seuil de réussite** : 75%
**Tentatives** : Illimitées

---

**Question 1**
Quelle est la première étape avant toute migration de LMS ?

- A) Désactiver l'ancien plugin LMS
- B) Installer TutorLMS Pro
- C) Faire un backup complet (base de données + fichiers) ✓
- D) Exporter les cours en CSV

**Explication** : Un backup complet est obligatoire avant toute migration. Si quelque chose tourne mal, tu peux revenir à l'état précédent.

---

**Question 2**
Où se trouve l'outil de migration dans TutorLMS ?

- A) Tutor LMS > Settings > Migration
- B) Tutor LMS > Tools > Migration ✓
- C) Tutor LMS > Addons > Migration
- D) WordPress > Tools > Import

**Explication** : L'outil de migration intégré se trouve dans Tutor LMS > Tools > Migration. Il détecte automatiquement les LMS installés.

---

**Question 3**
Lors d'une migration LearnDash vers TutorLMS, lequel de ces éléments n'est PAS migré automatiquement ?

- A) Les cours et leçons
- B) Les quiz et questions
- C) Les certificats et badges LearnDash ✓
- D) Les inscriptions étudiants

**Explication** : Les certificats et badges sont spécifiques à LearnDash. Ils doivent être recréés dans TutorLMS après migration.

---

**Question 4**
Pourquoi faut-il migrer de Zoom JWT vers OAuth ?

- A) OAuth est gratuit, JWT est payant
- B) JWT offre moins de fonctionnalités
- C) Zoom a déprécié les apps JWT — elles ne fonctionnent plus ✓
- D) OAuth permet plus de participants

**Explication** : Zoom a déprécié et désactivé les apps JWT. La migration vers OAuth est obligatoire pour continuer à utiliser l'intégration Zoom.

---

**Question 5**
Quel avantage principal offre le mode de monétisation natif TutorLMS par rapport à WooCommerce ?

- A) Plus de passerelles de paiement disponibles
- B) Moins de plugins, moins de complexité, moins de problèmes de compatibilité ✓
- C) Des prix plus bas pour les étudiants
- D) Un meilleur SEO pour les pages de cours

**Explication** : Le mode natif élimine la dépendance à WooCommerce, ce qui réduit la complexité, les risques de conflits et améliore les performances.

---

**Question 6**
Lors de l'export de cours TutorLMS, lequel de ces éléments n'est PAS inclus dans le fichier exporté ?

- A) La structure du cours (topics, leçons)
- B) Les quiz et questions
- C) Les inscriptions étudiants et leur progression ✓
- D) Les réglages du cours

**Explication** : L'export couvre la structure, le contenu et les quiz, mais pas les inscriptions étudiants, les médias ni les réglages globaux.

---

**Question 7**
Après une migration WooCommerce vers le mode natif TutorLMS, que se passe-t-il pour les étudiants déjà inscrits ?

- A) Ils perdent leur accès aux cours
- B) Ils doivent racheter les cours
- C) Ils gardent leur accès — seuls les nouveaux achats changent ✓
- D) Ils doivent créer un nouveau compte

**Explication** : Les inscriptions existantes sont préservées. La migration affecte uniquement le système de paiement pour les futurs achats.

---

**Question 8**
Quelle est la recommandation schoolsWP pour tester une migration de LMS ?

- A) Migrer directement en production pour gagner du temps
- B) Migrer sur un environnement de staging d'abord, vérifier, puis reproduire en production ✓
- C) Faire la migration un dimanche quand il y a moins de trafic
- D) Demander à l'hébergeur de faire la migration

**Explication** : Toujours tester sur un staging avant de migrer en production. Ça permet de vérifier que tout fonctionne sans risquer de casser le site en ligne.

---

**Fin du Module 13 — Migration**

Résumé du module :
- Migration LearnDash/LifterLMS/LearnPress : outil intégré Tutor LMS > Tools > Migration
- Backup complet obligatoire avant toute migration
- Certificats, badges et shortcodes de l'ancien LMS à reconfigurer manuellement
- Zoom JWT vers OAuth : migration obligatoire (apps JWT dépréciées)
- WooCommerce vers natif : moins de plugins, prix directement dans les cours
- Import/Export : transfert de cours entre sites via fichier JSON/ZIP
- Toujours tester sur staging avant production

Durée totale estimée du module : ~35 minutes

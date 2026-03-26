# Scripts video — Module 13 : Migration

**Formation** : Maitriser TutorLMS
**Module** : M13 — Migration (Premium)
**Lecons** : 6 videos + 1 quiz
**Duree totale** : ~35 min
**Date** : 2026-03-23

---

### Lecon 13.1 — Migration LearnDash

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + LearnDash
**Source** : Video #13 + doc migration/learndash

---

**[INTRO — face camera]**

Tu es sur LearnDash et tu veux passer a TutorLMS ? Bonne nouvelle : TutorLMS integre un outil de migration qui transfere tes cours, lecons, quiz et inscriptions etudiants. Pas besoin de tout reconstruire a la main. Mais avant de toucher a quoi que ce soit — on fait un backup complet. C'est la regle numero un de toute migration.

**[ECRAN — screencast admin WordPress]**

[Navigation vers l'outil de backup — UpdraftPlus ou equivalent]

Avant de commencer, sauvegarde tout. Base de donnees et fichiers. Utilise UpdraftPlus, WPVivid ou ton outil habituel. Telecharge la sauvegarde en local — pas juste sur le serveur. Si la migration tourne mal, tu veux pouvoir revenir a l'etat exact d'avant.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Migration]

Une fois le backup fait, va dans Tutor LMS, puis Tools, puis Migration. Tu vois la section "LearnDash". TutorLMS detecte automatiquement si LearnDash est installe et affiche le nombre de cours, lecons et quiz disponibles pour la migration.

**[ECRAN — screencast processus de migration]**

[Montre le bouton de migration et la progression]

Clique sur "Migrate". Le processus se lance. Selon le volume de contenu, ca peut prendre de quelques secondes a plusieurs minutes. Ne ferme pas la fenetre — laisse le processus terminer.

Ce qui est migre :
- Les cours avec leur structure (sections, lecons)
- Les quiz et leurs questions
- Les inscriptions etudiants — chaque eleve garde ses cours
- La progression des eleves — ce qui a ete complete reste complete

**[ECRAN — screencast verification post-migration]**

[Navigation vers Tutor LMS > Courses — verification d'un cours migre]

Une fois termine, verifie. Ouvre Tutor LMS, Courses. Tes cours LearnDash doivent apparaitre. Ouvre-en un, verifie la structure : sections, lecons, quiz. Passe cote front-end pour confirmer que l'affichage est correct.

Verifie aussi les inscriptions : va dans un cours, onglet Students. Les eleves doivent etre la avec leur progression.

**[TRANSITION — face camera]**

Points importants : certains elements ne migrent pas automatiquement. Les certificats LearnDash, les badges et les reglages specifiques de LearnDash — comme les timer de quiz avances — devront etre reconfigures dans TutorLMS. Pareil pour les shortcodes LearnDash dans tes pages — il faudra les remplacer par les shortcodes TutorLMS.

La recommandation schoolsWP : fais la migration sur un environnement de staging d'abord. Verifie tout, puis reproduis sur la production. Et garde LearnDash installe mais desactive pendant quelques semaines — au cas ou tu aurais besoin de verifier un detail.

---

**Points cles** :
- Backup complet obligatoire avant toute migration (base + fichiers)
- Outil integre : Tutor LMS > Tools > Migration > LearnDash
- Migration des cours, lecons, quiz, inscriptions et progression
- Certificats, badges et shortcodes LearnDash a reconfigurer manuellement
- Tester sur un staging avant de migrer en production
- Garder LearnDash desactive (pas supprime) pendant quelques semaines

**Mots cles SEO** : migration LearnDash TutorLMS, passer de LearnDash a TutorLMS, transferer cours LearnDash, migration LMS WordPress

---

### Lecon 13.2 — Migration LifterLMS

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + LifterLMS
**Source** : Video #24 + doc migration/lifterlms

---

**[INTRO — face camera]**

Tu utilises LifterLMS et tu veux migrer vers TutorLMS ? Le processus est similaire a la migration LearnDash — TutorLMS detecte LifterLMS et propose un transfert automatique. Comme toujours, on commence par un backup.

**[ECRAN — screencast admin WordPress]**

[Navigation vers l'outil de backup]

Meme reflexe qu'avant : backup complet. Base de donnees et fichiers. Sauvegarde locale. On ne lance jamais une migration sans filet de securite.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Migration]

Va dans Tutor LMS, Tools, Migration. Cette fois, c'est la section "LifterLMS" qui nous interesse. TutorLMS detecte les cours LifterLMS installes et affiche un resume du contenu a migrer.

**[ECRAN — screencast processus de migration]**

[Montre la migration en cours]

Clique sur "Migrate". Le processus transfere :
- Les cours et leurs sections
- Les lecons
- Les quiz et questions
- Les inscriptions etudiants
- La progression

La structure LifterLMS est proche de celle de TutorLMS, donc la correspondance est assez directe. Les sections deviennent des topics, les lecons restent des lecons.

**[ECRAN — screencast verification]**

[Verification d'un cours migre — structure et front-end]

Verification : ouvre un cours migre dans le Course Builder. Verifie que les topics contiennent les bonnes lecons. Ouvre un quiz — verifie les questions. Va en front-end pour verifier l'affichage.

Cote etudiants : verifie qu'un eleve inscrit a bien ses cours et sa progression intacte.

**[TRANSITION — face camera]**

Les elements specifiques a LifterLMS qui ne migrent pas : les Access Plans (les offres de vente LifterLMS), les memberships, les certificats et les achievements. Tu devras reconfigurer la monetisation dans TutorLMS — soit en mode natif, soit via WooCommerce si tu l'utilisais deja.

Meme conseil : staging d'abord, production ensuite. Et garde LifterLMS desactive quelques semaines en securite.

---

**Points cles** :
- Backup complet avant migration
- Outil integre : Tutor LMS > Tools > Migration > LifterLMS
- Migration des cours, lecons, quiz, inscriptions et progression
- Access Plans, memberships et certificats LifterLMS non migres
- Reconfigurer la monetisation dans TutorLMS apres migration
- Staging recommande avant production

**Mots cles SEO** : migration LifterLMS TutorLMS, passer de LifterLMS a TutorLMS, transferer cours LifterLMS, changer LMS WordPress

---

### Lecon 13.3 — Migration LearnPress

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + LearnPress
**Source** : Video #25 + doc migration/learnpress

---

**[INTRO — face camera]**

LearnPress est le LMS gratuit le plus utilise sur WordPress. Si tu as commence avec et que tu veux passer a TutorLMS pour ses fonctionnalites avancees, la migration est possible. LearnPress a une structure simple — cours, lecons, quiz — et TutorLMS sait la recuperer.

**[ECRAN — screencast admin WordPress]**

[Backup]

Tu connais la musique : backup complet avant tout. Base de donnees, fichiers, copie locale. Pas de raccourci.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Migration]

Direction Tutor LMS, Tools, Migration. La section "LearnPress" apparait si le plugin est installe. Tu vois le nombre de cours detectes.

**[ECRAN — screencast migration]**

[Lancement de la migration]

Clique sur "Migrate". LearnPress a une architecture plus simple que LearnDash ou LifterLMS, donc la migration est generalement rapide. Ce qui est transfere :
- Les cours
- Les lecons
- Les quiz et questions
- Les inscriptions etudiants

La progression des etudiants est aussi migree quand elle est disponible.

**[ECRAN — screencast verification]**

[Verification cours migre]

Verifie comme d'habitude : structure des cours dans le Course Builder, contenu des lecons, questions des quiz. Front-end pour l'affichage. Inscriptions etudiants.

**[TRANSITION — face camera]**

LearnPress utilise des addons payants pour des fonctions que TutorLMS integre nativement — certificats, prerequis, drip content. Une fois la migration faite, explore les reglages TutorLMS : tu auras probablement acces a des fonctions que tu payais en addon sur LearnPress.

Les shortcodes LearnPress dans tes pages sont a remplacer. Et les templates custom que tu aurais modifies dans LearnPress ne s'appliquent pas a TutorLMS — il faudra adapter le design via ton page builder ou les templates TutorLMS.

---

**Points cles** :
- Backup complet obligatoire
- Outil integre : Tutor LMS > Tools > Migration > LearnPress
- Migration des cours, lecons, quiz et inscriptions
- Structure simple = migration rapide
- Shortcodes et templates LearnPress a remplacer
- Fonctions payantes en addon LearnPress souvent incluses nativement dans TutorLMS

**Mots cles SEO** : migration LearnPress TutorLMS, passer de LearnPress a TutorLMS, transferer cours LearnPress, LearnPress vers TutorLMS

---

### Lecon 13.4 — Migration Zoom JWT vers OAuth

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + Zoom Marketplace
**Source** : Video #20 + doc zoom-jwt-migration

---

**[INTRO — face camera]**

Si tu utilises l'integration Zoom dans TutorLMS, tu as peut-etre configure la connexion avec une app JWT. Probleme : Zoom a deprecie les apps JWT. Elles ne fonctionnent plus. Tu dois migrer vers une app OAuth — c'est le nouveau standard. Cette lecon te montre comment faire la transition sans perdre tes meetings planifies.

**[ECRAN — screencast Zoom Marketplace]**

[Navigation vers marketplace.zoom.us > Develop > Build App]

Va sur marketplace.zoom.us. Connecte-toi avec ton compte Zoom. Clique sur "Develop" puis "Build App". Tu vas creer une nouvelle app de type "General App" — c'est le type qui remplace JWT pour les connexions serveur.

**[ECRAN — screencast configuration app OAuth]**

[Configuration de l'app dans le Zoom Marketplace]

Dans la configuration de l'app :
- Donne-lui un nom — par exemple "TutorLMS Integration"
- Note le Client ID et le Client Secret qui sont generes
- Dans Redirect URL, entre l'URL que TutorLMS affiche dans ses reglages Zoom
- Dans les Scopes, ajoute les permissions necessaires : meeting:read, meeting:write, user:read

Valide l'app. Elle passe en mode "activated".

**[ECRAN — screencast TutorLMS reglages Zoom]**

[Navigation vers Tutor LMS > Settings > Zoom]

Retourne dans TutorLMS, Settings, Zoom. Tu vois les champs pour la connexion. Remplace les anciennes valeurs JWT par le nouveau Client ID et Client Secret de ton app OAuth.

Clique sur "Connect" ou "Generate Token" — une fenetre d'autorisation Zoom s'ouvre. Accepte les permissions. Le token est genere et la connexion est active.

**[ECRAN — screencast verification]**

[Verification d'un meeting existant + creation d'un nouveau]

Verifie que tes meetings existants fonctionnent toujours. Ouvre un cours qui avait un meeting Zoom planifie — il doit toujours apparaitre. Cree un nouveau meeting pour confirmer que la connexion fonctionne dans les deux sens.

**[TRANSITION — face camera]**

La migration JWT vers OAuth est obligatoire — les apps JWT ne fonctionnent plus. Si tu avais une app JWT, elle est deja desactivee par Zoom. La bonne nouvelle : une fois la migration faite, OAuth est plus securise et plus stable. Tu n'auras plus a te soucier de tokens qui expirent sans prevenir.

Si tu n'utilisais pas encore Zoom avec TutorLMS, cette lecon te sert de guide de configuration initiale — c'est exactement la meme procedure.

---

**Points cles** :
- Zoom a deprecie les apps JWT — migration OAuth obligatoire
- Creer une "General App" sur marketplace.zoom.us
- Scopes necessaires : meeting:read, meeting:write, user:read
- Remplacer Client ID/Secret dans Tutor LMS > Settings > Zoom
- Meetings existants conserves apres migration
- OAuth est plus securise et plus stable que JWT

**Mots cles SEO** : migration Zoom JWT OAuth TutorLMS, Zoom OAuth TutorLMS, configurer Zoom TutorLMS, integration Zoom LMS WordPress

---

### Lecon 13.5 — Migration WooCommerce vers natif

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS + WooCommerce
**Source** : doc migration/woocommerce-migration

---

**[INTRO — face camera]**

TutorLMS a longtemps necessite WooCommerce pour vendre des cours. Ce n'est plus le cas — le systeme de monetisation natif de TutorLMS gere les paiements directement, avec Stripe ou PayPal, sans passer par WooCommerce. Moins de plugins, moins de complexite, moins de problemes de compatibilite. Dans cette lecon, on migre d'une configuration WooCommerce vers le mode natif.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Settings > Monetization]

Premiere etape : comprendre ta situation actuelle. Va dans Tutor LMS, Settings, Monetization. Tu vois le mode actif — normalement "WooCommerce". On va passer en mode natif, mais pas tout de suite. Il faut d'abord preparer la transition.

**[ECRAN — screencast WooCommerce]**

[Navigation vers WooCommerce > Orders — liste des commandes]

Avant de desactiver WooCommerce, fais l'inventaire. Va dans WooCommerce, Orders. Note le nombre de commandes actives, les abonnements en cours si tu en as, et les produits lies a tes cours. Ces informations sont importantes pour la transition.

Exporte tes commandes en CSV — ca te sert de reference. Si tu utilises WooCommerce Subscriptions pour des abonnements recurrents, c'est le point le plus delicat. Le mode natif TutorLMS gere les paiements recurrents via Stripe, mais il faudra reconfigurer les abonnements.

**[ECRAN — screencast configuration mode natif]**

[Navigation vers Tutor LMS > Settings > Monetization > Native]

Maintenant, active le mode natif. Dans Monetization, selectionne "Tutor Native". Tu vois les options de paiement : Stripe et PayPal.

Pour Stripe :
- Connecte ton compte Stripe avec les cles API (Publishable Key et Secret Key)
- Active le mode test d'abord pour verifier que tout fonctionne
- Configure les webhooks si TutorLMS te le demande

Pour PayPal :
- Entre ton Client ID et ton Secret
- Meme logique : mode test d'abord

**[ECRAN — screencast tarification des cours]**

[Navigation vers un cours > Settings > Prix]

Ensuite, configure les prix de tes cours. Ouvre chaque cours dans le Course Builder, va dans les Settings. Tu trouves la section prix. Definis :
- Le prix du cours
- Un prix barre (ancien prix) si tu veux afficher une remise
- Le type : achat unique ou abonnement

Avec WooCommerce, le prix etait sur le produit WooCommerce. En mode natif, il est directement dans le cours TutorLMS. Plus simple.

**[ECRAN — screencast test d'achat]**

[Test front-end : achat d'un cours en mode test Stripe]

Teste un achat. Passe en mode test Stripe, ouvre un cours en front-end, clique sur "Enroll" ou "Buy Now". Le formulaire de paiement Stripe apparait. Utilise la carte de test (4242 4242 4242 4242). Verifie que l'inscription au cours se fait automatiquement apres le paiement.

**[ECRAN — screencast desactivation WooCommerce]**

[Navigation vers Plugins > desactivation WooCommerce]

Une fois tout verifie en mode test, puis en mode live avec un vrai achat test, tu peux desactiver WooCommerce. Va dans Plugins, desactive WooCommerce. Verifie que ton site fonctionne normalement — pas d'erreurs, pas de pages cassees.

Ne supprime pas WooCommerce tout de suite. Desactive-le et laisse-le quelques semaines. Si tout roule, tu pourras le supprimer proprement.

**[TRANSITION — face camera]**

La recommandation schoolsWP : le mode natif est le meilleur choix pour la majorite des formateurs. C'est plus leger, plus rapide, et tu elimines une couche de complexite. Garde WooCommerce uniquement si tu vends aussi des produits physiques ou si tu as besoin de fonctions avancees comme les coupons complexes ou les bundles.

Point d'attention : les etudiants deja inscrits via WooCommerce gardent leur acces. La migration ne touche pas les inscriptions existantes. Par contre, les nouveaux achats passeront par le systeme natif.

---

**Points cles** :
- Mode natif TutorLMS = paiements directs sans WooCommerce
- Exporter les commandes WooCommerce en CSV avant migration
- Configurer Stripe et/ou PayPal dans Tutor LMS > Settings > Monetization
- Prix definis directement dans chaque cours (plus dans WooCommerce)
- Tester en mode test avant de passer en production
- Inscriptions existantes preservees — seuls les nouveaux achats changent
- Garder WooCommerce desactive (pas supprime) quelques semaines

**Mots cles SEO** : migration WooCommerce TutorLMS natif, TutorLMS sans WooCommerce, monetisation native TutorLMS, Stripe TutorLMS

---

### Lecon 13.6 — Import/Export de cours

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast TutorLMS
**Source** : Video #37 + doc import-export-courses

---

**[INTRO — face camera]**

Tu veux dupliquer un cours d'un site a un autre ? Ou creer un backup de tes cours independant de la base de donnees ? TutorLMS integre un systeme d'import/export qui transfere la structure complete d'un cours — contenu, lecons, quiz, questions. C'est aussi utile pour partager un modele de cours avec un collegue ou un client.

**[ECRAN — screencast TutorLMS admin]**

[Navigation vers Tutor LMS > Tools > Export]

Pour exporter, va dans Tutor LMS, Tools, puis Export. Tu vois la liste de tous tes cours. Selectionne ceux que tu veux exporter — tu peux en choisir plusieurs.

Clique sur "Export". TutorLMS genere un fichier JSON ou ZIP qui contient :
- La structure du cours (topics, lecons)
- Le contenu des lecons
- Les quiz avec toutes les questions et reponses
- Les reglages du cours (duree, niveau, prerequis)

Ce qui n'est pas exporte : les inscriptions etudiants, les medias (images, videos) qui restent sur le serveur d'origine, et les reglages globaux de TutorLMS.

**[ECRAN — screencast import sur un autre site]**

[Navigation vers Tutor LMS > Tools > Import sur un deuxieme site]

Sur le site de destination, va dans Tutor LMS, Tools, Import. Uploade le fichier exporte. TutorLMS lit le fichier et affiche un apercu du contenu a importer.

Clique sur "Import". Les cours sont crees avec toute leur structure. Les lecons, quiz, questions — tout est la.

**[ECRAN — screencast verification]**

[Ouverture d'un cours importe dans le Course Builder]

Verifie le cours importe dans le Course Builder. La structure doit correspondre a l'original. Ouvre quelques lecons — le contenu texte est la. Les quiz ont leurs questions.

Ce qu'il faut ajuster apres import :
- Les images et medias — re-uploade-les ou pointe vers les bonnes URLs
- Les liens internes qui pointaient vers l'ancien site
- Les instructeurs — assigne le bon profil instructeur sur le nouveau site
- Les prix — reconfigure-les si tu vends le cours

**[TRANSITION — face camera]**

L'export/import TutorLMS est pratique pour trois cas : migrer des cours entre sites, creer des templates de cours reutilisables, et faire des backups cibles. Pour un backup complet du site, utilise toujours un outil de backup classique en complement — l'export TutorLMS ne couvre que le contenu des cours, pas la config globale.

---

**Points cles** :
- Export : Tutor LMS > Tools > Export — selectionner les cours
- Fichier JSON/ZIP avec structure, contenu, quiz et reglages du cours
- Import : Tutor LMS > Tools > Import sur le site de destination
- Medias, inscriptions et reglages globaux non inclus
- Ajuster images, liens, instructeurs et prix apres import
- Utile pour migration entre sites, templates et backups cibles

**Mots cles SEO** : import export cours TutorLMS, exporter cours TutorLMS, transferer cours entre sites WordPress, backup cours TutorLMS

---

### Lecon 13.7 — Quiz Module 13

**Type** : Quiz TutorLMS
**Questions** : 8 QCM
**Seuil de reussite** : 75%
**Tentatives** : Illimitees

---

**Question 1**
Quelle est la premiere etape avant toute migration de LMS ?

- A) Desactiver l'ancien plugin LMS
- B) Installer TutorLMS Pro
- C) Faire un backup complet (base de donnees + fichiers) ✓
- D) Exporter les cours en CSV

**Explication** : Un backup complet est obligatoire avant toute migration. Si quelque chose tourne mal, tu peux revenir a l'etat precedent.

---

**Question 2**
Ou se trouve l'outil de migration dans TutorLMS ?

- A) Tutor LMS > Settings > Migration
- B) Tutor LMS > Tools > Migration ✓
- C) Tutor LMS > Addons > Migration
- D) WordPress > Tools > Import

**Explication** : L'outil de migration integre se trouve dans Tutor LMS > Tools > Migration. Il detecte automatiquement les LMS installes.

---

**Question 3**
Lors d'une migration LearnDash vers TutorLMS, lequel de ces elements n'est PAS migre automatiquement ?

- A) Les cours et lecons
- B) Les quiz et questions
- C) Les certificats et badges LearnDash ✓
- D) Les inscriptions etudiants

**Explication** : Les certificats et badges sont specifiques a LearnDash. Ils doivent etre recrees dans TutorLMS apres migration.

---

**Question 4**
Pourquoi faut-il migrer de Zoom JWT vers OAuth ?

- A) OAuth est gratuit, JWT est payant
- B) JWT offre moins de fonctionnalites
- C) Zoom a deprecie les apps JWT — elles ne fonctionnent plus ✓
- D) OAuth permet plus de participants

**Explication** : Zoom a deprecie et desactive les apps JWT. La migration vers OAuth est obligatoire pour continuer a utiliser l'integration Zoom.

---

**Question 5**
Quel avantage principal offre le mode de monetisation natif TutorLMS par rapport a WooCommerce ?

- A) Plus de passerelles de paiement disponibles
- B) Moins de plugins, moins de complexite, moins de problemes de compatibilite ✓
- C) Des prix plus bas pour les etudiants
- D) Un meilleur SEO pour les pages de cours

**Explication** : Le mode natif elimine la dependance a WooCommerce, ce qui reduit la complexite, les risques de conflits et ameliore les performances.

---

**Question 6**
Lors de l'export de cours TutorLMS, lequel de ces elements n'est PAS inclus dans le fichier exporte ?

- A) La structure du cours (topics, lecons)
- B) Les quiz et questions
- C) Les inscriptions etudiants et leur progression ✓
- D) Les reglages du cours

**Explication** : L'export couvre la structure, le contenu et les quiz, mais pas les inscriptions etudiants, les medias ni les reglages globaux.

---

**Question 7**
Apres une migration WooCommerce vers le mode natif TutorLMS, que se passe-t-il pour les etudiants deja inscrits ?

- A) Ils perdent leur acces aux cours
- B) Ils doivent racheter les cours
- C) Ils gardent leur acces — seuls les nouveaux achats changent ✓
- D) Ils doivent creer un nouveau compte

**Explication** : Les inscriptions existantes sont preservees. La migration affecte uniquement le systeme de paiement pour les futurs achats.

---

**Question 8**
Quelle est la recommandation schoolsWP pour tester une migration de LMS ?

- A) Migrer directement en production pour gagner du temps
- B) Migrer sur un environnement de staging d'abord, verifier, puis reproduire en production ✓
- C) Faire la migration un dimanche quand il y a moins de trafic
- D) Demander a l'hebergeur de faire la migration

**Explication** : Toujours tester sur un staging avant de migrer en production. Ca permet de verifier que tout fonctionne sans risquer de casser le site en ligne.

---

**Fin du Module 13 — Migration**

Resume du module :
- Migration LearnDash/LifterLMS/LearnPress : outil integre Tutor LMS > Tools > Migration
- Backup complet obligatoire avant toute migration
- Certificats, badges et shortcodes de l'ancien LMS a reconfigurer manuellement
- Zoom JWT vers OAuth : migration obligatoire (apps JWT depreciees)
- WooCommerce vers natif : moins de plugins, prix directement dans les cours
- Import/Export : transfert de cours entre sites via fichier JSON/ZIP
- Toujours tester sur staging avant production

Duree totale estimee du module : ~35 minutes

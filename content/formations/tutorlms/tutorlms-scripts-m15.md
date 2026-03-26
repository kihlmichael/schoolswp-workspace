# Scripts video — Module 15 : Troubleshooting

**Formation** : Maitriser TutorLMS
**Module** : M15 — Troubleshooting (Premium)
**Lecons** : 6 videos + 1 quiz
**Duree totale** : ~30 min
**Date** : 2026-03-23

---

### Lecon 15.1 — Diagnostics generaux

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin + outils
**Source** : Creation originale schoolsWP

---

**[INTRO — face camera]**

Quelque chose ne fonctionne pas sur ton site TutorLMS. Un cours ne s'affiche pas, un paiement ne passe pas, un email n'arrive pas. Avant de chercher des solutions specifiques, il faut poser un diagnostic. Dans cette lecon, je te donne la methode systematique pour identifier l'origine d'un probleme sur TutorLMS — en moins de 5 minutes.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Status]

Premier reflexe : verifie le statut systeme. Va dans Tutor LMS, puis Status. Cette page te donne un rapport complet : version PHP, version WordPress, version TutorLMS, extensions actives, et surtout les conflits detectes. Si une ligne est en rouge, c'est ton point de depart.

**[ECRAN — screencast page Status]**

Verifie trois choses dans l'ordre :

1. La version PHP. TutorLMS demande PHP 7.4 minimum, mais la recommandation schoolsWP est PHP 8.1 ou plus. Si tu es en dessous, contacte ton hebergeur pour upgrader.

2. La limite memoire. Si tu vois "WP Memory Limit" en dessous de 256M, c'est une source frequente de problemes. On va corriger ca.

3. Les extensions en conflit. TutorLMS liste les plugins qui posent probleme. Note-les.

**[ECRAN — screencast wp-config.php]**

[Montre l'edition de wp-config.php via le gestionnaire de fichiers ou FTP]

Pour augmenter la limite memoire, ouvre ton fichier wp-config.php. Ajoute cette ligne avant le commentaire "That's all, stop editing" :

```
define('WP_MEMORY_LIMIT', '256M');
```

Sauvegarde. Retourne sur la page Status — la valeur doit etre a jour.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Extensions > Extensions installees]

Deuxieme outil de diagnostic : le test de conflit de plugins. Desactive tous tes plugins sauf TutorLMS et TutorLMS Pro. Teste si le probleme persiste. Si le probleme disparait, reactive les plugins un par un jusqu'a trouver le coupable.

C'est la methode la plus fiable. Ca prend 5 minutes et ca evite de chercher dans le vide pendant des heures.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Apparence > Themes]

Troisieme test : le theme. Active temporairement un theme par defaut — Twenty Twenty-Four par exemple. Si le probleme disparait, c'est ton theme qui est en cause. Contacte le developpeur du theme ou verifie qu'il est compatible avec TutorLMS.

**[ECRAN — screencast navigateur]**

[Montre la console du navigateur — F12 > Console]

Dernier outil : la console du navigateur. Appuie sur F12, onglet Console. Les erreurs JavaScript s'affichent en rouge. Si tu vois des erreurs liees a "tutor" ou a un plugin specifique, tu tiens ta piste.

**[TRANSITION — face camera]**

Retiens cette methode en 4 etapes : page Status, limite memoire, test de conflit plugins, test de theme. Dans 80% des cas, tu identifies le probleme sans meme chercher sur Google. Les lecons suivantes traitent les problemes specifiques les plus frequents — mais commence toujours par ce diagnostic general.

---

**Points cles** :
- Page Tutor LMS > Status : premier reflexe pour tout probleme
- PHP 8.1+ recommande, memoire 256M minimum
- Test de conflit : desactiver tous les plugins sauf TutorLMS, reactiver un par un
- Test de theme : activer Twenty Twenty-Four temporairement
- Console navigateur (F12) pour les erreurs JavaScript

**Mots cles SEO** : TutorLMS probleme, debug TutorLMS, TutorLMS ne fonctionne pas, diagnostic WordPress LMS

---

### Lecon 15.2 — Erreur 404

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin
**Source** : Creation originale schoolsWP

---

**[INTRO — face camera]**

Tu cliques sur un cours et tu tombes sur une page 404. Ou pire : tes eleves te signalent que les lecons renvoient une erreur "page introuvable". C'est l'un des problemes les plus courants avec TutorLMS — et dans 90% des cas, la solution prend 30 secondes. On voit ca.

**[ECRAN — screencast navigateur]**

[Montre une page 404 sur un cours TutorLMS]

Le symptome : tu accedes a un cours, une lecon ou une page TutorLMS, et WordPress affiche une erreur 404. L'URL semble correcte, mais la page n'existe pas.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Reglages > Permaliens]

Cause numero un — et de loin la plus frequente : les permaliens. Quand tu installes TutorLMS, que tu actives un addon, ou que tu mets a jour le plugin, WordPress doit regenerer ses regles de reecriture d'URL. Si ca ne se fait pas automatiquement, tu obtiens des 404.

La solution : va dans Reglages, Permaliens. Tu n'as rien a changer. Clique simplement sur "Enregistrer les modifications". Ca force WordPress a regenerer le fichier .htaccess avec les nouvelles regles. Retourne sur ton cours — le 404 devrait avoir disparu.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Course]

Cause numero deux : le slug de cours en conflit. TutorLMS utilise par defaut le slug "courses" pour les cours. Si un autre plugin ou une page WordPress utilise deja ce slug, ca cree un conflit.

Verifie dans Tutor LMS, Settings, Course. Le champ "Course Permalink Base" te montre le slug utilise. Si tu as un conflit, change-le — par exemple "formation" au lieu de "courses". Sauvegarde, puis retourne dans Reglages > Permaliens et re-sauvegarde aussi.

**[ECRAN — screencast gestionnaire de fichiers]**

[Montre le fichier .htaccess a la racine du site]

Cause numero trois : le fichier .htaccess est corrompu ou mal configure. Si les deux premieres solutions ne marchent pas, verifie ton fichier .htaccess a la racine du site via FTP ou le gestionnaire de fichiers de ton hebergeur.

Un .htaccess WordPress standard doit contenir ce bloc :

```
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress
```

Si tu vois des lignes suspectes ou si le fichier est vide, remplace-le par ce contenu standard, puis re-sauvegarde les permaliens.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Status]

Cause numero quatre — plus rare : un probleme de cache. Si tu utilises un plugin de cache (WP Rocket, LiteSpeed Cache, W3 Total Cache), vide le cache completement apres avoir corrige les permaliens. Certains plugins de cache mettent en cache les pages 404, ce qui fait croire que le probleme persiste alors qu'il est resolu.

**[TRANSITION — face camera]**

La prevention : chaque fois que tu mets a jour TutorLMS ou que tu actives un addon, prends le reflexe de re-sauvegarder les permaliens. Ca prend 10 secondes et ca evite les 404. Si le probleme persiste apres toutes ces etapes, c'est probablement un conflit de plugin — reviens a la methode de diagnostic de la lecon precedente.

---

**Points cles** :
- Cause n1 : permaliens a re-sauvegarder (Reglages > Permaliens > Enregistrer)
- Cause n2 : slug de cours en conflit — changer dans Tutor LMS > Settings > Course
- Cause n3 : fichier .htaccess corrompu — remplacer par le contenu standard
- Cause n4 : cache a vider apres correction
- Prevention : re-sauvegarder les permaliens apres chaque mise a jour ou activation d'addon

**Mots cles SEO** : TutorLMS erreur 404, page introuvable TutorLMS, permaliens TutorLMS, 404 cours WordPress

---

### Lecon 15.3 — Commandes non completees

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin + WooCommerce
**Source** : Creation originale schoolsWP

---

**[INTRO — face camera]**

Un eleve a paye, mais sa commande reste en "pending" ou "processing". Il n'a pas acces au cours. C'est frustrant pour lui — et c'est une vente perdue si tu ne reagis pas vite. Dans cette lecon, on voit pourquoi les commandes restent bloquees et comment debloquer la situation.

**[ECRAN — screencast WordPress admin]**

[Navigation vers TutorLMS > Commandes ou WooCommerce > Commandes]

Le symptome : tu vois des commandes avec le statut "Pending", "On Hold" ou "Processing" qui ne passent jamais en "Completed". L'eleve a paye mais n'a pas acces au cours.

Premier cas : tu utilises le eCommerce natif de TutorLMS. Va dans Tutor LMS, puis Orders. Clique sur la commande bloquee. Verifie le statut du paiement. Si le paiement est bien recu (tu le vois dans ton tableau de bord Stripe ou PayPal), tu peux manuellement passer la commande en "Completed".

**[ECRAN — screencast Stripe Dashboard]**

[Montre le tableau de bord Stripe avec un paiement recu]

Verifie toujours dans le tableau de bord de ta passerelle de paiement. Si le paiement apparait comme "Succeeded" chez Stripe mais que la commande est en "Pending" dans TutorLMS, c'est un probleme de communication entre les deux — le webhook n'est pas passe.

**[ECRAN — screencast WordPress admin — Tutor LMS Settings]**

[Navigation vers Tutor LMS > Settings > Monetization]

Cause frequente : la configuration de la passerelle de paiement est incomplete. Va dans Tutor LMS, Settings, Monetization. Verifie que :

- La bonne passerelle est selectionnee (Stripe ou PayPal)
- Les cles API sont correctes (cle publique ET cle secrete)
- Tu es bien en mode "Live" et pas en mode "Test" (erreur classique)

Si tu etais en mode Test, passe en Live, puis demande a l'eleve de recommencer le paiement.

**[ECRAN — screencast WordPress admin — WooCommerce]**

[Navigation vers WooCommerce > Reglages > Paiements]

Deuxieme cas : tu utilises WooCommerce. Le probleme est le meme mais les reglages sont ailleurs. Va dans WooCommerce, Reglages, Paiements. Verifie que ta passerelle est activee et correctement configuree.

Point important avec WooCommerce : par defaut, les commandes de produits virtuels et telechargeables passent automatiquement en "Completed". Mais il faut que tes produits cours soient bien configures comme "Virtual". Si ce n'est pas le cas, WooCommerce attend une expedition — qui n'arrivera jamais.

**[ECRAN — screencast WooCommerce produit]**

[Montre l'edition d'un produit cours avec la case "Virtual" cochee]

Ouvre le produit WooCommerce lie a ton cours. Dans l'onglet "General" ou "Donnees produit", coche la case "Virtual". Sauvegarde. Les prochaines commandes pour ce cours passeront automatiquement en "Completed" apres paiement.

**[ECRAN — screencast WordPress admin]**

Pour debloquer les commandes existantes : dans WooCommerce > Commandes, ouvre la commande bloquee. Change manuellement le statut en "Completed". L'eleve recevra l'email de confirmation et aura acces au cours immediatement.

**[TRANSITION — face camera]**

La prevention : configure correctement tes passerelles de paiement des le depart — cles Live, pas Test. Si tu utilises WooCommerce, coche "Virtual" sur tous tes produits cours. Et verifie regulierement tes commandes — une commande bloquee pendant 48h, c'est un eleve qui ne revient pas.

---

**Points cles** :
- Verifier le statut du paiement dans le tableau de bord Stripe/PayPal
- eCommerce natif : cles API correctes + mode Live (pas Test)
- WooCommerce : produits cours doivent etre "Virtual" pour auto-completer
- Deblocage manuel : changer le statut de la commande en "Completed"
- Prevention : verification reguliere des commandes en attente

**Mots cles SEO** : TutorLMS commande bloquee, paiement TutorLMS pending, WooCommerce cours non complete, TutorLMS Stripe probleme

---

### Lecon 15.4 — Problemes certificats

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin
**Source** : Creation originale schoolsWP

---

**[INTRO — face camera]**

Ton eleve a termine le cours, mais son certificat ne s'affiche pas. Ou le certificat est la, mais le nom est faux, le design est casse, ou le PDF ne se telecharge pas. Les certificats sont un element de fidelisation important — si ca ne marche pas, tes eleves sont decus. On corrige ca.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Addons]

Premiere verification : l'addon Certificates est-il actif ? Va dans Tutor LMS, Addons. Cherche "Certificate". Il y a deux addons possibles :

- "Certificate" — l'addon de base
- "Certificate Customizer" — l'addon avance qui permet de creer des templates personnalises

Au minimum, "Certificate" doit etre actif. Si tu veux des certificats personnalises, active aussi "Certificate Customizer".

**[ECRAN — screencast Tutor LMS Settings]**

[Navigation vers Tutor LMS > Settings > Course]

Deuxieme verification : les certificats sont-ils actives au niveau des reglages. Va dans Tutor LMS, Settings, Course. Cherche l'option "Certificate". Elle doit etre activee.

Ensuite, verifie dans les reglages du cours specifique. Ouvre le cours dans le Course Builder, et dans les options du cours, verifie qu'un template de certificat est bien selectionne. Si aucun template n'est attribue, l'eleve ne verra rien meme apres avoir termine le cours.

**[ECRAN — screencast Course Builder]**

[Montre la selection d'un template de certificat dans un cours]

Ouvre le cours concerne. Dans les parametres du cours, section "Certificate", selectionne un template. Tu as les templates par defaut de TutorLMS, ou tes templates personnalises si tu utilises le Certificate Customizer. Sauvegarde le cours.

**[ECRAN — screencast navigateur — vue eleve]**

[Montre la page de cours cote eleve avec le bouton certificat]

Troisieme verification : est-ce que l'eleve a vraiment termine le cours a 100% ? Le certificat ne se debloque que quand toutes les conditions sont remplies :

- Toutes les lecons marquees comme terminees
- Tous les quiz passes (avec le score minimum requis si tu en as defini un)
- Le pourcentage de completion est a 100%

Si l'eleve a saute une lecon ou un quiz, le certificat reste bloque.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > rapport d'un eleve specifique]

Pour verifier : va dans le profil de l'eleve dans TutorLMS. Tu vois sa progression par cours. Si le cours n'est pas a 100%, identifie la lecon ou le quiz manquant et previens l'eleve.

**[ECRAN — screencast Certificate Customizer]**

Si le certificat s'affiche mais avec un design casse — texte qui deborde, nom mal place — c'est un probleme de template. Ouvre le Certificate Customizer et verifie que les champs dynamiques sont correctement places :

- {student_name} — nom de l'eleve
- {course_name} — nom du cours
- {completion_date} — date de completion
- {certificate_number} — numero unique

Repositionne les champs si necessaire et previsualise avant de sauvegarder.

**[TRANSITION — face camera]**

La prevention : quand tu crees un cours, attribue toujours un template de certificat des le depart. Teste le parcours complet toi-meme — inscris-toi comme eleve test, termine le cours, et verifie que le certificat se genere correctement. C'est 10 minutes de test qui evitent des dizaines de reclamations.

---

**Points cles** :
- Addon "Certificate" (+ optionnel "Certificate Customizer") doit etre actif
- Certificat active dans les reglages globaux ET dans chaque cours individuellement
- L'eleve doit avoir 100% de completion (lecons + quiz)
- Champs dynamiques a verifier dans le template : {student_name}, {course_name}, {completion_date}
- Prevention : tester le parcours complet avec un compte eleve test

**Mots cles SEO** : TutorLMS certificat ne s'affiche pas, probleme certificat TutorLMS, certificate not showing TutorLMS, certificat cours WordPress

---

### Lecon 15.5 — Emails non envoyes

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin + FluentSMTP
**Source** : Creation originale schoolsWP

---

**[INTRO — face camera]**

Tes eleves ne recoivent pas les emails de confirmation d'inscription, de completion de cours, ou de reinitialisation de mot de passe. C'est l'un des problemes les plus courants sur WordPress — et il n'est pas specifique a TutorLMS. Le probleme vient presque toujours de la facon dont WordPress envoie ses emails. On diagnostique et on corrige.

**[ECRAN — screencast WordPress admin]**

[Vue d'ensemble du probleme]

Le symptome : les emails partent de WordPress mais n'arrivent jamais dans la boite de reception de l'eleve. Ou ils arrivent dans les spams. Ou certains emails arrivent et d'autres non.

La cause : par defaut, WordPress envoie ses emails via la fonction PHP `wp_mail()`. Cette methode n'utilise pas d'authentification — les serveurs de messagerie (Gmail, Outlook) considerent ces emails comme suspects et les bloquent ou les mettent en spam.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Extensions > Ajouter]

La solution : utiliser un plugin SMTP qui authentifie les emails. La recommandation schoolsWP : FluentSMTP. C'est gratuit, leger, et developpe par la meme equipe que FluentCRM.

Installe et active FluentSMTP.

**[ECRAN — screencast FluentSMTP]**

[Navigation vers Reglages > FluentSMTP]

FluentSMTP te propose plusieurs services : Amazon SES, SendGrid, Mailgun, Gmail API, SMTP generique, et d'autres. Le choix depend de ton volume :

- Moins de 300 emails par jour : Gmail API ou le SMTP de ton hebergeur
- 300 a 10 000 emails par jour : SendGrid (gratuit jusqu'a 100/jour) ou Amazon SES
- Plus de 10 000 : Amazon SES (le moins cher)

Pour cette demo, on configure avec le SMTP de base — ca fonctionne avec n'importe quel hebergeur.

**[ECRAN — screencast FluentSMTP configuration]**

[Montre la configuration SMTP pas a pas]

Clique sur "Add Another Connection", puis selectionne "Other SMTP". Remplis :

- Sender Email : ton email professionnel (ex: contact@ton-site.fr)
- Sender Name : le nom qui apparaitra (ex: le nom de ta formation)
- SMTP Host : celui de ton hebergeur (ex: mail.ton-site.fr ou smtp.gmail.com)
- Port : 587 (TLS) ou 465 (SSL) — 587 est le standard
- Username : ton adresse email complete
- Password : le mot de passe ou le mot de passe d'application

Sauvegarde la connexion.

**[ECRAN — screencast FluentSMTP test]**

[Montre l'envoi d'un email de test]

Maintenant, teste. FluentSMTP a un bouton "Send Test Email". Entre ton adresse personnelle et envoie. Verifie que l'email arrive dans ta boite — pas dans les spams.

Si le test echoue, verifie :
- Le host et le port (demande a ton hebergeur si tu doutes)
- Le mot de passe (pour Gmail, il faut un "mot de passe d'application", pas ton mot de passe habituel)
- Que le port 587 n'est pas bloque par ton hebergeur

**[ECRAN — screencast FluentSMTP logs]**

[Montre l'onglet Email Logs]

FluentSMTP a un onglet "Email Logs" qui enregistre tous les emails envoyes. Tu vois le statut de chaque email : envoye, echoue, en attente. Si un email echoue, le log te donne le message d'erreur exact.

Active les logs — c'est indispensable pour diagnostiquer les problemes d'email.

**[ECRAN — screencast Tutor LMS Settings]**

[Navigation vers Tutor LMS > Settings > Email]

Dernier point : verifie que les notifications email sont activees dans TutorLMS. Va dans Tutor LMS, Settings, Email. Tu vois la liste de toutes les notifications : inscription, completion de cours, nouveau quiz, etc. Active celles que tu veux envoyer et personnalise les templates si necessaire.

**[TRANSITION — face camera]**

La recommandation schoolsWP est claire : installe FluentSMTP des le jour un. Meme avant de creer ton premier cours. Sans SMTP authentifie, tes emails finiront en spam — c'est une certitude, pas un risque. Et active les logs pour pouvoir diagnostiquer les problemes rapidement.

---

**Points cles** :
- WordPress envoie des emails non authentifies par defaut — d'ou le spam
- Solution : FluentSMTP (gratuit) pour authentifier les envois
- Configuration : host, port 587, identifiants email
- Tester avec le bouton "Send Test Email" avant de mettre en production
- Activer les Email Logs pour diagnostiquer les echecs
- Verifier les notifications activees dans Tutor LMS > Settings > Email

**Mots cles SEO** : TutorLMS email non recu, emails spam WordPress, FluentSMTP TutorLMS, notification email LMS WordPress

---

### Lecon 15.6 — Compatibilite Yoast/RankMath

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress admin
**Source** : Creation originale schoolsWP

---

**[INTRO — face camera]**

TutorLMS cree des pages de cours, de lecons, de quiz — et ton plugin SEO doit les gerer correctement. Que tu utilises RankMath ou Yoast, il y a des conflits potentiels : balises meta en double, sitemaps incomplets, ou schema markup qui se contredit. Dans cette lecon, on configure la cohabitation proprement.

**[ECRAN — screencast WordPress admin]**

[Montre un cours TutorLMS avec RankMath ou Yoast actif]

Le symptome : tu installes RankMath ou Yoast, et tu remarques des problemes sur tes pages de cours :

- Deux balises title differentes dans le code source
- Les cours n'apparaissent pas dans le sitemap
- Le schema markup "Course" de TutorLMS entre en conflit avec le schema de ton plugin SEO
- Les meta descriptions sont vides ou dupliquees

**[ECRAN — screencast WordPress admin — RankMath]**

[Navigation vers RankMath > Titles & Meta > Custom Post Types]

Commencons par RankMath — c'est la recommandation schoolsWP. Va dans RankMath, Titles & Meta, puis cherche la section pour les types de contenu personnalises. Tu dois voir "Courses", "Lessons", "Quizzes".

Pour les cours : active l'indexation et configure le template de titre et de meta description. Utilise les variables dynamiques de RankMath :

- Titre : `%title% - %sitename%`
- Meta description : `%excerpt%` ou ecris un template personnalise

Pour les lecons et les quiz : desactive l'indexation. Les lecons ne doivent pas etre indexees individuellement — elles font partie d'un cours. Si tu les indexes, tu crees du contenu duplique et tu dilues l'autorite de tes pages de cours.

**[ECRAN — screencast RankMath Sitemap]**

[Navigation vers RankMath > Sitemap Settings]

Deuxieme etape : le sitemap. Va dans RankMath, Sitemap Settings. Verifie que "Courses" est inclus dans le sitemap. Exclue "Lessons" et "Quizzes" du sitemap — coherent avec le choix de ne pas les indexer.

**[ECRAN — screencast RankMath Schema]**

[Navigation vers RankMath > Schema sur une page de cours]

Troisieme etape : le schema markup. TutorLMS genere automatiquement un schema "Course" sur les pages de cours. RankMath genere aussi un schema. Resultat : deux schemas "Course" sur la meme page — Google n'aime pas ca.

La solution : dans RankMath, sur les pages de type "Course", desactive le schema automatique de RankMath ou configure-le pour utiliser le type "Article" au lieu de "Course". Laisse TutorLMS gerer le schema "Course" — il contient les donnees structurees les plus completes (prix, duree, nombre d'eleves, note moyenne).

**[ECRAN — screencast WordPress admin — Yoast]**

[Navigation vers Yoast SEO > Search Appearance > Content Types]

Si tu utilises Yoast : meme logique. Va dans Yoast SEO, Search Appearance, Content Types. Pour "Courses" : active l'affichage dans les resultats de recherche. Pour "Lessons" et "Quizzes" : desactive.

Pour le schema : Yoast ajoute automatiquement un schema sur toutes les pages. Pour eviter le doublon avec TutorLMS, tu peux utiliser le filtre `wpseo_schema_graph` dans un snippet PHP pour retirer le schema "Course" de Yoast sur les pages de cours TutorLMS. Ou plus simplement : dans les reglages schema de Yoast pour le type "Course", selectionne "Web Page" au lieu de "Course".

**[ECRAN — screencast code source page]**

[Montre la verification du code source avec Ctrl+U]

Pour verifier que tout est propre : ouvre une page de cours, fais Ctrl+U pour voir le code source. Cherche "schema" ou "ld+json". Tu dois voir un seul bloc schema de type "Course" — celui de TutorLMS. Si tu en vois deux, il reste un conflit a corriger.

**[TRANSITION — face camera]**

La recommandation schoolsWP : utilise RankMath. L'integration avec TutorLMS est plus propre qu'avec Yoast. Indexe les cours, pas les lecons ni les quiz. Et laisse TutorLMS gerer le schema "Course" — c'est lui qui a les donnees les plus completes. Avec cette configuration, tes pages de cours sont optimisees pour Google sans conflit.

---

**Points cles** :
- Indexer les cours, ne PAS indexer les lecons ni les quiz (contenu duplique)
- Sitemap : inclure les cours, exclure lecons et quiz
- Schema : laisser TutorLMS gerer le schema "Course", configurer RankMath/Yoast sur "Article" ou "Web Page"
- Verification : Ctrl+U sur une page de cours, chercher "ld+json" — un seul bloc "Course"
- Recommandation schoolsWP : RankMath plutot que Yoast pour TutorLMS

**Mots cles SEO** : TutorLMS RankMath, TutorLMS Yoast SEO, schema cours WordPress, SEO formation en ligne WordPress, TutorLMS sitemap

---

### Lecon 15.7 — Quiz Module 15

**Duree** : ~4 min (8 questions)
**Type** : Quiz TutorLMS
**Seuil de reussite** : 70%

---

**Question 1**
Quel est le premier reflexe a avoir quand quelque chose ne fonctionne pas sur TutorLMS ?

- A) Reinstaller le plugin
- B) Contacter le support Themeum
- C) Consulter la page Tutor LMS > Status pour verifier le rapport systeme ✓
- D) Desactiver tous les plugins

**Explication** : La page Status donne un rapport complet (version PHP, memoire, conflits). C'est toujours le point de depart du diagnostic.

---

**Question 2**
Quelle est la solution la plus frequente pour une erreur 404 sur un cours TutorLMS ?

- A) Reinstaller TutorLMS
- B) Changer de theme
- C) Re-sauvegarder les permaliens dans Reglages > Permaliens ✓
- D) Vider le cache du navigateur

**Explication** : Dans 90% des cas, re-sauvegarder les permaliens force WordPress a regenerer les regles de reecriture d'URL et corrige les 404.

---

**Question 3**
Une commande reste en "Pending" alors que l'eleve a paye via Stripe. Que faut-il verifier en priorite ?

- A) Que l'eleve a bien un compte WordPress
- B) Que le paiement apparait comme "Succeeded" dans le tableau de bord Stripe ✓
- C) Que le cours est bien publie
- D) Que le theme est compatible

**Explication** : Si le paiement est recu chez Stripe mais que la commande est en "Pending" dans TutorLMS, c'est un probleme de webhook — le paiement a ete effectue mais la notification n'est pas passee.

---

**Question 4**
Quelles sont les conditions pour qu'un certificat se debloque pour un eleve ?

- A) L'eleve doit avoir visionne au moins 80% des lecons
- B) L'eleve doit avoir complete 100% du cours (lecons + quiz) ET un template de certificat doit etre attribue au cours ✓
- C) L'eleve doit en faire la demande manuelle
- D) Le certificat se debloque automatiquement apres 30 jours

**Explication** : Le certificat necessite 100% de completion (toutes les lecons + tous les quiz au score minimum) et un template de certificat selectionne dans les parametres du cours.

---

**Question 5**
Pourquoi les emails WordPress finissent-ils souvent en spam ?

- A) Parce que WordPress envoie trop d'emails
- B) Parce que la fonction wp_mail() par defaut n'utilise pas d'authentification SMTP ✓
- C) Parce que Gmail bloque tous les emails WordPress
- D) Parce que TutorLMS n'envoie pas les bons headers

**Explication** : Par defaut, WordPress utilise wp_mail() sans authentification. Les serveurs de messagerie traitent ces emails comme suspects. Un plugin SMTP (FluentSMTP) resout le probleme.

---

**Question 6**
Quel plugin SMTP gratuit schoolsWP recommande-t-il ?

- A) WP Mail SMTP
- B) Post SMTP
- C) FluentSMTP ✓
- D) Easy WP SMTP

**Explication** : FluentSMTP est gratuit, leger, et developpe par la meme equipe que FluentCRM. Il offre des logs d'emails integres pour diagnostiquer les problemes.

---

**Question 7**
Faut-il indexer les lecons TutorLMS individuellement dans Google ?

- A) Oui, chaque lecon doit etre indexee pour maximiser le trafic
- B) Non — les lecons ne doivent pas etre indexees individuellement pour eviter le contenu duplique ✓
- C) Seulement les lecons gratuites
- D) Seulement si on utilise RankMath

**Explication** : Les lecons font partie d'un cours. Les indexer individuellement cree du contenu duplique et dilue l'autorite des pages de cours. Seuls les cours doivent etre indexes.

---

**Question 8**
Comment eviter un doublon de schema markup "Course" entre TutorLMS et RankMath ?

- A) Desactiver le schema dans TutorLMS
- B) Configurer RankMath sur le type "Article" ou "Web Page" pour les cours, et laisser TutorLMS gerer le schema "Course" ✓
- C) Desinstaller RankMath sur les pages de cours
- D) Utiliser un plugin tiers pour fusionner les schemas

**Explication** : TutorLMS genere un schema "Course" avec les donnees les plus completes (prix, duree, note). Il faut configurer RankMath pour ne pas generer un second schema "Course" sur ces pages.

---

**Fin du Module 15 — Troubleshooting**

Resume du module :
- Diagnostic general : page Status, test de conflit plugins, test de theme, console navigateur
- Erreur 404 : re-sauvegarder les permaliens (solution dans 90% des cas)
- Commandes bloquees : verifier passerelle de paiement, mode Live, produits "Virtual"
- Certificats : addon actif + template attribue + completion 100%
- Emails : FluentSMTP obligatoire des le jour un + logs actifs
- SEO : indexer les cours uniquement, schema "Course" gere par TutorLMS

Duree totale estimee du module : ~30 minutes

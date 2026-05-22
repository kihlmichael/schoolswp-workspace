# Scripts vidéo — Module 15 : Troubleshooting

**Formation** : Maîtriser TutorLMS
**Module** : M15 — Troubleshooting (Premium)
**Leçons** : 6 vidéos + 1 quiz
**Durée totale** : ~30 min
**Date** : 2026-03-23

---

### Leçon 15.1 — Diagnostics généraux

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin + outils
**Source** : Création originale schoolsWP

---

**[INTRO — face caméra]**

Quelque chose ne fonctionne pas sur ton site TutorLMS. Un cours ne s'affiche pas, un paiement ne passe pas, un email n'arrive pas. Avant de chercher des solutions spécifiques, il faut poser un diagnostic. Dans cette leçon, je te donne la méthode systématique pour identifier l'origine d'un problème sur TutorLMS — en moins de 5 minutes.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Status]

Premier réflexe : vérifie le statut système. Va dans Tutor LMS, puis Status. Cette page te donne un rapport complet : version PHP, version WordPress, version TutorLMS, extensions actives, et surtout les conflits détectés. Si une ligne est en rouge, c'est ton point de départ.

**[ÉCRAN — screencast page Status]**

Vérifie trois choses dans l'ordre :

1. La version PHP. TutorLMS demande PHP 7.4 minimum, mais la recommandation schoolsWP est PHP 8.1 ou plus. Si tu es en dessous, contacte ton hébergeur pour upgrader.

2. La limite mémoire. Si tu vois "WP Memory Limit" en dessous de 256M, c'est une source fréquente de problèmes. On va corriger ça.

3. Les extensions en conflit. TutorLMS liste les plugins qui posent problème. Note-les.

**[ÉCRAN — screencast wp-config.php]**

[Montre l'édition de wp-config.php via le gestionnaire de fichiers ou FTP]

Pour augmenter la limite mémoire, ouvre ton fichier wp-config.php. Ajoute cette ligne avant le commentaire "That's all, stop editing" :

```
define('WP_MEMORY_LIMIT', '256M');
```

Sauvegarde. Retourne sur la page Status — la valeur doit être à jour.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Extensions > Extensions installées]

Deuxième outil de diagnostic : le test de conflit de plugins. Désactive tous tes plugins sauf TutorLMS et TutorLMS Pro. Teste si le problème persiste. Si le problème disparaît, réactive les plugins un par un jusqu'à trouver le coupable.

C'est la méthode la plus fiable. Ça prend 5 minutes et ça évite de chercher dans le vide pendant des heures.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Apparence > Thèmes]

Troisième test : le thème. Active temporairement un thème par défaut — Twenty Twenty-Four par exemple. Si le problème disparaît, c'est ton thème qui est en cause. Contacte le développeur du thème ou vérifie qu'il est compatible avec TutorLMS.

**[ÉCRAN — screencast navigateur]**

[Montre la console du navigateur — F12 > Console]

Dernier outil : la console du navigateur. Appuie sur F12, onglet Console. Les erreurs JavaScript s'affichent en rouge. Si tu vois des erreurs liées à "tutor" ou à un plugin spécifique, tu tiens ta piste.

**[TRANSITION — face caméra]**

Retiens cette méthode en 4 étapes : page Status, limite mémoire, test de conflit plugins, test de thème. Dans 80% des cas, tu identifies le problème sans même chercher sur Google. Les leçons suivantes traitent les problèmes spécifiques les plus fréquents — mais commence toujours par ce diagnostic général.

---

**Points clés** :
- Page Tutor LMS > Status : premier réflexe pour tout problème
- PHP 8.1+ recommandé, mémoire 256M minimum
- Test de conflit : désactiver tous les plugins sauf TutorLMS, réactiver un par un
- Test de thème : activer Twenty Twenty-Four temporairement
- Console navigateur (F12) pour les erreurs JavaScript

**Mots clés SEO** : TutorLMS problème, debug TutorLMS, TutorLMS ne fonctionne pas, diagnostic WordPress LMS

---

### Leçon 15.2 — Erreur 404

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin
**Source** : Création originale schoolsWP

---

**[INTRO — face caméra]**

Tu cliques sur un cours et tu tombes sur une page 404. Ou pire : tes élèves te signalent que les leçons renvoient une erreur "page introuvable". C'est l'un des problèmes les plus courants avec TutorLMS — et dans 90% des cas, la solution prend 30 secondes. On voit ça.

**[ÉCRAN — screencast navigateur]**

[Montre une page 404 sur un cours TutorLMS]

Le symptôme : tu accèdes à un cours, une leçon ou une page TutorLMS, et WordPress affiche une erreur 404. L'URL semble correcte, mais la page n'existe pas.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Réglages > Permaliens]

Cause numéro un — et de loin la plus fréquente : les permaliens. Quand tu installes TutorLMS, que tu actives un addon, ou que tu mets à jour le plugin, WordPress doit régénérer ses règles de réécriture d'URL. Si ça ne se fait pas automatiquement, tu obtiens des 404.

La solution : va dans Réglages, Permaliens. Tu n'as rien à changer. Clique simplement sur "Enregistrer les modifications". Ça force WordPress à régénérer le fichier .htaccess avec les nouvelles règles. Retourne sur ton cours — le 404 devrait avoir disparu.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Course]

Cause numéro deux : le slug de cours en conflit. TutorLMS utilise par défaut le slug "courses" pour les cours. Si un autre plugin ou une page WordPress utilise déjà ce slug, ça crée un conflit.

Vérifie dans Tutor LMS, Settings, Course. Le champ "Course Permalink Base" te montre le slug utilisé. Si tu as un conflit, change-le — par exemple "formation" au lieu de "courses". Sauvegarde, puis retourne dans Réglages > Permaliens et re-sauvegarde aussi.

**[ÉCRAN — screencast gestionnaire de fichiers]**

[Montre le fichier .htaccess à la racine du site]

Cause numéro trois : le fichier .htaccess est corrompu ou mal configuré. Si les deux premières solutions ne marchent pas, vérifie ton fichier .htaccess à la racine du site via FTP ou le gestionnaire de fichiers de ton hébergeur.

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

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Status]

Cause numéro quatre — plus rare : un problème de cache. Si tu utilises un plugin de cache (WP Rocket, LiteSpeed Cache, W3 Total Cache), vide le cache complètement après avoir corrigé les permaliens. Certains plugins de cache mettent en cache les pages 404, ce qui fait croire que le problème persiste alors qu'il est résolu.

**[TRANSITION — face caméra]**

La prévention : chaque fois que tu mets à jour TutorLMS ou que tu actives un addon, prends le réflexe de re-sauvegarder les permaliens. Ça prend 10 secondes et ça évite les 404. Si le problème persiste après toutes ces étapes, c'est probablement un conflit de plugin — reviens à la méthode de diagnostic de la leçon précédente.

---

**Points clés** :
- Cause n1 : permaliens à re-sauvegarder (Réglages > Permaliens > Enregistrer)
- Cause n2 : slug de cours en conflit — changer dans Tutor LMS > Settings > Course
- Cause n3 : fichier .htaccess corrompu — remplacer par le contenu standard
- Cause n4 : cache à vider après correction
- Prévention : re-sauvegarder les permaliens après chaque mise à jour ou activation d'addon

**Mots clés SEO** : TutorLMS erreur 404, page introuvable TutorLMS, permaliens TutorLMS, 404 cours WordPress

---

### Leçon 15.3 — Commandes non complétées

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin + WooCommerce
**Source** : Création originale schoolsWP

---

**[INTRO — face caméra]**

Un élève a payé, mais sa commande reste en "pending" ou "processing". Il n'a pas accès au cours. C'est frustrant pour lui — et c'est une vente perdue si tu ne réagis pas vite. Dans cette leçon, on voit pourquoi les commandes restent bloquées et comment débloquer la situation.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers TutorLMS > Commandes ou WooCommerce > Commandes]

Le symptôme : tu vois des commandes avec le statut "Pending", "On Hold" ou "Processing" qui ne passent jamais en "Completed". L'élève a payé mais n'a pas accès au cours.

Premier cas : tu utilises le eCommerce natif de TutorLMS. Va dans Tutor LMS, puis Orders. Clique sur la commande bloquée. Vérifie le statut du paiement. Si le paiement est bien reçu (tu le vois dans ton tableau de bord Stripe ou PayPal), tu peux manuellement passer la commande en "Completed".

**[ÉCRAN — screencast Stripe Dashboard]**

[Montre le tableau de bord Stripe avec un paiement reçu]

Vérifie toujours dans le tableau de bord de ta passerelle de paiement. Si le paiement apparaît comme "Succeeded" chez Stripe mais que la commande est en "Pending" dans TutorLMS, c'est un problème de communication entre les deux — le webhook n'est pas passé.

**[ÉCRAN — screencast WordPress admin — Tutor LMS Settings]**

[Navigation vers Tutor LMS > Settings > Monetization]

Cause fréquente : la configuration de la passerelle de paiement est incomplète. Va dans Tutor LMS, Settings, Monetization. Vérifie que :

- La bonne passerelle est sélectionnée (Stripe ou PayPal)
- Les clés API sont correctes (clé publique ET clé secrète)
- Tu es bien en mode "Live" et pas en mode "Test" (erreur classique)

Si tu étais en mode Test, passe en Live, puis demande à l'élève de recommencer le paiement.

**[ÉCRAN — screencast WordPress admin — WooCommerce]**

[Navigation vers WooCommerce > Réglages > Paiements]

Deuxième cas : tu utilises WooCommerce. Le problème est le même mais les réglages sont ailleurs. Va dans WooCommerce, Réglages, Paiements. Vérifie que ta passerelle est activée et correctement configurée.

Point important avec WooCommerce : par défaut, les commandes de produits virtuels et téléchargeables passent automatiquement en "Completed". Mais il faut que tes produits cours soient bien configurés comme "Virtual". Si ce n'est pas le cas, WooCommerce attend une expédition — qui n'arrivera jamais.

**[ÉCRAN — screencast WooCommerce produit]**

[Montre l'édition d'un produit cours avec la case "Virtual" cochée]

Ouvre le produit WooCommerce lié à ton cours. Dans l'onglet "General" ou "Données produit", coche la case "Virtual". Sauvegarde. Les prochaines commandes pour ce cours passeront automatiquement en "Completed" après paiement.

**[ÉCRAN — screencast WordPress admin]**

Pour débloquer les commandes existantes : dans WooCommerce > Commandes, ouvre la commande bloquée. Change manuellement le statut en "Completed". L'élève recevra l'email de confirmation et aura accès au cours immédiatement.

**[TRANSITION — face caméra]**

La prévention : configure correctement tes passerelles de paiement dès le départ — clés Live, pas Test. Si tu utilises WooCommerce, coche "Virtual" sur tous tes produits cours. Et vérifie régulièrement tes commandes — une commande bloquée pendant 48h, c'est un élève qui ne revient pas.

---

**Points clés** :
- Vérifier le statut du paiement dans le tableau de bord Stripe/PayPal
- eCommerce natif : clés API correctes + mode Live (pas Test)
- WooCommerce : produits cours doivent être "Virtual" pour auto-compléter
- Déblocage manuel : changer le statut de la commande en "Completed"
- Prévention : vérification régulière des commandes en attente

**Mots clés SEO** : TutorLMS commande bloquée, paiement TutorLMS pending, WooCommerce cours non complété, TutorLMS Stripe problème

---

### Leçon 15.4 — Problèmes certificats

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin
**Source** : Création originale schoolsWP

---

**[INTRO — face caméra]**

Ton élève a terminé le cours, mais son certificat ne s'affiche pas. Ou le certificat est là, mais le nom est faux, le design est cassé, ou le PDF ne se télécharge pas. Les certificats sont un élément de fidélisation important — si ça ne marche pas, tes élèves sont déçus. On corrige ça.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Addons]

Première vérification : l'addon Certificates est-il actif ? Va dans Tutor LMS, Addons. Cherche "Certificate". Il y a deux addons possibles :

- "Certificate" — l'addon de base
- "Certificate Customizer" — l'addon avancé qui permet de créer des templates personnalisés

Au minimum, "Certificate" doit être actif. Si tu veux des certificats personnalisés, active aussi "Certificate Customizer".

**[ÉCRAN — screencast Tutor LMS Settings]**

[Navigation vers Tutor LMS > Settings > Course]

Deuxième vérification : les certificats sont-ils activés au niveau des réglages. Va dans Tutor LMS, Settings, Course. Cherche l'option "Certificate". Elle doit être activée.

Ensuite, vérifie dans les réglages du cours spécifique. Ouvre le cours dans le Course Builder, et dans les options du cours, vérifie qu'un template de certificat est bien sélectionné. Si aucun template n'est attribué, l'élève ne verra rien même après avoir terminé le cours.

**[ÉCRAN — screencast Course Builder]**

[Montre la sélection d'un template de certificat dans un cours]

Ouvre le cours concerné. Dans les paramètres du cours, section "Certificate", sélectionne un template. Tu as les templates par défaut de TutorLMS, ou tes templates personnalisés si tu utilises le Certificate Customizer. Sauvegarde le cours.

**[ÉCRAN — screencast navigateur — vue élève]**

[Montre la page de cours côté élève avec le bouton certificat]

Troisième vérification : est-ce que l'élève a vraiment terminé le cours à 100% ? Le certificat ne se débloque que quand toutes les conditions sont remplies :

- Toutes les leçons marquées comme terminées
- Tous les quiz passés (avec le score minimum requis si tu en as défini un)
- Le pourcentage de complétion est à 100%

Si l'élève a sauté une leçon ou un quiz, le certificat reste bloqué.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > rapport d'un élève spécifique]

Pour vérifier : va dans le profil de l'élève dans TutorLMS. Tu vois sa progression par cours. Si le cours n'est pas à 100%, identifie la leçon ou le quiz manquant et préviens l'élève.

**[ÉCRAN — screencast Certificate Customizer]**

Si le certificat s'affiche mais avec un design cassé — texte qui déborde, nom mal placé — c'est un problème de template. Ouvre le Certificate Customizer et vérifie que les champs dynamiques sont correctement placés :

- {student_name} — nom de l'élève
- {course_name} — nom du cours
- {completion_date} — date de complétion
- {certificate_number} — numéro unique

Repositionne les champs si nécessaire et prévisualise avant de sauvegarder.

**[TRANSITION — face caméra]**

La prévention : quand tu crées un cours, attribue toujours un template de certificat dès le départ. Teste le parcours complet toi-même — inscris-toi comme élève test, termine le cours, et vérifie que le certificat se génère correctement. C'est 10 minutes de test qui évitent des dizaines de réclamations.

---

**Points clés** :
- Addon "Certificate" (+ optionnel "Certificate Customizer") doit être actif
- Certificat activé dans les réglages globaux ET dans chaque cours individuellement
- L'élève doit avoir 100% de complétion (leçons + quiz)
- Champs dynamiques à vérifier dans le template : {student_name}, {course_name}, {completion_date}
- Prévention : tester le parcours complet avec un compte élève test

**Mots clés SEO** : TutorLMS certificat ne s'affiche pas, problème certificat TutorLMS, certificate not showing TutorLMS, certificat cours WordPress

---

### Leçon 15.5 — Emails non envoyés

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin + FluentSMTP
**Source** : Création originale schoolsWP

---

**[INTRO — face caméra]**

Tes élèves ne reçoivent pas les emails de confirmation d'inscription, de complétion de cours, ou de réinitialisation de mot de passe. C'est l'un des problèmes les plus courants sur WordPress — et il n'est pas spécifique à TutorLMS. Le problème vient presque toujours de la façon dont WordPress envoie ses emails. On diagnostique et on corrige.

**[ÉCRAN — screencast WordPress admin]**

[Vue d'ensemble du problème]

Le symptôme : les emails partent de WordPress mais n'arrivent jamais dans la boîte de réception de l'élève. Ou ils arrivent dans les spams. Ou certains emails arrivent et d'autres non.

La cause : par défaut, WordPress envoie ses emails via la fonction PHP `wp_mail()`. Cette méthode n'utilise pas d'authentification — les serveurs de messagerie (Gmail, Outlook) considèrent ces emails comme suspects et les bloquent ou les mettent en spam.

**[ÉCRAN — screencast WordPress admin]**

[Navigation vers Extensions > Ajouter]

La solution : utiliser un plugin SMTP qui authentifie les emails. La recommandation schoolsWP : FluentSMTP. C'est gratuit, léger, et développé par la même équipe que FluentCRM.

Installe et active FluentSMTP.

**[ÉCRAN — screencast FluentSMTP]**

[Navigation vers Réglages > FluentSMTP]

FluentSMTP te propose plusieurs services : Amazon SES, SendGrid, Mailgun, Gmail API, SMTP générique, et d'autres. Le choix dépend de ton volume :

- Moins de 300 emails par jour : Gmail API ou le SMTP de ton hébergeur
- 300 à 10 000 emails par jour : SendGrid (gratuit jusqu'à 100/jour) ou Amazon SES
- Plus de 10 000 : Amazon SES (le moins cher)

Pour cette démo, on configure avec le SMTP de base — ça fonctionne avec n'importe quel hébergeur.

**[ÉCRAN — screencast FluentSMTP configuration]**

[Montre la configuration SMTP pas à pas]

Clique sur "Add Another Connection", puis sélectionne "Other SMTP". Remplis :

- Sender Email : ton email professionnel (ex: contact@ton-site.fr)
- Sender Name : le nom qui apparaîtra (ex: le nom de ta formation)
- SMTP Host : celui de ton hébergeur (ex: mail.ton-site.fr ou smtp.gmail.com)
- Port : 587 (TLS) ou 465 (SSL) — 587 est le standard
- Username : ton adresse email complète
- Password : le mot de passe ou le mot de passe d'application

Sauvegarde la connexion.

**[ÉCRAN — screencast FluentSMTP test]**

[Montre l'envoi d'un email de test]

Maintenant, teste. FluentSMTP a un bouton "Send Test Email". Entre ton adresse personnelle et envoie. Vérifie que l'email arrive dans ta boîte — pas dans les spams.

Si le test échoue, vérifie :
- Le host et le port (demande à ton hébergeur si tu doutes)
- Le mot de passe (pour Gmail, il faut un "mot de passe d'application", pas ton mot de passe habituel)
- Que le port 587 n'est pas bloqué par ton hébergeur

**[ÉCRAN — screencast FluentSMTP logs]**

[Montre l'onglet Email Logs]

FluentSMTP a un onglet "Email Logs" qui enregistre tous les emails envoyés. Tu vois le statut de chaque email : envoyé, échoué, en attente. Si un email échoue, le log te donne le message d'erreur exact.

Active les logs — c'est indispensable pour diagnostiquer les problèmes d'email.

**[ÉCRAN — screencast Tutor LMS Settings]**

[Navigation vers Tutor LMS > Settings > Email]

Dernier point : vérifie que les notifications email sont activées dans TutorLMS. Va dans Tutor LMS, Settings, Email. Tu vois la liste de toutes les notifications : inscription, complétion de cours, nouveau quiz, etc. Active celles que tu veux envoyer et personnalise les templates si nécessaire.

**[TRANSITION — face caméra]**

La recommandation schoolsWP est claire : installe FluentSMTP dès le jour un. Même avant de créer ton premier cours. Sans SMTP authentifié, tes emails finiront en spam — c'est une certitude, pas un risque. Et active les logs pour pouvoir diagnostiquer les problèmes rapidement.

---

**Points clés** :
- WordPress envoie des emails non authentifiés par défaut — d'où le spam
- Solution : FluentSMTP (gratuit) pour authentifier les envois
- Configuration : host, port 587, identifiants email
- Tester avec le bouton "Send Test Email" avant de mettre en production
- Activer les Email Logs pour diagnostiquer les échecs
- Vérifier les notifications activées dans Tutor LMS > Settings > Email

**Mots clés SEO** : TutorLMS email non reçu, emails spam WordPress, FluentSMTP TutorLMS, notification email LMS WordPress

---

### Leçon 15.6 — Compatibilité Yoast/RankMath

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress admin
**Source** : Création originale schoolsWP

---

**[INTRO — face caméra]**

TutorLMS crée des pages de cours, de leçons, de quiz — et ton plugin SEO doit les gérer correctement. Que tu utilises RankMath ou Yoast, il y a des conflits potentiels : balises meta en double, sitemaps incomplets, ou schéma markup qui se contredit. Dans cette leçon, on configure la cohabitation proprement.

**[ÉCRAN — screencast WordPress admin]**

[Montre un cours TutorLMS avec RankMath ou Yoast actif]

Le symptôme : tu installes RankMath ou Yoast, et tu remarques des problèmes sur tes pages de cours :

- Deux balises title différentes dans le code source
- Les cours n'apparaissent pas dans le sitemap
- Le schéma markup "Course" de TutorLMS entre en conflit avec le schéma de ton plugin SEO
- Les meta descriptions sont vides ou dupliquées

**[ÉCRAN — screencast WordPress admin — RankMath]**

[Navigation vers RankMath > Titles & Meta > Custom Post Types]

Commençons par RankMath — c'est la recommandation schoolsWP. Va dans RankMath, Titles & Meta, puis cherche la section pour les types de contenu personnalisés. Tu dois voir "Courses", "Lessons", "Quizzes".

Pour les cours : active l'indexation et configure le template de titre et de meta description. Utilise les variables dynamiques de RankMath :

- Titre : `%title% - %sitename%`
- Meta description : `%excerpt%` ou écris un template personnalisé

Pour les leçons et les quiz : désactive l'indexation. Les leçons ne doivent pas être indexées individuellement — elles font partie d'un cours. Si tu les indexes, tu crées du contenu dupliqué et tu dilues l'autorité de tes pages de cours.

**[ÉCRAN — screencast RankMath Sitemap]**

[Navigation vers RankMath > Sitemap Settings]

Deuxième étape : le sitemap. Va dans RankMath, Sitemap Settings. Vérifie que "Courses" est inclus dans le sitemap. Exclue "Lessons" et "Quizzes" du sitemap — cohérent avec le choix de ne pas les indexer.

**[ÉCRAN — screencast RankMath Schema]**

[Navigation vers RankMath > Schema sur une page de cours]

Troisième étape : le schéma markup. TutorLMS génère automatiquement un schéma "Course" sur les pages de cours. RankMath génère aussi un schéma. Résultat : deux schémas "Course" sur la même page — Google n'aime pas ça.

La solution : dans RankMath, sur les pages de type "Course", désactive le schéma automatique de RankMath ou configure-le pour utiliser le type "Article" au lieu de "Course". Laisse TutorLMS gérer le schéma "Course" — il contient les données structurées les plus complètes (prix, durée, nombre d'élèves, note moyenne).

**[ÉCRAN — screencast WordPress admin — Yoast]**

[Navigation vers Yoast SEO > Search Appearance > Content Types]

Si tu utilises Yoast : même logique. Va dans Yoast SEO, Search Appearance, Content Types. Pour "Courses" : active l'affichage dans les résultats de recherche. Pour "Lessons" et "Quizzes" : désactive.

Pour le schéma : Yoast ajoute automatiquement un schéma sur toutes les pages. Pour éviter le doublon avec TutorLMS, tu peux utiliser le filtre `wpseo_schema_graph` dans un snippet PHP pour retirer le schéma "Course" de Yoast sur les pages de cours TutorLMS. Ou plus simplement : dans les réglages schéma de Yoast pour le type "Course", sélectionne "Web Page" au lieu de "Course".

**[ÉCRAN — screencast code source page]**

[Montre la vérification du code source avec Ctrl+U]

Pour vérifier que tout est propre : ouvre une page de cours, fais Ctrl+U pour voir le code source. Cherche "schema" ou "ld+json". Tu dois voir un seul bloc schéma de type "Course" — celui de TutorLMS. Si tu en vois deux, il reste un conflit à corriger.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : utilise RankMath. L'intégration avec TutorLMS est plus propre qu'avec Yoast. Indexe les cours, pas les leçons ni les quiz. Et laisse TutorLMS gérer le schéma "Course" — c'est lui qui a les données les plus complètes. Avec cette configuration, tes pages de cours sont optimisées pour Google sans conflit.

---

**Points clés** :
- Indexer les cours, ne PAS indexer les leçons ni les quiz (contenu dupliqué)
- Sitemap : inclure les cours, exclure leçons et quiz
- Schéma : laisser TutorLMS gérer le schéma "Course", configurer RankMath/Yoast sur "Article" ou "Web Page"
- Vérification : Ctrl+U sur une page de cours, chercher "ld+json" — un seul bloc "Course"
- Recommandation schoolsWP : RankMath plutôt que Yoast pour TutorLMS

**Mots clés SEO** : TutorLMS RankMath, TutorLMS Yoast SEO, schéma cours WordPress, SEO formation en ligne WordPress, TutorLMS sitemap

---

### Leçon 15.7 — Quiz Module 15

**Durée** : ~4 min (8 questions)
**Type** : Quiz TutorLMS
**Seuil de réussite** : 70%

---

**Question 1**
Quel est le premier réflexe à avoir quand quelque chose ne fonctionne pas sur TutorLMS ?

- A) Réinstaller le plugin
- B) Contacter le support Themeum
- C) Consulter la page Tutor LMS > Status pour vérifier le rapport système ✓
- D) Désactiver tous les plugins

**Explication** : La page Status donne un rapport complet (version PHP, mémoire, conflits). C'est toujours le point de départ du diagnostic.

---

**Question 2**
Quelle est la solution la plus fréquente pour une erreur 404 sur un cours TutorLMS ?

- A) Réinstaller TutorLMS
- B) Changer de thème
- C) Re-sauvegarder les permaliens dans Réglages > Permaliens ✓
- D) Vider le cache du navigateur

**Explication** : Dans 90% des cas, re-sauvegarder les permaliens force WordPress à régénérer les règles de réécriture d'URL et corrige les 404.

---

**Question 3**
Une commande reste en "Pending" alors que l'élève a payé via Stripe. Que faut-il vérifier en priorité ?

- A) Que l'élève a bien un compte WordPress
- B) Que le paiement apparaît comme "Succeeded" dans le tableau de bord Stripe ✓
- C) Que le cours est bien publié
- D) Que le thème est compatible

**Explication** : Si le paiement est reçu chez Stripe mais que la commande est en "Pending" dans TutorLMS, c'est un problème de webhook — le paiement a été effectué mais la notification n'est pas passée.

---

**Question 4**
Quelles sont les conditions pour qu'un certificat se débloque pour un élève ?

- A) L'élève doit avoir visionné au moins 80% des leçons
- B) L'élève doit avoir complété 100% du cours (leçons + quiz) ET un template de certificat doit être attribué au cours ✓
- C) L'élève doit en faire la demande manuelle
- D) Le certificat se débloque automatiquement après 30 jours

**Explication** : Le certificat nécessite 100% de complétion (toutes les leçons + tous les quiz au score minimum) et un template de certificat sélectionné dans les paramètres du cours.

---

**Question 5**
Pourquoi les emails WordPress finissent-ils souvent en spam ?

- A) Parce que WordPress envoie trop d'emails
- B) Parce que la fonction wp_mail() par défaut n'utilise pas d'authentification SMTP ✓
- C) Parce que Gmail bloque tous les emails WordPress
- D) Parce que TutorLMS n'envoie pas les bons headers

**Explication** : Par défaut, WordPress utilise wp_mail() sans authentification. Les serveurs de messagerie traitent ces emails comme suspects. Un plugin SMTP (FluentSMTP) résout le problème.

---

**Question 6**
Quel plugin SMTP gratuit schoolsWP recommande-t-il ?

- A) WP Mail SMTP
- B) Post SMTP
- C) FluentSMTP ✓
- D) Easy WP SMTP

**Explication** : FluentSMTP est gratuit, léger, et développé par la même équipe que FluentCRM. Il offre des logs d'emails intégrés pour diagnostiquer les problèmes.

---

**Question 7**
Faut-il indexer les leçons TutorLMS individuellement dans Google ?

- A) Oui, chaque leçon doit être indexée pour maximiser le trafic
- B) Non — les leçons ne doivent pas être indexées individuellement pour éviter le contenu dupliqué ✓
- C) Seulement les leçons gratuites
- D) Seulement si on utilise RankMath

**Explication** : Les leçons font partie d'un cours. Les indexer individuellement crée du contenu dupliqué et dilue l'autorité des pages de cours. Seuls les cours doivent être indexés.

---

**Question 8**
Comment éviter un doublon de schéma markup "Course" entre TutorLMS et RankMath ?

- A) Désactiver le schéma dans TutorLMS
- B) Configurer RankMath sur le type "Article" ou "Web Page" pour les cours, et laisser TutorLMS gérer le schéma "Course" ✓
- C) Désinstaller RankMath sur les pages de cours
- D) Utiliser un plugin tiers pour fusionner les schémas

**Explication** : TutorLMS génère un schéma "Course" avec les données les plus complètes (prix, durée, note). Il faut configurer RankMath pour ne pas générer un second schéma "Course" sur ces pages.

---

**Fin du Module 15 — Troubleshooting**

Résumé du module :
- Diagnostic général : page Status, test de conflit plugins, test de thème, console navigateur
- Erreur 404 : re-sauvegarder les permaliens (solution dans 90% des cas)
- Commandes bloquées : vérifier passerelle de paiement, mode Live, produits "Virtual"
- Certificats : addon actif + template attribué + complétion 100%
- Emails : FluentSMTP obligatoire dès le jour un + logs actifs
- SEO : indexer les cours uniquement, schéma "Course" géré par TutorLMS

Durée totale estimée du module : ~30 minutes

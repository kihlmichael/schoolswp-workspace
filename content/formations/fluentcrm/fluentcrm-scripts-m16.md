# Scripts vidéo — Module 16 : Délivrabilité et performance

**Formation** : Maîtriser FluentCRM
**Module** : M16 — Délivrabilité et performance (Premium)
**Leçons** : 7 vidéos + 1 quiz final
**Durée totale** : ~45 min
**Prérequis** : M15 (rapports), M6 (automations), toute la formation
**Date** : 2026-03-23

---

### Leçon 16.1 — Comprends la délivrabilité : pourquoi tes emails arrivent (ou pas) en inbox

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast + slides

---

**[INTRO — face caméra]**

Tu as configuré FluentCRM, créé tes automations, segmenté tes contacts. Mais si tes emails arrivent en spam, tout ça ne sert à rien. La délivrabilité, c'est la capacité de tes emails à atteindre la boîte de réception de tes destinataires. Et c'est un sujet que la plupart des formateurs WordPress ignorent jusqu'au jour où leur taux d'ouverture chute sans explication. Dans cette leçon, tu comprends les mécanismes et les facteurs qui déterminent si ton email arrive en inbox ou en spam.

**[ÉCRAN — slide "Le parcours d'un email"]**

[Schéma : ton serveur → serveur SMTP → filtres anti-spam → inbox OU spam OU rejet]

Étape 1 : quand tu envoies un email depuis FluentCRM, voici ce qui se passe. FluentCRM passe le message à ton serveur SMTP — que ce soit le SMTP de ton hébergeur, Amazon SES, SendGrid, Mailgun ou Postmark. Le SMTP envoie au serveur du destinataire. Ce serveur vérifie plusieurs choses avant d'accepter le message.

**[ÉCRAN — slide "Les 5 facteurs de délivrabilité"]**

[Liste numérotée des 5 facteurs]

Étape 2 : les cinq facteurs principaux. Un — l'authentification (SPF, DKIM, DMARC). Le serveur destinataire vérifie que tu es bien autorisé à envoyer depuis ton domaine. Deux — la réputation de l'IP d'envoi. Si ton IP est sur des listes noires ou a un historique de spam, tes emails sont rejetés. Trois — le contenu de l'email. Certains mots, formats ou ratios image/texte déclenchent les filtres anti-spam. Quatre — l'engagement des destinataires. Si beaucoup de tes destinataires n'ouvrent jamais tes emails, les fournisseurs comme Gmail en déduisent que tu envoies du contenu non désiré. Cinq — les aspects techniques : bounce rate, plaintes spam, fréquence d'envoi.

**[ÉCRAN — slide "Hébergement mutualisé vs VPS"]**

[Tableau comparatif]

Étape 3 : ton type d'hébergement impacte directement ta délivrabilité. En mutualisé, tu partages une IP avec d'autres sites. Si un voisin envoie du spam, ta réputation en souffre — tu n'y peux rien. En VPS ou dédié, tu as ta propre IP. Ta réputation ne dépend que de toi.

C'est pourquoi la recommandation schoolsWP est claire : pour l'envoi d'emails marketing, utilise un service SMTP dédié — Amazon SES, SendGrid, Mailgun ou Postmark. Ne te repose pas sur le SMTP de ton hébergeur mutualisé. Même sur un VPS, un service SMTP dédié offre de meilleurs outils de monitoring et une meilleure délivrabilité.

**[ÉCRAN — slide "Les signaux d'alerte"]**

[Liste de 4 signaux]

Étape 4 : comment savoir si tu as un problème de délivrabilité ? Quatre signaux. Taux d'ouverture en baisse progressive — tes emails atterrissent de plus en plus en spam. Taux de bounce supérieur à 2% — des adresses invalides polluent ta base. Plaintes spam en hausse — des destinataires cliquent "signaler comme spam". Emails qui arrivent en spam quand tu testes avec ta propre adresse Gmail.

**[TRANSITION — face caméra]**

La délivrabilité n'est pas un réglage unique. C'est un ensemble de bonnes pratiques techniques et comportementales. Dans les prochaines leçons, on s'attaque à chaque facteur : authentification DNS, bounce handlers, cron et multi-threading. On commence par le plus critique : SPF, DKIM et DMARC.

---

**Points clés** :
- Délivrabilité = capacité à atteindre l'inbox (pas juste "envoyer")
- 5 facteurs : authentification DNS, réputation IP, contenu, engagement, technique
- Mutualisé : IP partagée = réputation partagée — risque de délivrabilité
- Recommandation : SMTP dédié (Amazon SES, SendGrid, Mailgun, Postmark)
- Signaux d'alerte : ouverture en baisse, bounce > 2%, plaintes spam, test inbox négatif

**Mots clés SEO** : délivrabilité email WordPress, FluentCRM délivrabilité, emails en spam WordPress, SMTP WordPress

---

### Leçon 16.2 — Configure SPF, DKIM et DMARC pour ton domaine

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast DNS + outils de vérification

---

**[INTRO — face caméra]**

SPF, DKIM, DMARC — trois acronymes qui font fuir. Pourtant, ce sont les trois piliers de l'authentification email. Sans eux, les serveurs destinataires ne peuvent pas vérifier que tes emails viennent bien de toi. Et en 2024, Google et Yahoo les exigent explicitement. Un email non authentifié a une forte probabilité d'atterrir en spam ou d'être rejeté. Dans cette leçon, tu configures les trois — pas besoin d'être admin système.

**[ÉCRAN — slide "SPF, DKIM, DMARC — c'est quoi ?"]**

[Schéma simplifié des 3 mécanismes]

Étape 1 : comprends ce que fait chaque mécanisme. SPF (Sender Policy Framework) — un enregistrement DNS qui dit : "Voici les serveurs autorisés à envoyer des emails pour mon domaine." DKIM (DomainKeys Identified Mail) — une signature cryptographique ajoutée à chaque email, prouvant que le contenu n'a pas été modifié. DMARC (Domain-based Message Authentication) — une politique qui dit aux serveurs destinataires quoi faire si SPF ou DKIM échouent : rien, mettre en quarantaine, ou rejeter.

**[ÉCRAN — screencast panel DNS de l'hébergeur]**

[Ouvre le panel DNS — ex: Cloudflare, OVH ou le panel de WP1]

Étape 2 : configure le SPF. Va dans la zone DNS de ton domaine. Ajoute un enregistrement TXT. Le contenu dépend de ton service SMTP.

Pour Amazon SES : `v=spf1 include:amazonses.com ~all`
Pour SendGrid : `v=spf1 include:sendgrid.net ~all`
Pour Mailgun : `v=spf1 include:mailgun.org ~all`
Pour Postmark : `v=spf1 include:spf.mtasv.net ~all`

Si tu as déjà un enregistrement SPF (tu en as peut-être un pour ton hébergeur), ne crée pas un deuxième — ajoute le `include:` au SPF existant. Un domaine ne doit avoir qu'un seul enregistrement SPF.

[Montre l'ajout dans le panel DNS]

**[ÉCRAN — screencast configuration DKIM]**

[Montre l'interface du service SMTP]

Étape 3 : configure le DKIM. Dans le dashboard de ton service SMTP (SES, SendGrid, etc.), cherche la section "Domain Authentication" ou "DKIM". Le service te donne des enregistrements DNS à ajouter — généralement des enregistrements CNAME. Copie-les et ajoute-les dans ta zone DNS.

[Montre les enregistrements CNAME à copier]

Étape 4 : ajoute les enregistrements DKIM dans ton panel DNS. Ce sont des CNAME, pas des TXT. Chaque service en demande entre 1 et 3. Copie les valeurs exactement — une faute de frappe et le DKIM échoue.

**[ÉCRAN — screencast configuration DMARC]**

[Retour dans le panel DNS]

Étape 5 : configure le DMARC. Ajoute un enregistrement TXT avec le nom `_dmarc.tondomaine.com`. Pour commencer, utilise une politique de monitoring :

`v=DMARC1; p=none; rua=mailto:dmarc@tondomaine.com`

Ça ne bloque rien — ça envoie des rapports à ton adresse email pour que tu voies qui envoie des emails en ton nom. Après quelques semaines de monitoring, passe à `p=quarantine` puis `p=reject` quand tu es confiant.

**[ÉCRAN — screencast vérification avec MXToolbox]**

[Ouvre mxtoolbox.com/supertool]

Étape 6 : vérifie ta configuration. Va sur mxtoolbox.com et utilise le SuperTool. Tape ton domaine et vérifie le SPF, le DKIM et le DMARC. Tout doit être en vert. Si un élément est en rouge, reviens dans ta zone DNS et corrige.

[Montre les résultats de vérification — SPF pass, DKIM pass, DMARC pass]

Étape 7 : envoie un email de test à une adresse Gmail. Ouvre le message, clique sur les trois points, "Afficher l'original". Tu verras les en-têtes SPF, DKIM et DMARC avec le statut PASS ou FAIL. Les trois doivent être PASS.

**[TRANSITION — face caméra]**

SPF, DKIM, DMARC — c'est fait. La propagation DNS peut prendre jusqu'à 48 heures, mais c'est souvent plus rapide. Vérifie le lendemain. C'est une configuration à faire une fois — ensuite tu n'y touches plus sauf si tu changes de service SMTP. Prochaine leçon : les bounce handlers, pour gérer les emails qui reviennent en erreur.

---

**Points clés** :
- SPF : enregistrement TXT listant les serveurs autorisés à envoyer pour ton domaine
- DKIM : signature cryptographique — enregistrements CNAME fournis par ton service SMTP
- DMARC : politique de traitement si SPF/DKIM échouent — commencer par p=none (monitoring)
- Un seul enregistrement SPF par domaine — combiner les includes si nécessaire
- Vérifier avec MXToolbox + test email Gmail (Afficher l'original)
- Propagation DNS : jusqu'à 48h

**Mots clés SEO** : SPF DKIM DMARC WordPress, authentification email WordPress, configurer SPF FluentCRM, délivrabilité DNS email

---

### Leçon 16.3 — Configure les bounce handlers

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Un bounce, c'est un email qui revient. Soit parce que l'adresse n'existe pas (hard bounce), soit parce que la boîte est pleine ou le serveur temporairement indisponible (soft bounce). Si tu ne gères pas les bounces, tu continues à envoyer à des adresses mortes, ta réputation d'envoi se dégrade, et tes emails finissent en spam. FluentCRM gère les bounces automatiquement — mais tu dois connecter un bounce handler. C'est ce qu'on fait maintenant.

**[ÉCRAN — screencast FluentCRM > Settings > Bounce Handler]**

[Navigation vers les réglages bounce]

Étape 1 : va dans FluentCRM > Settings > Bounce Handler Settings. FluentCRM supporte quatre services : Amazon SES, SendGrid, Mailgun et Postmark. Chaque service a son propre mécanisme de notification de bounce — FluentCRM s'y connecte via webhook.

[Montre la liste des services supportés]

**[ÉCRAN — screencast configuration bounce Amazon SES]**

[Montre la configuration pour SES comme exemple principal]

Étape 2 : prenons Amazon SES comme exemple — c'est le service le plus utilisé pour les gros volumes. Le principe : SES envoie une notification SNS (Simple Notification Service) à FluentCRM quand un email bounce. FluentCRM reçoit la notification et met à jour le contact automatiquement.

Étape 3 : dans le dashboard AWS, va dans SES > Configuration Sets. Crée un configuration set si tu n'en as pas. Ajoute une destination de type SNS Topic pour les événements Bounce et Complaint. Crée le SNS Topic si nécessaire.

Étape 4 : dans le SNS Topic, ajoute un subscriber de type HTTPS. L'URL est fournie par FluentCRM dans les réglages Bounce Handler — copie-la exactement. Confirme l'abonnement. AWS envoie une requête de confirmation à FluentCRM, qui la valide automatiquement.

**[ÉCRAN — screencast configuration bounce SendGrid/Mailgun/Postmark]**

[Montre rapidement les 3 autres services]

Étape 5 : pour les autres services, le principe est le même. SendGrid : va dans Settings > Mail Settings > Event Webhook, ajoute l'URL FluentCRM, active les événements Bounce et Spam Report. Mailgun : va dans Sending > Webhooks, ajoute l'URL pour les événements Bounced et Complained. Postmark : va dans Servers > Webhooks, ajoute l'URL pour Bounce et Spam Complaint.

**[ÉCRAN — screencast vérification du bounce handler]**

[Montre un test de bounce]

Étape 6 : teste le bounce handler. La plupart des services SMTP proposent une adresse de test bounce. Pour SES, envoie un email à `bounce@simulator.amazonses.com`. Attends quelques minutes, puis vérifie dans FluentCRM > Contacts que l'adresse est marquée comme bounced. Si le statut change, le handler fonctionne.

Étape 7 : FluentCRM gère les bounces ainsi. Hard bounce : le contact est automatiquement marqué comme "bounced" et retiré des envois futurs. Soft bounce : FluentCRM réessaie. Après plusieurs soft bounces consécutifs (généralement 3), le contact passe en hard bounce. Complaint (signalement spam) : le contact est automatiquement désabonné.

**[TRANSITION — face caméra]**

Le bounce handler est configuré. Tes emails qui reviennent sont maintenant traités automatiquement. Ta base reste propre sans intervention manuelle. Prochaine leçon : on remplace WP-Cron par un vrai cron job — parce que WP-Cron n'est pas fiable pour l'envoi d'emails.

---

**Points clés** :
- Hard bounce = adresse invalide → contact retiré des envois
- Soft bounce = problème temporaire → FluentCRM réessaie puis hard bounce après ~3 échecs
- Complaint = signalement spam → désabonnement automatique
- 4 services supportés : Amazon SES, SendGrid, Mailgun, Postmark
- Configuration via webhook : URL fournie par FluentCRM à coller dans le service SMTP
- Tester avec les adresses simulateur du service SMTP

**Mots clés SEO** : FluentCRM bounce handler, gérer bounces email WordPress, Amazon SES bounce FluentCRM, SendGrid webhook FluentCRM

---

### Leçon 16.4 — Remplace WP-Cron par un vrai cron job

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress + panel hébergeur

---

**[INTRO — face caméra]**

WP-Cron n'est pas un vrai cron. C'est un faux cron qui se déclenche uniquement quand quelqu'un visite ton site. Si personne ne visite pendant 2 heures, tes tâches planifiées attendent — y compris l'envoi de tes emails FluentCRM. Sur un site à faible trafic, ça signifie que tes emails partent en retard ou par paquets irréguliers. La solution : désactiver WP-Cron et le remplacer par un vrai cron système.

**[ÉCRAN — screencast wp-config.php]**

[Ouvre le fichier wp-config.php]

Étape 1 : désactive WP-Cron. Ouvre `wp-config.php` (via le gestionnaire de fichiers de ton hébergeur ou en FTP). Ajoute cette ligne avant le commentaire "That's all, stop editing!" :

```php
define('DISABLE_WP_CRON', true);
```

Ça empêche WordPress de déclencher le cron à chaque visite. Les tâches planifiées ne s'exécutent plus automatiquement — c'est normal, on va les déclencher autrement.

**[ÉCRAN — screencast panel hébergeur — cron jobs]**

[Ouvre cPanel ou le panel spécifique — ex: WP1]

Étape 2 : configure un vrai cron job. Va dans le panel de ton hébergeur, section "Cron Jobs" ou "Tâches planifiées". Sur WP1, tu trouveras ça dans les outils avancés.

Étape 3 : crée une tâche cron. La commande à exécuter :

```bash
wget -q -O /dev/null https://tonsite.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

Ou avec curl :

```bash
curl -s https://tonsite.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

La fréquence recommandée : toutes les minutes (`* * * * *`) pour les envois email. Si tu n'envoies pas d'emails en volume, toutes les 5 minutes suffit (`*/5 * * * *`).

[Montre la création du cron job dans le panel]

**[ÉCRAN — screencast vérification]**

[Montre les tests de vérification]

Étape 4 : vérifie que le cron fonctionne. Installe le plugin "WP Crontrol" temporairement — il affiche toutes les tâches planifiées et leur dernière exécution. Tu devrais voir les tâches FluentCRM s'exécuter régulièrement. Les événements doivent montrer une heure d'exécution récente (moins de 5 minutes si ton cron tourne toutes les minutes).

Étape 5 : test concret. Planifie l'envoi d'une campagne FluentCRM pour dans 2 minutes. Attends. L'email doit partir à l'heure prévue, sans que tu visites le site. Si l'email part à l'heure : le cron fonctionne. Si l'email ne part pas : reviens dans le panel hébergeur et vérifie la commande et la fréquence.

**[ÉCRAN — slide "Mutualisé vs VPS — config cron"]**

[Montre les différences de configuration]

Étape 6 : une note sur les hébergeurs mutualisés. Certains limitent la fréquence minimale du cron à 5 ou 15 minutes. C'est une limitation du mutualisé. En VPS, tu as le contrôle total — toutes les minutes sans restriction. Sur WP1, le cron toutes les minutes est disponible dans les offres standard.

**[TRANSITION — face caméra]**

Le vrai cron est en place. Tes emails partent à l'heure, que ton site ait du trafic ou non. C'est un changement invisible pour tes abonnés mais fondamental pour la fiabilité de tes envois. Prochaine leçon : le multi-threading pour les gros volumes.

---

**Points clés** :
- WP-Cron = faux cron déclenché par les visites — non fiable pour les emails
- Desactiver avec `define('DISABLE_WP_CRON', true);` dans wp-config.php
- Vrai cron : wget ou curl vers wp-cron.php, toutes les minutes idéalement
- Vérifier avec WP Crontrol (plugin temporaire)
- Mutualisé : fréquence parfois limitée à 5-15 min — VPS : toutes les minutes sans restriction
- Sur WP1 : cron toutes les minutes disponible

**Mots clés SEO** : WP-Cron désactiver, vrai cron WordPress, cron job FluentCRM, remplacer WP-Cron, cron WordPress WP1

---

### Leçon 16.5 — Active le multi-threading pour les gros volumes

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Par défaut, FluentCRM envoie les emails un par un. Pour 100 contacts, ça va. Pour 5 000, ça prend des heures. Le multi-threading permet à FluentCRM d'envoyer plusieurs emails en parallèle — mais le réglage dépend de ton hébergement. Trop agressif, tu satures ton serveur ou tu te fais bloquer par ton SMTP. Pas assez, tes campagnes traînent. Dans cette leçon, tu trouves le bon réglage pour ta configuration.

**[ÉCRAN — screencast FluentCRM > Settings > Email Settings]**

[Navigation vers les réglages email]

Étape 1 : va dans FluentCRM > Settings > Email Settings. Cherche la section "Email Sending" ou "Email Engine". Tu trouves deux paramètres clés : le nombre d'emails par lot (batch size) et le délai entre les lots.

[Montre les champs de configuration]

Étape 2 : le batch size détermine combien d'emails FluentCRM envoie à chaque exécution du cron. Le délai entre les lots évite de surcharger le serveur.

**[ÉCRAN — slide "Réglages recommandés par type d'hébergement"]**

[Tableau avec 3 profils]

Étape 3 : les réglages recommandés.

Hébergement mutualisé : 50 emails par minute maximum. Batch size de 50, cron toutes les minutes. C'est conservateur mais ça évite les blocages. Ton hébergeur mutualisé a des limites — les dépasser entraîne un blocage temporaire ou un signalement.

VPS standard (2-4 Go RAM) : 200 à 300 emails par minute. Batch size de 100, cron toutes les 30 secondes ou toutes les minutes. Ton VPS tient la charge mais ton service SMTP a peut-être ses propres limites.

VPS performant + SMTP dédié (SES/SendGrid) : 300 à 500 emails par minute. Batch size de 200, cron toutes les 30 secondes. C'est le maximum recommandé avant d'avoir besoin d'une infrastructure email dédiée.

**[ÉCRAN — screencast configuration multi-threading]**

[Montre le réglage dans FluentCRM]

Étape 4 : configure ton batch size en fonction de ton profil. Commence conservateur et augmente progressivement. Si tu es sur un mutualisé, reste à 50. La tentation d'augmenter est forte — résiste. Mieux vaut une campagne qui prend 2 heures qu'un serveur bloqué.

Étape 5 : vérifie aussi les limites de ton service SMTP. Amazon SES : la limite de départ est de 1 email par seconde (200 par jour pour un nouveau compte). SendGrid : dépend de ton plan. Mailgun : 300 par minute sur le plan gratuit. Le goulot d'étranglement est souvent le service SMTP, pas FluentCRM.

**[ÉCRAN — screencast test d'envoi en volume]**

[Montre l'envoi d'une campagne test à un petit groupe]

Étape 6 : teste avant d'envoyer à toute ta base. Crée une campagne test pour 50 contacts. Vérifie que les emails partent sans erreur dans le log FluentCRM. Augmente à 200. Puis 500. Si tu vois des erreurs "timeout" ou "connection refused", réduis le batch size.

**[TRANSITION — face caméra]**

Le multi-threading est configuré. La règle d'or : commence petit et augmente. Mieux vaut un envoi lent qu'un envoi bloqué. Prochaine leçon : les réglages avancés de FluentCRM — quick nav, archives de campagnes et system log.

---

**Points clés** :
- Multi-threading = envoi d'emails en parallèle (batch size + délai entre lots)
- Mutualisé : 50 emails/min max — conservateur mais stable
- VPS standard : 200-300 emails/min
- VPS + SMTP dédié : 300-500 emails/min
- Le goulot est souvent le service SMTP (limites SES, SendGrid, Mailgun)
- Toujours tester progressivement : 50 → 200 → 500

**Mots clés SEO** : FluentCRM multi-threading, envoi masse FluentCRM, batch size FluentCRM, vitesse envoi email WordPress

---

### Leçon 16.6 — Réglages avancés : quick nav, campaign archives, system log

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

FluentCRM a des réglages avancés que la plupart des utilisateurs ne découvrent jamais. Quick navigation pour accéder plus vite aux contacts. Archives de campagnes pour publier tes newsletters en pages web. System log pour diagnostiquer les problèmes. Dans cette leçon, tu actives et configures ces trois fonctionnalités.

**[ÉCRAN — screencast FluentCRM > Settings > General > Quick Navigation]**

[Navigation vers les réglages généraux]

Étape 1 : la quick navigation. Va dans Settings > General. Cherche "Quick Navigation" ou "Admin Bar". Active l'option. Ça ajoute un raccourci FluentCRM dans la barre d'administration WordPress — tu peux accéder aux contacts, campagnes et automations depuis n'importe quelle page de ton back-office.

[Montre le raccourci dans la barre admin]

Étape 2 : la quick nav affiche aussi les dernières activités — derniers contacts ajoutés, dernière campagne envoyée. Pratique pour un coup d'œil rapide sans ouvrir FluentCRM.

**[ÉCRAN — screencast FluentCRM > Settings > Campaign Archives]**

[Montre les réglages d'archives]

Étape 3 : les archives de campagnes. FluentCRM peut générer une page web publique pour chaque campagne envoyée — comme un archive de newsletter. Va dans Settings, cherche "Campaign Archive" ou "Public Archives".

Étape 4 : active l'option. FluentCRM crée un slug URL pour chaque campagne archivée. Tes abonnés peuvent consulter les anciennes newsletters sur ton site. C'est utile pour deux choses : le SEO (les newsletters deviennent du contenu indexable) et la transparence (les nouveaux abonnés voient ce qu'ils vont recevoir).

[Montre une page d'archive publique]

Étape 5 : attention — n'archive pas toutes tes campagnes. Les emails de relance, les séquences de vente, les emails transactionnels n'ont pas vocation à être publics. Archive uniquement les newsletters et les campagnes de contenu.

**[ÉCRAN — screencast FluentCRM > Settings > System Log]**

[Navigation vers le system log]

Étape 6 : le system log. Va dans Settings > Log ou Tools > System Log. C'est le journal technique de FluentCRM. Tu y trouves les erreurs d'envoi, les problèmes de cron, les conflits de plugins.

[Montre des exemples d'entrées de log]

Étape 7 : les entrées à surveiller. Les erreurs d'envoi SMTP — elles indiquent un problème avec ton service d'envoi. Les timeouts de cron — ton cron ne tourne pas ou est trop lent. Les erreurs d'intégration — un plugin connecté qui ne répond plus.

Étape 8 : le system log est ton premier réflexe quand quelque chose ne fonctionne pas. Avant de contacter le support FluentCRM, vérifie le log. Dans 80% des cas, l'erreur est documentée ici. Copie le message d'erreur exact — ça accélère le diagnostic.

**[TRANSITION — face caméra]**

Trois réglages qui améliorent ton quotidien : la quick nav pour aller plus vite, les archives pour valoriser tes newsletters, et le system log pour diagnostiquer. Prochaine leçon : la REST API pour les développeurs — et les possibilités avec n8n.

---

**Points clés** :
- Quick Navigation : raccourci FluentCRM dans la barre admin WordPress
- Campaign Archives : newsletters accessibles en pages web publiques (SEO + transparence)
- N'archiver que les newsletters/contenus — pas les emails de vente ou transactionnels
- System Log : journal technique — erreurs SMTP, cron, intégrations
- Le log est le premier réflexe avant de contacter le support

**Mots clés SEO** : FluentCRM réglages avancés, FluentCRM campaign archive, system log FluentCRM, FluentCRM admin settings

---

### Leçon 16.7 — REST API : les bases pour développer dessus

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast API + n8n

---

**[INTRO — face caméra]**

FluentCRM expose une REST API. Ça signifie que tu peux lire et écrire des données FluentCRM depuis n'importe quel outil externe — n8n, Zapier, un script Python, ou une application custom. Dans cette leçon, tu découvres les endpoints principaux et tu fais un premier appel API. On reste sur les bases — l'objectif est que tu comprennes ce qui est possible, pas que tu deviennes développeur.

**[ÉCRAN — slide "REST API — c'est quoi ?"]**

[Schéma : outil externe → requête HTTP → FluentCRM → réponse JSON]

Étape 1 : la REST API de FluentCRM permet à des outils externes de communiquer avec FluentCRM via des requêtes HTTP. Tu envoies une requête (par exemple "donne-moi la liste des contacts tagués premium"), FluentCRM répond en JSON (le format de données standard du web).

**[ÉCRAN — screencast documentation API FluentCRM]**

[Ouvre la documentation REST API FluentCRM]

Étape 2 : les endpoints principaux. L'API FluentCRM couvre : les contacts (créer, lire, modifier, supprimer), les listes et tags (ajouter/retirer un contact), les campagnes (déclencher, consulter les stats), et les automations (lister, consulter les statuts).

Le format des URL : `https://tonsite.com/wp-json/fluent-crm/v2/contacts` pour les contacts. L'authentification utilise les Application Passwords de WordPress ou un JWT — les Application Passwords sont les plus simples.

**[ÉCRAN — screencast création d'un Application Password]**

[WordPress > Users > ton profil > Application Passwords]

Étape 3 : crée un Application Password. Va dans WordPress > Users > ton profil. En bas, section Application Passwords. Donne un nom ("FluentCRM API" par exemple) et clique "Add New". WordPress génère un mot de passe — copie-le immédiatement, il ne sera plus affiché.

[Montre la génération du mot de passe]

**[ÉCRAN — screencast premier appel API]**

[Utilise Postman, curl ou directement n8n]

Étape 4 : premier appel API. Dans un outil comme Postman ou directement dans le navigateur :

```
GET https://tonsite.com/wp-json/fluent-crm/v2/contacts
Authorization: Basic (ton-user:application-password en base64)
```

Tu reçois une réponse JSON avec la liste de tes contacts. Chaque contact inclut : id, email, first_name, last_name, status, tags, lists.

**[ÉCRAN — screencast n8n + FluentCRM API]**

[Montre un workflow n8n basique]

Étape 5 : l'intégration avec n8n. Dans n8n, utilise un nœud HTTP Request. Configure l'URL de l'endpoint, l'authentification Basic, et tu peux interagir avec FluentCRM depuis tes workflows. Par exemple : quand un formulaire Typeform est soumis, n8n crée un contact dans FluentCRM via l'API.

Cas d'usage concrets avec n8n et l'API FluentCRM :
- Synchroniser des contacts depuis un Google Sheet vers FluentCRM
- Déclencher une automation FluentCRM quand un événement se produit dans un outil externe
- Exporter les stats d'une campagne vers un dashboard Google Sheets
- Créer des contacts depuis un chatbot ou un formulaire externe

**[TRANSITION — face caméra]**

La REST API ouvre FluentCRM à tout ton écosystème. Tu n'es plus limité à ce que FluentCRM fait nativement — tu peux connecter n'importe quel outil. C'est le dernier morceau technique de la formation. Prochaine et dernière étape : le quiz final qui valide toute la formation.

---

**Points clés** :
- REST API = communication entre outils externes et FluentCRM via HTTP/JSON
- Endpoints principaux : contacts, listes, tags, campagnes, automations
- Authentification : Application Passwords WordPress (le plus simple)
- Intégration n8n : nœud HTTP Request pour lire/écrire dans FluentCRM
- Cas d'usage : sync Google Sheets, déclenchement externe d'automations, export stats

**Mots clés SEO** : FluentCRM REST API, API FluentCRM WordPress, n8n FluentCRM intégration, automatiser FluentCRM API

---

### Leçon 16.8 — Quiz final : Valide tes acquis M16 et la formation complète

**Durée** : 4 min
**Type** : Quiz (12 QCM, dont questions transversales M1-M16)
**Seuil de validation** : 80% (10/12)

---

**[INTRO — face caméra]**

Dernier quiz. Douze questions — les sept premières sur le module 16, les cinq dernières transversales sur l'ensemble de la formation. Tu dois obtenir au moins 10 bonnes réponses sur 12 pour valider. C'est le seuil le plus élevé de la formation, parce que c'est le quiz final. Prends ton temps.

---

**Question 1** : Quel est le rôle du SPF ?

- A) Chiffrer le contenu de l'email
- B) Indiquer quels serveurs sont autorisés à envoyer des emails pour ton domaine
- C) Vérifier que l'email n'a pas été modifié en transit
- D) Définir la politique de traitement des emails non authentifiés

**Réponse** : B — SPF liste les serveurs autorisés. Le chiffrement c'est TLS. La vérification d'intégrité c'est DKIM. La politique c'est DMARC.

---

**Question 2** : Quelle est la différence entre un hard bounce et un soft bounce ?

- A) Hard bounce = boîte pleine, soft bounce = adresse invalide
- B) Hard bounce = adresse invalide (permanent), soft bounce = problème temporaire
- C) Hard bounce = rejet par le filtre spam, soft bounce = rejet par le serveur
- D) Aucune différence, les deux retirent le contact

**Réponse** : B — Hard bounce = permanent (adresse inexistante). Soft bounce = temporaire (boîte pleine, serveur indisponible).

---

**Question 3** : Pourquoi remplacer WP-Cron par un vrai cron ?

- A) WP-Cron consomme trop de mémoire
- B) WP-Cron ne se déclenche que lors des visites sur le site
- C) WP-Cron est incompatible avec FluentCRM
- D) WP-Cron envoie les emails en double

**Réponse** : B — WP-Cron dépend des visites. Pas de visite = pas d'exécution = emails en retard.

---

**Question 4** : Sur un hébergement mutualisé, quel est le batch size recommandé pour l'envoi d'emails ?

- A) 10 emails par minute
- B) 50 emails par minute
- C) 200 emails par minute
- D) 500 emails par minute

**Réponse** : B — 50 emails/min sur un mutualisé. Conservateur mais stable — dépasser risque un blocage par l'hébergeur.

---

**Question 5** : Quel type de campagne est recommande pour les archives publiques ?

- A) Toutes les campagnes
- B) Les sequences de vente uniquement
- C) Les newsletters et campagnes de contenu uniquement
- D) Les emails transactionnels

**Réponse** : C — Seules les newsletters et campagnes de contenu ont vocation à être publiques.

---

**Question 6** : Comment authentifier un appel à l'API FluentCRM ?

- A) Clé API FluentCRM
- B) Application Passwords WordPress
- C) Token OAuth Google
- D) Cookie de session WordPress

**Réponse** : B — Les Application Passwords de WordPress sont la méthode la plus simple pour l'API FluentCRM.

---

**Question 7** : Avec une politique DMARC `p=none`, que se passe-t-il si un email échoue au SPF et au DKIM ?

- A) L'email est rejeté
- B) L'email est mis en quarantaine (spam)
- C) Rien — un rapport est envoyé mais l'email passe normalement
- D) L'email est renvoyé automatiquement

**Réponse** : C — `p=none` est le mode monitoring. Les emails passent mais tu reçois des rapports pour analyser les échecs.

---

**— Questions transversales (M1-M16) —**

---

**Question 8** : Dans une automation FluentCRM, qu'est-ce qu'un "goal" de type optionnel ?

- A) Un objectif que le contact doit atteindre pour continuer
- B) Un point de saut — si le contact remplit la condition, il avance directement au goal
- C) Un tag automatiquement appliqué en fin d'automation
- D) Un benchmark de performance de l'automation

**Réponse** : B — Le goal optionnel détecte une condition et fait sauter le contact à ce point de l'automation, où qu'il soit dans le flux.

---

**Question 9** : Quelle est la formule du Publish Score dans le pipeline schoolsWP ?

- A) SEO x 0.40 + LLM x 0.30 + Conversion x 0.30
- B) SEO x 0.30 + LLM x 0.25 + Conversion x 0.25 + Autorité x 0.20
- C) Tous les scores pondérés également à 25%
- D) SEO x 0.50 + Conversion x 0.50

**Réponse** : B — Publish Score = SEO x 0.30 + LLM x 0.25 + Conversion x 0.25 + Autorité x 0.20.

---

**Question 10** : Comment segmenter les contacts qui sont inscrits à un cours TutorLMS mais ne l'ont pas terminé ?

- A) Tag "student" + liste "actifs"
- B) Enrolled in Course X + Course X not completed
- C) Tag "enrolled" uniquement
- D) Enrolled in any course + No tag

**Réponse** : B — La combinaison des deux filtres TutorLMS donne le segment précis.

---

**Question 11** : Que se passe-t-il quand un contact clique "Signaler comme spam" sur ton email ?

- A) FluentCRM ne le sait pas
- B) Le bounce handler reçoit une complaint et désabonne automatiquement le contact
- C) Le contact est supprimé de la base
- D) L'email est renvoyé automatiquement

**Réponse** : B — La complaint est traitée par le bounce handler. Le contact est désabonné automatiquement.

---

**Question 12** : Tu veux envoyer une newsletter automatique chaque semaine avec tes derniers articles. Quel type de campagne utilises-tu ?

- A) Campagne classique programmée chaque semaine
- B) Recurring campaign avec le bloc Latest Post
- C) Automation avec un trigger hebdomadaire
- D) Email individuel à chaque publication

**Réponse** : B — La recurring campaign avec le bloc Latest Post envoie automatiquement tes derniers articles à la fréquence choisie.

---

**[TRANSITION — face caméra]**

Terminée. La formation complète FluentCRM est derrière toi. Tu sais configurer le CRM, créer des automations, intégrer WooCommerce et TutorLMS, gérer les campagnes, segmenter ta base, analyser tes résultats et assurer la délivrabilité de tes emails. Ce n'est pas de la théorie — tout ce que tu as vu est applicable immédiatement sur ton site WordPress. La prochaine étape, c'est la pratique quotidienne. Chaque semaine, consulte tes rapports, ajuste tes automations, teste de nouvelles approches. FluentCRM est un outil — c'est toi qui le rends performant.

---

**Points clés du quiz** :
- 12 questions : 7 sur le module 16, 5 transversales (M1-M16)
- Seuil de validation : 80% (10/12)
- Questions sur : SPF/DKIM/DMARC, bounces, WP-Cron, multi-threading, archives, REST API, goals, TutorLMS, recurring campaigns
- Quiz final de certification — valide l'ensemble de la formation
# Scripts video — Module 16 : Delivrabilite et performance

**Formation** : Maitriser FluentCRM
**Module** : M16 — Delivrabilite et performance (Premium)
**Lecons** : 7 videos + 1 quiz final
**Duree totale** : ~45 min
**Prerequis** : M15 (rapports), M6 (automations), toute la formation
**Date** : 2026-03-23

---

### Lecon 16.1 — Comprends la delivrabilite : pourquoi tes emails arrivent (ou pas) en inbox

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast + slides

---

**[INTRO — face camera]**

Tu as configure FluentCRM, cree tes automations, segmente tes contacts. Mais si tes emails arrivent en spam, tout ca ne sert a rien. La delivrabilite, c'est la capacite de tes emails a atteindre la boite de reception de tes destinataires. Et c'est un sujet que la plupart des formateurs WordPress ignorent jusqu'au jour ou leur taux d'ouverture chute sans explication. Dans cette lecon, tu comprends les mecanismes et les facteurs qui determinent si ton email arrive en inbox ou en spam.

**[ECRAN — slide "Le parcours d'un email"]**

[Schema : ton serveur → serveur SMTP → filtres anti-spam → inbox OU spam OU rejet]

Etape 1 : quand tu envoies un email depuis FluentCRM, voici ce qui se passe. FluentCRM passe le message a ton serveur SMTP — que ce soit le SMTP de ton hebergeur, Amazon SES, SendGrid, Mailgun ou Postmark. Le SMTP envoie au serveur du destinataire. Ce serveur verifie plusieurs choses avant d'accepter le message.

**[ECRAN — slide "Les 5 facteurs de delivrabilite"]**

[Liste numerotee des 5 facteurs]

Etape 2 : les cinq facteurs principaux. Un — l'authentification (SPF, DKIM, DMARC). Le serveur destinataire verifie que tu es bien autorise a envoyer depuis ton domaine. Deux — la reputation de l'IP d'envoi. Si ton IP est sur des listes noires ou a un historique de spam, tes emails sont rejetes. Trois — le contenu de l'email. Certains mots, formats ou ratios image/texte declenchent les filtres anti-spam. Quatre — l'engagement des destinataires. Si beaucoup de tes destinataires n'ouvrent jamais tes emails, les fournisseurs comme Gmail en deduisent que tu envoies du contenu non desire. Cinq — les aspects techniques : bounce rate, plaintes spam, frequence d'envoi.

**[ECRAN — slide "Hebergement mutualise vs VPS"]**

[Tableau comparatif]

Etape 3 : ton type d'hebergement impacte directement ta delivrabilite. En mutualise, tu partages une IP avec d'autres sites. Si un voisin envoie du spam, ta reputation en souffre — tu n'y peux rien. En VPS ou dedie, tu as ta propre IP. Ta reputation ne depend que de toi.

C'est pourquoi la recommandation schoolsWP est claire : pour l'envoi d'emails marketing, utilise un service SMTP dedie — Amazon SES, SendGrid, Mailgun ou Postmark. Ne te repose pas sur le SMTP de ton hebergeur mutualise. Meme sur un VPS, un service SMTP dedie offre de meilleurs outils de monitoring et une meilleure delivrabilite.

**[ECRAN — slide "Les signaux d'alerte"]**

[Liste de 4 signaux]

Etape 4 : comment savoir si tu as un probleme de delivrabilite ? Quatre signaux. Taux d'ouverture en baisse progressive — tes emails atterrissent de plus en plus en spam. Taux de bounce superieur a 2% — des adresses invalides polluent ta base. Plaintes spam en hausse — des destinataires cliquent "signaler comme spam". Emails qui arrivent en spam quand tu testes avec ta propre adresse Gmail.

**[TRANSITION — face camera]**

La delivrabilite n'est pas un reglage unique. C'est un ensemble de bonnes pratiques techniques et comportementales. Dans les prochaines lecons, on s'attaque a chaque facteur : authentification DNS, bounce handlers, cron et multi-threading. On commence par le plus critique : SPF, DKIM et DMARC.

---

**Points cles** :
- Delivrabilite = capacite a atteindre l'inbox (pas juste "envoyer")
- 5 facteurs : authentification DNS, reputation IP, contenu, engagement, technique
- Mutualise : IP partagee = reputation partagee — risque de delivrabilite
- Recommandation : SMTP dedie (Amazon SES, SendGrid, Mailgun, Postmark)
- Signaux d'alerte : ouverture en baisse, bounce > 2%, plaintes spam, test inbox negatif

**Mots cles SEO** : delivrabilite email WordPress, FluentCRM delivrabilite, emails en spam WordPress, SMTP WordPress

---

### Lecon 16.2 — Configure SPF, DKIM et DMARC pour ton domaine

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast DNS + outils de verification

---

**[INTRO — face camera]**

SPF, DKIM, DMARC — trois acronymes qui font fuir. Pourtant, ce sont les trois piliers de l'authentification email. Sans eux, les serveurs destinataires ne peuvent pas verifier que tes emails viennent bien de toi. Et en 2024, Google et Yahoo les exigent explicitement. Un email non authentifie a une forte probabilite d'atterrir en spam ou d'etre rejete. Dans cette lecon, tu configures les trois — pas besoin d'etre admin systeme.

**[ECRAN — slide "SPF, DKIM, DMARC — c'est quoi ?"]**

[Schema simplifie des 3 mecanismes]

Etape 1 : comprends ce que fait chaque mecanisme. SPF (Sender Policy Framework) — un enregistrement DNS qui dit : "Voici les serveurs autorises a envoyer des emails pour mon domaine." DKIM (DomainKeys Identified Mail) — une signature cryptographique ajoutee a chaque email, prouvant que le contenu n'a pas ete modifie. DMARC (Domain-based Message Authentication) — une politique qui dit aux serveurs destinataires quoi faire si SPF ou DKIM echouent : rien, mettre en quarantaine, ou rejeter.

**[ECRAN — screencast panel DNS de l'hebergeur]**

[Ouvre le panel DNS — ex: Cloudflare, OVH ou le panel de WP1]

Etape 2 : configure le SPF. Va dans la zone DNS de ton domaine. Ajoute un enregistrement TXT. Le contenu depend de ton service SMTP.

Pour Amazon SES : `v=spf1 include:amazonses.com ~all`
Pour SendGrid : `v=spf1 include:sendgrid.net ~all`
Pour Mailgun : `v=spf1 include:mailgun.org ~all`
Pour Postmark : `v=spf1 include:spf.mtasv.net ~all`

Si tu as deja un enregistrement SPF (tu en as peut-etre un pour ton hebergeur), ne cree pas un deuxieme — ajoute le `include:` au SPF existant. Un domaine ne doit avoir qu'un seul enregistrement SPF.

[Montre l'ajout dans le panel DNS]

**[ECRAN — screencast configuration DKIM]**

[Montre l'interface du service SMTP]

Etape 3 : configure le DKIM. Dans le dashboard de ton service SMTP (SES, SendGrid, etc.), cherche la section "Domain Authentication" ou "DKIM". Le service te donne des enregistrements DNS a ajouter — generalement des enregistrements CNAME. Copie-les et ajoute-les dans ta zone DNS.

[Montre les enregistrements CNAME a copier]

Etape 4 : ajoute les enregistrements DKIM dans ton panel DNS. Ce sont des CNAME, pas des TXT. Chaque service en demande entre 1 et 3. Copie les valeurs exactement — une faute de frappe et le DKIM echoue.

**[ECRAN — screencast configuration DMARC]**

[Retour dans le panel DNS]

Etape 5 : configure le DMARC. Ajoute un enregistrement TXT avec le nom `_dmarc.tondomaine.com`. Pour commencer, utilise une politique de monitoring :

`v=DMARC1; p=none; rua=mailto:dmarc@tondomaine.com`

Ca ne bloque rien — ca envoie des rapports a ton adresse email pour que tu voies qui envoie des emails en ton nom. Apres quelques semaines de monitoring, passe a `p=quarantine` puis `p=reject` quand tu es confiant.

**[ECRAN — screencast verification avec MXToolbox]**

[Ouvre mxtoolbox.com/supertool]

Etape 6 : verifie ta configuration. Va sur mxtoolbox.com et utilise le SuperTool. Tape ton domaine et verifie le SPF, le DKIM et le DMARC. Tout doit etre en vert. Si un element est en rouge, reviens dans ta zone DNS et corrige.

[Montre les resultats de verification — SPF pass, DKIM pass, DMARC pass]

Etape 7 : envoie un email de test a une adresse Gmail. Ouvre le message, clique sur les trois points, "Afficher l'original". Tu verras les en-tetes SPF, DKIM et DMARC avec le statut PASS ou FAIL. Les trois doivent etre PASS.

**[TRANSITION — face camera]**

SPF, DKIM, DMARC — c'est fait. La propagation DNS peut prendre jusqu'a 48 heures, mais c'est souvent plus rapide. Verifie le lendemain. C'est une configuration a faire une fois — ensuite tu n'y touches plus sauf si tu changes de service SMTP. Prochaine lecon : les bounce handlers, pour gerer les emails qui reviennent en erreur.

---

**Points cles** :
- SPF : enregistrement TXT listant les serveurs autorises a envoyer pour ton domaine
- DKIM : signature cryptographique — enregistrements CNAME fournis par ton service SMTP
- DMARC : politique de traitement si SPF/DKIM echouent — commencer par p=none (monitoring)
- Un seul enregistrement SPF par domaine — combiner les includes si necessaire
- Verifier avec MXToolbox + test email Gmail (Afficher l'original)
- Propagation DNS : jusqu'a 48h

**Mots cles SEO** : SPF DKIM DMARC WordPress, authentification email WordPress, configurer SPF FluentCRM, delivrabilite DNS email

---

### Lecon 16.3 — Configure les bounce handlers

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Un bounce, c'est un email qui revient. Soit parce que l'adresse n'existe pas (hard bounce), soit parce que la boite est pleine ou le serveur temporairement indisponible (soft bounce). Si tu ne geres pas les bounces, tu continues a envoyer a des adresses mortes, ta reputation d'envoi se degrade, et tes emails finissent en spam. FluentCRM gere les bounces automatiquement — mais tu dois connecter un bounce handler. C'est ce qu'on fait maintenant.

**[ECRAN — screencast FluentCRM > Settings > Bounce Handler]**

[Navigation vers les reglages bounce]

Etape 1 : va dans FluentCRM > Settings > Bounce Handler Settings. FluentCRM supporte quatre services : Amazon SES, SendGrid, Mailgun et Postmark. Chaque service a son propre mecanisme de notification de bounce — FluentCRM s'y connecte via webhook.

[Montre la liste des services supportes]

**[ECRAN — screencast configuration bounce Amazon SES]**

[Montre la configuration pour SES comme exemple principal]

Etape 2 : prenons Amazon SES comme exemple — c'est le service le plus utilise pour les gros volumes. Le principe : SES envoie une notification SNS (Simple Notification Service) a FluentCRM quand un email bounce. FluentCRM recoit la notification et met a jour le contact automatiquement.

Etape 3 : dans le dashboard AWS, va dans SES > Configuration Sets. Cree un configuration set si tu n'en as pas. Ajoute une destination de type SNS Topic pour les evenements Bounce et Complaint. Cree le SNS Topic si necessaire.

Etape 4 : dans le SNS Topic, ajoute un subscriber de type HTTPS. L'URL est fournie par FluentCRM dans les reglages Bounce Handler — copie-la exactement. Confirme l'abonnement. AWS envoie une requete de confirmation a FluentCRM, qui la valide automatiquement.

**[ECRAN — screencast configuration bounce SendGrid/Mailgun/Postmark]**

[Montre rapidement les 3 autres services]

Etape 5 : pour les autres services, le principe est le meme. SendGrid : va dans Settings > Mail Settings > Event Webhook, ajoute l'URL FluentCRM, active les evenements Bounce et Spam Report. Mailgun : va dans Sending > Webhooks, ajoute l'URL pour les evenements Bounced et Complained. Postmark : va dans Servers > Webhooks, ajoute l'URL pour Bounce et Spam Complaint.

**[ECRAN — screencast verification du bounce handler]**

[Montre un test de bounce]

Etape 6 : teste le bounce handler. La plupart des services SMTP proposent une adresse de test bounce. Pour SES, envoie un email a `bounce@simulator.amazonses.com`. Attends quelques minutes, puis verifie dans FluentCRM > Contacts que l'adresse est marquee comme bounced. Si le statut change, le handler fonctionne.

Etape 7 : FluentCRM gere les bounces ainsi. Hard bounce : le contact est automatiquement marque comme "bounced" et retire des envois futurs. Soft bounce : FluentCRM reessaie. Apres plusieurs soft bounces consecutifs (generalement 3), le contact passe en hard bounce. Complaint (signalement spam) : le contact est automatiquement desabonne.

**[TRANSITION — face camera]**

Le bounce handler est configure. Tes emails qui reviennent sont maintenant traites automatiquement. Ta base reste propre sans intervention manuelle. Prochaine lecon : on remplace WP-Cron par un vrai cron job — parce que WP-Cron n'est pas fiable pour l'envoi d'emails.

---

**Points cles** :
- Hard bounce = adresse invalide → contact retire des envois
- Soft bounce = probleme temporaire → FluentCRM reessaie puis hard bounce apres ~3 echecs
- Complaint = signalement spam → desabonnement automatique
- 4 services supportes : Amazon SES, SendGrid, Mailgun, Postmark
- Configuration via webhook : URL fournie par FluentCRM a coller dans le service SMTP
- Tester avec les adresses simulateur du service SMTP

**Mots cles SEO** : FluentCRM bounce handler, gerer bounces email WordPress, Amazon SES bounce FluentCRM, SendGrid webhook FluentCRM

---

### Lecon 16.4 — Remplace WP-Cron par un vrai cron job

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress + panel hebergeur

---

**[INTRO — face camera]**

WP-Cron n'est pas un vrai cron. C'est un faux cron qui se declenche uniquement quand quelqu'un visite ton site. Si personne ne visite pendant 2 heures, tes taches planifiees attendent — y compris l'envoi de tes emails FluentCRM. Sur un site a faible trafic, ca signifie que tes emails partent en retard ou par paquets irreguliers. La solution : desactiver WP-Cron et le remplacer par un vrai cron systeme.

**[ECRAN — screencast wp-config.php]**

[Ouvre le fichier wp-config.php]

Etape 1 : desactive WP-Cron. Ouvre `wp-config.php` (via le gestionnaire de fichiers de ton hebergeur ou en FTP). Ajoute cette ligne avant le commentaire "That's all, stop editing!" :

```php
define('DISABLE_WP_CRON', true);
```

Ca empeche WordPress de declencher le cron a chaque visite. Les taches planifiees ne s'executent plus automatiquement — c'est normal, on va les declencher autrement.

**[ECRAN — screencast panel hebergeur — cron jobs]**

[Ouvre cPanel ou le panel specifique — ex: WP1]

Etape 2 : configure un vrai cron job. Va dans le panel de ton hebergeur, section "Cron Jobs" ou "Taches planifiees". Sur WP1, tu trouveras ca dans les outils avances.

Etape 3 : cree une tache cron. La commande a executer :

```bash
wget -q -O /dev/null https://tonsite.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

Ou avec curl :

```bash
curl -s https://tonsite.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

La frequence recommandee : toutes les minutes (`* * * * *`) pour les envois email. Si tu n'envoies pas d'emails en volume, toutes les 5 minutes suffit (`*/5 * * * *`).

[Montre la creation du cron job dans le panel]

**[ECRAN — screencast verification]**

[Montre les tests de verification]

Etape 4 : verifie que le cron fonctionne. Installe le plugin "WP Crontrol" temporairement — il affiche toutes les taches planifiees et leur derniere execution. Tu devrais voir les taches FluentCRM s'executer regulierement. Les evenements doivent montrer une heure d'execution recente (moins de 5 minutes si ton cron tourne toutes les minutes).

Etape 5 : test concret. Planifie l'envoi d'une campagne FluentCRM pour dans 2 minutes. Attends. L'email doit partir a l'heure prevue, sans que tu visites le site. Si l'email part a l'heure : le cron fonctionne. Si l'email ne part pas : reviens dans le panel hebergeur et verifie la commande et la frequence.

**[ECRAN — slide "Mutualise vs VPS — config cron"]**

[Montre les differences de configuration]

Etape 6 : une note sur les hebergeurs mutualises. Certains limitent la frequence minimale du cron a 5 ou 15 minutes. C'est une limitation du mutualise. En VPS, tu as le controle total — toutes les minutes sans restriction. Sur WP1, le cron toutes les minutes est disponible dans les offres standard.

**[TRANSITION — face camera]**

Le vrai cron est en place. Tes emails partent a l'heure, que ton site ait du trafic ou non. C'est un changement invisible pour tes abonnes mais fondamental pour la fiabilite de tes envois. Prochaine lecon : le multi-threading pour les gros volumes.

---

**Points cles** :
- WP-Cron = faux cron declenche par les visites — non fiable pour les emails
- Desactiver avec `define('DISABLE_WP_CRON', true);` dans wp-config.php
- Vrai cron : wget ou curl vers wp-cron.php, toutes les minutes idealement
- Verifier avec WP Crontrol (plugin temporaire)
- Mutualise : frequence parfois limitee a 5-15 min — VPS : toutes les minutes sans restriction
- Sur WP1 : cron toutes les minutes disponible

**Mots cles SEO** : WP-Cron desactiver, vrai cron WordPress, cron job FluentCRM, remplacer WP-Cron, cron WordPress WP1

---

### Lecon 16.5 — Active le multi-threading pour les gros volumes

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Par defaut, FluentCRM envoie les emails un par un. Pour 100 contacts, ca va. Pour 5 000, ca prend des heures. Le multi-threading permet a FluentCRM d'envoyer plusieurs emails en parallele — mais le reglage depend de ton hebergement. Trop agressif, tu satures ton serveur ou tu te fais bloquer par ton SMTP. Pas assez, tes campagnes trainent. Dans cette lecon, tu trouves le bon reglage pour ta configuration.

**[ECRAN — screencast FluentCRM > Settings > Email Settings]**

[Navigation vers les reglages email]

Etape 1 : va dans FluentCRM > Settings > Email Settings. Cherche la section "Email Sending" ou "Email Engine". Tu trouves deux parametres cles : le nombre d'emails par lot (batch size) et le delai entre les lots.

[Montre les champs de configuration]

Etape 2 : le batch size determine combien d'emails FluentCRM envoie a chaque execution du cron. Le delai entre les lots evite de surcharger le serveur.

**[ECRAN — slide "Reglages recommandes par type d'hebergement"]**

[Tableau avec 3 profils]

Etape 3 : les reglages recommandes.

Hebergement mutualise : 50 emails par minute maximum. Batch size de 50, cron toutes les minutes. C'est conservateur mais ca evite les blocages. Ton hebergeur mutualise a des limites — les depasser entraine un blocage temporaire ou un signalement.

VPS standard (2-4 Go RAM) : 200 a 300 emails par minute. Batch size de 100, cron toutes les 30 secondes ou toutes les minutes. Ton VPS tient la charge mais ton service SMTP a peut-etre ses propres limites.

VPS performant + SMTP dedie (SES/SendGrid) : 300 a 500 emails par minute. Batch size de 200, cron toutes les 30 secondes. C'est le maximum recommande avant d'avoir besoin d'une infrastructure email dediee.

**[ECRAN — screencast configuration multi-threading]**

[Montre le reglage dans FluentCRM]

Etape 4 : configure ton batch size en fonction de ton profil. Commence conservateur et augmente progressivement. Si tu es sur un mutualise, reste a 50. La tentation d'augmenter est forte — resiste. Mieux vaut une campagne qui prend 2 heures qu'un serveur bloque.

Etape 5 : verifie aussi les limites de ton service SMTP. Amazon SES : la limite de depart est de 1 email par seconde (200 par jour pour un nouveau compte). SendGrid : depend de ton plan. Mailgun : 300 par minute sur le plan gratuit. Le goulot d'etranglement est souvent le service SMTP, pas FluentCRM.

**[ECRAN — screencast test d'envoi en volume]**

[Montre l'envoi d'une campagne test a un petit groupe]

Etape 6 : teste avant d'envoyer a toute ta base. Cree une campagne test pour 50 contacts. Verifie que les emails partent sans erreur dans le log FluentCRM. Augmente a 200. Puis 500. Si tu vois des erreurs "timeout" ou "connection refused", reduis le batch size.

**[TRANSITION — face camera]**

Le multi-threading est configure. La regle d'or : commence petit et augmente. Mieux vaut un envoi lent qu'un envoi bloque. Prochaine lecon : les reglages avances de FluentCRM — quick nav, archives de campagnes et system log.

---

**Points cles** :
- Multi-threading = envoi d'emails en parallele (batch size + delai entre lots)
- Mutualise : 50 emails/min max — conservateur mais stable
- VPS standard : 200-300 emails/min
- VPS + SMTP dedie : 300-500 emails/min
- Le goulot est souvent le service SMTP (limites SES, SendGrid, Mailgun)
- Toujours tester progressivement : 50 → 200 → 500

**Mots cles SEO** : FluentCRM multi-threading, envoi masse FluentCRM, batch size FluentCRM, vitesse envoi email WordPress

---

### Lecon 16.6 — Reglages avances : quick nav, campaign archives, system log

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

FluentCRM a des reglages avances que la plupart des utilisateurs ne decouvrent jamais. Quick navigation pour acceder plus vite aux contacts. Archives de campagnes pour publier tes newsletters en pages web. System log pour diagnostiquer les problemes. Dans cette lecon, tu actives et configures ces trois fonctionnalites.

**[ECRAN — screencast FluentCRM > Settings > General > Quick Navigation]**

[Navigation vers les reglages generaux]

Etape 1 : la quick navigation. Va dans Settings > General. Cherche "Quick Navigation" ou "Admin Bar". Active l'option. Ca ajoute un raccourci FluentCRM dans la barre d'administration WordPress — tu peux acceder aux contacts, campagnes et automations depuis n'importe quelle page de ton back-office.

[Montre le raccourci dans la barre admin]

Etape 2 : la quick nav affiche aussi les dernieres activites — derniers contacts ajoutes, derniere campagne envoyee. Pratique pour un coup d'oeil rapide sans ouvrir FluentCRM.

**[ECRAN — screencast FluentCRM > Settings > Campaign Archives]**

[Montre les reglages d'archives]

Etape 3 : les archives de campagnes. FluentCRM peut generer une page web publique pour chaque campagne envoyee — comme un archive de newsletter. Va dans Settings, cherche "Campaign Archive" ou "Public Archives".

Etape 4 : active l'option. FluentCRM cree un slug URL pour chaque campagne archivee. Tes abonnes peuvent consulter les anciennes newsletters sur ton site. C'est utile pour deux choses : le SEO (les newsletters deviennent du contenu indexable) et la transparence (les nouveaux abonnes voient ce qu'ils vont recevoir).

[Montre une page d'archive publique]

Etape 5 : attention — n'archive pas toutes tes campagnes. Les emails de relance, les sequences de vente, les emails transactionnels n'ont pas vocation a etre publics. Archive uniquement les newsletters et les campagnes de contenu.

**[ECRAN — screencast FluentCRM > Settings > System Log]**

[Navigation vers le system log]

Etape 6 : le system log. Va dans Settings > Log ou Tools > System Log. C'est le journal technique de FluentCRM. Tu y trouves les erreurs d'envoi, les problemes de cron, les conflits de plugins.

[Montre des exemples d'entrees de log]

Etape 7 : les entrees a surveiller. Les erreurs d'envoi SMTP — elles indiquent un probleme avec ton service d'envoi. Les timeouts de cron — ton cron ne tourne pas ou est trop lent. Les erreurs d'integration — un plugin connecte qui ne repond plus.

Etape 8 : le system log est ton premier reflexe quand quelque chose ne fonctionne pas. Avant de contacter le support FluentCRM, verifie le log. Dans 80% des cas, l'erreur est documentee ici. Copie le message d'erreur exact — ca accelere le diagnostic.

**[TRANSITION — face camera]**

Trois reglages qui ameliorent ton quotidien : la quick nav pour aller plus vite, les archives pour valoriser tes newsletters, et le system log pour diagnostiquer. Prochaine lecon : la REST API pour les developpeurs — et les possibilites avec n8n.

---

**Points cles** :
- Quick Navigation : raccourci FluentCRM dans la barre admin WordPress
- Campaign Archives : newsletters accessibles en pages web publiques (SEO + transparence)
- N'archiver que les newsletters/contenus — pas les emails de vente ou transactionnels
- System Log : journal technique — erreurs SMTP, cron, integrations
- Le log est le premier reflexe avant de contacter le support

**Mots cles SEO** : FluentCRM reglages avances, FluentCRM campaign archive, system log FluentCRM, FluentCRM admin settings

---

### Lecon 16.7 — REST API : les bases pour developper dessus

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast API + n8n

---

**[INTRO — face camera]**

FluentCRM expose une REST API. Ca signifie que tu peux lire et ecrire des donnees FluentCRM depuis n'importe quel outil externe — n8n, Zapier, un script Python, ou une application custom. Dans cette lecon, tu decouvres les endpoints principaux et tu fais un premier appel API. On reste sur les bases — l'objectif est que tu comprennes ce qui est possible, pas que tu deviennes developpeur.

**[ECRAN — slide "REST API — c'est quoi ?"]**

[Schema : outil externe → requete HTTP → FluentCRM → reponse JSON]

Etape 1 : la REST API de FluentCRM permet a des outils externes de communiquer avec FluentCRM via des requetes HTTP. Tu envoies une requete (par exemple "donne-moi la liste des contacts tagges premium"), FluentCRM repond en JSON (le format de donnees standard du web).

**[ECRAN — screencast documentation API FluentCRM]**

[Ouvre la documentation REST API FluentCRM]

Etape 2 : les endpoints principaux. L'API FluentCRM couvre : les contacts (creer, lire, modifier, supprimer), les listes et tags (ajouter/retirer un contact), les campagnes (declencher, consulter les stats), et les automations (lister, consulter les statuts).

Le format des URL : `https://tonsite.com/wp-json/fluent-crm/v2/contacts` pour les contacts. L'authentification utilise les Application Passwords de WordPress ou un JWT — les Application Passwords sont les plus simples.

**[ECRAN — screencast creation d'un Application Password]**

[WordPress > Users > ton profil > Application Passwords]

Etape 3 : cree un Application Password. Va dans WordPress > Users > ton profil. En bas, section Application Passwords. Donne un nom ("FluentCRM API" par exemple) et clique "Add New". WordPress genere un mot de passe — copie-le immediatement, il ne sera plus affiche.

[Montre la generation du mot de passe]

**[ECRAN — screencast premier appel API]**

[Utilise Postman, curl ou directement n8n]

Etape 4 : premier appel API. Dans un outil comme Postman ou directement dans le navigateur :

```
GET https://tonsite.com/wp-json/fluent-crm/v2/contacts
Authorization: Basic (ton-user:application-password en base64)
```

Tu recois une reponse JSON avec la liste de tes contacts. Chaque contact inclut : id, email, first_name, last_name, status, tags, lists.

**[ECRAN — screencast n8n + FluentCRM API]**

[Montre un workflow n8n basique]

Etape 5 : l'integration avec n8n. Dans n8n, utilise un noeud HTTP Request. Configure l'URL de l'endpoint, l'authentification Basic, et tu peux interagir avec FluentCRM depuis tes workflows. Par exemple : quand un formulaire Typeform est soumis, n8n cree un contact dans FluentCRM via l'API.

Cas d'usage concrets avec n8n et l'API FluentCRM :
- Synchroniser des contacts depuis un Google Sheet vers FluentCRM
- Declencher une automation FluentCRM quand un evenement se produit dans un outil externe
- Exporter les stats d'une campagne vers un dashboard Google Sheets
- Creer des contacts depuis un chatbot ou un formulaire externe

**[TRANSITION — face camera]**

La REST API ouvre FluentCRM a tout ton ecosysteme. Tu n'es plus limite a ce que FluentCRM fait nativement — tu peux connecter n'importe quel outil. C'est le dernier morceau technique de la formation. Prochaine et derniere etape : le quiz final qui valide toute la formation.

---

**Points cles** :
- REST API = communication entre outils externes et FluentCRM via HTTP/JSON
- Endpoints principaux : contacts, listes, tags, campagnes, automations
- Authentification : Application Passwords WordPress (le plus simple)
- Integration n8n : noeud HTTP Request pour lire/ecrire dans FluentCRM
- Cas d'usage : sync Google Sheets, declenchement externe d'automations, export stats

**Mots cles SEO** : FluentCRM REST API, API FluentCRM WordPress, n8n FluentCRM integration, automatiser FluentCRM API

---

### Lecon 16.8 — Quiz final : Valide tes acquis M16 et la formation complete

**Duree** : 4 min
**Type** : Quiz (12 QCM, dont questions transversales M1-M16)
**Seuil de validation** : 80% (10/12)

---

**[INTRO — face camera]**

Dernier quiz. Douze questions — les sept premieres sur le module 16, les cinq dernieres transversales sur l'ensemble de la formation. Tu dois obtenir au moins 10 bonnes reponses sur 12 pour valider. C'est le seuil le plus eleve de la formation, parce que c'est le quiz final. Prends ton temps.

---

**Question 1** : Quel est le role du SPF ?

- A) Chiffrer le contenu de l'email
- B) Indiquer quels serveurs sont autorises a envoyer des emails pour ton domaine
- C) Verifier que l'email n'a pas ete modifie en transit
- D) Definir la politique de traitement des emails non authentifies

**Reponse** : B — SPF liste les serveurs autorises. Le chiffrement c'est TLS. La verification d'integrite c'est DKIM. La politique c'est DMARC.

---

**Question 2** : Quelle est la difference entre un hard bounce et un soft bounce ?

- A) Hard bounce = boite pleine, soft bounce = adresse invalide
- B) Hard bounce = adresse invalide (permanent), soft bounce = probleme temporaire
- C) Hard bounce = rejet par le filtre spam, soft bounce = rejet par le serveur
- D) Aucune difference, les deux retirent le contact

**Reponse** : B — Hard bounce = permanent (adresse inexistante). Soft bounce = temporaire (boite pleine, serveur indisponible).

---

**Question 3** : Pourquoi remplacer WP-Cron par un vrai cron ?

- A) WP-Cron consomme trop de memoire
- B) WP-Cron ne se declenche que lors des visites sur le site
- C) WP-Cron est incompatible avec FluentCRM
- D) WP-Cron envoie les emails en double

**Reponse** : B — WP-Cron depend des visites. Pas de visite = pas d'execution = emails en retard.

---

**Question 4** : Sur un hebergement mutualise, quel est le batch size recommande pour l'envoi d'emails ?

- A) 10 emails par minute
- B) 50 emails par minute
- C) 200 emails par minute
- D) 500 emails par minute

**Reponse** : B — 50 emails/min sur un mutualise. Conservateur mais stable — depasser risque un blocage par l'hebergeur.

---

**Question 5** : Quel type de campagne est recommande pour les archives publiques ?

- A) Toutes les campagnes
- B) Les sequences de vente uniquement
- C) Les newsletters et campagnes de contenu uniquement
- D) Les emails transactionnels

**Reponse** : C — Seules les newsletters et campagnes de contenu ont vocation a etre publiques.

---

**Question 6** : Comment authentifier un appel a l'API FluentCRM ?

- A) Cle API FluentCRM
- B) Application Passwords WordPress
- C) Token OAuth Google
- D) Cookie de session WordPress

**Reponse** : B — Les Application Passwords de WordPress sont la methode la plus simple pour l'API FluentCRM.

---

**Question 7** : Avec une politique DMARC `p=none`, que se passe-t-il si un email echoue au SPF et au DKIM ?

- A) L'email est rejete
- B) L'email est mis en quarantaine (spam)
- C) Rien — un rapport est envoye mais l'email passe normalement
- D) L'email est renvoye automatiquement

**Reponse** : C — `p=none` est le mode monitoring. Les emails passent mais tu recois des rapports pour analyser les echecs.

---

**— Questions transversales (M1-M16) —**

---

**Question 8** : Dans une automation FluentCRM, qu'est-ce qu'un "goal" de type optionnel ?

- A) Un objectif que le contact doit atteindre pour continuer
- B) Un point de saut — si le contact remplit la condition, il avance directement au goal
- C) Un tag automatiquement applique en fin d'automation
- D) Un benchmark de performance de l'automation

**Reponse** : B — Le goal optionnel detecte une condition et fait sauter le contact a ce point de l'automation, ou qu'il soit dans le flux.

---

**Question 9** : Quelle est la formule du Publish Score dans le pipeline schoolsWP ?

- A) SEO x 0.40 + LLM x 0.30 + Conversion x 0.30
- B) SEO x 0.30 + LLM x 0.25 + Conversion x 0.25 + Autorite x 0.20
- C) Tous les scores ponderes egalement a 25%
- D) SEO x 0.50 + Conversion x 0.50

**Reponse** : B — Publish Score = SEO x 0.30 + LLM x 0.25 + Conversion x 0.25 + Autorite x 0.20.

---

**Question 10** : Comment segmenter les contacts qui sont inscrits a un cours TutorLMS mais ne l'ont pas termine ?

- A) Tag "student" + liste "actifs"
- B) Enrolled in Course X + Course X not completed
- C) Tag "enrolled" uniquement
- D) Enrolled in any course + No tag

**Reponse** : B — La combinaison des deux filtres TutorLMS donne le segment precis.

---

**Question 11** : Que se passe-t-il quand un contact clique "Signaler comme spam" sur ton email ?

- A) FluentCRM ne le sait pas
- B) Le bounce handler recoit une complaint et desabonne automatiquement le contact
- C) Le contact est supprime de la base
- D) L'email est renvoye automatiquement

**Reponse** : B — La complaint est traitee par le bounce handler. Le contact est desabonne automatiquement.

---

**Question 12** : Tu veux envoyer une newsletter automatique chaque semaine avec tes derniers articles. Quel type de campagne utilises-tu ?

- A) Campagne classique programmee chaque semaine
- B) Recurring campaign avec le bloc Latest Post
- C) Automation avec un trigger hebdomadaire
- D) Email individuel a chaque publication

**Reponse** : B — La recurring campaign avec le bloc Latest Post envoie automatiquement tes derniers articles a la frequence choisie.

---

**[TRANSITION — face camera]**

Terminee. La formation complete FluentCRM est derriere toi. Tu sais configurer le CRM, creer des automations, integrer WooCommerce et TutorLMS, gerer les campagnes, segmenter ta base, analyser tes resultats et assurer la delivrabilite de tes emails. Ce n'est pas de la theorie — tout ce que tu as vu est applicable immediatement sur ton site WordPress. La prochaine etape, c'est la pratique quotidienne. Chaque semaine, consulte tes rapports, ajuste tes automations, teste de nouvelles approches. FluentCRM est un outil — c'est toi qui le rends performant.

---

**Points cles du quiz** :
- 12 questions : 7 sur le module 16, 5 transversales (M1-M16)
- Seuil de validation : 80% (10/12)
- Questions sur : SPF/DKIM/DMARC, bounces, WP-Cron, multi-threading, archives, REST API, goals, TutorLMS, recurring campaigns
- Quiz final de certification — valide l'ensemble de la formation
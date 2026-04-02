# Script video — Module 7, Lecon 2 : FluentForms + FluentSMTP

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 — Ecosysteme et integrations
**Lecon** : 2/9 — FluentForms + FluentSMTP
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast config FluentSMTP, slide probleme/solution
**Objectif** : Configurer FluentSMTP pour garantir la delivrabilite des notifications formulaires

---

**[INTRO — face camera]**

Tu as configure tes formulaires, tes notifications email, tes confirmations. Tout fonctionne en test. Mais en production, les emails n'arrivent pas. Ou ils arrivent en spam. Ou ils arrivent avec 30 minutes de retard.

Le probleme n'est pas FluentForms. Le probleme, c'est la facon dont WordPress envoie les emails par defaut.

**[SECTION 1 — slide "Le probleme"]**

WordPress utilise la fonction PHP mail() pour envoyer les emails. C'est la methode la plus basique qui existe. La plupart des hebergeurs la limitent, la ralentissent, ou la bloquent partiellement.

Resultat : tes notifications FluentForms partent via un serveur d'envoi generique. Pas d'authentification SPF, pas de DKIM, pas de DMARC. Les fournisseurs email (Gmail, Outlook, Yahoo) voient ca comme du spam potentiel.

La consequence : le client remplit ton formulaire de contact, tu recois la notification avec 2 heures de retard. Le client qui a paye ne recoit jamais son email de confirmation. Et toi, tu ne sais meme pas que ca ne marche pas.

**[SECTION 2 — screencast "Installer FluentSMTP"]**

FluentSMTP est gratuit. Dashboard WordPress, Plugins, Add New, cherche "FluentSMTP". Installe et active.

FluentSMTP remplace la fonction mail() de WordPress par un envoi authentifie via un service professionnel. Tous les emails WordPress passent par FluentSMTP — les notifications FluentForms, les emails FluentCRM, les emails WooCommerce, tout.

**[SECTION 3 — screencast "Configurer un service d'envoi"]**

FluentSMTP supporte plusieurs services. Voici les principaux.

Brevo (ex-Sendinblue). Mon recommandation. Offre gratuite : 300 emails par jour. Serveurs en Europe. RGPD natif. Parfait pour demarrer.

Amazon SES. Le moins cher a grande echelle. 0.10 dollar pour 1000 emails. Mais la configuration est plus technique.

SendGrid. Fiable, bien documente. Offre gratuite limitee.

Gmail / Google Workspace. Si tu as un compte Google Workspace, tu peux envoyer via l'API Gmail. Limite : 500 emails par jour.

SMTP generique. Si tu as deja un serveur SMTP (OVH, Gandi, autre), tu peux l'utiliser.

Pour cette demo, on configure Brevo.

Connecte-toi a brevo.com, cree un compte si tu n'en as pas. Va dans Settings, SMTP & API, API Keys. Genere une cle API.

Retour dans FluentSMTP. Selectionne "Brevo" comme service. Colle ta cle API. Configure l'adresse d'expediteur : ton-email@ton-domaine.com. Configure le nom d'expediteur : "schoolsWP" ou ton nom.

Sauvegarde.

**[SECTION 4 — screencast "Authentification DNS"]**

Pour que tes emails arrivent vraiment en boite de reception, il faut authentifier ton domaine.

Brevo te donne des enregistrements DNS a ajouter chez ton registrar ou ton hebergeur. Trois types :

SPF : dit aux serveurs email "Brevo est autorise a envoyer des emails pour mon domaine."

DKIM : signe cryptographiquement chaque email. Le destinataire peut verifier que l'email n'a pas ete modifie.

DMARC : indique quoi faire si un email echoue SPF ou DKIM — le rejeter, le mettre en quarantaine, ou l'accepter quand meme.

Ajoute ces enregistrements DNS. Brevo verifie automatiquement. Quand les trois sont valides, tes emails ont une delivrabilite optimale.

Si tu ne sais pas comment ajouter des enregistrements DNS, ton hebergeur a une documentation. OVH, Infomaniak, o2switch — ils ont tous un tutoriel pour ca.

**[SECTION 5 — screencast "Tester l'envoi"]**

FluentSMTP inclut un outil de test. Va dans FluentSMTP, Settings, et cherche "Send Test Email".

Entre ton adresse email. Envoie. L'email doit arriver en quelques secondes — pas en minutes, en secondes.

Verifie dans ta boite de reception. L'email est-il arrive ? Dans la boite principale ou en spam ? Si c'est en spam, verifie les enregistrements DNS.

FluentSMTP affiche aussi un log de tous les emails envoyes. Tu vois le destinataire, l'objet, le statut (envoye, echec). Si un email echoue, tu sais pourquoi.

**[SECTION 6 — slide "Apres FluentSMTP"]**

Une fois FluentSMTP configure, tous tes emails WordPress passent par le service que tu as choisi.

Les notifications FluentForms arrivent en boite de reception. Les emails FluentCRM arrivent en boite de reception. Les confirmations de commande WooCommerce arrivent en boite de reception.

C'est un changement invisible pour tes visiteurs, mais critique pour ton business. Un email qui n'arrive pas, c'est un client perdu.

FluentSMTP est le fondement invisible de tout ton ecosysteme email. Configure-le une fois, oublie-le. Il fait son travail en silence.

**[OUTRO — face camera]**

FluentSMTP est en place. Tes emails arrivent. Dans la prochaine lecon, on connecte FluentForms a FluentBooking — la prise de rendez-vous dans WordPress.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- WordPress envoie mal les emails par defaut (PHP mail() = spam)
- FluentSMTP : gratuit, remplace mail() par un envoi authentifie
- Brevo recommande : 300 emails/jour gratuits, serveurs EU, RGPD
- Authentification DNS : SPF + DKIM + DMARC obligatoires
- Tester avec l'outil integre : l'email doit arriver en secondes
- Tous les emails WordPress passent par FluentSMTP une fois configure

**Mots cles SEO** : FluentSMTP configuration, email WordPress spam, delivrabilite email WordPress, FluentSMTP Brevo

---

**Notes de production** :
- Face camera : intro (le probleme invisible) + outro (transition FluentBooking)
- Screencast : installation + config Brevo + test (~4 min)
- Slides : 2 slides (probleme + apres FluentSMTP)
- Ton : technique mais accessible — insister sur l'importance critique de la delivrabilite

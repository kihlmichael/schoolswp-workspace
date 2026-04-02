# Script video — Module 7, Lecon 5 : FluentForms + Brevo

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 — Ecosysteme et integrations
**Lecon** : 5/9 — FluentForms + Brevo
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast config Brevo + FluentForms, slide comparatif
**Objectif** : Connecter FluentForms a Brevo pour l'email marketing heberge

---

**[INTRO — face camera]**

FluentCRM est natif WordPress — parfait si tu veux tout garder chez toi. Mais certains preferent un service heberge pour l'email marketing. Plus d'infrastructure a gerer, delivrabilite geree par le service, interface web accessible de partout.

Brevo — anciennement Sendinblue — est le service le plus utilise en France. Serveurs EU, RGPD natif, offre gratuite genereuse. Et FluentForms s'y connecte nativement.

**[SECTION 1 — slide "Pourquoi Brevo"]**

Brevo a plusieurs avantages pour le marche francais.

Serveurs en Europe. Tes donnees restent en EU. C'est un point RGPD important.

Offre gratuite. 300 emails par jour, contacts illimites. Pour un site qui demarre, c'est largement suffisant.

Interface en francais. Dashboard, rapports, templates — tout est traduit.

Multi-canal. Email, SMS, WhatsApp, chat. Si tu veux envoyer des SMS de rappel en plus des emails, Brevo le fait.

API documentee. L'integration avec FluentForms passe par l'API. Ca prend 2 minutes.

**[SECTION 2 — screencast "Obtenir la cle API Brevo"]**

Connecte-toi a app.brevo.com. Si tu n'as pas de compte, cree-en un — c'est gratuit.

Va dans Settings (en haut a droite), SMTP & API, API Keys. Genere une nouvelle cle API v3. Copie-la — tu en auras besoin dans FluentForms.

Note : cette cle API donne acces a ton compte Brevo. Ne la partage pas et ne la commite pas dans un repo git.

**[SECTION 3 — screencast "Configurer l'integration dans FluentForms"]**

Direction FluentForms, Settings (global), Integrations. Cherche Brevo dans la liste.

Colle ta cle API. FluentForms verifie la connexion. Si c'est vert, tu es connecte.

Maintenant, ouvre un formulaire. Va dans Settings, Marketing & CRM Integrations. Tu vois "Brevo" dans la liste. Ajoute un feed.

Le feed te demande de mapper les champs.

Email : champ Email du formulaire.
First Name : champ Prenom.
Last Name : champ Nom (si disponible).

Selectionne la liste Brevo dans laquelle le contact sera ajoute. Si tu n'as pas encore cree de listes dans Brevo, fais-le d'abord : Brevo, Contacts, Lists, Create a new list.

Sauvegarde le feed. A chaque soumission de ce formulaire, le contact est ajoute dans Brevo avec les bons champs et la bonne liste.

**[SECTION 4 — screencast "Double opt-in avec Brevo"]**

Brevo gere le double opt-in de son cote. Si tu actives l'option DOI dans la liste Brevo, le contact recoit un email de confirmation apres l'inscription.

C'est different du double opt-in FluentCRM qui est gere dans WordPress. Ici, c'est Brevo qui envoie l'email de confirmation depuis ses serveurs.

Pour une configuration propre : active le double opt-in dans Brevo pour les listes de newsletter. Desactive-le pour les listes de clients ou de prospects qualifies (ils t'ont deja contacte ou achete).

**[SECTION 5 — slide "FluentCRM vs Brevo — quand utiliser quoi"]**

La question que tu te poses : FluentCRM ou Brevo ?

Utilise FluentCRM si tu veux tout garder dans WordPress, si tu maitrises ton hebergement, et si tu preferes une solution sans abonnement mensuel. FluentCRM Pro est une licence annuelle — pas de cout par email.

Utilise Brevo si tu preferes un service heberge, si tu n'as pas un hebergement performant, si tu veux du multi-canal (SMS, WhatsApp), ou si tu as une equipe qui doit acceder au CRM sans acces WordPress.

Tu peux aussi utiliser les deux. FluentCRM pour la segmentation et les automations internes, Brevo pour l'envoi massif de newsletters. FluentSMTP fait le pont entre les deux — il envoie les emails FluentCRM via les serveurs Brevo.

Sur schoolsWP, on utilise FluentCRM pour le CRM et les automations, et FluentSMTP + Brevo pour l'envoi. Le meilleur des deux mondes.

**[SECTION 6 — screencast "Tester l'integration"]**

Soumets le formulaire avec une adresse email de test. Va dans Brevo, Contacts. Verifie que le contact apparait dans la bonne liste avec les bons champs.

Si le double opt-in est actif, verifie que l'email de confirmation arrive. Clique sur le lien de confirmation. Le statut du contact doit passer a "Confirmed" dans Brevo.

Si le contact n'apparait pas : verifie la cle API, verifie que la liste existe, verifie le mapping des champs. L'erreur la plus courante : l'email est deja dans la liste Brevo en statut "Unsubscribed" — dans ce cas, Brevo ne le reinscrit pas.

**[OUTRO — face camera]**

FluentForms et Brevo sont connectes. Tu as une alternative hebergee a FluentCRM pour l'email marketing. Dans la prochaine lecon, on connecte FluentForms a Google Sheets — pour centraliser les donnees dans un tableur partage.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Brevo : service email marketing heberge, serveurs EU, RGPD natif, 300 emails/jour gratuits
- Integration via cle API v3 : FluentForms Settings → Integrations → Brevo
- Feed par formulaire : mapping email + prenom + nom + liste
- Double opt-in gere par Brevo (pas par FluentForms)
- FluentCRM vs Brevo : natif WordPress vs service heberge — les deux sont compatibles
- Tester : verifier le contact dans la bonne liste Brevo apres soumission

**Mots cles SEO** : FluentForms Brevo, Sendinblue WordPress formulaire, email marketing WordPress Brevo, FluentForms integration Brevo

---

**Notes de production** :
- Face camera : intro (service heberge vs natif) + outro (transition Google Sheets)
- Screencast : config API + feed + test (~5 min)
- Slides : 2 slides (pourquoi Brevo + FluentCRM vs Brevo)
- Ton : neutre, comparatif — pas de parti pris, montrer les cas d'usage de chaque option

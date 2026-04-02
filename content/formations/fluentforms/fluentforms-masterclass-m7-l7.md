# Script video — Module 7, Lecon 7 : Webhooks et Zapier

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 — Ecosysteme et integrations
**Lecon** : 7/9 — Webhooks et Zapier
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast config webhook + Zapier, slide cas pratiques
**Objectif** : Connecter FluentForms a n'importe quelle application via webhooks et Zapier

---

**[INTRO — face camera]**

FluentForms se connecte nativement a FluentCRM, Brevo, Google Sheets. Mais il existe des milliers d'autres applications — Slack, Trello, Airtable, Notion, ton propre systeme interne. Les webhooks et Zapier te permettent de tout connecter.

**[SECTION 1 — slide "Webhook vs Zapier"]**

Un webhook, c'est un appel HTTP. Quand le formulaire est soumis, FluentForms envoie les donnees a une URL que tu definis. L'application qui recoit ces donnees les traite comme elle veut.

C'est gratuit. C'est rapide. Mais il faut que l'application de destination sache recevoir des webhooks.

Zapier, c'est un intermediaire. FluentForms envoie les donnees a Zapier. Zapier les transmet a l'application de ton choix — Slack, Trello, Airtable, et 6000 autres. Pas besoin de savoir coder.

Zapier a un cout. L'offre gratuite permet 100 taches par mois. Les plans payants commencent a 19 dollars par mois.

Alternative gratuite : n8n. C'est un outil d'automatisation open source que tu peux heberger toi-meme. Il recoit les webhooks FluentForms exactement comme Zapier, mais sans frais mensuels. C'est ce qu'on utilise sur schoolsWP.

**[SECTION 2 — screencast "Configurer un webhook"]**

Ouvre ton formulaire dans FluentForms. Settings, Webhooks. Ajoute un webhook.

URL : l'adresse ou FluentForms va envoyer les donnees. Ca depend de l'application de destination.

Pour n8n : cree un workflow avec un noeud "Webhook" en trigger. n8n te donne une URL. Colle-la dans FluentForms.

Pour un serveur custom : ton URL d'API qui recoit les POST.

Methode : POST (par defaut). Format : JSON.

Mapping des champs. Selectionne quels champs du formulaire envoyer. Tu peux tous les envoyer ou en selectionner certains.

Ajoute des headers si necessaire — par exemple un header d'authentification : "Authorization: Bearer ton-token". Ca securise le webhook pour que personne d'autre ne puisse envoyer des donnees a ton URL.

**[SECTION 3 — screencast "Configurer Zapier"]**

Si tu utilises Zapier, c'est encore plus simple.

Connecte-toi a zapier.com. Cree un nouveau Zap.

Trigger : FluentForms. L'integration Zapier de FluentForms te connecte directement. Selectionne ton formulaire. Zapier teste la connexion en envoyant une soumission de test.

Action : l'application de destination. Par exemple, Slack.

Configure l'action : dans quel channel Slack envoyer le message, quel format, quels champs inclure.

Active le Zap. A chaque soumission de formulaire, Zapier envoie une notification Slack.

**[SECTION 4 — slide "Cas pratiques"]**

Voici des automatisations concretes.

Soumission → Slack. Une notification dans le channel #leads a chaque nouvelle soumission. L'equipe est alertee en temps reel.

Soumission → Trello. Chaque demande de devis cree une carte dans le tableau "Pipeline Commercial". Colonnes : Nouveau, En cours, Envoye, Gagne, Perdu.

Soumission → Airtable. Les donnees du formulaire alimentent une base Airtable — plus structure que Google Sheets, avec des vues, des filtres, des relations entre tables.

Soumission → Notion. Chaque lead cree une page dans une base de donnees Notion. L'equipe ajoute ses notes et suit le pipeline.

Soumission → n8n → Multiple actions. Un seul webhook declenche un workflow n8n qui fait 5 choses en parallele : cree le contact dans FluentCRM, envoie une notification Slack, ajoute une ligne dans Google Sheets, cree une tache dans Trello, et envoie un SMS de confirmation via Brevo.

C'est la puissance des webhooks : un point d'entree, des actions illimitees.

**[SECTION 5 — screencast "Webhook conditionnel"]**

Tu ne veux pas envoyer toutes les soumissions au meme endroit.

Exemple : les demandes de devis "Budget > 5000 euros" vont dans un channel Slack #high-value. Les autres vont dans #leads-standard.

Configure deux webhooks avec des conditions. Webhook 1 : condition "Budget IS Plus de 5000 euros" → URL du webhook Slack #high-value. Webhook 2 : condition "Budget IS NOT Plus de 5000 euros" → URL du webhook Slack #leads-standard.

Comme pour les feeds FluentCRM, tu peux conditionner chaque webhook selon les reponses du formulaire.

**[SECTION 6 — screencast "Debugger un webhook"]**

Les webhooks echouent parfois. Voici comment debugger.

Verifie l'URL. La moindre erreur de caractere et le webhook ne trouve pas la destination.

Verifie le format. Certaines applications attendent du JSON, d'autres du form-data. FluentForms envoie du JSON par defaut — verifie que c'est bien ce que l'application attend.

Verifie les headers. Si ton application demande un token d'authentification, il doit etre dans les headers du webhook.

Utilise un outil de debug. webhook.site te donne une URL temporaire qui affiche tout ce qu'elle recoit. Utilise cette URL pour verifier que FluentForms envoie bien les bonnes donnees au bon format. Une fois confirme, remplace par l'URL de production.

Verifie les logs. FluentForms Pro affiche un log des webhooks envoyes et leur statut (succes, echec, code HTTP). Si tu vois un code 400 ou 500, c'est un probleme cote destination.

**[OUTRO — face camera]**

Tu peux maintenant connecter FluentForms a n'importe quelle application. Les webhooks sont la porte de sortie universelle. Dans la prochaine lecon, on s'attaque a un sujet obligatoire : le RGPD et la conformite legale de tes formulaires.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Webhook : appel HTTP direct vers n'importe quelle URL (gratuit)
- Zapier : intermediaire no-code vers 6000+ apps (payant au-dela de 100 taches/mois)
- n8n : alternative open source auto-hebergee (utilise sur schoolsWP)
- Webhooks conditionnels : destination differente selon les reponses
- Debug : webhook.site pour tester, verifier URL/format/headers/logs
- Cas pratiques : Slack, Trello, Airtable, Notion, n8n multi-actions

**Mots cles SEO** : FluentForms webhook, FluentForms Zapier, automatisation formulaire WordPress, webhook WordPress formulaire

---

**Notes de production** :
- Face camera : intro (connecter a tout) + outro (transition RGPD)
- Screencast : config webhook + Zapier + debug (~7 min)
- Slides : 2 slides (webhook vs Zapier + cas pratiques)
- Ton : oriente possibilites — montrer l'etendue des connexions possibles

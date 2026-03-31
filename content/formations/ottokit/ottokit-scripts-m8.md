# Scripts video — Module 8 : Integrations WordPress : WooCommerce, LMS, CRM

**Formation** : Maitriser OttoKit
**Module** : M8 — Integrations WordPress : WooCommerce, LMS, CRM
**Lecons** : 8 videos + 1 quiz
**Duree totale** : ~50 min de video
**Date** : 2026-03-30

---

## Lecon 8.1 — Connecter tes plugins WordPress a OttoKit

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit + WordPress admin

---

**[INTRO — face camera]**

Tu as un site WordPress avec WooCommerce, TutorLMS, FluentCRM, des formulaires. Chacun de ces plugins produit des evenements : une commande, une inscription, un tag ajoute. OttoKit peut reagir a tous ces evenements — mais il faut d'abord qu'il les detecte.

**[ECRAN — screencast WordPress admin]**

[Ouvre le tableau de bord WordPress]
[Va dans Extensions > Extensions installees]
[Montre la liste des plugins actifs : WooCommerce, TutorLMS, FluentCRM, Fluent Forms, SureForms]

Voici les plugins actifs sur le site schoolsWP. Chacun est une source d'evenements potentielle pour OttoKit.

**[ECRAN — screencast OttoKit dashboard]**

[Ouvre app.ottokit.com]
[Va dans Connections]
[Clique sur la connexion WordPress du site schoolsWP]
[Montre la liste des plugins detectes automatiquement]

Quand tu connectes ton site WordPress a OttoKit, le plugin scanne automatiquement les extensions actives. Ici, tu vois la liste de tout ce qu'OttoKit a detecte : WooCommerce, TutorLMS, FluentCRM, Fluent Forms, SureForms.

**[ECRAN — screencast verification]**

[Montre un plugin detecte — ex: WooCommerce — avec un badge "Connected" ou une icone verte]
[Montre un plugin non detecte ou non supporte — ex: un plugin obscur sans icone]

Si un plugin apparait dans la liste avec un badge vert, c'est bon. OttoKit peut utiliser ses triggers et ses actions. Si un plugin n'apparait pas, deux raisons possibles : soit OttoKit ne le supporte pas encore, soit le plugin est desactive.

**[ECRAN — slide "Les plugins WordPress les plus utilises avec OttoKit"]**

| Plugin | Triggers | Actions | Usage |
|--------|----------|---------|-------|
| WooCommerce | Commande, produit, client | Creer coupon, modifier commande | E-commerce |
| TutorLMS | Inscription, progression, completion | Inscrire, desinscrire | Formation |
| FluentCRM | Tag ajoute, liste, contact | Ajouter tag, envoyer email | CRM |
| Fluent Forms | Soumission formulaire | — | Formulaires |
| SureForms | Soumission formulaire | — | Formulaires |
| Elementor | Soumission formulaire | — | Page builder |
| BuddyBoss | Inscription, activite | Creer groupe | Communaute |

**[ECRAN — screencast ajout d'un plugin manquant]**

[Retourne dans WordPress admin]
[Active un plugin desactive — ex: BuddyBoss]
[Reviens dans OttoKit > Connections]
[Rafraichit la page]
[Montre le plugin qui apparait maintenant dans la liste]

Si tu actives un nouveau plugin sur ton site, OttoKit le detecte lors de la prochaine synchronisation. Parfois, un simple rafraichissement de la page suffit.

**[TRANSITION — face camera]**

Tes plugins sont detectes. A partir de maintenant, on entre dans le concret. Prochaine lecon : on construit un workflow WooCommerce complet avec notification, Google Sheets et email.

---

**Points cles**
- OttoKit detecte automatiquement les plugins WordPress actifs sur ton site
- La detection se fait via le plugin OttoKit installe dans WordPress
- Si un plugin n'apparait pas, verifier qu'il est active et supporte par OttoKit
- Les plugins les plus courants : WooCommerce, TutorLMS, FluentCRM, Fluent Forms

**Mots-cles SEO**
- OttoKit plugins WordPress
- connecter WooCommerce OttoKit
- OttoKit detection automatique plugins
- integrations WordPress OttoKit

---

## Lecon 8.2 — WooCommerce : commande → notification + Sheets + email

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Un client passe commande sur ton site. Tu veux trois choses : recevoir une notification, enregistrer la vente dans un Google Sheet, et envoyer un email de remerciement personnalise au client. Avec OttoKit, un seul workflow gere les trois.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Clique sur "Create Workflow"]
[Nomme le workflow : "Commande WooCommerce → notification + Sheets + email"]

On commence par nommer le workflow. Un nom clair, ca fait gagner du temps quand tu en auras vingt.

**[ECRAN — screencast configuration du trigger]**

[Clique sur le bloc trigger]
[Selectionne "WooCommerce"]
[Selectionne l'evenement "Order Created"]
[Pointe le badge "Instant"]
[Selectionne la connexion WordPress]
[Clique sur "Fetch Data"]
[Montre les champs retournes : order_id, billing_first_name, billing_email, total, line_items, status]
[Clique sur "Save"]

Le trigger est "Order Created" — instantane. Des qu'une commande arrive, le workflow demarre. Le Fetch Data montre tous les champs disponibles : numero de commande, nom du client, email, montant total, produits commandes.

**[ECRAN — screencast ajout de l'action 1 — Notification Slack/email admin]**

[Clique sur "+" pour ajouter une action]
[Selectionne "Slack" (ou "Send Email" si pas de Slack)]
[Selectionne l'evenement "Send Channel Message"]
[Selectionne la connexion Slack et le channel #ventes]
[Configure le message :]

```
Nouvelle commande #{{order_id}}
Client : {{billing_first_name}} {{billing_last_name}}
Montant : {{total}} EUR
```

[Clique sur "Test Action"]
[Montre le message envoye dans Slack]
[Clique sur "Save"]

Premiere action : notifier l'equipe. Ici on envoie un message Slack dans le channel #ventes. Le message utilise les donnees du trigger : numero de commande, nom du client, montant. Tu testes, ca fonctionne, tu enregistres.

**[ECRAN — screencast ajout de l'action 2 — Google Sheets]**

[Clique sur "+" pour ajouter une deuxieme action]
[Selectionne "Google Sheets"]
[Selectionne l'evenement "Add Row"]
[Selectionne la connexion Google]
[Selectionne le spreadsheet "Ventes schoolsWP"]
[Selectionne la feuille "2026"]
[Mappe les colonnes :]

| Colonne Sheet | Champ OttoKit |
|---------------|---------------|
| Date | {{date_created}} |
| Commande | {{order_id}} |
| Client | {{billing_first_name}} {{billing_last_name}} |
| Email | {{billing_email}} |
| Montant | {{total}} |

[Clique sur "Test Action"]
[Montre la nouvelle ligne dans Google Sheets]
[Clique sur "Save"]

Deuxieme action : enregistrer la vente dans ton tableur. Tu mappes chaque colonne avec les donnees de la commande. Le test confirme que la ligne s'ajoute.

**[ECRAN — screencast ajout de l'action 3 — Email client]**

[Clique sur "+" pour ajouter une troisieme action]
[Selectionne "Gmail" ou "Send Email"]
[Configure :]
- To : {{billing_email}}
- Subject : Merci pour ta commande #{{order_id}}
- Body :

```
Bonjour {{billing_first_name}},

Merci pour ta commande sur schoolsWP !

Recapitulatif :
- Commande : #{{order_id}}
- Montant : {{total}} EUR

Tu recevras un email de suivi des que ta commande sera expediee.

A tres vite,
L'equipe schoolsWP
```

[Clique sur "Test Action"]
[Montre l'email recu dans Gmail]
[Clique sur "Save"]

Troisieme action : envoyer un email de remerciement personnalise. Le prenom, le numero de commande, le montant — tout vient du trigger.

**[ECRAN — screencast vue globale du workflow]**

[Zoom out pour voir le workflow complet : Trigger → Slack → Sheets → Email]
[Active le workflow (bouton "Publish" ou "Activate")]

Voila le workflow complet. Un trigger, trois actions enchainees. Chaque commande declenche une notification, un enregistrement et un email — automatiquement.

**[TRANSITION — face camera]**

Ce workflow est la base de tout site e-commerce sur WordPress. Dans la prochaine lecon, on va plus loin avec WooCommerce : creer automatiquement un coupon de fidelisation apres le premier achat.

---

**Points cles**
- Un seul trigger WooCommerce peut alimenter plusieurs actions en cascade
- Toujours tester chaque action individuellement avant de publier
- Les donnees du trigger (order_id, billing_email, total) sont reutilisables dans toutes les actions
- Ce workflow remplace 3 taches manuelles : notification, saisie tableur, email

**Mots-cles SEO**
- OttoKit WooCommerce workflow
- automatiser commande WooCommerce
- notification vente WordPress
- Google Sheets WooCommerce automatique

---

## Lecon 8.3 — WooCommerce : coupon automatique apres premier achat

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Un client achete pour la premiere fois. Tu veux le remercier avec un coupon de reduction pour l'inciter a revenir. Probleme : comment savoir que c'est son premier achat ? Et comment generer le coupon automatiquement ? OttoKit gere les deux.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Premier achat → coupon fidelite"]
[Clique sur le bloc trigger]
[Selectionne "WooCommerce" > "Order Completed"]
[Selectionne la connexion WordPress]
[Clique sur "Fetch Data" > "Save"]

Le trigger est "Order Completed" — pas "Order Created". On veut etre sur que le paiement est valide avant d'envoyer un coupon.

**[ECRAN — screencast ajout du Filter]**

[Clique sur "+" > selectionne "Filter"]
[Configure la condition : "Order Count" equals "1"]
[Si le champ n'existe pas directement, montre comment utiliser une Condition sur le nombre de commandes du client]

On ajoute un filtre. La condition : le client n'a qu'une seule commande. Si c'est son deuxieme ou troisieme achat, le workflow s'arrete ici. On ne veut pas envoyer un coupon a chaque commande.

**[ECRAN — screencast creation du coupon]**

[Clique sur "+" > selectionne "WooCommerce"]
[Selectionne l'action "Create Coupon"]
[Configure :]
- Code : BIENVENUE-{{order_id}}
- Type : Percentage discount
- Montant : 10
- Usage limit : 1
- Expiration : 30 jours

[Clique sur "Save"]

On cree un coupon via l'action WooCommerce "Create Coupon". Le code est unique grace au numero de commande. 10% de reduction, utilisable une seule fois, valable 30 jours. Pas de triche possible.

**[ECRAN — screencast envoi de l'email avec le coupon]**

[Clique sur "+" > selectionne "Gmail" ou "Send Email"]
[Configure :]
- To : {{billing_email}}
- Subject : -10% sur ta prochaine commande
- Body :

```
Bonjour {{billing_first_name}},

Merci pour ton premier achat chez schoolsWP !

Pour te remercier, voici un coupon de -10% :
Code : BIENVENUE-{{order_id}}

Valable 30 jours, sur ta prochaine commande.

A bientot,
L'equipe schoolsWP
```

[Clique sur "Test Action"]
[Clique sur "Save"]

L'email transmet le coupon au client. Le code est injecte dynamiquement — chaque client recoit un coupon unique.

**[ECRAN — screencast vue globale]**

[Montre le workflow complet : Trigger (Order Completed) → Filter (premier achat) → Create Coupon → Send Email]
[Active le workflow]

Le workflow complet : commande terminee → verification premier achat → creation coupon → email. Quatre etapes, zero intervention manuelle.

**[TRANSITION — face camera]**

La fidelisation automatisee, c'est ce qui fait la difference entre un site qui vend une fois et un site qui fait revenir ses clients. Prochaine lecon : on connecte TutorLMS a OttoKit pour automatiser le parcours de formation.

---

**Points cles**
- Utiliser "Order Completed" (pas "Order Created") pour s'assurer que le paiement est valide
- Le Filter verifie que c'est le premier achat avant de continuer
- Le coupon est genere avec un code unique (numero de commande)
- Usage limit = 1 et expiration = 30 jours pour eviter les abus

**Mots-cles SEO**
- OttoKit coupon automatique WooCommerce
- fidelisation automatique WordPress
- coupon premier achat WooCommerce
- automatiser coupon WordPress

---

## Lecon 8.4 — TutorLMS : inscription cours → email + tag CRM

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Un eleve s'inscrit a un cours gratuit sur ton site TutorLMS. Tu veux deux choses : lui envoyer un email de bienvenue et l'identifier dans ton CRM avec un tag. C'est le debut du parcours automatise formateur → eleve → client.

**[ECRAN — slide "Le parcours formateur schoolsWP"]**

```
Inscription gratuite → tag "lead" → email bienvenue → nurturing → achat premium → tag "client" → acces cours
```

Ce schema, c'est toute la strategie. OttoKit est le moteur qui fait avancer l'eleve d'une etape a l'autre. Aujourd'hui, on construit la premiere partie : inscription → tag → email.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Inscription TutorLMS → CRM + email"]
[Clique sur le bloc trigger]
[Selectionne "TutorLMS"]
[Selectionne l'evenement "Student Enrolled in a Course"]
[Pointe le badge "Instant"]
[Selectionne la connexion WordPress]

Le trigger TutorLMS "Student Enrolled in a Course" se declenche en temps reel. Des qu'un eleve s'inscrit, le workflow demarre.

**[ECRAN — screencast Fetch Data]**

[Clique sur "Fetch Data"]
[Montre les champs retournes : student_id, student_email, student_name, course_id, course_title, enrollment_date]
[Clique sur "Save"]

Le Fetch Data remonte les informations de l'eleve et du cours : son email, son nom, le titre du cours, la date d'inscription. Ces champs vont alimenter les actions suivantes.

**[ECRAN — screencast ajout de l'action 1 — FluentCRM tag]**

[Clique sur "+" > selectionne "FluentCRM"]
[Selectionne l'action "Add Tag to Contact"]
[Selectionne la connexion WordPress]
[Configure :]
- Contact Email : {{student_email}}
- Tag : "lead"

[Si le contact n'existe pas, montre l'option "Create if not exists"]
[Clique sur "Test Action"]
[Clique sur "Save"]

Premiere action : ajouter le tag "lead" dans FluentCRM. Si le contact existe deja, le tag s'ajoute. Sinon, OttoKit cree le contact. C'est cette option "Create if not exists" qui fait le lien automatique entre TutorLMS et FluentCRM.

**[ECRAN — screencast ajout de l'action 2 — Email bienvenue]**

[Clique sur "+" > selectionne "Gmail" ou "Send Email"]
[Configure :]
- To : {{student_email}}
- Subject : Bienvenue dans "{{course_title}}" !
- Body :

```
Bonjour {{student_name}},

Tu viens de t'inscrire a "{{course_title}}". Bravo, c'est le premier pas.

Voici comment bien demarrer :
1. Connecte-toi a ton espace : [lien]
2. Commence par la lecon 1 — elle prend 5 minutes
3. Si tu as une question, reponds a cet email

A tres vite dans le cours,
L'equipe schoolsWP
```

[Clique sur "Test Action"]
[Clique sur "Save"]

Deuxieme action : l'email de bienvenue. Le titre du cours est injecte dynamiquement. Chaque eleve recoit un message adapte au cours dans lequel il s'est inscrit.

**[ECRAN — screencast vue globale]**

[Montre le workflow complet : Trigger (Inscription TutorLMS) → FluentCRM (tag "lead") → Email bienvenue]
[Active le workflow]

Trois etapes. Chaque inscription declenche un tag CRM et un email. Ton eleve est identifie et accueilli sans que tu leves le petit doigt.

**[TRANSITION — face camera]**

L'inscription, c'est fait. Mais que se passe-t-il si un eleve s'inscrit et disparait ? Dans la prochaine lecon, on construit la relance automatique des eleves inactifs.

---

**Points cles**
- TutorLMS "Student Enrolled" est un trigger instantane
- FluentCRM "Add Tag" avec "Create if not exists" cree le lien LMS → CRM
- Le tag "lead" identifie les inscrits gratuits dans le CRM
- L'email de bienvenue utilise le titre du cours dynamiquement

**Mots-cles SEO**
- OttoKit TutorLMS integration
- automatiser inscription cours WordPress
- TutorLMS FluentCRM OttoKit
- email bienvenue automatique formation

---

## Lecon 8.5 — TutorLMS : relance des eleves inactifs

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Un eleve s'inscrit, suit une ou deux lecons, puis disparait. Ca arrive tout le temps. Le probleme, c'est que tu ne le sais pas — sauf si tu verifies manuellement. Avec OttoKit, tu peux detecter l'inactivite et relancer automatiquement.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Relance eleves inactifs TutorLMS"]
[Clique sur le bloc trigger]
[Selectionne "Schedule App"]
[Configure : Weekly, Monday, 09:00, Europe/Paris]
[Clique sur "Save"]

Ce workflow ne reagit pas a un evenement ponctuel. Il se lance chaque lundi matin et verifie qui est inactif. C'est un trigger planifie — le Schedule App.

**[ECRAN — screencast ajout de l'action 1 — Recuperer les eleves]**

[Clique sur "+" > selectionne "TutorLMS"]
[Selectionne l'action "Get Students" ou "List Enrolled Students"]
[Selectionne le cours cible]
[Clique sur "Fetch Data"]
[Montre la liste des eleves avec leurs progressions]
[Clique sur "Save"]

Premiere action : recuperer la liste des eleves inscrits au cours. OttoKit retourne chaque eleve avec sa progression.

**[ECRAN — screencast ajout du Filter]**

[Clique sur "+" > selectionne "Filter"]
[Configure la condition : "Progress" is less than "50%"]
[Ajoute une deuxieme condition : "Last Activity" is more than "7 days ago"]
[Combine en AND]
[Clique sur "Save"]

Le filtre est la cle de ce workflow. On ne veut relancer que les eleves qui ont une progression inferieure a 50% ET qui n'ont rien fait depuis plus de 7 jours. Les eleves actifs ne sont pas deranges.

**[ECRAN — screencast ajout de l'action 2 — Email de relance]**

[Clique sur "+" > selectionne "Send Email"]
[Configure :]
- To : {{student_email}}
- Subject : On t'attend dans "{{course_title}}" !
- Body :

```
Bonjour {{student_name}},

Tu as commence "{{course_title}}" il y a quelques jours et tu en es a {{progress}}%.

Il te reste encore des lecons qui valent le detour. Reprends la ou tu t'es arrete — ca prend 5 minutes.

[Bouton : Reprendre le cours]

Si tu as un blocage, reponds a cet email. On est la pour t'aider.

L'equipe schoolsWP
```

[Clique sur "Save"]

L'email de relance est personnalise. Le prenom, le titre du cours, le pourcentage de progression — tout est dynamique. L'eleve voit exactement ou il en est.

**[ECRAN — screencast vue globale]**

[Montre le workflow : Schedule (lundi 9h) → Get Students → Filter (inactifs) → Send Email]
[Active le workflow]

Chaque lundi, OttoKit recupere les eleves, filtre ceux qui sont en decrochage et envoie un email de relance cible. Tu ne fais rien — et ton taux de completion augmente.

**[TRANSITION — face camera]**

TutorLMS est connecte. Passons maintenant a FluentCRM : comment un simple tag peut declencher toute une sequence email automatique.

---

**Points cles**
- Le Schedule App lance le workflow a heure fixe (chaque lundi)
- Le filtre combine deux conditions : progression faible ET inactivite recente
- L'email de relance est personnalise avec les donnees de progression
- Ce workflow augmente le taux de completion sans travail manuel

**Mots-cles SEO**
- relance eleves inactifs TutorLMS
- OttoKit TutorLMS relance automatique
- automatiser suivi formation WordPress
- email relance cours en ligne

---

## Lecon 8.6 — FluentCRM : tag → sequence email → suivi

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Dans FluentCRM, un tag represente une action ou un statut. "lead", "client", "abandonniste", "VIP". Le vrai pouvoir, c'est quand l'ajout d'un tag declenche automatiquement une sequence d'actions. Et c'est exactement ce qu'on va construire.

**[ECRAN — slide "Le systeme de tags schoolsWP"]**

| Tag | Signification | Declencheur |
|-----|--------------|-------------|
| lead | Inscrit gratuit | Inscription TutorLMS (lecon 8.4) |
| prospect | A montre de l'interet | Visite page premium ou telechargement |
| client | A achete | Commande WooCommerce completee |
| VIP | Client fidele | 3+ achats ou panier > 200 EUR |
| inactif | Aucune activite 30j | Schedule hebdomadaire |

Chaque tag correspond a un moment du parcours client. OttoKit reagit a chaque changement de tag.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Tag prospect → sequence nurturing"]
[Clique sur le bloc trigger]
[Selectionne "FluentCRM"]
[Selectionne l'evenement "Tag Added to Contact"]
[Selectionne la connexion WordPress]
[Configure le tag : "prospect"]
[Clique sur "Fetch Data"]
[Montre les champs : contact_email, first_name, tags, lists]
[Clique sur "Save"]

Le trigger se declenche quand le tag "prospect" est ajoute a un contact FluentCRM. Peu importe comment le tag arrive — manuellement, via un autre workflow, via un formulaire. Des qu'il est pose, le workflow demarre.

**[ECRAN — screencast action 1 — Email J+0]**

[Clique sur "+" > selectionne "Send Email"]
[Configure :]
- To : {{contact_email}}
- Subject : 3 questions a te poser avant de choisir ta formation
- Body : [contenu email nurturing — conseils concrets, pas de vente directe]

[Clique sur "Save"]

Premier email : de la valeur, pas de la vente. Tu reponds a une question que le prospect se pose. C'est le debut de la sequence de nurturing.

**[ECRAN — screencast ajout du Delay]**

[Clique sur "+" > selectionne "Delay"]
[Configure : 3 jours]
[Clique sur "Save"]

On attend 3 jours. Pas d'email tous les jours — ca fatigue.

**[ECRAN — screencast action 2 — Email J+3]**

[Clique sur "+" > selectionne "Send Email"]
[Configure :]
- Subject : Le piege que 80% des formateurs WordPress font
- Body : [contenu email — erreur courante + solution]

[Clique sur "Save"]

Deuxieme email : un contenu qui montre ton expertise. Tu identifies un probleme courant et tu donnes la solution. Le prospect commence a te faire confiance.

**[ECRAN — screencast ajout d'un deuxieme Delay + action 3]**

[Clique sur "+" > Delay 4 jours]
[Clique sur "+" > Send Email]
- Subject : Pret a passer au niveau suivant ?
- Body : [contenu email — presentation de l'offre premium, lien vers la page de vente]

[Clique sur "Save"]

Troisieme email, jour 7 : cette fois tu presentes l'offre. Le prospect a recu deux emails de valeur — il est pret a entendre ta proposition.

**[ECRAN — screencast vue globale]**

[Montre le workflow complet : Tag "prospect" → Email J+0 → Delay 3j → Email J+3 → Delay 4j → Email J+7]
[Active le workflow]

Voila ta sequence de nurturing : 3 emails en 7 jours, declenchee par un simple tag. Tu peux ajouter des branches conditionelles — si le prospect ouvre l'email 2, envoyer un email different au jour 7. Mais cette version lineaire est deja tres efficace pour demarrer.

**[TRANSITION — face camera]**

Le CRM est branche. Prochaine lecon : on connecte les formulaires. Fluent Forms et SureForms vers FluentCRM et Google Sheets — en un seul workflow.

---

**Points cles**
- Le trigger FluentCRM "Tag Added" reagit a l'ajout d'un tag specifique
- Une sequence de nurturing alterne valeur et delai avant de proposer l'offre
- Le Delay App espace les emails (3-4 jours entre chaque)
- Cette sequence fonctionne en continu — chaque nouveau prospect la recoit

**Mots-cles SEO**
- OttoKit FluentCRM tag automatisation
- sequence email automatique WordPress
- nurturing automatise FluentCRM
- email marketing automation OttoKit

---

## Lecon 8.7 — Fluent Forms / SureForms : formulaire → CRM + Sheets

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Un visiteur remplit un formulaire de contact ou telecharge un guide gratuit. Tu veux que ses informations arrivent dans ton CRM, dans un Google Sheet, et qu'il recoive un email de confirmation. Trois destinations, un seul workflow.

**[ECRAN — screencast OttoKit canvas]**

[Cree un nouveau workflow : "Formulaire → CRM + Sheets + email"]
[Clique sur le bloc trigger]
[Selectionne "Fluent Forms"]
[Selectionne l'evenement "Form Submitted"]
[Selectionne la connexion WordPress]

Le trigger Fluent Forms "Form Submitted" est instantane. Des que le visiteur clique sur "Envoyer", le workflow demarre.

**[ECRAN — screencast selection du formulaire]**

[Dans les parametres du trigger, selectionne le formulaire specifique — ex: "Telecharger le guide LMS"]
[Clique sur "Fetch Data"]
[Montre les champs retournes : name, email, phone, message, form_id, form_title]
[Clique sur "Save"]

Tu choisis le formulaire exact. Les champs du formulaire deviennent les champs disponibles dans le workflow : nom, email, telephone, message.

**[ECRAN — slide "SureForms : meme logique"]**

Si tu utilises SureForms plutot que Fluent Forms, la demarche est identique. Tu selectionnes "SureForms" au lieu de "Fluent Forms", tu choisis le formulaire et l'evenement "Form Submitted". Les champs sont les memes.

**[ECRAN — screencast action 1 — FluentCRM]**

[Clique sur "+" > selectionne "FluentCRM"]
[Selectionne "Add/Update Contact"]
[Configure :]
- Email : {{email}}
- First Name : {{name}}
- Tags : "lead", "guide-lms"
- Lists : "Prospects"

[Clique sur "Test Action" > "Save"]

Premiere destination : FluentCRM. Le contact est cree avec deux tags ("lead" et "guide-lms") et ajoute a la liste "Prospects". Si le contact existe deja, ses informations sont mises a jour.

**[ECRAN — screencast action 2 — Google Sheets]**

[Clique sur "+" > selectionne "Google Sheets"]
[Selectionne "Add Row"]
[Configure le mapping :]
- Date : {{submission_date}}
- Nom : {{name}}
- Email : {{email}}
- Source : {{form_title}}

[Clique sur "Test Action" > "Save"]

Deuxieme destination : Google Sheets. Chaque soumission ajoute une ligne. Le champ "Source" indique quel formulaire a ete rempli — utile quand tu as plusieurs formulaires.

**[ECRAN — screencast action 3 — Email confirmation]**

[Clique sur "+" > selectionne "Send Email"]
[Configure :]
- To : {{email}}
- Subject : Ton guide LMS est pret
- Body :

```
Bonjour {{name}},

Merci pour ta demande. Voici ton guide :
[Lien de telechargement]

Si tu as des questions, reponds a cet email.

L'equipe schoolsWP
```

[Clique sur "Test Action" > "Save"]

Troisieme destination : l'email de confirmation avec le lien de telechargement. Le visiteur recoit son guide immediatement.

**[ECRAN — screencast vue globale]**

[Montre le workflow : Trigger (Fluent Forms) → FluentCRM → Google Sheets → Email]
[Active le workflow]

Un formulaire, trois actions. Le lead est dans ton CRM, dans ton tableur et a recu son guide. Zero travail manuel, zero oubli.

**[TRANSITION — face camera]**

On a couvert les integrations mono-site. Mais que faire si tu geres plusieurs sites WordPress ? Prochaine lecon : l'automatisation inter-sites — une specialite d'OttoKit que tu ne trouveras pas chez Zapier.

---

**Points cles**
- Fluent Forms et SureForms fonctionnent de la meme maniere avec OttoKit
- Un seul trigger peut alimenter trois destinations (CRM, Sheets, email)
- Le tag dans FluentCRM sert de marqueur pour les workflows suivants
- Le champ "Source" (form_title) permet de differencier les formulaires

**Mots-cles SEO**
- OttoKit Fluent Forms integration
- formulaire WordPress automatisation CRM
- Fluent Forms FluentCRM OttoKit
- SureForms OttoKit workflow

---

## Lecon 8.8 — Automatisation inter-sites : site A → site B

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas + deux sites WordPress

---

**[INTRO — face camera]**

Tu geres deux sites WordPress. Un site vitrine qui genere des leads, et un site de formation qui vend des cours. Quand quelqu'un remplit un formulaire sur le site vitrine, tu veux creer un compte sur le site de formation. Avec OttoKit, c'est possible — et c'est une fonctionnalite que tu ne trouveras pas chez Zapier ou Make.

**[ECRAN — slide "Architecture inter-sites"]**

```
Site A (vitrine)               Site B (formation)
  Formulaire contact     →       Creer compte utilisateur
  OttoKit plugin         →       OttoKit plugin
       ↓                              ↑
  Webhook OttoKit ──────────────→ Webhook OttoKit
```

Le principe : le site A envoie un webhook a OttoKit. Un second workflow OttoKit recoit ce webhook et execute une action sur le site B. Les deux sites sont connectes au meme compte OttoKit.

**[ECRAN — screencast OttoKit — Workflow 1 (Site A)]**

[Cree un nouveau workflow : "Site A → envoie lead vers site B"]
[Trigger : Fluent Forms > Form Submitted (site A)]
[Action : Webhook / API > Send Data to URL]
[Configure l'URL : celle du webhook du workflow 2 (on la copiera apres)]
[Configure le payload :]

```json
{
  "name": "{{name}}",
  "email": "{{email}}",
  "source": "site-vitrine"
}
```

[Clique sur "Save"]

Workflow 1, sur le site A. Le trigger detecte la soumission du formulaire. L'action envoie les donnees vers une URL webhook — celle du workflow du site B.

**[ECRAN — screencast OttoKit — Workflow 2 (Site B)]**

[Cree un nouveau workflow : "Site B → recoit lead et cree compte"]
[Trigger : Webhook / API > Receive Data from Webhook]
[Copie l'URL webhook generee]
[Retourne dans le workflow 1 et colle cette URL dans l'action "Send Data"]

La cle, c'est l'URL webhook. Le workflow 2 genere une URL. Tu la copies et tu la colles dans le workflow 1. C'est le pont entre les deux sites.

**[ECRAN — screencast configuration des actions du workflow 2]**

[Clique sur "Fetch Data" pour verifier que les donnees arrivent]
[Ajoute une action : WordPress > Create User]
[Configure :]
- Email : {{email}}
- Display Name : {{name}}
- Role : Subscriber
- Connection : site B

[Clique sur "Test Action" > "Save"]

Sur le site B, l'action cree un compte utilisateur avec les donnees recues du webhook. L'email, le nom et le role sont mappes directement.

**[ECRAN — screencast vue globale des deux workflows]**

[Montre les deux workflows cote a cote dans le dashboard OttoKit]
[Active les deux]

Deux workflows, deux sites, un seul compte OttoKit. Le formulaire sur le site A cree automatiquement un compte sur le site B. Pas de copier-coller, pas d'export CSV, pas de synchronisation manuelle.

**[ECRAN — slide "Autres cas d'usage inter-sites"]**

- **E-commerce + blog** : un achat sur la boutique ajoute un tag sur le blog
- **Site principal + sous-site evenementiel** : une inscription sur le sous-site envoie une notification au site principal
- **Multi-langue** : un nouveau contenu sur le site FR declenche une tache de traduction sur le site EN
- **Reseau de sites** : centraliser tous les leads dans un seul Google Sheet

**[TRANSITION — face camera]**

L'automatisation inter-sites, c'est un avantage majeur d'OttoKit pour les professionnels WordPress qui gerent plusieurs projets. Ce module est termine. Passe au quiz pour valider tes acquis avant d'attaquer les integrations SaaS dans le Module 9.

---

**Points cles**
- L'automatisation inter-sites utilise deux workflows relies par un webhook
- Les deux sites doivent etre connectes au meme compte OttoKit
- Le webhook transporte les donnees du site A vers le site B
- C'est une fonctionnalite unique a OttoKit — absente de Zapier et Make

**Mots-cles SEO**
- OttoKit automatisation inter-sites WordPress
- connecter deux sites WordPress OttoKit
- webhook entre sites WordPress
- synchronisation multi-sites OttoKit

---

## Notes de production — Module 8

### Captures a preparer
- WordPress admin : liste des plugins actifs (WooCommerce, TutorLMS, FluentCRM, Fluent Forms)
- OttoKit Connections : liste des plugins detectes avec badges verts
- Canvas workflow WooCommerce : trigger + 3 actions (Slack, Sheets, Email)
- Canvas workflow coupon : trigger + filter + create coupon + email
- Canvas workflow TutorLMS : trigger inscription + FluentCRM tag + email
- Canvas workflow relance : schedule + get students + filter + email
- Canvas workflow FluentCRM : tag trigger + 3 emails avec delays
- Canvas workflow formulaire : trigger Fluent Forms + FluentCRM + Sheets + email
- Canvas deux workflows inter-sites : workflow A (envoie webhook) + workflow B (recoit webhook)
- Google Sheets avec lignes ajoutees automatiquement
- Email recu dans Gmail (bienvenue, coupon, relance, guide)
- FluentCRM : contact avec tags ajoutes

### Environnement de demo
- Compte OttoKit avec plan actif
- Site WordPress schoolsWP avec tous les plugins actifs :
  - WooCommerce (au moins 2 produits, quelques commandes de test)
  - TutorLMS Pro (au moins 1 cours avec des eleves inscrits, differentes progressions)
  - FluentCRM Pro (contacts avec tags, au moins 1 liste "Prospects")
  - Fluent Forms (au moins 1 formulaire de capture avec champs nom/email)
  - SureForms (optionnel — pour montrer la compatibilite)
- Deuxieme site WordPress pour la demo inter-sites (meme compte OttoKit)
- Google Sheet "Ventes schoolsWP" avec colonnes preparees
- Compte Gmail pour les envois d'email
- Channel Slack #ventes pour les notifications

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 8.1 | 5 min |
| 8.2 | 8 min |
| 8.3 | 6 min |
| 8.4 | 7 min |
| 8.5 | 6 min |
| 8.6 | 6 min |
| 8.7 | 6 min |
| 8.8 | 6 min |
| **Total M8** | **50 min** |

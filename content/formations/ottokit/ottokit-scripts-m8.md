# Scripts vidéo — Module 8 : Intégrations WordPress : WooCommerce, LMS, CRM

**Formation** : Maîtriser OttoKit
**Module** : M8 — Intégrations WordPress : WooCommerce, LMS, CRM
**Leçons** : 8 vidéos + 1 quiz
**Durée totale** : ~50 min de vidéo
**Date** : 2026-03-30

---

## Leçon 8.1 — Connecter tes plugins WordPress à OttoKit

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit + WordPress admin

---

**[INTRO — face caméra]**

Tu as un site WordPress avec WooCommerce, TutorLMS, FluentCRM, des formulaires. Chacun de ces plugins produit des événements : une commande, une inscription, un tag ajouté. OttoKit peut réagir à tous ces événements — mais il faut d'abord qu'il les détecte.

**[ÉCRAN — screencast WordPress admin]**

[Ouvre le tableau de bord WordPress]
[Va dans Extensions > Extensions installées]
[Montre la liste des plugins actifs : WooCommerce, TutorLMS, FluentCRM, Fluent Forms, SureForms]

Voici les plugins actifs sur le site schoolsWP. Chacun est une source d'événements potentielle pour OttoKit.

**[ÉCRAN — screencast OttoKit dashboard]**

[Ouvre app.ottokit.com]
[Va dans Connections]
[Clique sur la connexion WordPress du site schoolsWP]
[Montre la liste des plugins détectés automatiquement]

Quand tu connectes ton site WordPress à OttoKit, le plugin scanne automatiquement les extensions actives. Ici, tu vois la liste de tout ce qu'OttoKit a détecté : WooCommerce, TutorLMS, FluentCRM, Fluent Forms, SureForms.

**[ÉCRAN — screencast vérification]**

[Montre un plugin détecté — ex: WooCommerce — avec un badge "Connected" ou une icône verte]
[Montre un plugin non détecté ou non supporté — ex: un plugin obscur sans icône]

Si un plugin apparaît dans la liste avec un badge vert, c'est bon. OttoKit peut utiliser ses triggers et ses actions. Si un plugin n'apparaît pas, deux raisons possibles : soit OttoKit ne le supporte pas encore, soit le plugin est désactivé.

**[ÉCRAN — slide "Les plugins WordPress les plus utilisés avec OttoKit"]**

| Plugin | Triggers | Actions | Usage |
|--------|----------|---------|-------|
| WooCommerce | Commande, produit, client | Créer coupon, modifier commande | E-commerce |
| TutorLMS | Inscription, progression, complétion | Inscrire, désinscrire | Formation |
| FluentCRM | Tag ajouté, liste, contact | Ajouter tag, envoyer email | CRM |
| Fluent Forms | Soumission formulaire | — | Formulaires |
| SureForms | Soumission formulaire | — | Formulaires |
| Elementor | Soumission formulaire | — | Page builder |
| BuddyBoss | Inscription, activité | Créer groupe | Communauté |

**[ÉCRAN — screencast ajout d'un plugin manquant]**

[Retourne dans WordPress admin]
[Active un plugin désactivé — ex: BuddyBoss]
[Reviens dans OttoKit > Connections]
[Rafraîchit la page]
[Montre le plugin qui apparaît maintenant dans la liste]

Si tu actives un nouveau plugin sur ton site, OttoKit le détecte lors de la prochaine synchronisation. Parfois, un simple rafraîchissement de la page suffit.

**[TRANSITION — face caméra]**

Tes plugins sont détectés. À partir de maintenant, on entre dans le concret. Prochaine leçon : on construit un workflow WooCommerce complet avec notification, Google Sheets et email.

---

**Points clés**
- OttoKit détecte automatiquement les plugins WordPress actifs sur ton site
- La détection se fait via le plugin OttoKit installé dans WordPress
- Si un plugin n'apparaît pas, vérifier qu'il est activé et supporté par OttoKit
- Les plugins les plus courants : WooCommerce, TutorLMS, FluentCRM, Fluent Forms

**Mots-clés SEO**
- OttoKit plugins WordPress
- connecter WooCommerce OttoKit
- OttoKit détection automatique plugins
- intégrations WordPress OttoKit

---

## Leçon 8.2 — WooCommerce : commande → notification + Sheets + email

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Un client passe commande sur ton site. Tu veux trois choses : recevoir une notification, enregistrer la vente dans un Google Sheet, et envoyer un email de remerciement personnalisé au client. Avec OttoKit, un seul workflow gère les trois.

**[ÉCRAN — screencast OttoKit canvas]**

[Ouvre OttoKit]
[Clique sur "Create Workflow"]
[Nomme le workflow : "Commande WooCommerce → notification + Sheets + email"]

On commence par nommer le workflow. Un nom clair, ça fait gagner du temps quand tu en auras vingt.

**[ÉCRAN — screencast configuration du trigger]**

[Clique sur le bloc trigger]
[Sélectionne "WooCommerce"]
[Sélectionne l'événement "Order Created"]
[Pointe le badge "Instant"]
[Sélectionne la connexion WordPress]
[Clique sur "Fetch Data"]
[Montre les champs retournés : order_id, billing_first_name, billing_email, total, line_items, status]
[Clique sur "Save"]

Le trigger est "Order Created" — instantané. Dès qu'une commande arrive, le workflow démarre. Le Fetch Data montre tous les champs disponibles : numéro de commande, nom du client, email, montant total, produits commandés.

**[ÉCRAN — screencast ajout de l'action 1 — Notification Slack/email admin]**

[Clique sur "+" pour ajouter une action]
[Sélectionne "Slack" (ou "Send Email" si pas de Slack)]
[Sélectionne l'événement "Send Channel Message"]
[Sélectionne la connexion Slack et le channel #ventes]
[Configure le message :]

```
Nouvelle commande #{{order_id}}
Client : {{billing_first_name}} {{billing_last_name}}
Montant : {{total}} EUR
```

[Clique sur "Test Action"]
[Montre le message envoyé dans Slack]
[Clique sur "Save"]

Première action : notifier l'équipe. Ici on envoie un message Slack dans le channel #ventes. Le message utilise les données du trigger : numéro de commande, nom du client, montant. Tu testes, ça fonctionne, tu enregistres.

**[ÉCRAN — screencast ajout de l'action 2 — Google Sheets]**

[Clique sur "+" pour ajouter une deuxième action]
[Sélectionne "Google Sheets"]
[Sélectionne l'événement "Add Row"]
[Sélectionne la connexion Google]
[Sélectionne le spreadsheet "Ventes schoolsWP"]
[Sélectionne la feuille "2026"]
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

Deuxième action : enregistrer la vente dans ton tableur. Tu mappes chaque colonne avec les données de la commande. Le test confirme que la ligne s'ajoute.

**[ÉCRAN — screencast ajout de l'action 3 — Email client]**

[Clique sur "+" pour ajouter une troisième action]
[Sélectionne "Gmail" ou "Send Email"]
[Configure :]
- To : {{billing_email}}
- Subject : Merci pour ta commande #{{order_id}}
- Body :

```
Bonjour {{billing_first_name}},

Merci pour ta commande sur schoolsWP !

Récapitulatif :
- Commande : #{{order_id}}
- Montant : {{total}} EUR

Tu recevras un email de suivi dès que ta commande sera expédiée.

À très vite,
L'équipe schoolsWP
```

[Clique sur "Test Action"]
[Montre l'email reçu dans Gmail]
[Clique sur "Save"]

Troisième action : envoyer un email de remerciement personnalisé. Le prénom, le numéro de commande, le montant — tout vient du trigger.

**[ÉCRAN — screencast vue globale du workflow]**

[Zoom out pour voir le workflow complet : Trigger → Slack → Sheets → Email]
[Active le workflow (bouton "Publish" ou "Activate")]

Voilà le workflow complet. Un trigger, trois actions enchaînées. Chaque commande déclenche une notification, un enregistrement et un email — automatiquement.

**[TRANSITION — face caméra]**

Ce workflow est la base de tout site e-commerce sur WordPress. Dans la prochaine leçon, on va plus loin avec WooCommerce : créer automatiquement un coupon de fidélisation après le premier achat.

---

**Points clés**
- Un seul trigger WooCommerce peut alimenter plusieurs actions en cascade
- Toujours tester chaque action individuellement avant de publier
- Les données du trigger (order_id, billing_email, total) sont réutilisables dans toutes les actions
- Ce workflow remplace 3 tâches manuelles : notification, saisie tableur, email

**Mots-clés SEO**
- OttoKit WooCommerce workflow
- automatiser commande WooCommerce
- notification vente WordPress
- Google Sheets WooCommerce automatique

---

## Leçon 8.3 — WooCommerce : coupon automatique après premier achat

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Un client achète pour la première fois. Tu veux le remercier avec un coupon de réduction pour l'inciter à revenir. Problème : comment savoir que c'est son premier achat ? Et comment générer le coupon automatiquement ? OttoKit gère les deux.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Premier achat → coupon fidélité"]
[Clique sur le bloc trigger]
[Sélectionne "WooCommerce" > "Order Completed"]
[Sélectionne la connexion WordPress]
[Clique sur "Fetch Data" > "Save"]

Le trigger est "Order Completed" — pas "Order Created". On veut être sûr que le paiement est valide avant d'envoyer un coupon.

**[ÉCRAN — screencast ajout du Filter]**

[Clique sur "+" > sélectionne "Filter"]
[Configure la condition : "Order Count" equals "1"]
[Si le champ n'existe pas directement, montre comment utiliser une Condition sur le nombre de commandes du client]

On ajoute un filtre. La condition : le client n'a qu'une seule commande. Si c'est son deuxième ou troisième achat, le workflow s'arrête ici. On ne veut pas envoyer un coupon à chaque commande.

**[ÉCRAN — screencast création du coupon]**

[Clique sur "+" > sélectionne "WooCommerce"]
[Sélectionne l'action "Create Coupon"]
[Configure :]
- Code : BIENVENUE-{{order_id}}
- Type : Percentage discount
- Montant : 10
- Usage limit : 1
- Expiration : 30 jours

[Clique sur "Save"]

On crée un coupon via l'action WooCommerce "Create Coupon". Le code est unique grâce au numéro de commande. 10% de réduction, utilisable une seule fois, valable 30 jours. Pas de triche possible.

**[ÉCRAN — screencast envoi de l'email avec le coupon]**

[Clique sur "+" > sélectionne "Gmail" ou "Send Email"]
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

À bientôt,
L'équipe schoolsWP
```

[Clique sur "Test Action"]
[Clique sur "Save"]

L'email transmet le coupon au client. Le code est injecté dynamiquement — chaque client reçoit un coupon unique.

**[ÉCRAN — screencast vue globale]**

[Montre le workflow complet : Trigger (Order Completed) → Filter (premier achat) → Create Coupon → Send Email]
[Active le workflow]

Le workflow complet : commande terminée → vérification premier achat → création coupon → email. Quatre étapes, zéro intervention manuelle.

**[TRANSITION — face caméra]**

La fidélisation automatisée, c'est ce qui fait la différence entre un site qui vend une fois et un site qui fait revenir ses clients. Prochaine leçon : on connecte TutorLMS à OttoKit pour automatiser le parcours de formation.

---

**Points clés**
- Utiliser "Order Completed" (pas "Order Created") pour s'assurer que le paiement est valide
- Le Filter vérifie que c'est le premier achat avant de continuer
- Le coupon est généré avec un code unique (numéro de commande)
- Usage limit = 1 et expiration = 30 jours pour éviter les abus

**Mots-clés SEO**
- OttoKit coupon automatique WooCommerce
- fidélisation automatique WordPress
- coupon premier achat WooCommerce
- automatiser coupon WordPress

---

## Leçon 8.4 — TutorLMS : inscription cours → email + tag CRM

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Un élève s'inscrit à un cours gratuit sur ton site TutorLMS. Tu veux deux choses : lui envoyer un email de bienvenue et l'identifier dans ton CRM avec un tag. C'est le début du parcours automatisé formateur → élève → client.

**[ÉCRAN — slide "Le parcours formateur schoolsWP"]**

```
Inscription gratuite → tag "lead" → email bienvenue → nurturing → achat premium → tag "client" → accès cours
```

Ce schéma, c'est toute la stratégie. OttoKit est le moteur qui fait avancer l'élève d'une étape à l'autre. Aujourd'hui, on construit la première partie : inscription → tag → email.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Inscription TutorLMS → CRM + email"]
[Clique sur le bloc trigger]
[Sélectionne "TutorLMS"]
[Sélectionne l'événement "Student Enrolled in a Course"]
[Pointe le badge "Instant"]
[Sélectionne la connexion WordPress]

Le trigger TutorLMS "Student Enrolled in a Course" se déclenche en temps réel. Dès qu'un élève s'inscrit, le workflow démarre.

**[ÉCRAN — screencast Fetch Data]**

[Clique sur "Fetch Data"]
[Montre les champs retournés : student_id, student_email, student_name, course_id, course_title, enrollment_date]
[Clique sur "Save"]

Le Fetch Data remonte les informations de l'élève et du cours : son email, son nom, le titre du cours, la date d'inscription. Ces champs vont alimenter les actions suivantes.

**[ÉCRAN — screencast ajout de l'action 1 — FluentCRM tag]**

[Clique sur "+" > sélectionne "FluentCRM"]
[Sélectionne l'action "Add Tag to Contact"]
[Sélectionne la connexion WordPress]
[Configure :]
- Contact Email : {{student_email}}
- Tag : "lead"

[Si le contact n'existe pas, montre l'option "Create if not exists"]
[Clique sur "Test Action"]
[Clique sur "Save"]

Première action : ajouter le tag "lead" dans FluentCRM. Si le contact existe déjà, le tag s'ajoute. Sinon, OttoKit crée le contact. C'est cette option "Create if not exists" qui fait le lien automatique entre TutorLMS et FluentCRM.

**[ÉCRAN — screencast ajout de l'action 2 — Email bienvenue]**

[Clique sur "+" > sélectionne "Gmail" ou "Send Email"]
[Configure :]
- To : {{student_email}}
- Subject : Bienvenue dans "{{course_title}}" !
- Body :

```
Bonjour {{student_name}},

Tu viens de t'inscrire à "{{course_title}}". Bravo, c'est le premier pas.

Voici comment bien démarrer :
1. Connecte-toi à ton espace : [lien]
2. Commence par la leçon 1 — elle prend 5 minutes
3. Si tu as une question, réponds à cet email

À très vite dans le cours,
L'équipe schoolsWP
```

[Clique sur "Test Action"]
[Clique sur "Save"]

Deuxième action : l'email de bienvenue. Le titre du cours est injecté dynamiquement. Chaque élève reçoit un message adapté au cours dans lequel il s'est inscrit.

**[ÉCRAN — screencast vue globale]**

[Montre le workflow complet : Trigger (Inscription TutorLMS) → FluentCRM (tag "lead") → Email bienvenue]
[Active le workflow]

Trois étapes. Chaque inscription déclenche un tag CRM et un email. Ton élève est identifié et accueilli sans que tu lèves le petit doigt.

**[TRANSITION — face caméra]**

L'inscription, c'est fait. Mais que se passe-t-il si un élève s'inscrit et disparaît ? Dans la prochaine leçon, on construit la relance automatique des élèves inactifs.

---

**Points clés**
- TutorLMS "Student Enrolled" est un trigger instantané
- FluentCRM "Add Tag" avec "Create if not exists" crée le lien LMS → CRM
- Le tag "lead" identifie les inscrits gratuits dans le CRM
- L'email de bienvenue utilise le titre du cours dynamiquement

**Mots-clés SEO**
- OttoKit TutorLMS intégration
- automatiser inscription cours WordPress
- TutorLMS FluentCRM OttoKit
- email bienvenue automatique formation

---

## Leçon 8.5 — TutorLMS : relance des élèves inactifs

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Un élève s'inscrit, suit une ou deux leçons, puis disparaît. Ça arrive tout le temps. Le problème, c'est que tu ne le sais pas — sauf si tu vérifies manuellement. Avec OttoKit, tu peux détecter l'inactivité et relancer automatiquement.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Relance élèves inactifs TutorLMS"]
[Clique sur le bloc trigger]
[Sélectionne "Schedule App"]
[Configure : Weekly, Monday, 09:00, Europe/Paris]
[Clique sur "Save"]

Ce workflow ne réagit pas à un événement ponctuel. Il se lance chaque lundi matin et vérifie qui est inactif. C'est un trigger planifié — le Schedule App.

**[ÉCRAN — screencast ajout de l'action 1 — Récupérer les élèves]**

[Clique sur "+" > sélectionne "TutorLMS"]
[Sélectionne l'action "Get Students" ou "List Enrolled Students"]
[Sélectionne le cours cible]
[Clique sur "Fetch Data"]
[Montre la liste des élèves avec leurs progressions]
[Clique sur "Save"]

Première action : récupérer la liste des élèves inscrits au cours. OttoKit retourne chaque élève avec sa progression.

**[ÉCRAN — screencast ajout du Filter]**

[Clique sur "+" > sélectionne "Filter"]
[Configure la condition : "Progress" is less than "50%"]
[Ajoute une deuxième condition : "Last Activity" is more than "7 days ago"]
[Combine en AND]
[Clique sur "Save"]

Le filtre est la clé de ce workflow. On ne veut relancer que les élèves qui ont une progression inférieure à 50% ET qui n'ont rien fait depuis plus de 7 jours. Les élèves actifs ne sont pas dérangés.

**[ÉCRAN — screencast ajout de l'action 2 — Email de relance]**

[Clique sur "+" > sélectionne "Send Email"]
[Configure :]
- To : {{student_email}}
- Subject : On t'attend dans "{{course_title}}" !
- Body :

```
Bonjour {{student_name}},

Tu as commencé "{{course_title}}" il y a quelques jours et tu en es à {{progress}}%.

Il te reste encore des leçons qui valent le détour. Reprends là où tu t'es arrêté — ça prend 5 minutes.

[Bouton : Reprendre le cours]

Si tu as un blocage, réponds à cet email. On est là pour t'aider.

L'équipe schoolsWP
```

[Clique sur "Save"]

L'email de relance est personnalisé. Le prénom, le titre du cours, le pourcentage de progression — tout est dynamique. L'élève voit exactement où il en est.

**[ÉCRAN — screencast vue globale]**

[Montre le workflow : Schedule (lundi 9h) → Get Students → Filter (inactifs) → Send Email]
[Active le workflow]

Chaque lundi, OttoKit récupère les élèves, filtre ceux qui sont en décrochage et envoie un email de relance ciblé. Tu ne fais rien — et ton taux de complétion augmente.

**[TRANSITION — face caméra]**

TutorLMS est connecté. Passons maintenant à FluentCRM : comment un simple tag peut déclencher toute une séquence email automatique.

---

**Points clés**
- Le Schedule App lance le workflow à heure fixe (chaque lundi)
- Le filtre combine deux conditions : progression faible ET inactivité récente
- L'email de relance est personnalisé avec les données de progression
- Ce workflow augmente le taux de complétion sans travail manuel

**Mots-clés SEO**
- relance élèves inactifs TutorLMS
- OttoKit TutorLMS relance automatique
- automatiser suivi formation WordPress
- email relance cours en ligne

---

## Leçon 8.6 — FluentCRM : tag → séquence email → suivi

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Dans FluentCRM, un tag représente une action ou un statut. "lead", "client", "abandonniste", "VIP". Le vrai pouvoir, c'est quand l'ajout d'un tag déclenche automatiquement une séquence d'actions. Et c'est exactement ce qu'on va construire.

**[ÉCRAN — slide "Le système de tags schoolsWP"]**

| Tag | Signification | Déclencheur |
|-----|--------------|-------------|
| lead | Inscrit gratuit | Inscription TutorLMS (leçon 8.4) |
| prospect | A montré de l'intérêt | Visite page premium ou téléchargement |
| client | A acheté | Commande WooCommerce complétée |
| VIP | Client fidèle | 3+ achats ou panier > 200 EUR |
| inactif | Aucune activité 30j | Schedule hebdomadaire |

Chaque tag correspond à un moment du parcours client. OttoKit réagit à chaque changement de tag.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Tag prospect → séquence nurturing"]
[Clique sur le bloc trigger]
[Sélectionne "FluentCRM"]
[Sélectionne l'événement "Tag Added to Contact"]
[Sélectionne la connexion WordPress]
[Configure le tag : "prospect"]
[Clique sur "Fetch Data"]
[Montre les champs : contact_email, first_name, tags, lists]
[Clique sur "Save"]

Le trigger se déclenche quand le tag "prospect" est ajouté à un contact FluentCRM. Peu importe comment le tag arrive — manuellement, via un autre workflow, via un formulaire. Dès qu'il est posé, le workflow démarre.

**[ÉCRAN — screencast action 1 — Email J+0]**

[Clique sur "+" > sélectionne "Send Email"]
[Configure :]
- To : {{contact_email}}
- Subject : 3 questions à te poser avant de choisir ta formation
- Body : [contenu email nurturing — conseils concrets, pas de vente directe]

[Clique sur "Save"]

Premier email : de la valeur, pas de la vente. Tu réponds à une question que le prospect se pose. C'est le début de la séquence de nurturing.

**[ÉCRAN — screencast ajout du Delay]**

[Clique sur "+" > sélectionne "Delay"]
[Configure : 3 jours]
[Clique sur "Save"]

On attend 3 jours. Pas d'email tous les jours — ça fatigue.

**[ÉCRAN — screencast action 2 — Email J+3]**

[Clique sur "+" > sélectionne "Send Email"]
[Configure :]
- Subject : Le piège que 80% des formateurs WordPress font
- Body : [contenu email — erreur courante + solution]

[Clique sur "Save"]

Deuxième email : un contenu qui montre ton expertise. Tu identifies un problème courant et tu donnes la solution. Le prospect commence à te faire confiance.

**[ÉCRAN — screencast ajout d'un deuxième Delay + action 3]**

[Clique sur "+" > Delay 4 jours]
[Clique sur "+" > Send Email]
- Subject : Prêt à passer au niveau suivant ?
- Body : [contenu email — présentation de l'offre premium, lien vers la page de vente]

[Clique sur "Save"]

Troisième email, jour 7 : cette fois tu présentes l'offre. Le prospect a reçu deux emails de valeur — il est prêt à entendre ta proposition.

**[ÉCRAN — screencast vue globale]**

[Montre le workflow complet : Tag "prospect" → Email J+0 → Delay 3j → Email J+3 → Delay 4j → Email J+7]
[Active le workflow]

Voilà ta séquence de nurturing : 3 emails en 7 jours, déclenchée par un simple tag. Tu peux ajouter des branches conditionnelles — si le prospect ouvre l'email 2, envoyer un email différent au jour 7. Mais cette version linéaire est déjà très efficace pour démarrer.

**[TRANSITION — face caméra]**

Le CRM est branché. Prochaine leçon : on connecte les formulaires. Fluent Forms et SureForms vers FluentCRM et Google Sheets — en un seul workflow.

---

**Points clés**
- Le trigger FluentCRM "Tag Added" réagit à l'ajout d'un tag spécifique
- Une séquence de nurturing alterne valeur et délai avant de proposer l'offre
- Le Delay App espace les emails (3-4 jours entre chaque)
- Cette séquence fonctionne en continu — chaque nouveau prospect la reçoit

**Mots-clés SEO**
- OttoKit FluentCRM tag automatisation
- séquence email automatique WordPress
- nurturing automatisé FluentCRM
- email marketing automation OttoKit

---

## Leçon 8.7 — Fluent Forms / SureForms : formulaire → CRM + Sheets

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Un visiteur remplit un formulaire de contact ou télécharge un guide gratuit. Tu veux que ses informations arrivent dans ton CRM, dans un Google Sheet, et qu'il reçoive un email de confirmation. Trois destinations, un seul workflow.

**[ÉCRAN — screencast OttoKit canvas]**

[Crée un nouveau workflow : "Formulaire → CRM + Sheets + email"]
[Clique sur le bloc trigger]
[Sélectionne "Fluent Forms"]
[Sélectionne l'événement "Form Submitted"]
[Sélectionne la connexion WordPress]

Le trigger Fluent Forms "Form Submitted" est instantané. Dès que le visiteur clique sur "Envoyer", le workflow démarre.

**[ÉCRAN — screencast sélection du formulaire]**

[Dans les paramètres du trigger, sélectionne le formulaire spécifique — ex: "Télécharger le guide LMS"]
[Clique sur "Fetch Data"]
[Montre les champs retournés : name, email, phone, message, form_id, form_title]
[Clique sur "Save"]

Tu choisis le formulaire exact. Les champs du formulaire deviennent les champs disponibles dans le workflow : nom, email, téléphone, message.

**[ÉCRAN — slide "SureForms : même logique"]**

Si tu utilises SureForms plutôt que Fluent Forms, la démarche est identique. Tu sélectionnes "SureForms" au lieu de "Fluent Forms", tu choisis le formulaire et l'événement "Form Submitted". Les champs sont les mêmes.

**[ÉCRAN — screencast action 1 — FluentCRM]**

[Clique sur "+" > sélectionne "FluentCRM"]
[Sélectionne "Add/Update Contact"]
[Configure :]
- Email : {{email}}
- First Name : {{name}}
- Tags : "lead", "guide-lms"
- Lists : "Prospects"

[Clique sur "Test Action" > "Save"]

Première destination : FluentCRM. Le contact est créé avec deux tags ("lead" et "guide-lms") et ajouté à la liste "Prospects". Si le contact existe déjà, ses informations sont mises à jour.

**[ÉCRAN — screencast action 2 — Google Sheets]**

[Clique sur "+" > sélectionne "Google Sheets"]
[Sélectionne "Add Row"]
[Configure le mapping :]
- Date : {{submission_date}}
- Nom : {{name}}
- Email : {{email}}
- Source : {{form_title}}

[Clique sur "Test Action" > "Save"]

Deuxième destination : Google Sheets. Chaque soumission ajoute une ligne. Le champ "Source" indique quel formulaire a été rempli — utile quand tu as plusieurs formulaires.

**[ÉCRAN — screencast action 3 — Email confirmation]**

[Clique sur "+" > sélectionne "Send Email"]
[Configure :]
- To : {{email}}
- Subject : Ton guide LMS est prêt
- Body :

```
Bonjour {{name}},

Merci pour ta demande. Voici ton guide :
[Lien de téléchargement]

Si tu as des questions, réponds à cet email.

L'équipe schoolsWP
```

[Clique sur "Test Action" > "Save"]

Troisième destination : l'email de confirmation avec le lien de téléchargement. Le visiteur reçoit son guide immédiatement.

**[ÉCRAN — screencast vue globale]**

[Montre le workflow : Trigger (Fluent Forms) → FluentCRM → Google Sheets → Email]
[Active le workflow]

Un formulaire, trois actions. Le lead est dans ton CRM, dans ton tableur et a reçu son guide. Zéro travail manuel, zéro oubli.

**[TRANSITION — face caméra]**

On a couvert les intégrations mono-site. Mais que faire si tu gères plusieurs sites WordPress ? Prochaine leçon : l'automatisation inter-sites — une spécialité d'OttoKit que tu ne trouveras pas chez Zapier.

---

**Points clés**
- Fluent Forms et SureForms fonctionnent de la même manière avec OttoKit
- Un seul trigger peut alimenter trois destinations (CRM, Sheets, email)
- Le tag dans FluentCRM sert de marqueur pour les workflows suivants
- Le champ "Source" (form_title) permet de différencier les formulaires

**Mots-clés SEO**
- OttoKit Fluent Forms intégration
- formulaire WordPress automatisation CRM
- Fluent Forms FluentCRM OttoKit
- SureForms OttoKit workflow

---

## Leçon 8.8 — Automatisation inter-sites : site A → site B

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas + deux sites WordPress

---

**[INTRO — face caméra]**

Tu gères deux sites WordPress. Un site vitrine qui génère des leads, et un site de formation qui vend des cours. Quand quelqu'un remplit un formulaire sur le site vitrine, tu veux créer un compte sur le site de formation. Avec OttoKit, c'est possible — et c'est une fonctionnalité que tu ne trouveras pas chez Zapier ou Make.

**[ÉCRAN — slide "Architecture inter-sites"]**

```
Site A (vitrine)               Site B (formation)
  Formulaire contact     →       Créer compte utilisateur
  OttoKit plugin         →       OttoKit plugin
       ↓                              ↑
  Webhook OttoKit ──────────────→ Webhook OttoKit
```

Le principe : le site A envoie un webhook à OttoKit. Un second workflow OttoKit reçoit ce webhook et exécute une action sur le site B. Les deux sites sont connectés au même compte OttoKit.

**[ÉCRAN — screencast OttoKit — Workflow 1 (Site A)]**

[Crée un nouveau workflow : "Site A → envoie lead vers site B"]
[Trigger : Fluent Forms > Form Submitted (site A)]
[Action : Webhook / API > Send Data to URL]
[Configure l'URL : celle du webhook du workflow 2 (on la copiera après)]
[Configure le payload :]

```json
{
  "name": "{{name}}",
  "email": "{{email}}",
  "source": "site-vitrine"
}
```

[Clique sur "Save"]

Workflow 1, sur le site A. Le trigger détecte la soumission du formulaire. L'action envoie les données vers une URL webhook — celle du workflow du site B.

**[ÉCRAN — screencast OttoKit — Workflow 2 (Site B)]**

[Crée un nouveau workflow : "Site B → reçoit lead et crée compte"]
[Trigger : Webhook / API > Receive Data from Webhook]
[Copie l'URL webhook générée]
[Retourne dans le workflow 1 et colle cette URL dans l'action "Send Data"]

La clé, c'est l'URL webhook. Le workflow 2 génère une URL. Tu la copies et tu la colles dans le workflow 1. C'est le pont entre les deux sites.

**[ÉCRAN — screencast configuration des actions du workflow 2]**

[Clique sur "Fetch Data" pour vérifier que les données arrivent]
[Ajoute une action : WordPress > Create User]
[Configure :]
- Email : {{email}}
- Display Name : {{name}}
- Role : Subscriber
- Connection : site B

[Clique sur "Test Action" > "Save"]

Sur le site B, l'action crée un compte utilisateur avec les données reçues du webhook. L'email, le nom et le rôle sont mappés directement.

**[ÉCRAN — screencast vue globale des deux workflows]**

[Montre les deux workflows côte à côte dans le dashboard OttoKit]
[Active les deux]

Deux workflows, deux sites, un seul compte OttoKit. Le formulaire sur le site A crée automatiquement un compte sur le site B. Pas de copier-coller, pas d'export CSV, pas de synchronisation manuelle.

**[ÉCRAN — slide "Autres cas d'usage inter-sites"]**

- **E-commerce + blog** : un achat sur la boutique ajoute un tag sur le blog
- **Site principal + sous-site événementiel** : une inscription sur le sous-site envoie une notification au site principal
- **Multi-langue** : un nouveau contenu sur le site FR déclenche une tâche de traduction sur le site EN
- **Réseau de sites** : centraliser tous les leads dans un seul Google Sheet

**[TRANSITION — face caméra]**

L'automatisation inter-sites, c'est un avantage majeur d'OttoKit pour les professionnels WordPress qui gèrent plusieurs projets. Ce module est terminé. Passe au quiz pour valider tes acquis avant d'attaquer les intégrations SaaS dans le Module 9.

---

**Points clés**
- L'automatisation inter-sites utilise deux workflows reliés par un webhook
- Les deux sites doivent être connectés au même compte OttoKit
- Le webhook transporte les données du site A vers le site B
- C'est une fonctionnalité unique à OttoKit — absente de Zapier et Make

**Mots-clés SEO**
- OttoKit automatisation inter-sites WordPress
- connecter deux sites WordPress OttoKit
- webhook entre sites WordPress
- synchronisation multi-sites OttoKit

---

## Notes de production — Module 8

### Captures à préparer
- WordPress admin : liste des plugins actifs (WooCommerce, TutorLMS, FluentCRM, Fluent Forms)
- OttoKit Connections : liste des plugins détectés avec badges verts
- Canvas workflow WooCommerce : trigger + 3 actions (Slack, Sheets, Email)
- Canvas workflow coupon : trigger + filter + create coupon + email
- Canvas workflow TutorLMS : trigger inscription + FluentCRM tag + email
- Canvas workflow relance : schedule + get students + filter + email
- Canvas workflow FluentCRM : tag trigger + 3 emails avec delays
- Canvas workflow formulaire : trigger Fluent Forms + FluentCRM + Sheets + email
- Canvas deux workflows inter-sites : workflow A (envoie webhook) + workflow B (reçoit webhook)
- Google Sheets avec lignes ajoutées automatiquement
- Email reçu dans Gmail (bienvenue, coupon, relance, guide)
- FluentCRM : contact avec tags ajoutés

### Environnement de démo
- Compte OttoKit avec plan actif
- Site WordPress schoolsWP avec tous les plugins actifs :
  - WooCommerce (au moins 2 produits, quelques commandes de test)
  - TutorLMS Pro (au moins 1 cours avec des élèves inscrits, différentes progressions)
  - FluentCRM Pro (contacts avec tags, au moins 1 liste "Prospects")
  - Fluent Forms (au moins 1 formulaire de capture avec champs nom/email)
  - SureForms (optionnel — pour montrer la compatibilité)
- Deuxième site WordPress pour la démo inter-sites (même compte OttoKit)
- Google Sheet "Ventes schoolsWP" avec colonnes préparées
- Compte Gmail pour les envois d'email
- Channel Slack #ventes pour les notifications

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
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

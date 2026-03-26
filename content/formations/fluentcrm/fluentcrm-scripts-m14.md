# Scripts video — Module 14 : Event tracking et comportement utilisateur

**Formation** : Maitriser FluentCRM
**Module** : M14 — Event tracking et comportement utilisateur (Premium)
**Lecons** : 5 videos + 1 exercice + 1 quiz
**Duree totale** : ~40 min
**Prerequis** : M8 (smart links), M13 (scoring avance)
**Date** : 2026-03-23

---

### Lecon 14.1 — Comprends l'event tracking : suivre ce que font tes contacts

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu sais qui sont tes contacts. Tu connais leurs tags, leurs listes, leur score. Mais tu ne sais pas ce qu'ils font sur ton site. Est-ce qu'un etudiant gratuit visite ta page de formation premium ? Est-ce qu'un prospect clique sur ton bouton d'inscription sans jamais finaliser ? L'event tracking de FluentCRM repond a ces questions. Il enregistre les actions concretes de tes contacts — pages visitees, boutons cliques, formulaires soumis — directement dans leur fiche. Dans cette lecon, tu comprends le principe et tu vois pourquoi c'est different des smart links que tu connais deja.

**[ECRAN — slide "Event tracking : definition"]**

[Montre un schema simple : visiteur sur le site > action detectee > event enregistre dans FluentCRM]

Etape 1 : l'event tracking, c'est un systeme de surveillance comportementale integre a WordPress. Chaque fois qu'un contact identifie realise une action sur ton site, FluentCRM l'enregistre comme un evenement. L'action, la date, l'heure, l'URL — tout est consigne dans la fiche du contact.

**[ECRAN — slide "4 types d'evenements"]**

[Montre les 4 types avec une icone pour chacun]

Etape 2 : FluentCRM peut tracker quatre types d'evenements.

Page view — le contact visite une page specifique. Par exemple, ta page de vente formation premium ou ta page tarifs.

Button click — le contact clique sur un element precis. Un bouton "S'inscrire", un CTA dans un article, un lien d'affiliation.

Form submission — le contact soumet un formulaire. Un formulaire de contact, une demande de devis, une inscription a un webinaire.

Custom event — un evenement sur mesure que tu definis toi-meme. Par exemple : "a regarde 80% de la video de demo" ou "a telecharge le PDF gratuit".

**[ECRAN — slide "Event tracking vs Smart links"]**

[Montre un tableau comparatif cote a cote]

Etape 3 : tu as vu les smart links dans le module 8. Ne confonds pas les deux. Les smart links trackent les clics dans tes emails — un contact clique sur un lien dans ta newsletter, tu le sais. L'event tracking, lui, traque ce qui se passe sur ton site WordPress — independamment des emails. Un contact peut arriver depuis Google, depuis un favori, depuis un lien partage sur un forum — l'event tracking le capte quand meme.

En resume : smart links = suivi des clics email. Event tracking = suivi du comportement sur site.

**[ECRAN — slide "Cas concret schoolsWP"]**

[Montre un scenario avec fleches]

Etape 4 : scenario concret. Tu as une formation gratuite sur TutorLMS et une formation premium payante. Un etudiant inscrit au gratuit visite ta page de vente premium deux fois en une semaine. Sans event tracking, tu ne le sais pas. Avec event tracking, FluentCRM enregistre chaque visite. Tu peux alors declencher une automation : envoyer un email personnalise avec un code promo ou un temoignage d'etudiant satisfait.

C'est la difference entre deviner l'intention d'un contact et la mesurer.

**[TRANSITION — face camera]**

L'event tracking transforme FluentCRM en outil d'intelligence comportementale. Tu ne te contentes plus de savoir qui sont tes contacts — tu sais ce qu'ils font. Dans la prochaine lecon, tu actives et configures le module.

---

**Points cles** :
- Event tracking = suivi des actions des contacts sur ton site WordPress
- 4 types : page view, button click, form submission, custom event
- Difference avec smart links (M8) : smart links = clics email, event tracking = comportement sur site
- Fonctionne independamment de la source de trafic (email, Google, direct)
- Cas schoolsWP : detecter un etudiant gratuit qui visite la page premium

**Mots cles SEO** : FluentCRM event tracking, suivi comportemental WordPress, tracker contacts WordPress, FluentCRM comportement utilisateur

---

### Lecon 14.2 — Active et configure le module event tracking

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

L'event tracking n'est pas active par defaut dans FluentCRM. Tu dois l'activer, configurer les parametres de base et verifier que tout fonctionne avant de creer tes evenements. Six etapes pour mettre le systeme en place.

**[ECRAN — screencast FluentCRM > Settings > Modules]**

[Navigue vers les settings de FluentCRM]

Etape 1 : va dans FluentCRM, puis Settings, puis Modules. C'est ici que tu actives ou desactives les fonctionnalites optionnelles. Cherche le module "Event Tracking" dans la liste. Il est desactive par defaut — active-le.

[Active le toggle du module Event Tracking]

Une fois active, un nouvel onglet apparait dans les settings : "Event Tracking". C'est la que tu vas configurer le comportement global du suivi.

**[ECRAN — screencast FluentCRM > Settings > Event Tracking]**

[Ouvre l'onglet Event Tracking dans les settings]

Etape 2 : configure le tracking de pages automatique. FluentCRM peut enregistrer automatiquement chaque page visitee par un contact identifie. Active l'option "Auto Page Tracking". Attention : ca genere beaucoup de donnees si ton site a beaucoup de pages. Pour commencer, active-le — tu pourras filtrer ensuite.

[Montre l'option Auto Page Tracking et son toggle]

Etape 3 : definis les pages a tracker. Plutot que de tracker toutes les pages sans distinction, concentre-toi sur les pages strategiques. FluentCRM te permet de definir des URLs specifiques ou des patterns d'URL. Par exemple :

- `/formation-premium/` — ta page de vente
- `/tarifs/` — ta page de prix
- `/inscription/` — ta page d'inscription

[Montre l'ajout d'URLs specifiques dans le champ de configuration]

Etape 4 : configure la retention des donnees. Les evenements prennent de l'espace en base de donnees. FluentCRM te permet de definir une duree de retention — 30 jours, 90 jours, 6 mois, illimitee. Pour un site de formation schoolsWP, 90 jours est un bon compromis : assez long pour analyser les parcours de conversion, pas assez pour saturer ta base.

[Montre le parametre de retention]

**[ECRAN — screencast FluentCRM > verification]**

[Ouvre une session privee ou un autre navigateur]

Etape 5 : verifie que le tracking fonctionne. Ouvre ton site dans un autre navigateur — connecte avec un compte test qui est aussi un contact FluentCRM. Visite une des pages que tu as configurees. Retourne dans FluentCRM, ouvre la fiche du contact test, et va dans l'onglet "Activities" ou "Events". Tu devrais voir l'evenement de page view apparaitre.

[Montre la fiche contact avec l'evenement enregistre]

Etape 6 : verifie l'impact sur les performances. L'event tracking ajoute un script JavaScript sur tes pages. Sur un site bien optimise, l'impact est negligeable. Mais verifie quand meme : ouvre les outils developpeur de ton navigateur, onglet Network, et verifie que le script de tracking se charge correctement sans erreur. Si tu utilises un plugin de cache, purge le cache apres l'activation.

[Montre les DevTools > Network avec le script FluentCRM]

**[TRANSITION — face camera]**

Le module est actif, les pages strategiques sont configurees, le tracking fonctionne. Maintenant, tu peux aller plus loin en creant des evenements personnalises — c'est le sujet de la prochaine lecon.

---

**Points cles** :
- Module Event Tracking a activer dans Settings > Modules
- Auto Page Tracking : active par defaut pour commencer, puis affiner avec des URLs specifiques
- Retention des donnees : 90 jours recommande pour equilibrer analyse et performance
- Toujours verifier avec un contact test apres activation
- Purger le cache si plugin de cache actif

**Mots cles SEO** : activer event tracking FluentCRM, configurer suivi comportemental FluentCRM, FluentCRM page tracking setup

---

### Lecon 14.3 — Cree des evenements personnalises (page visitee, bouton clique)

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + editeur WordPress

---

**[INTRO — face camera]**

Le tracking automatique de pages, c'est bien. Mais les evenements personnalises, c'est la ou ca devient vraiment utile. Tu definis exactement ce que tu veux surveiller : un clic sur le bouton "Acheter la formation", une visite sur ta page de checkout, un scroll jusqu'au bloc temoignages. Dans cette lecon, tu crees trois types d'evenements concrets.

**[ECRAN — screencast FluentCRM > Event Tracking > Custom Events]**

[Navigue vers la section Custom Events]

Etape 1 : va dans FluentCRM, Settings, Event Tracking, puis "Custom Events" ou "Manage Events". C'est ici que tu crees et geres tes evenements personnalises. Clique sur "Add New Event".

[Montre le formulaire de creation d'evenement]

Etape 2 : cree un evenement "Page de vente visitee". Donne-lui un nom interne clair — `page_vente_premium_visited`. Le nom interne est ce que FluentCRM utilise dans ses automations — pas d'espaces, pas d'accents, tout en minuscules avec des underscores. Ajoute un titre lisible : "A visite la page de vente premium". Selectionne le type "Page View".

[Remplit les champs du formulaire]

Etape 3 : associe l'URL. Indique l'URL de ta page de vente — par exemple `/formation-premium/`. FluentCRM va matcher cette URL. Chaque fois qu'un contact identifie visite cette page, l'evenement se declenche et s'enregistre dans sa fiche.

[Montre le champ URL et la configuration]

**[ECRAN — screencast editeur WordPress + page de vente]**

[Ouvre l'editeur de la page de vente dans WordPress]

Etape 4 : cree un evenement "Bouton CTA clique". Retourne dans Custom Events et cree un nouvel evenement : `cta_achat_premium_clicked`, titre "A clique sur Acheter Premium", type "Button Click".

[Montre la creation du deuxieme evenement]

Pour un evenement de type clic, tu dois identifier l'element HTML. FluentCRM te donne un selecteur CSS ou un attribut `data-fc-event` a ajouter a ton bouton. Ouvre ta page de vente dans l'editeur WordPress, selectionne le bouton CTA, et ajoute l'attribut dans les options avancees du bloc.

[Montre l'ajout de l'attribut data-fc-event sur le bouton dans l'editeur WordPress]

Le code ressemble a ca : `data-fc-event="cta_achat_premium_clicked"`. Quand un contact clique sur ce bouton, FluentCRM enregistre l'evenement.

**[ECRAN — screencast creation du 3e evenement]**

[Retour dans FluentCRM > Custom Events]

Etape 5 : cree un evenement "Formulaire soumis". Troisieme evenement : `form_demo_submitted`, titre "A soumis le formulaire de demo", type "Form Submission". Associe-le au formulaire concerne — FluentCRM detecte automatiquement les formulaires FluentForms si tu utilises cette extension.

[Montre l'association avec un formulaire]

**[ECRAN — slide "Convention de nommage"]**

[Montre un tableau avec les conventions]

Etape 6 : adopte une convention de nommage coherente. Tes evenements vont se multiplier — 10, 20, 50 evenements sur un site actif. Sans convention, c'est le chaos.

Structure recommandee : `element_action`. Exemples :

- `page_vente_premium_visited` — page + action
- `cta_achat_premium_clicked` — element + action
- `form_demo_submitted` — formulaire + action
- `video_demo_watched` — contenu + action

Prefixe par categorie si tu as beaucoup d'evenements : `lms_page_cours_visited`, `crm_form_contact_submitted`.

**[ECRAN — screencast verification]**

[Teste les 3 evenements en visitant la page, cliquant le bouton, soumettant le formulaire]

Etape 7 : teste chaque evenement. Avec ton contact test, visite la page de vente, clique sur le bouton CTA, soumets le formulaire de demo. Retourne dans la fiche du contact dans FluentCRM. Tu devrais voir les trois evenements dans l'historique, avec l'heure exacte de chaque action.

[Montre la fiche contact avec les 3 evenements]

**[TRANSITION — face camera]**

Tu as trois evenements personnalises en place. Chaque action de tes contacts est maintenant enregistree. Mais ces donnees ne servent a rien si tu ne les exploites pas. Dans la prochaine lecon, tu utilises ces evenements pour declencher des automations ciblees.

---

**Points cles** :
- Evenement personnalise = action specifique que tu definis et que FluentCRM enregistre
- 3 types crees : page view, button click, form submission
- Nommage interne : minuscules, underscores, format `element_action`
- Attribut `data-fc-event` sur les boutons HTML pour tracker les clics
- Toujours tester chaque evenement avec un contact test

**Mots cles SEO** : FluentCRM custom event, evenement personnalise FluentCRM, tracker clic bouton FluentCRM, event tracking WordPress

---

### Lecon 14.4 — Utilise les evenements comme triggers d'automation

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM Automations

---

**[INTRO — face camera]**

Tu enregistres des evenements. Tes contacts visitent des pages, cliquent sur des boutons, soumettent des formulaires — tout est dans FluentCRM. Maintenant, tu transformes ces donnees en actions. L'objectif : quand un contact fait quelque chose de specifique, une automation se declenche automatiquement. C'est la que l'event tracking prend toute sa valeur.

**[ECRAN — screencast FluentCRM > Automations > New Automation]**

[Cree une nouvelle automation]

Etape 1 : cree une nouvelle automation. Va dans Automations, clique sur "Create Automation". Donne-lui un nom clair — par exemple "Relance visiteur page premium". Dans la liste des triggers disponibles, cherche "Event Tracked" ou "Custom Event".

[Montre le trigger "Event Tracked" dans la liste des triggers]

C'est ce trigger qui fait le lien entre tes evenements et tes automations. Selectionne-le.

**[ECRAN — screencast configuration du trigger]**

[Configure le trigger avec l'evenement page_vente_premium_visited]

Etape 2 : configure le trigger. Selectionne l'evenement qui doit declencher l'automation — `page_vente_premium_visited`. FluentCRM te propose aussi des conditions supplementaires :

- Nombre d'occurrences : declencher apres 1 visite, 2 visites, 3 visites. Par exemple, declencher uniquement quand le contact a visite la page 2 fois — ca indique un interet reel, pas une visite accidentelle.
- Periode : les visites doivent avoir eu lieu dans les 7 derniers jours, les 30 derniers jours.

[Montre les champs de configuration : evenement, occurrences, periode]

Pour notre scenario schoolsWP : declenche l'automation quand un contact visite la page de vente premium au moins 2 fois en 7 jours.

**[ECRAN — screencast ajout des actions]**

[Ajoute les actions dans le workflow de l'automation]

Etape 3 : ajoute une condition de filtre. Avant d'envoyer quoi que ce soit, verifie que le contact n'est pas deja client premium. Ajoute un bloc "Condition" : si le contact a le tag "client-premium", il sort de l'automation. Sinon, il continue.

[Montre le bloc condition avec la verification du tag]

Etape 4 : ajoute un delai strategique. Ne reagis pas a la seconde. Le contact vient de visiter ta page — si tu envoies un email dans la minute, ca fait intrusif. Ajoute un delai de 2 heures. Le contact recoit l'email un peu plus tard, comme une coincidence bienvenue.

[Ajoute un bloc Wait de 2 heures]

Etape 5 : cree l'email de relance. Ajoute un bloc "Send Email". L'objet : "Ta prochaine etape avec schoolsWP". Le contenu : personnalise. Tu sais que le contact s'interesse a la formation premium — parle-lui directement de ce qui l'attend. Inclus un temoignage, un apercu du programme, et un lien direct vers l'inscription.

[Montre la creation de l'email avec contenu personnalise]

**[ECRAN — screencast deuxieme automation]**

[Cree une deuxieme automation]

Etape 6 : cree une deuxieme automation basee sur un clic. Nouvelle automation : "Suivi CTA abandonne". Trigger : `cta_achat_premium_clicked`. Condition : le contact n'a PAS le tag "client-premium" (il a clique sur acheter mais n'a pas finalise). Delai : 24 heures. Email : "Tu etais a deux doigts — voici ce que tu rates".

[Montre le workflow complet de la 2e automation]

C'est un abandon de panier sans panier e-commerce. Tu detectes l'intention d'achat grace a l'evenement de clic, et tu relances si la conversion n'a pas eu lieu.

**[ECRAN — slide "Event + scoring"]**

[Montre un schema event > points > score total]

Etape 7 : combine evenements et scoring. Chaque evenement peut ajouter des points au score du contact. Visite page premium : +5 points. Clic CTA achat : +10 points. Soumission formulaire demo : +15 points. Tu configures ca dans les actions de tes automations — ajoute un bloc "Add Contact Score" apres le trigger.

[Montre l'ajout du bloc scoring dans l'automation]

Resultat : un contact qui visite ta page 3 fois et clique sur le CTA accumule 25 points. Quand il depasse un seuil — par exemple 30 points — une autre automation le qualifie comme "prospect chaud" et alerte ton equipe.

**[TRANSITION — face camera]**

Tes evenements ne sont plus de simples lignes dans un historique. Ils declenchent des emails, ajoutent des scores, qualifient des prospects. C'est de l'automatisation basee sur le comportement reel, pas sur des suppositions. Dans la prochaine lecon, tu apprends a lire l'historique comportemental complet d'un contact.

---

**Points cles** :
- Trigger "Event Tracked" : lie un evenement a une automation
- Conditions d'occurrences : "au moins 2 visites en 7 jours" pour filtrer l'interet reel
- Toujours verifier que le contact n'est pas deja client avant de relancer
- Delai strategique (2h-24h) pour eviter l'effet surveillance
- Combiner evenements + scoring : chaque action = points, seuil = qualification

**Mots cles SEO** : FluentCRM automation event tracking, trigger evenement FluentCRM, automation comportementale WordPress, relance automatique FluentCRM

---

### Lecon 14.5 — Consulte l'historique comportemental d'un contact

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM fiche contact

---

**[INTRO — face camera]**

Tu as active l'event tracking, cree des evenements, monte des automations. Tout ca genere des donnees. Mais ou les consulter ? Dans la fiche de chaque contact, FluentCRM affiche une timeline comportementale complete — chaque page visitee, chaque clic, chaque evenement, avec la date et l'heure. Dans cette lecon, tu apprends a lire et exploiter cet historique.

**[ECRAN — screencast FluentCRM > Contacts > fiche contact]**

[Ouvre la fiche d'un contact avec des evenements enregistres]

Etape 1 : ouvre la fiche d'un contact. Va dans Contacts, selectionne un contact qui a de l'activite — ton contact test ou un vrai contact si tu as deja du trafic. Dans la fiche, cherche l'onglet "Activities", "Events" ou "Timeline" selon la version de FluentCRM.

[Montre l'onglet avec la timeline]

Etape 2 : lis la timeline. Chaque ligne represente une action. Tu vois le type d'evenement (page view, click, form), le nom de l'evenement, l'URL concernee, et la date/heure exacte. Les evenements les plus recents sont en haut.

[Scrolle la timeline en montrant differents types d'evenements]

Ce que tu lis ici, c'est le parcours reel du contact sur ton site. Pas ce que tu imagines qu'il fait — ce qu'il fait vraiment.

**[ECRAN — screencast analyse d'un parcours]**

[Montre un contact avec un parcours type : 3 visites page premium, 1 clic CTA, 1 email recu]

Etape 3 : analyse un parcours concret. Regarde ce contact. Le 15 mars, il visite ta page d'accueil. Le 17, il visite la page formation gratuite. Le 18, il visite la page formation premium. Le 19, il y retourne. Le 20, il clique sur le CTA "Acheter". Le 21, il recoit l'email de relance automatique.

Tu vois le cheminement : curiosite > exploration > interet > intention d'achat. Sans l'event tracking, tu n'aurais vu que l'email envoye. Avec, tu comprends tout le contexte.

**[ECRAN — screencast filtrage de la timeline]**

[Montre les filtres disponibles sur la timeline]

Etape 4 : filtre la timeline. Sur un contact actif, la timeline peut contenir des dizaines d'evenements. Utilise les filtres pour te concentrer sur ce qui compte. Filtre par type d'evenement — uniquement les page views, uniquement les clics. Filtre par periode — les 7 derniers jours, le dernier mois. Filtre par evenement specifique — uniquement les visites de la page premium.

[Applique un filtre et montre le resultat]

**[ECRAN — screencast vue globale contacts]**

[Retourne dans la liste des contacts, montre les colonnes de tri]

Etape 5 : utilise les evenements pour segmenter ta liste. Au-dela de la fiche individuelle, tu peux creer des segments bases sur les evenements. Va dans Contacts, utilise les filtres avances, et selectionne "Has Event" comme critere. Tu peux chercher tous les contacts qui ont visite ta page premium au moins une fois, ou ceux qui ont clique sur le CTA sans acheter.

[Montre la creation d'un segment avec un filtre evenement]

C'est un outil puissant pour identifier des groupes de contacts par comportement — pas seulement par tags ou listes.

**[TRANSITION — face camera]**

L'historique comportemental est la piece qui relie tout : les evenements que tu as crees, les automations que tu as montees, et la comprehension de chaque contact. Tu sais maintenant ou regarder et comment lire ces donnees. Dans l'exercice suivant, tu mets tout en pratique de bout en bout.

---

**Points cles** :
- Timeline comportementale dans la fiche de chaque contact (onglet Activities/Events)
- Chaque evenement : type, nom, URL, date/heure
- Lire un parcours = comprendre le cheminement reel du contact
- Filtres disponibles : par type, par periode, par evenement specifique
- Segmentation avancee : creer des segments bases sur les evenements

**Mots cles SEO** : historique comportemental FluentCRM, timeline contact FluentCRM, suivi activite contact WordPress, segmentation comportementale FluentCRM

---

### Lecon 14.6 — Exercice : configure le tracking de ta page de vente et declenche une relance

**Duree** : 5 min
**Type** : Exercice guide
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM + WordPress

---

**[INTRO — face camera]**

Exercice pratique. Tu vas configurer le tracking complet de ta page de vente — de l'evenement jusqu'a l'email de relance automatique. Cinq etapes. A la fin, un visiteur qui revient deux fois sur ta page de vente recoit un email personnalise 2 heures plus tard.

**[ECRAN — slide "Objectif de l'exercice"]**

[Montre le schema : page visitee 2x > event > automation > delai 2h > email relance]

Voici ce que tu vas construire. Un contact visite ta page de vente (ou une page strategique de ton site) deux fois en 7 jours. FluentCRM detecte ce comportement, attend 2 heures, et envoie un email de relance personnalise. Si le contact est deja client, rien ne se passe.

**[ECRAN — screencast etape par etape]**

[Montre chaque etape avec le resultat attendu]

Etape 1 : cree l'evenement. Va dans Settings > Event Tracking > Custom Events. Cree un evenement `page_vente_visited`, titre "A visite la page de vente", type "Page View", URL : l'adresse de ta page de vente. Si tu n'as pas de page de vente, utilise ta page "A propos" ou ta page "Tarifs" pour l'exercice.

Etape 2 : ajoute le tracking de clic sur le CTA. Cree un deuxieme evenement `cta_vente_clicked`, titre "A clique sur le CTA de vente", type "Button Click". Ouvre ta page dans l'editeur WordPress et ajoute l'attribut `data-fc-event="cta_vente_clicked"` sur ton bouton principal.

Etape 3 : cree l'automation de relance. Va dans Automations, cree "Relance page de vente". Trigger : "Event Tracked", evenement `page_vente_visited`, occurrences minimum : 2, periode : 7 jours. Ajoute une condition : si tag "client-premium" existe, sortie. Sinon, delai 2 heures, puis email de relance.

Etape 4 : redige l'email. Objet : "J'ai remarque que tu t'interesses a [nom de ton offre]". Contenu : rappel de la valeur de l'offre, un temoignage, un lien direct vers l'inscription. Garde un ton naturel — pas de pression, pas d'urgence artificielle.

Etape 5 : teste le parcours complet. Connecte-toi avec ton contact test. Visite ta page de vente deux fois (en espaçant de quelques minutes). Retourne dans FluentCRM : verifie que les evenements apparaissent dans la fiche du contact, et que l'automation s'est declenchee. Verifie que l'email est en file d'attente ou envoye.

**[TRANSITION — face camera]**

Si tout fonctionne, tu as un systeme de relance comportementale complet. Chaque visiteur interesse recoit un suivi personnalise, automatiquement, sans que tu interviennes. C'est exactement le type de systeme que tu peux dupliquer pour chaque page strategique de ton site.

---

**Checklist de validation** :
- [ ] Evenement `page_vente_visited` cree et associe a l'URL
- [ ] Evenement `cta_vente_clicked` cree et attribut HTML ajoute au bouton
- [ ] Automation "Relance page de vente" creee avec trigger event (2 occurrences, 7 jours)
- [ ] Condition d'exclusion des clients existants en place
- [ ] Delai de 2 heures configure
- [ ] Email de relance redige et personnalise
- [ ] Test complet avec contact test : evenements enregistres + automation declenchee

---

### Lecon 14.7 — Quiz : valide tes acquis M14

**Duree** : 5 min
**Type** : Quiz (8 QCM)

---

**Question 1** : Quelle est la difference principale entre les smart links (M8) et l'event tracking (M14) ?

A) Les smart links sont gratuits, l'event tracking est payant
B) Les smart links trackent les clics dans les emails, l'event tracking suit le comportement sur le site
C) Les smart links sont plus precis que l'event tracking
D) Il n'y a pas de difference, ce sont deux noms pour la meme fonctionnalite

**Reponse** : B — Les smart links suivent les clics dans tes emails. L'event tracking suit ce que font tes contacts sur ton site WordPress, quelle que soit la source de trafic.

---

**Question 2** : Quel type d'evenement utilises-tu pour savoir si un contact a visite ta page de tarifs ?

A) Button Click
B) Form Submission
C) Page View
D) Custom Event

**Reponse** : C — Un evenement de type Page View enregistre la visite d'une page specifique par un contact identifie.

---

**Question 3** : Quelle convention de nommage est recommandee pour les evenements personnalises ?

A) Noms en francais avec espaces : "A visite la page premium"
B) Noms en camelCase : pageVentePremiumVisited
C) Noms en minuscules avec underscores : page_vente_premium_visited
D) Noms en majuscules : PAGE_VENTE_PREMIUM_VISITED

**Reponse** : C — Minuscules avec underscores, format `element_action`. Coherent, lisible, et compatible avec tous les systemes.

---

**Question 4** : Pourquoi ajouter un delai de 2 heures entre un evenement et l'email de relance ?

A) FluentCRM a besoin de 2 heures pour traiter l'evenement
B) Pour eviter l'effet surveillance et paraitre naturel
C) Pour laisser le temps au contact de revenir sur la page
D) C'est le delai minimum impose par FluentCRM

**Reponse** : B — Un email envoye dans la minute apres une visite donne l'impression d'etre surveille. Un delai de quelques heures rend l'email naturel.

---

**Question 5** : Quel attribut HTML ajoutes-tu a un bouton pour tracker son clic avec FluentCRM ?

A) `onclick="fluentcrm_track()"`
B) `class="fc-track-click"`
C) `data-fc-event="nom_evenement"`
D) `id="fluentcrm-button"`

**Reponse** : C — L'attribut `data-fc-event` avec le nom de l'evenement permet a FluentCRM de detecter le clic sur l'element.

---

**Question 6** : Tu veux declencher une automation uniquement quand un contact visite ta page premium au moins 2 fois en 7 jours. Ou configures-tu ca ?

A) Dans les settings globaux de l'event tracking
B) Dans le trigger de l'automation (occurrences et periode)
C) Dans un bloc condition a l'interieur de l'automation
D) Dans la fiche du contact, onglet Events

**Reponse** : B — Le trigger "Event Tracked" de l'automation permet de definir le nombre minimum d'occurrences et la periode.

---

**Question 7** : Quel est l'interet de combiner event tracking et scoring ?

A) Augmenter la vitesse de chargement du site
B) Quantifier l'engagement reel et qualifier les contacts par comportement
C) Remplacer les tags et les listes par un systeme unique
D) Envoyer plus d'emails automatiques

**Reponse** : B — Chaque evenement ajoute des points au score. Un contact qui accumule des points sur des pages strategiques est objectivement plus engage — tu le qualifies par ses actions, pas par des suppositions.

---

**Question 8** : Un contact test visite ta page de vente, mais l'evenement n'apparait pas dans sa fiche FluentCRM. Quelle est la premiere chose a verifier ?

A) Que le contact a un score superieur a 10
B) Que le contact est bien identifie (connecte a WordPress) et que le module Event Tracking est actif
C) Que le contact a un tag "tracking-actif"
D) Que l'automation associee est en mode "Active"

**Reponse** : B — L'event tracking ne fonctionne que pour les contacts identifies (connectes). Verifie aussi que le module est bien active dans Settings > Modules.

---

**Bareme** :
- 8/8 : Module maitrise
- 6-7/8 : Bonne comprehension, relis les points manques
- 4-5/8 : Revois les lecons 14.1 a 14.5
- <4/8 : Reprends le module depuis le debut

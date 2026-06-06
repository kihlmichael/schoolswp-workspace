# Scripts vidéo - Module 14 : Event tracking et comportement utilisateur

**Formation** : Maîtriser FluentCRM
**Module** : M14 - Event tracking et comportement utilisateur (Premium)
**Leçons** : 5 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~40 min
**Prérequis** : M8 (smart links), M13 (scoring avancé)
**Date** : 2026-03-23

---

### Leçon 14.1 : Comprends l'event tracking : suivre ce que font tes contacts

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO - face caméra]**

Tu sais qui sont tes contacts. Tu connais leurs tags, leurs listes, leur score. Mais tu ne sais pas ce qu'ils font sur ton site. Est-ce qu'un étudiant gratuit visite ta page de formation premium ? Est-ce qu'un prospect clique sur ton bouton d'inscription sans jamais finaliser ? L'event tracking de FluentCRM répond à ces questions. Il enregistre les actions concrètes de tes contacts - pages visitées, boutons cliqués, formulaires soumis - directement dans leur fiche. Dans cette leçon, tu comprends le principe et tu vois pourquoi c'est différent des smart links que tu connais déjà.

**[ÉCRAN - slide "Event tracking : définition"]**

[Montre un schéma simple : visiteur sur le site > action détectée > event enregistré dans FluentCRM]

Étape 1 : l'event tracking, c'est un système de surveillance comportementale intégré à WordPress. Chaque fois qu'un contact identifié réalise une action sur ton site, FluentCRM l'enregistre comme un événement. L'action, la date, l'heure, l'URL - tout est consigné dans la fiche du contact.

**[ÉCRAN - slide "4 types d'événements"]**

[Montre les 4 types avec une icône pour chacun]

Étape 2 : FluentCRM peut tracker quatre types d'événements.

Page view - le contact visite une page spécifique. Par exemple, ta page de vente formation premium ou ta page tarifs.

Button click - le contact clique sur un élément précis. Un bouton "S'inscrire", un CTA dans un article, un lien d'affiliation.

Form submission - le contact soumet un formulaire. Un formulaire de contact, une demande de devis, une inscription à un webinaire.

Custom event - un événement sur mesure que tu définis toi-même. Par exemple : "a regardé 80% de la vidéo de démo" ou "a téléchargé le PDF gratuit".

**[ÉCRAN - slide "Event tracking vs Smart links"]**

[Montre un tableau comparatif côte à côte]

Étape 3 : tu as vu les smart links dans le module 8. Ne confonds pas les deux. Les smart links trackent les clics dans tes emails - un contact clique sur un lien dans ta newsletter, tu le sais. L'event tracking, lui, traque ce qui se passe sur ton site WordPress - indépendamment des emails. Un contact peut arriver depuis Google, depuis un favori, depuis un lien partagé sur un forum - l'event tracking le capte quand même.

En résumé : smart links = suivi des clics email. Event tracking = suivi du comportement sur site.

**[ÉCRAN - slide "Cas concret schoolsWP"]**

[Montre un scénario avec fleches]

Étape 4 : scénario concret. Tu as une formation gratuite sur TutorLMS et une formation premium payante. Un étudiant inscrit au gratuit visite ta page de vente premium deux fois en une semaine. Sans event tracking, tu ne le sais pas. Avec event tracking, FluentCRM enregistre chaque visite. Tu peux alors déclencher une automation : envoyer un email personnalisé avec un code promo ou un témoignage d'étudiant satisfait.

C'est la différence entre deviner l'intention d'un contact et la mesurer.

**[TRANSITION - face caméra]**

L'event tracking transforme FluentCRM en outil d'intelligence comportementale. Tu ne te contentes plus de savoir qui sont tes contacts - tu sais ce qu'ils font. Dans la prochaine leçon, tu actives et configures le module.

---

**Points clés** :
- Event tracking = suivi des actions des contacts sur ton site WordPress
- 4 types : page view, button click, form submission, custom event
- Différence avec smart links (M8) : smart links = clics email, event tracking = comportement sur site
- Fonctionne indépendamment de la source de trafic (email, Google, direct)
- Cas schoolsWP : détecter un étudiant gratuit qui visite la page premium

**Mots clés SEO** : FluentCRM event tracking, suivi comportemental WordPress, tracker contacts WordPress, FluentCRM comportement utilisateur

---

### Leçon 14.2 : Active et configure le module event tracking

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO - face caméra]**

L'event tracking n'est pas activé par défaut dans FluentCRM. Tu dois l'activer, configurer les paramètres de base et vérifier que tout fonctionne avant de créer tes événements. Six étapes pour mettre le système en place.

**[ÉCRAN - screencast FluentCRM > Settings > Modules]**

[Navigue vers les settings de FluentCRM]

Étape 1 : va dans FluentCRM, puis Settings, puis Modules. C'est ici que tu actives ou désactives les fonctionnalités optionnelles. Cherche le module "Event Tracking" dans la liste. Il est désactivé par défaut - active-le.

[Active le toggle du module Event Tracking]

Une fois activé, un nouvel onglet apparaît dans les settings : "Event Tracking". C'est là que tu vas configurer le comportement global du suivi.

**[ÉCRAN - screencast FluentCRM > Settings > Event Tracking]**

[Ouvre l'onglet Event Tracking dans les settings]

Étape 2 : configure le tracking de pages automatique. FluentCRM peut enregistrer automatiquement chaque page visitée par un contact identifié. Active l'option "Auto Page Tracking". Attention : ça génère beaucoup de données si ton site a beaucoup de pages. Pour commencer, active-le - tu pourras filtrer ensuite.

[Montre l'option Auto Page Tracking et son toggle]

Étape 3 : définis les pages à tracker. Plutôt que de tracker toutes les pages sans distinction, concentre-toi sur les pages stratégiques. FluentCRM te permet de définir des URLs spécifiques ou des patterns d'URL. Par exemple :

- `/formation-premium/` - ta page de vente
- `/tarifs/` - ta page de prix
- `/inscription/` - ta page d'inscription

[Montre l'ajout d'URLs spécifiques dans le champ de configuration]

Étape 4 : configure la rétention des données. Les événements prennent de l'espace en base de données. FluentCRM te permet de définir une durée de rétention - 30 jours, 90 jours, 6 mois, illimitée. Pour un site de formation schoolsWP, 90 jours est un bon compromis : assez long pour analyser les parcours de conversion, pas assez pour saturer ta base.

[Montre le paramètre de rétention]

**[ÉCRAN - screencast FluentCRM > vérification]**

[Ouvre une session privée ou un autre navigateur]

Étape 5 : vérifie que le tracking fonctionne. Ouvre ton site dans un autre navigateur - connecté avec un compte test qui est aussi un contact FluentCRM. Visite une des pages que tu as configurées. Retourne dans FluentCRM, ouvre la fiche du contact test, et va dans l'onglet "Activities" ou "Events". Tu devrais voir l'événement de page view apparaître.

[Montre la fiche contact avec l'événement enregistré]

Étape 6 : vérifie l'impact sur les performances. L'event tracking ajoute un script JavaScript sur tes pages. Sur un site bien optimisé, l'impact est négligeable. Mais vérifie quand même : ouvre les outils développeur de ton navigateur, onglet Network, et vérifie que le script de tracking se charge correctement sans erreur. Si tu utilises un plugin de cache, purge le cache après l'activation.

[Montre les DevTools > Network avec le script FluentCRM]

**[TRANSITION - face caméra]**

Le module est actif, les pages stratégiques sont configurées, le tracking fonctionne. Maintenant, tu peux aller plus loin en créant des événements personnalisés - c'est le sujet de la prochaine leçon.

---

**Points clés** :
- Module Event Tracking à activer dans Settings > Modules
- Auto Page Tracking : activé par défaut pour commencer, puis affiner avec des URLs spécifiques
- Rétention des données : 90 jours recommandé pour équilibrer analyse et performance
- Toujours vérifier avec un contact test après activation
- Purger le cache si plugin de cache actif

**Mots clés SEO** : activer event tracking FluentCRM, configurer suivi comportemental FluentCRM, FluentCRM page tracking setup

---

### Leçon 14.3 : Crée des événements personnalisés (page visitée, bouton cliqué)

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + éditeur WordPress

---

**[INTRO - face caméra]**

Le tracking automatique de pages, c'est bien. Mais les événements personnalisés, c'est là où ça devient vraiment utile. Tu définis exactement ce que tu veux surveiller : un clic sur le bouton "Acheter la formation", une visite sur ta page de checkout, un scroll jusqu'au bloc témoignages. Dans cette leçon, tu crées trois types d'événements concrets.

**[ÉCRAN - screencast FluentCRM > Event Tracking > Custom Events]**

[Navigue vers la section Custom Events]

Étape 1 : va dans FluentCRM, Settings, Event Tracking, puis "Custom Events" ou "Manage Events". C'est ici que tu crées et gères tes événements personnalisés. Clique sur "Add New Event".

[Montre le formulaire de création d'événement]

Étape 2 : crée un événement "Page de vente visitée". Donne-lui un nom interne clair - `page_vente_premium_visited`. Le nom interne est ce que FluentCRM utilise dans ses automations - pas d'espaces, pas d'accents, tout en minuscules avec des underscores. Ajoute un titre lisible : "A visité la page de vente premium". Sélectionne le type "Page View".

[Remplit les champs du formulaire]

Étape 3 : associe l'URL. Indique l'URL de ta page de vente - par exemple `/formation-premium/`. FluentCRM va matcher cette URL. Chaque fois qu'un contact identifié visite cette page, l'événement se déclenche et s'enregistre dans sa fiche.

[Montre le champ URL et la configuration]

**[ÉCRAN - screencast éditeur WordPress + page de vente]**

[Ouvre l'éditeur de la page de vente dans WordPress]

Étape 4 : crée un événement "Bouton CTA cliqué". Retourne dans Custom Events et crée un nouvel événement : `cta_achat_premium_clicked`, titre "A cliqué sur Acheter Premium", type "Button Click".

[Montre la création du deuxième événement]

Pour un événement de type clic, tu dois identifier l'élément HTML. FluentCRM te donne un sélecteur CSS ou un attribut `data-fc-event` à ajouter à ton bouton. Ouvre ta page de vente dans l'éditeur WordPress, sélectionne le bouton CTA, et ajoute l'attribut dans les options avancées du bloc.

[Montre l'ajout de l'attribut data-fc-event sur le bouton dans l'éditeur WordPress]

Le code ressemble à ça : `data-fc-event="cta_achat_premium_clicked"`. Quand un contact clique sur ce bouton, FluentCRM enregistre l'événement.

**[ÉCRAN - screencast création du 3e événement]**

[Retour dans FluentCRM > Custom Events]

Étape 5 : crée un événement "Formulaire soumis". Troisième événement : `form_demo_submitted`, titre "A soumis le formulaire de démo", type "Form Submission". Associe-le au formulaire concerné - FluentCRM détecte automatiquement les formulaires FluentForms si tu utilises cette extension.

[Montre l'association avec un formulaire]

**[ÉCRAN - slide "Convention de nommage"]**

[Montre un tableau avec les conventions]

Étape 6 : adopte une convention de nommage cohérente. Tes événements vont se multiplier - 10, 20, 50 événements sur un site actif. Sans convention, c'est le chaos.

Structure recommandée : `element_action`. Exemples :

- `page_vente_premium_visited` - page + action
- `cta_achat_premium_clicked` - élément + action
- `form_demo_submitted` - formulaire + action
- `vidéo_demo_watched` - contenu + action

Préfixe par catégorie si tu as beaucoup d'événements : `lms_page_cours_visited`, `crm_form_contact_submitted`.

**[ÉCRAN - screencast vérification]**

[Teste les 3 événements en visitant la page, cliquant le bouton, soumettant le formulaire]

Étape 7 : teste chaque événement. Avec ton contact test, visite la page de vente, clique sur le bouton CTA, soumets le formulaire de démo. Retourne dans la fiche du contact dans FluentCRM. Tu devrais voir les trois événements dans l'historique, avec l'heure exacte de chaque action.

[Montre la fiche contact avec les 3 événements]

**[TRANSITION - face caméra]**

Tu as trois événements personnalisés en place. Chaque action de tes contacts est maintenant enregistrée. Mais ces données ne servent à rien si tu ne les exploites pas. Dans la prochaine leçon, tu utilises ces événements pour déclencher des automations ciblées.

---

**Points clés** :
- Événement personnalisé = action spécifique que tu définis et que FluentCRM enregistre
- 3 types créés : page view, button click, form submission
- Nommage interne : minuscules, underscores, format `element_action`
- Attribut `data-fc-event` sur les boutons HTML pour tracker les clics
- Toujours tester chaque événement avec un contact test

**Mots clés SEO** : FluentCRM custom event, événement personnalisé FluentCRM, tracker clic bouton FluentCRM, event tracking WordPress

---

### Leçon 14.4 : Utilise les événements comme triggers d'automation

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM Automations

---

**[INTRO - face caméra]**

Tu enregistres des événements. Tes contacts visitent des pages, cliquent sur des boutons, soumettent des formulaires - tout est dans FluentCRM. Maintenant, tu transformes ces données en actions. L'objectif : quand un contact fait quelque chose de spécifique, une automation se déclenche automatiquement. C'est là que l'event tracking prend toute sa valeur.

**[ÉCRAN - screencast FluentCRM > Automations > New Automation]**

[Crée une nouvelle automation]

Étape 1 : crée une nouvelle automation. Va dans Automations, clique sur "Create Automation". Donne-lui un nom clair - par exemple "Relance visiteur page premium". Dans la liste des triggers disponibles, cherche "Event Tracked" ou "Custom Event".

[Montre le trigger "Event Tracked" dans la liste des triggers]

C'est ce trigger qui fait le lien entre tes événements et tes automations. Sélectionne-le.

**[ÉCRAN - screencast configuration du trigger]**

[Configure le trigger avec l'événement page_vente_premium_visited]

Étape 2 : configure le trigger. Sélectionne l'événement qui doit déclencher l'automation - `page_vente_premium_visited`. FluentCRM te propose aussi des conditions supplémentaires :

- Nombre d'occurrences : déclencher après 1 visite, 2 visites, 3 visites. Par exemple, déclencher uniquement quand le contact a visité la page 2 fois - ça indique un intérêt réel, pas une visite accidentelle.
- Période : les visites doivent avoir eu lieu dans les 7 derniers jours, les 30 derniers jours.

[Montre les champs de configuration : événement, occurrences, période]

Pour notre scénario schoolsWP : déclenche l'automation quand un contact visite la page de vente premium au moins 2 fois en 7 jours.

**[ÉCRAN - screencast ajout des actions]**

[Ajoute les actions dans le workflow de l'automation]

Étape 3 : ajoute une condition de filtre. Avant d'envoyer quoi que ce soit, vérifie que le contact n'est pas déjà client premium. Ajoute un bloc "Condition" : si le contact a le tag "client-premium", il sort de l'automation. Sinon, il continue.

[Montre le bloc condition avec la vérification du tag]

Étape 4 : ajoute un délai stratégique. Ne réagis pas à la seconde. Le contact vient de visiter ta page - si tu envoies un email dans la minute, ça fait intrusif. Ajoute un délai de 2 heures. Le contact reçoit l'email un peu plus tard, comme une coïncidence bienvenue.

[Ajoute un bloc Wait de 2 heures]

Étape 5 : crée l'email de relance. Ajoute un bloc "Send Email". L'objet : "Ta prochaine étape avec schoolsWP". Le contenu : personnalisé. Tu sais que le contact s'intéresse à la formation premium - parle-lui directement de ce qui l'attend. Inclus un témoignage, un aperçu du programme, et un lien direct vers l'inscription.

[Montre la création de l'email avec contenu personnalisé]

**[ÉCRAN - screencast deuxième automation]**

[Crée une deuxième automation]

Étape 6 : crée une deuxième automation basée sur un clic. Nouvelle automation : "Suivi CTA abandonné". Trigger : `cta_achat_premium_clicked`. Condition : le contact n'a PAS le tag "client-premium" (il a cliqué sur acheter mais n'a pas finalisé). Délai : 24 heures. Email : "Tu étais à deux doigts - voici ce que tu rates".

[Montre le workflow complet de la 2e automation]

C'est un abandon de panier sans panier e-commerce. Tu détectes l'intention d'achat grace a l'événement de clic, et tu relances si la conversion n'a pas eu lieu.

**[ÉCRAN - slide "Event + scoring"]**

[Montre un schéma event > points > score total]

Étape 7 : combine événements et scoring. Chaque événement peut ajouter des points au score du contact. Visite page premium : +5 points. Clic CTA achat : +10 points. Soumission formulaire démo : +15 points. Tu configures ça dans les actions de tes automations - ajoute un bloc "Add Contact Score" après le trigger.

[Montre l'ajout du bloc scoring dans l'automation]

Résultat : un contact qui visite ta page 3 fois et clique sur le CTA accumule 25 points. Quand il dépasse un seuil - par exemple 30 points - une autre automation le qualifie comme "prospect chaud" et alerte ton équipe.

**[TRANSITION - face caméra]**

Tes événements ne sont plus de simples lignes dans un historique. Ils déclenchent des emails, ajoutent des scores, qualifient des prospects. C'est de l'automatisation basée sur le comportement réel, pas sur des suppositions. Dans la prochaine leçon, tu apprends à lire l'historique comportemental complet d'un contact.

---

**Points clés** :
- Trigger "Event Tracked" : lie un événement à une automation
- Conditions d'occurrences : "au moins 2 visites en 7 jours" pour filtrer l'intérêt réel
- Toujours vérifier que le contact n'est pas déjà client avant de relancer
- Délai stratégique (2h-24h) pour éviter l'effet surveillance
- Combiner événements + scoring : chaque action = points, seuil = qualification

**Mots clés SEO** : FluentCRM automation event tracking, trigger événement FluentCRM, automation comportementale WordPress, relance automatique FluentCRM

---

### Leçon 14.5 : Consulte l'historique comportemental d'un contact

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM fiche contact

---

**[INTRO - face caméra]**

Tu as activé l'event tracking, créé des événements, monté des automations. Tout ça génère des données. Mais où les consulter ? Dans la fiche de chaque contact, FluentCRM affiche une timeline comportementale complète - chaque page visitée, chaque clic, chaque événement, avec la date et l'heure. Dans cette leçon, tu apprends à lire et exploiter cet historique.

**[ÉCRAN - screencast FluentCRM > Contacts > fiche contact]**

[Ouvre la fiche d'un contact avec des événements enregistrés]

Étape 1 : ouvre la fiche d'un contact. Va dans Contacts, sélectionne un contact qui a de l'activité - ton contact test ou un vrai contact si tu as déjà du trafic. Dans la fiche, cherche l'onglet "Activities", "Events" ou "Timeline" selon la version de FluentCRM.

[Montre l'onglet avec la timeline]

Étape 2 : lis la timeline. Chaque ligne représente une action. Tu vois le type d'événement (page view, click, form), le nom de l'événement, l'URL concernée, et la date/heure exacte. Les événements les plus récents sont en haut.

[Scrolle la timeline en montrant différents types d'événements]

Ce que tu lis ici, c'est le parcours réel du contact sur ton site. Pas ce que tu imagines qu'il fait - ce qu'il fait vraiment.

**[ÉCRAN - screencast analyse d'un parcours]**

[Montre un contact avec un parcours type : 3 visites page premium, 1 clic CTA, 1 email reçu]

Étape 3 : analyse un parcours concret. Regarde ce contact. Le 15 mars, il visite ta page d'accueil. Le 17, il visite la page formation gratuite. Le 18, il visite la page formation premium. Le 19, il y retourne. Le 20, il clique sur le CTA "Acheter". Le 21, il reçoit l'email de relance automatique.

Tu vois le cheminement : curiosité > exploration > intérêt > intention d'achat. Sans l'event tracking, tu n'aurais vu que l'email envoyé. Avec, tu comprends tout le contexte.

**[ÉCRAN - screencast filtrage de la timeline]**

[Montre les filtres disponibles sur la timeline]

Étape 4 : filtre la timeline. Sur un contact actif, la timeline peut contenir des dizaines d'événements. Utilise les filtres pour te concentrer sur ce qui compte. Filtre par type d'événement - uniquement les page views, uniquement les clics. Filtre par période - les 7 derniers jours, le dernier mois. Filtre par événement spécifique - uniquement les visites de la page premium.

[Applique un filtre et montre le résultat]

**[ÉCRAN - screencast vue globale contacts]**

[Retourne dans la liste des contacts, montre les colonnes de tri]

Étape 5 : utilise les événements pour segmenter ta liste. Au-delà de la fiche individuelle, tu peux créer des segments basés sur les événements. Va dans Contacts, utilise les filtres avancés, et sélectionne "Has Event" comme critère. Tu peux chercher tous les contacts qui ont visité ta page premium au moins une fois, ou ceux qui ont cliqué sur le CTA sans acheter.

[Montre la création d'un segment avec un filtre événement]

C'est un outil puissant pour identifiér des groupes de contacts par comportement - pas seulement par tags ou listes.

**[TRANSITION - face caméra]**

L'historique comportemental est la pièce qui relie tout : les événements que tu as créés, les automations que tu as montées, et la compréhension de chaque contact. Tu sais maintenant où regarder et comment lire ces données. Dans l'exercice suivant, tu mets tout en pratique de bout en bout.

---

**Points clés** :
- Timeline comportementale dans la fiche de chaque contact (onglet Activities/Events)
- Chaque événement : type, nom, URL, date/heure
- Lire un parcours = comprendre le cheminement réel du contact
- Filtres disponibles : par type, par période, par événement spécifique
- Segmentation avancée : créer des segments basés sur les événements

**Mots clés SEO** : historique comportemental FluentCRM, timeline contact FluentCRM, suivi activite contact WordPress, segmentation comportementale FluentCRM

---

### Leçon 14.6 : Exercice : configure le tracking de ta page de vente et déclenche une relance

**Durée** : 5 min
**Type** : Exercice guidé
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM + WordPress

---

**[INTRO - face caméra]**

Exercice pratique. Tu vas configurer le tracking complet de ta page de vente - de l'événement jusqu'à l'email de relance automatique. Cinq étapes. À la fin, un visiteur qui revient deux fois sur ta page de vente reçoit un email personnalisé 2 heures plus tard.

**[ÉCRAN - slide "Objectif de l'exercice"]**

[Montre le schéma : page visitée 2x > event > automation > délai 2h > email relance]

Voici ce que tu vas construire. Un contact visite ta page de vente (ou une page stratégique de ton site) deux fois en 7 jours. FluentCRM détecte ce comportement, attend 2 heures, et envoie un email de relance personnalisé. Si le contact est déjà client, rien ne se passe.

**[ÉCRAN - screencast étape par étape]**

[Montre chaque étape avec le résultat attendu]

Étape 1 : crée l'événement. Va dans Settings > Event Tracking > Custom Events. Crée un événement `page_vente_visited`, titre "A visité la page de vente", type "Page View", URL : l'adresse de ta page de vente. Si tu n'as pas de page de vente, utilise ta page "À propos" ou ta page "Tarifs" pour l'exercice.

Étape 2 : ajoute le tracking de clic sur le CTA. Crée un deuxième événement `cta_vente_clicked`, titre "A cliqué sur le CTA de vente", type "Button Click". Ouvre ta page dans l'éditeur WordPress et ajoute l'attribut `data-fc-event="cta_vente_clicked"` sur ton bouton principal.

Étape 3 : crée l'automation de relance. Va dans Automations, crée "Relance page de vente". Trigger : "Event Tracked", événement `page_vente_visited`, occurrences minimum : 2, période : 7 jours. Ajoute une condition : si tag "client-premium" existe, sortie. Sinon, délai 2 heures, puis email de relance.

Étape 4 : rédige l'email. Objet : "J'ai remarqué que tu t'intéresses à [nom de ton offre]". Contenu : rappel de la valeur de l'offre, un témoignage, un lien direct vers l'inscription. Garde un ton naturel - pas de pression, pas d'urgence artificielle.

Étape 5 : teste le parcours complet. Connecte-toi avec ton contact test. Visite ta page de vente deux fois (en espaçant de quelques minutes). Retourne dans FluentCRM : vérifie que les événements apparaissent dans la fiche du contact, et que l'automation s'est déclenchée. Vérifie que l'email est en file d'attente ou envoyé.

**[TRANSITION - face caméra]**

Si tout fonctionne, tu as un système de relance comportementale complet. Chaque visiteur intéressé reçoit un suivi personnalisé, automatiquement, sans que tu interviennes. C'est exactement le type de système que tu peux dupliquer pour chaque page stratégique de ton site.

---

**Checklist de validation** :
- [ ] Événement `page_vente_visited` créé et associé à l'URL
- [ ] Événement `cta_vente_clicked` créé et attribut HTML ajouté au bouton
- [ ] Automation "Relance page de vente" créée avec trigger event (2 occurrences, 7 jours)
- [ ] Condition d'exclusion des clients existants en place
- [ ] Délai de 2 heures configuré
- [ ] Email de relance rédigé et personnalisé
- [ ] Test complet avec contact test : événements enregistrés + automation déclenchée

---

### Leçon 14.7 : Quiz : valide tes acquis M14

**Durée** : 5 min
**Type** : Quiz (8 QCM)

---

**Question 1** : Quelle est la différence principale entre les smart links (M8) et l'event tracking (M14) ?

A) Les smart links sont gratuits, l'event tracking est payant
B) Les smart links trackent les clics dans les emails, l'event tracking suit le comportement sur le site
C) Les smart links sont plus précis que l'event tracking
D) Il n'y a pas de différence, ce sont deux noms pour la même fonctionnalité

**Réponse** : B - Les smart links suivent les clics dans tes emails. L'event tracking suit ce que font tes contacts sur ton site WordPress, quelle que soit la source de trafic.

---

**Question 2** : Quel type d'événement utilises-tu pour savoir si un contact a visité ta page de tarifs ?

A) Button Click
B) Form Submission
C) Page View
D) Custom Event

**Réponse** : C - Un événement de type Page View enregistre la visite d'une page spécifique par un contact identifié.

---

**Question 3** : Quelle convention de nommage est recommandée pour les événements personnalisés ?

A) Noms en français avec espaces : "A visité la page premium"
B) Noms en camelCase : pageVentePremiumVisited
C) Noms en minuscules avec underscores : page_vente_premium_visited
D) Noms en majuscules : PAGE_VENTE_PREMIUM_VISITED

**Réponse** : C - Minuscules avec underscores, format `element_action`. Cohérent, lisible, et compatible avec tous les systèmes.

---

**Question 4** : Pourquoi ajouter un délai de 2 heures entre un événement et l'email de relance ?

A) FluentCRM a besoin de 2 heures pour traiter l'événement
B) Pour éviter l'effet surveillance et paraître naturel
C) Pour laisser le temps au contact de revenir sur la page
D) C'est le délai minimum imposé par FluentCRM

**Réponse** : B - Un email envoyé dans la minute après une visite donne l'impression d'être surveillé. Un délai de quelques heures rend l'email naturel.

---

**Question 5** : Quel attribut HTML ajoutes-tu a un bouton pour tracker son clic avec FluentCRM ?

A) `onclick="fluentcrm_track()"`
B) `class="fc-track-click"`
C) `data-fc-event="nom_événement"`
D) `id="fluentcrm-button"`

**Réponse** : C - L'attribut `data-fc-event` avec le nom de l'événement permet à FluentCRM de détecter le clic sur l'élément.

---

**Question 6** : Tu veux déclencher une automation uniquement quand un contact visite ta page premium au moins 2 fois en 7 jours. Où configures-tu ça ?

A) Dans les settings globaux de l'event tracking
B) Dans le trigger de l'automation (occurrences et période)
C) Dans un bloc condition à l'intérieur de l'automation
D) Dans la fiche du contact, onglet Events

**Réponse** : B - Le trigger "Event Tracked" de l'automation permet de définir le nombre minimum d'occurrences et la période.

---

**Question 7** : Quel est l'intérêt de combiner event tracking et scoring ?

A) Augmenter la vitesse de chargement du site
B) Quantifier l'engagement réel et qualifier les contacts par comportement
C) Remplacer les tags et les listes par un système unique
D) Envoyer plus d'emails automatiques

**Réponse** : B - Chaque événement ajoute des points au score. Un contact qui accumule des points sur des pages strategiques est objectivement plus engage - tu le qualifies par ses actions, pas par des suppositions.

---

**Question 8** : Un contact test visite ta page de vente, mais l'événement n'apparaît pas dans sa fiche FluentCRM. Quelle est la première chose à vérifier ?

A) Que le contact a un score supérieur à 10
B) Que le contact est bien identifié (connecté à WordPress) et que le module Event Tracking est actif
C) Que le contact a un tag "tracking-actif"
D) Que l'automation associée est en mode "Active"

**Réponse** : B - L'event tracking ne fonctionne que pour les contacts identifiés (connectés). Vérifie aussi que le module est bien activé dans Settings > Modules.

---

**Barème** :
- 8/8 : Module maîtrisé
- 6-7/8 : Bonne compréhension, relis les points manqués
- 4-5/8 : Revois les leçons 14.1 à 14.5
- <4/8 : Reprends le module depuis le début

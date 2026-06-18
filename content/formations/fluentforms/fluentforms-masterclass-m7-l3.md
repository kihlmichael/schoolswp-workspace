# Script video - Module 7, Lecon 3 : FluentForms + FluentBooking

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 - Ecosysteme et integrations
**Lecon** : 3/9 - FluentForms + FluentBooking
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast FluentBooking + formulaire, slide schema flux
**Objectif** : Connecter un formulaire de demande a FluentBooking pour la prise de rendez-vous

---

**[INTRO - face camera]**

Un visiteur remplit ton formulaire de contact. Tu reponds par email. Il repond. Tu proposes des creneaux. Il en choisit un. Quatre echanges d'emails pour caler un rendez-vous. Ca prend 3 jours.

Avec FluentBooking connecte a FluentForms, le visiteur remplit le formulaire et reserve son creneau directement. Zero email, zero friction.

**[SECTION 1 - slide "FluentBooking en 30 secondes"]**

FluentBooking, c'est le Calendly natif WordPress.

Tu definis tes disponibilites - jours, heures, duree des creneaux. Tu synchronises avec Google Calendar pour eviter les conflits. Tu publies un lien de reservation ou tu l'integres dans une page.

Le visiteur voit tes creneaux disponibles, en choisit un, confirme. Tu recois la notification. Le rendez-vous est dans ton calendrier.

Pas de compte SaaS. Pas de frais mensuels. Tout dans WordPress.

**[SECTION 2 - screencast "Scenario 1 : formulaire → page booking"]**

Premier scenario : le formulaire de decouverte.

Le visiteur remplit un formulaire "Demande de consultation gratuite". Champs : Prenom, Email, Textarea "Decris ton projet en quelques lignes".

Apres la soumission, au lieu d'un simple message de confirmation, tu rediriges vers ta page FluentBooking.

Configure la confirmation du formulaire : Type "Redirect", URL = la page FluentBooking. Le visiteur est envoye directement sur le calendrier de reservation.

L'avantage : tu as deja les infos du visiteur (prenom, email, description du projet) via le formulaire. Et le rendez-vous est cale immediatement.

Cote FluentCRM, le feed du formulaire cree le contact avec les tags "source-formulaire-consultation" et "status-prospect". Tu as le contact dans ton CRM avant meme que le rendez-vous ait lieu.

**[SECTION 3 - screencast "Scenario 2 : booking integre dans le formulaire"]**

Deuxieme scenario : le booking directement dans le formulaire.

Si FluentBooking propose un shortcode ou un embed, tu peux l'integrer dans une page qui contient aussi le formulaire FluentForms. Le visiteur remplit le formulaire et reserve son creneau sur la meme page.

Sinon, utilise un formulaire multi-etapes. Etape 1 : informations personnelles (Prenom, Email, Description). Etape 2 : choix du creneau - integre le widget FluentBooking ou redirige apres soumission de l'etape 1.

L'idee est de reduire le nombre de clics entre "je suis interesse" et "le rendez-vous est cale".

**[SECTION 4 - screencast "Configuration FluentBooking"]**

Si tu n'as pas encore configure FluentBooking, voici les bases.

Installe et active le plugin. Va dans FluentBooking, Settings. Cree un type de rendez-vous : "Consultation Decouverte - 30 min".

Configure tes disponibilites. Jours : lundi a vendredi. Heures : 10h-12h et 14h-17h. Duree : 30 minutes. Buffer entre deux rendez-vous : 15 minutes.

Connecte Google Calendar : FluentBooking, Settings, Integrations, Google Calendar. Autorise l'acces. FluentBooking voit tes evenements existants et bloque automatiquement les creneaux deja pris.

Configure les notifications : email de confirmation au visiteur, email de rappel H-24, email de rappel H-1.

**[SECTION 5 - slide "Le flux complet"]**

Visualise le flux.

Le visiteur arrive sur ta page de service. Il voit la description de la consultation gratuite + le formulaire FluentForms.

Il remplit le formulaire (prenom, email, description du projet). Il soumet.

FluentForms cree le contact dans FluentCRM (tag "source-consultation", liste "prospects"). Redirection vers la page FluentBooking.

Il choisit un creneau et confirme. FluentBooking envoie la confirmation + ajoute l'evenement dans Google Calendar.

H-24 : rappel automatique. Le jour J : le rendez-vous a lieu. Apres : tu as le contact dans FluentCRM avec toutes les infos pour le suivi commercial.

De l'interet a la consultation en 2 minutes. Zero email manuel.

**[SECTION 6 - screencast "Suivi post-consultation"]**

Apres la consultation, ajoute manuellement le tag "consultation-done" dans FluentCRM. Ou mieux : configure une automation qui le fait automatiquement quand le rendez-vous est marque comme termine dans FluentBooking.

L'automation post-consultation peut enchainer : tag "consultation-done" → delai 1 jour → email "Merci pour notre echange, voici le recapitulatif" → delai 3 jours → email "As-tu eu le temps de reflechir a notre proposition ?".

Le formulaire a capte le lead. FluentBooking a cale le rendez-vous. FluentCRM fait le suivi. Chaque outil joue son role.

**[OUTRO - face camera]**

FluentForms et FluentBooking travaillent main dans la main. Dans la prochaine lecon, on connecte FluentForms a FluentSupport - les soumissions de formulaire qui creent des tickets de support automatiquement.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- FluentBooking = Calendly natif WordPress (pas de SaaS, pas de frais mensuels)
- Scenario 1 : formulaire → redirection vers page FluentBooking
- Scenario 2 : booking integre dans la meme page que le formulaire
- Synchronisation Google Calendar pour eviter les conflits
- Notifications automatiques : confirmation + rappels H-24 et H-1
- Flux complet : formulaire → CRM → booking → suivi post-consultation

**Mots cles SEO** : FluentBooking FluentForms, prise de rendez-vous WordPress, Calendly WordPress, formulaire booking WordPress

---

**Notes de production** :
- Face camera : intro (le probleme des emails pour caler un RDV) + outro (transition FluentSupport)
- Screencast : config FluentBooking + connexion formulaire (~5 min)
- Slides : 2 slides (FluentBooking en 30 sec + flux complet)
- Ton : oriente productivite - eliminer les frictions

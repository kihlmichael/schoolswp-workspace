# Script video - Module 4, Lecon 7 : Cas pratique - reservation avec paiement

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 - Paiements
**Lecon** : 7/7 - Cas pratique : reservation avec paiement
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast construction complete, slide recapitulatif
**Objectif** : Construire un formulaire de reservation complet avec date, options, coupon et paiement Stripe

---

**[INTRO - face camera]**

On a vu les passerelles, les paiements simples, les abonnements, la tarification conditionnelle, l'inventaire et les coupons. Maintenant on assemble tout dans un cas concret.

On va construire un formulaire de reservation pour un atelier WordPress. Le client choisit sa date, son creneau, le nombre de personnes, des options payantes, applique un coupon, et paie par carte. Le tout en un seul formulaire.

**[SECTION 1 - screencast "Structure du formulaire"]**

Cree un nouveau formulaire. "Reservation Atelier WordPress".

Voici les champs qu'on va ajouter, dans l'ordre :

Etape 1 - Informations personnelles : Name, Email, Phone.

Etape 2 - Choix de la reservation : Date Picker, Select (creneau), Number (nombre de personnes).

Etape 3 - Options et paiement : Checkbox Payment Items (options), Coupon, Payment Summary, Stripe Card Element.

Si tu veux en faire un formulaire multi-etapes, c'est le moment d'utiliser les Form Steps qu'on a vus au module precedent. Sinon, un formulaire long avec des sections bien separees fonctionne aussi.

**[SECTION 2 - screencast "Champs de reservation"]**

Date Picker. Label : "Date de l'atelier". Configure les dates disponibles - desactive les jours feries et les week-ends si necessaire. Tu peux aussi definir une date minimum (pas de reservation pour demain) et une date maximum.

Select conditionnel. Label : "Creneau horaire". Options : "Matin (9h-12h)", "Apres-midi (14h-17h)".

Pour aller plus loin, tu peux rendre les creneaux conditionnels selon la date. Si le mardi il n'y a qu'un creneau matin, tu masques l'option apres-midi. Configure ca avec la logique conditionnelle.

Number. Label : "Nombre de personnes". Minimum 1, maximum 5. Chaque personne supplementaire ajoute au prix. On va connecter ca au paiement.

**[SECTION 3 - screencast "Paiement avec options"]**

Payment Item. Label : "Tarif par personne". Prix : 97 euros. Ajoute un champ Item Quantity lie au champ "Nombre de personnes". Comme ca, si le client reserve pour 3 personnes, le total passe a 291 euros.

Checkbox Payment Items pour les options supplementaires :
- "Kit de bienvenue" : 25 euros
- "Dejeuner inclus" : 18 euros
- "Support post-atelier (1 mois)" : 49 euros

Chaque option cochee s'ajoute au total. Et ces options sont par personne ou forfaitaires - a toi de decider. Pour simplifier, on les met en forfaitaire.

**[SECTION 4 - screencast "Coupon et recapitulatif"]**

Ajoute le champ Coupon. Le client peut taper un code promo si tu en as distribue.

Juste en dessous, le Payment Summary. Il affiche tout :
- Tarif : 97 euros x 3 personnes = 291 euros
- Kit de bienvenue : 25 euros
- Dejeuner inclus : 18 euros
- Coupon EARLYBIRD (-10%) : -33.40 euros
- Total : 300.60 euros

Le client voit exactement le detail avant de payer. Transparence totale.

Ajoute le Stripe Card Element. Et modifie le label du bouton : "Confirmer et payer".

**[SECTION 5 - screencast "Notifications"]**

Configure deux notifications.

Notification 1 - Confirmation client. Destinataire : {inputs.email}. Objet : "Confirmation de reservation - Atelier WordPress". Corps : recap de la reservation (date, creneau, nombre de personnes, options, montant paye). Ajoute l'adresse du lieu, les consignes d'acces, et un lien pour ajouter l'evenement au calendrier.

Notification 2 - Alerte admin. Destinataire : ton email. Objet : "Nouvelle reservation atelier". Corps : toutes les infos du client + details de la reservation. Tu vois chaque reservation en temps reel dans ta boite mail.

**[SECTION 6 - screencast "Confirmation conditionnelle"]**

Pour la page de confirmation, on va utiliser une confirmation conditionnelle.

Si le client a choisi le creneau matin : redirige vers une page avec les informations specifiques au matin (horaires, parking, cafe offert).

Si le client a choisi le creneau apres-midi : redirige vers une page differente avec les informations de l'apres-midi.

Configure ca dans Settings, Confirmations. Ajoute une condition : IF "Creneau horaire" IS "Matin" THEN redirect to page-matin. Ajoute une deuxieme condition pour l'apres-midi.

Si aucune condition n'est remplie, le message de confirmation par defaut s'affiche.

**[SECTION 7 - screencast "Test complet"]**

On teste le formulaire de bout en bout. Stripe en mode test.

Remplis les infos. Choisis une date, le creneau matin, 2 personnes. Coche "Kit de bienvenue" et "Dejeuner inclus". Tape le coupon "EARLYBIRD". Verifie que le Payment Summary est correct. Paie avec la carte test.

Verifie : la page de confirmation du matin s'affiche. L'email client arrive avec le recap. L'email admin arrive avec les details. La transaction apparait dans Stripe.

Si tout est bon, tu as un formulaire de reservation professionnel.

**[OUTRO - face camera]**

Voila. Tu as un systeme de reservation complet - date, creneaux, options, coupon, paiement, confirmations. Tout dans un seul formulaire FluentForms.

Le module 4 est termine. Tu maitrises les paiements. Dans le prochain module, on connecte FluentForms a FluentCRM - et la, les formulaires deviennent de vrais outils de croissance.

On se retrouve au module 5.

---

**Points cles** :
- Formulaire complet : date + creneau + personnes + options + coupon + paiement
- Payment Item + Item Quantity pour le calcul par nombre de personnes
- Checkbox Payment Items pour les options supplementaires
- Payment Summary pour la transparence totale avant paiement
- 2 notifications : confirmation client + alerte admin
- Confirmation conditionnelle selon le creneau choisi
- Test complet de bout en bout avant mise en production

**Mots cles SEO** : formulaire reservation WordPress, FluentForms reservation paiement, booking formulaire Stripe, formulaire evenement WordPress

---

**Notes de production** :
- Face camera : intro (on assemble tout) + outro (transition module 5)
- Screencast : construction complete du formulaire (~8 min)
- Slide : aucune - tout en screencast pour ce cas pratique
- Ton : rythme soutenu mais clair - beaucoup de champs a configurer, garder le fil

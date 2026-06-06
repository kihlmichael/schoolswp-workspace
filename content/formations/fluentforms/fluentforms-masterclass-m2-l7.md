# Script video - Module 2, Lecon 7 : Cas pratique - inscription evenement avec options

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 2 - Logique conditionnelle
**Lecon** : 7/7 - Cas pratique : inscription evenement avec options
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast construction complete
**Objectif** : Construire un formulaire d'inscription evenement avec paiement et logique conditionnelle

---

**[INTRO - face camera]**

Deuxieme cas pratique. On construit un formulaire d'inscription a un evenement - conference, atelier, workshop, peu importe.

Le formulaire gere les inscriptions, les options de menu, les tarifs de groupe, un code promo, et le paiement. Tout avec de la logique conditionnelle.

**[ECRAN - screencast "Structure du formulaire"]**

Nouveau formulaire : "Inscription Evenement schoolsWP".

Les champs, dans l'ordre :

Name (prenom + nom). Email. Les bases.

Number "Nombre de places" - min 1, max 20, defaut 1.

Select "Menu" avec les options : Standard, Vegetarien, Vegan. Ce champ est toujours visible - chaque participant doit choisir son menu.

Text Input "Code promo" - champ optionnel. Le visiteur entre un code s'il en a un.

Et un champ Payment Item "Inscription" avec le prix unitaire de l'evenement. Disons 49 euros par place.

**[ECRAN - screencast "Logique conditionnelle - tarif groupe"]**

Premiere logique : le tarif groupe.

Si le nombre de places est superieur a 5, on veut afficher un message et proposer un tarif degressif.

J'ajoute un champ Custom HTML "Tarif groupe" avec le texte : "Plus de 5 places ? Contacte-nous pour un tarif groupe a contact@schoolswp.com."

Logique conditionnelle : Show si "Nombre de places" Greater Than "5".

Le visiteur qui inscrit 3 personnes ne voit pas ce message. Celui qui inscrit 8 personnes le voit et peut nous contacter pour negocier.

Alternative pour les gros volumes : ajouter un deuxieme Payment Item "Tarif groupe" a 39 euros par place, visible seulement si places > 5, et masquer le Payment Item standard dans ce cas. Le prix s'adapte automatiquement.

**[ECRAN - screencast "Logique conditionnelle - code promo"]**

Deuxieme logique : le code promo.

FluentForms Pro a un champ natif "Coupon" dans la categorie Payment. C'est plus propre que de gerer manuellement un champ texte.

Je remplace le Text Input par un champ Coupon. Dans les settings du formulaire, je configure les codes valides : "EARLY20" pour 20% de reduction, "VIP50" pour 50% de reduction.

Le visiteur entre le code, clique sur "Appliquer", et la reduction s'affiche en temps reel sur le total.

Si le code est invalide, un message d'erreur apparait : "Code promo non reconnu."

**[ECRAN - screencast "Notifications conditionnelles"]**

Les notifications.

Notification 1 - confirmation visiteur : email a {inputs.email}. Sujet : "Confirmation d'inscription - Evenement schoolsWP". Body : recap du nombre de places, du menu choisi, du montant paye. Envoyee a chaque soumission.

Notification 2 - alerte organisateur : email a l'equipe. Toutes les infos du participant. Envoyee a chaque soumission.

Notification 3 - notification menu special : email au traiteur. Condition : "Menu" Not Equal "Standard". Le traiteur est prevenu uniquement quand quelqu'un choisit vegetarien ou vegan. Il n'a pas besoin d'etre notifie pour les menus standard.

**[ECRAN - screencast "Confirmation conditionnelle selon le menu"]**

Confirmation par defaut : "Inscription confirmee. Tu recevras un email avec tous les details pratiques."

Confirmation conditionnelle 1 : si "Menu" Equal "Vegetarien" → message : "Inscription confirmee. Menu vegetarien note - on s'occupe de tout. Tu recevras les details par email."

Confirmation conditionnelle 2 : si "Menu" Equal "Vegan" → message : "Inscription confirmee. Menu vegan note. Si tu as des allergies specifiques, reponds a l'email de confirmation."

Petit detail, mais ca montre au participant que sa demande est prise en compte. C'est de l'experience client.

**[ECRAN - screencast "Configuration du paiement"]**

Le paiement. FluentForms Pro supporte Stripe et PayPal.

J'utilise Stripe. Le champ Payment Item est configure a 49 euros. Le champ Quantity est lie au nombre de places - le total se calcule automatiquement : 49 x nombre de places.

Si un coupon est applique, la reduction se soustrait du total. Le visiteur voit le montant final avant de payer.

Le paiement Stripe est integre directement dans le formulaire. Le visiteur ne quitte pas la page. Il entre sa carte, confirme, et c'est fait.

Apres le paiement, la soumission est enregistree et les notifications partent.

**[ECRAN - screencast "Test complet"]**

Test 1 : 2 places, menu standard, pas de code promo. Total : 98 euros. Notification standard + organisateur. Confirmation par defaut. Correct.

Test 2 : 1 place, menu vegan, code "EARLY20". Total : 49 - 20% = 39,20 euros. Notification standard + organisateur + traiteur (menu special). Confirmation vegan. Correct.

Test 3 : 8 places, menu vegetarien, pas de code promo. Total : 392 euros. Message tarif groupe visible. Notification standard + organisateur + traiteur. Confirmation vegetarien. Correct.

Trois scenarios, trois parcours, un seul formulaire.

**[OUTRO - face camera]**

Et voila le Module 2 termine. Tu maitrises maintenant la logique conditionnelle - des conditions simples aux groupes avances, en passant par les notifications et confirmations conditionnelles.

Tu as aussi deux formulaires complets que tu peux adapter a tes besoins.

Dans le Module 3, on passe aux formulaires avances : multi-step, conversational forms, calculs, upload de fichiers, et l'AI Form Builder. C'est le niveau suivant. On se retrouve dans la premiere lecon.

---

**Points cles** :
- Formulaire d'inscription evenement avec paiement Stripe integre
- Logique conditionnelle : tarif groupe si > 5 places, notification traiteur si menu special
- Champ Coupon natif avec codes configures dans les settings
- Confirmation personnalisee selon le menu choisi
- Paiement calcule automatiquement : prix unitaire x nombre de places - coupon

**Mots cles SEO** : FluentForms inscription evenement, formulaire paiement WordPress, FluentForms Stripe, FluentForms code promo coupon, formulaire evenement WordPress

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (20 sec, transition Module 3)
- Screencast integral : construction + configuration + 3 tests
- Montrer le champ Coupon en action (code valide + code invalide)
- Montrer le paiement Stripe integre dans le formulaire
- Rythme : moderement rapide, le viewer connait deja la logique conditionnelle

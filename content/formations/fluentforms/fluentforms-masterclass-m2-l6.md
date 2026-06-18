# Script video - Module 2, Lecon 6 : Cas pratique - formulaire de devis automatique

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 2 - Logique conditionnelle
**Lecon** : 6/7 - Cas pratique : formulaire de devis automatique
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast construction complete du formulaire
**Objectif** : Construire un formulaire de devis fonctionnel avec logique conditionnelle de A a Z

---

**[INTRO - face camera]**

On a vu la theorie. Maintenant on construit.

Dans cette lecon, on cree un formulaire de devis complet pour un freelance web. Champs adaptatifs, calcul dynamique du prix, notification conditionnelle selon le budget. Le tout en 10 minutes.

Tu peux suivre en parallele dans ton FluentForms. Meme formulaire, memes reglages.

**[ECRAN - screencast "Creer le formulaire"]**

Nouveau formulaire. Je pars d'un formulaire vierge - pas de template.

Nom du formulaire : "Demande de devis - Freelance Web".

On commence par les champs d'identite. Name (prenom + nom) et Email. Classique.

**[ECRAN - screencast "Champ type de projet"]**

Deuxieme section : le type de projet.

J'ajoute un Select "Type de projet" avec les options :
- Site vitrine
- E-commerce
- Refonte de site existant
- Application web
- Autre

Ce champ va piloter toute la logique conditionnelle du formulaire.

**[ECRAN - screencast "Champs conditionnels par type"]**

Maintenant, les champs specifiques a chaque type.

Pour "Site vitrine", j'ajoute un Range Slider "Nombre de pages" (min 1, max 30, defaut 5). Logique conditionnelle : Show si "Type de projet" Equal "Site vitrine".

Pour "E-commerce", j'ajoute trois champs :
- Number "Nombre de produits" - Show si type = E-commerce
- Checkbox "Fonctionnalites e-commerce" avec les options : Panier avance, Gestion de stock, Paiement Stripe, Paiement PayPal, Abonnements, Multi-devises - Show si type = E-commerce
- Select "Plateforme preferee" : WooCommerce, Shopify, PrestaShop, Pas de preference - Show si type = E-commerce

Pour "Refonte de site existant", j'ajoute un Text Input "URL du site actuel" - Show si type = Refonte.

Pour "Application web", j'ajoute un Textarea "Description des fonctionnalites" - Show si type = Application web.

En preview, je verifie : je selectionne "E-commerce" - les trois champs e-commerce apparaissent. Je passe a "Site vitrine" - le range slider apparait, les champs e-commerce disparaissent. Parfait.

**[ECRAN - screencast "Budget et deadline"]**

Section suivante : budget et timing.

J'ajoute un Radio "Budget estimé" avec les options :
- Moins de 2 000 euros
- 2 000 a 5 000 euros
- 5 000 a 10 000 euros
- Plus de 10 000 euros

Et un Date Picker "Deadline souhaitee" avec date minimum = aujourd'hui (pas de date dans le passe).

Ces deux champs sont toujours visibles, quel que soit le type de projet.

**[ECRAN - screencast "Calcul dynamique du devis"]**

Maintenant, le calcul dynamique. C'est une feature Pro.

J'ajoute un champ Number en mode "Custom Calculation". Ce champ affichera l'estimation du devis en temps reel.

La formule depend du type de projet. Pour simplifier, on va utiliser le nombre de pages ou de produits comme base :

Pour un site vitrine : nombre de pages multiplié par 200 euros.

Je configure le champ calcule avec la formule : {inputs.nombre_pages} * 200.

Pour l'e-commerce, c'est plus complexe - on pourrait ajouter un deuxieme champ calcule avec : {inputs.nombre_produits} * 15 + 2000 (base e-commerce).

Chaque champ calcule a sa propre logique conditionnelle pour s'afficher au bon moment.

Note : ce calcul est une estimation affichee au visiteur. Ce n'est pas un prix definitif - c'est un outil d'engagement qui donne une idee du cout et qui qualifie le prospect.

**[ECRAN - screencast "Textarea et soumission"]**

Dernier champ avant le bouton submit : un Textarea "Informations complementaires". Toujours visible, optionnel. Le visiteur ajoute ce qu'il veut.

Et le bouton Submit que je renomme : "Recevoir mon estimation".

**[ECRAN - screencast "Notifications conditionnelles"]**

Les notifications.

Notification 1 - confirmation visiteur : envoyee a {inputs.email}, sujet "Ton estimation de devis - schoolsWP". Body avec recap des reponses et l'estimation calculee. Pas de condition - envoyee a chaque soumission.

Notification 2 - alerte freelance standard : envoyee a ton email pro. Contient toutes les reponses. Pas de condition.

Notification 3 - alerte prioritaire : envoyee a ton email + SMS (via webhook ou integration). Condition : "Budget" Equal "Plus de 10 000 euros". Sujet : "DEVIS PRIORITAIRE - {inputs.name}". Ce prospect est chaud, tu veux reagir vite.

**[ECRAN - screencast "Confirmation conditionnelle"]**

Confirmation par defaut : message "Merci pour ta demande. On te recontacte sous 48h avec une proposition detaillee."

Confirmation conditionnelle : si "Budget" Equal "Plus de 10 000 euros" → redirection vers une page de prise de RDV Calendly. Ce prospect merite un appel, pas un email.

**[ECRAN - screencast "Test complet"]**

Testons le formulaire complet.

Test 1 : Site vitrine, 8 pages, budget 2000-5000, deadline dans 3 mois. Le calcul affiche 1600 euros. La notification standard part. Le message de remerciement s'affiche. Correct.

Test 2 : E-commerce, 200 produits, WooCommerce, Panier avance + Stripe, budget plus de 10 000. La notification prioritaire part. Redirection vers Calendly. Correct.

Test 3 : Refonte, URL du site remplie, budget moins de 2000. Notification standard. Message de remerciement. Correct.

Trois scenarios, trois parcours differents, un seul formulaire.

**[OUTRO - face camera]**

Tu viens de construire un formulaire de devis complet : champs adaptatifs, calcul dynamique, notifications intelligentes, confirmation personnalisee. Un outil de qualification de prospects qui travaille pour toi 24 heures sur 24.

Prochaine lecon : un formulaire d'inscription evenement avec options, paiement et code promo. On se retrouve tout de suite.

---

**Points cles** :
- Formulaire de devis freelance complet construit de A a Z
- Champs conditionnels par type de projet (vitrine, e-commerce, refonte, app)
- Calcul dynamique du prix en temps reel
- Notification prioritaire si budget > 10 000 euros
- Redirection Calendly pour les gros budgets
- Un formulaire = multiple parcours visiteur

**Mots cles SEO** : FluentForms formulaire de devis, formulaire devis automatique WordPress, FluentForms calcul dynamique, formulaire freelance WordPress

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast integral : construction du formulaire de A a Z
- Montrer chaque configuration de logique conditionnelle
- Montrer les 3 tests complets en preview
- Rythme soutenu mais clair - le viewer peut mettre en pause pour suivre

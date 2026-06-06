# Script video - Module 4, Lecon 2 : Formulaire de paiement simple

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 - Paiements
**Lecon** : 2/7 - Formulaire de paiement simple
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast builder + Stripe test, slide recapitulatif
**Objectif** : Creer un formulaire de vente de produit simple (ebook a 27 euros) avec paiement Stripe

---

**[INTRO - face camera]**

Tu veux vendre un ebook, une prestation, un template - et tu n'as pas envie d'installer WooCommerce pour ca. FluentForms permet de vendre directement via un formulaire.

On va construire ensemble un formulaire de vente pour un ebook a 27 euros. Paiement par carte via Stripe. De A a Z.

**[SECTION 1 - screencast "Creer le formulaire"]**

Cree un nouveau formulaire. Appelle-le "Vente Ebook SEO WordPress". Formulaire vierge.

D'abord, les champs client. Ajoute un champ Name - format First Name + Last Name. Ajoute un champ Email. Ces deux-la sont obligatoires pour toute vente.

Si tu vends un produit physique, ajoute un champ Address. Pour un produit numerique comme un ebook, pas besoin.

**[SECTION 2 - screencast "Ajouter le champ Payment Item"]**

Maintenant, le coeur du formulaire. Dans la colonne de gauche, cherche la categorie Payment Fields. Ajoute un champ Payment Item.

Configure-le. Label : "Ebook SEO WordPress - Guide Complet". Price : 27.00. Payment Type : Single Payment.

C'est un prix fixe. Le client ne peut pas modifier la quantite ni le montant. Il voit le prix, il paie.

Si tu veux que le client puisse choisir entre plusieurs produits, utilise le type "Multiple Items" a la place. Mais pour un produit unique, "Single" est parfait.

**[SECTION 3 - screencast "Ajouter le recapitulatif et le bouton"]**

Ajoute un champ Payment Summary. Il affiche automatiquement le recapitulatif de la commande - nom du produit, prix, total. Le client voit exactement ce qu'il va payer avant de cliquer.

Ensuite, ajoute le champ Stripe Card Element. C'est le champ ou le client entre son numero de carte. Il est securise - les donnees de carte ne passent jamais par ton serveur, elles vont directement chez Stripe.

Le bouton Submit existant fera office de bouton de paiement. Modifie son label : "Payer 27 euros" au lieu de "Submit". C'est plus clair.

**[SECTION 4 - screencast "Configurer la notification email"]**

Apres le paiement, le client doit recevoir quelque chose. Va dans Settings, Notifications.

Cree une notification "Confirmation de commande". Destinataire : {inputs.email} - l'email du client. Objet : "Ton ebook SEO WordPress est pret". Corps du message : remerciement + lien de telechargement.

Pour le lien de telechargement, tu as deux options. Soit tu mets un lien direct vers le fichier (heberge sur ton serveur ou Google Drive). Soit tu rediriges vers une page WordPress dediee apres le paiement. Je prefere la deuxieme option - elle te permet de tracker les telechargements et d'ajouter un upsell.

**[SECTION 5 - screencast "Configurer la confirmation"]**

Va dans Settings, Confirmations. Remplace le message par defaut par quelque chose d'utile.

"Merci pour ton achat. Tu vas recevoir un email avec le lien de telechargement dans les prochaines minutes. Verifie tes spams si tu ne le vois pas."

Ou mieux : utilise le type "Redirect" et redirige vers une page de remerciement dediee. Sur cette page, tu mets le lien de telechargement, un message de bienvenue, et pourquoi pas une offre complementaire.

**[SECTION 6 - screencast "Tester le paiement"]**

On teste. Assure-toi que Stripe est en mode Test dans les settings.

Remplis le formulaire. Nom, email, et pour la carte utilise 4242 4242 4242 4242, date future, CVC 123. Soumets.

Tu devrais voir le message de confirmation. Verifie dans Stripe Dashboard que la transaction apparait. Verifie que l'email de notification part.

Si tout fonctionne, remplace les cles test par les cles live et tu es en production.

**[SECTION 7 - slide "Ce que tu viens de construire"]**

Recapitulons ce qu'on a fait.

Un formulaire qui collecte les infos client, affiche le prix, encaisse le paiement par carte via Stripe, envoie un email de confirmation avec le lien de telechargement, et affiche un message ou redirige vers une page de remerciement.

Tout ca sans WooCommerce. Sans plugin e-commerce. Juste FluentForms et Stripe.

Pour un produit simple - ebook, template, prestation forfaitaire - c'est la methode la plus directe.

**[OUTRO - face camera]**

Tu sais maintenant vendre un produit via FluentForms. Dans la prochaine lecon, on passe aux paiements recurrents - abonnements mensuels, coaching, SaaS. C'est un autre monde.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Payment Item en Single Payment pour un produit a prix fixe
- Payment Summary pour afficher le recapitulatif au client
- Stripe Card Element pour la saisie securisee de la carte
- Notification email avec lien de telechargement
- Confirmation : message ou redirection vers page de remerciement
- Toujours tester en mode Test avant de passer en Live
- Cas pratique : ebook a 27 euros

**Mots cles SEO** : vendre avec FluentForms, formulaire paiement WordPress, FluentForms Stripe tutoriel, vendre ebook WordPress

---

**Notes de production** :
- Face camera : intro (le besoin) + outro (transition abonnements)
- Screencast : construction complete du formulaire de A a Z (~7 min)
- Slide : 1 slide recapitulatif final
- Ton : pas a pas, concret - le viewer doit pouvoir reproduire en meme temps

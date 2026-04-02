# Script video — Module 4, Lecon 5 : Gestion d'inventaire

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 — Paiements
**Lecon** : 5/7 — Gestion d'inventaire
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast builder + settings inventaire, slide recapitulatif
**Objectif** : Limiter les quantites disponibles et afficher "Complet" automatiquement

---

**[INTRO — face camera]**

Tu vends des places a un evenement, des exemplaires limites d'un produit, ou des creneaux de coaching. Tu as un stock fini. Il faut que le formulaire le sache — et qu'il se bloque automatiquement quand c'est complet.

FluentForms Pro gere ca nativement. On va configurer ca ensemble.

**[SECTION 1 — screencast "Le cas pratique"]**

On va creer un formulaire pour un atelier WordPress en presentiel. 50 places maximum. Quand les 50 places sont prises, le formulaire affiche "Complet" et n'accepte plus de soumissions.

Cree un nouveau formulaire. "Inscription Atelier WordPress — 50 places".

Ajoute les champs : Name, Email, Phone. Ajoute un Payment Item pour le tarif de l'atelier — disons 97 euros.

**[SECTION 2 — screencast "Configurer la limite de quantite"]**

La gestion d'inventaire passe par les reglages de soumission du formulaire, pas par le champ Payment Item directement.

Va dans Settings, Form Settings, et cherche l'option Maximum Number of Entries. C'est la que tu definis ta limite.

Entre 50. A partir de la 51eme tentative de soumission, le formulaire sera bloque.

Pour le message affiche quand c'est complet, personnalise le texte. Remplace le message par defaut par quelque chose d'utile : "Toutes les places pour l'atelier WordPress sont prises. Laisse ton email pour etre prevenu du prochain atelier."

Et la, astuce maline : ajoute un lien vers un formulaire de liste d'attente. Tu ne perds pas le contact.

**[SECTION 3 — screencast "Quantite par item"]**

Si tu vends plusieurs items dans le meme formulaire, tu peux aussi limiter chaque item individuellement.

Exemple : tu proposes 3 formules pour ton atelier. Standard (30 places), VIP (15 places), Premium (5 places).

Utilise un champ Payment Item de type Multiple Choice. Pour chaque option, tu peux definir une quantite maximale dans les settings du champ — c'est le Item Quantity Limit.

Quand les 15 places VIP sont prises, l'option VIP se grise ou disparait. Les autres options restent disponibles.

**[SECTION 4 — screencast "Champ Quantity"]**

Autre scenario : tu veux que le client puisse acheter plusieurs unites. Par exemple, des billets pour un evenement — "Combien de places veux-tu reserver ?"

Ajoute un champ Item Quantity a cote de ton Payment Item. Le client entre un nombre. Le prix se multiplie automatiquement.

Tu peux definir un minimum (1) et un maximum (par exemple 5 par commande). Ca evite qu'une seule personne prenne toutes les places.

Et la limite globale des 50 soumissions s'applique toujours. Donc meme si chacun peut prendre 5 places, le formulaire se bloque a 50 soumissions totales.

Si tu veux que la limite tienne compte du nombre de places reelles (pas juste du nombre de soumissions), il faudra utiliser un calcul custom ou un webhook vers un systeme externe. Pour la plupart des cas, la limite par soumissions suffit.

**[SECTION 5 — slide "Checklist inventaire"]**

Recapitulatif pour chaque formulaire avec inventaire.

Definir la limite dans Maximum Number of Entries. Personnaliser le message "complet" avec un CTA de liste d'attente. Si plusieurs options : limiter chaque item individuellement. Si quantite par commande : definir min et max. Tester en envoyant des soumissions de test pour verifier que le blocage fonctionne.

Et un conseil : surveille tes soumissions. Quand tu approches de la limite, previens ta communaute — "Plus que 5 places" fonctionne tres bien pour accelerer les inscriptions.

**[OUTRO — face camera]**

Ton formulaire gere maintenant un stock fini. Dans la prochaine lecon, on ajoute les coupons de reduction — pour booster tes ventes avec des codes promo.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Maximum Number of Entries : limite globale de soumissions
- Message personnalise quand le formulaire est complet + CTA liste d'attente
- Item Quantity Limit : limiter chaque option individuellement
- Champ Item Quantity : laisser le client choisir le nombre d'unites
- Tester le blocage avant de passer en production
- Cas pratique : atelier 50 places a 97 euros

**Mots cles SEO** : FluentForms inventaire, limiter places formulaire WordPress, formulaire inscription evenement WordPress, FluentForms stock

---

**Notes de production** :
- Face camera : intro (probleme stock fini) + outro (transition coupons)
- Screencast : config limite + quantite par item + champ quantity (~4 min)
- Slide : 1 slide checklist inventaire
- Ton : pratique, rapide — lecon courte et ciblee

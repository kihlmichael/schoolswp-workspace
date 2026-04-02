# Lecon 5.6 — Segments : cibler par historique d'achat

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 5 — One-Click Upsells et Downsells
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre les segments CartFlows, configurer des regles basees sur les achats precedents du client, eviter de proposer un produit deja achete, et faire le lien avec FluentCRM.

---

## Script narration

**[INTRO — face camera]**

Les Dynamic Offers adaptent ton upsell a la commande en cours. Les Segments vont plus loin : ils adaptent l'offre en fonction de l'historique complet du client. Nouveau client, client fidele, client qui a deja achete un produit specifique — chacun voit une offre differente.

---

**[SECTION 1 — Pourquoi l'historique d'achat change tout]**

**[ECRAN — scenario : client recurrent qui voit un upsell pour un produit qu'il possede deja]**

Imagine : un client a deja achete ta formation premium il y a 3 mois. Il revient aujourd'hui pour acheter un autre produit. Ton upsell lui propose... la formation premium qu'il possede deja. C'est genant. Et ca tue la confiance.

A l'inverse, un tout nouveau client qui decouvre ton univers pour la premiere fois ne devrait pas voir la meme offre qu'un client fidele qui a deja 4 produits dans son compte.

Les Segments CartFlows resolvent ce probleme en ajoutant une couche d'intelligence basee sur l'historique.

---

**[SECTION 2 — Les segments disponibles dans CartFlows]**

**[ECRAN — liste des types de segments]**

CartFlows Pro propose plusieurs criteres de segmentation pour tes upsells et downsells :

- **Nouveau client vs client existant** : le client a-t-il deja passe une commande sur ta boutique ?
- **Produit deja achete** : le client possede-t-il deja un produit specifique ?
- **Nombre de commandes** : combien de commandes le client a-t-il passees au total ?
- **Total depense** : combien le client a-t-il depense au total sur ta boutique ?

Ces criteres te permettent de creer des parcours differencies. Un nouveau client recoit une offre d'introduction. Un client fidele recoit une offre exclusive de fidelite.

---

**[SECTION 3 — Configuration : Upsell → Segments → Add Rule]**

**[ECRAN — CartFlows → Step Upsell → Segments]**

Ouvre les parametres de ton step Upsell. Dans la section Segments (ou Conditional Rules selon la version), clique sur "Add Rule".

**Regle 1 : ne pas proposer un produit deja achete.**

C'est la regle la plus importante. Configure : "If customer has purchased → [nom du produit upsell] → then skip this offer."

**[ECRAN — configuration de la regle "has purchased"]**

Concretement : si ton upsell propose le "Coaching Premium" et que le client l'a deja achete dans une commande precedente, CartFlows saute l'upsell et passe directement au step suivant (downsell ou Thank You).

**Regle 2 : offre differente pour les nouveaux clients.**

Add Rule : "If customer order count → equals → 0 → show Offer A." Et une deuxieme regle : "If customer order count → greater than → 0 → show Offer B."

**[ECRAN — deux regles configurees]**

L'Offer A pourrait etre un guide de demarrage a 27 euros — adapte a quelqu'un qui ne te connait pas encore. L'Offer B pourrait etre un coaching avance a 147 euros — adapte a quelqu'un qui te fait deja confiance.

---

**[SECTION 4 — Combiner Segments et Dynamic Offers]**

**[ECRAN — schema : segments + dynamic offers = offre ultra-ciblee]**

Les Segments et les Dynamic Offers ne sont pas mutuellement exclusifs. Tu peux les combiner pour un ciblage precis :

- **Dynamic Offer** : regarde ce que le client achete maintenant
- **Segment** : regarde ce que le client a achete avant

Exemple combine : si le client achete la "Formation Basique" (Dynamic Offer) ET c'est un nouveau client (Segment), propose le "Pack Bienvenue" a 37 euros. Si c'est un client existant qui achete la meme formation, propose le "Coaching Avance" a 147 euros.

C'est puissant parce que chaque client vit un parcours unique, adapte a sa relation avec ta marque.

---

**[SECTION 5 — Le lien avec FluentCRM]**

**[ECRAN — schema CartFlows → WooCommerce → FluentCRM]**

Si tu utilises FluentCRM (et si tu suis les formations schoolsWP, tu devrais), les actions CartFlows alimentent automatiquement ton CRM.

Voici comment ca fonctionne :

1. Le client accepte l'upsell dans CartFlows
2. WooCommerce enregistre la commande avec le produit upsell
3. FluentCRM detecte le nouvel achat et applique automatiquement les tags configures

Par exemple : le client accepte le "Coaching Premium" en upsell → FluentCRM ajoute le tag "coaching-premium" → ce tag declenche une sequence email d'onboarding coaching.

**[ECRAN — FluentCRM → Automations → trigger "Product Purchased"]**

Pour configurer ca dans FluentCRM : cree une automation avec le trigger "Product Purchased", selectionne le produit upsell, et definis les actions (tag, sequence, notification).

Les donnees de segmentation circulent dans les deux sens. Les segments CartFlows utilisent l'historique WooCommerce, et les tags FluentCRM se nourrissent des actions CartFlows. Tu construis progressivement un profil client riche qui te permet de personnaliser toute ta communication.

---

**[SECTION 6 — Bonnes pratiques]**

**[ECRAN — checklist des bonnes pratiques segments]**

Trois regles pour bien utiliser les segments :

**1. Toujours exclure les produits deja achetes.** C'est la regle zero. Rien ne casse plus la confiance que de proposer un produit que le client possede deja.

**2. Differencier nouveau vs recurrent des le premier upsell.** Un nouveau client a besoin de confiance. Un client recurrent a besoin de valeur. Adapte le ton et le prix en consequence.

**3. Ne pas sur-segmenter au debut.** Deux ou trois segments suffisent : nouveau client, client existant, client VIP (plus de 3 commandes ou plus de 500 euros depenses). Affine quand tu auras les donnees.

---

**[OUTRO — face camera]**

Les Segments ajoutent de l'intelligence a tes upsells. Combine-les avec les Dynamic Offers et tu obtiens un systeme ou chaque client voit l'offre la plus pertinente, en fonction de ce qu'il achete maintenant et de ce qu'il a achete avant.

Dans la prochaine lecon, on aborde un sujet technique important : les upsells avec PayPal et les limites a connaitre.

---

## Notes de production

- **Visuels** : schema parcours avec segments, captures CartFlows (Segments UI), schema FluentCRM integration, checklist bonnes pratiques
- **Captures d'ecran** : configuration regles segments, FluentCRM automations
- **Prerequis** : CartFlows Pro, FluentCRM recommande
- **Ton** : strategique, lien CRM
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine sur L5.7 (Upsell avec PayPal)

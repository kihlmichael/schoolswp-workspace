# Lecon 4.4 - Rules Engine : afficher le bon bump au bon client

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 4 - Order Bumps
- **Duree cible** : 10 min (~1300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Maitriser le Rules Engine de CartFlows Pro pour afficher ou masquer des order bumps selon des conditions precises (produit dans le panier, montant, role utilisateur, historique d'achat).

---

## Script narration

**[INTRO - face camera]**

Jusqu'ici, ton bump s'affiche pour tout le monde. Meme client, meme offre, a chaque fois. Ca fonctionne, mais c'est du one-size-fits-all.

Le Rules Engine de CartFlows Pro change ca. Il te permet de definir des conditions : affiche ce bump seulement si le panier depasse 50 euros, masque cet autre bump si le client a deja achete le produit, montre un bump specifique aux nouveaux clients.

C'est de la personnalisation sans code, directement dans l'interface CartFlows. Et ca fait une difference mesurable sur les taux de prise.

---

**[SECTION 1 - Qu'est-ce que le Rules Engine]**

**[ECRAN - schema du fonctionnement du Rules Engine]**

Le Rules Engine, c'est un systeme de conditions qui s'appliquent a chaque order bump. Pour chaque bump, tu peux definir une ou plusieurs regles. Si les regles sont satisfaites, le bump s'affiche. Sinon, il reste masque.

Le client ne voit jamais les bumps qui ne le concernent pas. Il voit uniquement les offres pertinentes pour lui, a ce moment precis. C'est plus propre pour le client et plus efficace pour toi.

---

**[SECTION 2 - Acceder au Rules Engine]**

**[ECRAN - CartFlows → Step Checkout → Order Bump → Rules]**

Ouvre ton step Checkout, onglet Order Bump. Clique sur le bump que tu veux conditionner. Dans les options du bump, tu vas trouver un onglet ou une section "Rules" (selon ta version de CartFlows Pro).

**[ECRAN - section Rules du bump]**

Clique sur "Add Condition". CartFlows te propose plusieurs types de conditions. On va les passer en revue.

---

**[SECTION 3 - Types de conditions disponibles]**

**[ECRAN - liste des conditions avec exemples pour chaque]**

**Produit dans le panier.** La condition la plus courante. Tu choisis un produit specifique : si ce produit est dans le panier, le bump s'affiche. Exemple : le bump "extension garantie" s'affiche seulement si le client achete le produit physique. Pas de sens de proposer une garantie pour un ebook.

**Montant du panier.** Tu definis un seuil : minimum, maximum, ou entre deux valeurs. Exemple : le bump "livraison express" s'affiche seulement si le panier depasse 30 euros. En dessous, le cout de la livraison express serait disproportionne.

**Role utilisateur.** WooCommerce et WordPress attribuent des roles aux utilisateurs : client, abonne, administrateur. Tu peux afficher un bump uniquement pour un role specifique. Exemple : le bump "upgrade premium" s'affiche seulement pour les utilisateurs avec le role "client" - pas pour les administrateurs qui testent le site.

**Historique d'achat.** C'est la condition la plus puissante. Tu peux cibler les clients qui ont deja achete un produit specifique - ou au contraire ceux qui ne l'ont jamais achete. Exemple : le bump "niveau avance" s'affiche seulement pour les clients qui ont deja achete la formation niveau debutant.

---

**[SECTION 4 - Cas pratique 1 : bump conditionnel au montant]**

**[ECRAN - configuration etape par etape]**

Mettons ca en pratique. Tu vends des produits physiques entre 20 et 200 euros. Tu veux proposer un bump "extension garantie 2 ans" a 15 euros, mais seulement si la commande depasse 50 euros. En dessous, une garantie supplementaire pour un produit a 25 euros n'a pas de sens - le client prefere racheter le produit.

Dans le Rules Engine du bump : Add Condition → Cart Total → Greater Than → 50.

**[ECRAN - condition configuree]**

Sauvegarde. Maintenant, un client qui commande pour 35 euros ne verra pas le bump. Un client qui commande pour 75 euros le verra. Le bump est cible, pertinent, et il ne pollue pas les petites commandes.

---

**[SECTION 5 - Cas pratique 2 : bump pour nouveaux clients uniquement]**

**[ECRAN - configuration etape par etape]**

Deuxieme cas. Tu veux proposer un bump "pack de demarrage" a 12 euros, mais seulement aux nouveaux clients. Ceux qui ont deja achete n'en ont pas besoin - ils connaissent deja ton ecosysteme.

Dans le Rules Engine : Add Condition → Purchase History → Has Not Purchased → [n'importe quel produit].

**[ECRAN - condition configuree]**

Le bump s'affiche uniquement pour les clients qui passent leur premiere commande. Les clients recurrents voient un checkout epure, sans offre qui ne les concerne pas.

Tu peux affiner : au lieu de "n'importe quel produit", tu peux cibler un produit specifique. "Affiche le bump seulement si le client n'a jamais achete la formation debutant." Ca te permet de proposer la formation debutant en bump aux clients qui ne l'ont pas, et un bump different aux clients qui l'ont deja.

---

**[SECTION 6 - Combiner plusieurs conditions]**

**[ECRAN - interface avec deux conditions sur un meme bump]**

Tu peux empiler les conditions. CartFlows les combine avec un "ET" logique : toutes les conditions doivent etre remplies pour que le bump s'affiche.

Exemple : affiche le bump "coaching VIP" seulement si le panier depasse 100 euros ET si le client n'a jamais achete de coaching. Les deux conditions doivent etre vraies simultanement.

Attention : plus tu ajoutes de conditions, plus tu restreins l'audience du bump. C'est bien pour la pertinence, mais si tu es trop restrictif, le bump ne s'affiche presque jamais et son impact est negligeable. Trouve le juste milieu.

---

**[SECTION 7 - Tester les rules]**

**[ECRAN - test en mode preview]**

Les conditions ne se testent pas en mode preview. Il faut faire de vrais tests.

Cree deux scenarios. Scenario A : un client qui remplit les conditions - verifie que le bump apparait. Scenario B : un client qui ne remplit pas les conditions - verifie que le bump est masque.

Pour le test d'historique d'achat, cree un compte test avec une commande precedente et un compte test sans commande. Pour le test de montant, ajoute differents produits au panier et verifie le seuil.

C'est methodique, mais c'est la seule facon de s'assurer que les rules fonctionnent. Un bump qui s'affiche au mauvais moment fait plus de mal qu'un bump absent.

---

**[OUTRO - face camera]**

Le Rules Engine transforme tes bumps generiques en offres personnalisees. Le bon bump, au bon client, au bon moment. C'est plus de travail en configuration, mais c'est aussi plus de conversions et une meilleure experience client.

Dans la prochaine lecon, on s'attaque au design et au copywriting - les mots et le visuel qui font qu'un client coche la case.

---

## Notes de production

- **Captures d'ecran necessaires** : section Rules du bump, liste des types de conditions, configuration condition montant, configuration condition historique, deux conditions combinees, tests avec deux comptes
- **Schemas** : fonctionnement du Rules Engine (condition → affichage/masquage), arbre de decision avec conditions multiples
- **Timing** : intro (1 min) → definition Rules Engine (0.5 min) → acces (0.5 min) → types de conditions (2 min) → cas pratique montant (1.5 min) → cas pratique nouveaux clients (1.5 min) → combiner conditions (1 min) → tests (1 min) → outro (0.5 min)
- **Ton** : technique mais accessible, chaque condition illustree par un cas concret - pas de theorie abstraite

# Lecon 3.6 - Gerer les variations produit dans le checkout

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 3 - Checkout optimise
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir afficher et gerer les variations de produits WooCommerce dans un checkout CartFlows - choix radio, select, pricing dynamique - et comprendre les bonnes pratiques pour ne pas nuire a la conversion.

---

## Script narration

**[INTRO - face camera]**

Tu vends un produit avec plusieurs options - une formation avec un plan basique et un plan premium, un t-shirt en trois tailles, un plugin avec une licence mensuelle ou annuelle. Comment tu geres ca dans ton checkout CartFlows ?

Par defaut, WooCommerce affiche les variations sur la page produit. Le client choisit, ajoute au panier, puis arrive au checkout. Mais avec CartFlows, tu peux afficher les variations directement dans le checkout - et ca change tout. Le client voit les options, compare, et achete. Tout sur la meme page.

---

**[SECTION 1 - Produits variables WooCommerce : le principe]**

**[ECRAN - WooCommerce → Produits → Produit variable avec attributs]**

Un produit variable dans WooCommerce, c'est un produit avec des attributs - taille, couleur, plan, duree - et des variations qui combinent ces attributs avec un prix different.

Par exemple, une formation avec deux plans : "Basique" a 47 euros et "Premium" a 97 euros. Dans WooCommerce, tu crees un produit variable avec un attribut "Plan" et deux variations - chacune avec son propre prix.

La ou ca devient interessant, c'est quand tu integres ce produit dans un flow CartFlows. Au lieu de la page produit WooCommerce classique - qui est generalement pauvre en design - tu affiches les options directement dans ton checkout optimise.

---

**[SECTION 2 - Product Options dans CartFlows]**

**[ECRAN - CartFlows checkout step → "Product Options" settings]**

CartFlows a une fonctionnalite dediee : "Product Options". Tu la trouves dans les reglages de ton checkout step, onglet "Product Options" ou "Checkout Products" selon ta version.

C'est ici que tu choisis comment les variations s'affichent. Tu as deux modes principaux.

Le premier : des boutons radio. Chaque variation apparait comme un choix cliquable avec son nom et son prix. Le client voit toutes les options d'un coup et clique sur celle qu'il veut. C'est le mode que je recommande pour 2-3 variations - c'est le plus visuel et le plus rapide.

Le deuxieme : un menu deroulant (select). Les options sont cachees dans une liste deroulante. Le client doit cliquer pour voir les choix. C'est adapte si tu as beaucoup de variations - 5 ou plus - mais pour la vente classique, les radio buttons convertissent mieux.

Pour activer les Product Options, ajoute ton produit variable dans le checkout step. CartFlows detecte automatiquement les variations et te propose le mode d'affichage. Selectionne "radio" ou "select", configure l'ordre d'affichage, et c'est en place.

---

**[SECTION 3 - Pricing dynamique : le prix qui change en direct]**

**[ECRAN - checkout en frontend avec variation selectionnee → prix total qui se met a jour]**

Quand le client change de variation dans le checkout, le prix total doit se mettre a jour instantanement. C'est ce qu'on appelle le pricing dynamique, et CartFlows le gere nativement.

Tu selectionnes le plan Basique a 47 euros - le total affiche 47 euros. Tu cliques sur Premium a 97 euros - le total passe a 97 euros. Pas de rechargement de page, pas de delai. Le changement est immediat.

C'est important parce que le client prend sa decision en voyant le prix final. S'il doit deviner ou calculer, tu perds en conversion. Le prix affiche doit toujours correspondre exactement a ce qu'il va payer.

Dans CartFlows, le pricing dynamique est actif par defaut quand tu utilises les Product Options avec un produit variable. Tu n'as rien a configurer - verifie juste en preview que le total se met bien a jour quand tu changes de variation.

---

**[SECTION 4 - Cas pratique : formation avec 2 plans]**

**[ECRAN - creation pas a pas d'un checkout avec 2 plans de formation]**

On met ca en pratique. Tu vends une formation WordPress avec deux plans :

- **Plan Basique** - 47 euros : acces au cours, pas de support
- **Plan Premium** - 97 euros : acces au cours + support email + bonus

Dans WooCommerce, cree un produit variable. Ajoute un attribut "Plan" avec les valeurs "Basique" et "Premium". Cree les deux variations avec leurs prix respectifs.

Dans CartFlows, cree un flow de vente. Ajoute un checkout step. Dans les Product Options, ajoute ton produit variable. Selectionne l'affichage "radio buttons".

Le resultat sur la page checkout : le client voit deux options claires, avec le nom du plan et le prix. Il clique sur son choix, le total se met a jour, et il paie. C'est propre, c'est rapide, et c'est exactement ce que tu veux.

Un detail qui fait la difference : mets le plan le plus cher en premier. C'est l'effet d'ancrage - le client voit 97 euros d'abord, puis 47 euros parait "raisonnable" en comparaison. Ou alors, pre-selectionne le plan que tu veux vendre le plus. CartFlows te laisse choisir la variation par defaut.

---

**[SECTION 5 - Bonnes pratiques : la regle des 3 variantes maximum]**

**[ECRAN - exemple a 2 variantes (clean) vs exemple a 6 variantes (encombre)]**

Dernier point, et c'est un conseil que tu dois graver dans ta tete : maximum 3 variantes visibles dans ton checkout. Au-dela, tu complexifies la decision et tu baisses la conversion.

Le paradoxe du choix est reel. Plus tu donnes d'options, plus le client hesite, et plus il risque de ne rien choisir du tout. Trois options, c'est le sweet spot - une option economique, une option standard, une option premium. Le client se positionne facilement.

Si tu as un produit avec plus de 3 variations - par exemple un t-shirt en 6 tailles - gere les tailles sur la page produit WooCommerce, pas dans le checkout CartFlows. Le checkout doit rester simple : un choix deja fait, un prix clair, un bouton de paiement.

En resume : les variations dans le checkout CartFlows, c'est pour les choix strategiques - plan, formule, niveau d'acces. Pas pour les choix logistiques comme la taille ou la couleur.

---

**[CONCLUSION - face camera]**

Les Product Options de CartFlows te permettent d'afficher les variations directement dans le checkout - radio buttons ou select. Le pricing se met a jour en temps reel. Et la regle d'or : maximum 3 variantes visibles pour ne pas paralyser la decision du client.

Dans la prochaine lecon, on parle methodes de paiement - Stripe, PayPal, Apple Pay - et comment les configurer pour maximiser ta conversion.

---

## Notes de production

- **Visuels requis** : produit variable WooCommerce (attributs + variations), CartFlows Product Options settings, checkout frontend avec radio buttons et prix dynamique, comparaison 2 vs 6 variantes
- **Captures d'ecran** : WooCommerce edit product (variations tab), CartFlows checkout step Product Options, frontend checkout avec 2 plans de formation, exemple d'ancrage prix
- **Points d'insistance voix** : "Maximum 3 variantes visibles" (section 5), "Le prix affiche doit toujours correspondre exactement a ce qu'il va payer" (section 3)
- **Transitions** : progression logique - concept → outil → pratique → limites

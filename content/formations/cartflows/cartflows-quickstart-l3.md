# Lecon 3 - Creer ton premier funnel avec un template

## Metadata

- **Formation** : CartFlows Quick Start (offerte - FRM-006)
- **Lecon** : 3/5
- **Duree cible** : 15 min
- **Objectif pedagogique** : Creer un funnel complet a partir d'un template, connecter un produit WooCommerce au checkout, personnaliser les textes et le design, puis previsualiser le resultat.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

C'est la lecon la plus importante de toute la formation. Dans les 15 prochaines minutes, tu vas creer ton premier funnel de vente complet - de zero jusqu'a une page fonctionnelle.

Dans la lecon precedente, tu as installe CartFlows et verifie que tout etait en place. Maintenant, on passe a la construction. On va utiliser un template de la bibliotheque CartFlows, le connecter a un vrai produit WooCommerce, personnaliser les textes et le design, et terminer avec un funnel pret a recevoir du trafic.

Ouvre ton tableau de bord WordPress, on y va.

---

[SECTION 1 - Creer un nouveau Flow]

Dans le menu lateral, clique sur CartFlows, puis sur Flows. C'est ici que tu retrouves tous tes funnels. Pour l'instant, la liste est vide - ou tu as peut-etre le flow par defaut que CartFlows a cree a l'installation.

Clique sur le bouton "Add New" en haut de la page. CartFlows t'ouvre sa bibliotheque de templates. C'est un catalogue de funnels pre-construits, classes par categorie.

Prends quelques secondes pour regarder ce qui est disponible. Tu vas voir plusieurs categories : Sales, Optin, Webinar, Lead Magnet, et d'autres. Chaque template correspond a un type de parcours de vente different.

Voici ce qui nous interesse pour l'instant :

Les templates "Sales" sont conçus pour vendre un produit directement - checkout + page de remerciement. C'est le cas le plus courant.

Les templates "Optin" servent a capturer des emails avant d'envoyer le visiteur vers un checkout ou une page de contenu.

Les templates "Webinar" et "Lead Magnet" combinent capture d'email et page de confirmation - parfaits pour offrir un contenu gratuit en echange d'une inscription.

Pour cette lecon, choisis un template de type "Sales". C'est le plus simple et le plus concret pour demarrer. Si tu as la version gratuite de CartFlows, tu auras acces a quelques templates de base - c'est largement suffisant. Les templates premium sont reserves a la version Pro.

Selectionne un template qui te plait visuellement. Ne passe pas 20 minutes a choisir - on va tout personnaliser de toute façon. L'important, c'est la structure, pas les couleurs.

---

[SECTION 2 - Comprendre la structure d'un Flow]

Avant d'aller plus loin, je veux que tu comprennes ce que tu viens d'importer. Un Flow dans CartFlows, c'est un parcours de vente compose de plusieurs etapes - les "Steps".

Un template Sales classique contient trois steps :

Premier step : la Landing Page. C'est la page d'atterrissage, celle ou le visiteur arrive en premier. Elle presente ton offre, ton produit, tes arguments de vente. Son objectif : convaincre le visiteur de cliquer sur le bouton d'achat.

Deuxieme step : la Checkout Page. C'est le coeur de ton funnel. C'est ici que le visiteur entre ses informations de paiement et valide sa commande. CartFlows remplace le checkout standard de WooCommerce par une page optimisee, plus propre et plus performante.

Troisieme step : la Thank You Page. C'est la page de confirmation qui s'affiche apres le paiement. Elle confirme la commande, remercie le client, et peut proposer une action suivante - telechargement, acces a un espace membre, offre complementaire.

Voici un point important : tu n'es pas oblige d'utiliser les trois steps. Si tu veux aller vite, tu peux tres bien desactiver la Landing Page et envoyer les visiteurs directement sur le Checkout. C'est ce que je recommande pour un premier funnel - moins de pages a personnaliser, un parcours plus direct. Tu pourras toujours ajouter une Landing Page plus tard.

Le minimum vital, c'est : un Checkout et une Thank You Page. Avec ces deux pages, tu as un funnel fonctionnel.

---

[SECTION 3 - Importer le template]

Revenons a la bibliotheque. Tu as selectionne ton template - clique sur "Import" pour l'ajouter a ton site.

CartFlows te demande de nommer ton Flow. Donne-lui un nom clair - par exemple "Funnel Formation WordPress" ou "Vente Ebook SEO". Choisis un nom qui te permet de le retrouver facilement. Ce nom n'est visible que dans ton admin, pas par tes visiteurs.

Valide. L'import prend quelques secondes - CartFlows cree les pages, applique le design du template, et configure la structure du flow.

Une fois termine, tu arrives sur la page de ton Flow. Tu vois la liste des steps, dans l'ordre : Landing Page, Checkout, Thank You. Chaque step a un bouton "Edit" a droite. C'est par la qu'on va travailler.

---

[SECTION 4 - Connecter un produit WooCommerce]

On attaque le plus important : connecter un produit reel a ton checkout. Sans produit, ton funnel n'a aucune utilite.

Dans la liste des steps, clique sur "Edit" a cote du step Checkout. Tu arrives sur la page de configuration du checkout. Cherche l'onglet "Product" ou descends jusqu'a la section "Select Product".

Clique sur le champ de recherche de produit. CartFlows va te montrer la liste de tes produits WooCommerce. Selectionne le produit que tu veux vendre dans ce funnel.

Si tu n'as pas encore de produit, retourne dans WooCommerce, Produits, Ajouter, et cree un produit simple - meme a 1 euro pour tester. Ca prend 2 minutes. Ensuite, reviens ici.

Une fois le produit selectionne, tu as quelques options supplementaires :

La quantite - laisse a 1 par defaut sauf si tu veux forcer un pack.

Le prix affiche - par defaut, CartFlows reprend le prix du produit WooCommerce. Tu peux le laisser tel quel pour l'instant.

L'option "Enable Product Options" te permet d'afficher plusieurs variantes ou produits sur le meme checkout. C'est utile plus tard, mais pour un premier funnel, garde les choses simples - un seul produit.

Sauvegarde tes modifications en cliquant sur "Update" ou "Enregistrer" en haut de la page. Ton checkout est maintenant connecte a un produit reel.

---

[SECTION 5 - Personnaliser les textes]

Le template que tu as importe contient du texte generique - souvent en anglais. C'est normal, on va tout remplacer.

Trois elements cles a personnaliser :

Premierement, le titre de la page checkout. C'est le premier texte que le visiteur voit. Remplace le titre par defaut par quelque chose de clair et specifique. Par exemple : "Finalise ta commande" ou "Accede a ta formation maintenant". Evite les titres vagues comme "Checkout" - ca ne donne envie a personne.

Deuxiemement, la description du produit sur le checkout. CartFlows peut afficher un resume du produit au-dessus du formulaire de paiement. C'est l'endroit ideal pour rappeler ce que le visiteur va recevoir - une phrase ou deux, pas plus. Par exemple : "Formation WordPress - 12 modules video + acces a vie".

Troisiemement, le texte du bouton d'action - le CTA. Par defaut, WooCommerce met "Commander". C'est plat. Remplace-le par un texte qui indique clairement ce qui va se passer : "Acceder a la formation", "Recevoir mon guide", "Demarrer maintenant". Le bouton doit repondre a la question : "Qu'est-ce que j'obtiens quand je clique ?"

Pour modifier le texte du CTA, reste dans les reglages du step Checkout. Cherche la section "Checkout Offer" ou "Place Order Button Text" - c'est la que tu saisis le nouveau texte du bouton.

Si tu veux aller plus loin sur la personnalisation des champs du formulaire - reduire le nombre de champs, reordonner, supprimer les champs inutiles - on fera ca en detail dans la lecon suivante. Pour l'instant, concentre-toi sur ces trois textes.

---

[SECTION 6 - Personnaliser le design avec le page builder]

Les textes sont en place. Maintenant, on va ajuster le visuel pour que le funnel ressemble a ta marque et pas a un template generique.

Dans la page du step Checkout, clique sur le bouton "Edit" pour ouvrir l'editeur Gutenberg. Le bouton se trouve en haut de la page, juste en dessous du titre. Si tu as Kadence Blocks installe, tu auras acces a tous les blocs avances pour personnaliser ta page.

L'editeur visuel s'ouvre avec le design du template. Tu peux tout modifier : couleurs, polices, images, espacement, mise en page.

Mais attention - ne tombe pas dans le piege de la personnalisation infinie. Pour un premier funnel, limite-toi a trois choses :

Premiere chose : les couleurs. Remplace les couleurs du template par celles de ta marque. Couleur principale pour les boutons et les liens, couleur secondaire pour les accents. C'est tout. Pas besoin de 12 nuances differentes.

Deuxieme chose : les images. Si le template contient des images placeholder, remplace-les par tes propres visuels. Une image du produit, ton logo. Si tu n'as pas d'images pretes, supprime les placeholders - une page clean sans images vaut mieux qu'une page avec des photos generiques de banques d'images.

Troisieme chose : le texte restant. Parcours la page du haut en bas et remplace tout ce qui est encore en anglais ou generique. Titres de section, sous-titres, labels - tout doit etre en français et correspondre a ton offre.

Un conseil important : garde le design simple et lisible. Un checkout qui convertit, c'est un checkout ou le visiteur comprend immediatement ce qu'il achete, combien ca coute, et ou cliquer pour payer. Pas besoin d'animations, de sliders, ou de sections compliquees. Moins il y a de distractions, mieux c'est.

Fais la meme chose pour la Thank You Page. Clique sur "Edit" a cote du step Thank You, ouvre l'editeur, et personnalise : titre de confirmation, message de remerciement, et eventuellement un lien vers le contenu achete ou une prochaine etape.

Une fois que tu as termine, sauvegarde dans l'editeur, puis retourne sur la page du Flow.

---

[SECTION 7 - Sauvegarder et previsualiser]

Ton funnel est construit. Produit connecte, textes personnalises, design ajuste. Avant de l'envoyer au monde, on va verifier que tout fonctionne.

Dans la page du Flow, a cote de chaque step, tu as un bouton "View" ou une icone d'oeil. Clique dessus pour chaque page - Landing (si tu l'as gardee), Checkout, et Thank You.

Verifie ces points sur le Checkout :

Le nom du produit et le prix sont corrects. Le formulaire de paiement s'affiche bien. Le texte du bouton CTA est celui que tu as defini. La page est lisible sur mobile - redimensionne ta fenetre de navigateur ou utilise l'outil responsive de ton navigateur pour verifier.

Sur la Thank You Page, verifie que le message de confirmation s'affiche et que les informations sont coherentes.

Si quelque chose ne va pas - mauvais produit, texte manquant, bouton par defaut - retourne dans le step concerne, corrige, et sauvegarde.

A ce stade, tu peux aussi faire une commande test pour verifier le parcours complet. Active un moyen de paiement test dans WooCommerce - le virement bancaire fonctionne pour tester sans carte - et passe une commande fictive pour voir le flow de bout en bout.

---

[SECTION 8 - Le conseil qui change tout]

Je vais te donner le meilleur conseil de cette formation : commence simple.

Un produit. Un checkout. Une page merci. C'est tout ce dont tu as besoin pour demarrer.

Beaucoup de gens passent des semaines a peaufiner leur funnel avant de le mettre en ligne. Ils veulent la landing page parfaite, les upsells, les order bumps, l'A/B testing. Resultat : ils ne lancent jamais.

Toi, tu vas faire l'inverse. Tu vas mettre ce funnel en ligne avec le strict minimum, envoyer du trafic dessus, et voir ce qui se passe. Les premieres commandes - meme si c'est une seule - vont te donner des vraies donnees. Et c'est avec ces donnees que tu optimiseras ensuite.

Les order bumps, les upsells en un clic, l'A/B testing entre deux designs - tout ça existe dans CartFlows Pro. Et on verra tout ça en detail dans la Masterclass. Mais pour l'instant, ton objectif est simple : un funnel en ligne, qui fonctionne, qui encaisse des paiements.

---

[OUTRO]

Recapitulons. Dans cette lecon, tu as :

Cree un nouveau Flow a partir d'un template de la bibliotheque CartFlows. Compris la structure d'un funnel - Landing Page, Checkout, Thank You Page. Connecte un produit WooCommerce reel a ton checkout. Personnalise les textes - titre, description, bouton CTA. Ajuste le design avec ton page builder - couleurs, images, textes. Et previsualise le resultat pour verifier que tout fonctionne.

Tu as maintenant un funnel de vente complet. Dans la prochaine lecon, on va aller plus loin dans la personnalisation du checkout - simplifier le formulaire, ajouter des elements de confiance, et tester le parcours de bout en bout avec une vraie commande.

On se retrouve dans la lecon 4.

---

## Notes de production

### Captures d'ecran suggerees

1. **CartFlows > Flows** - Liste des flows, bouton "Add New"
2. **Bibliotheque de templates** - Vue d'ensemble avec les categories (Sales, Optin, Webinar, Lead Magnet)
3. **Template Sales selectionne** - Preview du template avant import
4. **Import + nommage** - Champ de nom du Flow
5. **Vue du Flow cree** - Liste des 3 steps (Landing, Checkout, Thank You) avec boutons Edit
6. **Step Checkout > Product** - Champ de recherche produit WooCommerce
7. **Produit selectionne** - Produit visible dans le checkout avec prix et quantite
8. **Texte CTA** - Champ "Place Order Button Text" avec le texte personnalise
9. **Editeur Gutenberg + Kadence Blocks** - Page checkout ouverte dans l'editeur
10. **Couleurs personnalisees** - Bouton CTA avec la couleur de marque appliquee
11. **Thank You Page** - Page de confirmation personnalisee dans l'editeur
12. **Preview Checkout** - Vue front-end de la page checkout finalisee
13. **Preview mobile** - Meme page en version responsive
14. **Preview Thank You** - Vue front-end de la page de confirmation

### Transitions

- Intro → Section 1 : cut direct sur le dashboard CartFlows
- Section 1 → Section 2 : pause pedagogique - retour avatar pour expliquer la structure
- Section 2 → Section 3 : retour sur l'ecran de la bibliotheque de templates
- Section 3 → Section 4 : transition sur la page du Flow avec les steps
- Section 4 → Section 5 : enchaînement direct, on reste sur le step Checkout
- Section 5 → Section 6 : transition vers l'ouverture du page builder
- Section 6 → Section 7 : retour sur la page du Flow, boutons "View"
- Section 7 → Section 8 : retour avatar, changement de ton (conseil)
- Section 8 → Outro : retour avatar, recap

### Notes avatar / voix

- Rythme pose mais dynamique - c'est la lecon la plus longue, il faut maintenir l'attention
- Section 2 (structure du flow) : ton pedagogique, prendre le temps d'expliquer - c'est un concept cle
- Section 4 (produit) : rythme technique, etape par etape, laisser le temps de suivre
- Section 6 (design) : insister sur "garde ça simple" - ton direct, presque autoritaire
- Section 8 (conseil) : ton complice et motivant - c'est le moment ou on pousse a l'action
- Prevoir une pause de 1-2 secondes entre chaque section pour les transitions ecran

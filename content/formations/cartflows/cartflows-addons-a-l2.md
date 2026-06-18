# Lecon A.2 - Installer et configurer Modern Cart Free

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : A - Modern Cart
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Installer Modern Cart depuis le repertoire WordPress, completer le wizard de configuration, et valider le fonctionnement du side cart sur la boutique.

---

## Script narration

**[INTRO - face camera]**

On passe a la pratique. Dans cette lecon, tu vas installer Modern Cart, le configurer avec le wizard integre, et verifier que le side cart fonctionne correctement sur ta boutique. En 8 minutes, ton panier lateral sera operationnel.

---

**[SECTION 1 - Installation depuis le repertoire WordPress]**

**[ECRAN - dashboard WordPress → Extensions → Ajouter]**

L'installation est standard. Dans ton dashboard WordPress, va dans Extensions puis Ajouter. Dans la barre de recherche, tape "modern cart". Le plugin s'appelle "Modern Cart - Free WooCommerce Side Cart" par Starter Templates / Brainstorm Force.

Clique sur Installer maintenant, puis Activer.

Un point important : Modern Cart necessite WooCommerce actif. Si WooCommerce n'est pas installe, le plugin ne s'activera pas. Mais si tu suis la formation CartFlows, WooCommerce est deja en place.

Apres activation, tu vas voir une notification en haut du dashboard qui t'invite a lancer le wizard de configuration. C'est exactement ce qu'on va faire.

---

**[SECTION 2 - Le wizard de configuration]**

**[ECRAN - wizard Modern Cart etape par etape]**

Le wizard te guide en quelques etapes. C'est bien fait - il couvre l'essentiel sans te noyer dans les options.

**Etape 1 - Declencheur.** Modern Cart te demande quand le side cart doit s'ouvrir. L'option par defaut et la plus logique : a chaque fois qu'un client clique sur "Ajouter au panier". C'est ce que tu veux. Le client ajoute un produit, le panneau glisse immediatement pour confirmer l'ajout. Garde cette option.

**Etape 2 - Position.** Le side cart peut s'ouvrir a droite ou a gauche de l'ecran. La convention e-commerce, c'est a droite. La majorite des utilisateurs sont droitiers, le regard se porte naturellement a droite. Sauf si ton menu principal est a droite et que ca cree un conflit visuel, reste sur droite.

**Etape 3 - Icone flottante.** Le wizard te propose d'activer une icone de panier flottante - un petit bouton sticky qui reste visible en permanence quand le client scrolle. Active-la. On verra les details de personnalisation dans la lecon A.4, mais pour l'instant, active-la avec les reglages par defaut.

**Etape 4 - Couleurs de base.** Le wizard te propose de choisir les couleurs principales du side cart : fond, texte, bouton "Commander". La regle : aligne-toi sur ta charte graphique. Si ton theme Kadence utilise un bleu principal, utilise le meme bleu pour le bouton du side cart. La coherence visuelle renforce la confiance.

Valide le wizard. Modern Cart est maintenant actif sur ta boutique.

---

**[SECTION 3 - Personnaliser les couleurs pour ta charte]**

**[ECRAN - Modern Cart → Settings → Apparence]**

Apres le wizard, tu peux affiner les couleurs dans les reglages du plugin. Va dans Modern Cart dans le menu lateral, puis Settings.

Tu as acces a plusieurs elements :

- **Fond du side cart** : blanc ou clair par defaut. Garde un fond neutre pour que les produits ressortent.
- **Couleur du texte** : noir ou gris fonce. Assure-toi que le contraste est suffisant pour la lisibilite.
- **Bouton principal** ("Passer commande" ou "Checkout") : c'est le bouton d'action. Utilise ta couleur d'accent - celle qui attire l'oeil. Meme couleur que tes boutons "Ajouter au panier" idealement.
- **Bouton secondaire** ("Continuer les achats") : plus discret. Un gris ou un contour simple.

Un piege courant : vouloir trop personnaliser des le depart. Commence avec des reglages simples et coherents. Tu optimiseras apres avoir observe le comportement de tes clients.

---

**[SECTION 4 - Premier test : ajouter un produit]**

**[ECRAN - page boutique front-end, ajout produit, side cart qui s'ouvre]**

Le moment de verite. Ouvre ta boutique en mode front-end - soit en navigation privee, soit en te deconnectant de l'admin.

Va sur une page produit ou une page boutique. Clique sur "Ajouter au panier".

Le side cart doit s'ouvrir immediatement depuis le cote droit (ou gauche si tu as choisi cette option). Tu dois voir :

- Le produit ajoute avec son image et son nom
- La quantite (modifiable avec + et -)
- Le prix unitaire et le sous-total
- Un bouton "Supprimer" pour retirer le produit
- Le total du panier en bas
- Le bouton "Passer commande" ou "Checkout"

Si tout ca s'affiche correctement, Modern Cart fonctionne. Ajoute un deuxieme produit pour verifier que la liste se met a jour en temps reel dans le side cart.

---

**[SECTION 5 - Verifications supplementaires]**

**[ECRAN - test mobile + test fermeture]**

Quelques verifications importantes avant de passer a la suite.

**Fermeture du side cart.** Clique en dehors du panneau ou sur le X de fermeture. Le side cart doit se refermer proprement. Le client doit pouvoir ouvrir et fermer le panneau sans probleme.

**Test sur mobile.** Ouvre ta boutique sur ton telephone ou utilise l'outil de responsive de ton navigateur (F12 puis mode mobile). Le side cart doit s'adapter a l'ecran - il prend generalement toute la largeur sur mobile. Verifie que les boutons sont assez grands pour etre cliques au doigt.

**Compatibilite theme.** Avec Kadence, la compatibilite est excellente - les deux plugins viennent du meme ecosysteme Brainstorm Force. Si tu utilises un autre theme, verifie qu'il n'y a pas de conflit CSS (elements qui se superposent, boutons non cliquables).

**Cache.** Si tu utilises un plugin de cache (LiteSpeed, WP Super Cache, etc.), vide le cache apres l'installation. Le side cart utilise du JavaScript qui doit etre charge correctement.

---

**[CONCLUSION - face camera]**

Modern Cart est installe et fonctionnel. En quelques minutes, tu as remplace le parcours page panier classique par un panneau lateral fluide.

Dans la prochaine lecon, on va aller plus loin dans le design : animations, largeur du panneau, et optimisation du rendu visuel.

---

## Notes de production

- **Visuels** : capture ecran installation plugin, wizard etape par etape, page boutique avec side cart ouvert, test mobile
- **Attention** : montrer le wizard reel de Modern Cart - les etapes peuvent varier selon la version du plugin
- **Prerequis** : WooCommerce actif avec au moins 2 produits publies pour les tests
- **Transition** : enchaine sur LA.3 (design du panier lateral)

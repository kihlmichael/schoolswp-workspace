# Lecon 5.2 - Site e-commerce : boutique SureCart + WooCommerce

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 5 - Sites business avec ZipWP
- **Lecon** : 2/8
- **Duree cible** : 12 min
- **Objectif pedagogique** : Installer et configurer les deux options e-commerce avec ZipWP - SureCart pour les produits digitaux et abonnements, WooCommerce pour les catalogues et produits physiques - et savoir laquelle choisir.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Tu veux vendre en ligne avec ton site ZipWP. Bonne nouvelle : tu as deux options solides. SureCart - un produit Brainstorm Force, leger et moderne. Et WooCommerce - le standard WordPress du e-commerce, avec son ecosysteme massif.

Mais ces deux outils ne ciblent pas le meme usage. Le bon choix depend de ce que tu vends, combien de produits tu as, et ou tu veux aller. On installe et configure les deux, et tu decides a la fin.

---

[SECTION 1 - SureCart : leger, rapide, ideal pour demarrer]

SureCart, c'est le e-commerce by Brainstorm Force. Et sa philosophie est claire : faire moins, mais le faire mieux.

Installe SureCart depuis le dashboard WordPress : Extensions → Ajouter → cherche "SureCart" → Installer → Activer. Un assistant de configuration se lance automatiquement. Entre le nom de ta boutique, ta devise, et connecte Stripe - c'est le systeme de paiement par defaut. La configuration Stripe prend 3 minutes si tu as deja un compte.

Cree ton premier produit. Dans le menu SureCart, clique sur "Products" → "Add New". Donne un nom, une description, un prix. Ajoute une image. Si c'est un produit digital - un ebook, un template, une formation - uploade le fichier directement. SureCart gere la livraison numerique nativement.

Le checkout SureCart est integre a Spectra. Tu peux ajouter un bouton d'achat directement dans n'importe quelle page avec un bloc Spectra. Le visiteur clique, un panneau lateral s'ouvre avec le checkout. Pas de redirection vers une page externe, pas de temps de chargement supplementaire. C'est fluide.

SureCart brille sur trois points : les abonnements - tu peux creer un paiement recurrent en 2 clics. Les produits digitaux - la livraison est automatique. Et la vitesse - aucun impact sur les performances du site parce que le traitement se fait cote SureCart, pas cote WordPress.

---

[SECTION 2 - WooCommerce : complet, extensible, le standard]

WooCommerce, c'est l'autre option. Et c'est un mastodonte : plus de 5 millions de boutiques actives dans le monde.

Installe WooCommerce : Extensions → Ajouter → "WooCommerce" → Installer → Activer. L'assistant est plus long que SureCart - il te pose des questions sur ton secteur, tes produits, ta localisation. Configure Stripe comme moyen de paiement (l'extension WooCommerce Stripe est gratuite).

Cree un produit : Produits → Ajouter. Tu retrouves un editeur plus detaille - prix regulier, prix promo, SKU, gestion de stock, categories, tags, attributs, variations (taille, couleur). WooCommerce gere tout ca nativement.

WooCommerce brille sur trois points : le catalogue - tu peux gerer des centaines de produits avec des variations complexes. Les produits physiques - gestion du stock, des livraisons, des taxes. L'ecosysteme - des milliers d'extensions pour ajouter des fonctionnalites (Mondial Relay, Colissimo, factures PDF, programmes de fidelite).

Le revers : WooCommerce est plus lourd. Chaque extension ajoute du code, des requetes en base de donnees, du temps de chargement. Sur un site ZipWP optimise avec Astra et Spectra, tu veux garder ce poids sous controle.

---

[SECTION 3 - Configurer le paiement Stripe]

Que tu choisisses SureCart ou WooCommerce, Stripe est le passage oblige. C'est le processeur de paiement le plus fiable pour WordPress.

Pour SureCart : la connexion se fait dans l'assistant de configuration. Clique sur "Connect Stripe", autorise l'acces, c'est fait. Stripe gere les cartes bancaires, Apple Pay, Google Pay.

Pour WooCommerce : installe l'extension "WooCommerce Stripe Gateway" - elle est gratuite. Va dans WooCommerce → Reglages → Paiements → Stripe. Entre tes cles API (tu les trouves dans ton dashboard Stripe → Developers → API Keys). Active le mode test pour verifier que tout fonctionne avant de passer en production.

Conseil important : fais toujours un achat test. Cree un produit a 1 euro, achete-le toi-meme avec Stripe en mode test, verifie que tu recois le mail de confirmation, que le produit est livre (si digital), et que la commande apparait dans le dashboard. Ne mets jamais une boutique en ligne sans avoir teste le parcours complet.

---

[SECTION 4 - SureCart vs WooCommerce : le guide de decision]

Mettons les deux cote a cote.

SureCart : ideal pour les produits digitaux (ebook, template, formation). Parfait pour les abonnements et paiements recurrents. Checkout rapide et integre. Moins de 20 produits. Pas d'impact sur les performances WordPress. Dashboard moderne et intuitif. Limite : pas de gestion de stock physique, pas de variations complexes.

WooCommerce : ideal pour les produits physiques. Gestion de stock, variations, livraisons. Catalogue de 20 a 10 000 produits. Ecosysteme d'extensions massif. Gestion des taxes avancee. Limite : plus lourd, necessite plus de maintenance, courbe d'apprentissage plus longue.

Le conseil schoolsWP : SureCart si tu vends moins de 20 produits. WooCommerce au-dela. Et si tu demarres et que tu ne sais pas encore - commence par SureCart. Tu pourras toujours migrer vers WooCommerce quand ton catalogue grandira.

Un point important : les deux fonctionnent avec Astra et Spectra. Ton site ZipWP reste coherent visuellement quel que soit ton choix.

---

[SECTION 5 - Integration avec le site ZipWP]

Derniere etape : integrer ta boutique dans la navigation du site.

Avec SureCart, ajoute tes blocs produits directement dans les pages Spectra. Pas besoin d'une page "Boutique" separee - tu peux integrer les boutons d'achat dans tes pages existantes. Un bouton "Acheter" sur ta page Services, un autre sur ta page d'accueil.

Avec WooCommerce, tu as une page "Boutique" automatiquement creee. Ajoute-la dans ton menu principal : Apparence → Menus → ajoute la page "Boutique". Si tu veux des produits sur d'autres pages, utilise les blocs WooCommerce dans l'editeur Gutenberg - "Produits par categorie", "Produits en vedette", "Produit unique".

Dans les deux cas, verifie sur mobile. Le checkout doit etre fluide sur smartphone - c'est la que la majorite de tes visiteurs va acheter.

---

[OUTRO]

Tu as maintenant deux chemins clairs pour vendre en ligne avec ZipWP. SureCart pour rester leger et rapide. WooCommerce pour un catalogue complet et extensible. Le paiement Stripe est configure, ton premier produit est cree, et la boutique est integree a ton site.

Dans la prochaine lecon, on attaque le use case schoolsWP par excellence : un site de formation avec ZipWP et TutorLMS. Le duo pour creer une veritable ecole en ligne.

---

## Notes de production

### Captures d'ecran suggerees

1. **Installation SureCart** - Ecran d'activation et assistant de configuration
2. **Checkout SureCart** - Panneau lateral de checkout integre dans une page Spectra
3. **Dashboard WooCommerce** - Creation d'un produit avec variations
4. **Stripe config** - Cles API dans le dashboard Stripe
5. **Comparatif** - Tableau SureCart vs WooCommerce (split screen)

### Transitions

- Intro → Section 1 : ouverture dashboard WP, installation SureCart
- Section 1 → Section 2 : transition vers installation WooCommerce
- Section 2 → Section 3 : zoom sur la configuration Stripe
- Section 3 → Section 4 : split screen comparatif
- Section 4 → Section 5 : retour sur le site, integration boutique
- Section 5 → Outro : vue du site final avec boutique active

### Notes HeyGen / ElevenLabs

- Ton pratique et comparatif - pas de favoritisme, presenter les deux options objectivement
- Section 1 et 2 : rythme tutoriel, montrer les etapes a l'ecran
- Section 4 (comparatif) : rythme plus lent, chaque critere bien pose
- Insister sur le conseil "SureCart si moins de 20 produits" - c'est la regle memorisable

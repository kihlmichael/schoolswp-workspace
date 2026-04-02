# Lecon 4 — Personnaliser le checkout

## Metadata
- Formation : CartFlows Quick Start (FRM-006, offerte)
- Duree cible : 10 min
- Objectif pedagogique : Configurer un checkout optimise (champs, branding, trust signals) et valider le parcours avec une commande test

## Script narration

[INTRO]

Dans la lecon precedente, tu as cree ton premier funnel avec un template et connecte un produit WooCommerce. Le squelette est la. Maintenant, on va transformer ce checkout generique en une page qui inspire confiance et qui convertit.

On va faire trois choses : simplifier le formulaire, appliquer ton branding, et ajouter des elements de confiance. Ensuite, on teste tout de bout en bout. C'est parti.

---

[SECTION 1 — Acceder aux reglages du checkout]

Ouvre ton dashboard WordPress, va dans CartFlows, puis clique sur ton flow. Tu vois la liste des steps : Landing, Checkout, Thank You. Clique sur "Edit" a cote du step Checkout.

Tu arrives sur les reglages specifiques de ce step. C'est ici que tu controles tout : les champs du formulaire, le layout, les couleurs. L'onglet qui nous interesse en premier, c'est "Checkout Layout".

CartFlows te propose plusieurs dispositions : one-column, two-column, ou two-step. Pour un produit simple, le one-column fonctionne tres bien. Si tu vends un produit physique avec adresse de livraison, le two-column est plus lisible. Choisis ce qui correspond a ton cas et passons aux champs.

---

[SECTION 2 — Modifier les champs du formulaire]

Descends jusqu'a la section "Checkout Fields". Tu vois la liste complete des champs que WooCommerce affiche par defaut. Et franchement, il y en a trop.

Voici la regle : chaque champ supplementaire dans ton formulaire est un obstacle. Des etudes montrent qu'un formulaire reduit de 10 a 6 champs peut augmenter le taux de conversion de 15 a 20%. Chaque champ que tu supprimes, c'est un frein en moins pour ton client.

Les champs a garder absolument :
- Prenom — pour personnaliser les emails de confirmation et les sequences de relance
- Email — c'est le minimum vital, c'est par la que passe la confirmation de commande
- Adresse — uniquement si tu vends un produit physique qui doit etre livre

Les champs a supprimer :
- Nom de societe — sauf si tu cibles exclusivement du B2B, ce champ n'apporte rien. La plupart de tes clients vont le laisser vide ou ecrire n'importe quoi. Supprime-le.
- Notes de commande — ce champ est un vestige du checkout WooCommerce classique. Personne ne l'utilise, et il allonge visuellement ton formulaire. Supprime-le.
- Telephone — si tu n'en as pas besoin pour la livraison ou le support, retire-le. Un champ telephone fait hesiter les acheteurs qui craignent d'etre deranges.

Pour supprimer un champ dans CartFlows, c'est simple : passe-le en "Hidden" ou desactive-le via le toggle. Tu peux aussi reordonner les champs par glisser-deposer pour que le parcours soit logique : prenom, email, puis adresse si necessaire.

Et voici le conseil cle de cette lecon : si tu vends un produit digital — une formation, un ebook, un template — tu n'as pas besoin de l'adresse physique. Supprime-la. Moins de champs, c'est plus de conversions. Ton client veut payer vite et acceder a son achat. Ne le ralentis pas.

---

[SECTION 3 — Ajouter le logo et les couleurs de ta marque]

Ton checkout doit ressembler a ton site. Si ton client arrive sur une page de paiement qui n'a rien a voir avec ce qu'il vient de voir, il va douter. Et le doute tue les conversions.

Ouvre ton step Checkout avec l'editeur — dans notre cas, Gutenberg avec Kadence Blocks. Tu retrouves la page comme n'importe quelle autre page WordPress.

Premiere chose : ajoute ton logo en haut de la page. Utilise un widget Image, place-le dans un conteneur centre en haut de page. Pas besoin de menu de navigation — tu ne veux pas que le client quitte le checkout. Le logo seul suffit pour rassurer sur l'identite du site.

Deuxieme chose : applique tes couleurs. Va dans les reglages du formulaire CartFlows et modifie les couleurs des boutons, des champs et du texte pour qu'elles correspondent a ta charte graphique. Le bouton d'achat doit etre dans ta couleur d'action principale — celle que tu utilises pour les CTA sur le reste de ton site.

Verifie aussi la typographie. Si ton site utilise une police specifique, applique-la ici. La coherence visuelle entre ta page de vente et ton checkout rassure le visiteur : il sait qu'il est au bon endroit.

---

[SECTION 4 — Ajouter des elements de confiance]

Le checkout, c'est le moment ou tu demandes a quelqu'un de sortir sa carte bancaire. Il faut le rassurer. Trois elements font la difference.

Premier element : les badges de paiement securise. Ajoute sous le bouton de commande une ligne avec les logos des moyens de paiement acceptes — Visa, Mastercard, PayPal si tu l'utilises — et un petit cadenas avec la mention "Paiement securise SSL". Tu peux trouver des icones libres de droit ou utiliser celles fournies par ton theme. Place-les juste sous le bouton d'action, la ou le regard se pose naturellement.

Deuxieme element : la garantie satisfaction. Si tu offres une garantie — 14 jours, 30 jours — affiche-la clairement. Un simple texte comme "Garantie satisfait ou rembourse 30 jours" avec une icone de bouclier ou de check fait l'affaire. C'est un signal puissant : le client se dit "je ne risque rien".

Troisieme element : la politique de retour. Ajoute un lien discret vers ta page de politique de remboursement. Pas un pave de texte — juste un lien cliquable sous les badges. Le fait que ce lien existe rassure, meme si la plupart des gens ne cliquent pas dessus.

Ces trois elements combines reduisent l'hesitation au moment critique. Ne les neglige pas.

---

[SECTION 5 — Tester le parcours complet]

Ton checkout est configure, brande, et les signaux de confiance sont en place. Avant de publier, tu dois tester le parcours de bout en bout. Pas "regarder si ca a l'air bien" — vraiment passer une commande test.

Premiere etape : active le mode test. Si tu utilises Stripe, va dans WooCommerce > Reglages > Paiements > Stripe, et coche "Enable Test Mode". Stripe fournit des numeros de carte de test — le plus courant, c'est 4242 4242 4242 4242, date d'expiration dans le futur, et n'importe quel CVC. Si tu utilises PayPal Sandbox ou un autre gateway, active son mode test equivalant.

Deuxieme etape : ouvre ton funnel en navigation privee. C'est important — la navigation privee simule un visiteur qui n'est pas connecte a ton WordPress. Parcours la landing page, clique sur le bouton d'achat, remplis le formulaire checkout avec les infos de test, et finalise la commande.

Troisieme etape : verifie l'email de confirmation. Regarde dans la boite mail associee a ta commande test. Tu dois recevoir l'email WooCommerce de confirmation avec le recapitulatif de commande. Si l'email n'arrive pas, verifie tes reglages SMTP — c'est un probleme frequent sur les hebergements mutualisables.

Quatrieme etape : verifie la commande dans WooCommerce. Va dans WooCommerce > Commandes. Ta commande test doit apparaitre avec le statut "Processing" ou "Completed" selon ta configuration. Verifie que le bon produit est associe, que le montant est correct, et que le client est bien enregistre.

Si tout fonctionne, desactive le mode test avant de publier pour de vrai. C'est une erreur classique : oublier de repasser en mode live. Mets-toi un rappel.

---

[OUTRO]

Tu as maintenant un checkout optimise : formulaire simplifie, branding coherent, elements de confiance en place, et un parcours teste de A a Z.

Dans la prochaine et derniere lecon, on publie le funnel, on verifie le rendu sur mobile, et on regarde les premieres stats dans CartFlows. On se retrouve tout de suite.

---

## Notes de production

### Captures d'ecran suggerees
1. Dashboard CartFlows > Flow > Step Checkout > bouton Edit (mise en evidence)
2. Onglet "Checkout Layout" avec les options one-column / two-column
3. Section "Checkout Fields" — avant (tous les champs) / apres (champs simplifies)
4. Editeur Gutenberg avec le logo place en haut du checkout (bloc Image Kadence)
5. Bouton d'achat avec couleur personnalisee + badges paiement en dessous
6. Badges de paiement securise (Visa, MC, cadenas SSL)
7. Texte garantie satisfaction avec icone
8. WooCommerce > Reglages > Stripe > Test Mode active
9. Formulaire rempli avec carte test 4242
10. Email de confirmation WooCommerce recu
11. WooCommerce > Commandes > commande test visible

### Transitions
- Intro → Section 1 : cut direct
- Section 1 → Section 2 : transition sur la capture du panneau Checkout Fields
- Section 2 → Section 3 : "Maintenant que le formulaire est propre, occupons-nous du visuel"
- Section 3 → Section 4 : fondu enchaine vers le bas de la page checkout
- Section 4 → Section 5 : "Tout est en place. On teste."
- Section 5 → Outro : cut apres la verification WooCommerce

### Notes HeyGen / ElevenLabs
- Rythme : modere, pauses de 1s entre les sections
- Insister vocalement sur "Moins de champs = plus de conversions"
- Ton direct et pedagogique — pas de survente
- Le passage sur la carte test 4242 doit etre articule lentement (chiffres)

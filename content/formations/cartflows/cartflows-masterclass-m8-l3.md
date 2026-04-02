# Lecon 8.3 — CartFlows + TutorLMS : vendre des formations via funnel

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 8 — Ecosysteme et automatisation
- **Duree cible** : 12 min (~1500 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Creer un funnel CartFlows dedie a la vente de formations TutorLMS. Structurer le parcours landing → checkout → thank you avec redirection vers le cours. Ajouter bump et upsell adaptes aux formations.

---

## Script narration

**[INTRO — face camera]**

Tu as cree une formation sur TutorLMS. Le contenu est pret, les lecons sont en place, les quiz fonctionnent. Maintenant, il faut la vendre. Et si tu utilises la page de cours TutorLMS par defaut pour ca, tu passes a cote de 30 a 50% de revenus supplementaires.

Pourquoi ? Parce que la page de cours TutorLMS est faite pour decrire un cours. Pas pour vendre. Il n'y a pas de preuve sociale mise en avant, pas de garantie, pas de compte a rebours, pas de bump, pas de upsell. C'est une fiche produit, pas une page de vente.

La solution : placer un funnel CartFlows devant chaque formation premium.

---

**[SECTION 1 — Le probleme de la page de cours par defaut]**

**[ECRAN — page de cours TutorLMS standard]**

Regarde une page de cours TutorLMS classique. Tu as le titre, la description, le curriculum avec les lecons, les prerequis, le prix, et un bouton "S'inscrire". C'est fonctionnel, mais c'est plat.

Il manque tout ce qui fait une page de vente performante : une promesse claire au-dessus de la ligne de flottaison, des temoignages clients, une section FAQ, un recapitulatif de la valeur, une garantie visible, et surtout un parcours post-achat qui maximise la valeur.

La page de cours TutorLMS est parfaite pour les formations gratuites ou les cours internes. Pour une formation payante que tu veux promouvoir activement, tu as besoin d'un vrai funnel.

---

**[SECTION 2 — La structure du funnel formation]**

**[ECRAN — schema du funnel en 3 etapes]**

Voici la structure que je recommande pour vendre une formation TutorLMS via CartFlows :

Etape 1 — Landing page de vente. C'est ta page de persuasion. Tu la construis avec Gutenberg + Kadence Blocks. Titre accrocheur, benefices, preuves sociales, curriculum resume, garantie, et un gros bouton CTA qui envoie vers le checkout. Cette page n'a rien a voir avec TutorLMS — c'est une page CartFlows pure.

Etape 2 — Checkout. Le formulaire de paiement CartFlows. Le client saisit ses informations, paie, et peut ajouter un order bump. Le produit WooCommerce est celui qui est lie a ta formation TutorLMS.

Etape 3 — Thank You. La page de confirmation. Et ici, c'est la que tu rediriges vers TutorLMS — soit vers le dashboard etudiant, soit directement vers la premiere lecon.

---

**[SECTION 3 — Connecter le produit WooCommerce au cours TutorLMS]**

**[ECRAN — WooCommerce > Produit > onglet TutorLMS]**

Pour que l'achat via CartFlows donne automatiquement acces au cours, il faut que le produit WooCommerce soit lie au cours TutorLMS. C'est une configuration qui se fait dans WooCommerce, pas dans CartFlows.

Va dans WooCommerce, Produits, et ouvre le produit lie a ta formation. Dans les options du produit, tu trouves un onglet ou un champ "TutorLMS Course" (selon la version). Tu selectionnes le cours concerne. Enregistre.

A partir de ce moment, chaque achat de ce produit WooCommerce — que ce soit via le checkout standard ou via CartFlows — inscrit automatiquement l'acheteur au cours. CartFlows n'a pas besoin de savoir que c'est un cours. Il traite le produit WooCommerce normalement. C'est WooCommerce + TutorLMS qui gerent l'inscription.

---

**[SECTION 4 — La redirection post-achat vers TutorLMS]**

**[ECRAN — CartFlows > Thank You step > Custom Redirect]**

Par defaut, apres l'achat, le client atterrit sur la Thank You page CartFlows. C'est bien pour afficher un message de confirmation et proposer un upsell. Mais une fois que le client a fini le parcours de vente, tu veux l'envoyer vers son cours.

Deux options :

Option 1 — Bouton sur la Thank You page. Tu gardes la Thank You CartFlows et tu ajoutes un gros bouton "Acceder a ta formation maintenant" qui pointe vers le dashboard TutorLMS ou directement vers la premiere lecon. L'URL ressemble a : tonsite.com/courses/nom-du-cours/lesson/lecon-1/

Option 2 — Redirection automatique. Dans les parametres du step Thank You, tu configures un delai (par exemple 5 secondes) puis une redirection automatique vers le cours. Le client voit "Merci pour ton achat ! Tu vas etre redirige vers ta formation..." et hop, il arrive sur TutorLMS.

Je recommande l'option 1 si tu as un upsell apres le checkout. Le client doit pouvoir voir la page upsell puis la Thank You avant d'etre redirige. L'option 2 fonctionne mieux si tu n'as pas de upsell et que tu veux un parcours ultra-direct.

---

**[SECTION 5 — Order bump adapte aux formations]**

**[ECRAN — checkout CartFlows avec order bump formation]**

L'order bump sur un checkout de formation, c'est une mine d'or si tu choisis le bon complement. Voici les bumps qui fonctionnent le mieux pour les formations en ligne :

- Pack de ressources telechargeable : templates, checklists, fiches recapitulatives en PDF. Prix recommande : 7 a 17 euros. Taux d'acceptation typique : 25-40%.
- Acces a une communaute privee : groupe Slack, Discord ou forum WordPress. Prix : 9 a 19 euros/mois. Moins courant en bump, mais ca marche si ta communaute a de la valeur percue.
- Module bonus exclusif : une lecon supplementaire qui n'est pas dans le cours standard. Prix : 12 a 27 euros. Fonctionne tres bien si le sujet est concret ("Template de page de vente inclus").

Le bump ideal pour une formation a 47 euros : un pack de ressources a 12 euros. Ca represente environ 25% du prix principal — le ratio ideal pour un bump.

---

**[SECTION 6 — Upsell apres une formation : coaching ou all-access]**

**[ECRAN — page upsell coaching individuel]**

Le upsell apres l'achat d'une formation, c'est le moment de proposer l'accompagnement personnalise. Le client vient d'acheter le contenu — maintenant tu lui proposes l'aide pour l'appliquer.

Deux upsells qui fonctionnent pour les formateurs :

Upsell 1 — Coaching individuel. "Tu viens d'acheter la formation. Veux-tu que je t'accompagne pendant 4 semaines pour mettre en place ce que tu apprends ?" Prix : 197 a 497 euros selon ta niche. Taux d'acceptation : 5 a 12%.

Upsell 2 — Acces a toutes les formations. "Tu viens d'acheter la formation CartFlows. Accede a l'integralite du catalogue schoolsWP pour 297 euros au lieu de 497." C'est un all-access pass. Taux d'acceptation : 8 a 15%.

Si le client refuse le upsell, tu peux proposer un downsell : un module supplementaire a 47 euros, ou un mois d'essai de la communaute a 1 euro.

---

**[OUTRO — face camera]**

La combinaison CartFlows + TutorLMS, c'est ce qu'on utilise sur schoolsWP pour toutes les formations payantes. La page de cours TutorLMS reste accessible pour les inscrits — mais c'est le funnel CartFlows qui fait le travail de vente.

Dans la prochaine lecon, on ajoute les abonnements WooCommerce Subscriptions a tes funnels.

---

## Notes de production

- **Visuels** : schema funnel 3 etapes, page de cours TutorLMS vs landing CartFlows, checkout avec bump formation
- **Captures d'ecran** : produit WooCommerce lie a TutorLMS, Thank You avec bouton acces cours, page upsell coaching
- **Ton** : strategique et pratique, comparaison page cours vs funnel
- **Duree estimee** : ~12 min a debit normal
- **Transition** : enchaine sur L8.4 (CartFlows + WooCommerce Subscriptions)

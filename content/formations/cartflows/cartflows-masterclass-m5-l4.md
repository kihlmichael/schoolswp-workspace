# Lecon 5.4 — Chainer upsell, downsell et thank you

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 5 — One-Click Upsells et Downsells
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Construire la sequence complete dans le Canvas Mode de CartFlows. Visualiser les 4 chemins possibles. Assembler un funnel complet Landing → Checkout + Bump → Upsell → Downsell → Thank You.

---

## Script narration

**[INTRO — face camera]**

Tu as ton upsell. Tu as ton downsell. Maintenant on assemble tout dans un parcours coherent. Dans cette lecon, tu vas construire la sequence complete et comprendre chaque chemin que ton client peut emprunter.

---

**[SECTION 1 — Le Canvas Mode pour visualiser le flow]**

**[ECRAN — CartFlows → Flow → Canvas Mode]**

Ouvre ton funnel et passe en Canvas Mode. C'est la vue visuelle de CartFlows qui te montre l'enchainement de tes steps sous forme de diagramme.

Tu dois voir tes steps alignes : Landing Page → Checkout → Upsell → Downsell → Thank You. Les fleches entre chaque step montrent le flux. C'est ici que tu verifies que tout est dans le bon ordre et que les connexions sont correctes.

**[ECRAN — canvas avec tous les steps visibles et connectes]**

Si un step est mal positionne, glisse-le a la bonne place. Le Canvas Mode est du drag-and-drop — c'est visuel et intuitif.

---

**[SECTION 2 — Les 4 chemins possibles]**

**[ECRAN — schema des 4 chemins avec montants]**

Ton client a 4 parcours possibles a travers ce funnel. Detaillons-les :

**Chemin 1 — Le client accepte tout.**
Landing → Checkout (produit 97 euros + bump 27 euros) → Upsell OUI (147 euros) → Thank You.
Total : 271 euros. C'est ton scenario ideal.

**Chemin 2 — Upsell accepte, pas de bump.**
Landing → Checkout (97 euros) → Upsell OUI (147 euros) → Thank You.
Total : 244 euros.

**Chemin 3 — Upsell refuse, downsell accepte.**
Landing → Checkout (97 euros + bump 27 euros) → Upsell NON → Downsell OUI (47 euros) → Thank You.
Total : 171 euros. Le downsell a recupere de la valeur.

**Chemin 4 — Tout refuse sauf le produit principal.**
Landing → Checkout (97 euros) → Upsell NON → Downsell NON → Thank You.
Total : 97 euros. Le minimum.

**[ECRAN — tableau recapitulatif des 4 chemins avec montants]**

Regarde la difference entre le chemin 4 et le chemin 1 : 97 euros contre 271 euros. Presque 3 fois plus, pour le meme client, le meme cout d'acquisition, le meme trafic.

---

**[SECTION 3 — Configurer les redirections dans CartFlows]**

**[ECRAN — parametres du step Upsell → onglet Design]**

CartFlows gere les redirections automatiquement en fonction de l'ordre des steps dans le flow. Mais verifions que tout est bien configure.

Dans les parametres de ton step Upsell, verifie le comportement des boutons :
- Bouton "Oui" (accepte) : redirige vers le step suivant. Si le step suivant est le Downsell, CartFlows le saute (puisque l'upsell a ete accepte) et va directement a la Thank You.
- Bouton "Non" (refuse) : redirige vers le step suivant, qui est le Downsell.

**[ECRAN — parametres du step Downsell]**

Pour le Downsell, meme logique :
- Bouton "Oui" : redirige vers la Thank You Page.
- Bouton "Non" : redirige vers la Thank You Page.

Dans les deux cas apres le downsell, le client arrive a la Thank You. C'est la fin du funnel.

---

**[SECTION 4 — Thank You Page : une ou plusieurs ?]**

**[ECRAN — options de la Thank You Page]**

Tu as deux approches pour la Thank You Page.

**Approche simple : une seule Thank You Page pour tout le monde.** Le contenu est generique : "Merci pour ta commande, voici tes acces." C'est plus simple a maintenir et ca fonctionne bien dans la majorite des cas.

**Approche avancee : des Thank You Pages differentes selon le chemin.** Le client qui a accepte l'upsell coaching voit une page avec les instructions de prise de rendez-vous. Le client qui n'a pris que le produit de base voit une page classique. CartFlows Pro permet cette personnalisation via des flows conditionnels, mais c'est rarement necessaire pour demarrer.

Mon conseil : commence avec une seule Thank You Page. Optimise quand tu auras du volume et des donnees.

---

**[SECTION 5 — Cas pratique : assembler le funnel complet]**

**[ECRAN — creation d'un flow de zero]**

Construisons le funnel complet ensemble, etape par etape :

1. **CartFlows → Flows → Add New.** Nomme-le "Funnel Formation WordPress".
2. **Add Step → Landing.** Template ou page vierge. C'est ta page de vente.
3. **Add Step → Checkout.** Configure le produit principal (Formation WordPress a 97 euros). Active l'order bump (Checklist PDF a 27 euros) — on a vu ca dans le module precedent.
4. **Add Step → Upsell.** Connecte le produit "Coaching Premium 1h" a 147 euros. Design la page avec titre + benefices + boutons.
5. **Add Step → Downsell.** Connecte le produit "Mini-Coaching 30min" a 47 euros. Design la page de repli.
6. **Add Step → Thank You.** Page de confirmation avec recap de commande.

**[ECRAN — flow complet dans le Canvas Mode]**

Voila. Cinq steps, un parcours fluide, quatre chemins possibles. Ton funnel est pret.

---

**[OUTRO — face camera]**

Tu as maintenant un funnel complet avec toutes les couches de monetisation : produit principal, order bump, upsell et downsell. C'est la structure qui maximise la valeur de chaque visiteur qui entre dans ton entonnoir.

Dans la prochaine lecon, on passe a un niveau superieur : les Dynamic Offers. Tu vas apprendre a adapter l'upsell en fonction de ce que le client a achete.

---

## Notes de production

- **Visuels** : Canvas Mode CartFlows, schema des 4 chemins avec montants, tableau recapitulatif, creation de flow pas-a-pas
- **Captures d'ecran** : canvas drag-and-drop, parametres redirections, Thank You Page
- **Ton** : structurant, vue d'ensemble
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine sur L5.5 (Dynamic Offers)

# Lecon 5.7 — Upsell avec PayPal

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 5 — One-Click Upsells et Downsells
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre les limitations de PayPal pour les upsells one-click, connaitre les solutions CartFlows, et savoir comment adapter son funnel selon la methode de paiement du client.

---

## Script narration

**[INTRO — face camera]**

Tout ce qu'on a construit jusqu'ici fonctionne parfaitement avec Stripe. Un clic, le debit passe, le produit est ajoute. Mais que se passe-t-il quand ton client paie avec PayPal ? C'est une question importante, parce que PayPal represente encore une part significative des paiements en ligne. Et la reponse n'est pas aussi simple qu'avec Stripe.

---

**[SECTION 1 — Le probleme technique de PayPal]**

**[ECRAN — schema comparatif : flux Stripe vs flux PayPal]**

Avec Stripe, quand le client paie au checkout, ses informations de carte sont tokenisees et stockees de maniere securisee. CartFlows peut reutiliser ce token pour debiter un montant supplementaire au moment de l'upsell. C'est instantane et transparent.

Avec PayPal, ca ne fonctionne pas de la meme maniere. PayPal ne supporte pas nativement les "Reference Transactions" — c'est-a-dire la possibilite de faire un deuxieme paiement automatique sans revalidation du client sur PayPal.

Concretement : quand le client paie avec PayPal au checkout, CartFlows ne peut pas debiter un montant supplementaire en un clic au moment de l'upsell. PayPal exige que le client soit redirige vers PayPal pour valider chaque transaction separement.

Ca casse l'experience one-click. Et ca casse les taux de conversion.

---

**[SECTION 2 — Les Reference Transactions PayPal]**

**[ECRAN — page PayPal Reference Transactions]**

Il existe une solution PayPal qui s'appelle "Reference Transactions". Ce feature permet exactement ce dont CartFlows a besoin : debiter un client qui a deja autorise un paiement precedent.

Le probleme : les Reference Transactions ne sont pas disponibles par defaut sur un compte PayPal Business. Tu dois en faire la demande a PayPal, et PayPal ne l'accorde pas a tout le monde. C'est reserve aux comptes avec un volume de transactions significatif et un historique propre.

Si tu es dans cette situation (gros volume PayPal, historique solide), contacte le support PayPal Business et demande l'activation des Reference Transactions. Si c'est accorde, CartFlows pourra gerer les upsells one-click via PayPal exactement comme avec Stripe.

Mais pour la majorite des utilisateurs, cette option n'est pas disponible. Voyons les alternatives.

---

**[SECTION 3 — Solution CartFlows : adapter le flow selon la methode de paiement]**

**[ECRAN — CartFlows → Settings → Upsell → PayPal]**

CartFlows propose des options pour gerer les paiements PayPal dans les upsells :

**Option 1 : Rediriger vers un checkout classique.**
Quand CartFlows detecte que le client a paye avec PayPal, au lieu d'afficher le bouton one-click, il affiche un bouton qui redirige vers une page de paiement PayPal standard. Le client doit se reconnecter a PayPal et valider le paiement manuellement.

C'est fonctionnel, mais le taux de conversion chute fortement. Chaque etape supplementaire est une sortie potentielle.

**Option 2 : Proposer un formulaire Stripe sur la page upsell.**
Au lieu de reutiliser PayPal, tu proposes au client de payer l'upsell par carte via Stripe. La page upsell affiche un mini-formulaire de carte. Ce n'est plus du one-click, mais c'est plus fluide qu'une redirection PayPal complete.

**[ECRAN — page upsell avec formulaire de paiement alternatif]**

**Option 3 : Sauter l'upsell pour les clients PayPal.**
Si tes upsells sont essentiels a ta marge et que l'experience degradee PayPal nuit a ta marque, tu peux configurer CartFlows pour ne pas afficher l'upsell aux clients qui ont paye en PayPal. Ils passent directement du Checkout a la Thank You Page.

C'est radical, mais ca evite de casser l'experience.

---

**[SECTION 4 — Comment detecter la methode de paiement]**

**[ECRAN — CartFlows Pro → Conditional Rules → Payment Method]**

Dans CartFlows Pro, tu peux creer des regles conditionnelles basees sur la methode de paiement utilisee au checkout.

Configure une regle sur ton step Upsell :
- SI methode de paiement = Stripe → affiche l'upsell one-click (comportement standard)
- SI methode de paiement = PayPal → applique le comportement que tu as choisi (redirect, formulaire alternatif, ou skip)

**[ECRAN — configuration de la regle conditionnelle]**

Cette detection est automatique. CartFlows sait quel moyen de paiement le client a utilise et applique la regle correspondante.

---

**[SECTION 5 — Conseil strategique : privilegier Stripe]**

**[ECRAN — comparaison Stripe vs PayPal pour les funnels]**

Si les upsells sont un pilier de ta strategie de monetisation — et apres ce module, ils devraient l'etre — alors Stripe doit etre ta passerelle de paiement principale.

Ca ne veut pas dire supprimer PayPal. Certains clients preferent PayPal et ne commander pas sans. Mais tu peux influencer le choix :

- **Affiche Stripe en premier** dans l'ordre des methodes de paiement sur ton checkout
- **Mets en avant la carte bancaire** avec un design plus visible que PayPal
- **Precise "Paiement securise par carte"** a cote du champ — ca rassure

L'objectif n'est pas de forcer, mais de guider. Plus de clients sur Stripe = plus de clients eligibles au one-click upsell = plus de revenus additionnels.

**[ECRAN — checkout avec Stripe en premier et PayPal en second]**

Et pour les clients qui choisissent quand meme PayPal, le comportement de repli que tu as configure prend le relais. Tout le monde est servi.

---

**[OUTRO — face camera]**

PayPal reste un moyen de paiement incontournable, mais il n'est pas ideal pour les upsells one-click. Maintenant tu connais les limites et les solutions. Mets Stripe en avant, configure un comportement de repli pour PayPal, et tu couvres 100% de tes clients.

Dans la prochaine lecon, on met tout en pratique avec un cas concret : un funnel complet pour un produit physique avec upsell digital.

---

## Notes de production

- **Visuels** : schema flux Stripe vs PayPal, captures CartFlows (PayPal settings, conditional rules), comparaison methodes de paiement
- **Captures d'ecran** : page Reference Transactions PayPal, CartFlows conditional rules, checkout avec ordre des methodes
- **Ton** : technique et pragmatique, pas alarmiste
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine sur L5.8 (cas pratique funnel complet)

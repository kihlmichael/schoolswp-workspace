# Funnel de vente FluentCart — LAUNCH (blueprint)

Spec du tunnel de vente propulsé par FluentCart pour la formation LAUNCH, avec order bump et upsell bundle.
Statut : NON CONSTRUIT. À monter quand LAUNCH est vendable (gate G3 du blueprint lead magnet).
Principe : la capture gratuite reste sur Fluent Forms ; FluentCart pilote uniquement le payant.

---

## Place dans l'architecture globale

```
Capture gratuite     Fluent Forms (landing + merci)        [LIVE]
Nurture              FluentCRM E1 a E7                      [E1-E2 live, E3-E7 stages]
Vente LAUNCH+bundle  FluentCart (ce funnel)                [a construire]
Livraison cours      TutorLMS (acces a l'achat)            [coquille a finaliser]
```

L'email E5 (J10) et E7 (J14) de la séquence pointent vers la page de vente LAUNCH, qui ouvre ce funnel.

---

## Le tunnel, étape par étape

### 1. Page de vente LAUNCH
Construite avec le skill mini-offre-page-de-vente (roadmap J+40). Bouton d'achat = ajout du produit LAUNCH au checkout FluentCart.

### 2. Checkout FluentCart + order bump
- Produit principal : LAUNCH.
- Instant checkout activé (le moins de friction possible, achat en une étape).
- Order bump (une case à cocher sous le récap) : ajouter SHIP à tarif réduit. Message type : "Ajoute SHIP maintenant : +47 EUR au lieu de 67 EUR. Produis et livre comme un pro." Un seul bump, pas trois.

### 3. Upsell post-achat (one-click)
Juste après le paiement, avant la page de remerciement, une offre en un clic (sans re-saisir la carte).
- Si l'acheteur a pris LAUNCH seul : "Complète en bundle. Ajoute SHIP + CART pour +80 EUR (au lieu de 134 EUR). Tu obtiens la méthode complète."
- S'il a déjà coché le bump SHIP : l'upsell propose CART seul pour +33 EUR.
- À confirmer selon la version de FluentCart : si l'upsell post-achat one-click n'est pas natif, fallback = page d'upsell dédiée juste après le merci, ou email d'upsell immédiat (J0+1h).

### 4. Downsell (optionnel, v2)
Si l'upsell bundle est refusé : proposer un seul module de plus à prix doux. À ne pas faire en v1, ça complexifie.

### 5. Page de remerciement + livraison
- Confirmation + reçu PDF (natif FluentCart).
- Accès au cours : inscription TutorLMS déclenchée par l'achat (intégration FluentCart vers TutorLMS, ou licence FluentCart qui débloque l'accès).
- Invitation Discord schoolsWP.
- Prochaine étape claire : "Commence par la leçon 01.01".

---

## Logique de prix (ancrage propre)

Prix solo : LAUNCH 47, SHIP 67, CART 67. Somme réelle = 181 EUR. Bundle = 127 EUR.

Règle d'or : **quel que soit le chemin, l'acheteur de la pile complète atterrit à 127 EUR.**
- LAUNCH 47 + upsell (SHIP+CART) 80 = 127.
- LAUNCH 47 + bump SHIP 47 = 94, puis upsell CART 33 = 127.

Ça préserve l'intégrité du prix bundle : personne ne paie plus cher en passant par le funnel que via la page bundle directe.

Ancrage du bundle (décidé 2026-05-29) : barrer **181 EUR** (somme réelle des 3 modules : 47+67+67), pas 297. Le bundle s'affiche "181 EUR barré, 127 EUR, économie 54 EUR". L'ancrage est honnête (181 - 127 = 54) et l'économie est vraie. On n'utilise pas le 297 comme valeur gonflée.

Promo lancement (décidé 2026-05-29, pas d'empilement) : LAUNCH -50 % pendant 72h = 23,50 EUR. Ne PAS empiler la promo -50 % LAUNCH ET les remises bump/upsell en même temps : une seule mécanique de promo par phase, sinon le prix devient illisible et la marge part. Pendant la fenêtre 72h, l'offre phare = LAUNCH à 23,50 ; le bump/upsell reste à ses conditions normales.

---

## Mécaniques FluentCart à activer

| Mécanique | Usage dans le funnel | Dispo FluentCart |
|---|---|---|
| Produits digitaux | LAUNCH, SHIP, CART | natif |
| Bundle | produit bundle 127 (page directe) | natif |
| Order bump | SHIP au checkout LAUNCH | natif (changelog 1.3.8) |
| Instant checkout | achat une étape | natif |
| Upsell one-click post-achat | SHIP+CART après LAUNCH | à confirmer selon version, sinon fallback |
| Coupons / promo programmée | -50 % LAUNCH 72h | natif |
| Licence / accès | débloque le cours TutorLMS | natif (License Management) |
| Reporting | suivi LTV, conversion bump/upsell | natif |

---

## Intégrations

- **FluentCRM** : à l'achat de LAUNCH, poser le tag client_launch_formation. Ce tag doit SORTIR le contact des emails E5-E7 du lead magnet (goal d'achat sur le funnel 45, pas une action linéaire). Ajouter le contact à la liste CLIENTS schoolsWP (24). Déclencher une séquence d'onboarding cours (séparée du nurture lead magnet).
- **TutorLMS** : l'achat FluentCart inscrit l'acheteur au cours LAUNCH (coquille TutorLMS à finaliser). Voir project_formation_delivery_stack.
- **Affiliation** : aucune (produit propre), donc pas de ref by=40 ici.

---

## Gaps connus et workarounds

- **Panier abandonné** : FluentCart n'a pas de relance native (limite identifiée dans le brief). Workaround : taguer "checkout démarré" via FluentCRM et déclencher une relance, ou accepter le gap en v1.
- **Upsell post-achat one-click** : si non natif sur la version installée, basculer sur page d'upsell post-merci ou email d'upsell immédiat.

---

## Gates avant build

1. Page de vente LAUNCH publiée (skill mini-offre).
2. Cours LAUNCH livrable (coquille TutorLMS finalisée + leçons).
3. Produits FluentCart créés (LAUNCH, SHIP, CART, bundle) avec prix.
4. Intégration FluentCart vers TutorLMS testée (un achat = un accès).
5. Tag client_launch_formation créé + goal de sortie ajouté au funnel 45.

---

## KPIs du funnel

- Taux de conversion page de vente vers achat.
- Taux de prise de l'order bump (objectif sain : 20-35 %).
- Taux de prise de l'upsell bundle.
- Panier moyen (AOV) avec vs sans bump/upsell.
- Taux d'accès effectif au cours après achat (livraison sans accroc).

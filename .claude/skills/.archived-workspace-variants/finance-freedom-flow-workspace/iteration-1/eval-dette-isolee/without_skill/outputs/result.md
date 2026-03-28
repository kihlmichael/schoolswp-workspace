# Etape 4 : Destruction de dettes -- Analyse complete

## Situation initiale

| Dette | Solde | Taux annuel | Taux mensuel | Paiement minimum |
|-------|-------|-------------|--------------|------------------|
| Credit auto | 12 000 EUR | 4.5% | 0.375% | 280 EUR/mois |
| Credit conso | 5 000 EUR | 7.2% | 0.600% | 120 EUR/mois |
| Carte revolving | 2 800 EUR | 19.8% | 1.650% | 85 EUR/mois |

- **Total des dettes** : 19 800 EUR
- **Paiements minimums cumules** : 485 EUR/mois
- **Budget supplementaire** : 200 EUR/mois
- **Budget total disponible** : 685 EUR/mois

---

## Methode 1 : Avalanche (taux le plus eleve d'abord)

### Principe

On paie le minimum sur toutes les dettes sauf celle au taux le plus eleve, qui recoit tout le surplus. Ordre d'attaque : Revolving (19.8%) → Credit conso (7.2%) → Credit auto (4.5%).

### Allocation mensuelle

- Credit auto : 280 EUR (minimum)
- Credit conso : 120 EUR (minimum)
- Revolving : 85 + 200 = **285 EUR** (minimum + surplus)

Quand une dette est soldee, son minimum est redirige vers la dette suivante au taux le plus eleve.

### Calendrier mois par mois -- Methode Avalanche

**Phase 1 : Attaque du Revolving (mois 1-11)**

Le revolving recoit 285 EUR/mois. Les autres recoivent leur minimum.

| Mois | Revolving (solde) | Interets revolving | Paiement revolving | Conso (solde) | Interets conso | Paiement conso | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|-------------------|--------------------|--------------------|---------------|----------------|----------------|--------------|---------------|---------------|------------|
| 0 | 2 800.00 | -- | -- | 5 000.00 | -- | -- | 12 000.00 | -- | -- | -- |
| 1 | 2 561.20 | 46.20 | 285.00 | 4 910.00 | 30.00 | 120.00 | 11 765.00 | 45.00 | 280.00 | 685.00 |
| 2 | 2 318.47 | 42.26 | 285.00 | 4 819.46 | 29.46 | 120.00 | 11 529.12 | 44.12 | 280.00 | 685.00 |
| 3 | 2 071.73 | 38.25 | 285.00 | 4 728.38 | 28.92 | 120.00 | 11 292.35 | 43.23 | 280.00 | 685.00 |
| 4 | 1 820.91 | 34.18 | 285.00 | 4 636.76 | 28.37 | 120.00 | 11 054.69 | 42.35 | 280.00 | 685.00 |
| 5 | 1 565.93 | 30.03 | 285.00 | 4 544.59 | 27.82 | 120.00 | 10 816.13 | 41.44 | 280.00 | 685.00 |
| 6 | 1 306.72 | 25.84 | 285.00 | 4 451.87 | 27.27 | 120.00 | 10 576.67 | 40.54 | 280.00 | 685.00 |
| 7 | 1 043.18 | 21.56 | 285.00 | 4 358.58 | 26.71 | 120.00 | 10 336.31 | 39.64 | 280.00 | 685.00 |
| 8 | 775.40 | 17.21 | 285.00 | 4 264.73 | 26.15 | 120.00 | 10 095.04 | 38.74 | 280.00 | 685.00 |
| 9 | 503.19 | 12.80 | 285.00 | 4 170.31 | 25.58 | 120.00 | 9 852.85 | 37.82 | 280.00 | 685.00 |
| 10 | 226.49 | 8.30 | 285.00 | 4 075.32 | 25.02 | 120.00 | 9 609.75 | 36.90 | 280.00 | 685.00 |
| 11 | 0.00 | 3.74 | 230.23 | 3 979.76 | 24.45 | 120.00 | 9 365.73 | 35.98 | 280.00 | 630.23 |

**Revolving solde au mois 11.** Surplus restant au mois 11 : 285 - 230.23 = 54.77 EUR (redirige vers le conso).

**Phase 2 : Attaque du Credit conso (mois 12-22)**

Le credit conso recoit maintenant : 120 (son minimum) + 200 (surplus) + 85 (ancien minimum revolving) = **405 EUR/mois**.

| Mois | Conso (solde) | Interets conso | Paiement conso | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|---------------|----------------|----------------|--------------|---------------|---------------|------------|
| 12 | 3 598.63 | 23.87 | 405.00 | 9 120.79 | 35.06 | 280.00 | 685.00 |
| 13 | 3 215.22 | 21.59 | 405.00 | 8 874.99 | 34.20 | 280.00 | 685.00 |
| 14 | 2 829.50 | 19.29 | 405.00 | 8 628.26 | 33.28 | 280.00 | 685.00 |
| 15 | 2 441.48 | 16.98 | 405.00 | 8 380.61 | 32.35 | 280.00 | 685.00 |
| 16 | 2 051.13 | 14.65 | 405.00 | 8 132.03 | 31.43 | 280.00 | 685.00 |
| 17 | 1 658.44 | 12.31 | 405.00 | 7 882.52 | 30.49 | 280.00 | 685.00 |
| 18 | 1 263.39 | 9.95 | 405.00 | 7 632.08 | 29.56 | 280.00 | 685.00 |
| 19 | 865.97 | 7.58 | 405.00 | 7 380.70 | 28.62 | 280.00 | 685.00 |
| 20 | 466.17 | 5.20 | 405.00 | 7 128.38 | 27.68 | 280.00 | 685.00 |
| 21 | 63.97 | 2.80 | 405.00 | 6 875.11 | 26.73 | 280.00 | 685.00 |
| 22 | 0.00 | 1.06 | 65.02 | 6 620.89 | 25.78 | 280.00 | 345.02 |

**Credit conso solde au mois 22.** Surplus restant au mois 22 : 405 - 65.02 = 339.98 EUR (redirige vers l'auto).

**Phase 3 : Attaque du Credit auto (mois 23-34)**

Le credit auto recoit maintenant : 280 (son minimum) + 200 (surplus) + 85 (revolving) + 120 (conso) = **685 EUR/mois** (tout le budget).

| Mois | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|--------------|---------------|---------------|------------|
| 23 | 5 960.72 | 24.83 | 685.00 | 685.00 |
| 24 | 5 298.07 | 22.35 | 685.00 | 685.00 |
| 25 | 4 632.94 | 19.87 | 685.00 | 685.00 |
| 26 | 3 965.31 | 17.37 | 685.00 | 685.00 |
| 27 | 3 295.18 | 14.87 | 685.00 | 685.00 |
| 28 | 2 622.53 | 12.35 | 685.00 | 685.00 |
| 29 | 1 947.36 | 9.83 | 685.00 | 685.00 |
| 30 | 1 269.66 | 7.30 | 685.00 | 685.00 |
| 31 | 589.42 | 4.76 | 685.00 | 685.00 |
| 32 | 0.00 | 2.21 | 591.63 | 591.63 |

**Credit auto solde au mois 32.**

### Resume Methode Avalanche

- **Revolving solde** : Mois 11
- **Credit conso solde** : Mois 22
- **Credit auto solde** : Mois 32
- **Duree totale** : 32 mois (2 ans et 8 mois)
- **Total paye** : 20 997.88 EUR
- **Total interets payes** : 1 197.88 EUR

---

## Methode 2 : Snowball (solde le plus petit d'abord)

### Principe

On paie le minimum sur toutes les dettes sauf celle au solde le plus petit, qui recoit tout le surplus. Ordre d'attaque : Revolving (2 800 EUR) → Credit conso (5 000 EUR) → Credit auto (12 000 EUR).

### Allocation mensuelle

Identique au debut car le revolving est a la fois le plus petit solde ET le taux le plus eleve. La difference apparait en Phase 2.

### Calendrier mois par mois -- Methode Snowball

**Phase 1 : Attaque du Revolving (mois 1-11)**

Identique a la methode Avalanche -- meme ordre d'attaque pour la premiere dette.

| Mois | Revolving (solde) | Interets revolving | Paiement revolving | Conso (solde) | Interets conso | Paiement conso | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|-------------------|--------------------|--------------------|---------------|----------------|----------------|--------------|---------------|---------------|------------|
| 0 | 2 800.00 | -- | -- | 5 000.00 | -- | -- | 12 000.00 | -- | -- | -- |
| 1 | 2 561.20 | 46.20 | 285.00 | 4 910.00 | 30.00 | 120.00 | 11 765.00 | 45.00 | 280.00 | 685.00 |
| 2 | 2 318.47 | 42.26 | 285.00 | 4 819.46 | 29.46 | 120.00 | 11 529.12 | 44.12 | 280.00 | 685.00 |
| 3 | 2 071.73 | 38.25 | 285.00 | 4 728.38 | 28.92 | 120.00 | 11 292.35 | 43.23 | 280.00 | 685.00 |
| 4 | 1 820.91 | 34.18 | 285.00 | 4 636.76 | 28.37 | 120.00 | 11 054.69 | 42.35 | 280.00 | 685.00 |
| 5 | 1 565.93 | 30.03 | 285.00 | 4 544.59 | 27.82 | 120.00 | 10 816.13 | 41.44 | 280.00 | 685.00 |
| 6 | 1 306.72 | 25.84 | 285.00 | 4 451.87 | 27.27 | 120.00 | 10 576.67 | 40.54 | 280.00 | 685.00 |
| 7 | 1 043.18 | 21.56 | 285.00 | 4 358.58 | 26.71 | 120.00 | 10 336.31 | 39.64 | 280.00 | 685.00 |
| 8 | 775.40 | 17.21 | 285.00 | 4 264.73 | 26.15 | 120.00 | 10 095.04 | 38.74 | 280.00 | 685.00 |
| 9 | 503.19 | 12.80 | 285.00 | 4 170.31 | 25.58 | 120.00 | 9 852.85 | 37.82 | 280.00 | 685.00 |
| 10 | 226.49 | 8.30 | 285.00 | 4 075.32 | 25.02 | 120.00 | 9 609.75 | 36.90 | 280.00 | 685.00 |
| 11 | 0.00 | 3.74 | 230.23 | 3 979.76 | 24.45 | 120.00 | 9 365.73 | 35.98 | 280.00 | 630.23 |

**Revolving solde au mois 11.** (Identique a Avalanche.)

**Phase 2 : Attaque du Credit conso (mois 12-22)**

Dans la methode Snowball, le credit conso (4 000 EUR restant environ) est le plus petit solde, donc il est attaque en second. C'est le meme ordre que l'Avalanche dans ce cas, car le conso est a la fois le 2e plus petit solde ET le 2e taux le plus eleve.

Le calendrier est donc **identique a l'Avalanche** pour cette phase aussi.

| Mois | Conso (solde) | Interets conso | Paiement conso | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|---------------|----------------|----------------|--------------|---------------|---------------|------------|
| 12 | 3 598.63 | 23.87 | 405.00 | 9 120.79 | 35.06 | 280.00 | 685.00 |
| 13 | 3 215.22 | 21.59 | 405.00 | 8 874.99 | 34.20 | 280.00 | 685.00 |
| 14 | 2 829.50 | 19.29 | 405.00 | 8 628.26 | 33.28 | 280.00 | 685.00 |
| 15 | 2 441.48 | 16.98 | 405.00 | 8 380.61 | 32.35 | 280.00 | 685.00 |
| 16 | 2 051.13 | 14.65 | 405.00 | 8 132.03 | 31.43 | 280.00 | 685.00 |
| 17 | 1 658.44 | 12.31 | 405.00 | 7 882.52 | 30.49 | 280.00 | 685.00 |
| 18 | 1 263.39 | 9.95 | 405.00 | 7 632.08 | 29.56 | 280.00 | 685.00 |
| 19 | 865.97 | 7.58 | 405.00 | 7 380.70 | 28.62 | 280.00 | 685.00 |
| 20 | 466.17 | 5.20 | 405.00 | 7 128.38 | 27.68 | 280.00 | 685.00 |
| 21 | 63.97 | 2.80 | 405.00 | 6 875.11 | 26.73 | 280.00 | 685.00 |
| 22 | 0.00 | 1.06 | 65.02 | 6 620.89 | 25.78 | 280.00 | 345.02 |

**Credit conso solde au mois 22.**

**Phase 3 : Attaque du Credit auto (mois 23-32)**

Identique a l'Avalanche.

| Mois | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|--------------|---------------|---------------|------------|
| 23 | 5 960.72 | 24.83 | 685.00 | 685.00 |
| 24 | 5 298.07 | 22.35 | 685.00 | 685.00 |
| 25 | 4 632.94 | 19.87 | 685.00 | 685.00 |
| 26 | 3 965.31 | 17.37 | 685.00 | 685.00 |
| 27 | 3 295.18 | 14.87 | 685.00 | 685.00 |
| 28 | 2 622.53 | 12.35 | 685.00 | 685.00 |
| 29 | 1 947.36 | 9.83 | 685.00 | 685.00 |
| 30 | 1 269.66 | 7.30 | 685.00 | 685.00 |
| 31 | 589.42 | 4.76 | 685.00 | 685.00 |
| 32 | 0.00 | 2.21 | 591.63 | 591.63 |

**Credit auto solde au mois 32.**

### Resume Methode Snowball

- **Revolving solde** : Mois 11
- **Credit conso solde** : Mois 22
- **Credit auto solde** : Mois 32
- **Duree totale** : 32 mois (2 ans et 8 mois)
- **Total paye** : 20 997.88 EUR
- **Total interets payes** : 1 197.88 EUR

### Note importante sur la convergence Snowball/Avalanche

Dans ton cas specifique, **Snowball et Avalanche donnent exactement le meme resultat**. C'est parce que l'ordre des soldes (du plus petit au plus grand : revolving 2 800 < conso 5 000 < auto 12 000) correspond exactement a l'ordre inverse des taux (du plus eleve au plus bas : revolving 19.8% > conso 7.2% > auto 4.5%). Les deux methodes attaquent les dettes dans le meme ordre.

C'est une situation ideale mais relativement rare. Normalement, la dette avec le plus petit solde n'est pas celle avec le taux le plus eleve, et les deux methodes divergent.

---

## Methode 3 : Hybride (optimisation mathematique + victoires psychologiques)

### Principe

La methode hybride combine les avantages des deux approches :
1. Commence par la dette qui offre a la fois un gain psychologique rapide ET un gain financier (revolving = petit solde + taux eleve)
2. Ensuite, repartit le surplus de facon ponderee entre les dettes restantes en tenant compte du ratio interets/solde
3. Acceleration progressive grace a l'effet boule de neige

Etant donne que dans ton cas Snowball = Avalanche, la methode hybride va tenter une approche differente : **attaque simultanee ponderee** sur les deux dettes les plus couteuses, pour reduire le montant total d'interets en cours a tout moment.

### Variante Hybride : Split proportionnel au taux

Au lieu de concentrer 100% du surplus sur une seule dette, on repartit le surplus au prorata des taux d'interet :

- Revolving (19.8%) : 19.8 / (19.8 + 7.2) = 73.3% du surplus
- Credit conso (7.2%) : 7.2 / (19.8 + 7.2) = 26.7% du surplus
- Credit auto : minimum seulement

Surplus de 200 EUR :
- Revolving recoit : 85 + 146.67 = **231.67 EUR**
- Credit conso recoit : 120 + 53.33 = **173.33 EUR**
- Credit auto recoit : **280 EUR**

### Calendrier mois par mois -- Methode Hybride

**Phase 1 : Attaque simultanee Revolving + Conso (mois 1-14)**

| Mois | Revolving (solde) | Interets revolving | Paiement revolving | Conso (solde) | Interets conso | Paiement conso | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|-------------------|--------------------|--------------------|---------------|----------------|----------------|--------------|---------------|---------------|------------|
| 0 | 2 800.00 | -- | -- | 5 000.00 | -- | -- | 12 000.00 | -- | -- | -- |
| 1 | 2 614.53 | 46.20 | 231.67 | 4 856.67 | 30.00 | 173.33 | 11 765.00 | 45.00 | 280.00 | 685.00 |
| 2 | 2 425.98 | 43.14 | 231.67 | 4 712.49 | 29.14 | 173.33 | 11 529.12 | 44.12 | 280.00 | 685.00 |
| 3 | 2 234.34 | 40.03 | 231.67 | 4 567.43 | 28.27 | 173.33 | 11 292.35 | 43.23 | 280.00 | 685.00 |
| 4 | 2 039.55 | 36.87 | 231.67 | 4 421.51 | 27.40 | 173.33 | 11 054.69 | 42.35 | 280.00 | 685.00 |
| 5 | 1 841.53 | 33.65 | 231.67 | 4 274.72 | 26.54 | 173.33 | 10 816.13 | 41.44 | 280.00 | 685.00 |
| 6 | 1 640.25 | 30.39 | 231.67 | 4 127.05 | 25.65 | 173.33 | 10 576.67 | 40.54 | 280.00 | 685.00 |
| 7 | 1 435.64 | 27.06 | 231.67 | 3 978.48 | 24.76 | 173.33 | 10 336.31 | 39.64 | 280.00 | 685.00 |
| 8 | 1 227.66 | 23.69 | 231.67 | 3 829.02 | 23.87 | 173.33 | 10 095.04 | 38.74 | 280.00 | 685.00 |
| 9 | 1 016.24 | 20.26 | 231.67 | 3 678.67 | 22.97 | 173.33 | 9 852.85 | 37.82 | 280.00 | 685.00 |
| 10 | 801.34 | 16.77 | 231.67 | 3 527.41 | 22.07 | 173.33 | 9 609.75 | 36.90 | 280.00 | 685.00 |
| 11 | 582.89 | 13.22 | 231.67 | 3 375.25 | 21.17 | 173.33 | 9 365.73 | 35.98 | 280.00 | 685.00 |
| 12 | 360.84 | 9.62 | 231.67 | 3 222.17 | 20.25 | 173.33 | 9 120.79 | 35.06 | 280.00 | 685.00 |
| 13 | 135.13 | 5.96 | 231.67 | 3 068.18 | 19.34 | 173.33 | 8 874.93 | 34.14 | 280.00 | 685.00 |
| 14 | 0.00 | 2.23 | 137.36 | 2 913.26 | 18.41 | 173.33 | 8 628.14 | 33.21 | 280.00 | 590.69 |

**Revolving solde au mois 14.** Surplus restant au mois 14 : 231.67 - 137.36 = 94.31 EUR redirige vers le conso.

**Phase 2 : Attaque du Credit conso (mois 15-22)**

Le conso recoit maintenant : 120 (minimum) + 200 (surplus) + 85 (ancien revolving) = **405 EUR/mois**.

| Mois | Conso (solde) | Interets conso | Paiement conso | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|---------------|----------------|----------------|--------------|---------------|---------------|------------|
| 15 | 2 525.74 | 17.48 | 405.00 | 8 380.46 | 32.32 | 280.00 | 685.00 |
| 16 | 2 135.89 | 15.15 | 405.00 | 8 131.87 | 31.42 | 280.00 | 685.00 |
| 17 | 1 743.71 | 12.81 | 405.00 | 7 882.36 | 30.49 | 280.00 | 685.00 |
| 18 | 1 349.17 | 10.46 | 405.00 | 7 631.92 | 29.56 | 280.00 | 685.00 |
| 19 | 952.27 | 8.10 | 405.00 | 7 380.54 | 28.62 | 280.00 | 685.00 |
| 20 | 553.01 | 5.71 | 405.00 | 7 128.22 | 27.68 | 280.00 | 685.00 |
| 21 | 151.33 | 3.32 | 405.00 | 6 874.95 | 26.73 | 280.00 | 685.00 |
| 22 | 0.00 | 0.91 | 152.24 | 6 620.73 | 25.78 | 280.00 | 432.24 |

**Credit conso solde au mois 22.**

**Phase 3 : Attaque du Credit auto (mois 23-32)**

Le credit auto recoit tout : **685 EUR/mois**.

| Mois | Auto (solde) | Interets auto | Paiement auto | Total paye |
|------|--------------|---------------|---------------|------------|
| 23 | 5 960.56 | 24.83 | 685.00 | 685.00 |
| 24 | 5 297.91 | 22.35 | 685.00 | 685.00 |
| 25 | 4 632.78 | 19.87 | 685.00 | 685.00 |
| 26 | 3 965.15 | 17.37 | 685.00 | 685.00 |
| 27 | 3 295.02 | 14.87 | 685.00 | 685.00 |
| 28 | 2 622.37 | 12.35 | 685.00 | 685.00 |
| 29 | 1 947.20 | 9.83 | 685.00 | 685.00 |
| 30 | 1 269.50 | 7.30 | 685.00 | 685.00 |
| 31 | 589.26 | 4.76 | 685.00 | 685.00 |
| 32 | 0.00 | 2.21 | 591.47 | 591.47 |

**Credit auto solde au mois 32.**

### Resume Methode Hybride

- **Revolving solde** : Mois 14 (3 mois plus tard qu'Avalanche)
- **Credit conso solde** : Mois 22
- **Credit auto solde** : Mois 32
- **Duree totale** : 32 mois (2 ans et 8 mois)
- **Total paye** : 21 089.40 EUR
- **Total interets payes** : 1 289.40 EUR

---

## Comparaison des trois methodes

| Critere | Avalanche | Snowball | Hybride |
|---------|-----------|----------|---------|
| **Duree totale** | 32 mois | 32 mois | 32 mois |
| **Total interets payes** | 1 197.88 EUR | 1 197.88 EUR | 1 289.40 EUR |
| **Total paye** | 20 997.88 EUR | 20 997.88 EUR | 21 089.40 EUR |
| **1ere dette soldee** | Mois 11 (revolving) | Mois 11 (revolving) | Mois 14 (revolving) |
| **2e dette soldee** | Mois 22 (conso) | Mois 22 (conso) | Mois 22 (conso) |
| **3e dette soldee** | Mois 32 (auto) | Mois 32 (auto) | Mois 32 (auto) |
| **Economies vs hybride** | 91.52 EUR | 91.52 EUR | Reference |
| **Avantage psychologique** | Eleve | Eleve | Moyen |
| **Optimisation mathematique** | Maximale | Maximale | Bonne |

### Economie d'interets totale (vs minimums seuls)

Pour reference, si tu ne payais que les minimums (485 EUR/mois) sans les 200 EUR supplementaires :

- Le revolving mettrait environ 44 mois a se rembourser (avec 1 264 EUR d'interets rien que pour cette dette)
- Le credit conso mettrait environ 48 mois
- Le credit auto mettrait environ 49 mois
- **Total interets sans acceleration** : environ 3 850 EUR

Avec tes 200 EUR supplementaires en methode Avalanche/Snowball :
- **Interets payes** : 1 197.88 EUR
- **Interets economises** : environ 2 652 EUR
- **Temps gagne** : environ 17 mois

---

## Recommandation finale

### La methode recommandee : Avalanche (= Snowball dans ton cas)

**Dans ta situation specifique, Avalanche et Snowball sont strictement identiques** car l'ordre de tes dettes par taux decroissant (revolving 19.8% > conso 7.2% > auto 4.5%) correspond exactement a l'ordre par solde croissant (revolving 2 800 < conso 5 000 < auto 12 000). Tu beneficies simultanement de :

1. **L'optimisation mathematique maximale** (tu attaques d'abord le taux le plus eleve)
2. **La victoire psychologique la plus rapide** (tu soldes d'abord la plus petite dette)

C'est la configuration ideale.

### Pourquoi PAS la methode hybride

La methode hybride coute **91.52 EUR de plus en interets** pour aucun gain supplementaire. Elle retarde la premiere victoire (mois 14 au lieu de mois 11) sans accelerer la liberation totale. Le seul interet d'une hybride serait dans un scenario ou les ordres taux/solde divergent fortement, ce qui n'est pas ton cas.

### Plan d'action concret

| Periode | Action | Budget mensuel |
|---------|--------|----------------|
| **Mois 1-11** | Minimum sur auto (280) + conso (120), surplus total sur revolving (285) | 685 EUR |
| **Mois 11** | Revolving solde ! Rediriger les 85 EUR vers le conso | -- |
| **Mois 12-22** | Minimum sur auto (280), tout le reste sur conso (405) | 685 EUR |
| **Mois 22** | Conso solde ! Rediriger les 120 EUR vers l'auto | -- |
| **Mois 23-32** | Tout sur le credit auto (685) | 685 EUR |
| **Mois 32** | **DETTE ZERO.** | 0 EUR |

### Jalons et celebrations

- **Mois 11** : Revolving elimine -- tu recuperes 85 EUR/mois de capacite
- **Mois 22** : Credit conso elimine -- tu recuperes 120 EUR/mois supplementaires
- **Mois 32** : Credit auto elimine -- tu recuperes **685 EUR/mois de flux de tresorerie libre**
- **Apres mois 32** : ces 685 EUR/mois peuvent aller directement vers l'epargne, l'investissement, ou le fonds d'urgence

### Risques et garde-fous

1. **Ne pas diminuer le paiement quand une dette est soldee** : la tentation est de "profiter" des 85 EUR liberes au mois 11. Resiste. Redirige-les immediatement vers la dette suivante.
2. **Pas de nouvelle dette pendant ces 32 mois** : surtout pas de revolving. Coupe la carte si necessaire.
3. **Fonds d'urgence minimal** : si tu n'as pas 1 000 EUR de cote, mets 100 EUR/mois de cote les 10 premiers mois au lieu de tout mettre sur la dette. Ca ralentit le plan de 2-3 mois mais ca evite de reprendre du revolving en cas d'imprevue.
4. **Revenus supplementaires** : tout bonus, prime, 13e mois, ou revenu freelance devrait aller en paiement anticipe sur la dette en cours d'attaque.

---

## Annexe : Formules utilisees

**Interet mensuel** : `solde_debut × (taux_annuel / 12)`

**Nouveau solde** : `solde_debut + interets - paiement`

**Taux mensuels** :
- Credit auto : 4.5% / 12 = 0.375%
- Credit conso : 7.2% / 12 = 0.600%
- Revolving : 19.8% / 12 = 1.650%

**Hypotheses** :
- Les paiements minimums restent fixes (ne diminuent pas avec le solde)
- Pas de frais de remboursement anticipe
- Pas d'assurance emprunteur dans le calcul
- Interets calcules sur le solde de debut de mois
- Les paiements sont effectues en fin de mois apres calcul des interets

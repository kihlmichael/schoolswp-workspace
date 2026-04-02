# Lecon 6.5 — Le tableau de bord Analytics CartFlows

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 6 — A/B Testing et Analytics
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Naviguer dans le tableau de bord Analytics de CartFlows. Lire les metriques par flow et par step. Identifier les fuites dans le funnel et exporter les donnees.

---

## Script narration

**[INTRO — face camera]**

Tu as des funnels en place. Tu fais des A/B tests. Mais comment tu vois la performance globale de tes parcours de vente ? Comment tu identifies quel step perd le plus de visiteurs ? Comment tu compares les performances d'un mois sur l'autre ?

C'est le role du tableau de bord Analytics de CartFlows. Et dans cette lecon, on va le decouvrir ensemble, ecran par ecran.

---

**[SECTION 1 — Acceder au tableau de bord]**

**[ECRAN — CartFlows > Analytics]**

Dans ton tableau de bord WordPress, va dans CartFlows puis Analytics. Tu arrives sur une vue d'ensemble qui resume la performance de tous tes flows.

La page affiche des metriques agregees : nombre total de visiteurs, nombre de conversions, revenu total, et valeur moyenne de commande. C'est ta photo globale. D'un coup d'oeil, tu sais si la tendance est a la hausse ou a la baisse.

En haut, tu as un filtre par date. Par defaut, CartFlows affiche les 30 derniers jours. Tu peux ajuster : 7 jours, 30 jours, 90 jours, ou une plage personnalisee. Utilise les 30 jours pour le suivi courant et les 90 jours pour identifier des tendances.

---

**[SECTION 2 — Metriques par flow]**

**[ECRAN — liste des flows avec metriques]**

En dessous de la vue globale, tu vois la liste de tes flows avec les metriques individuelles de chacun.

Pour chaque flow, CartFlows affiche :

Les visiteurs : combien de personnes sont entrees dans le funnel. C'est le haut de l'entonnoir.

Les conversions : combien ont finalise un achat. C'est le resultat.

Le revenu : le chiffre d'affaires genere par ce flow specifique.

L'AOV — Average Order Value : la valeur moyenne de chaque commande. C'est le revenu divise par le nombre de commandes. Si ton AOV augmente, ca signifie que tes bumps et upsells fonctionnent.

Si tu as plusieurs flows — un pour chaque produit, ou un pour chaque campagne — tu peux comparer directement lequel performe le mieux. Un flow avec moins de visiteurs mais un meilleur taux de conversion et un AOV plus eleve peut generer plus de revenu qu'un flow avec beaucoup de trafic.

---

**[SECTION 3 — Metriques par step : la vraie mine d'or]**

**[ECRAN — detail d'un flow avec metriques par step]**

Clique sur un flow. Tu accedes au detail par step — etape par etape. C'est la que tu trouves les informations les plus utiles.

CartFlows te montre le taux de passage entre chaque etape du funnel :

Landing Page : 1000 visiteurs.
Checkout : 320 visiteurs (32% de passage).
Order Bump : accepte par 85 acheteurs (taux d'acceptation du bump).
Upsell : vu par 200 acheteurs, accepte par 28 (14% d'acceptation).
Thank You : 200 acheteurs ont complete le parcours.

Ce que tu lis ici, c'est le comportement reel de tes clients a chaque etape. Tu vois ou ils avancent et ou ils decrochent.

---

**[SECTION 4 — Identifier les fuites]**

**[ECRAN — entonnoir avec fleches montrant les abandons]**

Le tableau de bord par step te revele les fuites de ton funnel. Une fuite, c'est une etape ou tu perds un pourcentage anormalement eleve de visiteurs.

Exemple : 1000 visiteurs sur ta landing page, mais seulement 120 arrivent au checkout. Ton taux de passage est de 12%. C'est faible. La landing page ne convainc pas assez de visiteurs de passer a l'achat. C'est ta priorite d'optimisation.

Autre exemple : 200 acheteurs voient l'upsell, mais seulement 6 l'acceptent. Taux d'acceptation de 3%. C'est en dessous de la moyenne. Ton offre upsell est soit trop chere, soit pas assez pertinente, soit mal presentee.

La regle : cherche le step qui a la plus grosse chute en pourcentage par rapport au step precedent. C'est ton maillon faible. C'est la que tu dois concentrer tes tests A/B en priorite.

Ne passe pas ton temps a optimiser un upsell qui a deja un bon taux d'acceptation. Concentre-toi sur le step qui saigne le plus.

---

**[SECTION 5 — Filtrer par date, par flow, par step]**

**[ECRAN — filtres du tableau de bord Analytics]**

CartFlows permet de filtrer les donnees de plusieurs manieres.

Par date : compare la performance de ce mois par rapport au mois dernier. Est-ce que tes conversions s'ameliorent ou stagnent ?

Par flow : isole un funnel specifique pour analyser ses performances independamment des autres.

Par step : plonge dans les details d'une etape specifique. Utile quand tu viens de modifier quelque chose et que tu veux voir l'impact.

Combine les filtres pour repondre a des questions precises. "Comment mon checkout a performe la semaine derniere par rapport a la semaine precedente ?" Filtre : flow X, step Checkout, 7 derniers jours vs 7 jours precedents.

---

**[SECTION 6 — Exporter les donnees]**

**[ECRAN — bouton export et fichier CSV]**

CartFlows permet d'exporter les donnees au format CSV. Tu trouveras un bouton d'export dans le tableau de bord Analytics.

Exporter les donnees est utile dans deux cas :

Premierement, pour une analyse plus poussee. Tu peux ouvrir le CSV dans Google Sheets et creer tes propres graphiques, calculer des tendances, ou comparer des periodes.

Deuxiemement, pour garder un historique. Les donnees dans CartFlows sont consultables, mais un export regulier te donne un backup et une trace historique de tes performances.

Conseil : exporte une fois par mois. Cree un dossier "Analytics CartFlows" dans ton Google Drive et stocke un fichier par mois. Au bout de 6 mois, tu auras une vue d'ensemble de l'evolution de tes funnels.

---

**[OUTRO — face camera]**

Le tableau de bord Analytics de CartFlows est ton cockpit. Il te dit ce qui fonctionne, ce qui ne fonctionne pas, et ou concentrer tes efforts. Prends l'habitude de le consulter chaque semaine — cinq minutes suffisent pour reperer une anomalie ou confirmer une tendance.

Dans la prochaine lecon, on va definir les trois KPIs que tu dois suivre en priorite : taux de conversion, AOV et RPV.

---

## Notes de production

- **Visuels** : captures CartFlows Analytics (vue globale, metriques par flow, detail par step, filtres, export), schema entonnoir avec abandons
- **Captures d'ecran** : CartFlows Pro — Analytics dashboard (6 captures minimum)
- **Ton** : guide pratique, navigation ecran par ecran
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine directement sur L6.6 (KPIs essentiels)

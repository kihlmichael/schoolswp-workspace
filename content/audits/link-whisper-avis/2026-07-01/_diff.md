---
slug: link-whisper-avis
type: diff
compare_from: 2026-05-22/synthese.md
compare_to: 2026-07-01/synthese.md
date: 2026-07-03
---

# Diff link-whisper-avis : 2026-05-22 (refonte) -> 2026-07-01 (J+40)

Comparaison du snapshot de refonte (22 mai) et du point de controle J+40 (mesures GSC + DataForSEO live du 3 juillet). But : voir ce que le refresh leger a reellement bouge.

> Attention sur les fenetres de temps : le baseline du 22 mai est un cumul GSC 90 jours (2026-02-21 -> 2026-05-22). Le J+40 compare deux fenetres de 28 jours (avant : 24 avr. - 21 mai / apres : 3 juin - 1er juil.). Les positions par requete et les rich results sont comparables ; les volumes de clics/impressions ne le sont pas directement (90j vs 28j), les colonnes ci-dessous le precisent.

## 1. Positions par requete cible

| Requete                                   | Position mai 2026     | Position juil. 2026 (GSC 28j) | Position juil. 2026 (SERP live FR) | Evolution                              |
| ----------------------------------------- | --------------------- | ----------------------------- | ---------------------------------- | -------------------------------------- |
| `link whisper` (cible #1, informationnel) | 8,6                   | 6,6                           | #4 organique (abs. 6)              | En hausse (-2,0)                       |
| `linkwhisper` (cible #2, navigationnel)   | 20,6                  | 21,0                          | #6 en live (volatil)               | Plat en moyenne GSC, bon en live       |
| `link whisper wordpress`                  | 5,4                   | 5,0                           | #4 organique (abs. 5)              | Stable / leger mieux                   |
| `link whisper avis` (fantome)             | #2 (thruuu, 0 volume) | 0 impression                  | #2 organique (abs. 3)              | Toujours bien place, toujours 0 trafic |

Lecture : la cible principale `link whisper` progresse nettement (8,6 -> 6,6). La cible navigationnelle `linkwhisper` reste bloquee en moyenne GSC (Google privilegie le site officiel + wordpress.org), avec une forte volatilite (un releve live la place a #6).

## 2. Trafic page

| Metrique    | Mai 2026 (baseline 90j) | Juil. 2026 (fenetre 28j apres)            | Evolution                               |
| ----------- | ----------------------- | ----------------------------------------- | --------------------------------------- |
| Clics       | 3 (sur 90j)             | 1 (sur 28j, soit ~3 / 90j au meme rythme) | Stable, toujours quasi nul              |
| Impressions | 1 343 (sur 90j)         | 390 (sur 28j) / 407 (28j avant)           | Stable a la baisse (-4,2 % avant/apres) |
| CTR         | 0,22 %                  | 0,26 %                                    | Plancher, pas de decollage              |

Lecture : aucun gain de trafic a J+40. Le CTR reste au plancher malgre l'etoile Review, qui n'a ete crawlee que le 19 juin (effet non encore visible sur la fenetre de mesure).

## 3. Signaux techniques (le vrai chantier du refresh)

| Signal                            | Mai 2026 (avant refresh)       | Juil. 2026 (J+40)                                                      | Evolution                                           |
| --------------------------------- | ------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------- |
| Rich result Review (etoile 4,5/5) | Absent                         | Detecte par Google + affiche dans la SERP live                         | GAGNE (levier CTR #1)                               |
| Rich result Breadcrumbs           | Valide                         | Valide                                                                 | Maintenu                                            |
| Rich result FAQPage               | Absent                         | Toujours pas de rich result SERP (normal : gov/sante only depuis 2023) | Inchange (blocage structurel Google, pas technique) |
| Dernier crawl Googlebot           | 2026-04-23 (un mois de retard) | 2026-06-19                                                             | GAGNE (indexation post-refresh prise en compte)     |
| Liens internes entrants           | 2                              | ~14                                                                    | GAGNE (fait au refresh)                             |

Lecture : c'est ici que le refresh a paye. Les trois signaux vises (etoile Review, fraicheur de crawl, maillage) sont tous acquis. Le trafic n'a simplement pas encore suivi.

## 4. Contexte marche (volumes DataForSEO, FR)

| Mot-cle        | Volume mai 2026 | Volume juil. 2026 | Tendance                               |
| -------------- | --------------- | ----------------- | -------------------------------------- |
| `link whisper` | 390             | 320               | Declin annuel -80 %, trimestriel -46 % |
| `linkwhisper`  | 480             | 320               | Idem (cluster synonyme)                |

Lecture : le declin structurel diagnostique en mai se confirme. Le plafond de trafic realiste est revu a la baisse (~20-30 clics/mois max meme en top 5). Cela valide le calibrage "effort leger" plutot que "reecriture lourde".

## 5. Bilan de l'evolution

| Statut du dossier | Mai 2026                                                          | Juil. 2026                                                                     |
| ----------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Etat              | Refonte appliquee (`refonte-appliquee`)                           | En monitoring (`en-monitoring`)                                                |
| Verdict           | Refresh leger cible (technique + signal) au lieu d'une reecriture | Resultats mitiges : signaux acquis, trafic pas encore suivi, plafond en baisse |

**Conclusion du diff :** le refresh a fait exactement ce qu'il devait cote signaux (etoile Review live, crawl frais, `link whisper` de 8,6 a 6,6, maillage a ~14), mais la conversion en clics n'a pas eu lieu a J+40. Deux causes : l'etoile est trop recente (crawl du 19 juin) pour avoir deja bouge le CTR, et le cluster decline structurellement (-80 %/an). Decision coherente : laisser murir l'etoile, monitoring leger, ne pas sur-investir. Prochain point de mesure : 2026-10-01 (ou plus tot si signal negatif).

> Note : la section 4 (re-scan thruuu) du snapshot 2026-07-01 reste a completer manuellement (pas d'API thruuu). Elle n'affecte pas le verdict, deja etaye par GSC + DataForSEO.

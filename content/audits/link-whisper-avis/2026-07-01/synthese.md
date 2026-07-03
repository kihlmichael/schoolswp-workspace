---
slug: link-whisper-avis
url: https://schoolswp.com/link-whisper-avis/
date_snapshot: 2026-07-01
trigger: Snapshot mesure d'impact post-refonte J+40 (routine programmee depuis 2026-05-22, trig_01LgU9Ei26gwnBuEuMMhjftQ)
status: en-monitoring
---

# Snapshot J+40 : link-whisper-avis - 2026-07-01

> Snapshot rempli le 2026-07-03. Sections 2 (GSC) et 3 (DataForSEO) : mesures live via MCP (gsc-mcp + dataforseo, marche FR). Section 4 : contenu verifie via Novamira + scores on-page mesures via DataForSEO ; les 2 metriques strictement proprietaires a thruuu (Page Rank, score global) sont remplacees par l'equivalent DataForSEO `onpage_score`, faute d'API thruuu. Section 5 : verdict a partir des sections 2 et 3. Un `_diff.md` accompagne ce fichier (comparaison avec `2026-05-22/synthese.md`).

## 1. Contexte - ce qui a ete fait le 22 mai 2026

Le 22 mai 2026, l'article `/link-whisper-avis/` (post WordPress 58166) a recu un refresh leger apres audit complet 4 sources (GSC + DataForSEO + thruuu + WP REST). Ce snapshot mesure l'impact 40 jours apres le deploiement.

### 1a. Diagnostic qui a declenche le refresh

L'audit 2026-05-22 avait etabli que la cible initiale du sprint (`linkwhisper avis`) etait un mot-cle fantome : 0 impression mesurable en 90 jours GSC, 0 volume DataForSEO. La page etait deja #2 dessus sans trafic. Les vraies cibles identifiees : `link whisper` (390/mois, informationnel, position GSC 8,6) et `linkwhisper` (480/mois, navigationnel, position 20,6). Le probleme n'etait pas le contenu (audit thruuu quasi tout vert) mais les signaux : 2 liens internes seulement, aucun rich result valide hormis les breadcrumbs, crawl Googlebot vieux d'un mois.

### 1b. Actions deployees le 22 mai 2026

| #                   | Action deployee                                                                                                                                                                                                                                                                         | Statut |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Ciblage             | Focus keyword change vers `link whisper` (abandon de `linkwhisper avis`)                                                                                                                                                                                                                | Fait   |
| Titre Rank Math     | `Link Whisper : mon avis apres 21 mois de maillage interne` (emoji et annee retires)                                                                                                                                                                                                    | Fait   |
| Contenu             | H2 "c'est quoi" ajoute, fonctionnalites remontes en H2 dedie, FAQ 6 Q/R (accordeon Kadence), encarts chiffres d'experience reels (195 liens crees, 449 articles analyses, 207 clics trackes, 144 liens brises), terme `google search console` integre                                   | Fait   |
| Schemas structures  | BlogPosting + Review (4,5/5 SoftwareApplication) + FAQPage (6 Q/R) via Rank Math - base : Breadcrumbs seul                                                                                                                                                                              | Fait   |
| Maillage interne    | 9 liens entrants ajoutes : thot-seo-avis, avis-linkcentral-wordpress, core-web-vitals-wordpress, changer-extension-seo-wordpress, surerank-avis-plugin-seo, avis-chatseo-test-complet, wisewand-avis-redaction-seo, avis-skoatch, wisewand-vs-skoatch. Total entrant : ~14 (vs 2 avant) | Fait   |
| Images a la une     | Hero editorial FR (media 2932527), DE post #58572 (media 2932818), EN post #58580 (media 2932822). Ancien media 58636 supprime.                                                                                                                                                         | Fait   |
| Signal de fraicheur | post_modified = 2026-05-22, URL inspection GSC : verdict PASS                                                                                                                                                                                                                           | Fait   |

### 1c. Metriques de reference pre-refresh (GSC 90j : 2026-02-21 -> 2026-05-22)

| KPI                               | Valeur baseline        |
| --------------------------------- | ---------------------- |
| Clics page 90j                    | 3                      |
| Impressions page 90j              | 1 343                  |
| CTR moyen                         | 0,22 %                 |
| Position moyenne                  | 13,9                   |
| Position `link whisper`           | 8,6                    |
| Position `linkwhisper`            | 20,6                   |
| Position `link whisper wordpress` | 5,4                    |
| Rich results valides Google       | Breadcrumbs uniquement |
| Liens internes entrants           | 2 (avant refresh)      |

---

## 2. Performance GSC : /link-whisper-avis/

**Instructions de releve :**
GSC -> Performance -> Filtrer : type = Web, page = `https://schoolswp.com/link-whisper-avis/`
Mode "Comparer" : periode avant = 2026-04-24 au 2026-05-21 (28j avant le refresh) / periode apres = 2026-06-03 au 2026-07-01 (28 derniers jours).

### 2a. Vue globale page (comparaison 28j avant vs 28j apres)

| KPI              | 28j avant (24 avr. - 21 mai 2026) | 28j apres (3 juin - 1er juil. 2026) | Delta                                 |
| ---------------- | --------------------------------- | ----------------------------------- | ------------------------------------- |
| Clics            | 1                                 | 1                                   | 0                                     |
| Impressions      | 407                               | 390                                 | -17 (-4,2 %)                          |
| CTR              | 0,25 %                            | 0,26 %                              | +0,01 pt (stable)                     |
| Position moyenne | 12,9                              | 14,6                                | +1,7 (leger recul de la moyenne page) |

> Lecture : la moyenne de position au niveau page recule (12,9 -> 14,6), mais c'est un artefact. Elle est tiree vers le bas par `linkwhisper` (185 impressions a la position 21), la plus grosse masse d'impressions de la page. La vraie cible `link whisper` progresse, elle (voir 2b). La position moyenne page-level n'est donc pas un bon KPI ici.

### 2b. Positions par requete cible (28 derniers jours : 2026-06-03 -> 2026-07-01)

GSC -> onglet "Requetes", filtre page `/link-whisper-avis/`, periode 28 derniers jours.

| Requete                             | Clics | Impressions | CTR | Position               |
| ----------------------------------- | ----- | ----------- | --- | ---------------------- |
| `link whisper`                      | 0     | 77          | 0 % | 6,6                    |
| `linkwhisper`                       | 0     | 185         | 0 % | 21,0                   |
| `link whisper wordpress`            | 0     | 4           | 0 % | 5,0                    |
| `link whisper plugin`               | 0     | 2           | 0 % | 7,0                    |
| `link whisper avis`                 | 0     | 0           | -   | absente (0 impression) |
| `linkwhisper avis`                  | 0     | 0           | -   | absente (0 impression) |
| `linkwisper` (typo)                 | 0     | 3           | 0 % | 6,7                    |
| `maillage interne plugin wordpress` | 0     | 0           | -   | absente (0 impression) |

> Lecture : 0 clic sur l'ensemble des requetes cibles en 28 jours. La masse d'impressions se concentre sur `linkwhisper` (185 impr, position 21 = page 2-3, aucun clic structurellement possible) et `link whisper` (77 impr, position 6,6 = bas de page 1, CTR plancher malgre l'etoile). Les deux requetes "avis" restent des mots-cles fantomes : 0 impression, ce qui confirme le diagnostic de mai. `link whisper` a bien gagne en position (8,6 -> 6,6) mais pas encore assez pour transformer les impressions en clics.

### 2c. Nouvelles requetes apparues depuis le refresh

Lister toutes les requetes presentes dans la periode apres mais absentes (ou < 5 impressions) dans la periode avant. Signe que l'enrichissement du contenu a capte de nouveaux signaux.

| Requete                                          | Clics | Impressions | Position | Note                                                                                           |
| ------------------------------------------------ | ----- | ----------- | -------- | ---------------------------------------------------------------------------------------------- |
| `link whisper review`                            | 0     | 7           | 48       | Seule vraie nouvelle requete >= 5 impr. Intention anglaise (page /en/), position 48 = hors jeu |
| `link whisper internal linking wordpress plugin` | 0     | 4           | 7,5      | Longue traine EN, nouvelle mais < 5 impr                                                       |
| `link whisper price`                             | 0     | 1           | 11       | Nouvelle, negligeable                                                                          |

> Bilan honnete : l'enrichissement du contenu n'a PAS capte de nouvelle requete FR significative. A l'inverse, deux requetes de longue traine "maillage interne" presentes avant le refresh ont disparu apres (`plugin maillage interne wordpress` : 2 impr pos 16 ; `plugin worpdpress maillage interne` : 5 impr pos 15,8). Le bilan net sur la longue traine est une legere erosion, pas un gain. La seule nouveaute reelle est anglophone et mal positionnee.

### 2d. Rich results - URL Inspect GSC

GSC -> Inspection d'URL -> `https://schoolswp.com/link-whisper-avis/` -> onglet "Resultats enrichis".

| Schema                           | Valide par Google                                                                                                                             | Eligible rich result SERP                                                                                     | Etat avant refresh      |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Breadcrumbs                      | Oui (detecte, verdict PASS)                                                                                                                   | Oui                                                                                                           | Valide                  |
| Review / AggregateRating (4,5/5) | Oui - `Review snippets` detecte par Google + etoile 4,5 affichee dans la SERP live (verifie sur link whisper, linkwhisper, link whisper avis) | Oui                                                                                                           | Absent                  |
| FAQPage (6 Q/R)                  | Non liste par Google                                                                                                                          | Non - normal : rich results FAQ reserves aux sites gov/sante depuis 2023 ; le schema reste valide et lu (GEO) | Absent                  |
| BlogPosting                      | Present dans le code (type non "rich result")                                                                                                 | n/a                                                                                                           | Present mais non valide |

> Signal fort : dernier crawl Googlebot = **2026-06-19 22:50** (contre 2026-04-23 au baseline, un mois de retard). La demande d'indexation post-refresh a ete prise en compte. Verdict d'indexation : PASS, `Submitted and indexed`, canonical correct, crawl mobile. C'est le gain le plus net du refresh cote signaux : l'etoile Review, absente en mai, est desormais servie dans la SERP.

---

## 3. Volumes et positions DataForSEO

**Instructions de releve :**
DataForSEO -> Keywords Data -> Search Volume -> marche FR (location_code 2250, language_code fr).
Puis SERP -> Organic pour verifier la position de schoolswp.com sur chaque mot-cle.

| Mot-cle                                      | Volume mai 2026 (ref.) | Volume juil. 2026            | Tendance                                 | KD (ref.)      | Position schoolsWP juil. 2026                         |
| -------------------------------------------- | ---------------------- | ---------------------------- | ---------------------------------------- | -------------- | ----------------------------------------------------- |
| `link whisper`                               | 390                    | 320                          | mensuel +53 %, trim. -46 %, annuel -80 % | 7 (9 en juil.) | #4 organique / abs. 6 (etoile 4,5 affichee)           |
| `linkwhisper`                                | 480                    | 320                          | idem (cluster synonyme de link whisper)  | 7 (9 en juil.) | #4 organique / abs. 6 en SERP live - mais GSC moy. 21 |
| `link whisper wordpress`                     | n.d. (< 10)            | 10                           | plat                                     | n.d.           | #4 organique / abs. 5                                 |
| `link whisper plugin`                        | n.d. (< 10)            | 10                           | trim. et annuel -100 %                   | n.d.           | GSC moy. 7,0 (SERP live non releve, volume marginal)  |
| `link whisper avis`                          | ~0 (fantome)           | 0 (aucune donnee DataForSEO) | -                                        | n.d.           | #2 organique / abs. 3 (etoile 4,5) - mais 0 volume    |
| `lien interne wordpress plugin`              | n.d.                   | 0 (aucune donnee DataForSEO) | -                                        | n.d.           | non releve (volume nul)                               |
| `meilleur plugin maillage interne wordpress` | n.d.                   | 0 (aucune donnee DataForSEO) | -                                        | n.d.           | non releve (volume nul)                               |

> Note structurelle CONFIRMEE : `link whisper` / `linkwhisper` (traites comme synonymes par DataForSEO, volume commun 320) poursuivent leur declin. Tendance annuelle -80 %, trimestrielle -46 %. Historique des mois : pic 880 en juin 2025, 480 en fev.-mars 2026, 170 en avril, 260 en mai 2026. Le +53 % mensuel est un rebond court terme (170 -> 260), pas une inversion de tendance. Consequence pour le Verdict : plafond de trafic revu a la baisse. Meme en top 5 sur `link whisper`, l'ordre de grandeur realiste reste ~20-30 clics/mois au maximum.

---

## 4. Score de re-scan thruuu

**Instructions de releve :**
thruuu -> Audit de page -> URL : `https://schoolswp.com/link-whisper-avis/` -> mot-cle : `link whisper` -> google.fr, FR, desktop.

> STATUT : section renseignee le 2026-07-03 avec de la donnee mesuree - Novamira (contenu, server-side) et DataForSEO on-page (scores + benchmark concurrentiel). Les deux metriques strictement propres a thruuu (Page Rank thruuu, checklist "score global") ne sont pas reproductibles sur leur echelle : elles sont accompagnees de l'equivalent mesure DataForSEO (`onpage_score`), clairement etiquete. Un run thruuu reste possible pour les chiffres exacts sur son echelle.

| Dimension                                  | Etat mai 2026                        | Etat juil. 2026                                                                                                                                                                  | Objectif                              |
| ------------------------------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Word count (fourchette SERP)               | OK - 2 567 mots (moy. SERP : 2 417)  | 3 422 mots page entiere / ~2 713 mots corps (DataForSEO + Novamira). 2e profondeur du top editorial FR : webandseo 3 197, acreferencement 1 940, blogdumoderateur 565            | Dans la fourchette                    |
| Nombre d'images                            | OK - 20 (moy. SERP : 20)             | 16 images (page, DataForSEO). Ordre de grandeur maintenu                                                                                                                         | Maintien                              |
| Couverture termes frequents SERP           | OK                                   | Maintenue - la page couvre tous les axes du top SERP : definition, prix, pour qui, avantages, liens brises/404, alternatives, compatibilite WordPress, FAQ, avis clients (11 H2) | Maintien ou amelioration              |
| Terme `google search console` present      | Absent (0)                           | Present (confirme Novamira)                                                                                                                                                      | Present (ajoute au refresh)           |
| Bloc FAQ structure detecte                 | Absent                               | Present - bloc `kadence/accordion` ("Des questions sur Link Whisper ?")                                                                                                          | Present (6 panes accordeon Kadence)   |
| H2 "c'est quoi" present                    | Absent                               | Present - 1er H2 : "Link Whisper, c'est quoi ?"                                                                                                                                  | Present (titre le plus frequent SERP) |
| Page Rank thruuu                           | 28 (SERP moy. : 31)                  | Echelle proprietaire thruuu, non reproductible via MCP. Equivalent mesure : `onpage_score` DataForSEO 97,07/100 (voir note)                                                      | 28 ou plus                            |
| Score global thruuu                        | Quasi tout vert (1 anomalie mineure) | Echelle proprietaire thruuu, non reproductible via MCP. Equivalent mesure : `onpage_score` DataForSEO 97,07/100 - top tier                                                       | Tout vert ou quasi                    |
| Position schoolswp.com dans la SERP thruuu | #2 sur `linkwhisper avis`            | #4 organique sur `link whisper` (DataForSEO live 2026-07-03)                                                                                                                     | Maintien #1-3                         |

> Benchmark on-page DataForSEO (2026-07-03) : `onpage_score` schoolswp = **97,07/100**, dans le peloton de tete du top FR (webandseo 98,9 / blogdumoderateur 98,2 / schoolswp 97,07 / acreferencement 93,4). C'est un score technique on-page DataForSEO, distinct de l'echelle "Page Rank / score global" de thruuu, mais il confirme que la page reste tres bien optimisee. Contenu (Novamira) : les 3 ajouts du refresh sont toujours en place (H2 "c'est quoi", FAQ Kadence, terme "google search console"), 11 H2 editoriaux, post_modified 2026-05-26.

---

## 5. Verdict et prochaines actions

### 5a. Verdict global

**Resultats mitiges.** Le refresh leger de mai a fait ce pour quoi il etait concu au niveau des signaux : l'etoile Review (4,5/5) est desormais servie dans la SERP (levier CTR #1 identifie en mai), le crawl a ete rafraichi (2026-06-19), et `link whisper` a gagne des positions (8,6 -> 6,6, 4e resultat organique). Mais l'impact trafic est nul a J+40 : toujours ~1 clic, CTR plancher (0,26 %), et la cible navigationnelle `linkwhisper` (la plus grosse masse d'impressions) reste bloquee en moyenne GSC autour de la position 21, meme si un releve SERP live ponctuel la place a #6 (forte volatilite). Le cluster poursuit son declin structurel (-80 %/an), ce qui confirme le calibrage "effort leger" de mai. En clair : les signaux sont poses, le trafic n'a pas encore suivi, et le plafond baisse. L'etoile n'ayant ete crawlee que le 19 juin, son effet CTR reste a confirmer sur le prochain point de mesure.

### 5b. Bilan KPI vs objectifs fixes au snapshot 2026-05-22

| Objectif                          | Baseline (2026-05-22) | Cible fixee | Resultat (2026-07-01)                              | Atteint ?                                      |
| --------------------------------- | --------------------- | ----------- | -------------------------------------------------- | ---------------------------------------------- |
| Position `link whisper`           | 8,6                   | top 5       | 6,6 (GSC) / #4 organique en SERP live              | Partiel - proche, hors top 5 strict            |
| Position `linkwhisper`            | 20,6                  | top 10      | 21,0 (GSC moy.) / #6 en SERP live                  | Non (GSC) - forte volatilite                   |
| Clics page 90j                    | 3                     | > 20        | ~1 clic / 28j (soit ~3 / 90j)                      | Non - tres loin                                |
| Rich result Review (4,5/5) valide | Non                   | Oui         | Oui - etoile detectee et affichee en SERP          | Oui                                            |
| Rich result FAQPage valide        | Non                   | Oui         | Non - FAQ rich result = gov/sante only depuis 2023 | Non (blocage structurel Google, pas technique) |
| Liens internes entrants           | 2                     | 8-10        | ~14                                                | Oui - atteint au refresh                       |

### 5c. Prochaines actions

| #   | Action                                                                                                                                                              | Priorite | Effort        | Responsable |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- | ----------- |
| 1   | Laisser murir l'etoile Review (crawlee le 19/06) et re-mesurer le CTR de `link whisper` : l'effet SERP d'un rich result met souvent 4-8 semaines a se refleter      | Haute    | Nul (attente) | Michael     |
| 2   | Ne PAS sur-investir : cluster en declin structurel (-80 %/an), plafond de trafic faible confirme. Monitoring Rank Math hebdo suffit                                 | Haute    | Nul           | Michael     |
| 3   | Accepter `linkwhisper` (navigationnel) comme plafond dur : le site officiel et wordpress.org occupent structurellement le haut. Ne pas y consacrer d'effort contenu | Moyenne  | Nul           | -           |
| 4   | Pousser 1-2 liens internes de plus depuis des pages a trafic pour aider `link whisper` a passer le top 5 strict (seul levier realiste restant)                      | Basse    | Faible        | radar       |
| 5   | Prochain snapshot : 2026-10-01 (3 mois) sauf signal negatif. Objectif : verifier si l'etoile a fait bouger le CTR                                                   | Moyenne  | Faible        | routine     |

> Reperes de decision :
>
> - Progression confirmee : monitoring Rank Math weekly suffit. Prochain snapshot si signal negatif ou dans 3 mois (vers 2026-10-01).
> - Stagnation : identifier le blocage (schema non valide par Google ? indexation lente ? maillage insuffisant ?) et planifier un ajustement cible.
> - Regression : audit urgent. Creer `_diff.md`, verifier la tendance day-by-day dans GSC.

---

_Snapshot rempli le 2026-07-03 (GSC + DataForSEO live via MCP, contenu via Novamira, on-page via DataForSEO). Commit : `audit(link-whisper-avis): snapshot 2026-07-01 + mesures remplies`. Le `_diff.md` de ce dossier compare avec `2026-05-22/synthese.md`._

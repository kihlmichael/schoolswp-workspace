# Audit DE J+30 - /de/vergleich-flyingpress-wp-rocket/

**Date du jalon** : 2026-06-25 (J+30 post-refonte)
**Capture des donnees** : 2026-06-24 (J+29, veille du jalon, choix "lancer maintenant"). A un jour pres les positions SERP sont materiellement identiques.
**Post ID** : 343161
**Permalink** : <https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/>
**Slug** : `vergleich-flyingpress-wp-rocket`
**Langue declaree** : `de` (Polylang)
**Statut** : publish
**Refonte poussee** : 2026-05-26 (SHA `e1dc5666...`)
**Translations Polylang** : `de=343161 | fr=52819 | en=343156` (triade intacte, verifiee live)

---

## 1. Synthese executive

**Verdict global** : 🟢 **SUCCES MAJEUR. La refonte a converti : de "absent du top 30" (J+7) a #1 organique (J+30) sur la requete exacte `flyingpress vs wp rocket` (de_DE).**

| Axe                        | Baseline 2026-05-26    | J+7 (2026-06-01)     | **J+30 (2026-06-24)**                 | Verdict             |
| -------------------------- | ---------------------- | -------------------- | ------------------------------------- | ------------------- |
| Position SERP de_DE (live) | Absent top 12          | Absent top 30        | **🏆 #1 (rank_absolute 1)**           | 🟢 Objectif explose |
| Langue body                | DE=4 / FR=197 (FR pur) | DE=297 / FR=27       | **DE pur (FR=0 marqueurs)**           | 🟢 Stable           |
| SHA256 body                | `7fd4d998...` (avant)  | `e1dc5666...`        | **`e1dc5666...` (identique)**         | 🟢 Zero derive      |
| Featured image evergreen   | "2025" + en-dash       | partiellement patche | **0 "2025", 0 dash**                  | 🟢 P1 cloture       |
| Cloaks /de/ affilies       | 301 casse vers review  | 301 casse            | **302 vers slug canonique**           | 🟢 P2 cloture       |
| Ranked keywords Labs (URL) | 0                      | 0                    | **0 (lag base Labs, voir section 4)** | 🟡 Lag DB           |

**Objectif J+30 du brief initial** : "emerger sur >= 1 keyword DE rank_group <= 30". **Resultat : #1 sur le keyword principal.** Objectif depasse.

**Actions appliquees ce jour** (decision Michael "lancer maintenant + P1 + P2") :

- ✅ P1 : retire la derniere occurrence "2025" de la description de l'attachment 350864.
- ✅ P2 : corrige le mu-plugin `schoolswp-affiliate-cloaks.php` (v1.1.1 -> v1.2.0) pour router les variantes localisees `/de|en|fr/flyingpress/` et `/wp-rocket/` vers le slug canonique (ClickWhale reprend la main, tracking + nofollow/sponsored preserves).

---

## 2. Resultat SERP de_DE (live, capture 2026-06-24)

Source : DataForSEO `serp_organic_live_advanced`, keyword `flyingpress vs wp rocket`, Germany / de, depth 100 (dump : [serp-live-de.json](./serp-live-de.json)).

| Pos abs | Type             | Domaine                                               | Note                                                        |
| ------- | ---------------- | ----------------------------------------------------- | ----------------------------------------------------------- |
| **1**   | **organic**      | **schoolswp.com/de/vergleich-flyingpress-wp-rocket/** | 🏆 **#1. Snippet date du 26.05.2026 (jour de la refonte).** |
| 2       | organic          | reddit.com (r/Wordpress, traduit DE)                  | thread communautaire                                        |
| 3       | organic          | wp-rocket.me (EN)                                     | la page officielle WP Rocket, derriere schoolsWP            |
| 4       | organic          | wpservice.pro (EN, 2024)                              |                                                             |
| 5       | video            | YouTube (3 videos, EN)                                | pack video                                                  |
| 6       | organic          | mcstarters.com (EN, 2026)                             |                                                             |
| 7       | PAA              | 3 questions DE                                        | Was macht WP Rocket / DSGVO / kostenlos                     |
| 8       | organic          | dowebwork.de (DE, 2023)                               | concurrent DE natif, recule (etait pos 7 au J+7)            |
| 9       | organic          | wpjohnny.com (EN, 2020)                               |                                                             |
| 10      | organic          | wpdiscounts.io (EN, 2026)                             |                                                             |
| 11      | organic          | linkedin.com (EN)                                     |                                                             |
| 12      | related_searches | 8 requetes liees                                      |                                                             |

**Lecture strategique** :

- schoolsWP passe **devant la page officielle de wp-rocket.me** et devant tous les concurrents EN. C'est la seule page DE native fraiche (2026) sur une SERP encore dominee par de l'anglais et des contenus DE vieux (dowebwork 2023).
- `techboys.de` (concurrent DE natif benchmark a J+0, pos 6) a disparu du top 12. La SERP recompense la fraicheur + la langue native.
- **AI Overview** : non observe dans ce pull live (la baseline notait un AIO asynch actif). A re-surveiller mensuellement.
- Le snippet servi par Google est l'amorce du H2 Fazit DE ("Das haengt von Ihren Beduerfnissen ab: FlyingPress besticht durch seine Einfachheit..."). C'est bien le contenu refondu qui rank, pas un cache FR residuel.

---

## 3. Verification on-page live (read-only via Novamira)

Lecture directe en base (`get_post` + post_meta), 2026-06-24 :

| Champ                              | Valeur                                                                                           | Verdict                                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| post_title                         | `FlyingPress vs WP Rocket 2026 : Welches Cache-Plugin fuer WordPress?`                           | 🟢 DE natif                                                                                                                |
| post_status / modified             | publish / 2026-05-26 17:34:29                                                                    | 🟢 inchange depuis refonte                                                                                                 |
| **SHA256 body**                    | `e1dc5666c12010606d927bebb56ecb644ca842b0bd77f989b504a1c198c3ebe5`                               | 🟢 **identique au push J+0, zero derive**                                                                                  |
| Bytes body                         | 18 737                                                                                           | 🟢 identique                                                                                                               |
| Langue (heuristique)               | DE=276 marqueurs / FR=0                                                                          | 🟢 DE pur                                                                                                                  |
| Marqueurs structure                | `Das schnelle Urteil` + `Optimale Einstellungen` + `Fazit` presents ; `Le Verdict Rapide` absent | 🟢                                                                                                                         |
| Em-dash / en-dash body             | 0 / 0                                                                                            | 🟢 brand-strict                                                                                                            |
| "2025" body / "2024" body          | 0 / 1 (URL upload SVG logo /2024/06/, legitime)                                                  | 🟢                                                                                                                         |
| Liens internes schoolswp.com       | 7                                                                                                | 🟢 densifie (etait 4)                                                                                                      |
| Cloaks /flyingpress/ + /wp-rocket/ | 3 + 2 (formes nues)                                                                              | 🟢                                                                                                                         |
| Boutons Kadence advancedbtn        | 4 occurrences (2 CTA)                                                                            | 🟢                                                                                                                         |
| rank_math_title                    | `FlyingPress vs WP Rocket 2026: welches Cache-Plugin?` (50 car.)                                 | 🟢 **raccourci depuis J+0** : corrige le defaut "title 72/75 car. trop long" de thruuu. C'est le titre affiche en SERP #1. |
| rank_math_description              | DE, 176 car.                                                                                     | 🟢                                                                                                                         |
| rank_math_focus_keyword            | `flyingpress vs wp rocket,wp rocket vs flyingpress`                                              | 🟢                                                                                                                         |
| rank_math_robots                   | (vide = index, follow)                                                                           | 🟢                                                                                                                         |
| Polylang triade                    | `{de:343161, fr:52819, en:343156}`                                                               | 🟢 intacte                                                                                                                 |

**Conclusion** : la page est stable, brand-strict, indexee, et le contenu refondu est exactement celui qui rank #1. Aucune regression depuis le push du 26/05.

---

## 4. DataForSEO Labs ranked_keywords : le lag de base (a comprendre)

Source : `dataforseo_labs_google_ranked_keywords`, target = l'URL exacte, Germany / de (dump : [dataforseo-ranked-keywords-de.json](./dataforseo-ranked-keywords-de.json)).

**Resultat : `items: []` (0 keyword), identique a la baseline du 2026-05-26.**

🟡 **Ce 0 n'est PAS la realite SERP. C'est le lag de la base d'index Labs de DataForSEO.**

- La base Labs `ranked_keywords` est construite a partir de crawls SERP periodiques. Pour un mot-cle ultra-niche (`flyingpress vs wp rocket` = 10 recherches/mois), la cadence de re-crawl de leur DB est lente : elle n'a pas encore enregistre la nouvelle position #1.
- La verite terrain est le **SERP live temps reel** (section 2) : `serp_organic_live_advanced` interroge Google en direct et montre #1.
- **A retenir pour le prochain re-audit** : la base Labs finira par rattraper (prochain crawl). Quand `ranked_keywords` passera de `[]` a un item rank_group 1, ce sera la confirmation differee de ce que le live montre deja aujourd'hui. Tant que la DB Labs n'a pas rattrape, ne pas conclure "0 keyword = echec" : croiser systematiquement avec le SERP live.

**Implication methodo** : pour les keywords ultra-niches, le SERP live est l'instrument de mesure fiable, pas la base Labs agregee.

---

## 5. P1 applique - residuel "2025" featured image

**Cible** : attachment 350864, champ description (post_content).

| Avant                                                        | Apres                                               |
| ------------------------------------------------------------ | --------------------------------------------------- |
| "...nach dem besten WordPress Cache Plugin **2025** suchen." | "...nach dem besten WordPress Cache Plugin suchen." |
| occurrences "2025" = 1                                       | occurrences "2025" = 0 ✅                           |

- Methode : `wpdb->update` sur `wp_posts.post_content`, verifie (`substr_count('2025') = 0` post-update), cache nettoye (`clean_post_cache`).
- Backup de l'ancienne description en postmeta `_schoolswp_bak_att_desc_20260624`.
- title + alt de l'attachment etaient deja propres (0 "2025", 0 dash) depuis la refonte. Cloture P1.
- Le "2024" residuel du body (URL d'upload du logo SVG `/2024/06/...`) est laisse tel quel : chemin d'upload legitime, non evergreen-critique (confirme par le brief).

---

## 6. P2 applique - mu-plugin affiliate cloaks Polylang-aware

### 6.1 Diagnostic affine (plus nuance que le brief)

Le brief decrivait `/de/flyingpress/` et `/de/wp-rocket/` comme "broken, redirige vers FR/EN review", a corriger dans `schoolswp-affiliate-cloaks.php`. La lecture du code a revele que :

- **`flyingpress` et `wp-rocket` ne sont PAS dans ce mu-plugin.** Ils sont geres par **ClickWhale** (table `yym2fb_clickwhale_links`, id 58 et 60) : `/flyingpress/` -> 307 -> `flyingpress.com?aff=fodc` et `/wp-rocket/` -> 307 -> `wp-rocket.me/?ref=69f9e3e7`, avec `nofollow=1` + `sponsored=1` + tracking de clics.
- Le mu-plugin gere d'autres cloaks (`novamira`, `rank-math`, `booknetic` + 3 profils sociaux) et **strippait deja le prefixe Polylang**.
- La cause du `/de/flyingpress/` casse : ClickWhale n'enregistre que la forme nue `/flyingpress/`. La variante prefixee `/de/flyingpress/` tombe dans le devinage 404 de WordPress, qui la resout en 301 vers `/flyingpress-avis/` (review FR). Idem `/en/flyingpress/`, `/fr/...`.

**Etat live verifie avant patch** (UA navigateur, le UA "bot" declenche un 500 Imunify360 trompeur) :

| URL              | Code | Destination                     |
| ---------------- | ---- | ------------------------------- |
| /flyingpress/    | 307  | flyingpress.com?aff=fodc (OK)   |
| /wp-rocket/      | 307  | wp-rocket.me/?ref=69f9e3e7 (OK) |
| /de/flyingpress/ | 301  | /flyingpress-avis/ (CASSE)      |
| /de/wp-rocket/   | 301  | /en/wp-rocket-review/ (CASSE)   |
| /en/flyingpress/ | 301  | /flyingpress-avis/ (CASSE)      |
| /fr/flyingpress/ | 301  | /flyingpress-avis/ (CASSE)      |

Note importante : le **body de l'article DE utilise les formes nues** `/flyingpress/` et `/wp-rocket/` (qui fonctionnent). Les CTA du #1 sont donc sains. Le fix P2 est une robustesse / future-proofing (si un lien `/de/...` est insere un jour).

### 6.2 Decision de design

Mauvaise approche (rejetee) : ajouter `flyingpress`/`wp-rocket` avec une destination en dur dans le mu-plugin. Ca aurait intercepte AUSSI la forme nue `/flyingpress/` (init priorite 1, avant ClickWhale) et **casse le tracking + les attributs nofollow/sponsored** de ClickWhale.

Bonne approche (appliquee, DRY) : **normaliser uniquement les variantes localisees** `/de|en|fr/<slug>/` vers le slug canonique `/<slug>/`, et laisser ClickWhale gerer le redirect final. La forme nue n'est jamais interceptee. ClickWhale reste la source unique de verite (destination + tracking + rel).

### 6.3 Patch (v1.1.1 -> v1.2.0)

- Nouvelle fonction `schoolswp_clickwhale_localized_slugs()` retournant `['flyingpress', 'wp-rocket']` (extensible).
- Handler : memorise `$had_lang_prefix`, et si un prefixe langue etait present ET le slug est gere par ClickWhale, redirige (302) vers la forme nue. Cible construite depuis l'hote canonique (`parse_url(home_url(), PHP_URL_HOST)`) pour eviter toute boucle avec le filtre `home_url()` de Polylang.
- Backup de l'original (sha `82e6b419...`) en `wp_option schoolswp_bak_mu_affiliate_cloaks_20260624`.
- Copies repo : [v1.1.1 original](./_mu-plugin-affiliate-cloaks-v1.1.1-original-backup.php) + [v1.2.0 patche](./_mu-plugin-affiliate-cloaks-v1.2.0-patched.php).

**Procedure d'ecriture securisee** (un mu-plugin qui fatal = site down, pas de crash-recovery) :

1. Transport base64 (fidelite octet) ; 2. `php -l` AVANT ecriture (No syntax errors) ; 3. backup original en wp_option ; 4. `file_put_contents` live + `opcache_invalidate` ; 5. smoke-test homepage (200) avec auto-rollback si != 200. Resultat : sha ecrit = sha source (`225ae165...`), homepage 200, pas de rollback.

### 6.4 Verification post-patch (live, UA navigateur)

| URL                   | Avant                        | Apres                                                           |
| --------------------- | ---------------------------- | --------------------------------------------------------------- |
| /de/flyingpress/      | 301 -> /flyingpress-avis/    | **302 -> /flyingpress/** ✅                                     |
| /de/wp-rocket/        | 301 -> /en/wp-rocket-review/ | **302 -> /wp-rocket/** ✅                                       |
| /en/flyingpress/      | 301 casse                    | **302 -> /flyingpress/** ✅                                     |
| /fr/wp-rocket/        | 301 casse                    | **302 -> /wp-rocket/** ✅                                       |
| /flyingpress/ (nue)   | 307 -> flyingpress.com       | **307 -> flyingpress.com** ✅ (inchange)                        |
| /wp-rocket/ (nue)     | 307 -> wp-rocket.me          | **307 -> wp-rocket.me** ✅ (inchange)                           |
| /de/novamira/         | 302 -> dynamic.ooo           | **302 -> dynamic.ooo** ✅ (cloak existant intact)               |
| /de/flyingpress-avis/ | 301 -> /flyingpress-avis/    | **301 -> /flyingpress-avis/** ✅ (vraie page, pas d'over-match) |

Chaine complete : `/de/flyingpress/` -> 302 -> `/flyingpress/` -> 307 -> `flyingpress.com?aff=fodc` (tracking ClickWhale + nofollow/sponsored conserves). Zero regression. P2 cloture.

---

## 7. thruuu (item optionnel du brief)

**Decision : skip documente.** La condition "position SERP top 30" est remplie (on est #1), mais la valeur marginale de thruuu est faible :

- thruuu sert a savoir quoi ajouter pour MONTER dans le SERP. Or on est deja #1.
- L'on-page est deja valide (SHA stable, 0 dash, DE pur, schemas presents, title raccourci). Rien a corriger.

Disponible sur demande si on veut un calibrage on-page formel (ex : densifier les images, 5 vs SERP avg 20, seul gap thruuu connu, non bloquant a #1).

---

## 8. KPI - boucle fermee

| KPI                                              | Baseline 2026-05-26 | Cible J+30         | Reel J+30 (2026-06-24)     |
| ------------------------------------------------ | ------------------- | ------------------ | -------------------------- |
| Position de_DE `flyingpress vs wp rocket` (live) | absent top 20       | >= 1 kw rank <= 30 | **#1** 🟢                  |
| Ranked keywords Labs (URL)                       | 0                   | (indicatif)        | 0 (lag DB, voir section 4) |
| Langue body                                      | FR=197/DE=4         | DE natif           | DE pur (FR=0) 🟢           |
| Brand evergreen (image)                          | "2025" + dash       | propre             | 0 "2025" / 0 dash 🟢       |
| Cloaks /de/ affilies                             | 301 casse           | route correct      | 302 -> canonique 🟢        |

---

## 9. Prochaines etapes recommandees

### Monitoring (pas d'action de refonte requise)

1. **Re-audit J+60 (vers 2026-07-25)** : confirmer la tenue du #1 + verifier que la base Labs DataForSEO a rattrape (ranked_keywords passe de `[]` a rank 1). Idealement coupler avec un check GSC (clics / impressions reels sur la page).
2. **AI Overview de_DE** : surveiller mensuellement si Google active un AIO sur cette query et si schoolsWP y est cite (signal d'autorite).
3. **Longue traine DE** : surveiller l'emergence de `wp rocket preise`, `wp rocket einstellungen`, `bestes wordpress cache plugin` (le contenu refondu inclut la section "Optimale Einstellungen").

### Cross-langues

4. La synthese cross-langues est mise a jour (section DE passe a #1). Voir [synthese-cross-langues.md](../../flyingpress-wp-rocket-comparison-fr/2026-05-26/synthese-cross-langues.md).
5. Le bug "AI Overview FR protege tant que la France n'active pas l'AIO" reste a surveiller cote FR (FS #1).

### Dette technique residuelle (hors scope refonte)

6. P2 etendu (optionnel) : si d'autres articles multilingues utilisent des cloaks ClickWhale en forme `/de/<slug>/`, ajouter ces slugs a `schoolswp_clickwhale_localized_slugs()`.

---

## 10. Artefacts de ce snapshot

```
content/audits/flyingpress-wp-rocket-comparison-de/2026-06-25/
├── audit.md                                          (ce fichier)
├── state-after-v2.json                               (etat machine-readable + diff vs J+0)
├── serp-live-de.json                                 (SERP live #1)
├── dataforseo-ranked-keywords-de.json                (reponse Labs [] + note lag)
├── _mu-plugin-affiliate-cloaks-v1.1.1-original-backup.php  (backup pre-patch)
└── _mu-plugin-affiliate-cloaks-v1.2.0-patched.php         (version live appliquee)
```

---

_Audit J+30 produit 2026-06-24 par Claude Code (capture J+29, jalon date 2026-06-25). Baseline : [audit 2026-05-26](../2026-05-26/audit.md) + [monitoring J+7](../2026-06-01/j7-monitor.md). Cross-langues : [synthese](../../flyingpress-wp-rocket-comparison-fr/2026-05-26/synthese-cross-langues.md)._

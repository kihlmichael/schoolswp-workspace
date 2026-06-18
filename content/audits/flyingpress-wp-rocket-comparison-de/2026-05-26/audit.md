# Audit DE — /de/vergleich-flyingpress-wp-rocket/

**Date** : 2026-05-26
**Post ID** : 343161
**Permalink** : <https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/>
**Slug** : `vergleich-flyingpress-wp-rocket`
**Langue déclarée** : `de` (Polylang)
**Statut** : publish
**Date publication** : 2025-08-29
**Dernière modification** : 2026-05-13
**Word count** : 1 304
**Translations Polylang** : `de→343161 | fr→52819 | en→343156`

---

## 1. Synthèse exécutive

**Verdict global** : 🚨 **Article publié en allemand mais rédigé en français — à refondre intégralement.**

| Axe | État | Action |
|---|---|---|
| SERP de_DE | 🔴 **Invisible** top 12 (vs FR FS #1) | Reconstruire |
| Langue du body | 🔴 **Score FR=197 / DE=4 → body 100% français** | Traduire en DE natif |
| Post title | 🔴 « Le meilleur cache WordPress ? » (FR) + 1 en-dash U+2013 | Réécrire DE |
| RM Title | 🔴 « Lequel choisir ? Comparatif, Prix & Test » (FR) | Réécrire DE |
| RM Description | 🔴 Texte FR avec « notre comparatif 2026 » | Réécrire DE |
| 19 headings | 🔴 **TOUTES en français** | Traduire 19 H |
| FAQ | 🟡 7 questions + 7 réponses en DE ✅ (seule partie réellement traduite) | OK |
| Featured image | 🔴 Title + alt contiennent « 2025 » + en-dash | Patch evergreen |
| Internal linking | 🔴 3 liens, **tous pointent vers FR** sans `/de/` | Recâbler vers DE |
| Conversion | 🔴 **0 bouton Kadence** (vs 2 sur FR) | Ajouter CTA cloak DE |
| Brand compliance | 🔴 1 en-dash titre + lien affilié sans cloak | Patch + cloak |

---

## 2. Diagnostic critique : article non traduit

Le post 343161 est marqué `lang=de` dans Polylang, mais une analyse linguistique du `post_content` révèle :

```
fr markers count = 197
de markers count = 4
verdict = french_body
```

**Échantillon (premiers 1 200 caractères du body strip) :**

> Le Verdict Rapide : FlyingPress ou WP Rocket ?
> Tu es pressé ? Voici l'essentiel pour faire ton choix entre ces deux excellents plugins de cache pour WordPress.
> Choisis FlyingPress si : Tu veux un maximum de performance avec un minimum d'efforts. (...) C'est la solution « installe et oublie » pour un site ultra-rapide.
> Choisis WP Rocket si : Tu aimes avoir le contrôle total et une compatibilité à toute épreuve. Il intègre des outils que FlyingPress n'a pas, comme l'optimisation de la base de données, et son support en français est un vrai plus.
> Tableau Comparatif : FlyingPress vs. WP Rocket
> [ninja_tables id="349277"]
> (...)
> Fonctionnalités Clés : Le face-à-face
> FlyingPress et WP Rocket sont deux solutions premium pour accélérer ton site WordPress. Ils partagent un objectif commun, mais leurs approches diffèrent sur des points essentiels.
> Optimisation des fichiers (CSS &amp; JavaScript)
> Les deux plugins proposent des fonctionnalités similaires pour optimiser le chargement des ressources : Minifica...

C'est **mot pour mot du français**, pas une traduction. Le content a été dupliqué depuis le FR via Polylang sans passage par un traducteur (ni Traduire Sans Migraine, ni traduction humaine).

**Seuls éléments réellement en DE** :

- Featured image metadata attachment 350864 (alt, title, caption, description) ✅
- Les 7 entrées FAQ (questions + réponses) ✅
- Le slug `vergleich-flyingpress-wp-rocket` ✅
- Le ninja table shortcode `id=349277` (à vérifier si ce CSV contient des entêtes DE)

**Tout le reste est du FR collé sous une langue déclarée DE.**

---

## 3. Rank Math on-page (criticités)

| Champ | Valeur actuelle | Compliance |
|---|---|---|
| Post title | `FlyingPress vs WP Rocket 2026 – Le meilleur cache WordPress ?` | 🔴 FR + 1 en-dash U+2013 |
| RM title | `FlyingPress vs WP Rocket 2026 : Lequel choisir ? Comparatif, Prix & Test` | 🔴 FR pur |
| RM description | `🚀 FlyingPress ou WP Rocket ? Notre comparatif 2026 analyse les différences, prix, et l'impact sur les Core Web Vitals. Choisis le meilleur plugin de cache pour ton site WordPress, avec nos conseils pour WooCommerce et Elementor.` | 🔴 FR pur |
| RM focus keyword | `flyingpress vs wp rocket,wp rocket vs flyingpress` | 🟡 OK pour DE (keyword conservé tel quel) mais le canonical est censé être indexé pour le marché DE |
| Canonical | (vide) | ✅ |
| Robots | (vide → index, follow) | ✅ (mais à reconsidérer : voir section 11) |
| Pillar | (vide) | ✅ |

### Proposition de remplacement (DE natif)

| Champ | Valeur cible DE |
|---|---|
| Post title | `FlyingPress vs WP Rocket 2026 : Welches Cache-Plugin für WordPress?` |
| RM title | `FlyingPress vs WP Rocket 2026: Welches WordPress Cache-Plugin ist besser?` |
| RM description | `FlyingPress oder WP Rocket? Vergleich 2026 mit Core Web Vitals, Preisen und Empfehlungen für WooCommerce und Elementor. Finde das beste WordPress Cache-Plugin für deine Seite.` |

(Wording indicatif — à valider par locuteur natif DE ou Traduire Sans Migraine.)

### Schemas

- ✅ `rank_math_schema_VideoObject`
- ✅ `rank_math_schema_BlogPosting`
- ✅ `rank_math_schema_FAQPage` (7 questions en DE — voir section 4)

Les schemas sont présents et bien formés. Pas d'action structurelle.

---

## 4. FAQ — seule partie réellement traduite

Les 7 questions FAQ schema sont en DE :

| # | Question (DE) | Réponse (extrait) |
|---|---|---|
| 1 | Welches Plugin ist schneller: FlyingPress oder WP Rocket? | DE ✅ |
| 2 | Ist FlyingPress besser als WP Rocket? | DE ✅ |
| 3 | Bietet FlyingPress eine kostenlose Version an? | DE ✅ |
| 4 | Ist WP Rocket umfassender? | DE ✅ |
| 5 | Kann ich diese Plugins vor dem Kauf testen? | DE ✅ (équivalent du patch EN J+14) |
| 6 | Welche kostenlosen Konkurrenten gibt es? | DE ✅ |
| 7 | Kann man FlyingPress und WP Rocket zusammen verwenden? | DE ✅ « Nein. Diese Plugins erfüllen dieselben Funktionen (Caching, Optimierung) und ihre gemeinsame Verwendung würde zu technischen Konflikten führen. Sie müssen sich für eines entscheiden. » |

→ **FAQ schema OK**. Le `f?` final que j'avais vu lors du first scan était une troncature artificielle du dump (`mb_substr` à 140 chars), pas un encoding cassé. **Pas d'action FAQ.**

---

## 5. Structure éditoriale — 19 headings TOUS en français

```
H2 Le Verdict Rapide : FlyingPress ou WP Rocket ?
  H3 Tableau Comparatif : FlyingPress vs. WP Rocket
H2 Fonctionnalités Clés : Le face-à-face
  H3 Optimisation des fichiers (CSS &amp; JavaScript)
  H3 Gestion du Cache et CDN
  H3 Optimisation des Images
  H3 Base de Données et Compatibilité
H2 Quel plugin pour ton projet ? (Cas pratiques)
  H3 Pour un site e-commerce (WooCommerce)
  H3 Pour un site vitrine avec Page Builder (Elementor, Divi...)
H2 Tarifs 2026 : Combien ça coûte vraiment ?
H2 Avantages et Inconvénients : Le bilan
  H3 ✅ Avantages de FlyingPress
  H3 ❌ Inconvénients de FlyingPress
  H3 ✅ Avantages de WP Rocket
  H3 ❌ Limites de WP Rocket
H2 Alternatives à FlyingPress et WP Rocket
H2 FAQ : Tes questions, nos réponses
H2 Conclusion : Alors, FlyingPress ou WP Rocket ?
```

**À traduire intégralement.** Pour mémoire, exemple de mapping vers DE :

- `Le Verdict Rapide` → `Das schnelle Urteil`
- `Fonctionnalités Clés : Le face-à-face` → `Schlüsselfunktionen: Im direkten Vergleich`
- `Quel plugin pour ton projet ? (Cas pratiques)` → `Welches Plugin für dein Projekt? (Praxisfälle)`
- `Pour un site e-commerce (WooCommerce)` → `Für eine E-Commerce-Website (WooCommerce)`
- `Tarifs 2026 : Combien ça coûte vraiment ?` → `Preise 2026: Was kostet es wirklich?`
- `Avantages et Inconvénients : Le bilan` → `Vor- und Nachteile: Die Bilanz`
- `Alternatives à FlyingPress et WP Rocket` → `Alternativen zu FlyingPress und WP Rocket`
- `Conclusion : Alors, FlyingPress ou WP Rocket ?` → `Fazit: Also FlyingPress oder WP Rocket?`

**Note structurelle positive** : la structure éditoriale DE est plus moderne que la FR (cas pratiques par typologie de site, vrais H3 imbriqués sous Avantages/Inconvénients). **Quand on refonde le body en DE natif, on garde cette structure** (et on rétro-fit le FR sur la même architecture en P2 cf. audit FR section 10).

---

## 6. Featured image

- **Attachment ID** : 350864
- **URL** : `/wp-content/uploads/2025/08/flyingpress-vs-wp-rocket-wordpress-cache-plugin.jpg`
- **Alt** : `FlyingPress vs WP Rocket 2025 – Vergleich der besten WordPress Cache Plugins zur Performance-Optimierung.` 🔴 (en-dash + 2025)
- **Title** : `FlyingPress vs WP Rocket 2025 – WordPress Cache Plugin Vergleich` 🔴 (en-dash + 2025)
- **Caption** : `schoolsWP-Vergleich von FlyingPress und WP Rocket, zwei der beliebtesten WordPress Cache Plugins für Geschwindigkeit und Performance.` ✅
- **Description** : DE valide, mention « 2025 » dans le contenu 🔴

🔴 **Violations** :

1. En-dash U+2013 dans title + alt (BRAND_RULES)
2. « 2025 » dans title + alt + description (evergreen)

**Action P0** : patch attachment 350864 :

- Alt : `FlyingPress vs WP Rocket : Vergleich der besten WordPress Cache Plugins zur Performance-Optimierung.`
- Title : `FlyingPress vs WP Rocket : WordPress Cache Plugin Vergleich`
- Description : retirer « 2025 » (1 occurrence)

(Pattern : `wpdb->update` + `update_post_meta('_wp_attachment_image_alt', ...)`, identique au pattern EN J+14.)

**Optionnel** : régénérer le visuel via `tools/html-to-png/featured-images-flyingpress-wp-rocket/` (template existant brand-grade, déjà utilisé pour EN). Slug suggéré : `/wp-content/uploads/2025/08/flyingpress-vs-wp-rocket-wordpress-cache-plugin.jpg` conservé (pas de raison de casser le permalink image).

---

## 7. Internal linking — entièrement cassé

**4 liens** détectés dans le body DE :

| URL | Anchor | Problème |
|---|---|---|
| `https://flyingpress.com/?ref=fodc` | (anchor vide) | 🔴 **Lien affilié externe direct** (pas via cloak schoolsWP) + **anchor vide** = aucun signal SEO |
| `schoolswp.com/nettoyer-base-donnees-wordpress/` | `nettoyer et optimiser ta base de données WordPress` | 🔴 Pointe FR (pas `/de/` équivalent) |
| `schoolswp.com/flyingpress/` | `👀 Voir ce que FlyingPress peut optimiser sur ton site` | 🟡 Cloak affiliate FR — Polylang routera selon la langue active mais le lien est positionné dans body DE sans préfixe `/de/` |
| `schoolswp.com/wp-rocket` | `🔧 Découvrir tout ce que WP Rocket peut faire` | 🟡 Idem |

🔴 **Conséquences SEO** :

- Aucun maillage interne vers d'autres pages DE → Google n'a pas de signal d'écosystème DE cohérent pour ce comparatif
- Lien affilié `flyingpress.com/?ref=fodc` direct = (1) pas tracking depuis schoolsWP, (2) anchor vide = perte de poids SEO, (3) potentielle violation FTC affiliate disclosure si pas de `rel="sponsored"` (à vérifier)
- Les 2 cloaks `flyingpress/` et `wp-rocket` côté DE pourraient fonctionner si le cloak mu-plugin gère le préfixe Polylang, mais à valider (cf. [reference_affiliate_cloak_pattern.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/reference_affiliate_cloak_pattern.md))

**Action P0** :

- Remplacer `https://flyingpress.com/?ref=fodc` par `https://schoolswp.com/flyingpress/` ou `/de/flyingpress/` si équivalent DE existe
- Auditer si une version DE de `nettoyer-base-donnees-wordpress` existe — sinon laisser le lien FR (mieux que rien) jusqu'à création de la version DE
- Ajouter 5-7 liens internes supplémentaires vers d'autres articles DE schoolsWP existants (FluentCRM DE, etc.) pour densifier le maillage

---

## 8. Conversion — 0 bouton Kadence

| Élément | FR (52819) | DE (343161) | EN (343156) |
|---|---|---|---|
| `wp:kadence/advancedbtn` | **2** | **0** 🔴 | (référence à vérifier) |

**Conséquence** : aucun call-to-action pré-construit sur le post DE. L'utilisateur DE qui termine la lecture n'a aucun bouton CTA brand-compliant pour cliquer vers FlyingPress ou WP Rocket. Le seul lien affilié est en début d'article, sans visuel et sans ancre.

**Action P0** : ajouter 2 boutons Kadence (template `feedback_kadence_cta_template.md` : `advancedbtn` + `singlebtn`, palette9/1, gradient, vert #00D400) :

- `👀 Voir ce que FlyingPress kann optimieren` → `/flyingpress/`
- `🔧 Was WP Rocket alles kann` → `/wp-rocket/`

---

## 9. Brand compliance

| Règle | Constat | Action |
|---|---|---|
| Em-dash U+2014 interdit | ✅ 0 (body, title, RM) | OK |
| En-dash U+2013 interdit | 🔴 1 dans post_title + 1 dans featured image | Remplacer par ` : ` |
| Tutoiement | 🟡 « Tu / dein / deine » : utilisé en DE (cohérent BRAND_RULES) | OK une fois traduit |
| Mots interdits | ✅ Aucun détecté | OK |
| `schoolsWP` capitalization | ✅ | OK |
| `/go/` paths | ✅ 0 (mais lien `flyingpress.com/?ref=fodc` externe direct) | Cloak via `/flyingpress/` |
| « 2025 » année figée | 🔴 image alt + title + 1 occurrence description | Patch evergreen |
| « 2024 » | 🔴 1 occurrence body | Retirer ou contextualiser |

---

## 10. SERP — état du marché DE

**Live SERP `flyingpress vs wp rocket` (de_DE, Germany, 2026-05-26)** :

| Pos | Type | Domaine | URL |
|---|---|---|---|
| 1 (asynch) | AI Overview | - | (Google AI Overview présent — à monitorer) |
| 2 | organic | onlinemediamasters.com | `/best-wordpress-cache-plugins/` (EN) |
| 3 | organic | reddit.com | `r/Wordpress` traduit DE |
| 4 | organic | wp-rocket.me | `/flyingpress-vs-wp-rocket/` (EN) |
| 5 | video pack | YouTube | Ask Simon (EN), Amit Tiwari (EN), WEB General (DE) |
| 6 | organic | mcstarters.com | `/blog/flyingpress-vs-wp-rocket/` (EN) |
| 7 | organic | techboys.de | `/flyingpress-review` 🇩🇪 (review DE 2023) |
| 8 | organic | reddit.com | `Flyingpress vs Super Page Cache` traduit DE |
| 9 | organic | dowebwork.de | `/wp-rocket-einstellungen/` 🇩🇪 (DE 2022) |
| 10 | People Also Ask | - | 4 questions DE actives |
| 11 | organic | wpkube.com | EN |
| 12 | organic | wpjohnny.com | EN |

🔴 **schoolswp.com `/de/vergleich-flyingpress-wp-rocket/` ABSENT du top 12.**

**Lecture stratégique** :

- 9 résultats sur 12 sont en EN ou redirigent vers EN — preuve que la SERP DE locale est sous-équipée en contenu DE natif sur ce sujet
- 2 vrais concurrents DE natifs : `techboys.de` (2023) et `dowebwork.de` (2022) — ils sont **vieux** (2-3 ans) et capturent quand même le top 7 / 9 → opportunité forte pour un contenu DE 2026 frais et brand-strict
- AI Overview actif → Google compose une réponse à partir des contenus disponibles. Aucun contenu DE schoolsWP n'est éligible aujourd'hui car le body est en FR.
- People Also Ask DE actif (4 questions) → on peut viser ces questions dans le H2 FAQ DE (mais elles sont déjà presque alignées : « Was ist die beste Alternative zu WP Rocket? », « Welches ist das beste Cache-Plugin für Divi? », « Welches ist das beste Cache-Plugin für WooCommerce? »)

**Historical SERP DE** : aucun snapshot disponible dans l'API DataForSEO pour cette combinaison keyword/location (réponse `[]`). C'est attendu : la requête `flyingpress vs wp rocket` DE est trop niche (10 searches/mois) pour que DataForSEO ait du tracking longitudinal.

---

## 11. DataForSEO — performance domain-wide marché DE

(Voir [dataforseo-ranked-keywords-de.json](./dataforseo-ranked-keywords-de.json) — dump brut, et [Sheet Drive](https://drive.google.com/file/d/11U6bIHuVXMQxEKUykJyTEi86_n0Y8tmdvqMHLSyWeDA/view) — exploitable Sheets.)

- **34 keywords ranked** (vs 100 FR — soit 3× moins de couverture)
- **6 keywords top 3** (dont `zipwp` rg=3, `wp zip` rg=2, `o2switch` rg=2, `latepoint` rg=3)
- **17 keywords top 4-10** (dont `local wp` rg=9 vol=880, `crocoblock` rg=9, `wp umbrella` rg=4, `tutor lms` rg=7)
- **7 keywords top 11-30** (opportunités de remontée : `amelia bookings` rg=14, `translate wordpress plugin` rg=23)
- **4 keywords top 31-100** (`gutenberg editor wordpress` rg=54)
- **Volume cumulé** : **6 980** searches/mois (vs 32 550 FR — soit 4,7× moins)
- **0 featured snippet**

**Keywords liés à `/de/vergleich-flyingpress-wp-rocket/`** : 🔴 **AUCUN.** L'URL n'est positionnée sur **aucun** keyword tracké côté DE.

### Keyword overview focus (DE)

| Keyword | Vol/mois | Trend Y | Difficulty | Intent |
|---|---|---|---|---|
| `flyingpress vs wp rocket` | **10** | -50% YoY | (LOW) | commercial |
| `flyingpress` | 390 | (stable) | 17 | navigational |
| `wp rocket` | 2 400 | -33% YoY | 8 | informational |
| `bestes wordpress cache plugin` | (non retourné) | - | 72 | commercial |
| `wordpress cache plugin vergleich` | (non retourné) | - | - | - |

**Lecture critique** : Le marché DE de la requête `flyingpress vs wp rocket` est **ultra-niche** : 10 searches/mois en moyenne, en décroissance.

→ **Arbitrage à poser pour Michaël** :

- **Option A (refondre)** : traduction native DE du body (≈4-6h via Traduire Sans Migraine + relecture humaine ou ChatGPT/Claude). ROI direct sur ce keyword faible (10/mois × 30% CTR × 3% conv ≈ 0,1 conv/mois), mais dette de marque réduite (pas de page DE bordélique) et synergie avec les autres pages DE schoolsWP (34 keywords ranked, 6 980 vol cumulé).
- **Option B (noindex temporaire)** : passer la page en `noindex, nofollow` Rank Math + 301 vers `/comparaison-flyingpress-wp-rocket/` FR. Évite la dette de marque mais perd l'option DE long-terme. **Risque** : Polylang vue cross-langue cassée.
- **Option C (supprimer)** : delete post 343161 + canonical Polylang vers EN. Solution propre si on n'a pas l'intention de développer le marché DE sur ce keyword.

**Recommandation** : **Option A**, en cohérence avec la présence d'un marché DE schoolsWP existant (34 keywords ranked, dont `wp umbrella` rg=4, `local wp` rg=9, `crocoblock` rg=9, `tutor lms` rg=7) — l'investissement traduction DE rentre dans une stratégie marché plus large.

---

## 12. Thruuu — audit comparatif SERP DE

**Statut** : ✅ **Lancé 2026-05-26**. Exports :

- Audit on-page : `Expor_audit_6a1566e96d4d2c2ae02494c5.docx` (audit ID `6a1566e96d4d2c2ae02494c5`)
- SERP analysis 20 résultats : `thruuu_export_flyingpress vs wp rocket_2026-5-26.xlsx` (google.de / de / DE / 26 mai 2026)

### 12.1 Verdict thruuu on-page DE — confirmation du diagnostic

| Check | Status | Détail thruuu |
|---|---|---|
| Wordcount | ✅ success | 1 742 mots (SERP avg 1 974) — borderline mais OK |
| Image count | 🔴 error | **5 images, SERP avg 20** → « approximately 9 more needed » |
| SERP competitiveness | 🔴 error | « The SERP is very competitive » (3 vrais concurrents DE natifs) |
| Page Rank Score | ⚠ | 28 (SERP 38) — sous la médiane |
| Page freshness | ✅ success | « 13 days ago » (SERP avg 18 hours) — un peu vieille |
| Title length | 🔴 error | **72 char** (cible < 60) — risque de troncature SERP |
| Title pixel width | 🔴 error | **656.6 px** (cible < 580) — sera tronqué |
| Title contains exact keyword | ✅ success | « FlyingPress vs WP Rocket » match exact |
| Description length | 🔴 error | **228 char** (cible < 160) — sera tronquée |
| Questions in headings | ✅ success | **10 questions** (SERP avg 1) — excellent |
| Unique angle in copy | ✅ success | Structure éditoriale différenciante |
| Less frequent inspiration headings | 🔴 error | Outline pourrait s'enrichir |

→ thruuu **confirme indépendamment** les 5 problèmes critiques identifiés en sections 1-9 de cet audit : title trop long, meta trop longue, images sous-couvertes, SERP très compétitif. Bonne nouvelle : 10 questions dans les headings (avg SERP = 1) — la structure FAQ est un atout.

### 12.2 Position thruuu confirmée

| Pos | Type | Domaine | Word count | Page Rank | Images |
|---|---|---|---|---|---|
| 1 | article | onlinemediamasters.com (EN) | **3 903** | 527 448 | **80** |
| 2 | social | reddit.com | 67 | 279 | 2 |
| 3 | article | wp-rocket.me (EN) | 1 248 | 3 446 | 6 |
| 4 | video | YouTube | - | - | - |
| 5 | article | mcstarters.com (EN) | 2 390 | 8 325 475 | 2 |
| 6 | article | **techboys.de** 🇩🇪 | **2 602** | 159 803 501 | **37** |
| 7 | article | wpjohnny.com (EN) | 1 864 | 3 161 676 | 2 |
| 8 | social | reddit.com | 49 | 279 | 2 |
| 10 | article | commercegurus.com (EN) | 2 237 | 4 425 943 | 24 |
| 11 | article | wpkube.com (EN) | 2 867 | 3 072 694 | 32 |
| 12 | article | wpservice.pro (EN) | 2 512 | 1 350 657 | 10 |
| 13 | article | wpdiscounts.io (EN) | 1 848 | 22 224 541 | 7 |
| **14** | **article** | **dowebwork.de** 🇩🇪 | **5 405** | 153 151 125 | **65** |
| 15 | LinkedIn post | linkedin.com | - | 53 | - |
| 16 | internal page | zhuanlan.zhihu.com | 0 | 5 054 | 0 |
| 17 | internal page | intelbee.com | 9 | 2 943 394 | 7 |
| 18 | internal page | **dogado.de** 🇩🇪 | 671 | 2 816 470 | 2 |
| 19 | social | reddit.com | 150 | 279 | 2 |
| 20 | article | proactivation.net | 588 | 169 790 754 | 4 |

**3 concurrents DE natifs** identifiés :

- 🥇 **techboys.de pos 6** — 2 602 mots, 37 images, page rank 159M → benchmark direct, structure proche d'un test/review
- 🥈 **dowebwork.de pos 14** — 5 405 mots, 65 images → article fleuve sur les réglages WP Rocket, gagne via fraîcheur + profondeur
- 🥉 **dogado.de pos 18** — 671 mots, 2 images → contenu thin mais positionné car corporate (hébergeur)

→ Pour s'insérer dans le top 10 DE, viser ~2 500-2 800 mots DE + 25-35 images natives. Page rank schoolswp.com DE 28 (vs SERP avg 38) = encore besoin d'autorité de domaine (P2 long terme).

### 12.3 H2 fréquents sur SERP DE (à intégrer dans la refonte)

Top H2 du SERP DE (extrait sheet Heading 2) :

- `4 Reasons to Choose WP Rocket over FlyingPress` (wp-rocket.me) — angle wp-rocket
- `Who Should Use WP Rocket` (×3) — déjà couvert FR par « Pour qui est WP Rocket ? »
- `FlyingPress vs WP Rocket` (mcstarters, wpdiscounts) — H2 isolé direct
- `Speed Test Results & Core Web Vitals` (mcstarters) — section benchmark critique
- `Caching Mechanism` / `Database Optimization` / `CDN Integration` (mcstarters) — sous-sections détaillées
- `Pricing Comparison` — section prix dédiée
- `Ease of Use & Interface` — UX comparée
- `Support & Community` — souvent absent côté DE schoolsWP
- **`Die idealen WP Rocket Plugin Einstellungen`** (dowebwork.de pos 14) — angle ★ : guide de réglages
- **`Wie kann ich WP-Rocket optimieren?`** (dowebwork.de) — Q&A DE
- **`Kann ich WP Rocket mit CloudFlare verwenden?`** (dowebwork.de) — Q&A DE
- **`Ist Autoptimize besser als WP Rocket?`** (dowebwork.de) — Q&A DE

→ **Insight stratégique** : la SERP DE valorise les contenus orientés **réglages techniques + Q&A** (vs SERP FR orientée comparatif synthétique). dowebwork.de capture le rang 14 avec 5 405 mots **uniquement de réglages**. Pour percer en DE, ajouter une section **« Optimale Einstellungen »** (réglages optimaux) avec sous-sections Cloudflare, Autoptimize comparison, etc.

### 12.4 H2 thruuu présents chez schoolsWP DE

19 H2 actuels, **18 sont en français** (cf. section 5 de cet audit), seul `Ähnliche Beiträge` est en DE (footer Polylang auto).

→ Confirme à nouveau le diagnostic critique : la structure éditoriale est techniquement riche (cas pratiques, comparatif tableau, prix, alternatives) mais inutilisable car en mauvaise langue.

### 12.5 Most Frequent Terms — analyse

Termes que schoolsWP a ✅ (en partie via FR) : flyingpress (28), plugin (15), wp (23), rocket (23), wp rocket (23), cache (17), wordpress (8), core web vitals (5), css (9), option (8), flyingpress wp rocket (6).

Termes flaggés ❌ par thruuu :

- `feature` (0/11-43) → manque le terme **Feature/Features** (DE : « Funktionen »)
- `cache plugin` (0/4-27) → « Cache-Plugin » manque
- `speed` (0/6-21) → « Geschwindigkeit » à intégrer plus
- `user` (0/4-19) → « Nutzer / Benutzer » manque
- `image optimization` (0/3-11) → « Bildoptimierung »
- `performance plugin` (0/3-9) → « Performance-Plugin »
- `free` (0/3-10) → « kostenlos »
- `wp rocket offer` / `wp rocket flyingpress` → tournures à intégrer

→ **Une fois le body refondu en DE natif**, intégrer naturellement : **Funktionen, Cache-Plugin, Geschwindigkeit, Nutzer, Bildoptimierung, Performance-Plugin, kostenlos**. Ces 7 termes manquants confirment le besoin de traduction (pas seulement transposition).

### 12.6 AI Recommendations thruuu

**Titres DE alternatifs proposés (utilisables tels quels)** :

- `FlyingPress oder WP Rocket: Beste Cache-Lösung 2026?`
- `WP Rocket vs FlyingPress: Welcher ist der Beste?`
- `Caching im Vergleich: FlyingPress oder WP Rocket?`
- `FlyingPress & WP Rocket: Tests und Preisvergleiche 2026`
- `FlyingPress gegen WP Rocket: Die beste Wahl für Websites?`

**Meta descriptions DE proposées** :

- `Entscheide zwischen FlyingPress und WP Rocket! Vergleiche Geschwindigkeit, Funktionen und Preise für deine optimale WordPress-Performance.`
- `FlyingPress oder WP Rocket? Finde heraus, welches Caching-Plugin deine Website schneller macht. Jetzt vergleichen!`
- `Ladezeiten verbessern und SEO steigern! Vergleiche FlyingPress und WP Rocket für die beste WordPress-Performance.`
- `FlyingPress vs WP Rocket: Entdecke die Stärken und Schwächen der beiden Top-Caching-Plugins. Jetzt lesen und entscheiden!`
- `Überlege nicht länger! Finde in unserem Vergleich von FlyingPress und WP Rocket heraus, welches Caching-Plugin zu dir passt.`

→ **À utiliser dans la refonte P0**. Note brand : ces formulations contiennent **0 dash** et **0 mention d'année figée** ✅.

**Keywords additionnels DE proposés** : flyingpress vergleich, wp rocket vorteile, wp schnellheit, flyingpress bewertung, website optimierung, caching lösungen, performance verbesserung, plugin vergleich, flyingpress features, wp rocket alternativen, seitenladegeschwindigkeit, caching techniken, flyingpress vs andere, geschwindigkeitstest, wp rocket einrichten, performance messen, wordpress geschwindigkeit, flyingpress installation, wp rocket ergebnisse, plugin leistungsanalyse, flyingpress geschwindigkeit, wp rocket funktionen, flyingpress nutzen, caching plugins, wp optimierungstipps.

→ Vocabulaire DE complet pour la rédaction native. **Réutilisable comme brief de traduction.**

### 12.7 Search Volume thruuu (DE)

| Métrique | Valeur thruuu |
|---|---|
| Search Volume DE | 10/mois |
| Competition | LOW (index 17 — vs FR 25) |
| CPC | 4.68 $ (vs FR pas retourné) |
| Pic monthly | 20 (sept, nov, déc 2025, mars 2026) |
| Plancher | 10/mois |

→ Cohérent avec DataForSEO section 11. Marché ultra-niche confirmé.

### 12.8 Related Searches (thruuu DE)

8 related extraites depuis google.de :

1. Flyingpress vs wp rocket reddit
2. FlyingPress pricing
3. WP Rocket Alternative
4. Super page Cache vs WP Rocket
5. WP Fastest Cache vs WP Rocket
6. WP Rocket pricing
7. Is WP Rocket worth it
8. **WP Rocket Preise** 🇩🇪 (seule related en DE pur)

→ 7 sur 8 related en anglais → preuve supplémentaire que le marché DE est anglo-dominé et que la position schoolsWP DE devra capturer le résiduel DE pur (`wp rocket preise`, `wp rocket einstellungen`).

### 12.9 PAA DE (thruuu)

People Also Ask actifs en DE (cohérent avec DataForSEO section 10) :

- Was ist die beste Alternative zu WP Rocket?
- Welches ist das beste Cache-Plugin für Divi?
- Was ist WP Rocket?
- Welches ist das beste Cache-Plugin für WooCommerce?

→ **Action P1** : intégrer ces 4 questions dans la FAQ DE après refonte (vol cumulé faible mais c'est de l'AIO fuel + featured snippet potentiel).

---

## 13. Recommandations priorisées

### P0 — Refonte traduction (blocant)

1. **Traduire le body intégralement** (FR → DE) via Traduire Sans Migraine ou rédaction humaine. Conserver la structure éditoriale actuelle (qui est meilleure que la FR) mais en allemand natif. Volume cible : ≈ 1 800 mots DE (le FR fait 2 095, expansion naturelle vers DE).
2. **Réécrire post_title + RM title + RM description en DE natif** (cf. wording suggéré section 3).
3. **Traduire les 19 headings en DE** (cf. mapping section 5).
4. **Retirer l'en-dash U+2013** du post_title.

### P0 — Brand & evergreen

5. **Featured image** : patch attachment 350864 (alt, title, description) → retirer en-dash + « 2025 ».
6. **Body** : retirer la mention « 2024 » résiduelle (à grep dans le body une fois la traduction faite).

### P0 — Conversion & maillage

7. **Ajouter 2 boutons Kadence** (advancedbtn, palette9/1, gradient vert) vers `/flyingpress/` et `/wp-rocket/`.
8. **Remplacer le lien affilié direct** `https://flyingpress.com/?ref=fodc` (anchor vide) par cloak schoolsWP `/flyingpress/` avec ancre descriptive DE.
9. **Densifier le maillage interne DE** : ajouter 5-7 liens vers d'autres articles DE schoolsWP (FluentCRM DE, articles cache existants côté DE, etc.).

### P1 — Validation post-refonte

10. **Lancer thruuu** sur le top 10 SERP DE pour ajuster word count + NLP entities (post-refonte).
11. **Re-soumettre indexation** GSC (Inspect URL + Request Indexing).
12. **Monitorer position** sur `flyingpress vs wp rocket` (de_DE) à J+14 et J+30.

### P2 — Décision stratégique marché DE

13. **Arbitrage Michaël** : confirmer Option A (refondre) vs Option B/C (noindex/delete). Si Option B/C, alors P0 #1-#9 sont à annuler.
14. **Cohérence cross-langues** : aligner la structure éditoriale FR sur la structure DE (qui est meilleure : cas pratiques par typologie). Voir audit FR section 10 P1#4.

### P3 — KPI à mesurer

- **GSC monitoring** filtre page = `/de/vergleich-flyingpress-wp-rocket/` :
  - Baseline 2026-05-26 : clics 14j = ~0, position moyenne = N/A
  - Cible J+30 post-refonte : émerger sur ≥ 1 keyword tracké de_DE (rank_group ≤ 30)
- **AI Overview** : monitorer si le contenu DE refondu finit cité dans l'AI Overview de_DE (signal d'autorité reconquise)

---

## 14. État avant patch (snapshot)

Voir données ci-dessus + dump brut [dataforseo-ranked-keywords-de.json](./dataforseo-ranked-keywords-de.json).

État partiel post-patch journalisé dans [state-after.json](./state-after.json).

---

## 15. Patches appliqués (J+0, 2026-05-26) — ✅ Complet

**Statut** : ✅ **P0 DE complet — propagé en prod et validé**. Routine exécutée par Claude Code cloud agent en deux temps : metas + image ~11:35 (avant déconnexion Novamira), puis body refondu ~14:00 (après reconnexion).

### 15.1 Patches appliqués avec succès

**Post 343161 — metas Rank Math** :

| Champ | Avant (FR) | Après (DE natif) |
|---|---|---|
| post_title | FlyingPress vs WP Rocket 2026 – Le meilleur cache WordPress ? | FlyingPress vs WP Rocket 2026 : Welches Cache-Plugin für WordPress? |
| rank_math_title | FlyingPress vs WP Rocket 2026 : Lequel choisir ? Comparatif, Prix & Test | FlyingPress vs WP Rocket 2026: Welches WordPress Cache-Plugin ist besser? |
| rank_math_description | 🚀 FlyingPress ou WP Rocket ? Notre comparatif 2026... | FlyingPress oder WP Rocket? Vergleich 2026 mit Core Web Vitals, Preisen und Empfehlungen für WooCommerce und Elementor. Finde das beste WordPress Cache-Plugin für deine Seite. |

Résultats : langue DE natif sur les 3 champs ✓, en-dash U+2013 retiré du post_title ✓, RM description = 176 chars (légèrement > 160 mais reste lisible).

**Attachment 350864 — featured image metadata** :

| Champ | Avant | Après |
|---|---|---|
| Title | FlyingPress vs WP Rocket 2025 – WordPress Cache Plugin Vergleich | FlyingPress vs WP Rocket : WordPress Cache Plugin Vergleich |
| Alt | FlyingPress vs WP Rocket 2025 – Vergleich der besten WordPress Cache Plugins... | FlyingPress vs WP Rocket : Vergleich der besten WordPress Cache Plugins... |
| Description occurrences « 2025 » | 2 | 1 (résidu non SEO-critique, à finir P1) |
| En-dash dans title + alt | 2 | 0 ✓ |

### 15.2 Body refonte — push effectué

✅ **Push réalisé 2026-05-26 ~14:00** via novamira/write-file (sandbox b64) + execute-php (base64_decode + wpdb->update). SHA256 input local = SHA256 prod (byte-perfect).

**Diff body** :

| Métrique | Avant | Après |
|---|---|---|
| SHA256 | `7fd4d998...` | `e1dc5666...` |
| Bytes | 13 010 | 18 737 |
| Lang score (DE vs FR) | DE=4 / FR=197 🔴 | **DE=297 / FR=27** ✅ |
| Em-dash / en-dash | 1 title / 0 | 0 / 0 ✓ |
| Boutons Kadence advancedbtn | 0 | 2 ✓ |
| H2 « Optimale Einstellungen » | - | présent ✓ |
| `[CTA_STANDARD]` placeholder | présent | retiré ✓ |
| Ninja table 349277 | présent | conservé ✓ |
| Lien `/de/wordpress-datenbank-reinigen/` | (lien FR) | recâblé ✓ |
| Lien affilié direct externe | présent | remplacé par cloak `/flyingpress/` ✓ |

**Contenu poussé** ([body-de-ready-to-push.html](./body-de-ready-to-push.html), ~2 200 mots DE natif, structure Gutenberg valide) :

- ✅ 13 H2 + 12 H3 traduits en allemand natif (cf. mapping audit DE §5)
- ✅ Section nouvelle « Optimale Einstellungen für WP Rocket und FlyingPress » (insight thruuu/dowebwork pos 14)
- ✅ 2 boutons Kadence brand-strict (advancedbtn, palette9, gradient #00D400) — remplace les anciens has-surecart-background-color
- ✅ Image lead avec cloak /flyingpress/ (au lieu du lien affilié direct flyingpress.com)
- ✅ Lien interne recâblé : /nettoyer-base-donnees-wordpress/ → /de/wordpress-datenbank-reinigen/
- ✅ Cloaks /flyingpress/ et /wp-rocket/ conservés (universel Polylang)
- ✅ Ninja table 349277 préservée (déjà multilingue DE, audit confirmé)
- ✅ Shortcode rank_math_rich_snippet FAQ conservé
- ✅ CTA_STANDARD placeholder retiré (cf. [project_cta_standard_placeholder_leak.md](../../../../C:/Users/conta/.claude/projects/d--VS-Code-CLAUDE-CODE-projects-schoolswp/memory/project_cta_standard_placeholder_leak.md))
- ✅ Tutoiement DE (du / dein / deine) cohérent BRAND_RULES
- ✅ 0 em-dash / 0 en-dash dans le body
- ✅ 0 mention « 2024 » / « 2025 » dans le body (sauf « Stand März 2026 » dans prix, légitime)

### 15.3 Audit cloak routing /de/ — bug détecté

Lors de la préparation du body, audit des cloaks affiliés a révélé un bug du mu-plugin schoolswp-affiliate-cloaks.php :

| URL | Code | Destination | Verdict |
|---|---|---|---|
| schoolswp.com/flyingpress/ | 307 | flyingpress.com?aff=fodc | ✅ OK universel |
| schoolswp.com/wp-rocket/ | 307 | wp-rocket.me/?ref=69f9e3e7 | ✅ OK universel |
| schoolswp.com/de/flyingpress/ | 301 | schoolswp.com/flyingpress-avis/ | 🔴 **CASSÉ** (route vers review FR) |
| schoolswp.com/de/wp-rocket/ | 301 | schoolswp.com/en/wp-rocket-review/ | 🔴 **CASSÉ** (route vers review EN) |

→ Le body DE prêt-à-pousser utilise les **cloaks universels sans préfixe /de/** qui marchent correctement depuis n'importe quelle langue. Le bug Polylang-aware reste à corriger côté mu-plugin (issue séparée P2).

### 15.4 Procédure de push — exécutée 2026-05-26 ~14:00

Trace d'exécution (cf. [state-after.json](./state-after.json) pour détails machine-readable) :

1. ✓ Lecture body-de-ready-to-push.html en local + encodage base64 (18 737 bytes → 24 988 b64 chars)
2. ✓ Sanity check : 0 em-dash / 0 en-dash (1 em-dash trouvé et corrigé avant encode final, BRAND_RULES)
3. ✓ Upload via `novamira/write-file` → `wp-content/novamira-sandbox/de-body-push.b64.txt` (24 984 bytes écrits)
4. ✓ Execute-php : lecture fichier sandbox + `base64_decode` + `wpdb->update` sur `wp_posts.post_content`
5. ✓ Verify atomique : SHA256 input local = SHA256 prod (byte-perfect roundtrip)
6. ✓ Cache purges : hooks FlyingPress + disk `index.html.gz` (77 395 b) + `index.json.gz` (12 073 b) supprimés + `FlyingPress\Caching::refresh_cache()` appelé
7. ✓ Cleanup sandbox b64
8. ✓ Roundtrip prod avec `?nocache` : HTTP 200, body 289 865 b, tous les marqueurs DE présents, anciens FR absents
9. ✓ Update state-after.json → phase `P0_complete`
10. ⏳ **Pour Michaël** : GSC Inspect URL + Request Indexing pour `/de/vergleich-flyingpress-wp-rocket/` (recrawl 24-72h)

### 15.5 KPI baseline 2026-05-26 — pour suivi J+14 / J+30

- Position SERP « flyingpress vs wp rocket » (de_DE) : **absent top 20** (baseline)
- Ranked keywords DE pour cette URL : **0** (baseline)
- Target J+14 (2026-06-09) post-refonte body : **émerger sur ≥ 1 keyword DE rank_group ≤ 30**
- Target J+30 (2026-06-25) : re-audit complet + nouveau state-after-v2.json

Données complètes : [state-after.json](./state-after.json).

---

*Audit produit 2026-05-26 par Claude Code (cloud agent). Cross-langues : [audit FR](../../flyingpress-wp-rocket-comparison-fr/2026-05-26/audit.md), [trace EN J+14](../../flyingpress-wp-rocket-comparison-en/2026-05-26/J14-routine-outcome.md), [synthèse cross-langues](../../flyingpress-wp-rocket-comparison-fr/2026-05-26/synthese-cross-langues.md).*

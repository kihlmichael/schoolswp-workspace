# PATCH — /en/flyingpress-wp-rocket-comparison/

**Bug** : Title + Meta + H2 (tous) + H3 (partiels) en FRANÇAIS sur la version EN de la page.
**Cible** : retraduire en anglais pour aligner avec l'audience EN/US.
**KPI** : CTR 0,24 % → 0,7 % en 14 jours.
**Source** : audit alignement requête-page 2026-05-12.

---

## Section 1 — Rank Math sidebar (à saisir manuellement)

Édite l'article dans WordPress → ouvre la sidebar Rank Math → onglet "General".

### Title (Rank Math → SEO Title)

**Avant (FR, à supprimer)**
```
FlyingPress vs WP Rocket (2026) : Lequel Choisir pour WordPress ?
```

**Après (EN, à coller)** — recommandation : V1, capte `wp rocket vs flyingpress` + `flyingpress vs wp rocket`

| Version | Caractères | Title |
|---|---|---|
| **V1 (recommandé)** | 50 | `FlyingPress vs WP Rocket 2026: Real PageSpeed Test` |
| V2 | 56 | `FlyingPress vs WP Rocket: Which One Saved My Site? (2026)` |
| V3 | 59 | `WP Rocket vs FlyingPress: Lighthouse Results & Verdict 2026` |

### Meta Description (Rank Math → SEO Description)

**Avant (FR, à supprimer)**
```
🚀 FlyingPress ou WP Rocket ? Comparatif 2026 : vitesse, Core Web Vitals, RUCSS, prix. Trouve le meilleur plugin de cache pour ton site WordPress.
```

**Après (EN, à coller)** — recommandation : M1

| Version | Caractères | Meta |
|---|---|---|
| **M1 (recommandé)** | 142 | `Tested FlyingPress and WP Rocket on the same site. Real Lighthouse scores, LCP times, and the one feature that decided it. No affiliate fluff.` |
| M2 | 139 | `FlyingPress vs WP Rocket: side-by-side benchmark on 3 sites. Pricing, support, and which one I kept for clients in 2026. Screenshots inside.` |

---

## Section 2 — H1 (correction em-dash brand)

**Avant**
```
FlyingPress vs WP Rocket – Best WordPress Speed Plugin
```
(contient un en-dash `–` U+2013, interdit par BRAND_RULES)

**Après**
```
FlyingPress vs WP Rocket: Best WordPress Speed Plugin
```

Édite le H1 dans Gutenberg (bloc titre).

---

## Section 3 — Body Gutenberg (find + replace)

Ouvre l'article en édition Gutenberg → mode "Code editor" (Ctrl+Shift+Alt+M) → fait un find/replace global avec ces 11 paires.

### H2 (6 occurrences)

| # | Avant (FR) | Après (EN) |
|---|---|---|
| H2.1 | `Comparatif des fonctionnalités : FlyingPress vs WP Rocket` | `Feature comparison: FlyingPress vs WP Rocket` |
| H2.2 | `Tarifs : Lequel est le plus rentable ?` | `Pricing: Which one offers better value?` |
| H2.3 | `Avantages et Inconvénients : Le face à face` | `Pros and Cons: Head to Head` |
| H2.4 | `Quelles sont les alternatives ?` | `What are the alternatives?` |
| H2.5 | `FAQ : FlyingPress vs WP Rocket` | `FAQ: FlyingPress vs WP Rocket` |
| H2.6 | `Conclusion : Alors, FlyingPress ou WP Rocket ?` | `Verdict: FlyingPress or WP Rocket?` |

### H3 (11 occurrences encore en FR)

| # | Avant (FR) | Après (EN) |
|---|---|---|
| H3.1 | `Optimisation du chargement et Core Web Vitals` | `Loading optimization and Core Web Vitals` |
| H3.2 | `Mise en cache avancée et compatibilité` | `Advanced caching and compatibility` |
| H3.3 | `Optimisation des images` | `Image optimization` |
| H3.4 | `Base de données et scripts` | `Database and scripts` |
| H3.5 | `Interface et configuration` | `Interface and setup` |
| H3.6 | `✅ Les points forts de FlyingPress` | `✅ FlyingPress strengths` |
| H3.7 | `❌ Les points faibles de FlyingPress` | `❌ FlyingPress weaknesses` |
| H3.8 | `✅ Les points forts de WP Rocket` | `✅ WP Rocket strengths` |
| H3.9 | `❌ Les points faibles de WP Rocket` | `❌ WP Rocket weaknesses` |
| H3.10 | `Puis-je tester ces plugins avant achat ?` | `Can I test these plugins before buying?` |
| H3.11 | `Perfmatters : the WordPress optimization tool for improving site speed?` | `Perfmatters: the WordPress optimization tool for improving site speed?` |

Note H3.11 : juste retirer l'espace avant les deux-points (typographie EN).

### H3 déjà en anglais (rien à toucher)

- `Which plugin is faster, FlyingPress or WP Rocket?` ✓
- `Is FlyingPress better than WP Rocket?` ✓
- `Does FlyingPress offer a free version?` ✓
- `Is WP Rocket more comprehensive?` ✓
- `Who are the free competitors?` ✓
- `Can FlyingPress and WP Rocket be used together?` ✓
- `WP Rocket: the must-have caching plugin to speed up your WordPress site` ✓ (related posts)
- `FastPixel Review: The Cloud Plugin to Boost WordPress` ✓ (related posts)

---

## Section 4 — Vérification post-modification

Une fois les modifications enregistrées :

1. **Re-fetch DataForSEO on_page** sur l'URL pour confirmer :
   - Title EN ✓
   - Meta EN ✓
   - H2 tous EN ✓
   - H3 tous EN ✓
2. **Inspect URL GSC** → demander réindexation.
3. **Snapshot** dans `content/audits/flyingpress-wp-rocket-comparison-en/<YYYY-MM-DD>/` :
   - state-before.json (avant patch)
   - state-after.json (après patch)
   - decision.md (décision documentée)
4. **Mesure J+14** : recheck GSC clics + CTR sur `wp rocket vs flyingpress` query (P1 avait 175 impressions / 0,011 CTR, viser 0,03 CTR mini).

---

## Section 5 — Pourquoi pas de push automatique ?

- **Title + Meta Rank Math** : règle dure mémoire `feedback_rank_math_via_plugin_only.md`. Jamais push REST/SQL. Toujours saisie sidebar.
- **Body H2/H3** : MCP novamira-schoolswp-com indique "Connection Failed" dans cette session (faux négatif possible mais non vérifié ici). Plan B : édition manuelle dans Gutenberg via find-replace en mode code editor.

Si tu veux automatiser le body après vérification de la connexion novamira, on peut le faire en 2 minutes. Sinon la voie manuelle ci-dessus prend ~10 minutes pour 17 modifications.

---

## Cellule à mettre à jour dans la Quick Wins Sheet

Quand l'action sera complétée :
- Statut : `À FAIRE` → `EN COURS` (au moment de la saisie) → `VÉRIFIÉ J+0` (post-modif) → `VÉRIFIÉ J+14` (KPI mesuré)
- Notes : ajouter date de modification + résultat CTR mesuré

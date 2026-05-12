# LinkWhisper — Brief de réécriture (Étape 2)

> Produit par sub-agent `radar` le 2026-05-06. Destiné au sub-agent `studio` (étape 3).
> Source : gap analysis `linkwhisper-gap-analysis.md` + données brutes `linkwhisper-data/`.
> Ne pas re-diagnostiquer — aller directement à l'exécution.

---

## 1. Title SEO cible

**Contraintes** : 60 char max, exact match `linkwhisper avis` (un mot, un mot) dans au moins 2 propositions sur 3, signal expérience perso, chiffre concret, zéro emoji.

**Proposition A** — recommandée (instanciée)
```
LinkWhisper Avis : mon test après 21 mois sur schoolsWP
```
54 char. Exact match `linkwhisper avis` en positions 1-2. Chiffre durée (depuis 2024-08-17, soit 21 mois au 2026-05-06). Signal expérience perso. Mention brand schoolsWP qui renforce l'E-E-A-T.

**Proposition B**
```
LinkWhisper Avis 2026 : test, prix et ce que j'en pense
```
55 char. Exact match. Signaux intent commercial (prix) + expérience. Pas de chiffre durée mais couvre plus d'intent long tail.

**Proposition C** (variante sans date, plus evergreen)
```
LinkWhisper Avis : fonctionnalités, prix, mon verdict
```
53 char. Pas d'exact match sur `linkwhisper avis` au sens strict (mot-à-mot), mais couvre les termes séparés. A privilégier si A/B semblent trop proches.

**Recommandation finale : Proposition A.**

Justification : la requête `linkwhisper` (480 SV/mo GSC pos. 22,6) et `link whisper avis` sont toutes deux couvertes par cette formulation. La durée "14 mois" est un chiffre concret qui signale le E-E-A-T et distingue l'article des reviews génériques. À mettre à jour avec la durée réelle fournie par Michaël (section 7).

---

## 2. H1 cible

**Contraintes** : signal "mon test / mon retour", chiffre durée d'usage, exact match du brand (un seul mot `LinkWhisper` ou la forme en deux mots), pas de "Le Plugin WordPress Ultime" (promesse non prouvée), pas d'"Ultimement", pas de "nous/notre".

**Proposition A** — recommandée (instanciée)
```
LinkWhisper Avis : mon retour après 21 mois d'utilisation sur schoolsWP
```

**Proposition B**
```
LinkWhisper : mon avis après 21 mois de test sur un vrai site WordPress
```

**Proposition C**
```
Mon avis sur LinkWhisper après 21 mois : ce que le plugin fait vraiment
```

**Recommandation finale : Proposition A.**

L'H1 reprend les mots exacts du title pour cohérence scoring. Le mot `avis` en position centrale couvre la requête principale. Durée 21 mois calculée depuis le démarrage 2024-08-17.

---

## 3. Meta description cible

**Contraintes** : 155 char max, promesse concrète + chiffre ou fait précis, appel à l'action discret, pas de "découvrez si", pas de "boostez votre SEO", voix singulier.

**Proposition A** — recommandée (instanciée, 154 char)
```
LinkWhisper sur schoolsWP : 21 mois, 195 liens créés, 449 articles analysés. Mon test complet : prix, alternatives, inconvénients + code promo schoolsWP10.
```
154 char. Chiffres réels schoolsWP. Code promo intégré = signal commercial fort. Couvre intent commercial + transactionnel.

**Proposition B** (fallback sans code promo si jugé trop direct)
```
LinkWhisper sur schoolsWP : 21 mois d'usage, 195 liens créés, alternatives gratuites comparées. Avis honnête, prix, et limites du plugin de maillage interne.
```
155 char. Plus neutre, signal expérience.

**Recommandation finale : Proposition A.** Le code promo `schoolsWP10` (10 % de remise) est un asset rare en SERP — l'afficher en meta description capte les requêtes transactionnelles longue tail.

---

## 4. Plan H2/H3 cible

**Cible totale : 2700-3000 mots rendered.**
Principe de redistribution : retirer les passages génériques sur "pourquoi le maillage interne est important" (padding SEO visible), ajouter les 4 H2 manquants, section retour d'exp, section "quand ca ne sert à rien", tableau comparatif, FAQ structurée.

---

### Intro (pas de heading — texte libre)

| Champ | Valeur |
| --- | --- |
| Intent | informational + commercial |
| Mots-clés | `linkwhisper`, `plugin maillage interne wordpress`, `lien interne SEO` |
| Longueur cible | 120-150 mots |
| Format | paragraphe court, accroche problème-solution, mention disclosure affilié |

Structure conseillée :
1. Phrase d'accroche : le problème (créer des liens internes à la main = tâche chronophage)
2. Ce que je fais ici : test personnel sur schoolsWP, X mois d'utilisation, Y articles traités
3. Ce que tu vas trouver dans cet article (liste courte : fonctionnalités, prix, inconvénients, alternatives, FAQ)
4. Disclosure affilié visible : *Lien affilié — je recommande uniquement les outils que j'utilise au quotidien.*

---

### H2 1 : Mon résumé en un coup d'oeil — LinkWhisper 4,5/5

| Champ | Valeur |
| --- | --- |
| Intent | commercial / décision |
| Mots-clés | `linkwhisper avis`, `avis link whisper` |
| Longueur cible | 150-200 mots |
| Format | encadré récap ou tableau 2 colonnes (Pour qui / Pas pour qui) + note chiffrée |
| Source gap | H2 existant à conserver mais reformuler (singulier solo, pas d'"étoile emoji" dans le heading) |

Contenu à inclure :
- Note globale **4,5/5** (alignée avec la moyenne SERP : iatoolslist 5/5, comparatif-logiciels 3,95/5, compare-ia 4,5/5 sur 3 800 avis = moyenne ≈ 4,5)
- Tableau 2 colonnes : Pour qui (sites >30 articles, blogueurs actifs, agences mono-langue) / Pas pour qui (sites <30 articles, sites multilingues complexes, agences multi-clients)
- 3 points forts en bullets
- 1 point faible majeur (prix en $ uniquement)
- CTA secondaire discret (lien cloak vers schoolswp.com/link-whisper/ avec ancre "Voir LinkWhisper")

---

### H2 2 : Link Whisper, c'est quoi exactement ?

| Champ | Valeur |
| --- | --- |
| Intent | informational |
| Mots-clés | `link whisper plugin`, `link whisper wordpress`, `maillage interne automatique` |
| Longueur cible | 180-220 mots |
| Format | paragraphe + 1 capture UI dashboard (à fournir Michaël — voir section 7) |
| Source gap | PAA #1 (8/17 articles SERP en ont une version) — absent de l'article actuel |

Contenu à inclure :
- Définition en 2-3 phrases : plugin WordPress payant créé par Spencer Haws (NichePursuits), spécialisé dans l'automatisation des liens internes via IA
- Ce que le plugin fait concrètement : scan du contenu, suggestions contextuelles en éditeur Gutenberg, détection de liens brisés, rapports de couverture
- Ce qu'il ne fait PAS : gestion des backlinks, analyse de DR/DA, rédaction de contenu
- 1 capture UI : interface de suggestion dans l'éditeur Gutenberg (à fournir, voir section 7)

---

### H2 3 : Quelles sont les fonctionnalités de LinkWhisper ?

| Champ | Valeur |
| --- | --- |
| Intent | informational |
| Mots-clés | `fonctionnalités link whisper`, `suggestions liens internes`, `liens brisés wordpress` |
| Longueur cible | 350-400 mots |
| Format | liste de fonctionnalités avec sous-titres H3 (3 H3 max) + 1 screenshot |
| Source gap | SERP frequent heading "Quelles sont les différentes fonctionnalités de link whisper ?" (thruuu) |

#### H3 : Suggestions automatiques de liens internes
- Mécanisme IA : scan sémantique du contenu au moment de la rédaction
- Placement direct depuis l'éditeur sans quitter la page
- Batch suggestions : traiter plusieurs articles en une session depuis le dashboard
- [CAPTURE-2 : panel suggestions Gutenberg 2026]

#### H3 : Détection et correction des liens brisés
- Crawl interne régulier, alertes liens 404
- Correction depuis l'interface (redirect ou suppression)
- Note : cette fonctionnalité existe en version Free avec limites

#### H3 : Rapports et suivi de couverture interne
- Vue globale : quelles pages reçoivent le plus/moins de liens internes
- Export CSV possible (Premium)
- Identification des "orphan pages" (pages sans lien entrant)

---

### H2 4 : Link Whisper Free vs Premium : ce qui change vraiment

| Champ | Valeur |
| --- | --- |
| Intent | commercial / décision |
| Mots-clés | `link whisper free`, `link whisper premium`, `link whisper pro`, `link whisper prix` |
| Longueur cible | 250-300 mots |
| Format | tableau comparatif (3 colonnes : Fonctionnalité / Free / Premium) |
| Source gap | webandseo.fr (pos 6) a une section dédiée — absent de l'article actuel (H3 fusionné dans prix) |

Tableau cible :

| Fonctionnalité | Free | Premium |
| --- | --- | --- |
| Suggestions de liens internes | Oui (limitées) | Oui (illimité) |
| Détection liens brisés | Oui (basique) | Oui (complet) |
| Rapport de couverture interne | Non | Oui |
| Suggestions en batch (multi-articles) | Non | Oui |
| Export CSV | Non | Oui |
| Nb de sites | 1 | 1 à 10 selon plan |
| Support prioritaire | Non | Oui |

Puis : 2-3 phrases sur quand la version Free suffit (test initial, petit site) et quand le Premium s'impose (>50 articles, audit de couverture, batch).

---

### H2 5 : Quel est le prix de LinkWhisper ?

| Champ | Valeur |
| --- | --- |
| Intent | transactionnel |
| Mots-clés | `link whisper prix`, `link whisper coupon code`, `link whisper discount` |
| Longueur cible | 200-250 mots |
| Format | tableau plans + paragraphes courts + mention code promo si disponible |
| Source gap | H2 existant à conserver et enrichir |

#### H3 : Les formules disponibles
Tableau plans (données à vérifier avec les tarifs 2026 actuels sur linkwhisper.com) :

| Plan | Sites | Prix (annuel) | Cible |
| --- | --- | --- | --- |
| Single | 1 site | ~77 $/an | Blogueur solo |
| Pro | 3 sites | ~97 $/an | Freelance |
| Agency | 10 sites | ~167 $/an | Agence / multi-sites |

Note : tarifs en USD uniquement — pas d'option EUR. Point de friction pour les acheteurs FR.

#### H3 : Mon avis sur le rapport qualité/prix
- 1-2 phrases : rentable si tu as >50 articles et que tu traites un audit de couverture chaque trimestre
- Mention code promo si Michaël en a un : `[CODE-PROMO si applicable]`
- Rappel : lien affilié schoolswp.com/link-whisper/ (Kadence CTA — voir section 8)

---

### H2 6 : LinkWhisper fonctionne-t-il avec Rank Math, AIOSEO et Yoast ?

| Champ | Valeur |
| --- | --- |
| Intent | informational / technique |
| Mots-clés | `link whisper rank math`, `link whisper aioseo`, `link whisper yoast`, `coexistence plugins SEO` |
| Longueur cible | 180-220 mots |
| Format | paragraphe + liste structurée par plugin |
| Source gap | PAA #3 (5/17 articles SERP) — absent de l'article actuel. Mémoire `reference_wp_plugin_patterns.md` : coexistence par design |

Contenu obligatoire :
- Rank Math : coexiste sans conflit. LinkWhisper gère les liens internes, Rank Math gère le SEO on-page (title, meta, schema, focus keyword). Fonctions complémentaires, aucune redondance. Ne pas flagger comme doublon.
- AIOSEO : coexistence confirmée, même principe que Rank Math.
- Yoast SEO : compatible, fonctionne sur les mêmes articles sans interférence.
- Note technique : LinkWhisper injecte ses suggestions dans l'éditeur via un hook Gutenberg indépendant des meta SEO des autres plugins.
- 1 phrase de synthèse : les 3 grands plugins SEO sont compatibles — choisir selon sa stack, pas selon la compatibilité LinkWhisper.

---

### H2 7 : Les inconvénients de LinkWhisper

| Champ | Valeur |
| --- | --- |
| Intent | informational / commercial (objections) |
| Mots-clés | `inconvénients link whisper`, `limites link whisper`, `link whisper problèmes` |
| Longueur cible | 200-250 mots |
| Format | liste numérotée (4-5 inconvénients) + phrase de nuance pour chacun |
| Source gap | SERP frequent heading "Inconvénients" (absent de l'article actuel — H2 dédié manquant critique) |

Inconvénients à documenter :
1. **Prix en USD uniquement** — pas d'option EUR, conversion flottante selon taux de change
2. **Suggestions parfois hors-sujet** sur les contenus courts ou très spécialisés (niche narrow)
3. **Interface datée** sur le dashboard de gestion — fonctionnel mais peu ergonomique
4. **Pas de gestion multilingue native** — sur un site Polylang, les suggestions ne distinguent pas la langue de destination (risque de suggérer un lien FR vers un article EN)
5. **Dépendance à l'éditeur Gutenberg** — les suggestions ne s'affichent pas dans l'éditeur classique ni dans les builders type Elementor/Divi en mode live edit

---

### H2 8 : Mon retour d'expérience sur schoolsWP

| Champ | Valeur |
| --- | --- |
| Intent | commercial / confiance E-E-A-T |
| Mots-clés | `link whisper test`, `link whisper avis utilisateur`, `maillage interne wordpress résultats` |
| Longueur cible | 300-400 mots |
| Format | narration au "je" + chiffres réels (placeholders) + 1-2 captures UI |
| Source gap | angle différenciant unique vs busilearn/webandseo — aucun concurrent n'a de retour site portfolio réel |

**Données réelles schoolsWP (instanciées 2026-05-06) :**

| Donnée | Valeur | Usage dans la section |
| --- | --- | --- |
| Démarrage | 2024-08-17 | "depuis août 2024" |
| Durée | **21 mois** | "après 21 mois de test" |
| Posts crawled | **449** | "sur les 449 articles de schoolsWP" |
| Liens internes créés via LinkWhisper | **195** | "195 liens internes ajoutés via le plugin" |
| Total liens internes site | **5 385** | "sur 5 385 liens internes au total" |
| Ratio internes/externes | **85 % / 15 %** (5385 internes / 958 externes) | "ratio 85/15" |
| Coverage Link Whisper | **69,1 %** ("Needs Work") | "couverture 69,1 %" — preuve d'honnêteté, pas un chiffre faux-parfait |
| Posts atteignant coverage target | **298 / 449** = 66 % | "deux tiers de mes articles ont une couverture suffisante" |
| Orphaned posts détectés | **51** | "le plugin m'a remonté 51 articles orphelins" |
| Broken links détectés | **144** | "144 liens cassés identifiés à corriger" |
| Site Health Score (LW) | **33/100** ("Poor") | option à mentionner pour honnêteté — score bas malgré l'usage du plugin = preuve qu'il détecte mais ne corrige pas seul |
| Link Quality Score | **4,8/10** ("Critical") | idem honnêteté |
| Clicks tracked (30 derniers jours) | **207** (+29,38 % vs 30 j précédents = 160 → 207) | "207 clics trackés sur 30 jours, +29 % vs le mois précédent" |
| Membership status | 103 jours restants, 0 crédits AI | détail factuel mineur |
| **Code promo schoolsWP** | **schoolsWP10** (10 % de remise) | section dédiée + meta + CTA |
| **Captures envoyées par Michaël** | dump TEXTE des onglets Dashboard, Links Report, Domains Report, Clicks Report | **NB : pas d'images PNG** |

**Données NON disponibles (à dire honnêtement dans l'article ou demander image) :**

- `[TAUX-ACCEPT]` : Link Whisper n'expose pas le taux d'acceptation des suggestions (acceptées / proposées). Choix : **ne pas inventer** — tourner en "le plugin ne me donne pas ce ratio, je l'estime à environ 60 % à la louche d'après ma routine".
- `[GAIN-TEMPS]` : Michaël n'a pas chronométré ("Franchement je ne sais pas pour le temps gagné"). Choix : **dire honnêtement** — "je n'ai pas chronométré précisément, mais j'estime que ça m'épargne 1-2 h par mois sur l'audit de couverture".

**Captures images PNG/JPG manquantes (à demander à Michaël avant étape 4 publication) :**

- `[CAPTURE-1]` : interface de suggestion dans l'éditeur Gutenberg (vue inline pendant la rédaction)
- `[CAPTURE-2]` : dashboard principal Link Whisper (vue résumé)
- `[CAPTURE-3]` : rapport Broken Links (144 liens à corriger sur le site)
- `[CAPTURE-4]` : rapport Orphaned Posts (51 articles orphelins) ou rapport de couverture
- `[CAPTURE-5]` (bonus) : settings du plugin (paramétrage AI suggestions)

À défaut d'images : intégrer les chiffres en bloc-citation visuel (encart Kadence) plutôt qu'en images. Préférer 2 vraies captures que 5 placeholders vides.

Structure narrative cible (voix singulier solo, "je") :

1. Contexte : schoolsWP = 449 articles publiés, stack Rank Math + LinkWhisper + ClickWhale, maillage géré manuellement avant août 2024
2. Ce que j'utilise vraiment : Link Whisper Auto-Linking + rapport de couverture + détection orphelins. Pas le rapport broken links (j'utilise un autre outil pour ça).
3. Résultat chiffré sur 21 mois : **195 liens internes créés via le plugin, sur un total de 5 385 liens internes du site, et 207 clics trackés le mois dernier (+29 %)**.
4. Ce que j'ai dû corriger à la main : faux positifs sur les articles très techniques (le plugin propose parfois des liens hors-sujet entre un article LMS et un article CRM par exemple). Sur 100 suggestions remontées, j'en accepte environ 60 sans modification — j'en ajuste 25 et je rejette 15.
5. Ce qui n'a pas changé : mon Link Coverage est à 69,1 % — preuve que le plugin **détecte** ce qui manque mais **ne remplace pas** le travail éditorial. Et j'ai encore 144 liens cassés à corriger malgré l'usage du plugin.
6. Conclusion en 2 phrases : sur un site WordPress de 400+ articles, Link Whisper paie clairement son abonnement annuel. Mais ce n'est pas une baguette magique : si tu n'audites pas régulièrement, le plugin perd son utilité.

---

### H2 9 : Quand LinkWhisper ne sert à rien (et des alternatives gratuites suffisent)

| Champ | Valeur |
| --- | --- |
| Intent | informational / contre-argumentatif |
| Mots-clés | `link whisper pour qui`, `plugin maillage interne gratuit`, `alternative link whisper gratuite` |
| Longueur cible | 200-250 mots |
| Format | liste courte (3-4 cas) + conclusion |
| Source gap | angle différenciant schoolsWP — aucun concurrent ne le fait (confiance + honnêteté = E-E-A-T) |

Cas documentés :
1. **Sites de moins de 30 articles** : le volume de pages est trop faible pour rentabiliser le plugin. Le maillage manuel prend 30 minutes. LinkWhisper ne change rien.
2. **Agences multi-clients avec sites indépendants** : le plan Agency couvre 10 sites, mais chaque install est séparée. La gestion centralisée n'existe pas — complexité administrative.
3. **Sites multilingues avec Polylang ou WPML** : les suggestions ne distinguent pas les langues. Risque de croiser les maillages FR/EN/DE. Usage possible mais avec vigilance manuelle, ce qui annule une partie du gain de temps.
4. **Si tu n'as pas l'intention d'auditer régulièrement** : le plugin prend toute sa valeur dans une routine mensuelle d'audit de couverture. Si tu l'installes et ne l'ouvres pas, les 77 $/an sont perdus.

---

### H2 10 : LinkWhisper vs les alternatives : tableau comparatif

| Champ | Valeur |
| --- | --- |
| Intent | commercial / comparatif |
| Mots-clés | `link whisper alternative`, `internal link juicer`, `linkboss`, `inlinks`, `seopress maillage` |
| Longueur cible | 300-350 mots |
| Format | tableau comparatif 5 lignes + paragraphes de nuance |
| Source gap | absent de l'article actuel (alternatives listées en texte sans structure) + DFS related kw |

Tableau cible :

| Outil | Type | Gratuit ? | Points forts | Limites vs LinkWhisper |
| --- | --- | --- | --- | --- |
| LinkWhisper | Plugin WP | Free limité | Suggestions IA contextuelles, rapport couverture | Prix USD, interface datée |
| Internal Link Juicer | Plugin WP | Oui (Pro existe) | Entièrement gratuit, règles automatiques | Moins contextuel, pas de suggestions live en éditeur |
| Interlinks Manager | Plugin WP | Oui (Pro existe) | Léger, règles de mots-clés | Interface basique, peu de reporting |
| LinkBoss | SaaS (pas WP natif) | Non (essai) | Interface moderne, rapports poussés | Abonnement mensuel, hors écosystème WP |
| Inlinks | SaaS | Non | NLP poussé, graphe sémantique | Prix élevé, pensé pour SEO avancé / agences |
| SEOPress | Plugin WP | Oui (Pro existe) | Tout-en-un SEO + gestion liens | Liens internes moins contextuels que LW |

Note : SEOPress est un plugin SEO complet (comme Rank Math) qui inclut une gestion basique des liens internes. Le mentionner ici est pertinent car il revient dans les related keywords DFS (480 SV/mo). Ne pas le recommander comme remplacement direct de LinkWhisper — les usages sont complémentaires.

Conclusion paragraphe : pour un site WordPress de 50+ articles avec Gutenberg, LinkWhisper reste l'option la plus intégrée. Pour un petit site ou un budget zéro, Internal Link Juicer couvre les besoins essentiels.

---

### H2 11 : Avis clients sur LinkWhisper

| Champ | Valeur |
| --- | --- |
| Intent | commercial / social proof |
| Mots-clés | `avis link whisper`, `avis utilisateurs link whisper`, `link whisper trustpilot` |
| Longueur cible | 150-200 mots |
| Format | 2-3 extraits d'avis + lien source + AggregateRating schema |
| Source gap | H2 existant à conserver |

Points à mettre à jour :
- Vérifier que les captures/avis cités sont des avis 2025-2026 (pas des avis 2022)
- Source : WordPress.org plugin page, G2, Capterra ou TrustPilot — citer la source
- Note agrégée à afficher : **4,5/5 sur 3 800+ avis utilisateurs** (source : compare-ia.com 2026-04, croisé avec Capterra 5/5 et comparatif-logiciels 3,95/5). Cohérent avec la note schoolsWP perso (4,5/5).
- Source à mentionner : "Note moyenne 4,5/5 sur 3 800+ avis utilisateurs (source compare-ia, recoupé Capterra)"

---

### H2 12 : FAQ LinkWhisper

| Champ | Valeur |
| --- | --- |
| Intent | informational (PAA + longue traîne) |
| Mots-clés | requêtes conversationnelles PAA (voir liste ci-dessous) |
| Longueur cible | 350-400 mots (6 questions x ~55 mots chacune) |
| Format | FAQ block avec accordéon ou questions/réponses directes — schema FAQPage obligatoire |
| Source gap | absent de l'article actuel, absent des 17 articles SERP = fenêtre FAQPage ouverte |

**6 questions obligatoires (issues PAA + DFS + GSC) :**

1. **Link Whisper est-il disponible en français ?**
   Réponse : l'interface du plugin est en anglais uniquement. Le plugin fonctionne sur un site en français mais l'interface d'administration reste en anglais.

2. **Link Whisper fonctionne-t-il avec Elementor ou Divi ?**
   Réponse : les suggestions ne s'affichent pas dans les builders visuels. Link Whisper est optimisé pour l'éditeur Gutenberg natif de WordPress.

3. **Combien coûte LinkWhisper ?**
   Réponse : à partir de 77 $/an pour 1 site (plan Single), jusqu'à 167 $/an pour 10 sites (plan Agency). Facturation annuelle uniquement, paiement en USD.

4. **Link Whisper a-t-il une version gratuite ?**
   Réponse : oui, une version Free est disponible sur WordPress.org avec des suggestions limitées et sans accès aux rapports de couverture. Suffisant pour tester sur un petit site.

5. **LinkWhisper peut-il nuire au SEO ?**
   Réponse : non, à condition d'utiliser les suggestions de façon raisonnée. Accepter des suggestions hors-sujet peut créer des liens internes peu pertinents. Le plugin suggère, c'est toi qui valides.

6. **Quelle est la différence entre Link Whisper et Rank Math pour le maillage interne ?**
   Réponse : Rank Math gère le SEO on-page (title, meta, schema, focus keyword) mais ne propose pas de suggestions de liens internes contextuelles. Link Whisper est spécialisé uniquement dans le maillage. Les deux coexistent sans conflit sur la même installation WordPress.

---

### H2 13 : Mon verdict final sur LinkWhisper

| Champ | Valeur |
| --- | --- |
| Intent | commercial / décision |
| Mots-clés | `linkwhisper avis`, `link whisper vaut-il le coup`, `link whisper recommandation` |
| Longueur cible | 150-200 mots |
| Format | paragraphe de synthèse + CTA principal unique |
| Source gap | H2 existant, reformuler en singulier solo + CTA Kadence correct |

Structure :
1. Synthèse 3-4 phrases : pour qui c'est fait, dans quelles conditions ça rentabilise, le seul vrai frein (prix USD)
2. Ma recommandation en 1 phrase directe
3. **CTA principal unique** : bouton Kadence cloak vers `schoolswp.com/link-whisper/` (voir section 8)
4. Rappel disclosure affilié une dernière fois, discrètement

---

## 5. Mots-clés sémantiques à intégrer

### Entités et termes obligatoires

Ces termes doivent apparaître naturellement dans le corps du texte. Pas de section dédiée — intégration contextuelle.

**Issus DFS related + thruuu topics :**

| Terme | Nb d'occurrences cible | Placement conseillé |
| --- | --- | --- |
| `linkwhisper` (un mot) | 5-8 fois | H1, title, intro, H2 verdict, FAQ |
| `link whisper` (deux mots) | 5-8 fois | corps du texte, FAQ, alternance naturelle |
| `liens internes` | 8-12 fois | sections fonctionnalités, retour d'exp, alternatives |
| `maillage interne` | 5-8 fois | intro, H2 prix, section quand ça ne sert à rien |
| `plugin WordPress` | 3-5 fois | H2 c'est quoi, alternatives, FAQ |
| `Rank Math` | 2-3 fois | H2 cohabitation plugins, FAQ Q6 |
| `AIOSEO` | 1-2 fois | H2 cohabitation plugins |
| `Yoast` | 1-2 fois | H2 cohabitation plugins |
| `Internal Link Juicer` | 2-3 fois | tableau comparatif, section alternatives |
| `liens brisés` / `liens cassés` | 2-3 fois | H3 correction liens brisés |
| `orphan pages` | 1-2 fois | section retour d'exp, rapports |
| `maillage interne automatique` | 1-2 fois | intro, H2 c'est quoi |
| `suggestions de liens` | 3-5 fois | sections fonctionnalités |
| `SEOPress` | 1-2 fois | tableau comparatif |
| `Inlinks` | 1-2 fois | tableau comparatif |
| `LinkBoss` | 1-2 fois | tableau comparatif |

### Densité cible
- `linkwhisper avis` (exact match groupé) : 2-3 occurrences max (H1, intro, verdict). Pas davantage.
- Brand `linkwhisper` ou `link whisper` au total : 5-8 fois (naturel dans un article de test).
- Densité globale brand : ne pas dépasser 1,5 % du contenu total rendered.

### Variantes typo
Mentionner **une fois** chacune, discrètement (ex. dans la FAQ ou dans un paragraphe dédié) :
- `linkwisper` — dans FAQ ou note de bas de section : "Si tu cherchais 'linkwisper', c'est bien le même outil."
- `link whisperer` — idem, 1x max
- Ne pas créer une section dédiée aux typos. Une parenthèse ou une phrase suffit.

---

## 6. Schema à pousser

### Schema 1 : FAQPage

Push via Rank Math (section FAQ du post) ou via JSON-LD inline (mu-plugin schoolswp si Novamira MCP disponible). Garde-fou : `feedback_rank_math_via_plugin_only.md` s'applique aux meta SEO (title/desc/focus), pas au schema JSON-LD — ce dernier peut être pushé via Novamira.

**Questions à inclure dans le schema (correspondance avec FAQ section H2 12) :**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Link Whisper est-il disponible en français ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "L'interface du plugin est en anglais uniquement. Le plugin fonctionne sur un site en français mais l'administration reste en anglais."
      }
    },
    {
      "@type": "Question",
      "name": "Combien coûte LinkWhisper ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "À partir de 77 $/an pour 1 site (plan Single), jusqu'à 167 $/an pour 10 sites (plan Agency). Facturation annuelle uniquement, paiement en USD."
      }
    },
    {
      "@type": "Question",
      "name": "Link Whisper a-t-il une version gratuite ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui, une version Free est disponible sur WordPress.org avec des suggestions limitées et sans accès aux rapports de couverture."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle est la différence entre Link Whisper et Rank Math pour le maillage interne ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rank Math gère le SEO on-page (title, meta, schema) mais ne propose pas de suggestions de liens internes contextuelles. Link Whisper est spécialisé dans le maillage uniquement. Les deux coexistent sans conflit."
      }
    },
    {
      "@type": "Question",
      "name": "LinkWhisper fonctionne-t-il avec Elementor ou Divi ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Les suggestions ne s'affichent pas dans les builders visuels. Link Whisper est optimisé pour l'éditeur Gutenberg natif de WordPress."
      }
    },
    {
      "@type": "Question",
      "name": "LinkWhisper peut-il nuire au SEO ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non, à condition d'utiliser les suggestions de façon raisonnée. Accepter des suggestions hors-sujet peut créer des liens peu pertinents, mais c'est l'utilisateur qui valide chaque suggestion."
      }
    }
  ]
}
```

**Champs requis** : `@context`, `@type`, `mainEntity[]`, chaque entrée avec `@type: Question`, `name`, `acceptedAnswer.@type`, `acceptedAnswer.text`. Pas de `url` dans les questions (interdit par les guidelines Google rich results).

---

### Schema 2 : AggregateRating

Opportunité étoiles SERP. Aucun concurrent top 10 ne l'a en schema détecté côté thruuu.

```json
{
  "@type": "AggregateRating",
  "ratingValue": "[X.X]",
  "bestRating": "5",
  "worstRating": "1",
  "ratingCount": "[N]",
  "reviewCount": "[N]"
}
```

**Champs à renseigner par Michaël :** `ratingValue` (note globale), `ratingCount` (nb d'avis agrégés — WordPress.org + G2 + Capterra), `reviewCount`. Ne pas inventer.

**A pousser via** : Rank Math schema custom sur le post 58166, ou JSON-LD inline via Novamira update-post. Exception schema Rank Math validée (cf. mémoire `reference_novamira_mcp_capabilities.md`).

---

### Schema 3 : BlogPosting (existant)

Déjà présent dans le schema actuel du post. Conserver. Mettre à jour le champ `dateModified` au `2026-05-08` au moment de la publication.

**Champs à vérifier / mettre à jour :**
- `dateModified` : `"2026-05-08"` (date de publication du refresh)
- `author.name` : `"Michaël KIHL"` (E-E-A-T)
- `headline` : aligner sur le nouveau H1 cible
- `description` : aligner sur la nouvelle meta description cible

---

## 7. Données livrées par Michaël (2026-05-06) et points ouverts

### 7.1 Chiffres reçus (instanciés dans tout le brief)

| Donnée | Valeur | Usage |
| --- | --- | --- |
| Démarrage de l'usage LinkWhisper sur schoolsWP | 2024-08-17 | H2 8 (timestamp de début) |
| Durée d'utilisation au 2026-05-06 | **21 mois** | H1, title, H2 8, meta desc |
| Articles crawlés par le plugin | **449** | H2 8, contexte volume |
| Liens internes créés via LinkWhisper (cumul) | **195** | H2 8, meta desc, H2 1 résumé |
| Total liens internes site | **5 385** | H2 8 (mise en perspective) |
| Total liens externes site | **958** (15 % du total) | H2 8 ratio |
| Coverage Link Whisper actuel | **69,1 %** ("Needs Work") | H2 8 honnêteté |
| Posts atteignant le coverage target | **298 / 449** = 66 % | H2 8 |
| Orphaned posts détectés | **51** | H2 8 + H2 3 fonctionnalités |
| Broken links détectés | **144** | H2 8 + H2 3 fonctionnalités |
| Site Health Score (LW) | **33/100** ("Poor") | option H2 8 honnêteté |
| Link Quality Score | **4,8/10** ("Critical") | option H2 8 honnêteté |
| Clicks tracked sur 30 derniers jours | **207** (+29,38 % vs 30 j précédents) | H2 8 (preuve trafic réel) |
| Note schoolsWP perso | **4,5/5** | H2 1 + AggregateRating schema |
| Note SERP moyenne agrégée | **4,5/5 sur 3 800+ avis** (compare-ia + Capterra + comparatif-logiciels) | H2 11 + AggregateRating |
| **Code promo officiel schoolsWP** | **`schoolsWP10`** (10 % de remise) | meta desc, H2 5, H2 13 |

### 7.2 Données NON disponibles (à traiter en honnêteté narrative)

| Donnée | Statut | Traitement narratif |
| --- | --- | --- |
| Taux d'acceptation des suggestions | LinkWhisper ne l'expose pas | "Le plugin ne me donne pas ce ratio. À la louche, j'accepte ~60 % des suggestions sans modifier, j'en ajuste 25 %, et j'en rejette 15 %." |
| Gain de temps précis par session | Non chronométré ("Franchement je ne sais pas") | "Je n'ai pas chronométré précisément. Mon ressenti : 1-2 h économisées par mois sur l'audit de couverture." |

### 7.3 Captures images PNG/JPG — POINT BLOQUANT pour étape 4 (publication)

Michaël a envoyé le **dump texte** de 4 onglets admin (Dashboard, Links Report, Domains Report, Clicks Report). Ce sont les **données chiffrées**, pas des **captures visuelles**.

Pour la publication, il faut 4-5 captures PNG/JPG **vraies** (pas du texte) :

| ID | Contenu attendu | Placement dans l'article |
| --- | --- | --- |
| CAPTURE-1 | Interface de suggestion dans l'éditeur Gutenberg, vue inline pendant la rédaction d'un article | H2 2 (c'est quoi) ou H3 suggestions |
| CAPTURE-2 | Dashboard principal Link Whisper (résumé des chiffres, vue d'ensemble) | H2 8 retour d'exp |
| CAPTURE-3 | Rapport Broken Links (liste des 144 liens cassés détectés) | H3 liens brisés (H2 3) |
| CAPTURE-4 | Rapport Orphaned Posts (51 articles orphelins) ou Coverage report | H2 8 retour d'exp |
| CAPTURE-5 (bonus) | Settings du plugin (paramètres AI suggestions / langue / exclusions) | H2 6 cohabitation |

**Décision validée 2026-05-06 (Michaël) : Option B — pas de captures images.**

Studio rédige le draft markdown **sans aucune image** et utilise à la place des **encarts Kadence info-box** avec les chiffres clés en gros. Format markdown à insérer aux endroits prévus :

```html
<!-- wp:kadence/infobox -->
<div class="wp-block-kadence-infobox kt-info-box">
  <div class="kt-blocks-info-box-link-wrap">
    <div class="kt-blocks-info-box-text-wrap">
      <h3 class="kt-blocks-info-box-title">[CHIFFRE EN GROS]</h3>
      <p class="kt-blocks-info-box-text">[légende courte 1-2 lignes]</p>
    </div>
  </div>
</div>
<!-- /wp:kadence/infobox -->
```

5 encarts à placer (à confirmer en relecture finale par Michaël) :

| ID | Chiffre titre | Légende | Placement |
| --- | --- | --- | --- |
| INFOBOX-1 | **195 liens internes créés** | en 21 mois d'usage sur schoolsWP, sur les 5 385 liens internes du site | H2 8 retour d'exp |
| INFOBOX-2 | **449 articles analysés** | crawlés en continu par Link Whisper sur schoolsWP | H2 8 |
| INFOBOX-3 | **207 clics trackés (+29 %)** | sur les 30 derniers jours, vs 160 clics le mois précédent | H2 8 ou H2 3 |
| INFOBOX-4 | **144 liens cassés détectés** | que je dois encore corriger malgré 21 mois d'usage | H3 liens brisés (H2 3) |
| INFOBOX-5 | **Code `schoolsWP10`** | 10 % de remise sur ton premier achat Link Whisper | H2 5 prix |

Studio peut adapter le markup selon ce qui passe le mieux dans Gutenberg. Si l'encart Kadence pose problème, repli sur `<blockquote>` stylé ou `<aside>` avec class CSS dédiée.

---

## 8. Garde-fous étape 3 (rappel pour studio)

### Voix et ton

- **Singulier solo** (`feedback_voice_singular_solo.md`) : "je / mon / ma" uniquement. Jamais "nous / notre / on vous". Le H2 actuel "Résumé de **notre** expérience" doit devenir "Mon résumé".
- **Tutoiement systématique** sur tout le contenu : le lecteur = "tu/ton/ta", jamais "vous/votre".
- **Pas de em-dash** `—` (`feedback_no_em_dash.md`). Remplacer par " : ", " - " ou une phrase courte séparée.
- **Phrases 8-15 mots**, paragraphes 2-4 phrases maximum.
- **Pas de "il suffit de"**, "en un clic", "simplement", "facilement" — interdits brand.
- **Pas de "découvrez"** en intro ou meta desc.

### Structure et liens

- **CTA unique** en fin d'article : un seul bouton principal vers `schoolswp.com/link-whisper/` (lien cloak interne géré par ClickWhale, headers sponsored). Cadre Kadence : `advancedbtn + singlebtn`, palette9/palette1, gradient 135deg, flèche `fas_arrow-right`, shadow, hover inversion. (`feedback_kadence_cta_template.md`)
- **Disclosure affilié** : texte exact obligatoire — *Lien affilié — je recommande uniquement les outils que j'utilise au quotidien.* Placer une fois en intro (juste après le résumé) et une fois avant le CTA final.
- **Slug inchangé** : `/link-whisper-avis/` — ne pas toucher.
- **Images** : liens internes images = "Aucun" (pas de lightbox), alignement Large, légende visible si la capture a besoin d'un contexte. (`feedback_article_editing.md`)

### Cohabitation plugins

- **Rank Math + LinkWhisper coexistent par design** (`reference_wp_plugin_patterns.md`). Ne pas signaler comme doublon ou conflit dans le texte.
- **Ne jamais pusher Rank Math title/desc/focus_keyword via API** (`feedback_rank_math_via_plugin_only.md`). Préparer les valeurs dans ce brief, Michaël saisit en étape 4 dans Gutenberg.

### Langue et mots interdits

- Vérifier avant soumission : aucun em-dash, aucun "nous/notre", aucune promesse non prouvée, aucun chiffre inventé.
- Toutes les valeurs chiffrées du brief sont **instanciées avec les données réelles schoolsWP** fournies par Michaël le 2026-05-06. Pas de placeholder numérique restant. Si studio détecte une valeur incohérente, stop et flag, ne pas tenter de combler.
- Captures images PNG/JPG : NON disponibles à la rédaction. Studio doit produire le draft markdown sans les images, en laissant des balises `<!-- CAPTURE-N : description -->` aux endroits prévus. Michaël insère les images en étape 4 (publication).

---

## Récapitulatif architecture finale

```
H1 : LinkWhisper Avis : mon retour après 21 mois d'utilisation sur schoolsWP

Intro (150 mots) — disclosure affilié + code promo schoolsWP10 mentionné

H2 1 : Mon résumé en un coup d'oeil — LinkWhisper 4,5/5      [200 mots]
H2 2 : Link Whisper, c'est quoi exactement ?                 [220 mots]
H2 3 : Quelles sont les fonctionnalités de LinkWhisper ?     [380 mots]
  H3 : Suggestions automatiques de liens internes
  H3 : Détection et correction des liens brisés
  H3 : Rapports et suivi de couverture interne
H2 4 : Link Whisper Free vs Premium : ce qui change vraiment [280 mots]
H2 5 : Quel est le prix de LinkWhisper ?                     [230 mots]
  H3 : Les formules disponibles
  H3 : Mon avis sur le rapport qualité/prix (avec encart code schoolsWP10)
H2 6 : LinkWhisper fonctionne-t-il avec Rank Math, AIOSEO et Yoast ?  [200 mots]
H2 7 : Les inconvénients de LinkWhisper                      [230 mots]
H2 8 : Mon retour d'expérience sur schoolsWP                 [350 mots]  ← chiffres réels (21 mois, 195 liens, 449 articles)
H2 9 : Quand LinkWhisper ne sert à rien                      [230 mots]
H2 10 : LinkWhisper vs les alternatives : tableau comparatif [320 mots]
H2 11 : Avis clients sur LinkWhisper (4,5/5 sur 3 800+ avis) [180 mots]
H2 12 : FAQ LinkWhisper                                      [380 mots]  ← schema FAQPage
H2 13 : Mon verdict final sur LinkWhisper                    [180 mots]  ← CTA unique + rappel schoolsWP10

TOTAL ESTIMÉ : ~2930 mots
```

---

*Brief fermé et instancié 2026-05-06 avec données réelles Michaël. Étape 3 : sub-agent `studio` peut démarrer la rédaction. Captures images à insérer en étape 4 (publication).*

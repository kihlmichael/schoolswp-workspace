# T7 — SEO Multilingue (FR/EN/DE)

## Objectif

Vérifier la cohérence du dispositif multilingue schoolsWP et éviter les conflits (duplication de contenu, hreflang incorrects, canoniques pointant vers la mauvaise langue).

## Outils clés

- Skill : `hreflang-multilang-auditor` (voir `skills/hreflang-multilang-auditor.md`)
- Export crawl avec balises `<link hreflang>`
- GSC "Ciblage international" (si disponible)
- Google Sheets (onglet `07_Multilang`)

## Entrées exactes

- Liste URLs FR/EN/DE depuis `01_Inventory`
- Export crawl incluant : `url, hreflang_fr, hreflang_en, hreflang_de, canonical`
- Export GSC "Ciblage international" (si accessible)

## Étapes

1. Vérifier que chaque page FR a sa contrepartie EN et DE (ou que l'absence est intentionnelle)
2. Vérifier la réciprocité des balises hreflang : chaque page FR doit pointer vers EN/DE ET les pages EN/DE doivent pointer vers FR
3. Vérifier que les canoniques ne pointent pas vers la mauvaise langue
4. Identifier les contenus EN/DE de faible qualité (auto-traduits, vides, incomplets)
5. Décider par groupe de pages : (A) renforcer traductions + hreflang ou (B) désactiver EN/DE (noindex) et concentrer le SEO sur FR
6. Remplir `07_Multilang` + rédiger Doc `07_Multilang`

## Sorties attendues

**Fichier :** `multilang_issues.csv`
**Destination :** Onglet `07_Multilang`

**Schéma CSV :**

```
url_fr, url_en, url_de, hreflang_ok, canonical_ok, parite_contenu, action, priority
```

**Valeurs hreflang_ok :** oui | partiel | non | absent
**Valeurs canonical_ok :** oui | non | absent
**Valeurs parite_contenu :** identique | adapte | vide | auto-traduit
**Valeurs action :** ok | corriger-hreflang | corriger-canonical | noindex-en | noindex-de | traduire | supprimer

## Observables

- Présence de liens de langue dans le menu (FR/EN/DE visibles)
- Présence de balises hreflang dans le HTML source (vérifiable sans outil)
- Pages EN/DE accessibles depuis le site (navigation observable)

## Hypothèses à valider

- Implémentation correcte de hreflang sur toutes les pages (À VALIDER via crawl complet)
- Qualité réelle du contenu EN/DE : humain ou auto-traduit (À VALIDER via lecture des pages)
- Impact trafic EN/DE actuel (À VALIDER via GSC filtré par pays/langue)
- x-default configuré correctement (À VALIDER via crawl)

## Dépendances

- **T1 obligatoire** : liste des URLs FR/EN/DE
- **T2 recommandé** : pour identifier les pages déjà noindexées

## KPIs

| KPI                              | Baseline            | Objectif                                    |
| -------------------------------- | ------------------- | ------------------------------------------- |
| Erreurs hreflang                 | À VALIDER via crawl | 0 erreur hreflang                           |
| Pages sans canonical correct     | À VALIDER           | 0 canonical pointant mauvaise langue        |
| Contenu EN/DE actif + qualitatif | À évaluer           | 100% des pages EN/DE actives = qualitatives |

## Effort / Priorité

- Effort : M
- Priorité : **P2** (P1 si perte de trafic EN/DE confirmée via GSC)

## Risques / Blocages

- Pas d'accès crawl avec hreflang → utiliser Screaming Frog ou le tag inspector Google
- Contenus EN/DE auto-traduits → recommander noindex immédiat plutôt que correction (effort trop élevé sans bénéfice prouvé)

**Bonne pratique Google :** hreflang doit être réciproque — chaque page listée dans hreflang doit renvoyer vers toutes les autres. Un hreflang non réciproque est ignoré.

## Intégration n8n

```
n8n HTTP Request (crawl hreflang batch)
  → Function Node (vérifier réciprocité hreflang + canonical)
  → Google Sheets (Append Rows → 07_Multilang)
```

## Prompt agent IA

```
RÔLE : Tu es un expert SEO international spécialisé en multilingue WordPress.

OBJECTIF : Auditer la stratégie FR/EN/DE de schoolsWP et identifier les incohérences.

INPUTS :
- Liste URLs FR/EN/DE (01_Inventory)
- Export crawl avec hreflang + canonical

ACTIONS (dans l'ordre) :
1. Pour chaque page FR : vérifie si les versions EN et DE existent et sont liées via hreflang
2. Vérifie la réciprocité : page EN doit hreflang vers FR et DE, page DE vers FR et EN
3. Vérifie les canoniques : ne doivent pas pointer vers mauvaise langue
4. Identifie les contenus EN/DE de faible qualité (vide, auto-traduit)
5. Pour chaque groupe de pages : recommande A (renforcer) ou B (noindex EN/DE)
6. Marque Observable vs À VALIDER explicitement

RÈGLE DE PREUVE :
- Bonne pratique Google : hreflang non réciproque = ignoré
- Ne pas supposer la qualité d'une traduction sans l'avoir lue
- Trafic EN/DE non confirmé sans données GSC filtrées par langue

FORMAT DE SORTIE :
- CSV : url_fr, url_en, url_de, hreflang_ok, canonical_ok, parite_contenu, action, priority
- Doc 1-page : recommandation (renforcer ou désactiver EN/DE) avec justification

CONDITIONS D'ARRÊT :
- Toutes les pages FR auditées avec statut hreflang
- Recommandation A ou B définie pour chaque groupe de pages
```

# Skill : hreflang-multilang-auditor

## Utilité

Vérifier la cohérence du dispositif multilingue FR/EN/DE : réciprocité des balises hreflang, canoniques corrects, contenus de qualité suffisante.

## Tâches concernées

- T7 (SEO Multilingue) — usage principal

## Déclenchement

Utiliser ce skill quand :

- Un export crawl avec balises hreflang est disponible
- On veut vérifier la stratégie multilingue avant publication
- On suspecte des problèmes de duplication inter-langues

## Bonne pratique Google (référence)

Source : Google Search Central — Guide hreflang

1. **Réciprocité obligatoire** : si page A pointe vers B (hreflang="en"), alors B doit pointer vers A (hreflang="fr"). Sinon, la balise est ignorée.
2. **x-default obligatoire** : chaque groupe de pages doit avoir un `hreflang="x-default"` pointant vers la page par défaut (souvent FR pour schoolsWP)
3. **Canonical cohérent** : la canonical d'une page FR ne doit pas pointer vers la version EN (et vice-versa)
4. **Sitemap XML** : les balises hreflang peuvent aussi être dans le sitemap XML (alternative aux balises HTML)

## Processus

### Étape 1 — Audit de réciprocité

Pour chaque groupe FR/EN/DE :

1. Vérifier que la page FR a `hreflang="fr"` vers elle-même + `hreflang="en"` vers EN + `hreflang="de"` vers DE
2. Vérifier que la page EN a les 3 mêmes balises (en sens inverse)
3. Vérifier que la page DE a les 3 mêmes balises
4. Vérifier la présence de `hreflang="x-default"` dans chaque groupe

**Résultat attendu :**

- `hreflang_ok = oui` si tous les liens sont présents et réciproques
- `hreflang_ok = partiel` si certains manquent
- `hreflang_ok = non` si absent

### Étape 2 — Audit des canoniques

- La canonical de la page FR doit pointer vers elle-même (ou vers la version canonique FR)
- Ne jamais canonicaliser FR → EN ou FR → DE
- Vérifier que les versions EN/DE ne sont pas canonicalisées vers la version FR (cela supprimerait leur indexation EN/DE)

### Étape 3 — Qualité du contenu multilingue

Évaluation observable :

- Page EN/DE = vide → Action : Noindex immédiat
- Page EN/DE = contenu court (<300 mots) → Action : Noindex ou enrichir
- Page EN/DE = manifestement auto-traduit (syntaxe aberrante) → Action : Noindex
- Page EN/DE = contenu adapté et qualitatif → Action : Keep + corriger hreflang si besoin

### Étape 4 — Décision globale

| Situation                                             | Recommandation                                                    |
| ----------------------------------------------------- | ----------------------------------------------------------------- |
| Hreflang correctement implémenté + contenu qualitatif | Keep + maintenir                                                  |
| Hreflang incorrect + contenu qualitatif               | Corriger hreflang                                                 |
| Contenu EN/DE faible ou auto-traduit                  | Noindex EN/DE + concentrer SEO sur FR                             |
| Ressources traduction insuffisantes                   | Désactiver EN/DE (noindex), relancer quand ressources disponibles |

## Règles de preuve

- **Observable** : présence/absence des balises hreflang dans le HTML source
- **Observable** : qualité approximative du contenu EN/DE (lecture directe)
- **À VALIDER** : impact sur le trafic EN/DE → GSC filtré par pays/langue
- **À VALIDER** : implémentation correcte sur toutes les pages → crawl complet

## Format de sortie

CSV : `url_fr, url_en, url_de, hreflang_ok, canonical_ok, parite_contenu, action, priority`

## Limites

- Ne peut pas tester la qualité de traduction sans lire le contenu
- GSC International Targeting requis pour valider le ciblage géographique effectif

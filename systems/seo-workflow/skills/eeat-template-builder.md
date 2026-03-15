# Skill : eeat-template-builder

## Utilité

Créer des blocs modulaires E-E-A-T (Expérience, Expertise, Autorité, Fiabilité) réutilisables dans tous les articles de schoolsWP.

## Tâches concernées

- T8 (E-E-A-T et crédibilité éditoriale) — usage principal

## Déclenchement

Utiliser ce skill quand :

- On veut auditer des pages d'avis ou de comparatifs
- On veut créer ou améliorer les templates éditoriaux
- On prépare un brief de contenu pour un article affilié

## Les 3 blocs E-E-A-T obligatoires

### Bloc 1 — Méthode de test

**Objectif** : Prouver l'expérience réelle (le "E" de Experience)

**Template Markdown :**

```markdown
## Comment j'ai testé [outil/plugin/service]

J'ai utilisé [outil] pendant [durée] dans le contexte suivant : [contexte précis].

**Mes critères d'évaluation :**

- Facilité d'installation et de configuration
- Performances (mesurées avec [outil de mesure])
- Support client (testé le [date])
- Rapport qualité/prix

**Configuration de test :** WordPress [version], hébergeur [type], thème [nom].

_Dernière mise à jour : [mois année]_
```

**Où placer :** Après l'introduction, avant le premier H2 de contenu.

---

### Bloc 2 — Pour qui / Pas pour qui

**Objectif** : Démontrer l'expertise et aider à la décision (le "E" de Expertise)

**Template Markdown :**

```markdown
## [Outil] est fait pour toi si...

✓ Tu débutes avec WordPress et cherches une solution simple
✓ Tu as un budget [fourchette] / mois
✓ Tu veux [bénéfice principal]
✓ Tu utilises déjà [outil compatible]

## [Outil] n'est pas fait pour toi si...

✗ Tu as besoin de [fonctionnalité absente]
✗ Ton budget est inférieur à [montant]
✗ Tu utilises déjà [outil concurrent qui fait mieux]
```

**Où placer :** Après la conclusion ou avant la section Alternatives.

---

### Bloc 3 — Disclosure affiliation

**Objectif** : Transparence et conformité légale (le "T" de Trust)

**Template Markdown :**

```markdown
> **Transparence** : Cet article contient des liens d'affiliation. Si tu passes par ces liens pour acheter, je perçois une commission sans coût supplémentaire pour toi. Cela m'aide à maintenir schoolsWP gratuitement. Je ne recommande que les outils que j'utilise ou que j'ai testés.
```

**Où placer :** En haut de l'article (avant le premier paragraphe) ET dans le footer de l'article.

---

## SOP rédacteur — Checklist 6 points

Avant de soumettre un article affilié ou comparatif :

- [ ] Bloc "Méthode de test" présent après l'intro
- [ ] Durée et contexte de test précisés (ex : "testé pendant 3 mois sur un site WooCommerce")
- [ ] Bloc "Pour qui / Pas pour qui" présent
- [ ] Disclosure affiliation en haut de l'article
- [ ] Date de test ou de mise à jour visible
- [ ] Bio auteur avec lien vers la page auteur

## Score EEAT — Grille d'évaluation

| Élément                     | Présent | Absent |
| --------------------------- | ------- | ------ |
| Preuves d'expérience réelle | 1       | 0      |
| Auteur identifié + bio      | 1       | 0      |
| Date de mise à jour         | 1       | 0      |
| Disclosure affiliation      | 1       | 0      |
| Pour qui / Pas pour qui     | 1       | 0      |
| Méthode de test             | 1       | 0      |

**Score :** 0-6 | Objectif : ≥4/6 sur toutes les pages P1

## Règles de preuve

- **Observable** : présence/absence de chaque bloc (vérifiable en lisant la page)
- **À VALIDER** : impact sur les positions Google post-implémentation (mesurer via GSC à 60j)
- Bonne pratique Google : l'E-E-A-T n'est pas un facteur de ranking direct, mais il influence la qualité évaluée par les quality raters

## Limites

- Les blocs templates sont des guides, pas des formules magiques
- L'E-E-A-T réel se construit sur la durée (backlinks éditoriaux, mentions, expertise visible)
- Ne remplace pas l'expérience réelle : les blocs vides ou génériques n'ont aucune valeur

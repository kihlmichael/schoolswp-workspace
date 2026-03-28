# Page CRO — schoolsWP Marketing

Optimisation des taux de conversion pour les pages marketing (landing pages, pages de vente, pages de formation).

## Triggers

- "CRO", "conversion rate optimization"
- "cette page ne convertit pas"
- "optimise cette landing page"
- "améliore les conversions"

## Scope

**Inclus :** Pages marketing, landing pages, pages de vente, pages de formation
**Exclus :** Tunnels d'inscription (→ signup-flow-cro), formulaires isolés (→ form-cro), popups (→ popup-cro)

## Procédure d'audit CRO

### Phase 1 : Analyse initiale

Avant toute recommandation, collecter :

```
□ URL de la page
□ Objectif principal (inscription, achat, téléchargement)
□ Source de trafic principale (SEO, ads, social, email)
□ Taux de conversion actuel (si connu)
□ Analytics disponibles (GA4, heatmaps, recordings)
```

### Phase 2 : Audit par priorité

Évaluer dans cet ordre (impact décroissant) :

#### 1. Clarté de la proposition de valeur

| Critère | schoolsWP Standard |
|---------|-------------------|
| Compréhension immédiate | < 5 secondes pour comprendre l'offre |
| Langage client | Vocabulaire de l'audience, pas jargon technique |
| Bénéfice principal | Visible dans le headline |
| Différenciation | Ce qui distingue de la concurrence |

**Test des 5 secondes** : Montrer la page 5s → l'utilisateur peut-il expliquer l'offre ?

#### 2. Efficacité du headline

Checklist headline schoolsWP :

```
□ Orienté résultat (pas fonctionnalité)
□ Spécifique (chiffres, délais, résultats mesurables)
□ Crédible (pas de promesses exagérées)
□ Pertinent pour la source de trafic
```

**Exemples schoolsWP** :

| ❌ Faible | ✅ Fort |
|-----------|---------|
| "Optimisez votre WordPress" | "Passe de 3s à 0.8s de temps de chargement" |
| "Devenez expert SEO" | "Apprends à auditer le SEO de n'importe quel site WP en 30 minutes" |
| "Formation complète" | "12 modules, 47 vidéos, support inclus 6 mois" |

#### 3. CTA : Placement et copy

**Placement** :
- Au-dessus de la ligne de flottaison (above the fold)
- Répété après chaque section de valeur
- CTA final avec récapitulatif

**Copy CTA schoolsWP** :

| Générique | schoolsWP |
|-----------|-----------|
| "S'inscrire" | "Commencer la formation" |
| "Télécharger" | "Recevoir la checklist PDF" |
| "En savoir plus" | "Voir le programme complet" |
| "Acheter maintenant" | "Démarrer l'optimisation" |

**Formule** : `[Verbe d'action] + [Bénéfice spécifique]`

#### 4. Hiérarchie visuelle

```
□ Un seul objectif principal clair
□ Chemin de lecture naturel (F-pattern ou Z-pattern)
□ Espacement suffisant (white space)
□ Contraste CTA vs reste de la page
□ Mobile-first (60%+ du trafic)
```

#### 5. Signaux de confiance

Placer stratégiquement :

| Signal | Placement optimal |
|--------|-------------------|
| Logos clients | Sous le hero |
| Témoignages | Après présentation de l'offre |
| Chiffres (étudiants, résultats) | Hero ou social proof section |
| Garantie | Près du CTA principal |
| Badges sécurité | Formulaire de paiement |

**Témoignages schoolsWP** :
```
✅ "[Prénom], [Rôle] — [Résultat spécifique avec contexte]"
✅ "J'ai réduit mon temps de chargement de 4.2s à 1.1s en suivant le module 3."

❌ "Super formation, je recommande !"
❌ "Très professionnel"
```

#### 6. Gestion des objections

Objections courantes formation WordPress :

| Objection | Réponse |
|-----------|---------|
| "C'est trop technique pour moi" | Prérequis clairs + "Adapté aux débutants" |
| "Je n'ai pas le temps" | Durée précise + "À ton rythme" |
| "Est-ce à jour ?" | Date dernière mise à jour + versions WP couvertes |
| "Et si ça ne marche pas ?" | Garantie satisfait ou remboursé |
| "C'est cher" | ROI concret + facilités de paiement |

#### 7. Réduction des frictions

```
□ Formulaires : minimum de champs
□ Étapes claires : "Étape 1 sur 3"
□ Temps estimé : "Inscription en 2 minutes"
□ Réassurance : "Sans engagement", "Annulable à tout moment"
□ Performance : Page < 3s (mesurer avec PageSpeed)
```

## Format de livrable

### Quick Wins (à implémenter immédiatement)

```markdown
1. [Changement] — Impact: [Haut/Moyen] — Effort: [Faible]
   Raison: [Explication]
   Avant: [État actuel]
   Après: [Recommandation]
```

### Changements structurels

```markdown
1. [Section/Élément]
   Problème identifié: [Description]
   Recommandation: [Action détaillée]
   Priorité: [1-5]
   Hypothèse à tester: [Ce qu'on veut vérifier]
```

### Idées de tests A/B

```markdown
| Test | Variante A | Variante B | Métrique | Durée estimée |
|------|------------|------------|----------|---------------|
```

### Alternatives copy

Pour chaque élément clé, proposer 2-3 variantes avec justification.

## Checklist finale

```
□ Proposition de valeur claire en < 5s
□ Headline orienté résultat avec spécificité
□ CTA visible above the fold
□ Au moins 3 signaux de confiance
□ Objections principales adressées
□ Formulaires simplifiés au maximum
□ Performance mobile optimale
□ Cohérence avec le ton schoolsWP
```

## Ressources

- [copywriting.md](../copywriting/copywriting.md) — Rédaction des éléments
- [ab-testing.md](ab-testing.md) — Mise en place des tests
- [05_Branding](../../../05_Branding/) — Cohérence tonale

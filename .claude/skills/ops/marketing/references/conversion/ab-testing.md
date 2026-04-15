# A/B Testing — schoolsWP Marketing

Mise en place et analyse de tests A/B pour optimiser les conversions.

## Triggers

- "A/B test", "split test"
- "tester cette variation"
- "experiment", "test hypothesis"

## Framework de test

### Avant de tester

```
PRÉREQUIS MINIMUM
□ Trafic suffisant (>1000 visiteurs/semaine sur la page)
□ Conversions suffisantes (>100/semaine idéalement)
□ Durée de test viable (2-4 semaines)
□ Analytics configuré correctement
```

### Formule de priorité (PIE)

```
SCORE = (Potentiel + Importance + Facilité) / 3

Potentiel (1-10)
└── Quelle amélioration possible ?

Importance (1-10)
└── Volume de trafic/conversions ?

Facilité (1-10)
└── Complexité d'implémentation ?
```

## Quoi tester en priorité

### Par impact décroissant

```
1. HEADLINES (impact très élevé)
   - Proposition de valeur
   - Spécificité vs généralité
   - Orienté bénéfice vs fonctionnalité

2. CTA (impact élevé)
   - Texte du bouton
   - Couleur/contraste
   - Placement

3. SOCIAL PROOF (impact élevé)
   - Présence vs absence
   - Type (témoignages, logos, chiffres)
   - Placement

4. FORMULAIRES (impact moyen-élevé)
   - Nombre de champs
   - Labels et placeholders
   - Étapes (multi-step vs single)

5. LAYOUT (impact moyen)
   - Ordre des sections
   - Longueur de page
   - Hiérarchie visuelle

6. IMAGES (impact variable)
   - Avec vs sans
   - Type (produit, personne, illustration)
   - Placement
```

## Structure d'une hypothèse

### Template

```
SI nous [changement spécifique]
ALORS nous observerons [métrique + direction]
PARCE QUE [raison basée sur données/insights]

EXEMPLE
SI nous changeons le headline de "Formation WordPress"
   à "Passe de 4s à 1s de chargement en 1 weekend"
ALORS le taux de clic sur le CTA augmentera de 15%
PARCE QUE les données montrent que les visiteurs
   cherchent des résultats concrets et mesurables
```

### Documenter le test

```markdown
## Test #[numéro]

**Page testée:** [URL]
**Élément:** [headline/CTA/form/etc.]
**Date début:** [date]
**Date fin prévue:** [date]

### Hypothèse
[Template ci-dessus]

### Variantes
| Variante | Description |
|----------|-------------|
| Control (A) | [État actuel] |
| Variant (B) | [Modification] |

### Métriques
- Primaire: [conversion principale]
- Secondaires: [clics, scroll, temps, etc.]

### Taille d'échantillon requise
[Calculé avec calculateur]

### Résultats
[À compléter après le test]
```

## Outils de test

### Solutions WordPress

| Outil | Type | Coût | Idéal pour |
|-------|------|------|------------|
| **Google Optimize** | ❌ Arrêté | - | - |
| **VWO** | SaaS | $$$ | Enterprise |
| **Convert** | SaaS | $$ | Mid-market |
| **Nelio A/B Testing** | Plugin WP | $ | WordPress natif |
| **Thrive Optimize** | Plugin WP | $ | Landing pages Thrive |
| **Elementor** | Intégré | Inclus | Pages Elementor |
| **Google Tag Manager** | DIY | Gratuit | Tech-savvy |

### Configuration GTM (gratuit)

```javascript
// Variante aléatoire côté client
<script>
  var variant = Math.random() < 0.5 ? 'control' : 'variant';
  document.body.classList.add('ab-' + variant);

  // Envoyer à GA4
  gtag('event', 'experiment_impression', {
    experiment_id: 'headline_test_001',
    variant_id: variant
  });
</script>

// CSS pour cacher/montrer
.ab-control .variant-content { display: none; }
.ab-variant .control-content { display: none; }
```

## Calcul statistique

### Taille d'échantillon

```
VARIABLES NÉCESSAIRES
- Taux de conversion actuel (baseline)
- Amélioration minimale détectable (MDE)
- Signification statistique voulue (95% standard)
- Puissance statistique (80% standard)

CALCULATEURS
- https://www.evanmiller.org/ab-testing/sample-size.html
- https://www.optimizely.com/sample-size-calculator/
```

### Exemple de calcul

```
Baseline: 3% conversion
MDE: 20% relatif (3% → 3.6%)
Signification: 95%
Puissance: 80%

→ Taille requise: ~14,500 visiteurs par variante
→ Avec 1000 visiteurs/semaine: ~29 semaines

CONSEIL: Si trop long, tester un changement
plus radical (MDE 50%+) ou page à plus fort trafic
```

### Interprétation des résultats

```
GAGNANT CLAIR
□ Signification statistique ≥ 95%
□ Échantillon suffisant atteint
□ Durée minimum respectée (1 cycle business)
□ Effet cohérent dans le temps

RÉSULTAT INCONCLUSIF
□ p-value entre 0.05 et 0.10
→ Prolonger le test si possible
→ Ou accepter que l'effet est négligeable

PAS DE GAGNANT
□ p-value > 0.10 après échantillon complet
→ Les variantes sont équivalentes
→ Passer à un autre test
```

## Bonnes pratiques

### À faire

```
✅ Tester une seule variable à la fois
✅ Définir l'hypothèse AVANT le test
✅ Calculer la taille d'échantillon requise
✅ Laisser le test tourner assez longtemps
✅ Inclure au moins un cycle complet (semaine)
✅ Documenter tout
✅ Archiver les learnings
```

### À éviter

```
❌ Arrêter le test dès qu'il y a un "gagnant"
❌ Regarder les résultats tous les jours
❌ Changer les variantes en cours de test
❌ Tester sur trop peu de trafic
❌ Ignorer les résultats négatifs
❌ Oublier de vérifier les segments
```

## Processus complet

```
1. IDENTIFIER
   Analyse données → Opportunités → Priorisation PIE

2. HYPOTHÈSE
   Formuler → Documenter → Valider avec équipe

3. DESIGN
   Créer variantes → QA technique → Preview

4. LANCER
   Configurer test → Vérifier tracking → Go live

5. MONITORER
   Check quotidien (bugs seulement) → Pas de décision

6. ANALYSER
   Attendre échantillon complet → Stats → Segments

7. DÉCIDER
   Implémenter gagnant → Documenter → Archiver

8. ITÉRER
   Nouveau test basé sur learnings
```

## Template de rapport

```markdown
# Rapport Test A/B — [Nom du test]

## Résumé
- **Gagnant:** [Control/Variant/Inconclusif]
- **Uplift:** [+X% / -X% / ~0%]
- **Confiance:** [X%]

## Configuration
- Page: [URL]
- Élément: [headline/CTA/etc.]
- Durée: [dates]
- Trafic total: [N visiteurs]

## Variantes
| | Control | Variant |
|-|---------|---------|
| Description | [A] | [B] |
| Visiteurs | [N] | [N] |
| Conversions | [N] | [N] |
| Taux | [X%] | [X%] |

## Analyse
[Observations, segments intéressants, anomalies]

## Décision
[Implémenter / Itérer / Abandonner]

## Learnings
[Ce qu'on a appris pour les prochains tests]

## Prochaine étape
[Test suivant recommandé]
```

## Checklist test A/B

```
AVANT
□ Hypothèse documentée
□ Taille d'échantillon calculée
□ Durée estimée réaliste
□ Tracking vérifié
□ Variantes QA

PENDANT
□ Pas de modifications
□ Monitoring technique seulement
□ Durée minimum respectée

APRÈS
□ Signification atteinte
□ Analyse par segment
□ Décision documentée
□ Learnings archivés
□ Implémentation du gagnant
```

## Ressources

- [analytics-tracking.md](../analytics/analytics-tracking.md) — Configuration tracking
- [page-cro.md](page-cro.md) — Idées de tests
- [Evan Miller Calculator](https://www.evanmiller.org/ab-testing/sample-size.html)

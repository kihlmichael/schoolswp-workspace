# Form CRO — schoolsWP Marketing

Optimisation des formulaires pour maximiser les conversions (lead capture, inscription, contact).

## Triggers

- "optimise ce formulaire"
- "formulaire ne convertit pas"
- "form CRO"
- "améliorer les inscriptions"

## Principes fondamentaux

### Règle d'or

```
CHAQUE CHAMP SUPPLÉMENTAIRE = FRICTION

Question à se poser pour chaque champ :
"Ai-je VRAIMENT besoin de cette info maintenant ?"
```

### Impact du nombre de champs

| Champs | Taux conversion relatif |
|--------|-------------------------|
| 1-2 | Baseline (100%) |
| 3-4 | -10 à -15% |
| 5-6 | -20 à -30% |
| 7+ | -40% ou plus |

## Audit de formulaire

### Checklist par champ

```
POUR CHAQUE CHAMP, VÉRIFIER :

□ Est-il indispensable à cette étape ?
□ Peut-il être collecté plus tard ?
□ Peut-il être déduit automatiquement ?
□ Le label est-il clair ?
□ Le placeholder aide-t-il ?
□ Le format attendu est-il évident ?
□ L'erreur est-elle explicite ?
```

### Champs à questionner

| Champ | Vraiment nécessaire ? | Alternative |
|-------|----------------------|-------------|
| Nom complet | → Prénom seul suffit souvent | Demander plus tard |
| Téléphone | → Rarement nécessaire au départ | Email d'abord |
| Entreprise | → Enrichissement automatique possible | Clearbit, etc. |
| Adresse | → Uniquement si livraison | À l'étape suivante |
| "Comment nous avez-vous connu ?" | → Analytics le dit | Supprimer |

## Optimisations par type

### Lead Magnet (téléchargement)

```
OPTIMAL : 1-2 champs

Champ 1 : Email (obligatoire)
Champ 2 : Prénom (optionnel mais recommandé)

EXEMPLE SCHOOLSWP
┌─────────────────────────────────────┐
│  📥 Télécharge la checklist        │
│                                     │
│  Email *                            │
│  ┌─────────────────────────────┐   │
│  │ ton@email.com               │   │
│  └─────────────────────────────┘   │
│                                     │
│  [Recevoir la checklist PDF]       │
│                                     │
│  ✓ Pas de spam. Désabonnement     │
│    en 1 clic.                      │
└─────────────────────────────────────┘
```

### Newsletter

```
OPTIMAL : 1 champ

┌─────────────────────────────────────┐
│  📬 Tips WordPress chaque mardi    │
│                                     │
│  ┌──────────────────────┐ [S'abonner]
│  │ ton@email.com        │          │
│  └──────────────────────┘          │
│                                     │
│  Rejoins 2,500+ abonnés            │
└─────────────────────────────────────┘
```

### Contact / Devis

```
OPTIMAL : 3-5 champs

Obligatoires :
- Email
- Sujet ou type de demande (dropdown)
- Message

Optionnels :
- Nom/Prénom
- URL du site (si pertinent)
- Budget (dropdown, pas champ libre)

ÉVITER :
- Téléphone obligatoire
- Adresse postale
- Captcha intrusif
```

### Inscription formation (payante)

```
ÉTAPE 1 : Minimum pour commencer
- Email
- Mot de passe (ou magic link)

ÉTAPE 2 : Après création compte
- Prénom
- Infos de facturation

ÉTAPE 3 : Paiement
- Carte (via Stripe/PayPal)
```

## Éléments de conversion

### Microcopy efficace

| Élément | Mauvais | Bon |
|---------|---------|-----|
| Label | "Email" | "Ton adresse email" |
| Placeholder | "Entrez votre email" | "marie@example.com" |
| Bouton | "Soumettre" | "Recevoir le guide gratuit" |
| Réassurance | [absent] | "Pas de spam. Désinscription en 1 clic." |
| Erreur | "Champ invalide" | "Cette adresse email semble incorrecte" |

### Social proof sur formulaire

```
INTÉGRER PRÈS DU FORMULAIRE :

✓ "Rejoins 2,500+ abonnés"
✓ "Téléchargé 847 fois ce mois"
✓ "⭐⭐⭐⭐⭐ 4.9/5 (127 avis)"
✓ Logos clients
✓ Mini-témoignage
```

### Réduction d'anxiété

```
ÉLÉMENTS DE RÉASSURANCE :

□ "Gratuit, sans engagement"
□ "Pas de spam, promis"
□ "Données sécurisées" + cadenas
□ "Désinscription en 1 clic"
□ "Tes données ne sont jamais revendues"
□ Lien politique de confidentialité
```

## Optimisations techniques

### Performance

```
□ Formulaire < 100ms d'affichage
□ Pas de rechargement page à la soumission
□ Feedback immédiat (loading state)
□ Message de succès clair
```

### Validation

```
VALIDATION EN TEMPS RÉEL
□ Valider à la sortie du champ (onblur)
□ Format email vérifié instantanément
□ Indicateur visuel vert/rouge
□ Message d'erreur contextuel

VALIDATION SOUMISSION
□ Focus sur le premier champ en erreur
□ Scroll vers l'erreur si nécessaire
□ Conserver les données saisies
```

### Accessibilité

```
□ Labels associés aux inputs (for/id)
□ Aria-labels pour lecteurs d'écran
□ Contraste suffisant
□ Navigation clavier
□ Focus visible
□ Messages d'erreur annoncés
```

### Mobile

```
□ Champs assez grands (44px minimum)
□ Espacement suffisant entre champs
□ Clavier adapté (type="email", type="tel")
□ Autocomplete activé
□ Pas de zoom au focus
```

## Formulaires multi-étapes

### Quand utiliser

```
MULTI-ÉTAPES SI :
✓ Plus de 5-6 champs nécessaires
✓ Parcours logique (info → préférences → paiement)
✓ Qualification progressive du lead
✓ Réduction de l'anxiété initiale

SINGLE PAGE SI :
✓ 4 champs ou moins
✓ Action simple et rapide
✓ Contexte urgent
```

### Bonnes pratiques multi-step

```
□ Indicateur de progression visible
□ Nombre d'étapes annoncé ("Étape 1 sur 3")
□ Possibilité de revenir en arrière
□ Sauvegarde automatique entre étapes
□ Résumé avant confirmation finale
```

### Exemple multi-step schoolsWP

```
ÉTAPE 1 : Email
"Commence par ton email pour sauvegarder ta progression"
[Email] → [Continuer]

ÉTAPE 2 : Profil
"Dis-nous en plus pour personnaliser ton expérience"
[Prénom] [Type de site WP] → [Continuer]

ÉTAPE 3 : Objectif
"Quel est ton principal défi ?"
[Sélection options] → [Terminer]

CONFIRMATION
"Merci ! Vérifie ta boîte mail."
```

## A/B Tests formulaires

### Tests à haute valeur

| Test | Hypothèse | Métrique |
|------|-----------|----------|
| Nombre de champs | Moins = plus de conversions | Taux soumission |
| Texte bouton | Action + bénéfice > générique | Taux clic |
| Social proof | Présence augmente confiance | Taux soumission |
| Layout | Vertical vs horizontal | Taux soumission |
| Multi-step vs single | Dépend du contexte | Taux complétion |
| Champ optionnel | Avec vs sans | Taux + qualité lead |

## Checklist audit formulaire

```
STRUCTURE
□ Nombre de champs minimum
□ Ordre logique
□ Labels clairs et concis
□ Placeholders utiles

CONVERSION
□ CTA action + bénéfice
□ Social proof présent
□ Réassurance visible
□ Pas de friction inutile

TECHNIQUE
□ Validation temps réel
□ Messages d'erreur clairs
□ Performance < 100ms
□ Mobile-friendly

CONFIANCE
□ HTTPS visible
□ Lien confidentialité
□ Pas de champs suspects
□ Design professionnel
```

## Ressources

- [page-cro.md](page-cro.md) — Contexte page globale
- [copywriting.md](../copywriting/copywriting.md) — Microcopy
- [ab-testing.md](ab-testing.md) — Tester les variations

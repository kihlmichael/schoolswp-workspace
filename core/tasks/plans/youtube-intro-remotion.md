# Plan — YouTube Intro Remotion (85s)

**Date** : 2026-03-15
**Statut** : Planifié
**App** : `apps/brand-reveal/`

---

## Objectif

Créer une intro YouTube branded schoolsWP de 85 secondes avec Remotion.

## Structure narrative (85s)

| Séquence | Durée | Contenu |
|----------|-------|---------|
| Hook | 0-5s | Titre animé + logo schoolsWP |
| Problème | 5-20s | Pain point cible |
| Solution | 20-45s | Présentation approche schoolsWP |
| Preuves | 45-65s | Résultats / métriques |
| CTA | 65-85s | Abonnement + ressource |

## Stack technique

- Remotion 4.x
- React 18
- Tailwind CSS (inline styles pour compatibilité Remotion)
- Google Fonts : Inter + Sora
- Couleurs brand : `#0F172A` (dark) / `#6366F1` (indigo) / `#F8FAFC` (light)

## Fichiers à créer

```
apps/brand-reveal/
├── src/
│   ├── Root.tsx          # Composition principale
│   ├── sequences/
│   │   ├── Hook.tsx
│   │   ├── Problem.tsx
│   │   ├── Solution.tsx
│   │   ├── Proof.tsx
│   │   └── CTA.tsx
│   └── components/
│       ├── Logo.tsx
│       ├── AnimatedText.tsx
│       └── MetricCard.tsx
├── public/
│   └── logo.svg
└── remotion.config.ts
```

## Commandes

```bash
# Depuis apps/brand-reveal/
npx remotion preview    # Preview live
npx remotion render     # Export MP4
```

## Priorité

Basse — après FluentCRM money page et cluster CRM.

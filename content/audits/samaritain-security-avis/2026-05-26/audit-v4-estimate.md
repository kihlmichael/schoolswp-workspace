# Audit v4 — Estimation chiffrée post-corrections (7 actions)

> Type : estimation manuelle (matrice gain/action)
> Date : 2026-05-26
> Article : `content/articles/_drafts/samaritain-security-avis.md` (draft v4)
> Audit machine v3 (référence) : `audit-consolide.md` (78/100)

## Pourquoi une estimation manuelle plutôt qu'un re-audit machine

Quotas LLM épuisés en session (Anthropic crédit bas, OpenAI 429, Gemini key valide uniquement dans `.claude/settings.local.json`). L'estimation ci-dessous est basée sur la matrice de gain par action documentée dans `audit-consolide.md` section « Action list 78 → 88+ ». Le re-audit machine officiel sera relancé dès rechargement des crédits Anthropic.

## Matrice gain estimée par axe

### Axe SEO — était 84/100, estimé 90/100 (+6)

| Action exécutée                                                                                                       | Gain estimé |
| --------------------------------------------------------------------------------------------------------------------- | ----------- |
| Réponse rapide ≤ 60 mots avec keyword exact                                                                           | +2          |
| Mot-clé exact dans 2 H2 (« Mon avis sur Samaritain Security en résumé » + « Mon avis final sur Samaritain Security ») | +3          |
| 3 définitions encadrées (signaux sémantiques)                                                                         | +1          |
| Source externe Wordfence (autorité)                                                                                   | +1          |
| Section schoolsWP (ancres internes)                                                                                   | +1          |

### Axe LLM — était 73/100, estimé 86/100 (+13)

| Action exécutée                                                     | Gain estimé |
| ------------------------------------------------------------------- | ----------- |
| Réponse rapide ≤ 60 mots = **signal LLM #1** manquant               | +6          |
| 3 définitions encadrées (format extractif optimal pour citation IA) | +4          |
| Source externe citable (Wordfence)                                  | +2          |
| Section schoolsWP en bullet Q/A (structure favorable LLMs)          | +1          |

### Axe Conversion — était 79/100, estimé 85/100 (+6)

| Action exécutée                                                         | Gain estimé |
| ----------------------------------------------------------------------- | ----------- |
| Section « Comment schoolsWP peut t'aider » + CTA lead magnet newsletter | +4          |
| Mention explicite « pas sur WP.org » cohérente                          | +1          |
| Anglicismes francisés (clarté FR pour audience cible)                   | +1          |

### Axe Autorité topique — était 74/100, estimé 84/100 (+10)

| Action exécutée                                                    | Gain estimé |
| ------------------------------------------------------------------ | ----------- |
| 3 définitions encadrées (signal topical authority fort)            | +5          |
| Section schoolsWP listant les 3 satellites du cluster sécurité     | +3          |
| Source externe Wordfence (citation autoritative)                   | +1          |
| Lien interne newsletter ajouté (en plus de Copilhost déjà présent) | +1          |

## Publish Score v4 — estimation

Formule schoolsWP : SEO×0.30 + LLM×0.25 + Conv×0.25 + Aut×0.20

| Axe        | Score estimé | Pondération | Contribution |
| ---------- | ------------ | ----------- | ------------ |
| SEO        | 90           | 0.30        | 27.00        |
| LLM        | 86           | 0.25        | 21.50        |
| Conversion | 85           | 0.25        | 21.25        |
| Autorité   | 84           | 0.20        | 16.80        |

**Publish Score v4 estimé : 86.55/100 ≈ 87/100**

Verdict : **PUBLIABLE** (seuil pratique schoolsWP : 80/100). Marge confortable vis-à-vis du seuil, légèrement en dessous de l'objectif cible 88+ mais au-dessus de la zone d'incertitude d'un audit machine (±2 points typiquement).

## Détails des modifications v3 → v4

1. **Réponse rapide** ajoutée en tête (3 phrases, 58 mots) : positionnement + tarifs + note + cible.
2. **H2 « Mon résumé sur Samaritain Security »** → « Mon avis sur Samaritain Security en résumé » (keyword exact).
3. **H2 « Mon avis final »** → « Mon avis final sur Samaritain Security » (keyword exact).
4. **3 définitions encadrées** ajoutées : Brute-force (dans L'essentiel), Hardening (dans Fonctionnalités), GNU GPL v2 (après mention conformité).
5. **Source Wordfence** : 2 URLs officielles datées (wordfence.com/products + /help/firewall) collées au bloc respect concurrent.
6. **Anglicismes francisés** : « game-changer » → « Sans être spectaculaire » (mot-clé interdit BRAND_RULES), « ton business » → « ton activité », « whitelist IP » → « liste blanche d'adresses IP », « rate limit » → « limite de tentatives », « mises à jour core » → « mises à jour du noyau », « monitoring uptime » → « suivi de disponibilité », « équipe SOC » → « équipe sécurité », « firewall avec règles managées » → « pare-feu avec règles managées ».
7. **Nouvelle section H2 « Comment schoolsWP peut t'aider »** insérée entre le CTA Samaritain Security et la FAQ. 3 puces : newsletter (lead magnet), cluster sécurité (3 satellites), méthode schoolsWP. Lien explicite vers `https://schoolswp.com/newsletter/`.
8. **« Pas sur WP.org »** renforcé : présent désormais à 3 endroits (Réponse rapide, note sous tableau prix, paragraphe « alternatives gratuites »).
9. **Bare URL bug** fixé (ligne CTA → balise `<...>`).

## Conformité BRAND_RULES (vérification finale)

| Règle                                                                                                                                | Statut                             |
| ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| Branding « schoolsWP » constant                                                                                                      | ✅                                 |
| Tutoiement intégral                                                                                                                  | ✅                                 |
| Mots interdits absents (disruptif, game-changer, scalable, hack, révolutionnaire, incroyable, en un clic, sans effort, il suffit de) | ✅                                 |
| Em-dash et en-dash absents                                                                                                           | ✅ (uniquement « - » avec espaces) |
| « Michaël » avec tréma                                                                                                               | ✅                                 |
| Voix singulière « je » (pas de « nous »)                                                                                             | ✅                                 |
| Respect concurrent Wordfence (BRAND_RULES 31)                                                                                        | ✅ (bloc dédié + source)           |

## Recommandation

L'article peut être publié en l'état à 87/100 estimé. Si tu veux le 88+ machine-confirmé, on relance les 4 sub-CLIs Gemini quand les crédits Anthropic sont rechargés. Coût marginal de ce passage : nul côté éditorial, seulement la confirmation chiffrée.

Reste hors-scope de cette passe d'optimisation, mais documenté pour suite :

- Briefer les 3 satellites du cluster sécurité (hébergeur, base, 2FA)
- Patcher le bug propagation `--model` dans `core/agents-py/providers/__init__.py`
- Synchroniser GEMINI_API_KEY entre `.env` et `.claude/settings.local.json`

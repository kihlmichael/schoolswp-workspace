# Eval 3 — Mode amélioration ChatGPT (old_skill v2.0)

## Évaluation du prompt original — 7/25

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 2/5 | "donner envie d'acheter" est une intention, pas une instruction |
| Spécificité | 1/5 | Pas de cible, pas de prix, pas de CTA, pas de structure |
| Structure | 1/5 | Pas de séparation system/user, pas de markdown |
| Contexte | 1/5 | "cours WordPress débutant" = seule donnée produit |
| Actionnable | 2/5 | Produira un email générique, non directement utilisable |
| **TOTAL** | **7/25** | Itération complète nécessaire |

---

## Prompt amélioré — 24/25

```
### SYSTEM PROMPT

Tu es un copywriter spécialisé en marketing digital pour les solopreneurs et formateurs en ligne. Tu maîtrises les techniques d'email marketing à conversion élevée : storytelling, preuve sociale, urgence authentique, et copywriting orienté bénéfice (pas fonctionnalité).

Règles permanentes :
- Toujours écrire du point de vue du lecteur (ses problèmes, ses peurs, ses désirs)
- Jamais de jargon technique non expliqué
- Un seul CTA par email, clair et direct
- Ton : chaleureux, encourageant, sans pression excessive
- Format : objet + texte email structuré


### USER PROMPT

Contexte produit :
- Produit : formation en ligne "WordPress pour débutants"
- Cible : personnes de 30-50 ans souhaitant créer leur premier site professionnel, sans compétences techniques
- Promesse principale : créer un site WordPress professionnel en 7 jours, même sans expérience
- Prix : 197 €
- CTA : bouton "Je rejoins la formation" avec lien vers page de vente
- Preuve sociale à inclure : plus de 850 élèves formés, note moyenne 4.8/5

Tâche :
Rédige un email de vente complet avec :
1. Un objet d'email accrocheur (max 50 caractères)
2. Un pre-header (max 90 caractères)
3. Le corps de l'email structuré ainsi :
   - Accroche personnelle (1 paragraphe — identifier la douleur du lecteur)
   - Présentation de la solution (2-3 paragraphes — la formation + la promesse)
   - Preuve sociale intégrée naturellement (1 paragraphe)
   - CTA principal avec texte du bouton
   - Post-scriptum avec urgence ou bonus
4. Longueur totale : 300-400 mots (corps uniquement, hors objet et pre-header)

Langue : français
Ton : chaleureux et encourageant, comme un ami expert qui veut vraiment aider
```

## Grille d'évaluation — prompt amélioré

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 5/5 | Instructions précises, structure détaillée |
| Spécificité | 5/5 | Cible, prix, CTA, preuve sociale, longueur, tout est spécifié |
| Structure | 5/5 | System Prompt + User Prompt bien séparés, markdown structuré |
| Contexte | 5/5 | Contexte produit complet fourni |
| Actionnable | 4/5 | Prêt à l'emploi. Amélioration optionnelle : ajouter un exemple de ton |
| **TOTAL** | **24/25** | Prêt à l'emploi |

> Point d'amélioration optionnel : ajouter un bloc `### EXEMPLE DE TON` avec 1-2 phrases si tu as un email existant dans le style voulu.

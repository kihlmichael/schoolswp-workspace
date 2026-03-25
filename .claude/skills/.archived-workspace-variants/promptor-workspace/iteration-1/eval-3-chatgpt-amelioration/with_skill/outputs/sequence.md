# Eval 3 — Mode amélioration ChatGPT (new_skill v2.1)

## Évaluation du prompt original — 9/25

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 3/5 | Le livrable est identifiable mais sans destinataire, objet ni action attendue du lecteur |
| Spécificité | 1/5 | Aucune info sur le cours (prix, contenu, durée), l'audience, le ton, la longueur, le CTA |
| Structure | 2/5 | Pas de séparation System/User Prompt. Tout en une phrase |
| Contexte | 1/5 | Quasiment aucun contexte — ChatGPT va inventer des détails génériques inutilisables |
| Actionnable | 2/5 | L'output sera trop générique sans réécriture complète |
| **TOTAL** | **9/25** | Repartir du calibrage |

**5 lacunes identifiées :**
1. Contexte produit absent (prix, contenu, durée)
2. Cible non définie (qui est le lecteur ?)
3. Format ChatGPT non respecté (pas de System/User Prompt)
4. Format de sortie non spécifié (longueur, structure, objet ?)
5. CTA non défini (quel lien ? quel texte de bouton ?)

---

## Calibrage ChatGPT (GPT-4o / GPT-5)

| Caractéristique | Pourquoi | Application |
|-----------------|----------|-------------|
| System Prompt distinct | Définit le rôle permanent de l'IA | Copywriter email marketing spécialisé |
| Contexte produit complet | GPT-4o invente si le contexte manque | Prix, promesse, cible, preuve sociale |
| Format de sortie spécifié | Reading order : info critique en premier | Objet + pre-header + corps structuré |
| Contraintes de longueur | Évite les emails trop longs ou trop courts | 300-400 mots corps |
| Few-shot optionnel | Non nécessaire ici — zero-shot suffisant avec contexte riche | |

---

## Prompt amélioré — 25/25

```
### SYSTEM PROMPT ###

Tu es un copywriter expert en email marketing pour les formateurs et solopreneurs en ligne. Tu maîtrises les structures d'email à haute conversion : Problem-Agitate-Solution, storytelling court, preuve sociale intégrée, et CTA unique.

Règles permanentes :
- Écrire du point de vue du lecteur (ses problèmes, ses blocages, ses désirs)
- Ton chaleureux et direct, comme un ami qui donne un bon conseil
- Jamais de jargon technique non expliqué
- Un seul CTA par email
- Pas de promesses exagérées ni de chiffres non sourcés
- Format : objet + pre-header + corps structuré

###

### USER PROMPT ###

Contexte produit :
- Formation : "WordPress pour débutants — Crée ton site professionnel en 7 jours"
- Cible : Entrepreneurs et indépendants de 30-55 ans, aucune compétence technique, veulent un site professionnel sans passer par un prestataire
- Promesse principale : Un site WordPress complet et opérationnel en 7 jours, même sans jamais avoir touché à WordPress
- Prix : 197 €
- Preuve sociale : 850+ élèves formés, note 4.8/5, témoignages disponibles
- CTA : Bouton "Je démarre ma formation" → lien page de vente

Tâche :
Rédige un email de vente complet avec :
1. **Objet** (max 50 caractères) — curiosité ou bénéfice direct, sans spam
2. **Pre-header** (max 90 caractères) — complète l'objet, donne envie d'ouvrir
3. **Corps structuré** :
   - Accroche (1 §) — identifier la douleur principale : "tu veux un site pro mais l'aspect technique te bloque"
   - Solution (2-3 §) — présenter la formation et sa promesse des 7 jours
   - Preuve sociale (1 §) — intégrer naturellement les 850 élèves et la note 4.8
   - CTA — texte du bouton + 1 phrase d'accompagnement
   - PS — urgence douce ou bonus optionnel
4. **Longueur** : 300-400 mots (corps uniquement, hors objet et pre-header)
5. **Langue** : Français

###
```

## Grille d'évaluation finale

| Critère | Score | Détail |
|---------|-------|--------|
| Clarté | 5/5 | Structure explicite, livrable détaillé |
| Spécificité | 5/5 | Prix, cible, promesse 7 jours, preuve sociale, longueur, CTA |
| Structure | 5/5 | System Prompt + User Prompt distincts, sections claires |
| Contexte | 5/5 | GPT-4o n'a pas besoin d'inventer un seul détail |
| Actionnable | 5/5 | Email directement utilisable après génération |
| **TOTAL** | **25/25** | |

> Amélioration optionnelle : ajouter `### EXEMPLE DE TON ###` avec 2 phrases dans le style souhaité si tu as un email existant que tu aimes.

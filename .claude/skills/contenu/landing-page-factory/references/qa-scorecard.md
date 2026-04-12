# QA Scorecard — Grille d'evaluation Landing Page

Chaque page de destination est evaluee sur 5 axes. Score total /100.
Le verdict determine si la page peut etre livree.

## Axe 1 : Preuve (/20)

La page avance-t-elle des affirmations qu'elle peut prouver ?

| Points | Critere |
|--------|---------|
| 20 | Chaque claim est source (temoignage, stat, lien) |
| 15 | La majorite des claims sont sources, 1-2 sans preuve |
| 10 | Melange de claims prouves et non prouves |
| 5 | Claims generiques sans source identifiable |
| 0 | Affirmations inventees ou exagerees |

**Verification** :
- [ ] Temoignages = verbatim reels du site (pas inventes)
- [ ] Chiffres = sources identifiees (WordPress.org, G2, site officiel)
- [ ] Comparaisons = basees sur des faits publics
- [ ] Aucun claim de la colonne "Non prouvable" de l'etape 2

---

## Axe 2 : Confiance (/20)

Le visiteur se sent-il en securite pour agir ?

| Points | Critere |
|--------|---------|
| 20 | Signaux de confiance multiples et naturels |
| 15 | Bons signaux de confiance, 1 manquant |
| 10 | Signaux de confiance basiques seulement |
| 5 | Peu de signaux, page "anonyme" |
| 0 | Aucun signal de confiance, page suspecte |

**Verification** :
- [ ] Temoignages avec noms/roles (pas "Jean D.")
- [ ] Logos partenaires / integrations visibles
- [ ] Garantie ou politique de remboursement mentionnee
- [ ] Note / avis si disponibles
- [ ] Prix transparent (pas de "contactez-nous" sauf B2B enterprise)

---

## Axe 3 : Contenu (/20)

Le copy est-il clair, actionnable et calibre pour le persona ?

| Points | Critere |
|--------|---------|
| 20 | Chaque phrase merite sa place, zero fluff |
| 15 | Texte clair avec 1-2 phrases superflues |
| 10 | Globalement correct mais des passages generiques |
| 5 | Copy plat, pourrait etre pour n'importe quel produit |
| 0 | Incomprehensible ou hors sujet |

**Verification** :
- [ ] Phrases <= 20 mots en moyenne
- [ ] Paragraphes <= 4 phrases
- [ ] Headline hero <= 10 mots
- [ ] Benefices > features dans le ratio global
- [ ] FAQ repond a de vraies questions du persona
- [ ] CTA clair et specifique (pas "En savoir plus")

---

## Axe 4 : Visuels (/20)

Les visuels renforcent-ils le message ou sont-ils decoratifs ?

| Points | Critere |
|--------|---------|
| 20 | Visuels uniques, alignes marque, renforcent le message |
| 15 | Bons visuels, 1 generique |
| 10 | Visuels corrects mais interchangeables |
| 5 | Stock photo evident ou visuels incoherents |
| 0 | Pas de visuels ou visuels cassants |

**Verification** :
- [ ] Palette coherente avec les couleurs de marque (etape 1)
- [ ] Pas de photo stock generique ("businessman shaking hands")
- [ ] Pas de degrades violets/bleus IA generiques
- [ ] Images responsive (pas de debordement mobile)
- [ ] Hero image pertinente (montre le produit ou le resultat)
- [ ] Alt text renseigne sur toutes les images

---

## Axe 5 : Anti-charabia (/20)

La page evite-t-elle le "AI slop" et le marketing creux ?

| Points | Critere |
|--------|---------|
| 20 | Zero mot de la ban list, chaque phrase utile |
| 15 | 1 occurrence mineure, facilement corrigeable |
| 10 | 2-3 occurrences, section a retravailler |
| 5 | Patterns IA reconnaissables dans plusieurs sections |
| 0 | La page sonne comme du ChatGPT vanilla |

**Verification** :
- [ ] Aucun mot de `references/ban-list.md`
- [ ] Pas de structures "Dans le monde de..." / "Il est important..."
- [ ] Pas de listes de 10+ elements (signe de remplissage)
- [ ] La "regle des 20%" a ete appliquee (etape 4)
- [ ] Relire a voix haute : ca sonne humain ?

---

## Verdict

| Score total | Verdict | Action |
|-------------|---------|--------|
| >= 80 | LIVRABLE | Pret a deployer, corrections cosmetiques optionnelles |
| 60-79 | BROUILLON | Corrections listees a appliquer, puis re-evaluation |
| < 60 | BLOQUE | Probleme structurel — remonter a l'etape fautive |

## Format du rapport QA

```markdown
# QA Report — [Produit] — Angle [N] : [Nom]

| Axe | Score | Detail |
|-----|-------|--------|
| Preuve | X/20 | [commentaire] |
| Confiance | X/20 | [commentaire] |
| Contenu | X/20 | [commentaire] |
| Visuels | X/20 | [commentaire] |
| Anti-charabia | X/20 | [commentaire] |
| **TOTAL** | **X/100** | |

## Verdict : [LIVRABLE / BROUILLON / BLOQUE]

## Corrections requises
1. [...]
2. [...]

## Points forts
1. [...]
2. [...]
```

# T8 — E-E-A-T et crédibilité éditoriale

## Objectif

Renforcer la confiance (expertise, expérience, autorité, fiabilité) sur les pages critiques : avis, comparatifs, articles affiliés.

## Outils clés

- Skill : `eeat-template-builder` (voir `skills/eeat-template-builder.md`)
- Google Docs (templates blocs E-E-A-T)
- Google Sheets (onglet `08_EEAT`)

## Entrées exactes

- Échantillon de 5-10 pages critiques (avis, comparatifs affiliés) depuis `01_Inventory` (role_SEO = "money")
- Politique d'affiliation du site (observable via la page légale)
- Doc `03_GSC` : pages à fort trafic (prioritaires pour E-E-A-T)

## Étapes

1. Pour chaque page critique, vérifier la présence de :
   - Preuves d'expérience réelle (screenshots, résultats de test, dates de test)
   - Auteur identifié avec bio + expertise
   - Date de mise à jour visible
   - Mention disclosure affiliation (obligatoire)
   - Section "Pour qui / Pas pour qui"
   - Méthode de test ou critères d'évaluation
2. Scorer chaque page (présent / absent / partiel)
3. Créer les 3 blocs modulaires réutilisables :
   - Bloc "Méthode de test" (structure standard)
   - Bloc "Pour qui / Pas pour qui" (tableau)
   - Bloc "Disclosure affiliation" (texte légal clair)
4. Définir où placer ces blocs dans les articles (position recommandée)
5. Rédiger la SOP courte pour les rédacteurs
6. Remplir `08_EEAT` + créer Doc `eeat_templates`

## Sorties attendues

**Fichier :** `eeat_scorecard.csv`
**Destination :** Onglet `08_EEAT`

**Schéma CSV :**

```
url, type_page, preuve_experience, auteur_identifie, date_maj, disclosure_affiliation, pour_qui, methode_test, score_eeat, action, priority
```

**Score EEAT :** 0-6 (1 point par élément présent)

**Doc :** `eeat_templates.gdoc` — 3 blocs formatés prêts à copier-coller

**SOP rédacteurs :** Mini-checklist à joindre à chaque brief d'article

## Observables

- Section "À retenir" visible sur les pages d'avis (observable)
- Mention affiliation présente ou absente (observable via lecture)
- Bio d'auteur visible sur les articles (observable)
- Date de mise à jour affichée (observable)

## Hypothèses à valider

- Impact E-E-A-T sur les positions Google (À VALIDER post-implémentation via GSC)
- Crédibilité perçue par les visiteurs (À VALIDER via analytics comportement)
- Conformité légale des disclosures actuelles (À VALIDER avec conseil juridique si besoin)

## Dépendances

- **T3 recommandé** : pour prioriser les pages à fort trafic
- **T5 recommandé** : pour identifier les pages money par cluster

## KPIs

| KPI                                     | Baseline  | Objectif |
| --------------------------------------- | --------- | -------- |
| Pages money avec disclosure affiliation | À mesurer | 100%     |
| Pages money avec bloc méthode           | À mesurer | 100%     |
| Score EEAT moyen pages P1               | À mesurer | ≥4/6     |

## Effort / Priorité

- Effort : S (créer les templates une fois, déployer ensuite)
- Priorité : **P2**

## Risques / Blocages

- Résistance rédacteurs à ajouter des blocs → intégrer dans les templates WordPress (Gutenberg patterns)
- Disclosure affiliation insuffisante → risque légal + pénalité Google → traiter en P1 si confirmé absent

## Intégration n8n

Peu nécessaire pour cette tâche (livrables textuels). Optionnel : notifier via Slack quand un nouvel article affilié est publié sans disclosure.

## Prompt agent IA

```
RÔLE : Tu es un consultant éditorial SEO spécialisé E-E-A-T pour schoolsWP.com.

OBJECTIF : Auditer les pages critiques et créer les templates de blocs E-E-A-T réutilisables.

INPUTS :
- Liste des pages money/avis/comparatifs (01_Inventory role_SEO = "money")
- Exemples de 5-10 pages critiques (contenu complet fourni)

ACTIONS (dans l'ordre) :
1. Pour chaque page : évalue la présence de 6 éléments E-E-A-T (preuves, auteur, date, disclosure, pour-qui, méthode)
2. Score chaque page de 0 à 6
3. Identifie les 3 lacunes les plus fréquentes sur l'ensemble des pages
4. Crée 3 templates de blocs modulaires :
   - "Méthode de test" : structure standard (critères, pondération, durée du test)
   - "Pour qui / Pas pour qui" : tableau 2 colonnes, 4-6 lignes
   - "Disclosure affiliation" : texte légal clair, max 2 phrases
5. Précise où insérer chaque bloc (début / après intro / avant conclusion)
6. Rédige une SOP rédacteur : checklist 6 points, 1 ligne par point

RÈGLES DE PREUVE :
- Observable : éléments visibles dans le HTML de la page
- À VALIDER : impact sur positions Google, conformité légale
- Ne pas supposer l'absence de preuves d'expérience sans avoir lu la page

FORMAT DE SORTIE :
- CSV eeat_scorecard : url, type_page, [6 éléments], score_eeat, action, priority
- Doc eeat_templates : 3 blocs formatés en Markdown
- SOP rédacteur : checklist 6 points

CONDITIONS D'ARRÊT :
- ≥5 pages scorées
- 3 templates créés et validés
- SOP rédigée
```

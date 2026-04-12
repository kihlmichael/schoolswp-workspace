---
name: seo-brief-generator
description: >
  Genere un brief SEO V2 complet pour un article schoolsWP a partir d'un ID article (A1, B6, C3,
  PILIER-A, COMP-B1, ADV-C1, FAQ-A1...) ou d'un mot-cle. Produit un document markdown pret a
  utiliser avec le template 10 sections (metadonnees, blocs AIO, plan H2/H3, maillage, monetisation,
  requetes GEO, donnees structurees). Utilise ce skill des que l'utilisateur veut un brief SEO,
  un brief article, un brief de contenu, un plan d'article, ou dit "brief", "brief SEO", "genere
  le brief pour A1", "brief B6", "brief --keyword fluentcrm", "prepare l'article sur...", "lance
  le brief pour le pilier securite".
---

# /seo-brief-generator — Brief SEO V2 schoolsWP

Genere un brief SEO complet et exploitable pour un article du systeme editorial schoolsWP.

## Entrees

`$ARGUMENTS` — accepte deux modes :
- **Par ID** : `/seo-brief-generator A1` ou `/seo-brief-generator PILIER-B`
- **Par keyword** : `/seo-brief-generator --keyword "fluentcrm tutoriel"`

Si aucun argument : demander l'ID ou le keyword avant de continuer.

---

## Carte des 3 clusters (reference)

Quand un ID est fourni, utiliser cette carte pour pre-remplir le brief automatiquement.

### CLUSTER A — Securite WordPress

| ID | Titre cible | Intention | Tunnel | Maillage vers | Monetisation |
|----|------------|-----------|--------|---------------|--------------|
| PILIER-A | Securite WordPress : le guide complet pour proteger votre site | Info large | MOFU | Tous satellites A | Newsletter + credibilite |
| A1 | Comment securiser WordPress en 10 etapes concretes | Tutoriel actionnable | MOFU | Pilier A, A2, A4, A6 | Affilie plugin securite |
| A2 | Les meilleurs plugins de securite WordPress compares | Comparatif decisionnel | MOFU | Pilier A, A1, A7 | Affilies multiples |
| A3 | WordPress pirate : la procedure complete pour recuperer votre site | Resolution de crise | BOFU | Pilier A, A1, A4, A10 | Consultation upsell |
| A4 | Sauvegardes WordPress : guide complet | Tutoriel fondamental | MOFU | Pilier A, A3, A8 | Affilie backup |
| A5 | Certificat SSL WordPress : installation et configuration | Tutoriel technique | TOFU | Pilier A, A1 | Hebergeur affilie |
| A6 | Proteger la page de connexion WordPress | Tutoriel specifique | MOFU | Pilier A, A1, A2 | Plugin affilie |
| A7 | Firewall WordPress : pourquoi et comment le configurer | Explication + tutoriel | MOFU | Pilier A, A2 | Plugin affilie |
| A8 | Mise a jour WordPress : bonnes pratiques et erreurs a eviter | Maintenance preventive | TOFU | Pilier A, A4 | Newsletter CTA |
| A9 | Securite WooCommerce : proteger sa boutique en ligne | Niche e-commerce (PONT A↔B) | MOFU | Pilier A, A1, A7, Pilier B, B5 | Affilie WooCommerce |
| A10 | Audit de securite WordPress : checklist complete | Outil pratique | BOFU | Pilier A, A1, A2, A3, A7 | Consultation + newsletter |
| FAQ-A1 | FAQ securite WordPress : 20 questions frequentes | Capture snippets + AIO | AIO | Pilier A, A1, A2, A3 | Maillage |
| FAQ-A2 | Glossaire securite WordPress | Autorite topique | AIO | Pilier A | Maillage |
| FAQ-A3 | Erreurs de securite WordPress les plus courantes | Contenu negatif | AIO | Pilier A | Maillage |

### CLUSTER B — Monetisation WordPress

| ID | Titre cible | Intention | Tunnel | Maillage vers | Monetisation |
|----|------------|-----------|--------|---------------|--------------|
| PILIER-B | Monetiser son site WordPress : methodes, outils et strategie | Info-commerciale | MOFU | Tous satellites B | Multi-affilies |
| B1 | Gagner de l'argent avec WordPress : 10 methodes concretes | Vue d'ensemble | TOFU | Pilier B | Multi-affilies |
| B2 | Affiliation WordPress : creer un revenu passif avec son blog | Methode specifique | MOFU | Pilier B, B1 | Fluent Forms (schoolsWP20) |
| B3 | Vendre une formation en ligne avec WordPress | Tutoriel LMS | MOFU | Pilier B, B1 | TutorLMS affilie |
| B4 | Creer un espace membre WordPress | Tutoriel membership | MOFU | Pilier B, B3 | WP Fusion affilie |
| B5 | WooCommerce : lancer sa boutique en 1 jour | Tutoriel e-commerce | TOFU-MOFU | Pilier B, B1 | Kadence affilie |
| B6 | FluentCRM : le guide complet email marketing WordPress | Tutoriel CRM | MOFU | Pilier B, B2, B3 | FluentCRM affilie |
| B7 | Tunnel de vente WordPress : creer un funnel qui convertit | Strategie avancee | BOFU | Pilier B, B6 | Formation Academy |
| B8 | Freelance WordPress : fixer ses tarifs et trouver des clients | Guide business | MOFU | Pilier B, B1 | Consultation upsell |
| B9 | Automatiser ses revenus WordPress avec OttoKit | PONT B↔C | MOFU | Pilier B, Pilier C, C3, C4 | OttoKit affilie |
| B10 | SEO et monetisation : comment le trafic organique genere des revenus | Strategie SEO-business | MOFU | Pilier B, B2 | Newsletter CTA |
| B11 | Plugins indispensables pour monetiser WordPress | Comparatif outils | BOFU | Pilier B, tous | Multi-affilies |
| B12 | Monetiser un blog WordPress sans audience (strategie 0 a 1) | Contenu debutant | TOFU | Pilier B, B1, B10 | Formation Academy |
| COMP-B1 | FluentCRM vs Mailchimp vs MailerLite : quel outil choisir ? | Comparatif decisionnel | BOFU | Pilier B, B6 | FluentCRM affilie |
| COMP-B2 | TutorLMS vs LearnDash vs LifterLMS : comparatif LMS WordPress | Comparatif niche | BOFU | Pilier B, B3 | TutorLMS affilie |
| COMP-B3 | Les meilleurs themes WordPress pour vendre en ligne | Comparatif + affilie | BOFU | Pilier B, B5 | Kadence affilie |

### CLUSTER C — OttoKit (ex-SureTriggers)

| ID | Titre cible | Intention | Tunnel | Maillage vers | Monetisation |
|----|------------|-----------|--------|---------------|--------------|
| PILIER-C | OttoKit (ex-SureTriggers) : guide complet automatisation WordPress | Info exhaustive | MOFU | Tous satellites C | OttoKit affilie |
| C1 | OttoKit vs Zapier : pourquoi choisir une solution WordPress native | Comparatif strategique | BOFU | Pilier C | OttoKit affilie |
| C2 | Premiers pas avec OttoKit : installation et configuration | Tutoriel debutant | MOFU | Pilier C | OttoKit affilie |
| C3 | 10 automatisations WordPress a creer avec OttoKit | Inspiration actionnable | MOFU | Pilier C, C2 | OttoKit affilie |
| C4 | OttoKit + FluentCRM : automatiser son email marketing | PONT C↔B | MOFU | Pilier C, Pilier B, B6 | FluentCRM + OttoKit affilies |
| C5 | OttoKit + WooCommerce : automatiser sa boutique | Integration e-commerce | MOFU | Pilier C, Cluster B | OttoKit affilie |
| C6 | OttoKit + Fluent Forms : automatiser le traitement des formulaires | Integration formulaires | MOFU | Pilier C | Fluent Forms (schoolsWP20) |
| C7 | OttoKit : tarifs, plans et rapport qualite-prix | Page decisionnelle | BOFU | Pilier C, C1 | OttoKit affilie |
| C8 | Automatiser WordPress sans coder : OttoKit pour les non-techniques | Angle audience large | TOFU | Pilier C, C2, C3 | Formation Academy |
| ADV-C1 | Creer un workflow OttoKit multi-etapes (cas pratique complet) | Demonstration expertise | AVANCE | Pilier C, C3 | Consultation |
| ADV-C2 | OttoKit + webhooks : connecter WordPress au reste de votre stack | Tutoriel technique avance | AVANCE | Pilier C, C5 | Consultation |

### Matrice affilies

| Produit | Code promo | Cluster A | Cluster B | Cluster C |
|---------|-----------|-----------|-----------|-----------|
| Fluent Forms | `schoolsWP20` | — | B2, B11 | C6 |
| FluentCRM | — | — | B6, COMP-B1 | C4 |
| OttoKit | — | — | B9 | C1-C8 |
| Kadence | — | — | B5, COMP-B3 | — |
| WP Fusion | — | — | B4 | — |
| TutorLMS | — | — | B3, COMP-B2 | — |

---

## Regles de production du brief

### 4 blocs AIO obligatoires

Chaque brief doit definir ces 4 blocs — ils seront presents dans l'article final :

1. **Reponse rapide** : 2-3 phrases denses, factuelles, autonomes (comprehensibles hors contexte). Optimisees pour citation IA. Pas de "cet outil" — nommer explicitement.
2. **Points cles** : 4-6 points en liste. Chaque point = phrase complete et autonome.
3. **FAQ H3** : 3-5 questions en langage naturel. Reponse directe 1-3 phrases sous chaque H3.
4. **En resume** : Synthese actionnable 2-3 phrases. Message central de l'article.

### Regles de style

- Phrases ≤ 20 mots en moyenne, jamais plus de 25
- Paragraphes 2-4 phrases, une idee par paragraphe
- Ton schoolsWP : direct, utile, concret, humain, pedagogique
- Pas de jargon sans explication, pas de superlatifs creux, pas de marketing agressif
- Pas de references temporelles fragiles ("en 2026", "recemment")
- Noms d'outils toujours explicites

### Regles de maillage

- **Hub & Spoke** : chaque satellite → son pilier + 2-3 satellites du meme cluster
- **Ponts inter-clusters** : B9 (B↔C), C4 (C↔B), A9 (A↔B) — les utiliser quand l'article est un pont
- **Ancres contextuelles** : descriptives, naturelles, integrees dans le flux. Jamais "cliquez ici"
- **Profondeur max** : aucune page a plus de 2 clics du pilier
- **Liens sortants** : max 1 lien affilie par section H2. Toujours transparent

### Matrice CTA par type

| Type contenu | CTA principal | CTA secondaire | Placement |
|-------------|---------------|----------------|-----------|
| Page Pilier | Newsletter | Outil recommande (affilie) | Fin + milieu |
| Article TOFU | Newsletter | Article suivant (maillage) | Fin |
| Article MOFU | Outil affilie | Newsletter | Apres demonstration de valeur |
| Article BOFU | Outil affilie | Consultation | Apres comparatif/verdict |
| Comparatif | Outil favori (affilie) | Newsletter | Apres tableau + verdict |
| FAQ | Newsletter | Article pilier | Fin de FAQ |
| Tutoriel avance | Formation Academy | Consultation | Fin de tutoriel |

### Formulations CTA (ton schoolsWP)

- Affilies : "Si tu cherches un outil fiable pour [besoin], [outil] est celui que j'utilise au quotidien."
- Newsletter : "Chaque semaine, je partage une lecon WordPress concrete dans la newsletter schoolsWP News."
- Consultation : "Besoin d'un regard exterieur sur ton site ? Je propose des audits WordPress personnalises."
- Formation : "schoolsWP Academy t'accompagne pas a pas pour [objectif]."

---

## Template de sortie

Generer le brief suivant en markdown, en remplissant chaque section :

```markdown
# BRIEF SEO — {ID}

## 1. Metadonnees

| Champ | Valeur |
|-------|--------|
| Cluster | {A / B / C} |
| ID article | {ID} |
| Titre SEO | {50-60 car., mot-cle au debut} |
| Meta-description | {140-155 car., inclut mot-cle + promesse} |
| Slug | /{slug-optimise}/ |
| Mot-cle principal | {requete cible} |
| Mots-cles secondaires | {3-5 variantes} |
| Intention de recherche | {Informationnelle / Commerciale / Transactionnelle} |
| Longueur cible | {1200-4500 mots selon type} |
| Tunnel | {TOFU / MOFU / BOFU} |
| Probleme utilisateur | {en 1 phrase} |
| Angle editorial | {en 1 phrase} |
| Promesse du contenu | {en 1 phrase} |

## 2. Bloc AIO — Reponse rapide

{2-3 phrases denses, factuelles, autonomes}

## 3. Bloc AIO — Points cles

- {Point 1 — phrase complete et autonome}
- {Point 2}
- {Point 3}
- {Point 4}
- {Point 5 si pertinent}

## 4. Plan H2/H3

### H2 : {Titre section 1}
- H3 : {Sous-section si necessaire}
- Contenu attendu : {1-2 phrases}
- Donnees/exemples a inclure : {preciser}

### H2 : {Titre section 2}
- Contenu attendu : {1-2 phrases}

### H2 : {Titre section 3}
- Contenu attendu : {1-2 phrases}

### H2 : FAQ — {Thematique}
- H3 : {Question 1 — langage naturel} → {Reponse directe 1-3 phrases}
- H3 : {Question 2} → {Reponse directe}
- H3 : {Question 3} → {Reponse directe}

## 5. Bloc AIO — En resume

{Synthese actionnable 2-3 phrases. Message central.}

## 6. Maillage interne

| Type | Cible | Ancre suggeree |
|------|-------|----------------|
| Vers pilier | {URL} | {texte d'ancre} |
| Vers satellite 1 | {URL} | {texte d'ancre} |
| Vers satellite 2 | {URL} | {texte d'ancre} |
| Pont inter-cluster | {URL si applicable} | {texte d'ancre} |

## 7. Monetisation

| Champ | Valeur |
|-------|--------|
| Levier principal | {Affilie / Formation / Newsletter / Consultation} |
| Produit/outil | {nom + code promo si applicable} |
| CTA principal | {formulation exacte} |
| Placement CTA | {apres quelle section H2} |
| CTA secondaire | {formulation} |

## 8. Requetes AIO/GEO

| Requete conversationnelle | Format de reponse optimal |
|--------------------------|--------------------------|
| {Question 1} | {Liste / Paragraphe / Tableau / Etapes} |
| {Question 2} | {Format} |
| {Question 3} | {Format} |

## 9. Donnees structurees

- [ ] Article Schema
- [ ] FAQ Schema
- [ ] HowTo Schema

## 10. Notes de production

{Particularites, sources a consulter, captures d'ecran necessaires}
```

---

## Exemple

**Entree** : `/seo-brief-generator B6`

**Sortie** : brief complet pour "FluentCRM : le guide complet email marketing WordPress" avec :
- Cluster B, MOFU, mot-cle "fluentcrm tutoriel"
- Reponse rapide sur FluentCRM (definition + avantage cle + pour qui)
- Plan H2/H3 : installation → configuration → premiere sequence → automatisation → FAQ
- Maillage vers Pilier B, B2, B3, COMP-B1
- Monetisation FluentCRM affilie, CTA apres section automatisation
- 3 requetes AIO ("FluentCRM est-il gratuit ?", "Comment configurer FluentCRM ?", "FluentCRM vs Mailchimp")
- FAQ Schema + Article Schema

---

## Actions suivantes

Apres generation du brief :
1. Valider le brief avec l'utilisateur
2. Lancer la redaction avec le skill thruuu-seo-writer ou manuellement
3. Apres redaction, auditer avec `/article-audit-score`
4. Apres publication, deriver avec `/article-multiformat`

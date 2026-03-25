# Système de contenu récurrent schoolsWP

**Objectif** : produire chaque semaine 1 article SEO + 1 newsletter FluentCRM + 1 post LinkedIn, de manière cohérente et peu chronophage.

**Principe central** : un article = une source. Tout le reste en découle.

---

## Architecture du système

### Flux de réutilisation : Article → Newsletter → LinkedIn

```
[Article SEO] (source principale)
      │
      ├─→ [Newsletter FluentCRM] — angle "praticien" : ce que j'ai appris, comment l'appliquer
      │
      └─→ [Post LinkedIn] — angle "preuve" : résultat concret, chiffre, ou question ouverte
```

L'article est produit en premier. Les deux autres formats en extraient un angle différent — sans réécrire le fond, juste en changeant le prisme.

---

## Production vs Distribution

### Production (une fois par semaine, idéalement lundi ou mardi)

| Livrable      | Rôle                               | Source                      | Temps estimé            |
| ------------- | ---------------------------------- | --------------------------- | ----------------------- |
| Article SEO   | Actif long terme, trafic organique | Brief + brain.bat           | 45-90 min (avec agents) |
| Newsletter    | Relation abonnés, nurturing        | Article de la semaine       | 20-30 min               |
| Post LinkedIn | Visibilité, acquisition            | Article ou résultat concret | 10-15 min               |

**Temps total production** : 1h30 à 2h30 par semaine (avec automatisation partielle).

### Distribution (programmée, ne nécessite pas de présence active)

| Canal          | Outil           | Moment             | Action                      |
| -------------- | --------------- | ------------------ | --------------------------- |
| Blog schoolsWP | WordPress       | Mercredi matin     | Publication programmée      |
| Newsletter     | FluentCRM       | Jeudi matin        | Envoi automatique ou manuel |
| LinkedIn       | Buffer / manuel | Vendredi 9h ou 18h | Publication programmée      |

---

## Logique de réutilisation par format

### Article SEO — la pièce centrale

Structure cible :

- Intention claire dès le titre (informationnelle / comparative / décisionnelle)
- Introduction : problème + promesse de réponse
- Corps : étapes, cas concrets, comparatifs si besoin
- Conclusion : récap + CTA vers ressource ou formation

Produit avec : `brain.bat --keyword "..." --intent décisionnelle --pillar LMS`

Ce que l'article doit contenir pour alimenter les formats suivants :

- Au moins un enseignement praticien ("j'ai testé X, résultat : Y")
- Au moins un chiffre ou exemple concret
- Une conclusion avec prise de position claire

### Newsletter FluentCRM — angle "praticien"

Longueur cible : 200-350 mots. Format : texte, pas de mise en page lourde.

Structure :

1. **Accroche** (1-2 phrases) — le problème que l'article résout
2. **Enseignement principal** (3-5 phrases) — ce que le lecteur doit retenir
3. **Extrait ciblé** — un passage de l'article (insight, erreur à éviter, méthode)
4. **CTA unique** — "Lire l'article complet" → lien

Segments FluentCRM à cibler :

- Liste principale schoolsWP (tous abonnés actifs)
- Sous-segment si le sujet est très spécifique (ex : LMS uniquement)

Règle : ne jamais réécrire l'article dans la newsletter. Extraire une idée et donner envie de lire.

### Post LinkedIn — angle "preuve ou question"

Longueur cible : 150-300 mots. Format : lignes courtes, pas de bullet points excessifs.

Deux angles possibles (choisir selon la semaine) :

**Option A — Preuve** :

- Ligne d'accroche : résultat ou observation concrète
- 3-5 lignes : contexte + ce qui a changé
- Fin : question ouverte ou lien vers l'article

**Option B — Question** :

- Ligne d'accroche : question provocante liée au sujet
- 3-5 lignes : ce que j'observe / ma réponse
- Fin : appel à partager un avis + lien article

Règle : le post LinkedIn ne vend rien. Il crée de la curiosité ou de la conversation.

---

## Calendrier type — semaine standard

| Jour     | Action                                                               | Durée               |
| -------- | -------------------------------------------------------------------- | ------------------- |
| Lundi    | Choisir le sujet (backlog ou pilier en cours), lancer brain.bat      | 15 min + génération |
| Mardi    | Relire l'article, corriger, programmer sur WordPress                 | 30-45 min           |
| Mercredi | Rédiger newsletter depuis l'article, programmer FluentCRM pour jeudi | 20-30 min           |
| Jeudi    | Newsletter envoyée automatiquement — rédiger post LinkedIn           | 10-15 min           |
| Vendredi | Post LinkedIn publié (manuel ou Buffer)                              | 5 min               |

---

## Backlog de sujets — comment le maintenir

Tenir une liste simple (Notion ou fichier Markdown) avec :

```
[sujet] | [pilier] | [intention] | [statut : idée / en cours / publié]
```

Règle de priorisation : choisir le sujet qui correspond au pilier le moins couvert dans le cocon actuel. Utiliser `agents.roi_editorial_plan.cli` une fois par mois pour re-prioriser.

---

## Automatisation possible (n8n)

### Niveau 1 — Notification de démarrage (quick win)

**Trigger** : Webhook ou Schedule (lundi 8h)
**Action** : envoyer un message Telegram ou email avec le sujet de la semaine depuis le backlog

```
scheduleTrigger (lundi 8h)
  → Read Backlog Sheet (Google Sheets)
  → Filter [statut = "idée"] → [0] premier résultat
  → Send Telegram: "Sujet de la semaine : [titre] | Pilier : [pilier]"
```

### Niveau 2 — Pipeline article → newsletter (semi-automatisé)

**Trigger** : webhook déclenché après publication WordPress
**Action** : créer un draft FluentCRM avec l'intro + lien article

```
Webhook (WordPress post published)
  → Extract [title, excerpt, url, category]
  → OpenAI node: "Rédige une newsletter de 250 mots à partir de cet article..."
  → Create FluentCRM Campaign Draft
  → Send Telegram: "Draft newsletter créé, à valider"
```

Point de contrôle humain obligatoire : valider le draft avant envoi.

### Niveau 3 — Draft LinkedIn (optionnel)

Même déclencheur que niveau 2, branche parallèle :

```
  → OpenAI node: "Rédige un post LinkedIn angle preuve, 200 mots..."
  → Save to Google Sheets (colonne "LinkedIn draft cette semaine")
```

Règle : les drafts IA sont des points de départ. Toujours relire et ajuster le ton avant publication.

---

## Cohérence entre les 3 formats

Pour que la semaine soit cohérente :

- **Un seul sujet par semaine** — pas de dispersion
- **Un seul CTA dominant** — article → newsletter → LinkedIn pointent vers la même page ou ressource
- **Même angle pilier** — ne pas traiter LMS sur l'article et CRM sur LinkedIn
- **Ton constant** : direct, pédagogique, basé sur l'expérience — pas de teasing creux

---

## Indicateurs à suivre (mensuel, 15 min)

| Indicateur                       | Source             | Seuil d'alerte                              |
| -------------------------------- | ------------------ | ------------------------------------------- |
| Articles publiés dans le mois    | WordPress          | < 3 = retard                                |
| Taux d'ouverture newsletter      | FluentCRM          | < 35% = problème sujet ou liste             |
| Impressions LinkedIn             | LinkedIn Analytics | tendance à surveiller, pas un objectif fixe |
| Articles avec Publish Score < 70 | publish_ready.cli  | à réviser avant publication                 |

---

## Actifs réutilisables issus de ce système

1. **Template brief semaine** — 5 champs : sujet, pilier, intention, CTA cible, angle LinkedIn
2. **Prompt newsletter** — extracteur de l'insight principal d'un article (réutilisable dans n8n ou manuellement)
3. **Prompt post LinkedIn** — deux variantes (preuve / question) à copier-coller
4. **Workflow n8n** — pipeline article → draft newsletter → draft LinkedIn (niveau 2+3)
5. **Backlog Google Sheets** — colonnes : sujet / pilier / intention / statut / date publication / Publish Score / taux ouverture

---

## Ce qu'il ne faut pas faire

- Produire la newsletter sans avoir l'article finalisé
- Publier 3 sujets différents sur 3 canaux la même semaine
- Automatiser sans checkpoint humain sur les drafts IA
- Créer un calendrier éditorial sur 3 mois sans backlog vivant
- Optimiser le post LinkedIn avant d'avoir l'article indexé

# LinkWhisper Refresh Sprint — Brief de relais

> Brief créé en session Cowork le 2026-05-06 pour transmission à une session Claude Code projet schoolsWP. Tout est paste-able. Ne pas relancer le diagnostic depuis zéro — partir directement de l'exécution.

## Contexte (3 lignes)

Rapport Rank Math 26 avr. → 03 mai : -41 mots-clés top 3, -83 mots-clés top 10, position moyenne dégradée de +2.28 sur 7 jours. Trafic encore amorti à 137 (-3) mais la chute va arriver sous 14-21 jours.

LinkWhisper choisi comme premier sprint refresh : 53 impressions, position 33, outil de la stack officielle schoolsWP, intent commerciale pure, levier d'affiliation.

URL cible : `https://schoolswp.com/link-whisper-avis/`
Mot-clé principal : `linkwhisper avis`

## Mission

Refresh complet de l'article LinkWhisper en 48h pour récupérer une position top 20 sous 14 jours. Méthode de rédaction schoolsWP en 5 étapes appliquée intégralement.

## Data à pull en priorité (MCPs disponibles dans cette session Claude Code)

### 1. Article actuel — MCP Novamira

```
Récupérer le contenu complet de https://schoolswp.com/link-whisper-avis/ via novamira-schoolswp-com :
- Titre, slug, catégories, tags
- Date publication + date dernière mise à jour
- Contenu complet (H1/H2/H3 + corps)
- Meta title + meta description Rank Math
- Featured image, images insérées
- Liens internes sortants + entrants
- Score Rank Math actuel
```

### 2. SERP top 10 — fichier thruuu

Localisation : `E:\TÉLÉCHARGEMENT\linkwhisper avis\` (dossier hors workspace, accessible depuis Claude Code en local Windows).

Fichier thruuu à lire : extraire pour chaque résultat top 10 :
- URL + Title + Meta description
- Nombre de mots
- Structure H2/H3 complète
- Présence de : tableau comparatif, screenshots (combien), vidéo embed, FAQ, CTA affilié
- Date publication + dernière MAJ
- Featured Snippet source si présent
- People Also Ask (les 4-8 questions)

### 3. Volume + KD + secondary keywords — MCP DataForSEO

```
dataforseo : keywords_data pour "linkwhisper avis" (FR)
- Search volume mensuel
- KD (keyword difficulty)
- CPC
- Tendance 12 mois
- Related keywords avec volume (top 30)
- Questions associées
```

Pousser aussi sur les variantes :
- `link whisper avis`
- `linkwhisper review`
- `linkwhisper alternative`
- `linkwhisper prix`
- `link whisper vs`

### 4. Performance historique — MCP GSC

```
gsc-mcp : Search Analytics pour schoolswp.com
- Filtrer page = /link-whisper-avis/
- 90 derniers jours
- Top 50 queries qui amènent du trafic
- CTR moyen, position moyenne
- Évolution semaine par semaine
- URL Inspect : statut indexation, dernière visite Googlebot
```

## Plan d'exécution — 5 étapes méthode schoolsWP

### Étape 1 — Diagnostic (heure 0-2)

Comparer l'article actuel (Novamira) au top 3 SERP (thruuu) :
- Gap de couverture : quels H2 du top 3 manquent dans la version actuelle ?
- Gap de format : tableau, screenshots, vidéo, FAQ ?
- Gap d'intent : intent dominant du top 3 vs angle actuel
- Gap de fraîcheur : date des concurrents vs date schoolsWP
- Gap de longueur : mots actuels vs moyenne top 3

Output : `core/tasks/plans/linkwhisper-gap-analysis.md`

### Étape 2 — Brief de réécriture (heure 2-4)

Construire le brief via le sub-agent `radar` ou skill `thruuu-writer` :
- Plan H2/H3 cible (basé sur gaps + PAA + secondary keywords DataForSEO)
- Title cible (orienté résultat, ex: « LinkWhisper Avis 2026 : Mon test après X mois sur schoolsWP »)
- Meta cible (155 caractères, promesse + chiffre)
- Mots-clés sémantiques à intégrer (NER + secondary)
- Sections différenciantes : « Mon retour d'expérience sur schoolsWP » + « Quand LinkWhisper ne sert à rien »

### Étape 3 — Réécriture (heure 4-12)

Sub-agent `studio` pour la production :
- Nouvelle intro (problème → solution → ce que tu vas apprendre)
- Contenu enrichi selon plan brief
- Section retour d'expérience avec chiffres réels schoolsWP (à demander à Michaël ou extraire de GSC)
- FAQ longue traîne sur les 8 PAA + variantes
- Voix schoolsWP (tutoiement, expressions signature, vocabulaire validé)
- Disclosure affilié obligatoire en pied de section recommandation

### Étape 4 — Optimisation technique (heure 12-16)

- Title + Meta dans Rank Math (via Novamira write)
- Slug inchangé (URL = /link-whisper-avis/)
- Schema FAQ + Article (Rank Math auto)
- 3-4 screenshots récents 2026 (interface LinkWhisper actuelle)
- Image featured WebP optimisée
- Date « Dernière mise à jour » au 2026-05-08

### Étape 5 — Distribution & signal (heure 16-48)

- Maillage interne : sub-agent `radar` identifie 5 articles connexes pour insérer ancres contextuelles vers /link-whisper-avis/
- GSC URL Inspection → demande indexation
- IndexNow ping (via Rank Math)
- Post LinkedIn + Bluesky (sub-agent `pulse`) — angle expérience perso, pas annonce mou
- Mention dans prochaine schoolsWP News si départ < 7 jours

## KPIs — mesure à J+14 (2026-05-20)

Trois indicateurs, GSC source de vérité :

1. **Position moyenne sur `linkwhisper avis`** : objectif ≤ 20 (gain de 13 places min)
2. **Impressions sur la query principale** : objectif +30% vs baseline 53 imp/7j
3. **CTR moyen page** : objectif > 2%

Si 2 KPIs sur 3 atteints à J+14 → décliner sprint sur Tunnel de vente WordPress.
Si échec → diagnostic complémentaire : pénalité, technique, concurrence ?

## Garde-fous schoolsWP (non négociables)

- Tutoiement systématique
- Aucune promesse non prouvée — chiffres avec source
- Disclosure affilié exact : *Lien affilié — je recommande uniquement les outils que j'utilise au quotidien.*
- Code promo si applicable (vérifier si LinkWhisper a un code partenaire pour Michaël)
- Stack officielle respectée — aucune reco hors Rank Math / Link Whisper / Easy Content Linker pour le maillage
- Phrases 8-15 mots, paragraphes 2-4 phrases
- Un seul CTA principal en fin d'article (essai gratuit ou test)
- Checklist 10 points appliquée avant publication

## Sub-agents à mobiliser

- `radar` : diagnostic SERP + maillage interne + brief
- `studio` : réécriture article
- `pulse` : posts sociaux distribution
- `seo-specialist` : audit technique avant publish (schema, CWV, indexation)

## Ne PAS faire

- Ne PAS changer l'URL (slug actuel garde le jus historique)
- Ne PAS supprimer les liens entrants existants
- Ne PAS sur-optimiser le mot-clé principal (densité naturelle 1-2%)
- Ne PAS publier sans la disclosure affilié
- Ne PAS infantiliser le lecteur (« il suffit de », « en un clic » bannis)

---

**Prompt de démarrage à coller dans la session Claude Code projet schoolsWP :**

```
Lance le sprint refresh LinkWhisper documenté dans core/tasks/plans/linkwhisper-refresh-sprint.md.
Commence par l'étape 1 : pull des 4 sources de data (Novamira pour la page actuelle, fichier thruuu E:\TÉLÉCHARGEMENT\linkwhisper avis\, DataForSEO sur "linkwhisper avis" FR, GSC sur la page /link-whisper-avis/). Produis ensuite le gap analysis dans core/tasks/plans/linkwhisper-gap-analysis.md. Stop avant de passer à l'étape 2 — je veux valider le diagnostic avant la réécriture.
```

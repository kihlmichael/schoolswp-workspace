# schoolsWP SEO Agent

Agent automatise qui lit Google Search Console, agit dans WordPress,
et produit des actions pretes a valider.

Objectif:
GSC decide, WP execute, humain valide.

---

# Architecture cible (simple + robuste)
- n8n (orchestrateur)
- Google Search Console API (donnees SEO)
- WordPress REST API (lecture/ecriture)
- Rank Math (metas/schema si utile)
- FluentCRM / FluentBoards (suivi optionnel)

Principe:
GSC -> Decision -> Actions -> Drafts -> Validation -> Publish
---

# Les 3 boucles de l agent

## 1) Loop Radar (quotidien)
But: detecter quoi bouge et ou agir.
- Pages en baisse (clics, impressions, CTR, position)
- Requetes qui montent (opportunites)
- Requetes positions 4-12 (presque top 3)
- Alertes: chute brutale, CTR anormal, cannibalisation

Sortie:
Liste priorisee P1/P2/P3 + actions proposees.

## 2) Loop Ops (2-3x / semaine)
But: produire des patchs SEO rapides.
- Titles / metas (CTR)
- FAQ IA-friendly (citabilite)
- Liens internes vers money/piliers
- Brouillon mise a jour

Sortie:
Drafts + checklist de validation.
## 3) Loop Publishing (hebdo)
But: transformer les opportunites en production.
- Brief SEO + plan H2/H3
- Brouillon WP structure
- Bloc FAQ + extraits IA
- CTA + liens internes

Sortie:
1-3 drafts prets a publier.

---

# Garde-fous (indispensable)
Mode recommande: human-in-the-loop.
- Jamais d ecriture directe sur du contenu publie
- Creation de drafts / propositions
- Validation manuelle avant publication

Securite:
- OAuth GSC scopes minimum
- WP Application Password pour user "Agent SEO"
- Secrets stockes dans n8n
- Logs + rollback (avant/apres)
---

# Logique de decision (exemple clean)
P1 Quick ROI
- Position 4-12 + impressions elevees + CTR faible
  -> title/meta + enrichir snippet
- Position 1-3 + CTR en baisse
  -> title/meta + FAQ + intent match

P2 Maintenance
- Pages en baisse sur 28j vs 28j
  -> mise a jour + liens internes + section manquante

P3 Expansion
- Requetes montantes non couvertes
  -> nouvelle section ou nouvelle page (draft)

---

# Workflow n8n (concret)
Workflow A - GSC Daily Watch
- Cron 07:30
- GSC search analytics (28j + comparaison)
- Filtre: delta clics negatif OU CTR faible OU pos 4-12
- Enrichissement WP: slug, categories, last update
- Score = impressions * (1/position) * (1-CTR)
- Sortie: tache + actions proposees
Workflow B - SEO Patch Builder
- Trigger manuel sur page P1
- Lire page WP
- Generer: 3 titles, 2 metas, 5 FAQs, 5 liens internes
- Ecrire en draft ou custom field
- Checklist validation

Workflow C - Publish Gate
- Statut APPROVED
- Appliquer changements sur WP
- Ping sitemap / IndexNow
- Log + notification

---

# Actions standard (schoolsWP)
Chaque action doit inclure:
- Pourquoi ca bouge (hypothese)
- Action (1 phrase)
- Impact attendu (KPI)
- Effort (S/M/L)
- Patch (title/meta/FAQ/liens)

---

# Plan de mise en place
1) Brancher GSC -> n8n (lecture only)
2) Brancher WP REST (lecture + drafts)
3) Rapports quotidiens 7 jours (sans ecriture)
4) Activer Patch Builder sur 5 pages P1
5) Ajouter Publish Gate (approbation)
6) Rythme hebdo: 1-3 drafts

---

# V1 recommandee (safe)
- Daily Watch + scoring + taches
- Patch Builder en drafts
- Validation manuelle

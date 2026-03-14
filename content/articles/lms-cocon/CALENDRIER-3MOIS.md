# Calendrier éditorial — Pilier LMS WordPress (3 mois)

**Objectifs** : Autorité LMS +15 à +25 pts · Connexions CRM/WooCommerce · Article signature · 2-3 quick wins SEO
**Période** : Mars → Mai 2026
**Cadence** : 1 article / semaine · 12 articles total

---

## Scoring ROI — Tableau général

Formule : `Score ROI = (SEO×0.35) + (Business×0.35) + (Autorité×0.2) − (Effort×0.1)`

| # | Article | SEO | Biz | Auth | Effort | **Score ROI** | Priorité |
|---|---------|-----|-----|------|--------|--------------|----------|
| M1S1 | Architecture complète LMS WordPress rentable | 7 | 9 | 9 | 9 | **6.50** | 🔥 A |
| M1S2 | Tutor LMS vs LearnDash | 8 | 8 | 7 | 7 | **6.30** | 🔥 A |
| M2S1 | Tunnel de vente formation WordPress | 7 | 9 | 8 | 8 | **6.40** | 🔥 A |
| M1S3 | Tutor LMS + FluentCRM (automatisation) | 6 | 9 | 8 | 7 | **6.15** | 🟡 B |
| M3S1 | Structurer ses cours pour maximiser la complétion | 6 | 7 | 8 | 6 | **5.55** | 🔥 A |
| M3S2 | Hébergement recommandé pour LMS WordPress | 7 | 7 | 6 | 5 | **5.60** | 🟡 B |
| M2S3 | Automatiser l'onboarding des élèves | 6 | 8 | 7 | 7 | **5.60** | 🟡 B |
| M2S2 | Optimiser la vitesse d'un LMS WordPress | 7 | 6 | 7 | 6 | **5.35** | 🟡 B |
| M1S4 | LMS gratuit vs premium : analyse ROI | 7 | 6 | 6 | 5 | **5.25** | 🔵 C |
| M2S4 | WooCommerce + LMS : configuration idéale | 6 | 7 | 6 | 7 | **5.05** | 🔵 C |
| M3S3 | Gérer 1000 élèves sur WordPress | 5 | 6 | 9 | 8 | **4.85** | 🟡 B |
| M3S4 | Gamification dans un LMS WordPress | 5 | 5 | 6 | 5 | **4.20** | 🔵 C |

---

## MOIS 1 — Fondation stratégique

### 🔥 Semaine 1 — Article signature pilier

**Architecture complète d'un LMS WordPress rentable**
*(Tutor LMS + FluentCRM + WooCommerce)*

| Champ | Valeur |
|-------|--------|
| Mot-clé | `lms wordpress rentable` |
| Intent | Décisionnelle stratégique |
| Score ROI | **6.50/9** |
| Rôle | Article signature — nœud central du maillage |
| Impact | Autorité max · Business (3 produits) · Maillage vers tous les clusters |
| Format | Pipeline complet (V1 existante → run-from-v1) |

> V1 disponible dans `articles/lms-architecture-signature/v1.md` (682 mots)
> V3 générée : 2782 mots · Audit : 5.0/10 → relancer après édition manuelle V2

**Commande (à partir de la V1 existante) :**
```bash
python scripts/run-from-v1.py \
  --v1 articles/lms-architecture-signature/v1.md \
  --keyword "lms wordpress rentable" \
  --intent décisionnelle
```

**Liens sortants obligatoires :**
- → M1S2 (Tutor vs LearnDash)
- → M1S3 (Tutor + FluentCRM)
- → M2S1 (Tunnel de vente)
- → M2S4 (WooCommerce + LMS)

---

### 🔥 Semaine 2 — Quick win SEO comparatif

**Tutor LMS vs LearnDash : lequel choisir selon ton modèle économique**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `tutor lms vs learndash` |
| Intent | Comparative |
| Score ROI | **6.30/9** |
| Rôle | Quick win SEO · Affilié × 2 plugins · Décision business |
| Impact | Trafic organique rapide · Revenus affiliés · Maillage CRM |

**Commande :**
```bash
python -m agents.schoolswp_brain.workflow_cli seo-audit \
  --keyword "tutor lms vs learndash" \
  --intent comparative \
  --audience "formateur WordPress ou freelance qui veut créer des cours en ligne" \
  --context "Comparer selon 4 critères : prix, fonctionnalités, écosystème WooCommerce, courbe d'apprentissage" \
  --save-dir articles/tutor-vs-learndash/
```

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M1S3 (Tutor + FluentCRM)
- → M1S4 (LMS gratuit vs premium)

---

### 🟡 Semaine 3 — Cluster CRM

**Connecter Tutor LMS à FluentCRM : automatisation complète**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `tutor lms fluentcrm automatisation` |
| Intent | Décisionnelle technique |
| Score ROI | **6.15/9** |
| Rôle | Pont LMS ↔ CRM · Différenciation forte · Segment avancé |
| Impact | Business fort · Autorité CRM · Maillage triangulaire |

**Commande :**
```bash
brain-lite.bat \
  --keyword "tutor lms fluentcrm automatisation" \
  --intent décisionnelle \
  --pilier lms
```

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M2S3 (Onboarding élèves)
- → M2S1 (Tunnel de vente)

---

### 🔵 Semaine 4 — Longue traîne

**LMS gratuit vs premium WordPress : analyse ROI réelle**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `lms wordpress gratuit ou payant` |
| Intent | Comparative |
| Score ROI | **5.25/9** |
| Rôle | Captation longue traîne · Entrée dans le funnel |
| Impact | Volume organique · Filtre audience selon budget |

**Commande :**
```bash
brain-lite.bat \
  --keyword "lms wordpress gratuit payant" \
  --intent comparative \
  --pilier lms
```

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M1S2 (Tutor vs LearnDash)

---

## MOIS 2 — Profondeur & différenciation

### 🔥 Semaine 1 — Connexion CRM + WooCommerce

**Tunnel de vente pour formation WordPress : architecture optimale**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `tunnel de vente formation wordpress` |
| Intent | Stratégique décisionnelle |
| Score ROI | **6.40/9** |
| Rôle | Connexion cluster CRM ↔ WooCommerce · Fort potentiel conversion |
| Impact | Business maximal · Autorité funnel · Maillage vers FluentCRM |

**Commande :**
```bash
python -m agents.schoolswp_brain.workflow_cli seo-audit \
  --keyword "tunnel de vente formation wordpress" \
  --intent décisionnelle \
  --audience "formateur en ligne qui vend ses cours via WordPress" \
  --context "Architecture : page de vente WooCommerce + FluentCRM séquences + Tutor LMS accès cours" \
  --save-dir articles/tunnel-vente-formation/
```

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M1S3 (Tutor + FluentCRM)
- → M2S3 (Onboarding élèves)
- → M2S4 (WooCommerce + LMS)

---

### 🟡 Semaine 2 — Cluster performance

**Optimiser la vitesse d'un LMS WordPress**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `optimiser vitesse lms wordpress` |
| Intent | Technique |
| Score ROI | **5.35/9** |
| Rôle | Autorité performance · Affilié hébergement/cache |
| Impact | SEO technique · Différenciation expert |

**Commande :**
```bash
brain-lite.bat \
  --keyword "optimiser vitesse lms wordpress" \
  --intent informationnelle \
  --pilier lms
```

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M3S2 (Hébergement LMS)
- → M3S3 (Gérer 1000 élèves)

---

### 🟡 Semaine 3 — Automatisation onboarding

**Automatiser l'onboarding des élèves sur WordPress**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `onboarding eleves wordpress automatisation` |
| Intent | Décisionnelle |
| Score ROI | **5.60/9** |
| Rôle | Forte valeur perçue · FluentCRM automation · Différenciation |
| Impact | Business CRM · Rétention élèves · Citabilité IA |

**Commande :**
```bash
brain-lite.bat \
  --keyword "onboarding élèves wordpress automatisation" \
  --intent décisionnelle \
  --pilier lms
```

**Liens sortants :**
- → M1S3 (Tutor + FluentCRM)
- → M2S1 (Tunnel de vente)

---

### 🔵 Semaine 4 — WooCommerce + LMS

**WooCommerce + LMS WordPress : configuration idéale**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `woocommerce lms wordpress configuration` |
| Intent | Technique stratégique |
| Score ROI | **5.05/9** |
| Rôle | Pont WooCommerce ↔ LMS · Maillage e-commerce |
| Impact | Cluster WooCommerce · Affilié plugins |

**Commande :**
```bash
brain-lite.bat \
  --keyword "woocommerce lms wordpress" \
  --intent décisionnelle \
  --pilier lms
```

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M2S1 (Tunnel de vente)

---

## MOIS 3 — Consolidation & expansion

### 🔥 Semaine 1 — Différenciation contenu

**Comment structurer ses cours pour maximiser la complétion**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `structurer cours en ligne completion wordpress` |
| Intent | Informationnelle experte |
| Score ROI | **5.55/9** |
| Rôle | Différenciation forte · Peu traité en profondeur · Citabilité IA |
| Impact | Autorité pédagogique · Business formation |

**Commande :**
```bash
python -m agents.schoolswp_brain.workflow_cli content-factory \
  --keyword "structurer cours en ligne completion" \
  --topic "Comment structurer ses cours pour maximiser la complétion sur WordPress" \
  --intent informationnelle \
  --save-dir articles/structurer-cours-completion/
```

> W3 recommandé ici : article + newsletter + LinkedIn + FAQ AIO simultanément

**Liens sortants :**
- → M1S1 (Architecture LMS)
- → M2S3 (Onboarding élèves)

---

### 🟡 Semaine 2 — Affilié hébergement

**Hébergement recommandé pour un LMS WordPress**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `meilleur hébergement lms wordpress` |
| Intent | Informationnelle experte |
| Score ROI | **5.60/9** |
| Rôle | Potentiel affilié (hébergement = revenus récurrents) |
| Impact | SEO volume · Business affilié |

**Commande :**
```bash
python -m agents.schoolswp_brain.workflow_cli seo-audit \
  --keyword "meilleur hébergement lms wordpress" \
  --intent comparative \
  --audience "formateur qui cherche à héberger son LMS WordPress" \
  --context "Comparer O2Switch, Kinsta, Cloudways selon : vitesse, support, prix, compatibilité Tutor LMS" \
  --save-dir articles/hebergement-lms-wordpress/
```

**Liens sortants :**
- → M2S2 (Vitesse LMS)
- → M3S3 (Gérer 1000 élèves)

---

### 🟡 Semaine 3 — Autorité technique expert

**Gérer 1000 élèves sur WordPress : scalabilité réelle**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `wordpress lms scalabilite 1000 eleves` |
| Intent | Informationnelle experte |
| Score ROI | **4.85/9** |
| Rôle | Différenciation expert · Faible concurrence · Citabilité IA forte |
| Impact | Autorité durable · Référence technique |

**Commande :**
```bash
brain-lite.bat \
  --keyword "lms wordpress scalabilité 1000 élèves" \
  --intent informationnelle \
  --pilier lms
```

**Liens sortants :**
- → M2S2 (Vitesse LMS)
- → M3S2 (Hébergement LMS)
- → M1S1 (Architecture LMS)

---

### 🔵 Semaine 4 — Différenciation UX

**Gamification dans un LMS WordPress**

| Champ | Valeur |
|-------|--------|
| Mot-clé | `gamification lms wordpress` |
| Intent | Informationnelle |
| Score ROI | **4.20/9** |
| Rôle | Différenciation UX · Niche peu couverte |
| Impact | Autorité UX/engagement |

**Commande :**
```bash
brain-lite.bat \
  --keyword "gamification lms wordpress" \
  --intent informationnelle \
  --pilier lms
```

**Liens sortants :**
- → M3S1 (Structurer ses cours)
- → M1S1 (Architecture LMS)

---

## Maillage interne — Matrice complète

> Lire : ligne = article source · colonne = article cible · ✓ = lien recommandé

|  | M1S1 Archi | M1S2 Tutor/LD | M1S3 CRM | M1S4 Gratuit | M2S1 Tunnel | M2S2 Vitesse | M2S3 Onboard | M2S4 WooC | M3S1 Cours | M3S2 Héberg | M3S3 Scale | M3S4 Gamif |
|--|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| M1S1 Archi | — | ✓ | ✓ | · | ✓ | · | · | ✓ | · | · | · | · |
| M1S2 Tutor/LD | ✓ | — | ✓ | ✓ | · | · | · | · | · | · | · | · |
| M1S3 CRM | ✓ | · | — | · | ✓ | · | ✓ | · | · | · | · | · |
| M1S4 Gratuit | ✓ | ✓ | · | — | · | · | · | · | · | · | · | · |
| M2S1 Tunnel | ✓ | · | ✓ | · | — | · | ✓ | ✓ | · | · | · | · |
| M2S2 Vitesse | ✓ | · | · | · | · | — | · | · | · | ✓ | ✓ | · |
| M2S3 Onboard | · | · | ✓ | · | ✓ | · | — | · | · | · | · | · |
| M2S4 WooC | ✓ | · | · | · | ✓ | · | · | — | · | · | · | · |
| M3S1 Cours | ✓ | · | · | · | · | · | ✓ | · | — | · | · | ✓ |
| M3S2 Héberg | · | · | · | · | · | ✓ | · | · | · | — | ✓ | · |
| M3S3 Scale | · | · | · | · | · | ✓ | · | · | · | ✓ | — | · |
| M3S4 Gamif | ✓ | · | · | · | · | · | · | · | ✓ | · | · | — |

**Règle** : l'article signature M1S1 reçoit des liens de tous les articles (nœud central).

---

## Pipeline de production recommandé par priorité

| Priorité | Workflow recommandé | Raison |
|----------|-------------------|--------|
| 🔥 A ROI ≥ 6.0 | `workflow_cli seo-audit` | V1 + audit + V2 : qualité maximale |
| 🔥 A ROI < 6.0 | `workflow_cli content-factory` | Article + 5 formats distribués simultanément |
| 🟡 B | `brain-lite.bat` | Vitesse · LLM + maillage |
| 🔵 C | `brain-lite.bat` | Consolidation rapide |

---

## KPI par mois

### Mois 1 — Fondation
- [ ] 4 articles publiés (M1S1 → M1S4)
- [ ] Article signature M1S1 : score audit ≥ 7.5/10 après édition manuelle
- [ ] M1S2 indexé Google dans les 14 jours
- [ ] Maillage : M1S1 reçoit ≥ 3 liens internes
- [ ] Pilier LMS : +5 pts autorité estimée

### Mois 2 — Profondeur
- [ ] 4 articles supplémentaires (M2S1 → M2S4)
- [ ] M2S1 Tunnel de vente : CTA FluentCRM intégré + suivi conversions
- [ ] M1S2 Tutor vs LearnDash : positions SERP suivies (keyword tracker)
- [ ] Pilier LMS : +8 pts autorité cumulée
- [ ] 1 article en top 10 SERP (M1S2 ou M1S4)

### Mois 3 — Consolidation
- [ ] 4 articles finaux (M3S1 → M3S4)
- [ ] M3S1 W3 : newsletter + LinkedIn publiés
- [ ] Révision maillage interne : audit des ancres sur les 12 articles
- [ ] Pilier LMS : +15 à +25 pts autorité totale
- [ ] Score citabilité IA M1S1 ≥ 7/10 (re-passer LLM Optimizer)

---

## Alertes stratégiques

- ⚠ **M1S1 V2 manquante** : audit score 5.0/10 (RÉÉCRITURE MAJEURE) — édition manuelle requise avant publication
- ⚠ **Rate limiting W3** : `asyncio.gather` × 5 appels simultanés — si `APIStatusError 529`, relancer uniquement les formats échoués
- ⚠ **Mots interdits** : vérifier chaque article avant publication (`disruptif`, `game changer`, `scalable`, `hack`, `révolutionnaire`, `incroyable`, `en un clic`, `sans effort`, `il suffit de`)
- ⚠ **Affiliés** : disclosure obligatoire sur M1S2 (Tutor/LearnDash), M3S2 (hébergement) — ajouter note en début d'article
- ⚠ **Tutoiement** : valider systématiquement — les agents respectent la règle mais les éditions manuelles peuvent l'oublier

# Templates Google Sheets — SEO Workflow schoolsWP

## Instructions de création

1. Créer un Google Sheet nommé : `[schoolsWP] SEO Workflow — Pilotage`
2. Créer les 10 onglets dans l'ordre ci-dessous
3. Copier les en-têtes exacts (sensibles à la casse)
4. Récupérer l'ID du Sheet depuis l'URL → remplacer `SHEET_ID_PLACEHOLDER` dans `n8n/seo-workflow.json`

---

## Onglet 01_Inventory

**En-têtes (ligne 1) :**

```
url | type_page | langue | cluster | sous_cluster | role_SEO | role_business | priorite | observations | notes
```

**Valeurs acceptées :**

- type_page : hub | categorie | article | page-conversion | outil | statique
- langue : fr | en | de
- cluster : SEO | LMS | Automatisation | Hebergement | Performance | Plugins | Affiliation | Business | Divers
- role_SEO : pilier | support | money | orpheline
- role_business : lead | affilie | vente | support | newsletter
- priorite : P1 | P2 | P3

**Mise en forme recommandée :**

- P1 → fond vert (#00D400)
- P2 → fond orange (#FFB300)
- P3 → fond gris (#EEEEEE)

---

## Onglet 02_Hygiene

**En-têtes (ligne 1) :**

```
url_or_pattern | issue | action | impact | effort | priority | status | date_traitement | notes
```

**Valeurs acceptées :**

- action : Keep | Noindex | Canonical | Redirect | Investigate
- impact : H | M | L
- effort : XS | S | M | L
- priority : P1 | P2 | P3
- status : todo | en-cours | done | bloque

---

## Onglet 03_GSC

**En-têtes (ligne 1) :**

```
url | query | impressions | clics | ctr | position | type_opportunite | action | priority | date_analyse
```

**Valeurs type_opportunite :** ctr-faible | position-8-20 | cannibalisation | impressions-zero | ok

**Formules utiles (à entrer en G2) :**

- CTR faible : `=IF(AND(C2>500,D2/C2<0.03),"ctr-faible","")`
- Position opportunité : `=IF(AND(F2>=8,F2<=20),"position-8-20","")`
- Combinée : `=IF(AND(C2>500,D2/C2<0.03),"ctr-faible",IF(AND(F2>=8,F2<=20),"position-8-20","ok"))`

---

## Onglet 04_Competitors

**En-têtes (ligne 1) :**

```
mot_cle | volume | cluster | top1 | top2 | top3 | top_format | presence_schoolsWP | gap | opportunite | priorite
```

**Valeurs top_format :** guide | comparatif | liste | avis | faq | video | news
**Valeurs presence_schoolsWP :** oui | non | partiel

---

## Onglet 05_Clusters

**En-têtes (ligne 1) :**

```
cluster | pilier_url | satellites_urls | complete | cannibal_risk | gaps_keywords | action_recommandee | notes
```

**Valeurs complete :** oui | partiel | non
**Valeurs cannibal_risk :** haut | moyen | faible | aucun
**Valeurs action :** renforcer | fusionner | rediriger | creer | archiver

---

## Onglet 06_Linking

**En-têtes (ligne 1) :**

```
source_url | cible_url | anchor_recommande | contexte | reason_SEO | reason_CRO | priority | status
```

**Valeurs priority :** P1 | P2 | P3
**Valeurs status :** todo | done | bloque

---

## Onglet 07_Multilang

**En-têtes (ligne 1) :**

```
url_fr | url_en | url_de | hreflang_ok | canonical_ok | parite_contenu | action | priority | notes
```

**Valeurs hreflang_ok :** oui | partiel | non | absent
**Valeurs canonical_ok :** oui | non | absent
**Valeurs parite_contenu :** identique | adapte | vide | auto-traduit
**Valeurs action :** ok | corriger-hreflang | corriger-canonical | noindex-en | noindex-de | traduire | supprimer

---

## Onglet 08_EEAT

**En-têtes (ligne 1) :**

```
url | type_page | preuve_experience | auteur_identifie | date_maj | disclosure_affiliation | pour_qui | methode_test | score_eeat | action | priority
```

**Valeurs (colonnes C-H) :** 1 (présent) | 0 (absent)
**score_eeat :** `=C2+D2+E2+F2+G2+H2` (formule automatique, résultat 0-6)

---

## Onglet 09_Conversion

**En-têtes (ligne 1) :**

```
url_source | intention_visiteur | objectif_business | cta_actuel | probleme_cta | cta_recommande | page_cible | parcours | priority
```

**Valeurs intention :** informationnelle | comparative | transactionnelle | navigationnelle
**Valeurs objectif :** affiliation | lead | newsletter | vente | support
**Valeurs parcours :** A-affiliation | B-newsletter | C-lead

---

## Onglet 10_Backlog

**En-têtes (ligne 1) :**

```
id | action | categorie | impact_SEO | impact_business | effort | priorite | horizon | outils | owner | etat | date_creation | date_done
```

**Format id :** SEO-001, SEO-002, ...
**Valeurs categorie :** indexation | clusters | maillage | multilingue | eeat | conversion | roadmap
**Valeurs horizon :** 30j | 60j | 90j
**Valeurs etat :** todo | en-cours | done | bloque

**Vue filtrée recommandée :**

- Vue "P1 - À faire" : filtrer priorite = P1 ET etat = todo
- Vue "30j" : filtrer horizon = 30j
- Vue "Quick wins" : filtrer effort = XS ou S ET priorite = P1

# Prompt SOP-08 — Rapport final HTML

> A utiliser dans un noeud Claude dedie, en fin de pipeline.
> Input : toutes les sorties des phases precedentes. Output : HTML complet.

---

Tu executes la SOP-08 : Generation du rapport HTML final.

## Objectif

Produire un rapport HTML complet, propre, lisible et sobre a partir de toutes les donnees du pipeline.

## Input

```json
{{final_pipeline_json}}
```

## Structure HTML attendue

### 1. Header
- Titre : "Rapport Prospection LinkedIn"
- Nom de campagne
- Date d'execution
- URL du post source (lien cliquable)

### 2. Resume du post
- Auteur
- Texte du post (tronque a 300 caracteres si trop long, avec "...")
- Date
- Reactions / commentaires

### 3. Statistiques globales
Tableau recapitulatif :

| Metrique | Valeur |
|---|---|
| Commentaires bruts | X |
| Commentaires nettoyes | X |
| Leads enrichis | X |
| Leads qualifies | X |
| Leads a revoir | X |
| Leads rejetes | X |
| Score moyen (qualified) | X |
| Score max | X |
| Messages generes | X |
| Emails verifies (Hunter) | X |

### 4. Leads qualifies
Tableau avec colonnes : Nom, Role, Entreprise, Secteur, Score, Action

Fond : `#e8f5e9` (vert clair)

### 5. Leads a revoir
Tableau avec colonnes : Nom, Role, Entreprise, Score, Raison review

Fond : `#fff3e0` (orange clair)

### 6. Leads rejetes
Nombre total + top 3 raisons de rejet

Fond : `#fce4ec` (rouge clair)

### 7. Messages generes
Pour chaque lead qualifie :
- Nom du lead
- Angle choisi
- Les 3 variantes (soft, direct, expert) dans des blocs distincts

### 8. Verification email
Si Hunter active : tableau avec Nom, Email, Confiance, Statut

Si Hunter non active : mention "Verification email non activee pour cette campagne."

### 9. Warnings
Liste a puces des alertes remontees pendant le pipeline.

## Contraintes HTML

- HTML simple et autonome (pas de framework externe)
- CSS inline leger
- Police : `font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- Largeur max : `max-width: 960px; margin: 0 auto`
- Tableaux avec bordures legeres : `border: 1px solid #ddd; border-collapse: collapse`
- Padding cellules : `padding: 8px 12px`
- Lisible sur desktop
- Sobre, professionnel, oriente rapport

## Format de sortie

Retourne **uniquement** le HTML complet, sans texte avant ni apres.
Commence par `<!DOCTYPE html>` et termine par `</html>`.

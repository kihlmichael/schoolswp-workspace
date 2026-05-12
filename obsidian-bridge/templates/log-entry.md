# Modèle d'entrée pour `log.md` du vault

Format strict imposé par la charte du wiki Obsidian schoolsWP.

À copier-coller dans la section 6 (Entrées) du fichier `log.md` à la racine du vault.

## 1. Modèle d'entrée

```markdown
### [YYYY-MM-DD] type | Titre court

- **Auteur** : agent (L0 / L1 / L2) ou Michaël
- **Cible** : fichier(s) ou zone(s) concerné(s)
- **Action** : ce qui a été fait, en une phrase
- **Raison** : pourquoi
- **Validation** : oui / non / non requise
- **Notes** : (optionnel - détails utiles, contexte, ancien contenu résumé)
```

## 2. Types autorisés (un seul par entrée)

| Type                | Signification                                                    |
|---------------------|------------------------------------------------------------------|
| `ajout`             | Nouvelle information, fichier ou section ajouté                  |
| `modification`      | Contenu existant modifié                                         |
| `suppression`       | Contenu retiré (avec résumé de l'ancien dans **Notes**)          |
| `decision`          | Décision engageante enregistrée                                  |
| `correction`        | Correction d'une erreur, faute, lien cassé, incohérence          |
| `synthese`          | Production d'une synthèse à partir de plusieurs sources          |
| `validation_memoire`| Élément promu en mémoire durable après accord explicite          |
| `lint`              | Contrôle de cohérence (orphelins, doublons, contradictions)      |
| `archive`           | Contenu déplacé en archive sans destruction                      |

## 3. Règles strictes

- Append-only : on ne réécrit pas le passé.
- Une action significative = une entrée.
- Pas de regroupement abusif.
- Pas de modification silencieuse.
- Écrasement = résumé obligatoire de l'ancien contenu dans **Notes**.
- Suppression = justification obligatoire dans **Raison**.
- Validation mémoire = accord explicite de Michaël consigné dans **Validation**.
- Préférer la concision : 1 phrase pour l'action, 1 phrase pour la raison.

## 4. Mise à jour de la grille (section 5 du log.md)

Après ajout d'une entrée détaillée dans la section 6, ajouter une ligne dans la grille section 5 :

```markdown
| YYYY-MM-DD | type               | cible                                                  | auteur   | validation       |
```

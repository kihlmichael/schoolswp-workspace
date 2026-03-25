# Organisateur de Photos de Vacances avec Gemini Vision

## Description

Ce workflow n8n organise automatiquement vos photos de vacances stockées sur Google Drive en utilisant Gemini Vision pour :
- Identifier la ville de chaque photo par analyse visuelle
- Évaluer la qualité (netteté, composition, lumière)
- Renommer les fichiers de manière descriptive
- Organiser par dossiers (un par ville)
- Sélectionner les 20 meilleures photos

## Prérequis

### Credentials n8n requis

1. **Google Drive OAuth2**
   - Créer un projet Google Cloud
   - Activer l'API Google Drive
   - Créer des credentials OAuth2 (application de bureau)
   - Ajouter les scopes : `drive`, `drive.file`, `drive.metadata`

2. **Google Gemini API (PaLM)**
   - Obtenir une clé API sur [Google AI Studio](https://aistudio.google.com/)
   - Ou utiliser Vertex AI avec un projet GCP

### Configuration du workflow

Dans le node **Configuration**, renseigner :

| Paramètre | Description | Obligatoire |
|-----------|-------------|-------------|
| `sourceFolderId` | ID du dossier Google Drive contenant vos photos | Oui |
| `destinationFolderId` | ID du dossier de destination (optionnel, sinon même emplacement) | Non |
| `topPhotosCount` | Nombre de meilleures photos (défaut: 20) | Non |

### Comment trouver l'ID d'un dossier Google Drive

1. Ouvrir le dossier dans Google Drive
2. L'URL est : `https://drive.google.com/drive/folders/FOLDER_ID`
3. Copier le `FOLDER_ID`

## Fonctionnement

### Étape 1 : Recherche des images
Le workflow recherche toutes les images (JPEG, PNG, etc.) dans le dossier source.

### Étape 2 : Analyse Gemini
Pour chaque image, Gemini Vision analyse :
- **Ville** : Identification par monuments, architecture, signalétique
- **Lieu/Landmark** : Monument ou lieu principal visible
- **Qualité** : Score de 1 à 10 sur netteté, composition, lumière, intérêt visuel
- **Problèmes** : Détection de flou, doublons potentiels

### Étape 3 : Filtrage qualité
- Photos floues : Exclues automatiquement
- Score qualité < 40/100 : Exclues
- Photos valides : Conservées pour organisation

### Étape 4 : Organisation par ville
Pour chaque ville identifiée :
1. Création d'un dossier avec le nom de la ville
2. Déplacement des photos dans le dossier correspondant
3. Renommage selon le format : `Ville_Element_Description_ID.jpg`

### Étape 5 : Sélection des meilleures
Les 20 photos avec le meilleur score qualité sont copiées dans le dossier **Meilleures photos**.

## Format de nommage

```
Ville_Lieu_Description_123456.jpg
```

**Exemples :**
- `Rome_Colisee_vue_au_crepuscule_948271.jpg`
- `Paris_Tour_Eiffel_depuis_Trocadero_837492.jpg`
- `Barcelone_Sagrada_Familia_facade_729384.jpg`

**Ce qui est évité :**
- `IMG_4839.jpg`
- `DSC_0001.jpg`
- `photo_vacances.jpg`

## Structure finale

```
📁 Dossier destination/
├── 📁 Rome/
│   ├── Rome_Colisee_vue_au_crepuscule_948271.jpg
│   ├── Rome_Vatican_place_Saint_Pierre_837492.jpg
│   └── ...
├── 📁 Paris/
│   ├── Paris_Tour_Eiffel_depuis_Trocadero_729384.jpg
│   └── ...
├── 📁 Non_Classe/
│   └── (photos dont la ville n'a pas pu être identifiée)
└── 📁 Meilleures photos/
    ├── 01_Rome_Colisee_coucher_soleil_948271.jpg
    ├── 02_Paris_Tour_Eiffel_nuit_837492.jpg
    └── ... (20 photos au total)
```

## Limites et considérations

### Limites techniques
- **Batch de 5** : Traitement par lots pour éviter les timeouts API
- **500 photos max** : Limite de recherche (modifiable)
- **Quota Gemini** : Respecter les limites de l'API (2000 requêtes/min pour Flash)

### Précision de l'identification
- Gemini identifie les villes par indices visuels (monuments, architecture)
- Si aucun indice fiable, la photo est classée dans `Non_Classe`
- Confiance signalée : high/medium/low

### Photos exclues
Les photos sont exclues automatiquement si :
- Elles sont floues (`is_blurry: true`)
- Le score qualité est < 40/100
- Ce sont des doublons potentiels

## Personnalisation

### Modifier le prompt Gemini
Dans le node **Analyser avec Gemini**, ajuster le `text` pour :
- Ajouter des critères de qualité spécifiques
- Modifier le format de nommage souhaité
- Adapter les instructions de détection

### Modifier les seuils de qualité
Dans le node **Parser Analyse**, ajuster :
```javascript
const shouldKeep = !analysis.is_blurry && qualityScore >= 40;
```

### Changer le nombre de meilleures photos
Dans le node **Configuration**, modifier `topPhotosCount`.

## Dépannage

| Problème | Solution |
|----------|----------|
| "Credentials not found" | Vérifier les credentials Google Drive et Gemini dans n8n |
| "Quota exceeded" | Réduire la taille des batches ou attendre le reset du quota |
| "File not found" | Vérifier que l'ID du dossier source est correct |
| Photos mal classées | Ajuster le prompt Gemini pour plus de précision |
| Trop de photos exclues | Baisser le seuil de qualité (ligne `qualityScore >= 40`) |

## Ressources

- [Documentation n8n Google Drive](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/)
- [Google Gemini API](https://ai.google.dev/docs)
- [Google Drive API](https://developers.google.com/drive/api/v3/reference)

---
name: n8n-sheets-multi-agent
description: |
  Orchestre 3 sub-agents en parallèle (JSON Analyst, Column Verifier, Mapping Generator) pour configurer un node Google Sheets dans n8n schoolsWP : analyse du JSON d'entrée, vérification des colonnes du Sheet, génération du mapping prêt à coller. Sortie structurée en 7 sections.
  Utilise ce skill quand l'utilisateur dit : "configure mon node Google Sheets n8n", "mapping n8n sheets", "append row n8n", "expressions pour Google Sheets dans n8n", "multi-agent parallèle pour Sheets", ou colle un JSON avec des noms de colonnes Sheet à mapper.
  NE PAS utiliser pour : un Sheets non lié à n8n (utiliser le MCP google_sheets direct), créer un workflow complet (utiliser n8n-workflow-architect), ou debug un schema appendOrUpdate partiel (voir mémoire feedback_n8n_sheets_appendorupdate_full_schema).
---

## Rôle

Tu es l'orchestrateur. Ton travail est de déléguer 3 analyses spécialisées en
parallèle, collecter les résultats, et produire une réponse finale structurée.
Chaque agent a un angle unique — les lancer en même temps réduit le temps total
d'une tâche qui serait longue à faire séquentiellement.

---

## Étape 0 — Collecter les inputs si absents

Avant de lancer les agents, vérifie que tu as :

1. **Le JSON d'entrée** — sortie du nœud précédent dans n8n (onglet "Output")
2. **Les noms exacts des colonnes** — ligne 1 du Google Sheet, copiés tels quels

Si l'un des deux manque, demande-les **en une seule question**. Ne lance pas les
agents sans ces deux éléments.

---

## Étape 1 — Lancer les 3 agents en parallèle

Dès que tu as le JSON et les colonnes, utilise l'outil **Agent** pour spawner les
3 agents dans le **même appel** (un seul bloc d'appels d'outils simultanés).

### Agent 1 — JSON Analyst

**Prompt à envoyer :**

```
Tu es un expert n8n spécialisé dans l'analyse de structures JSON.

Analyse ce JSON d'entrée et produis un rapport structuré :

[COLLER LE JSON ICI]

Ton rapport doit contenir :
1. Liste complète des champs disponibles avec leur nom EXACT (respecte la casse,
   les accents, les underscores, les espaces)
2. Pour chaque champ : type de valeur détecté (string, number, boolean, null,
   objet imbriqué, tableau)
3. Structure des champs imbriqués avec le chemin complet
   (ex: data.contact.email)
4. Champs à risque : dates (format ?), téléphones (commence par 0 ou + ?),
   valeurs null ou vides, nombres qui ressemblent à des identifiants
5. Résumé : JSON plat ou imbriqué ? Combien de niveaux ?

Réponds en markdown, sois précis et exhaustif.
```

### Agent 2 — Columns Analyst

**Prompt à envoyer :**

```
Tu es un expert n8n spécialisé dans la vérification de correspondances entre
champs JSON et colonnes Google Sheets.

JSON d'entrée :
[COLLER LE JSON ICI]

Colonnes du Google Sheet (ligne 1, noms exacts) :
[COLLER LES COLONNES ICI]

Analyse et produis un rapport structuré :
1. Pour chaque colonne : existe-t-il un champ JSON correspondant ?
   - Correspondance exacte ✓
   - Correspondance approximative (casse différente, accent manquant,
     underscore vs espace) ⚠️ — précise la différence exacte
   - Aucune correspondance ✗ — la colonne n'a pas de champ JSON
2. Champs JSON sans colonne correspondante (seront ignorés)
3. Risques identifiés : noms trop similaires qui pourraient se confondre,
   caractères spéciaux dans les noms de colonnes
4. Recommandation : Auto-Map utilisable ? Ou mapping manuel obligatoire ?

Réponds en markdown avec des tableaux clairs.
```

### Agent 3 — Mapper

**Prompt à envoyer :**

```
Tu es un expert n8n spécialisé dans la génération d'expressions de mapping
pour le nœud Google Sheets.

JSON d'entrée :
[COLLER LE JSON ICI]

Colonnes du Google Sheet (ligne 1, noms exacts) :
[COLLER LES COLONNES ICI]

Génère :
1. Les réglages exacts du nœud Google Sheets :
   - Resource, Operation, Mapping Column Mode, Data Mode
2. Le mapping colonne par colonne — pour chaque colonne du sheet :
   - Expression n8n exacte avec doubles guillemets : {{ $json["champ"] }}
   - Pour les champs imbriqués : {{ $json["niveau1"]["niveau2"]["champ"] }}
   - Si colonne sans correspondance JSON : indique "(valeur statique — à définir)"
3. Un bloc final copy-paste prêt à utiliser directement dans n8n

Règles strictes :
- Ne jamais inventer un champ absent du JSON
- Toujours utiliser les doubles guillemets dans les expressions
- Adapter les chemins pour les structures imbriquées

Réponds en markdown avec des blocs de code clairs.
```

---

## Étape 2 — Collecter et agréger les résultats

Une fois les 3 agents terminés, agrège leurs rapports en une **réponse finale
structurée en 7 sections**. Ne répète pas les analyses brutes — synthétise.

---

## Structure de sortie finale obligatoire

### 1. Diagnostic rapide

Synthèse des 3 analyses :

- Nature du JSON (plat / imbriqué, nombre de champs)
- Correspondances trouvées / incohérences détectées
- Ce qui est correct, ce qui pose problème

### 2. Réglages du nœud à utiliser

```
Resource  : Sheet Within Document
Operation : Append Row
Mode      : Map Each Column Manually
Data Mode : Define Below
```

### 3. Mapping colonne par colonne

```
[Colonne]  → {{ $json["champ"] }}
[Colonne]  → {{ $json["niveau1"]["champ"] }}
```

### 4. Erreurs ou incohérences détectées

Liste structurée — une ligne par problème avec la correction recommandée.
Si aucun problème : confirme explicitement.

### 5. Erreurs fréquentes à éviter

Pièges spécifiques au cas analysé (téléphone, date, Auto-Map, guillemets...).

### 6. Checklist avant test

```
[ ] Credentials Google configurées dans n8n
[ ] Onglet cible sélectionné
[ ] Ligne 1 du sheet = en-têtes exacts
[ ] Mode = Map Each Column Manually
[ ] Expressions en doubles guillemets
[ ] Workflow sauvegardé
```

### 7. Mapping final copy-paste

Bloc propre, directement utilisable :

```
RÉGLAGES
--------
Resource  : Sheet Within Document
Operation : Append Row
Mode      : Map Each Column Manually
Data Mode : Define Below

MAPPING
-------
[Colonne 1] → {{ $json["champ1"] }}
[Colonne 2] → {{ $json["champ2"] }}
```

---

## Règles absolues

- Lancer les 3 agents **simultanément** — jamais séquentiellement
- Ne jamais inventer un champ ou une colonne
- Si une colonne n'a pas de correspondance JSON : le signaler, ne pas mapper
- Répondre en français, ton direct et orienté exécution

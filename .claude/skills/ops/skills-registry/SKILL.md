---
name: skills-registry
description: |
  Registre centralisé des skills Claude Code du workspace schoolsWP : scan de tous les SKILL.md, détection des nouveaux/modifiés/archivés, génération du rapport d'état + JSON webhook n8n, sync Google Sheets via `skills_registry.py --sync`.
  Utilise ce skill quand l'utilisateur dit : "registre skills", "inventaire skills", "sync skills", "liste des skills", "état du registre", "nouveaux skills", ou "rapport skills".
  NE PAS utiliser pour : créer ou modifier un skill (utiliser `skill-creator`), auditer la santé globale du workspace (utiliser `workspace-audit`), ou nettoyer les skills archivés (suivre le pattern feedback_skill_archival.md).
---

# schoolsWP Skills Registry

Registre centralisé. Détection automatique. Sync Google Sheets.

## Rôle

Maintenir une base de référence unique et à jour de tous les skills dans `d:\VS Code\CLAUDE CODE\.claude\skills\`.

**Objectif :** Produire à chaque exécution un rapport d'état + un JSON prêt à envoyer au webhook n8n pour mise à jour du Google Sheet.

---

## Inputs

| Input | Description | Requis |
|---|---|---|
| Aucun (mode scan complet) | Lance le scan de tous les SKILL.md | Défaut |
| `--skill <name>` | Vérifie un skill spécifique | Optionnel |
| `--status <new\|modified\|archived>` | Filtre par statut | Optionnel |

---

## Outputs obligatoires

1. **Rapport console** — toujours affiché en premier (voir format ci-dessous)
2. **JSON webhook** — prêt à envoyer à n8n (voir format ci-dessous)

Sur demande :
- CSV à coller dans Google Sheets
- Fichier XLSX via le skill `xlsx`

---

## Exemple

**Entrée :** "Scan complet des skills"

**Sortie attendue :**
```
SKILLS REGISTRY — 2026-03-16 10:00
────────────────────────────────────
Total     : 83 skills
Nouveaux  : 2  → schoolswp-skills-registry, instagram-strategy
Modifiés  : 3  → schoolswp-brain, n8n-workflow-patterns, authority-promise
Inchangés : 77
Archivés  : 1  → old-skill-name

SYNC
→ JSON prêt pour webhook n8n
→ XLSX disponible sur demande
```

---

## Procédure d'exécution

### 1 — Scanner les skills

```
Glob : d:\VS Code\CLAUDE CODE\.claude\skills\**\SKILL.md
```

Pour chaque fichier trouvé, extraire :
- Chemin relatif
- `name` et `description` depuis le frontmatter YAML
- Commandes depuis la section "Commandes rapides" (colonne gauche du tableau, si présente)
- `last_modified` via stat fichier

### 2 — Détecter les changements

Comparer avec `registry_cache.json` (voir Cache local). Méthode :

| Situation | Statut |
|---|---|
| Hash absent du cache | `new` |
| Hash identique | `unchanged` |
| Hash différent | `modified` |
| Dans le cache mais plus sur disque | `archived` |

Fallback si hash indisponible : comparer `last_modified` vs `detected_at` du cache.

### 3 — Produire le JSON de sortie

```json
{
  "execution_date": "2026-03-16T10:00:00",
  "skills": [
    {
      "name": "schoolswp-brain",
      "description": "Agent stratégique schoolsWP...",
      "triggers": "wordpress strategy, SEO WordPress",
      "commands": "Workflow A, Active l'Architect",
      "path": ".claude/skills/schoolswp-brain/SKILL.md",
      "status": "unchanged",
      "last_modified": "2026-02-15",
      "detected_at": "2026-03-16"
    }
  ],
  "summary": {
    "total": 83,
    "new": 2,
    "modified": 3,
    "unchanged": 77,
    "archived": 1
  }
}
```

### 4 — Afficher le rapport console puis proposer la sync

---

## Données extraites par skill

| Champ | Source | Obligatoire |
|---|---|---|
| `name` | Frontmatter `name:` | Oui |
| `description` | Frontmatter — 150 premiers chars | Oui |
| `description_full` | Frontmatter complet | Oui |
| `commands` | Section "Commandes rapides" — colonne gauche | Non |
| `path` | Chemin relatif du SKILL.md | Oui |
| `last_modified` | Date fichier via stat | Oui |
| `status` | `new` / `modified` / `unchanged` / `archived` | Oui |
| `detected_at` | Date + heure de l'exécution | Oui |

---

## Structure Google Sheet cible

Feuille : **`skills_registry`**

| A — name | B — description | C — triggers | D — commands | E — path | F — status | G — last_modified | H — detected_at |
|---|---|---|---|---|---|---|---|

- Colonne A = clé de déduplification
- Ligne 1 = en-têtes fixes, jamais modifiées
- Tri par défaut : F (status) puis A (name)

Le workflow n8n fait `appendOrUpdate` avec `matchingColumns: ["name"]`.

---

## Cas particuliers

| Cas | Comportement |
|---|---|
| SKILL.md sans frontmatter | Nom = dossier parent, description = vide |
| Description > 150 chars | Tronquer pour `description`, stocker complet en `description_full` |
| Skill sans "Commandes rapides" | `commands` = vide, pas d'erreur |
| Même nom, chemin différent | Warning doublon — à résoudre manuellement |
| Sheet inaccessible | Stocker le JSON dans `registry_cache.json` |

---

## Cache local

Chemin : `d:\VS Code\CLAUDE CODE\.claude\skills\.registry\registry_cache.json`

```json
{
  "last_run": "2026-03-16T10:00:00",
  "skills": { "skill-name": { "hash": "abc123", "last_modified": "..." } }
}
```

---

## Webhook n8n

**URL :** `https://schoolswp-n8n.wp1.host/webhook/skills-registry-sync`

**Script de sync :**
```bash
python "d:\VS Code\CLAUDE CODE\.claude\skills\.registry\skills_registry.py" --sync
```

---

## Commandes rapides

| Commande | Action |
|---|---|
| `Scan complet` | Exécution complète + rapport + JSON webhook |
| `Nouveaux skills` | Liste uniquement les skills `new` |
| `Skills modifiés` | Liste uniquement les skills `modified` |
| `Rapport rapide` | Compte + statuts sans extraction détaillée |
| `Export CSV` | CSV prêt à coller dans Google Sheets |
| `Export XLSX` | Fichier Excel via le skill xlsx |
| `Sync webhook` | Envoie le JSON au webhook n8n |
| `Vérifie [skill-name]` | Données d'un skill spécifique |
| `Archivés` | Skills dans le cache mais plus sur disque |

---

## Actions suivantes

Après chaque scan :
1. Afficher le rapport console
2. Proposer : "Lancer la sync webhook ?" (si nouveaux ou modifiés détectés)
3. Si archivés détectés : signaler explicitement avec les noms
4. Mettre à jour `registry_cache.json`

---

## Règles

- Tutoiement systématique
- Toujours afficher le rapport console avant tout autre output
- Ne jamais modifier les SKILL.md scannés
- Préférer vide plutôt qu'une valeur inventée en cas de doute
- Signaler clairement les anomalies : doublons, frontmatter manquant, skills orphelins

# Prompt SOP-06 — Messages personnalises

> A utiliser dans un noeud Claude dedie, apres le scoring.
> Input : leads qualifies + contexte. Output : messages JSON.

---

Tu executes la SOP-06 : Generation de messages outbound personnalises.

## Objectif

Produire des messages de prospection LinkedIn personnalises pour chaque lead qualifie.

## Input

### Leads qualifies

```json
{{qualified_leads_json}}
```

### Contexte

- offre = {{offre}}
- ton_message = {{ton_message}}

## Procedure

Pour chaque lead :

1. **Identifier la raison de personnalisation** — pourquoi ce lead, pourquoi maintenant
2. **Choisir un angle** parmi :
   - `curiosity` : le lead a pose une question ou montre de la curiosite
   - `problem` : le lead a evoque un probleme concret
   - `benchmark` : secteur comparable, partage utile
   - `useful_resource` : ressource pertinente a proposer
   - `quick_exchange` : invitation a un echange rapide
3. **Generer 3 variantes** :
   - `first_message_soft` : leger, non engageant
   - `first_message_direct` : clair, proposition nette
   - `first_message_expert` : posture expertise, valeur ajoutee

## Contraintes redactionnelles

### Obligatoire
- Max 500 caracteres par message
- Ton = {{ton_message}}
- Tutoiement
- Relier au commentaire, au profil ou au contexte du post
- Call-to-action leger (question ouverte ou proposition de partage)

### Interdit
- Compliments creux ("super profil", "j'adore ton parcours")
- Pitch agressif ("je vends X qui fait Y")
- Promesse trop forte ("multiplier tes leads par 10")
- Message generique copie-colle
- Mots interdits : disruptif, game changer, scalable, hack, revolutionnaire, incroyable, en un clic, sans effort, il suffit de
- Flatterie vide
- Longueur excessive

## Format de sortie

Retourne **uniquement** un JSON strict :

```json
{
  "generated_messages": [
    {
      "lead_id": "",
      "lead_name": "",
      "personalization_reason": "",
      "message_angle": "curiosity|problem|benchmark|useful_resource|quick_exchange",
      "first_message_soft": "",
      "first_message_direct": "",
      "first_message_expert": ""
    }
  ],
  "warnings": []
}
```

## Regles strictes

- Pas de texte hors du JSON
- Chaque lead qualifie doit avoir ses 3 variantes
- Chaque message < 500 caracteres
- `personalization_reason` obligatoire

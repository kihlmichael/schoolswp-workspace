# SOP-06 — Messages personnalises

## Objectif

Generer un message outbound personnalise pour chaque lead qualifie.

## Outil

Claude (prompt `prompts/prompt-06-messages.md`)

## Conditions de generation

| Lead | Generer message ? |
|---|---|
| qualified + contact_now | oui, toujours |
| qualified + manual_review | oui |
| review + score >= seuil - 10 | oui, si angle valable |
| review + score < seuil - 10 | non |
| rejected | non |

## Angles de personnalisation

| Angle | Quand l'utiliser |
|---|---|
| `curiosity` | Le lead a pose une question ou montre de la curiosite |
| `problem` | Le lead a evoque un probleme concret |
| `benchmark` | Le lead est dans un secteur comparable, partage utile |
| `useful_resource` | On peut partager une ressource pertinente |
| `quick_exchange` | Le commentaire invite a un echange rapide |

## Selection de l'angle

```
SI commentaire contient question -> curiosity
SI commentaire evoque probleme -> problem
SI profil secteur similar + pas de question -> benchmark
SI on a une ressource pertinente a partager -> useful_resource
SINON -> quick_exchange
```

## Contraintes redactionnelles

### Obligatoire
- Max 500 caracteres par message
- Ton = `{{ton_message}}`
- Relier au commentaire OU au profil OU au contexte du post
- Naturel, comme un message LinkedIn reel

### Interdit
- Compliments creux ("super profil", "j'adore votre parcours")
- Pitch agressif ("je vends X qui fait Y")
- Promesse trop forte ("je vais multiplier vos leads par 10")
- Message generique copie-colle
- Jargon marketing vide ("disruptif", "game changer", "scalable")
- Longueur excessive

## Structure par lead

```json
{
  "lead_id": "lead_001",
  "personalization_reason": "Le lead a commente sur l'automatisation outbound et occupe un role Growth dans une PME SaaS.",
  "message_angle": "useful_resource",
  "first_message_soft": "Bonjour Jane, j'ai vu ton commentaire sur la structuration de l'outbound LinkedIn. On travaille justement sur ce type de pipeline. Je peux te partager une approche simple si utile.",
  "first_message_direct": "Bonjour Jane, ton commentaire sur l'outbound m'a interpelle. J'ai une methode concrete pour transformer les interactions LinkedIn en pipeline qualifie. Partante pour que je te montre le framework ?",
  "first_message_expert": "Bonjour Jane, ton point sur l'outbound LinkedIn touche un vrai sujet : passer du signal social au lead exploitable sans bruit. On a modelise ce process. Je peux t'envoyer le schema si pertinent."
}
```

## Criteres qualite message

- [ ] Mentionne un element specifique (commentaire, role, secteur)
- [ ] Ton coherent avec `ton_message`
- [ ] < 500 caracteres
- [ ] Pas de flatterie vide
- [ ] Pas de pitch agressif
- [ ] Call-to-action leger (question ouverte, proposition de partage)

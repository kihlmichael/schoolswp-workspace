---
name: whatsapp
description: |
  Pilote WhatsApp via le CLI `wacli` : envoie de messages texte/fichier à un destinataire tiers, recherche dans l'historique, synchronisation initiale (auth QR) et continue, backfill d'historique. Sortie machine-readable possible avec `--json`. Authentification stockée dans `~/.wacli`.
  Utilise ce skill quand l'utilisateur dit : "envoie un message WhatsApp à ce numéro", "cherche dans mon historique WhatsApp le mot facture", "synchronise WhatsApp", "récupère les conversations avec untel", ou demande explicitement à contacter une personne tierce sur WhatsApp.
  NE PAS utiliser pour : répondre à une conversation WhatsApp utilisateur en cours (OpenClaw route automatiquement, ne pas appeler `wacli`), poster un broadcast marketing (WhatsApp Business API hors scope ce skill), ou pipeline notification routine (utiliser Discord).
homepage: https://wacli.sh
metadata: {"openclaw":{"emoji":"📱","requires":{"bins":["wacli"]},"install":[{"id":"brew","kind":"brew","formula":"steipete/tap/wacli","bins":["wacli"],"label":"Installer wacli (brew)"},{"id":"go","kind":"go","module":"github.com/steipete/wacli/cmd/wacli@latest","bins":["wacli"],"label":"Installer wacli (go)"}]}}
---

# wacli

Utilisez `wacli` uniquement quand l'utilisateur demande explicitement d'envoyer un message à quelqu'un d'autre sur WhatsApp ou quand il demande de synchroniser/rechercher l'historique WhatsApp.
N'utilisez PAS `wacli` pour les conversations utilisateur normales ; OpenClaw route automatiquement les conversations WhatsApp.
Si l'utilisateur discute avec vous sur WhatsApp, vous ne devez pas utiliser cet outil sauf s'il vous demande de contacter un tiers.

## Sécurité

- Exiger explicitement le destinataire + texte du message.
- Confirmer le destinataire + message avant l'envoi.
- En cas d'ambiguïté, poser une question de clarification.

## Authentification + synchronisation

- `wacli auth` (connexion QR + sync initiale)
- `wacli sync --follow` (synchronisation continue)
- `wacli doctor` (diagnostic)

## Trouver des conversations + messages

- `wacli chats list --limit 20 --query "nom ou numéro"`
- `wacli messages search "requête" --limit 20 --chat <jid>`
- `wacli messages search "facture" --after 2025-01-01 --before 2025-12-31`

## Remplissage de l'historique

- `wacli history backfill --chat <jid> --requests 2 --count 50`

## Envoi

- Texte : `wacli send text --to "+33612345678" --message "Bonjour ! Êtes-vous disponible à 15h ?"`
- Groupe : `wacli send text --to "1234567890-123456789@g.us" --message "J'ai 5 min de retard."`
- Fichier : `wacli send file --to "+33612345678" --file /chemin/agenda.pdf --caption "Ordre du jour"`

## Notes

- Répertoire de stockage : `~/.wacli` (remplacer avec `--store`).
- Utiliser `--json` pour une sortie machine-readable lors du parsing.
- Le remplissage d'historique nécessite votre téléphone en ligne ; résultats best-effort.
- Le CLI WhatsApp n'est pas nécessaire pour les conversations utilisateur de routine ; c'est pour envoyer des messages à d'autres personnes.
- JIDs : les chats directs ressemblent à `<numéro>@s.whatsapp.net` ; les groupes à `<id>@g.us` (utiliser `wacli chats list` pour trouver).

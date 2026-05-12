---
name: gws-gmail-send
version: 1.0.0
description: |
  Helper gws gmail +send : envoie un email Gmail (to, subject, body, support cc/bcc, html, pièces jointes). Une commande shell pour notifications, relances, ou alertes pilotées par script.
  Utilise ce skill quand l'utilisateur dit : "envoie un email", "send mail Gmail CLI", "notification mail depuis script", "envoie un récap par email", ou pour brancher Gmail comme transport notification dans un workflow n8n / cron.
  NE PAS utiliser pour : répondre à un thread existant avec threading correct (utiliser gws-gmail-reply ou gws-gmail-reply-all), forwarder un message (utiliser gws-gmail-forward), gérer une campagne marketing (utiliser FluentCRM via MCP fluentcrm), ou envoi multi-destinataires segmenté (CRM, pas Gmail).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws gmail +send --help"
---

# gmail +send

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Send an email

## Usage

```bash
gws gmail +send --to <EMAILS> --subject <SUBJECT> --body <TEXT>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--to` | ✓ | — | Recipient email address(es), comma-separated |
| `--subject` | ✓ | — | Email subject |
| `--body` | ✓ | — | Email body (plain text, or HTML with --html) |
| `--from` | — | — | Sender address (for send-as/alias; omit to use account default) |
| `--attach` | — | — | Attach a file (can be specified multiple times) |
| `--cc` | — | — | CC email address(es), comma-separated |
| `--bcc` | — | — | BCC email address(es), comma-separated |
| `--html` | — | — | Treat --body as HTML content (default is plain text) |
| `--dry-run` | — | — | Show the request that would be sent without executing it |

## Examples

```bash
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi Alice!'
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi!' --cc bob@example.com
gws gmail +send --to alice@example.com --subject 'Hello' --body '<b>Bold</b> text' --html
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi!' --from alias@example.com
gws gmail +send --to alice@example.com --subject 'Report' --body 'See attached' -a report.pdf
gws gmail +send --to alice@example.com --subject 'Files' --body 'Two files' -a a.pdf -a b.csv
```

## Tips

- Handles RFC 5322 formatting, MIME encoding, and base64 automatically.
- Use --from to send from a configured send-as alias instead of your primary address.
- Use -a/--attach to add file attachments. Can be specified multiple times. Total size limit: 25MB.
- With --html, use fragment tags (<p>, <b>, <a>, <br>, etc.) — no <html>/<body> wrapper needed.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-gmail](../gws-gmail/SKILL.md) — All send, read, and manage email commands

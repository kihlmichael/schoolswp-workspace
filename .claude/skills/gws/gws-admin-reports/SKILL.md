---
name: gws-admin-reports
version: 1.0.0
description: |
  Google Workspace Admin SDK Reports v1 via la CLI gws : audit logs et rapports d'usage du tenant Workspace (activities admin, drive, login, gmail, meet... ; usage reports utilisateurs et tenant). Source brute pour audit sécu, conformité, monitoring de domaine.
  Utilise ce skill quand l'utilisateur dit : "logs admin Workspace", "audit login", "rapport usage Drive", "qui a fait quoi sur le tenant", "activity report admin", ou pour exporter des activités Workspace vers Sheets ou un SIEM.
  NE PAS utiliser pour : opérations data utilisateur final (utiliser gws-gmail / gws-drive / gws-calendar selon le service), monitoring temps réel des events Workspace (utiliser gws-events-subscribe), ou audits SecuPress côté WordPress (hors périmètre Google).
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws admin-reports --help"
---

# admin-reports (reports_v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws admin-reports <resource> <method> [flags]
```

## API Resources

### activities

  - `list` — Retrieves a list of activities for a specific customer's account and application such as the Admin console application or the Google Drive application. For more information, see the guides for administrator and Google Drive activity reports. For more information about the activity report's parameters, see the activity parameters reference guides.
  - `watch` — Start receiving notifications for account activities. For more information, see Receiving Push Notifications.

### channels

  - `stop` — Stop watching resources through this channel.

### customerUsageReports

  - `get` — Retrieves a report which is a collection of properties and statistics for a specific customer's account. For more information, see the Customers Usage Report guide. For more information about the customer report's parameters, see the Customers Usage parameters reference guides.

### entityUsageReports

  - `get` — Retrieves a report which is a collection of properties and statistics for entities used by users within the account. For more information, see the Entities Usage Report guide. For more information about the entities report's parameters, see the Entities Usage parameters reference guides.

### userUsageReport

  - `get` — Retrieves a report which is a collection of properties and statistics for a set of users with the account. For more information, see the User Usage Report guide. For more information about the user report's parameters, see the Users Usage parameters reference guides.

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws admin-reports --help

# Inspect a method's required params, types, and defaults
gws schema admin-reports.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.


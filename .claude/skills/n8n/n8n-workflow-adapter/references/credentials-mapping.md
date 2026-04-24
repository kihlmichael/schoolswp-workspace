# Mapping credentials externes → credentials schoolsWP

Liste des credentials placeholders rencontrés dans les templates enescingoz (et assimilés) et leur équivalent dans l'instance schoolswp-n8n.wp1.host.

Pour tout placeholder non listé ici : **demander à Michael** avant de remplacer, ne jamais inventer.

## Credentials connus

| Placeholder externe | Credential schoolsWP | Type n8n | Notes |
|---|---|---|---|
| `OPENAI_API` | **retirer** | OpenAI | Stack schoolsWP = Anthropic par défaut. Swap le node vers lmChatAnthropic ou embeddingsOpenAi (si vraiment OpenAI voulu, demander confirmation) |
| `ANTHROPIC_API` | `anthropic-main` | Anthropic API | Le credential principal, utilisé par tous les workflows Claude |
| `SUPABASE_API` | `supabase-schoolswp` | Supabase | Instance Supabase schoolsWP (vector store + DB) |
| `COHERE_API` | **à demander** | Cohere | Pas encore configuré. Si template en dépend, swap vers embeddings OpenAI ou flagger |
| `PINECONE_API` | **à demander** | Pinecone | Pas encore configuré. Swap vers Supabase vector si possible |
| `TELEGRAM_BOT` | **à demander** | Telegram Bot | 9 bots actifs. Demander lequel (schoolsWP_bot, telegram-claude, etc.) |
| `WORDPRESS_API` | `wp-schoolswp-main` | WordPress | REST API de schoolswp.com avec app password |
| `GMAIL_API` | `gmail-michael-perso` | Gmail OAuth2 | Compte perso michaelkihlpro@gmail.com |
| `GOOGLE_SHEETS_API` | `google-sheets-schoolswp` | Google Sheets OAuth2 | Workspace schoolsWP |
| `GOOGLE_DRIVE_API` | `google-drive-schoolswp` | Google Drive OAuth2 | Même compte Google Workspace |
| `NOTION_API` | **à demander** | Notion | Vérifier si Michael veut connecter Notion |
| `AIRTABLE_API` | **à demander** | Airtable | Non configuré par défaut |
| `SLACK_API` | **retirer** | Slack | schoolsWP n'a pas de Slack. Remplacer par Discord webhook |
| `DISCORD_API` | `discord-webhook-schoolswp` | Discord Webhook | Webhooks Discord configurés pour notifs |
| `HUBSPOT_API` | **non applicable** | HubSpot | Pas dans la stack. Template HubSpot à écarter |
| `MAILCHIMP_API` | **non applicable** | Mailchimp | Pas dans la stack. FluentCRM à la place (pas d'équivalent n8n natif, passer par webhook) |
| `SENDGRID_API` | **non applicable** | SendGrid | Pas dans la stack |

## Credentials schoolsWP spécifiques (sans placeholder amont)

Credentials disponibles côté schoolsWP mais rarement présents dans les templates externes :

| Credential | Type n8n | Usage typique |
|---|---|---|
| `fluentcrm-webhook-in` | Webhook (custom) | Entrée webhook depuis FluentCRM (contact-added, sequence-complete) |
| `rank-math-api` | HTTP (custom header) | Utilisation de l'endpoint rankmath/v1/updateMeta (voir mémoire `reference_rank_math_rest_limits`) |
| `firecrawl-api` | HTTP (auth) | Scraping via Firecrawl |
| `dataforseo-api` | HTTP (basic auth) | Keyword research DataForSEO |
| `n8n-internal-creds` | n8n native | Pour appeler d'autres workflows n8n en interne |

## Protocole de remplacement (checklist)

Pour chaque node du workflow :

1. Lister tous les `credentials` présents (dans le champ `credentials` de chaque node)
2. Pour chaque credential :
   - Est-il dans la table "Credentials connus" ? → remplacer automatiquement
   - Est-il dans la table "à demander" ? → flagger à l'utilisateur
   - Est-il "non applicable" ? → retirer le node entier, demander alternative
3. Après remplacement, vérifier que tous les `credentials.id` référencent des credentials qui existent côté instance n8n (via MCP n8n-mcp si disponible)

## Règle anti-fuite

**Ne jamais** écrire un secret en dur dans le JSON workflow. Le credential doit toujours être une **référence** (id + name) vers un credential stocké côté n8n.

Si un template amont contient une clé en dur (ex : `"apiKey": "sk-xxx"`), c'est un placeholder/exemple : retirer la clé et utiliser un credential de référence à la place.

## Mise à jour de ce mapping

Quand un nouveau credential est ajouté à l'instance schoolswp-n8n.wp1.host :

1. Ajouter une ligne dans la table correspondante ci-dessus
2. Si c'est un credential récurrent dans les templates externes, pousser la convention de nommage `<service>-<scope>-<owner>` (ex : `supabase-schoolswp`, `gmail-michael-perso`)
3. Commit avec message `chore(skills): add <credential> to n8n-workflow-adapter mapping`

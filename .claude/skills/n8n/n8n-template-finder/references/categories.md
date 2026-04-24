# Mapping catégories enescingoz → cas d'usage schoolsWP

Source : `enescingoz/awesome-n8n-templates` (branche `main`).

Pour chaque catégorie du repo, on liste les cas d'usage schoolsWP qui peuvent s'y greffer. Ce mapping aide le matching du skill `n8n-template-finder` quand l'utilisateur formule un besoin en langage naturel.

## WordPress (6 templates, très ciblé)

**Cas d'usage schoolsWP qui matchent** :
- Auto-tagging rétroactif des 144 articles existants
- Génération d'articles dans la voix de marque (pipeline content factory)
- Chatbot site schoolswp.com (RAG sur articles)
- Ingestion articles vers vector store (alimente chatbot + recherche)
- Auto-summary (bloc TL;DR) en tête d'article

**Priorité** : MAX. Tout besoin WordPress passe par cette catégorie en premier.

## OpenAI_and_LLMs (83 templates, généraliste mais riche)

**Cas d'usage schoolsWP qui matchent** :
- Résumé de contenus longs
- Extraction d'entités nommées (NER) depuis un texte
- Classification / routage de contenus
- Agents conversationnels custom
- Recherche sémantique sur base de données interne
- Analyse de sentiment / scoring

**Filtres utiles** :
- Contient "AI Agent" → patterns agentiques
- Contient "RAG" → patterns vector + retrieval
- Contient "Supabase" → vector store compatible schoolsWP
- Contient "Ollama" → écarter sauf intérêt pour self-hosting

## Telegram (21 templates)

**Cas d'usage schoolsWP qui matchent** :
- Extension de l'écosystème Telegram (9 bots actifs)
- Bot avec mémoire long-terme (Supabase)
- Chat avec PDF (utile pour ressources internes)
- Translation audio messages
- Image analysis via LLM

**Connexion avec l'existant** : schoolsWP a déjà `telegram-claude` et 8 autres bots. Les templates peuvent inspirer de nouveaux bots ou enrichir les existants.

## Gmail_and_Email_Automation

**Cas d'usage schoolsWP qui matchent** :
- Parsing de reçus / factures (utile pour comptabilité side-business)
- Parsing d'emails reçus pour recyclage contenu (voir skill `email-to-content`)
- Auto-archiving de promos (hygiène inbox)
- Follow-up sequences simples (pour prospection, pas pour nurturing CRM qui reste FluentCRM)

**Attention** : ne pas doublonner avec FluentCRM qui gère déjà les séquences marketing. Scope ici : automatisations inbox perso, pas email marketing.

## Notion

**Cas d'usage schoolsWP qui matchent** :
- Sync knowledge base interne ↔ WordPress (Notion = scratchpad, WP = publication)
- Ingestion pages Notion vers vector store
- Auto-création de pages Notion depuis signaux externes

**Usage probable** : faible. Michael utilise moins Notion que l'écosystème WP direct.

## Airtable / Google_Sheets

**Cas d'usage schoolsWP qui matchent** :
- Briefs éditoriaux (Sheet → brain-lite → WP draft)
- Tracking affiliation (conversions → Sheet → alerte)
- Planning Pinterest (Airtable → API Pinterest, voir skill `pinterest-pipeline`)

## Slack / Discord

**Cas d'usage schoolsWP qui matchent** :
- Discord : notifications workflow + community bots (voir `telegram-agents` + `discord-orchestrator` déjà déployés)
- Slack : non pertinent (pas d'instance Slack schoolsWP)

## WhatsApp

**Cas d'usage schoolsWP qui matchent** : aucun à ce jour (pas dans la stack). Ignorer sauf changement de roadmap.

## PDF_and_Document_Processing

**Cas d'usage schoolsWP qui matchent** :
- Extraction de contenus PDF pour ingestion RAG
- Traitement de lead magnets PDF (metadata)

## AI_Research_RAG_and_Data_Analysis

**Cas d'usage schoolsWP qui matchent** :
- Patterns RAG sophistiqués (multi-source, hybrid search)
- Analyse de logs / métriques

## DevOps

**Cas d'usage schoolsWP qui matchent** :
- Monitoring uptime / alertes
- Automatisation CI/CD pour les repos schoolsWP
- Backup automatisé (WordPress, n8n, DB)

## HR_and_Recruitment / Instagram_Twitter_Social_Media

**Cas d'usage schoolsWP qui matchent** : faible. HR non applicable (solo). Social : préférer `social-media-manager` + `pinterest-pipeline` internes qui sont déjà adaptés.

## Database_and_Storage / Forms_and_Surveys / Other / Other_Integrations

Catégories fourre-tout. Recherche à la demande, pas de match systématique.

## Règles de priorité pour le finder

Quand un besoin matche plusieurs catégories, ordre de préférence :

1. **WordPress** si la stack mentionne WordPress / schoolswp.com
2. **Telegram** si la stack mentionne un des 9 bots existants
3. **OpenAI_and_LLMs** pour tout besoin agent IA / RAG transverse
4. **Gmail_and_Email_Automation** pour automatisations inbox perso
5. Autres au cas par cas

**Écarter systématiquement** : HR_and_Recruitment (pas applicable solo), WhatsApp (pas dans stack), Slack (pas dans stack).

# thruuu SERP API - integration schoolsWP

Trois manieres d'appeler l'API SERP de thruuu (https://thruuu.com/learn/serp-api/) depuis le projet schoolsWP. Toutes partagent la meme cle API (THRUUU_API_KEY dans .env racine projet) et le meme client sous-jacent.

## TL;DR - choisir le bon mode

| Tu veux... | Mode | Comment |
|---|---|---|
| Que les agents (brain.bat, content_factory, ...) appellent thruuu en backend | **A - Client Py** | from tools.thruuu_client import ThruuuClient |
| Demander une analyse SERP **en session Claude Code** | **B - Serveur MCP** | Active dans .mcp.json, puis Claude utilise les tools thruuu_* |
| Batch nocturne ou declenchement depuis Telegram/Discord/Form | **C - Workflow n8n** | Importer systems/n8n/workflows/thruuu-serp-analysis.json |

Les trois sont independants. Tu peux activer A, B, C ou les 3.

## Setup commun (1 fois)

Ajouter au .env racine projet (deja present dans .env.example) :

    THRUUU_API_KEY=eyJxxxxxxxxxxxxx...

Recuperer le token depuis ton compte thruuu, onglet API. Plan Pro (ChatGPT only sur include_llm) ou Agency (4 moteurs : ChatGPT, Gemini, Perplexity, Google AI Mode). httpx est deja dans le venv projet.

---

## Plan A - Client Py (fondation)

**Location** : tools/thruuu_client/

### Usage programmatique

    import asyncio
    from tools.thruuu_client import ThruuuClient, SerpRequest

    async def main():
        client = ThruuuClient()  # lit THRUUU_API_KEY depuis l'env
        req = SerpRequest(
            keywords=["tutor lms vs learndash"],
            country="fr",
            language="fr",
            device="desktop",
            num=10,
        )
        # End-to-end : submit + poll jusqu'au done
        results = await client.analyze(req, poll_interval=5.0, timeout=300.0)
        print(results[0])  # 1 keyword -> 1 SERP

    asyncio.run(main())

### Usage CLI (debug manuel)

Lancer depuis la racine projet via le venv (commande de Plan B en parallele dans la doc launcher) :

    .venv/Scripts/py -m tools.thruuu_client.cli analyze --keyword "fluentcrm avis" --country fr
    .venv/Scripts/py -m tools.thruuu_client.cli submit  --keyword "fluentcrm avis"
    .venv/Scripts/py -m tools.thruuu_client.cli get     abc123
    .venv/Scripts/py -m tools.thruuu_client.cli list    --page 1 --per-page 20

### Tests

    .venv/Scripts/py -m pytest tests/test_thruuu_client.py -v

17 tests unitaires - pas d'appel reseau (httpx mocke).

### API exposee

- ThruuuClient(api_key=None, base_url=..., http_timeout=30.0)
- SerpRequest(keywords, country='fr', language='fr', device='desktop', num=10, search_volume=True, analyze_headings=True, analyze_content=True, analyze_top_topics=True, include_llm=[], webhook_url=None, minified_response=False)
- await client.submit(request) -> reponse brute thruuu
- await client.get(serp_id) -> SERP par id
- await client.list(page, per_page) -> liste paginee
- await client.wait_for(serp_id, poll_interval, timeout) -> polling jusqu'a done
- await client.analyze(request, poll, poll_interval, timeout) -> end-to-end

### Exceptions

- ThruuuError - toutes les erreurs API ou config
- ThruuuTimeout - sous-classe de ThruuuError, levee si polling expire

---

## Plan B - Serveur MCP

**Location** : tools/mcp-servers/thruuu/server.py + tools/mcp-servers/_launch-thruuu.mjs

### Activation

Le bloc est deja dans .mcp.json.example. Copier dans ton .mcp.json (gitignored) si pas deja fait, et verifier que THRUUU_API_KEY est dans .env. Relancer Claude Code pour que le serveur MCP soit charge.

Le bloc a ajouter (deja present dans le template) :

    "thruuu": {
      "command": "node",
      "args": ["tools/mcp-servers/_launch-thruuu.mjs"]
    }

### Ce que fait le launcher

1. Lit THRUUU_API_KEY depuis le .env racine du projet.
2. Injecte la cle dans l'environnement du process enfant.
3. Lance le serveur FastMCP via uv run (recupere fastmcp, httpx, dotenv a la volee).
4. Le serveur lit server.py situe dans tools/mcp-servers/thruuu/.

### Tools MCP exposes

| Tool | Usage |
|---|---|
| thruuu_submit_serp | POST async, retourne les ids (non-bloquant) |
| thruuu_get_serp | GET un SERP par id |
| thruuu_list_serps | Liste paginee des SERPs du compte |
| thruuu_analyze_serp | End-to-end submit + wait (bloquant, parfait en session) |
| thruuu_extract_brief | Convertit un SERP termine en brief editorial structure |

### Exemples d'invocation en session

Demander a Claude : "Analyse-moi la SERP tutor lms vs learndash en FR puis extraits le brief." Claude appelle thruuu_analyze_serp(keyword="tutor lms vs learndash", country="fr"), attend ~30-60s, puis thruuu_extract_brief(serp_id=...) pour recuperer competitors + headings + PAA + related + top topics.

Demander a Claude : "Liste mes 10 derniers SERPs thruuu." Claude appelle thruuu_list_serps(per_page=10).

### Smoke test manuel (apres activation)

Une fois THRUUU_API_KEY ajoute au .env et .mcp.json mis a jour, relancer Claude Code. Le serveur devrait apparaitre dans la liste MCP. Tester avec un keyword peu couteux (1 SERP = 1 credit).

---

## Plan C - Workflow n8n

**Location** : systems/n8n/workflows/thruuu-serp-analysis.json

### Architecture

    Manual Trigger
        |
    Config (Set node : keyword, country, language, sheet_id, ...)
        |
    thruuu Submit (HTTP POST avec webhook_url = $execution.resumeUrl)
        |
    Wait for thruuu callback (resume webhook, timeout 10 min)
        |
    Extract Brief (Code node : flatten SERP -> brief editorial)
        |
        +-- Append to Sheets (1 ligne par analyse)
        +-- Notify Discord (resume + lien Sheets)

**Pourquoi Wait + webhook et pas polling ?** thruuu expose un parametre webhook_url qui callback a la completion. Le node Wait de n8n genere $execution.resumeUrl a la volee, on l'envoie a thruuu dans la requete POST, et n8n reprend l'execution quand le callback arrive. Beaucoup plus propre qu'une boucle polling + IF + Wait.

### Import dans n8n

1. Cote n8n (https://schoolswp-n8n.wp1.host) : Workflows -> Import from File -> selectionner thruuu-serp-analysis.json.
2. Ajouter THRUUU_API_KEY=... dans l'env n8n (docker-compose ou Settings -> Environment Variables) et redemarrer le container.
3. Configurer les credentials :
   - **Google Sheets OAuth2** sur le node "Append to Sheets"
   - **Discord Webhook** sur le node "Notify Discord"
4. Remplacer dans le node "Config" :
   - sheet_id -> l'ID de ton Google Sheet de tracking thruuu
   - discord_channel_id -> l'ID du channel Discord cible (Discord webhook suffit)
5. Creer un onglet thruuu-serps dans le Sheet avec les headers en ligne 1 :

       keyword | country | language | device | target_word_count | competitors_count | top_titles | top_urls | related_searches | people_also_ask | top_topics | analyzed_at | serp_id

### Tester

Manual Trigger -> modifier le keyword dans Config -> "Execute Workflow". Attendre 30s a 5 min selon la charge thruuu. La Wait node reprend des le callback recu.

### Extension possible

- Remplacer le Manual Trigger par un **Webhook Trigger** pour appel HTTP depuis Telegram/Discord/Form.
- Brancher en sortie un appel a thruuu-article-orchestrator (sub-agent) pour declencher la redaction d'article auto depuis le brief.
- Ajouter une boucle d'enrichissement DataForSEO (volumes, intentions) sur les related_searches.

### Validation

Le JSON a ete valide via mcp__n8n-mcp__validate_workflow : valid: true, 0 erreur, 0 connexion invalide, 7 nodes, 6 connexions, 9 expressions validees. Warnings cosmetiques resolus (typeVersions a jour, cachedResultName, onError sur HTTP/Sheets).

---

## Architecture cross-mode

                      +-------------------------------+
                      |   thruuu API v2 (Bearer)      |
                      |   https://api.thruuu.com/...  |
                      +--------------+----------------+
                                     |
            +------------------------+-------------------------+
            |                        |                         |
       +----v-----+         +--------v--------+       +--------v------+
       |  Plan A  |         |     Plan B      |       |    Plan C     |
       |  Client  | <------ |  Serveur MCP    |       |  Workflow n8n |
       |  Py      | import  |  (FastMCP)      |       |  (Wait+wh)    |
       +----+-----+         +-----------------+       +---------------+
            |
            | utilise par
            v
       core/agents-py/*
       (futurs agents qui veulent thruuu en backend)

Plan B et Plan C sont **independants de Plan A** cote runtime (B importe le client Py directement, C utilise un HTTP node n8n). Le sous-jacent est le meme : Bearer + POST /api/v2/serps + webhook ou polling.

---

## Couts (a valider sur ton plan)

| Action | Credits |
|---|---|
| 1 SERP standard (organic + headings + content + topics) | ~1 credit |
| include_llm avec chatgpt (Pro) | +1 credit |
| include_llm avec les 4 moteurs (Agency) | +4 credits |
| LLM engine qui fail | refund auto |

Surveiller le quota via thruuu_list_serps (Plan B) ou directement dans le dashboard thruuu.

---

## Roadmap (idees non implementees)

- Cache local des SERPs (Plan A) - eviter de rappeler thruuu pour un keyword analyse dans les N derniers jours
- Tool MCP thruuu_compare_serps (Plan B) - diff entre 2 SERPs pour suivi positions concurrents
- Workflow n8n batch (Plan C) - input = liste de keywords depuis Sheets, output = 1 ligne par SERP + declenchement orchestrator
- Integration directe dans agents.article_pipeline (remplace le --include-serp actuel par appel thruuu)

## Maintenance

- Si l'API thruuu change de shape de reponse : ajuster _extract_serp_ids et _serp_status dans tools/thruuu_client/client.py (parsing defensif deja en place).
- Si thruuu change l'endpoint : THRUUU_API_BASE en haut de client.py.
- Si la cle API leak : regenerer depuis le dashboard thruuu + mettre a jour .env + redemarrer Claude Code (Plan B) et le container n8n (Plan C).

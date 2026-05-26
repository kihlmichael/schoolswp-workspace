"""thruuu MCP Server - schoolsWP

Wrap MCP des endpoints SERP de l'API thruuu v2.
Source : https://thruuu.com/learn/serp-api/

Lance par Claude Code via le launcher tools/mcp-servers/_launch-thruuu.mjs.
Voir le launcher .mjs pour la commande d'invocation exacte (lit la cle, spawn fastmcp).

Le serveur reutilise tools/thruuu_client/client.py (meme couche d'auth + polling).

Tools exposes :
- thruuu_submit_serp     : POST async, retourne les ids (non-bloquant)
- thruuu_get_serp        : GET un SERP par id
- thruuu_list_serps      : liste paginee des SERPs du compte
- thruuu_analyze_serp    : end-to-end submit + wait (bloquant, parfait en session)
- thruuu_extract_brief   : convert un SERP complete en brief editorial structure
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path
from typing import Any

# tools/mcp-servers/thruuu/server.py -> root = parent.parent.parent
_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from fastmcp import FastMCP  # noqa: E402

from tools.thruuu_client.client import (  # noqa: E402
    SerpRequest,
    ThruuuClient,
    ThruuuError,
)

mcp = FastMCP("thruuu")

# Cache 1 client par process (FastMCP keep-alive sur stdio).
_client: ThruuuClient | None = None


def _get_client() -> ThruuuClient:
    global _client
    if _client is None:
        _client = ThruuuClient()
    return _client


def _build_request(
    keyword: str,
    country: str,
    language: str,
    device: str,
    num: int,
    include_llm: list[str] | None,
) -> SerpRequest:
    return SerpRequest(
        keywords=[keyword],
        country=country,
        language=language,
        device=device,
        num=num,
        include_llm=include_llm or [],
    )


@mcp.tool()
async def thruuu_submit_serp(
    keyword: str,
    country: str = "fr",
    language: str = "fr",
    device: str = "desktop",
    num: int = 10,
    include_llm: list[str] | None = None,
) -> dict[str, Any]:
    """Submit a SERP scrape job to thruuu (async, non-blocking).

    Args:
        keyword: target search query
        country: ISO country code (fr, us, de, ...). Default fr.
        language: ISO language code. Default fr.
        device: desktop or mobile. Default desktop.
        num: number of organic results to return (1-100). Default 10.
        include_llm: optional list of LLM engines to also query
            (chatgpt, gemini, perplexity, google-ai). Costs 1 credit each.

    Returns:
        The raw submission response from thruuu (contains the job id(s) and status).
        Use thruuu_get_serp(id) afterwards to fetch results, or use thruuu_analyze_serp
        for an end-to-end call.
    """
    try:
        client = _get_client()
        req = _build_request(keyword, country, language, device, num, include_llm)
        return await client.submit(req)
    except ThruuuError as e:
        return {"error": str(e)}


@mcp.tool()
async def thruuu_get_serp(serp_id: str) -> dict[str, Any]:
    """Fetch a single SERP by id.

    Args:
        serp_id: the id returned by thruuu_submit_serp.

    Returns:
        Full SERP payload (status, organic results, headings, related, PAA, etc.)
        or an error key on failure.
    """
    try:
        return await _get_client().get(serp_id)
    except ThruuuError as e:
        return {"error": str(e)}


@mcp.tool()
async def thruuu_list_serps(page: int = 1, per_page: int = 20) -> dict[str, Any]:
    """List recent SERPs from the thruuu account (paginated).

    Args:
        page: page number, 1-indexed.
        per_page: results per page (1-100).

    Returns:
        Paginated SERP list.
    """
    try:
        return await _get_client().list(page=page, per_page=per_page)
    except ThruuuError as e:
        return {"error": str(e)}


@mcp.tool()
async def thruuu_analyze_serp(
    keyword: str,
    country: str = "fr",
    language: str = "fr",
    device: str = "desktop",
    num: int = 10,
    include_llm: list[str] | None = None,
    poll_interval: float = 5.0,
    timeout: float = 300.0,
) -> dict[str, Any]:
    """End-to-end: submit a SERP, poll until done, return the full result.

    Best for interactive use in session (analyse-moi la SERP X maintenant).
    Blocks until completion or timeout. For batch / long-running, prefer
    thruuu_submit_serp + thruuu_get_serp later.

    Args: same as thruuu_submit_serp, plus:
        poll_interval: seconds between status polls. Default 5s.
        timeout: max seconds to wait. Default 300s (5 min).

    Returns:
        The completed SERP payload, or an error key on failure / timeout.
    """
    try:
        client = _get_client()
        req = _build_request(keyword, country, language, device, num, include_llm)
        results = await client.analyze(req, poll_interval=poll_interval, timeout=timeout)
        # 1 keyword -> 1 SERP. On retourne directement le SERP, pas la liste.
        return results[0] if results else {"error": "no SERP returned"}
    except ThruuuError as e:
        return {"error": str(e)}


@mcp.tool()
async def thruuu_extract_brief(serp_id: str) -> dict[str, Any]:
    """Extract a structured editorial brief from a completed SERP.

    Fetch the SERP and project the most useful fields for content production :
    competitor titles + URLs, headings (H1/H2/H3) from top results, related
    searches, people also ask, top topics / NLP entities, word count target.

    Args:
        serp_id: the id of a SERP that is already done.

    Returns:
        A flattened brief dict, or an error key if the SERP is not done yet
        or fetch failed.
    """
    try:
        serp = await _get_client().get(serp_id)
    except ThruuuError as e:
        return {"error": str(e)}

    status = (serp.get("status") or serp.get("state") or "").lower()
    if status and status not in {"done", "completed", "ready", "success", "finished"}:
        return {"error": f"SERP not ready, status={status}"}

    organic = serp.get("organic") or serp.get("results") or serp.get("organic_results") or []
    if not isinstance(organic, list):
        organic = []

    competitors = []
    word_counts = []
    headings_pool: list[dict[str, Any]] = []
    for item in organic[:10]:
        if not isinstance(item, dict):
            continue
        competitors.append(
            {
                "position": item.get("position") or item.get("rank"),
                "title": item.get("title"),
                "url": item.get("url") or item.get("link"),
                "meta_description": item.get("description") or item.get("meta_description"),
                "word_count": item.get("word_count") or item.get("words"),
            }
        )
        wc = item.get("word_count") or item.get("words")
        if isinstance(wc, (int, float)):
            word_counts.append(int(wc))
        h = item.get("headings") or item.get("structure")
        if h:
            headings_pool.append({"url": item.get("url"), "headings": h})

    avg_wc = int(sum(word_counts) / len(word_counts)) if word_counts else None

    return {
        "keyword": serp.get("keyword") or serp.get("query"),
        "search_engine": serp.get("search_engine"),
        "country": serp.get("country"),
        "language": serp.get("language"),
        "device": serp.get("device"),
        "target_word_count": avg_wc,
        "competitors": competitors,
        "headings_pool": headings_pool,
        "related_searches": serp.get("related_searches") or [],
        "people_also_ask": serp.get("people_also_ask") or serp.get("similar_questions") or serp.get("paa") or [],
        "top_topics": serp.get("top_topics") or serp.get("topics") or [],
        "_raw_status": status,
    }


if __name__ == "__main__":
    # Permet python server.py pour debug local, sinon le runtime FastMCP
    # est invoque via le launcher .mjs depuis Claude Code.
    asyncio.run(mcp.run_async())  # type: ignore[attr-defined]

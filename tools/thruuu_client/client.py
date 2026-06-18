"""thruuu SERP API client.

Wrap minimal de l'API v2 documentee sur https://thruuu.com/learn/serp-api/.

Endpoints exposes :
- POST /api/v2/serps        -> submit (lance une analyse SERP, asynchrone)
- GET  /api/v2/serps/       -> list  (liste paginee)
- GET  /api/v2/serps/:id    -> get   (recupere un job)

Helpers :
- wait_for(serp_id)         -> polling jusqu'au statut "done"
- analyze(request)          -> submit + wait_for end-to-end

Auth : Bearer token via THRUUU_API_KEY (charge depuis .env racine projet).
"""

from __future__ import annotations

import asyncio
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

THRUUU_API_BASE = "https://api.thruuu.com/api/v2"
DEFAULT_POLL_INTERVAL = 5.0
DEFAULT_POLL_TIMEOUT = 300.0
DEFAULT_HTTP_TIMEOUT = 30.0

_logger = logging.getLogger("thruuu")


def _load_dotenv_once() -> None:
    """Charge le .env racine projet schoolsWP si python-dotenv est dispo."""
    try:
        from dotenv import load_dotenv  # type: ignore[import-untyped]
    except ImportError:
        return
    # tools/thruuu-client/client.py -> root = parent.parent.parent
    root = Path(__file__).resolve().parent.parent.parent
    env_file = root / ".env"
    if env_file.exists():
        load_dotenv(env_file, override=False)


_load_dotenv_once()


class ThruuuError(Exception):
    """Erreur API ou polling thruuu."""


class ThruuuTimeout(ThruuuError):
    """Le polling a expire avant que le SERP soit pret."""


@dataclass
class SerpRequest:
    """Requete SERP thruuu. 1 keyword = 1 SERP (ou plus en bulk).

    Defaults FR + desktop + Google + analyse complete (headings, content, topics).
    """

    keywords: list[str]
    country: str = "fr"
    language: str = "fr"
    device: str = "desktop"
    num: int = 10
    search_volume: bool = True
    analyze_headings: bool = True
    analyze_content: bool = True
    analyze_top_topics: bool = True
    include_llm: list[str] = field(default_factory=list)
    webhook_url: str | None = None
    minified_response: bool = False
    search_engine: str = "google"

    def to_payload(self) -> dict[str, Any]:
        parameters: dict[str, Any] = {
            "search_engine": self.search_engine,
            "country": self.country,
            "language": self.language,
            "device": self.device,
            "num": self.num,
            "search_volume": self.search_volume,
            "analyze_headings": self.analyze_headings,
            "analyze_content": self.analyze_content,
            "analyze_top_topics": self.analyze_top_topics,
        }
        payload: dict[str, Any] = {
            "keywords": self.keywords,
            "parameters": parameters,
        }
        if self.include_llm:
            payload["include_llm"] = self.include_llm
        if self.webhook_url:
            payload["webhook_url"] = self.webhook_url
        if self.minified_response:
            payload["minified_response"] = True
        return payload


def _extract_serp_ids(submission: dict[str, Any]) -> list[str]:
    """Recupere les ids des SERPs cree(s) - tolerant a la forme de la reponse.

    L'API peut renvoyer differents wrappers (data, serps, items, list ou objet seul).
    On essaie plusieurs cles, puis on tombe sur l'objet racine si rien ne matche.
    """
    for key in ("data", "serps", "items", "results"):
        items = submission.get(key)
        if isinstance(items, list):
            return [str(it.get("id") or it.get("_id")) for it in items if it.get("id") or it.get("_id")]
    # cas reponse = un seul objet SERP
    sid = submission.get("id") or submission.get("_id")
    if sid:
        return [str(sid)]
    return []


def _serp_status(serp: dict[str, Any]) -> str | None:
    """Status courant du SERP - cherche plusieurs cles connues."""
    for key in ("status", "state", "scrape_status"):
        v = serp.get(key)
        if v:
            return str(v).lower()
    return None


_TERMINAL_OK = {"done", "completed", "ready", "success", "finished"}
_TERMINAL_FAIL = {"failed", "error", "errored"}


class ThruuuClient:
    """Client HTTP asynchrone pour l'API SERP thruuu."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = THRUUU_API_BASE,
        http_timeout: float = DEFAULT_HTTP_TIMEOUT,
    ):
        key = api_key or os.environ.get("THRUUU_API_KEY")
        if not key:
            raise ThruuuError("THRUUU_API_KEY absent. Ajoute-le au .env racine projet ou passe api_key=...")
        self._api_key = key
        self._base_url = base_url.rstrip("/")
        self._http_timeout = http_timeout

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "User-Agent": "schoolswp-thruuu-client/0.1",
        }

    async def submit(self, request: SerpRequest) -> dict[str, Any]:
        """POST /serps - lance une analyse SERP. Retourne le wrapper de creation."""
        async with httpx.AsyncClient(timeout=self._http_timeout) as client:
            resp = await client.post(
                f"{self._base_url}/serps",
                headers=self._headers,
                json=request.to_payload(),
            )
        if resp.status_code >= 400:
            raise ThruuuError(f"submit failed [{resp.status_code}] {resp.text[:500]}")
        data = resp.json()
        _logger.info("submitted %d keyword(s) - ids=%s", len(request.keywords), _extract_serp_ids(data))
        return data

    async def get(self, serp_id: str) -> dict[str, Any]:
        """GET /serps/:id - recupere un SERP par id."""
        async with httpx.AsyncClient(timeout=self._http_timeout) as client:
            resp = await client.get(
                f"{self._base_url}/serps/{serp_id}",
                headers=self._headers,
            )
        if resp.status_code >= 400:
            raise ThruuuError(f"get {serp_id} failed [{resp.status_code}] {resp.text[:500]}")
        return resp.json()

    async def list(self, page: int = 1, per_page: int = 20) -> dict[str, Any]:
        """GET /serps/ - liste paginee."""
        async with httpx.AsyncClient(timeout=self._http_timeout) as client:
            resp = await client.get(
                f"{self._base_url}/serps/",
                headers=self._headers,
                params={"page": page, "per_page": per_page},
            )
        if resp.status_code >= 400:
            raise ThruuuError(f"list failed [{resp.status_code}] {resp.text[:500]}")
        return resp.json()

    async def wait_for(
        self,
        serp_id: str,
        poll_interval: float = DEFAULT_POLL_INTERVAL,
        timeout: float = DEFAULT_POLL_TIMEOUT,
    ) -> dict[str, Any]:
        """Polling jusqu'au statut terminal (done) ou timeout."""
        elapsed = 0.0
        while elapsed < timeout:
            serp = await self.get(serp_id)
            status = _serp_status(serp)
            _logger.debug("poll %s status=%s elapsed=%.0fs", serp_id, status, elapsed)
            if status in _TERMINAL_OK:
                return serp
            if status in _TERMINAL_FAIL:
                raise ThruuuError(f"job {serp_id} failed terminal status={status} payload={serp}")
            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
        raise ThruuuTimeout(f"job {serp_id} not done within {timeout:.0f}s")

    async def analyze(
        self,
        request: SerpRequest,
        poll: bool = True,
        poll_interval: float = DEFAULT_POLL_INTERVAL,
        timeout: float = DEFAULT_POLL_TIMEOUT,
    ) -> list[dict[str, Any]]:
        """End-to-end : submit + (optionnel) wait_for sur chaque SERP retourne.

        Retourne la liste des SERPs (1 par keyword). Si poll=False, retourne les
        objets bruts de la creation (pas encore enrichis avec les resultats SERP).
        """
        submission = await self.submit(request)
        ids = _extract_serp_ids(submission)
        if not ids:
            raise ThruuuError(f"aucun id SERP dans la reponse submit : {submission}")
        if not poll:
            # renvoie la liste des objets bruts si disponible, sinon refait un get rapide
            raw = submission.get("data") or submission.get("serps")
            if isinstance(raw, list):
                return raw
            return [await self.get(sid) for sid in ids]
        results = await asyncio.gather(*[self.wait_for(sid, poll_interval, timeout) for sid in ids])
        return list(results)

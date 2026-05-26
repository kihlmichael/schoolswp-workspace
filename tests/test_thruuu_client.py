"""Tests unitaires pour tools.thruuu_client.

Pas d'appel reseau : on mocke httpx.AsyncClient avec respx ou directement avec
monkeypatch + AsyncMock. Ici on prend l'approche legere (monkeypatch).
"""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

# Ajoute la racine projet a sys.path pour importer tools.thruuu_client
_ROOT = Path(__file__).parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tools.thruuu_client.client import (  # noqa: E402
    SerpRequest,
    ThruuuClient,
    ThruuuError,
    ThruuuTimeout,
    _extract_serp_ids,
    _serp_status,
)

# ----------------- helpers parsing --------------------------------


def test_extract_serp_ids_from_data_wrapper():
    payload = {"data": [{"id": "abc"}, {"id": "def"}]}
    assert _extract_serp_ids(payload) == ["abc", "def"]


def test_extract_serp_ids_from_serps_wrapper():
    payload = {"serps": [{"_id": "xyz"}]}
    assert _extract_serp_ids(payload) == ["xyz"]


def test_extract_serp_ids_single_object():
    payload = {"id": "single", "status": "queued"}
    assert _extract_serp_ids(payload) == ["single"]


def test_extract_serp_ids_empty_when_no_match():
    payload = {"foo": "bar"}
    assert _extract_serp_ids(payload) == []


def test_serp_status_picks_first_known_key():
    assert _serp_status({"status": "DONE"}) == "done"
    assert _serp_status({"state": "Queued"}) == "queued"
    assert _serp_status({"scrape_status": "running"}) == "running"
    assert _serp_status({"unknown": "x"}) is None


# ----------------- SerpRequest payload ----------------------------


def test_serp_request_default_payload():
    req = SerpRequest(keywords=["foo"])
    payload = req.to_payload()
    assert payload["keywords"] == ["foo"]
    assert payload["parameters"]["country"] == "fr"
    assert payload["parameters"]["device"] == "desktop"
    assert payload["parameters"]["num"] == 10
    assert "include_llm" not in payload
    assert "webhook_url" not in payload


def test_serp_request_with_llm_and_webhook():
    req = SerpRequest(
        keywords=["bar"],
        include_llm=["chatgpt", "gemini"],
        webhook_url="https://example.com/hook",
        minified_response=True,
    )
    payload = req.to_payload()
    assert payload["include_llm"] == ["chatgpt", "gemini"]
    assert payload["webhook_url"] == "https://example.com/hook"
    assert payload["minified_response"] is True


# ----------------- ThruuuClient init ------------------------------


def test_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("THRUUU_API_KEY", raising=False)
    with pytest.raises(ThruuuError, match="THRUUU_API_KEY"):
        ThruuuClient()


def test_client_uses_env_api_key(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "test-token-123")
    client = ThruuuClient()
    assert client._headers["Authorization"] == "Bearer test-token-123"


def test_client_uses_explicit_api_key(monkeypatch):
    monkeypatch.delenv("THRUUU_API_KEY", raising=False)
    client = ThruuuClient(api_key="explicit-key")
    assert client._headers["Authorization"] == "Bearer explicit-key"


# ----------------- HTTP methods mocked ----------------------------


def _make_http_response(status: int, json_body: dict, text: str = ""):
    resp = MagicMock()
    resp.status_code = status
    resp.json = MagicMock(return_value=json_body)
    resp.text = text or str(json_body)
    return resp


def _patch_async_client(monkeypatch, response):
    """Remplace httpx.AsyncClient pour qu'il retourne `response` sur tous les verbes."""
    mock_instance = AsyncMock()
    mock_instance.post = AsyncMock(return_value=response)
    mock_instance.get = AsyncMock(return_value=response)
    mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
    mock_instance.__aexit__ = AsyncMock(return_value=None)

    mock_ctor = MagicMock(return_value=mock_instance)
    monkeypatch.setattr("tools.thruuu_client.client.httpx.AsyncClient", mock_ctor)
    return mock_instance


async def test_submit_returns_json(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    body = {"data": [{"id": "abc", "status": "queued"}]}
    _patch_async_client(monkeypatch, _make_http_response(200, body))
    client = ThruuuClient()
    result = await client.submit(SerpRequest(keywords=["x"]))
    assert result == body


async def test_submit_raises_on_4xx(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    _patch_async_client(monkeypatch, _make_http_response(401, {}, "Unauthorized"))
    client = ThruuuClient()
    with pytest.raises(ThruuuError, match="submit failed"):
        await client.submit(SerpRequest(keywords=["x"]))


async def test_get_returns_json(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    body = {"id": "abc", "status": "done", "results": []}
    _patch_async_client(monkeypatch, _make_http_response(200, body))
    client = ThruuuClient()
    result = await client.get("abc")
    assert result["status"] == "done"


async def test_wait_for_returns_when_done(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    body = {"id": "abc", "status": "done"}
    _patch_async_client(monkeypatch, _make_http_response(200, body))
    client = ThruuuClient()
    result = await client.wait_for("abc", poll_interval=0.01, timeout=1.0)
    assert result == body


async def test_wait_for_raises_on_failure(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    body = {"id": "abc", "status": "failed"}
    _patch_async_client(monkeypatch, _make_http_response(200, body))
    client = ThruuuClient()
    with pytest.raises(ThruuuError, match="failed terminal"):
        await client.wait_for("abc", poll_interval=0.01, timeout=1.0)


async def test_wait_for_times_out(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    body = {"id": "abc", "status": "queued"}
    _patch_async_client(monkeypatch, _make_http_response(200, body))
    client = ThruuuClient()
    with pytest.raises(ThruuuTimeout):
        await client.wait_for("abc", poll_interval=0.01, timeout=0.05)


async def test_analyze_end_to_end(monkeypatch):
    monkeypatch.setenv("THRUUU_API_KEY", "k")
    # submit renvoie un id, get renvoie status=done immediatement
    body = {"data": [{"id": "abc", "status": "queued"}]}
    done = {"id": "abc", "status": "done", "results": [{"position": 1}]}

    mock_instance = AsyncMock()
    mock_instance.post = AsyncMock(return_value=_make_http_response(200, body))
    mock_instance.get = AsyncMock(return_value=_make_http_response(200, done))
    mock_instance.__aenter__ = AsyncMock(return_value=mock_instance)
    mock_instance.__aexit__ = AsyncMock(return_value=None)
    monkeypatch.setattr(
        "tools.thruuu_client.client.httpx.AsyncClient",
        MagicMock(return_value=mock_instance),
    )

    client = ThruuuClient()
    results = await client.analyze(SerpRequest(keywords=["x"]), poll_interval=0.01, timeout=1.0)
    assert len(results) == 1
    assert results[0]["status"] == "done"

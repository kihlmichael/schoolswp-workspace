"""Fixtures and import setup for schoolsWP agent tests."""

import importlib.util
import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

# ── Import aliasing ─────────────────────────────────────────────
# The real agent code lives in core/agents-py/ but is imported as
# "agents.*" at runtime (CLIs add project root to sys.path).
# We register core/agents-py/ as the "agents" package so pytest
# can resolve "from agents.base import ..." without path hacks.
_PROJECT_ROOT = Path(__file__).parent.parent
_AGENTS_SRC = _PROJECT_ROOT / "core" / "agents-py"

if "agents" not in sys.modules:
    spec = importlib.util.spec_from_file_location(
        "agents",
        _AGENTS_SRC / "__init__.py",
        submodule_search_locations=[str(_AGENTS_SRC)],
    )
    mod = importlib.util.module_from_spec(spec)
    mod.__path__ = [str(_AGENTS_SRC)]
    sys.modules["agents"] = mod
    spec.loader.exec_module(mod)


# ── Fixtures ────────────────────────────────────────────────────


@pytest.fixture(autouse=True)
def _clear_provider_cache():
    """Clear the provider cache before each test to avoid cross-test pollution."""
    from agents.providers import clear_provider_cache

    clear_provider_cache()
    yield
    clear_provider_cache()


@pytest.fixture
def fake_env(monkeypatch):
    """Set minimal env vars so agents don't hit real APIs."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test-fake-key-for-testing")
    monkeypatch.setenv("MODEL_WRITER", "claude-sonnet-4-6")


@pytest.fixture
def mock_anthropic_client():
    """Factory: returns a mock AsyncAnthropic with a predictable response.

    Usage:
        agent._client = mock_anthropic_client("some response text")

    Note: Historique — préférer mock_provider pour les nouveaux tests.
    """

    def _factory(response_text: str = "Mock response"):
        client = AsyncMock()
        message = MagicMock()
        message.content = [MagicMock(text=response_text)]
        client.messages.create = AsyncMock(return_value=message)
        return client

    return _factory


@pytest.fixture
def mock_provider():
    """Factory: returns a mock LLMProvider with a predictable response.

    Usage:
        agent._provider = mock_provider("some response text")
    """
    from agents.providers.base import LLMResponse

    def _factory(response_text: str = "Mock response"):
        provider = AsyncMock()
        provider.complete = AsyncMock(return_value=LLMResponse(text=response_text))
        return provider

    return _factory


@pytest.fixture
def tmp_article(tmp_path):
    """Create a temporary markdown file for file-based tests."""
    article = tmp_path / "test-article.md"
    article.write_text(
        "# Test Article\n\nThis is a test article for unit testing.\n",
        encoding="utf-8",
    )
    return article

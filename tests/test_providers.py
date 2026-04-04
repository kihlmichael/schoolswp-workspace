"""Tests unitaires pour la couche providers LLM."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from agents.providers import resolve_provider
from agents.providers.base import LLMProvider, LLMRequest, LLMResponse


def _openai_available() -> bool:
    try:
        import openai  # noqa: F401

        return True
    except ImportError:
        return False


# ---------------------------------------------------------------------------
# LLMRequest / LLMResponse — construction et valeurs par défaut
# ---------------------------------------------------------------------------


class TestLLMRequest:
    def test_required_fields(self):
        req = LLMRequest(model="test", system="sys", user_message="hello")
        assert req.model == "test"
        assert req.system == "sys"
        assert req.user_message == "hello"
        assert req.max_tokens == 4096
        assert req.temperature is None
        assert req.stop_sequences is None

    def test_optional_fields(self):
        req = LLMRequest(
            model="test",
            system="sys",
            user_message="hello",
            max_tokens=1000,
            temperature=0.7,
            stop_sequences=["END"],
        )
        assert req.max_tokens == 1000
        assert req.temperature == 0.7
        assert req.stop_sequences == ["END"]


class TestLLMResponse:
    def test_defaults(self):
        resp = LLMResponse(text="output")
        assert resp.text == "output"
        assert resp.model == ""
        assert resp.input_tokens == 0
        assert resp.output_tokens == 0

    def test_with_metrics(self):
        resp = LLMResponse(text="output", model="gpt-4o", input_tokens=100, output_tokens=50)
        assert resp.model == "gpt-4o"
        assert resp.input_tokens == 100


# ---------------------------------------------------------------------------
# Parsing / routing factory
# ---------------------------------------------------------------------------


class TestResolveProvider:
    def test_anthropic_implicit_claude_model(self, fake_env):
        provider, model = resolve_provider("claude-sonnet-4-6")
        assert model == "claude-sonnet-4-6"
        from agents.providers.anthropic import AnthropicProvider

        assert isinstance(provider, AnthropicProvider)

    def test_anthropic_explicit_prefix(self, fake_env):
        provider, model = resolve_provider("anthropic:claude-opus-4")
        assert model == "claude-opus-4"
        from agents.providers.anthropic import AnthropicProvider

        assert isinstance(provider, AnthropicProvider)

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_openai_prefix(self, fake_env, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        provider, model = resolve_provider("openai:gpt-4o")
        assert model == "gpt-4o"
        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(provider, OpenAICompatProvider)

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_gemini_prefix(self, fake_env, monkeypatch):
        monkeypatch.setenv("GEMINI_API_KEY", "AI-test")
        provider, model = resolve_provider("gemini:gemini-2.0-flash")
        assert model == "gemini-2.0-flash"
        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(provider, OpenAICompatProvider)

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_deepseek_prefix(self, fake_env, monkeypatch):
        monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-test")
        provider, model = resolve_provider("deepseek:deepseek-chat")
        assert model == "deepseek-chat"

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_ollama_with_colon_in_model(self, fake_env):
        """Split sur le premier ':' uniquement — ollama:llama3.3:70b."""
        provider, model = resolve_provider("ollama:llama3.3:70b")
        assert model == "llama3.3:70b"
        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(provider, OpenAICompatProvider)

    def test_unknown_prefix_falls_back_to_anthropic(self, fake_env):
        """Un préfixe inconnu est traité comme un nom de modèle Anthropic."""
        provider, model = resolve_provider("custom-model-v1")
        assert model == "custom-model-v1"
        from agents.providers.anthropic import AnthropicProvider

        assert isinstance(provider, AnthropicProvider)


# ---------------------------------------------------------------------------
# Contrat LLMProvider — protocol check
# ---------------------------------------------------------------------------


class TestProviderProtocol:
    def test_anthropic_satisfies_protocol(self, fake_env):
        from agents.providers.anthropic import AnthropicProvider

        assert isinstance(AnthropicProvider(), LLMProvider)

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_openai_compat_satisfies_protocol(self, fake_env):
        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(OpenAICompatProvider(api_key="test", base_url="http://localhost"), LLMProvider)


# ---------------------------------------------------------------------------
# AnthropicProvider.complete — mock
# ---------------------------------------------------------------------------


class TestAnthropicProviderComplete:
    async def test_complete_returns_llm_response(self, fake_env):
        from agents.providers.anthropic import AnthropicProvider

        provider = AnthropicProvider()

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Hello from Claude")]
        mock_response.model = "claude-sonnet-4-6"
        mock_response.usage = MagicMock(input_tokens=10, output_tokens=20)
        provider._client = MagicMock()
        provider._client.messages = MagicMock()
        provider._client.messages.create = AsyncMock(return_value=mock_response)

        request = LLMRequest(model="claude-sonnet-4-6", system="Be helpful", user_message="Hi")
        response = await provider.complete(request)

        assert response.text == "Hello from Claude"
        assert response.model == "claude-sonnet-4-6"
        assert response.input_tokens == 10
        assert response.output_tokens == 20

    async def test_complete_passes_optional_params(self, fake_env):
        from agents.providers.anthropic import AnthropicProvider

        provider = AnthropicProvider()

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="response")]
        mock_response.model = "claude-sonnet-4-6"
        mock_response.usage = None
        provider._client = MagicMock()
        provider._client.messages = MagicMock()
        provider._client.messages.create = AsyncMock(return_value=mock_response)

        request = LLMRequest(
            model="claude-sonnet-4-6",
            system="sys",
            user_message="msg",
            temperature=0.5,
            stop_sequences=["END"],
        )
        await provider.complete(request)

        call_kwargs = provider._client.messages.create.call_args[1]
        assert call_kwargs["temperature"] == 0.5
        assert call_kwargs["stop_sequences"] == ["END"]

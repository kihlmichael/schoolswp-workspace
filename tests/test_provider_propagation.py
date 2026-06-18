"""Tests de regression pour la propagation du model prefix aux sub-agents.

Bug originel (corrige 2026-05-26) : BaseContentAgent.__init__ stockait
self.model = model_name_clean (sans prefixe provider), et les pipelines
(publish_ready, content_factory, article_pipeline, etc.) propageaient
ce model_name aux sub-agents via `model=self.model`. Resultat : un sub-agent
recevait `gpt-4o-mini` au lieu de `openai:gpt-4o-mini`, et tombait
silencieusement en fallback Anthropic via la regle "pas de prefixe = anthropic"
de _parse_model_string.

Fix : BaseContentAgent.__init__ stocke aussi self.raw_model (chaine complete
avec prefixe), et les pipelines propagent via `model=self.raw_model`.
"""

import pytest

from agents.base import BaseContentAgent


def _openai_available() -> bool:
    try:
        import openai  # noqa: F401

        return True
    except ImportError:
        return False


class _DummyAgent(BaseContentAgent):
    name = "dummy"
    system_prompt = "You are dummy."


class TestRawModelPreservation:
    """self.raw_model doit conserver la chaine model complete avec prefixe."""

    def test_anthropic_implicit(self, fake_env):
        agent = _DummyAgent(model="claude-sonnet-4-6")
        assert agent.raw_model == "claude-sonnet-4-6"
        assert agent.model == "claude-sonnet-4-6"

    def test_anthropic_explicit_prefix(self, fake_env):
        agent = _DummyAgent(model="anthropic:claude-opus-4")
        assert agent.raw_model == "anthropic:claude-opus-4"
        assert agent.model == "claude-opus-4"

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_openai_prefix_preserved(self, fake_env, monkeypatch):
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        agent = _DummyAgent(model="openai:gpt-4o-mini")
        assert agent.raw_model == "openai:gpt-4o-mini"
        assert agent.model == "gpt-4o-mini"

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_gemini_prefix_preserved(self, fake_env, monkeypatch):
        monkeypatch.setenv("GEMINI_API_KEY", "AI-test")
        agent = _DummyAgent(model="gemini:gemini-2.0-flash")
        assert agent.raw_model == "gemini:gemini-2.0-flash"
        assert agent.model == "gemini-2.0-flash"

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_ollama_with_colon_in_model_preserved(self, fake_env):
        agent = _DummyAgent(model="ollama:llama3.3:70b")
        assert agent.raw_model == "ollama:llama3.3:70b"
        assert agent.model == "llama3.3:70b"


class TestPropagationToSubAgent:
    """Regression : creer un sub-agent avec parent.raw_model doit preserver le provider."""

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_propagation_openai_to_sub_agent(self, fake_env, monkeypatch):
        """Le bug originel : sub-agent recevait gpt-4o-mini sans prefixe -> fallback Anthropic."""
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        parent = _DummyAgent(model="openai:gpt-4o-mini")

        # Pattern de fan-out reel (publish_ready/agent.py, content_factory/agent.py, etc.)
        sub_agent = _DummyAgent(model=parent.raw_model)

        # Le sub-agent doit ressortir avec un OpenAICompatProvider, pas un AnthropicProvider
        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(sub_agent._provider, OpenAICompatProvider), (
            "Bug regression : sub-agent fallback vers Anthropic au lieu d'OpenAI"
        )
        assert sub_agent.model == "gpt-4o-mini"
        assert sub_agent.raw_model == "openai:gpt-4o-mini"

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_propagation_gemini_to_sub_agent(self, fake_env, monkeypatch):
        monkeypatch.setenv("GEMINI_API_KEY", "AI-test")
        parent = _DummyAgent(model="gemini:gemini-2.0-flash")
        sub_agent = _DummyAgent(model=parent.raw_model)

        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(sub_agent._provider, OpenAICompatProvider)
        assert sub_agent.raw_model == "gemini:gemini-2.0-flash"

    def test_anthropic_propagation_unchanged(self, fake_env):
        """Le cas Anthropic natif n'est pas casse par le fix."""
        parent = _DummyAgent(model="claude-sonnet-4-6")
        sub_agent = _DummyAgent(model=parent.raw_model)

        from agents.providers.anthropic import AnthropicProvider

        assert isinstance(sub_agent._provider, AnthropicProvider)
        assert sub_agent.model == "claude-sonnet-4-6"


class TestBugReproduction:
    """Test qui aurait FAILED avant le fix - protection regression."""

    @pytest.mark.skipif(not _openai_available(), reason="openai SDK not installed")
    def test_old_bug_using_self_model_falls_to_anthropic(self, fake_env, monkeypatch):
        """Demontre le bug originel : utiliser self.model (sans prefixe) tombe en Anthropic.

        Ce test prouve que le bug existait : il VERIFIE que le mauvais usage
        (model=parent.model au lieu de model=parent.raw_model) reproduit bien
        le fallback Anthropic. C'est la garantie que notre fix etait necessaire.
        """
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        parent = _DummyAgent(model="openai:gpt-4o-mini")

        # Pattern OLD bug : propagation via self.model (sans prefixe)
        sub_agent_old_pattern = _DummyAgent(model=parent.model)

        from agents.providers.anthropic import AnthropicProvider

        # Le sub-agent tombait en Anthropic au lieu d'OpenAI - c'est le bug
        assert isinstance(sub_agent_old_pattern._provider, AnthropicProvider), (
            "Si ce test fail, c'est que _parse_model_string a change de regle "
            "et le bug originel ne se manifeste plus. Verifier que le fix tient toujours."
        )

"""Contract tests: every agent must satisfy BaseContentAgent interface."""

import pytest

from agents.base import BaseContentAgent


def _openai_sdk_available() -> bool:
    try:
        import openai  # noqa: F401

        return True
    except ImportError:
        return False


def _load_agent_classes():
    """Lazily import agent classes — skip any that fail to import."""
    agents = []
    imports = [
        ("agents.seo_auditor.agent", "SeoAuditorAgent"),
        ("agents.seo_writer.agent", "SeoWriterAgent"),
        ("agents.conversion_auditor.agent", "ConversionAuditorAgent"),
        ("agents.llm_seo.agent", "LlmSeoAgent"),
        ("agents.topical_authority.agent", "TopicalAuthorityAgent"),
        ("agents.knowledge_graph.agent", "KnowledgeGraphAgent"),
        ("agents.pillar_authority.agent", "PillarAuthorityAgent"),
        ("agents.cocon_builder.agent", "CoconBuilderAgent"),
        ("agents.cluster_architect.agent", "ClusterArchitectAgent"),
        ("agents.automation_consultant.agent", "AutomationConsultantAgent"),
        ("agents.plugin_comparator.agent", "PluginComparatorAgent"),
        ("agents.lms_trainer.agent", "LmsTrainerAgent"),
        ("agents.niche_scout.agent", "NicheScoutAgent"),
        ("agents.strategic_brain.agent", "StrategicBrainAgent"),
    ]
    for module_path, class_name in imports:
        try:
            import importlib

            mod = importlib.import_module(module_path)
            cls = getattr(mod, class_name)
            agents.append(cls)
        except (ImportError, AttributeError):
            pass
    return agents


_AGENT_CLASSES = _load_agent_classes()


@pytest.mark.parametrize("agent_class", _AGENT_CLASSES, ids=lambda c: c.name if hasattr(c, "name") else c.__name__)
class TestAgentContract:
    """Every agent must satisfy the BaseContentAgent contract."""

    def test_inherits_base(self, agent_class):
        assert issubclass(agent_class, BaseContentAgent)

    def test_has_name(self, agent_class):
        assert hasattr(agent_class, "name")
        assert isinstance(agent_class.name, str)
        assert agent_class.name != "base"

    def test_has_system_prompt(self, agent_class):
        assert hasattr(agent_class, "system_prompt")
        assert len(agent_class.system_prompt) > 0

    def test_instantiates_with_default_model(self, fake_env, agent_class):
        agent = agent_class()
        assert agent.model == "claude-sonnet-4-6"

    def test_instantiates_with_custom_model(self, fake_env, agent_class):
        agent = agent_class(model="claude-opus-4")
        assert agent.model == "claude-opus-4"

    @pytest.mark.skipif(not _openai_sdk_available(), reason="openai SDK not installed")
    def test_instantiates_with_provider_prefix(self, fake_env, monkeypatch, agent_class):
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
        agent = agent_class(model="openai:gpt-4o")
        assert agent.model == "gpt-4o"
        from agents.providers.openai_compat import OpenAICompatProvider

        assert isinstance(agent._provider, OpenAICompatProvider)

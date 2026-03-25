"""Contract tests for ContentFactoryAgent — ContentFactoryResult dataclass and wiring."""

from agents.content_factory.agent import (
    ContentFactoryAgent,
    ContentFactoryResult,
    _build_factory_report,
)
from agents.conversion_auditor.agent import ConversionAuditResult
from agents.llm_seo.agent import CitationSignalResult
from agents.publish_ready.agent import PublishReadyResult
from agents.seo_auditor.agent import AuditResult
from agents.topical_authority.agent import TopicalAuditResult

# ── ContentFactoryResult dataclass ─────────────────────────────────


class TestContentFactoryResultDefaults:
    """Default values are sane."""

    def test_defaults(self):
        r = ContentFactoryResult()
        assert r.keyword == ""
        assert r.intent == ""
        assert r.pillar == ""
        assert r.topic == ""
        assert r.article == ""
        assert r.roi_ok is True
        assert r.pipeline is None
        assert r.publish is None
        assert r.cluster_plan == ""
        assert r.factory_report == ""

    def test_publish_score_zero_without_publish(self):
        r = ContentFactoryResult()
        assert r.publish_score == 0

    def test_publish_emoji_dash_without_publish(self):
        r = ContentFactoryResult()
        assert r.publish_emoji == "—"

    def test_publish_diagnostic_dash_without_publish(self):
        r = ContentFactoryResult()
        assert r.publish_diagnostic == "—"


class TestContentFactoryResultPublishScore:
    """publish_score delegates to PublishReadyResult."""

    def test_delegates_to_publish(self):
        pub = PublishReadyResult(publish_score=84)
        r = ContentFactoryResult(publish=pub)
        assert r.publish_score == 84

    def test_emoji_delegates(self):
        pub = PublishReadyResult(publish_score=92)
        r = ContentFactoryResult(publish=pub)
        assert r.publish_emoji == "✅"


class TestContentFactoryResultBestArticle:
    """best_article returns the best available version."""

    def test_returns_article_if_set(self):
        r = ContentFactoryResult(article="Final article")
        assert r.best_article == "Final article"

    def test_empty_if_nothing(self):
        r = ContentFactoryResult()
        assert r.best_article == ""


class TestContentFactoryResultVersionLabel:
    """article_version_label reflects which version is available."""

    def test_fourni_without_pipeline(self):
        r = ContentFactoryResult()
        assert r.article_version_label == "Fourni"


class TestContentFactoryResultWordCount:
    """word_count counts words in best_article."""

    def test_counts_words(self):
        r = ContentFactoryResult(article="Un deux trois quatre cinq")
        assert r.word_count == 5

    def test_zero_when_empty(self):
        r = ContentFactoryResult()
        assert r.word_count == 0


# ── _build_factory_report ──────────────────────────────────────────


class TestBuildFactoryReport:
    """_build_factory_report produces markdown with key sections."""

    def test_includes_keyword(self):
        r = ContentFactoryResult(keyword="lms wordpress", intent="décisionnelle")
        report = _build_factory_report(r)
        assert "lms wordpress" in report

    def test_includes_strategy_section_when_topic_set(self):
        r = ContentFactoryResult(
            keyword="k",
            intent="i",
            topic="Mon sujet",
            angle="Un angle",
            audience="freelances",
        )
        report = _build_factory_report(r)
        assert "Stratégie éditoriale" in report
        assert "Mon sujet" in report

    def test_includes_publish_score_when_available(self):
        pub = PublishReadyResult(
            publish_score=84,
            seo_result=AuditResult(score_global=85),
            llm_result=CitationSignalResult(citation_score=80),
            conversion_result=ConversionAuditResult(score_conversion=90),
            authority_result=TopicalAuditResult(score_autorite=75),
            weakest_module="Citabilité IA",
        )
        r = ContentFactoryResult(keyword="k", intent="i", publish=pub)
        report = _build_factory_report(r)
        assert "84/100" in report
        assert "Publish Score" in report

    def test_includes_cluster_when_set(self):
        r = ContentFactoryResult(
            keyword="k",
            intent="i",
            cluster_plan="## Cluster\n- Article 1\n- Article 2",
        )
        report = _build_factory_report(r)
        assert "Article 1" in report


# ── ContentFactoryAgent contract ───────────────────────────────────


class TestContentFactoryAgentContract:
    """ContentFactoryAgent satisfies BaseContentAgent contract."""

    def test_agent_name(self):
        assert ContentFactoryAgent.name == "content-factory"

    def test_system_prompt_empty(self):
        # Orchestrator — no own system prompt
        assert ContentFactoryAgent.system_prompt == ""

    def test_instantiates_with_default_model(self, fake_env):
        agent = ContentFactoryAgent()
        assert agent.model == "claude-sonnet-4-6"

    def test_instantiates_with_custom_model(self, fake_env):
        agent = ContentFactoryAgent(model="claude-opus-4")
        assert agent.model == "claude-opus-4"

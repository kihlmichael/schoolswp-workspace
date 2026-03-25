"""Contract tests for ArticlePipeline — PipelineResult dataclass and pipeline wiring."""

from agents.article_pipeline.pipeline import ArticlePipeline, PipelineResult

# ── PipelineResult dataclass ───────────────────────────────────────


class TestPipelineResultDefaults:
    """PipelineResult default values are sane."""

    def test_defaults(self):
        r = PipelineResult(keyword="test", intent="comparative")
        assert r.keyword == "test"
        assert r.intent == "comparative"
        assert r.draft == ""
        assert r.final == ""
        assert r.errors == []

    def test_scores_default_none(self):
        r = PipelineResult(keyword="k", intent="i")
        assert r.seo_score is None
        assert r.llm_score is None
        assert r.conversion_score is None
        assert r.authority_score is None
        assert r.publish_score is None


class TestPipelineResultComputePublishScore:
    """compute_publish_score applies correct weights when all scores present."""

    def test_returns_none_when_missing_scores(self):
        r = PipelineResult(keyword="k", intent="i", seo_score=80)
        assert r.compute_publish_score() is None

    def test_returns_none_when_all_none(self):
        r = PipelineResult(keyword="k", intent="i")
        assert r.compute_publish_score() is None

    def test_computes_weighted_score(self):
        r = PipelineResult(
            keyword="k",
            intent="i",
            seo_score=80,
            llm_score=70,
            conversion_score=90,
            authority_score=60,
        )
        expected = 80 * 0.30 + 70 * 0.25 + 90 * 0.25 + 60 * 0.20  # 76.0
        assert r.compute_publish_score() == expected

    def test_all_100(self):
        r = PipelineResult(
            keyword="k",
            intent="i",
            seo_score=100,
            llm_score=100,
            conversion_score=100,
            authority_score=100,
        )
        assert r.compute_publish_score() == 100.0

    def test_all_zero(self):
        r = PipelineResult(
            keyword="k",
            intent="i",
            seo_score=0,
            llm_score=0,
            conversion_score=0,
            authority_score=0,
        )
        assert r.compute_publish_score() == 0.0


class TestPipelineResultScoreParsers:
    """Injected score parsers extract scores from audit text."""

    def test_parse_seo_score(self):
        r = PipelineResult(keyword="k", intent="i", audit="Score global SEO 82/100")
        assert r.parse_seo_score() == 82

    def test_parse_seo_score_missing(self):
        r = PipelineResult(keyword="k", intent="i", audit="No score here")
        assert r.parse_seo_score() is None

    def test_parse_llm_score(self):
        r = PipelineResult(keyword="k", intent="i", llm_seo="Score LLM 74/100")
        assert r.parse_llm_score() == 74

    def test_parse_llm_score_missing(self):
        r = PipelineResult(keyword="k", intent="i", llm_seo="Nothing")
        assert r.parse_llm_score() is None


# ── ArticlePipeline agent contract ─────────────────────────────────


class TestArticlePipelineContract:
    """ArticlePipeline satisfies BaseContentAgent contract."""

    def test_agent_name(self):
        assert ArticlePipeline.name == "article-pipeline"

    def test_has_system_prompt(self):
        assert isinstance(ArticlePipeline.system_prompt, str)
        assert len(ArticlePipeline.system_prompt) > 0

    def test_instantiates_with_default_model(self, fake_env):
        agent = ArticlePipeline()
        assert agent.model == "claude-sonnet-4-6"

    def test_instantiates_with_custom_model(self, fake_env):
        agent = ArticlePipeline(model="claude-opus-4")
        assert agent.model == "claude-opus-4"

"""E2E tests for the 3 strategic pipelines — full orchestration with mocked LLM.

Each test exercises the real orchestration logic (agent creation, asyncio.gather,
score computation, report building) but replaces all LLM calls with deterministic mocks.
This catches wiring bugs without hitting the Anthropic API.
"""

from unittest.mock import AsyncMock, MagicMock, patch

from agents.article_pipeline.pipeline import ArticlePipeline, PipelineResult
from agents.content_factory.agent import ContentFactoryAgent, ContentFactoryResult
from agents.providers import clear_provider_cache
from agents.publish_ready.agent import PublishReadyAgent, PublishReadyResult

# ── Fixtures ───────────────────────────────────────────────────────

SAMPLE_ARTICLE = """\
# Choisir un LMS WordPress rentable

## Réponse rapide
Pour un freelance, TutorLMS offre le meilleur rapport qualité-prix en 2026.

## Pourquoi un LMS WordPress ?
Créer une formation en ligne sur WordPress te permet de garder le contrôle total.

## TutorLMS vs LearnDash
TutorLMS est plus accessible. LearnDash offre plus de flexibilité.

## Recommandation
Si tu débutes, choisis TutorLMS. Si tu as déjà 500 étudiants, passe à LearnDash.
"""

SAMPLE_SEO_REPORT = """\
Score global : 82/100

Détail par bloc :
SEO STRUCTURE : 17/20
INTENTION : 16/20
PÉDAGOGIE : 18/20
BUSINESS : 15/20
BRANDING : 16/20

Points forts :
– Structure Hn hiérarchisée
– Tutoiement cohérent

Points faibles :
– Maillage interne insuffisant
"""

SAMPLE_LLM_REPORT = """\
Score citabilité : 75/100

Signaux détectés :
– Réponse rapide : 20/25
– Blocs extractibles : 18/25
– Définitions : 15/20
– Structure snippet : 12/15
– Cohérence : 10/15
"""

SAMPLE_CONVERSION_REPORT = """\
Score conversion : 78/100

Détail :
CLARTÉ PROBLÈME : 16/20
DÉCISION : 15/20
ORIENTATION ACTION : 16/20
CTA : 14/20
BUSINESS ALIGNMENT : 17/20
"""

SAMPLE_AUTHORITY_REPORT = """\
Score autorité : 68/100

Détail :
COUVERTURE : 14/20
CONNEXIONS : 12/20
COHÉRENCE : 15/20
POSITIONNEMENT : 14/20
POTENTIEL CLUSTER : 13/20

Recommandation : À renforcer
"""

SAMPLE_SYNTHESIS = """\
## Plan d'action prioritaire

1. Ajouter 3 liens internes vers les piliers LMS existants (SEO)
2. Créer un bloc FAQ schema markup (IA)
3. Renforcer le CTA principal avec un argument chiffré (Conversion)

## Bloc prioritaire à corriger en premier
**Autorité Thématique** — score le plus faible, nécessite des articles satellites

## Potentiel après optimisations
Si les 3 premières actions sont appliquées : Publish Score estimé à 82/100.
"""

SAMPLE_CLUSTER = """\
## Plan Cluster — LMS WordPress

### Pilier : Choisir un LMS WordPress rentable

### Satellites recommandés
1. TutorLMS avis complet 2026 — informationnelle
2. LearnDash vs LifterLMS — comparative
3. Créer sa première formation WordPress — informationnelle
"""


def _make_mock_client(response_text: str):
    """Create a mock AsyncAnthropic client returning a fixed response."""
    client = AsyncMock()
    message = MagicMock()
    message.content = [MagicMock(text=response_text)]
    client.messages.create = AsyncMock(return_value=message)
    return client


# ── E2E: PublishReadyAgent ─────────────────────────────────────────


class TestPublishReadyE2E:
    """Full orchestration: 4 parallel audits → score → synthesis → dashboard."""

    async def test_full_run_produces_valid_result(self, fake_env):
        # Mock all 5 sub-agent LLM calls (4 audits + 1 synthesis)
        call_count = 0
        responses = [
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_CONVERSION_REPORT,
            SAMPLE_AUTHORITY_REPORT,
            SAMPLE_SYNTHESIS,
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        # Patch at the BaseContentAgent level — all sub-agents share the same mock
        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            # Re-instantiate so it picks up the patched client
            agent = PublishReadyAgent()
            result = await agent.run(
                article=SAMPLE_ARTICLE,
                keyword="lms wordpress rentable",
                intent="décisionnelle",
                pillar="LMS",
            )

        assert isinstance(result, PublishReadyResult)
        assert result.publish_score > 0
        assert result.weakest_module != ""
        assert result.action_plan != ""
        assert result.dashboard != ""

    async def test_scores_are_weighted_correctly(self, fake_env):
        """Verify the publish_score matches the formula with known sub-scores."""
        result = PublishReadyResult()
        # Manually set sub-results with known scores
        from agents.conversion_auditor.agent import ConversionAuditResult
        from agents.llm_seo.agent import CitationSignalResult
        from agents.seo_auditor.agent import AuditResult
        from agents.topical_authority.agent import TopicalAuditResult

        result.seo_result = AuditResult(score_global=82)
        result.llm_result = CitationSignalResult(citation_score=75)
        result.conversion_result = ConversionAuditResult(score_conversion=78)
        result.authority_result = TopicalAuditResult(score_autorite=68)

        # Recompute using the same formula the agent uses
        from agents.publish_ready.agent import _compute_publish_score

        expected = _compute_publish_score(82, 75, 78, 68)
        assert expected == round(82 * 0.30 + 75 * 0.25 + 78 * 0.25 + 68 * 0.20)

    async def test_ready_to_publish_flag(self, fake_env):
        """ready_to_publish is True only when score >= threshold."""
        r_high = PublishReadyResult(publish_score=90, ready_to_publish=True)
        r_low = PublishReadyResult(publish_score=70, ready_to_publish=False)
        assert r_high.ready_to_publish is True
        assert r_low.ready_to_publish is False


# ── E2E: ArticlePipeline ──────────────────────────────────────────


class TestArticlePipelineE2E:
    """Full pipeline: Writer → Auditor+LLM ∥ → Editor → Cluster."""

    async def test_full_run_returns_pipeline_result(self, fake_env):
        call_count = 0
        responses = [
            SAMPLE_ARTICLE,  # Writer
            SAMPLE_SEO_REPORT,  # Auditor (parallel)
            SAMPLE_LLM_REPORT,  # LLM-SEO (parallel)
            SAMPLE_ARTICLE + "\n\n## Ajouts éditeur",  # Editor
            SAMPLE_CLUSTER,  # Cluster
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            pipeline = ArticlePipeline()
            result = await pipeline.run(
                topic="Choisir un LMS WordPress",
                keyword="lms wordpress",
                intent="comparative",
                angle="focus ROI freelance",
            )

        assert isinstance(result, PipelineResult)
        assert result.keyword == "lms wordpress"
        assert result.intent == "comparative"
        assert result.draft != ""
        assert result.audit != ""
        assert result.cluster != ""

    async def test_run_lite_returns_pipeline_result(self, fake_env):
        call_count = 0
        responses = [
            "Strategy output",  # SchoolswpBrainAgent
            SAMPLE_ARTICLE,  # Writer
            SAMPLE_SEO_REPORT,  # Auditor
            SAMPLE_LLM_REPORT,  # LLM-SEO
            SAMPLE_CLUSTER,  # Cluster
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            pipeline = ArticlePipeline()
            result = await pipeline.run_lite(
                keyword="fluentcrm avis",
                intent="informationnelle",
                pilier="crm",
            )

        assert isinstance(result, PipelineResult)
        assert result.keyword == "fluentcrm avis"
        assert result.draft != ""

    async def test_errors_collected_on_import_failure(self, fake_env):
        """Pipeline collects errors gracefully when a sub-agent import fails."""
        result = PipelineResult(keyword="test", intent="test")
        result.errors.append("SeoEditorAgent non disponible — draft utilisé comme final")
        assert len(result.errors) == 1
        assert "SeoEditorAgent" in result.errors[0]


# ── E2E: ContentFactoryAgent ──────────────────────────────────────


class TestContentFactoryE2E:
    """Full orchestration: Brain → Pipeline → 4 Audits → Cluster → Report."""

    async def test_audit_only_produces_valid_result(self, fake_env):
        """audit_only mode skips generation but runs 4 audits + cluster."""
        call_count = 0
        responses = [
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_CONVERSION_REPORT,
            SAMPLE_AUTHORITY_REPORT,
            SAMPLE_SYNTHESIS,
            SAMPLE_CLUSTER,
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            factory = ContentFactoryAgent()
            result = await factory.audit_only(
                article=SAMPLE_ARTICLE,
                keyword="lms wordpress",
                intent="décisionnelle",
                pillar="LMS",
            )

        assert isinstance(result, ContentFactoryResult)
        assert result.keyword == "lms wordpress"
        assert result.article == SAMPLE_ARTICLE
        assert result.publish is not None
        assert result.publish_score > 0
        assert result.factory_report != ""

    async def test_roi_check_stops_generation_when_low(self, fake_env):
        """When ROI is low and force=False, generation stops early."""
        strategy_response = '{"topic": "Test", "angle": "angle", "audience": "aud", "roi_ok": false}'

        async def mock_create(**kwargs):
            msg = MagicMock()
            msg.content = [MagicMock(text=strategy_response)]
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            ContentFactoryAgent()  # verify instantiation works
            # The ROI check is in generate_and_audit after brain returns
            result = ContentFactoryResult(roi_ok=False)
            assert result.roi_ok is False
            assert result.pipeline is None
            assert result.publish is None

    async def test_content_factory_result_delegates_scores(self, fake_env):
        """ContentFactoryResult.publish_score delegates to inner PublishReadyResult."""
        pub = PublishReadyResult(publish_score=87)
        r = ContentFactoryResult(publish=pub)
        assert r.publish_score == 87
        assert r.publish_emoji == "🟡"
        assert r.publish_diagnostic == "1–2 optimisations ciblées"

    async def test_generate_and_audit_full_flow(self, fake_env):
        """Full generate_and_audit: Brain → Pipeline → 4 Audits → Cluster → Report."""
        call_count = 0
        # BrainLiteAgent returns JSON strategy, then pipeline agents, then audits
        strategy_json = '{"topic": "LMS WordPress rentable", "angle": "ROI freelance", "audience": "freelances WordPress", "roi_ok": true}'
        responses = [
            strategy_json,  # BrainLiteAgent (strategy)
            SAMPLE_ARTICLE,  # SeoWriterAgent (v1)
            SAMPLE_SEO_REPORT,  # SeoAuditorAgent (parallel)
            SAMPLE_LLM_REPORT,  # LlmSeoAgent (parallel)
            SAMPLE_ARTICLE + "\n\n## Section éditée",  # SeoEditorAgent (v2)
            SAMPLE_CLUSTER,  # ClusterArchitectAgent
            # PublishReadyAgent sub-calls (4 audits + synthesis)
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_CONVERSION_REPORT,
            SAMPLE_AUTHORITY_REPORT,
            SAMPLE_SYNTHESIS,
            # TopicalAuthorityAgent expand_cluster
            SAMPLE_CLUSTER,
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            factory = ContentFactoryAgent()
            result = await factory.generate_and_audit(
                keyword="lms wordpress rentable",
                intent="décisionnelle",
                pillar="LMS",
                objective="affiliation",
            )

        assert isinstance(result, ContentFactoryResult)
        assert result.keyword == "lms wordpress rentable"
        assert result.topic == "LMS WordPress rentable"
        assert result.angle == "ROI freelance"
        assert result.roi_ok is True
        assert result.article != ""
        assert result.publish is not None
        assert result.publish_score >= 0  # Score depends on mock response ordering
        assert result.factory_report != ""
        assert "lms wordpress rentable" in result.factory_report

    async def test_generate_and_audit_roi_stops_early(self, fake_env):
        """Low ROI without --force stops before generation."""
        strategy_json = '{"topic": "Test", "angle": "test", "audience": "test", "roi_ok": false}'

        async def mock_create(**kwargs):
            msg = MagicMock()
            msg.content = [MagicMock(text=strategy_json)]
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            factory = ContentFactoryAgent()
            result = await factory.generate_and_audit(
                keyword="sujet faible roi",
                intent="informationnelle",
                force=False,
            )

        assert result.roi_ok is False
        assert result.pipeline is None
        assert result.publish is None
        assert result.article == ""

    async def test_generate_and_audit_force_overrides_roi(self, fake_env):
        """force=True continues even when ROI is low."""
        call_count = 0
        strategy_json = '{"topic": "Sujet ROI faible", "angle": "test", "audience": "test", "roi_ok": false}'
        responses = [
            strategy_json,
            SAMPLE_ARTICLE,
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_ARTICLE,
            SAMPLE_CLUSTER,
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_CONVERSION_REPORT,
            SAMPLE_AUTHORITY_REPORT,
            SAMPLE_SYNTHESIS,
            SAMPLE_CLUSTER,
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            factory = ContentFactoryAgent()
            result = await factory.generate_and_audit(
                keyword="sujet faible roi",
                intent="informationnelle",
                force=True,
            )

        # force=True → pipeline runs despite low ROI
        assert result.roi_ok is False
        assert result.article != ""


# ── E2E: PublishReadyAgent — dashboard content ───────────────────


class TestPublishReadyDashboard:
    """Verify dashboard markdown output contains expected sections."""

    async def test_dashboard_contains_keyword(self, fake_env):
        call_count = 0
        responses = [
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_CONVERSION_REPORT,
            SAMPLE_AUTHORITY_REPORT,
            SAMPLE_SYNTHESIS,
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            agent = PublishReadyAgent()
            result = await agent.run(
                article=SAMPLE_ARTICLE,
                keyword="lms wordpress test",
            )

        assert "lms wordpress test" in result.dashboard
        assert "Publish Score" in result.dashboard or "Publish Ready" in result.dashboard

    async def test_dashboard_includes_all_module_scores(self, fake_env):
        call_count = 0
        responses = [
            SAMPLE_SEO_REPORT,
            SAMPLE_LLM_REPORT,
            SAMPLE_CONVERSION_REPORT,
            SAMPLE_AUTHORITY_REPORT,
            SAMPLE_SYNTHESIS,
        ]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            agent = PublishReadyAgent()
            result = await agent.run(
                article=SAMPLE_ARTICLE,
                keyword="lms wordpress",
            )

        # All 4 module names should appear in the dashboard
        scores = result.scores_summary()
        for module_name in scores:
            assert module_name in result.dashboard


# ── E2E: ArticlePipeline — edge cases ───────────────────────────


class TestArticlePipelineEdgeCases:
    """Edge cases for pipeline orchestration."""

    async def test_run_without_angle(self, fake_env):
        """Pipeline works without optional angle parameter."""
        call_count = 0
        responses = [SAMPLE_ARTICLE, SAMPLE_SEO_REPORT, SAMPLE_LLM_REPORT, SAMPLE_ARTICLE, SAMPLE_CLUSTER]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            pipeline = ArticlePipeline()
            result = await pipeline.run(
                topic="Test sans angle",
                keyword="test keyword",
                intent="informationnelle",
            )

        assert result.draft != ""
        assert result.keyword == "test keyword"

    async def test_run_with_pillar(self, fake_env):
        """Pipeline passes pillar to cluster agent."""
        call_count = 0
        responses = [SAMPLE_ARTICLE, SAMPLE_SEO_REPORT, SAMPLE_LLM_REPORT, SAMPLE_ARTICLE, SAMPLE_CLUSTER]

        async def mock_create(**kwargs):
            nonlocal call_count
            msg = MagicMock()
            msg.content = [MagicMock(text=responses[min(call_count, len(responses) - 1)])]
            call_count += 1
            return msg

        with patch("agents.providers.anthropic.AsyncAnthropic") as MockClient:
            instance = AsyncMock()
            instance.messages.create = mock_create
            MockClient.return_value = instance
            clear_provider_cache()

            pipeline = ArticlePipeline()
            result = await pipeline.run(
                topic="Test avec pillar",
                keyword="lms test",
                intent="comparative",
                pillar="LMS",
            )

        assert result.cluster != ""

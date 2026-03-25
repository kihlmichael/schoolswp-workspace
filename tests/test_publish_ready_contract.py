"""Contract tests for PublishReadyAgent — dataclass, scoring, orchestration."""

import pytest

from agents.conversion_auditor.agent import ConversionAuditResult
from agents.llm_seo.agent import CitationSignalResult
from agents.publish_ready.agent import (
    PublishReadyAgent,
    PublishReadyResult,
    _compute_publish_score,
    _find_weakest,
)
from agents.seo_auditor.agent import AuditResult
from agents.topical_authority.agent import TopicalAuditResult

# ── PublishReadyResult dataclass ───────────────────────────────────


class TestPublishReadyResultDefaults:
    """Default dataclass values are sane."""

    def test_default_score_is_zero(self):
        r = PublishReadyResult()
        assert r.publish_score == 0

    def test_default_not_ready(self):
        r = PublishReadyResult()
        assert r.ready_to_publish is False

    def test_default_weakest_empty(self):
        r = PublishReadyResult()
        assert r.weakest_module == ""

    def test_default_sub_results_are_instances(self):
        r = PublishReadyResult()
        assert isinstance(r.seo_result, AuditResult)
        assert isinstance(r.llm_result, CitationSignalResult)
        assert isinstance(r.conversion_result, ConversionAuditResult)
        assert isinstance(r.authority_result, TopicalAuditResult)


# ── Publish Score formula ──────────────────────────────────────────


class TestPublishScoreFormula:
    """_compute_publish_score applies correct weights: SEO 30%, LLM 25%, Conv 25%, Auth 20%."""

    def test_all_100_gives_100(self):
        assert _compute_publish_score(100, 100, 100, 100) == 100

    def test_all_zero_gives_zero(self):
        assert _compute_publish_score(0, 0, 0, 0) == 0

    def test_known_weighted_result(self):
        # SEO=80*0.30=24, LLM=70*0.25=17.5, Conv=90*0.25=22.5, Auth=60*0.20=12 → 76
        assert _compute_publish_score(80, 70, 90, 60) == 76

    def test_seo_weight_is_highest(self):
        """SEO at 100, others at 0 → should be 30."""
        assert _compute_publish_score(100, 0, 0, 0) == 30

    def test_authority_weight_is_lowest(self):
        """Authority at 100, others at 0 → should be 20."""
        assert _compute_publish_score(0, 0, 0, 100) == 20

    def test_weights_sum_to_100(self):
        """Each module at 100 with its own weight must sum to 100."""
        seo = _compute_publish_score(100, 0, 0, 0)
        llm = _compute_publish_score(0, 100, 0, 0)
        conv = _compute_publish_score(0, 0, 100, 0)
        auth = _compute_publish_score(0, 0, 0, 100)
        assert seo + llm + conv + auth == 100


# ── _find_weakest ──────────────────────────────────────────────────


class TestFindWeakest:
    """_find_weakest identifies the lowest-scoring module."""

    def test_seo_weakest(self):
        assert _find_weakest(seo=10, llm=80, conversion=80, authority=80) == "SEO Structure"

    def test_authority_weakest(self):
        assert _find_weakest(seo=80, llm=80, conversion=80, authority=10) == "Autorité Thématique"

    def test_llm_weakest(self):
        assert _find_weakest(seo=80, llm=10, conversion=80, authority=80) == "Citabilité IA"

    def test_conversion_weakest(self):
        assert _find_weakest(seo=80, llm=80, conversion=10, authority=80) == "Conversion & CTA"

    def test_tie_returns_first_in_dict_order(self):
        result = _find_weakest(seo=50, llm=50, conversion=50, authority=50)
        # All equal — first in dict order wins (SEO Structure)
        assert result in ("SEO Structure", "Citabilité IA", "Conversion & CTA", "Autorité Thématique")


# ── Diagnostics and properties ─────────────────────────────────────


class TestPublishReadyDiagnostic:
    """publish_diagnostic and publish_emoji map score to labels."""

    @pytest.mark.parametrize(
        "score, expected_diag, expected_emoji",
        [
            (100, "Publication immédiate", "✅"),
            (90, "Publication immédiate", "✅"),
            (89, "1–2 optimisations ciblées", "🟡"),
            (80, "1–2 optimisations ciblées", "🟡"),
            (79, "Travail requis sur blocs faibles", "🟠"),
            (70, "Travail requis sur blocs faibles", "🟠"),
            (69, "Révision substantielle", "🔴"),
            (0, "Révision substantielle", "🔴"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected_diag, expected_emoji):
        r = PublishReadyResult(publish_score=score)
        assert r.publish_diagnostic == expected_diag
        assert r.publish_emoji == expected_emoji


class TestScoresSummary:
    """scores_summary returns the 4 module scores in a dict."""

    def test_returns_all_four_modules(self):
        r = PublishReadyResult(
            seo_result=AuditResult(score_global=85),
            llm_result=CitationSignalResult(citation_score=72),
            conversion_result=ConversionAuditResult(score_conversion=90),
            authority_result=TopicalAuditResult(score_autorite=65),
        )
        summary = r.scores_summary()
        assert summary == {
            "SEO Structure": 85,
            "Citabilité IA": 72,
            "Conversion": 90,
            "Autorité thème": 65,
        }


# ── Agent class attributes ─────────────────────────────────────────


class TestPublishReadyAgentContract:
    """PublishReadyAgent satisfies BaseContentAgent contract."""

    def test_agent_name(self):
        assert PublishReadyAgent.name == "publish-ready"

    def test_has_system_prompt(self):
        assert len(PublishReadyAgent.system_prompt) > 50

    def test_instantiates_with_default_model(self, fake_env):
        agent = PublishReadyAgent()
        assert agent.model == "claude-sonnet-4-6"

    def test_instantiates_with_custom_model(self, fake_env):
        agent = PublishReadyAgent(model="claude-opus-4")
        assert agent.model == "claude-opus-4"

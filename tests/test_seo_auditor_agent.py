"""Tests for SeoAuditorAgent — AuditResult parsing and smoke test."""

import pytest

from agents.seo_auditor.agent import AuditResult, SeoAuditorAgent

# ── Sample LLM output for parse testing ──────────────────────────

SAMPLE_AUDIT_REPORT = """\
Score global : 82/100

Détail par bloc :
SEO STRUCTURE : 17/20
INTENTION : 16/20
PÉDAGOGIE : 18/20
BUSINESS : 15/20
BRANDING : 16/20

Points forts :
– Structure Hn bien hiérarchisée
– Tutoiement systématique

Points faibles :
– Pas de cas d'usage chiffré
– Maillage interne insuffisant

Axes d'amélioration prioritaires :
1. Ajouter un cas d'usage concret avec données
2. Insérer 2-3 liens internes vers les piliers existants
3. Renforcer la section recommandation avec profils cibles
"""


class TestAuditResultParse:
    """AuditResult.parse() extracts structured data from LLM output."""

    def test_parses_global_score(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        assert result.score_global == 82

    def test_parses_all_bloc_scores(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        assert result.seo_structure == 17
        assert result.intention == 16
        assert result.pedagogie == 18
        assert result.business == 15
        assert result.branding == 16

    def test_bloc_scores_sum_to_global(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        total = result.seo_structure + result.intention + result.pedagogie + result.business + result.branding
        assert total == result.score_global

    def test_parses_points_forts(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        assert len(result.points_forts) == 2
        assert "Structure Hn" in result.points_forts[0]

    def test_parses_points_faibles(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        assert len(result.points_faibles) == 2
        assert "Maillage" in result.points_faibles[1]

    def test_parses_axes_amelioration(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        assert len(result.axes_amelioration) == 3
        assert "cas d'usage" in result.axes_amelioration[0].lower()

    def test_stores_raw_report(self):
        result = AuditResult.parse(SAMPLE_AUDIT_REPORT)
        assert result.report == SAMPLE_AUDIT_REPORT

    def test_empty_report_returns_zeros(self):
        result = AuditResult.parse("")
        assert result.score_global == 0
        assert result.seo_structure == 0
        assert result.points_forts == []

    def test_partial_report_parses_what_it_can(self):
        partial = "Score global : 65/100\n\nSEO STRUCTURE : 12/20\n"
        result = AuditResult.parse(partial)
        assert result.score_global == 65
        assert result.seo_structure == 12
        assert result.intention == 0  # missing → 0


class TestAuditResultDiagnostic:
    """diagnostic property maps score to French label."""

    @pytest.mark.parametrize(
        "score, expected",
        [
            (100, "Publication immédiate"),
            (95, "Publication immédiate"),
            (90, "Ajustements mineurs"),
            (85, "Ajustements mineurs"),
            (82, "Optimisation nécessaire"),
            (70, "Optimisation nécessaire"),
            (69, "Réécriture stratégique"),
            (0, "Réécriture stratégique"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected):
        result = AuditResult(score_global=score)
        assert result.diagnostic == expected


class TestSeoAuditorSmoke:
    """Smoke test: agent runs with mocked API."""

    async def test_run_returns_audit_result(self, fake_env, mock_provider):
        agent = SeoAuditorAgent()
        agent._provider = mock_provider(SAMPLE_AUDIT_REPORT)

        result = await agent.run(article="# Test\n\nContent.", keyword="lms wordpress")

        assert isinstance(result, AuditResult)
        assert result.score_global == 82
        agent._provider.complete.assert_called_once()

    async def test_run_with_intent(self, fake_env, mock_provider):
        agent = SeoAuditorAgent()
        agent._provider = mock_provider(SAMPLE_AUDIT_REPORT)

        result = await agent.run(
            article="# Test\n\nContent.",
            keyword="lms wordpress",
            intent="comparative",
        )

        assert result.score_global == 82
        # Verify intent was passed in the user message via LLMRequest
        call_args = agent._provider.complete.call_args[0][0]
        assert "comparative" in call_args.user_message

    async def test_audit_and_fix_above_threshold_no_fix(self, fake_env, mock_provider):
        """When score >= threshold, no fix is triggered."""
        high_report = SAMPLE_AUDIT_REPORT.replace("82/100", "95/100")
        agent = SeoAuditorAgent()
        agent._provider = mock_provider(high_report)

        result = await agent.audit_and_fix(
            article="# Test\n\nContent.",
            keyword="lms wordpress",
            threshold=90,
        )

        assert result.fixed is False
        assert result.v2 == ""

    def test_agent_class_attrs(self):
        assert SeoAuditorAgent.name == "seo-auditor"
        assert len(SeoAuditorAgent.system_prompt) > 100

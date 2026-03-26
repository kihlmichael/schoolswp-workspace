"""Contract tests for the 4 audit result dataclasses + PipelineResult + PublishReadyResult.

Each dataclass must:
- Have sane defaults (zero scores, empty lists, empty strings)
- Parse realistic LLM output correctly via .parse()
- Return correct diagnostic/emoji for each score threshold
- Handle malformed/empty input without crashing
"""

import pytest

from agents.seo_auditor.agent import AuditResult
from agents.llm_seo.agent import CitationSignalResult
from agents.conversion_auditor.agent import ConversionAuditResult
from agents.topical_authority.agent import TopicalAuditResult
from agents.article_pipeline.pipeline import PipelineResult
from agents.publish_ready.agent import (
    PublishReadyResult,
    _compute_publish_score,
    _find_weakest,
)


# ── AuditResult ──────────────────────────────────────────────────


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
– Pas de FAQ optimisée

Axes d'amélioration prioritaires :
1. Ajouter 3 liens internes
2. Créer une FAQ de 5 questions
3. Renforcer le CTA principal
"""


class TestAuditResultDefaults:
    def test_zero_defaults(self):
        r = AuditResult()
        assert r.score_global == 0
        assert r.seo_structure == 0
        assert r.intention == 0
        assert r.pedagogie == 0
        assert r.business == 0
        assert r.branding == 0
        assert r.points_forts == []
        assert r.points_faibles == []
        assert r.axes_amelioration == []
        assert r.report == ""
        assert r.v2 == ""
        assert r.fixed is False


class TestAuditResultParse:
    def test_parses_score_global(self):
        r = AuditResult.parse(SAMPLE_SEO_REPORT)
        assert r.score_global == 82

    def test_parses_blocs(self):
        r = AuditResult.parse(SAMPLE_SEO_REPORT)
        assert r.seo_structure == 17
        assert r.intention == 16
        assert r.pedagogie == 18
        assert r.business == 15
        assert r.branding == 16

    def test_parses_points_forts(self):
        r = AuditResult.parse(SAMPLE_SEO_REPORT)
        assert len(r.points_forts) == 2
        assert "Structure Hn hiérarchisée" in r.points_forts[0]

    def test_parses_points_faibles(self):
        r = AuditResult.parse(SAMPLE_SEO_REPORT)
        assert len(r.points_faibles) == 2

    def test_parses_axes_amelioration(self):
        r = AuditResult.parse(SAMPLE_SEO_REPORT)
        assert len(r.axes_amelioration) == 3
        assert "liens internes" in r.axes_amelioration[0]

    def test_stores_raw_report(self):
        r = AuditResult.parse(SAMPLE_SEO_REPORT)
        assert r.report == SAMPLE_SEO_REPORT

    def test_empty_input(self):
        r = AuditResult.parse("")
        assert r.score_global == 0
        assert r.points_forts == []

    def test_malformed_input(self):
        r = AuditResult.parse("No structured data here, just text.")
        assert r.score_global == 0


class TestAuditResultDiagnostic:
    @pytest.mark.parametrize(
        "score, expected_diag, expected_emoji",
        [
            (95, "Publication immédiate", "✅"),
            (96, "Publication immédiate", "✅"),
            (85, "Ajustements mineurs", "🟡"),
            (90, "Ajustements mineurs", "🟡"),
            (70, "Optimisation nécessaire", "🟠"),
            (82, "Optimisation nécessaire", "🟠"),
            (50, "Réécriture stratégique", "🔴"),
            (0, "Réécriture stratégique", "🔴"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected_diag, expected_emoji):
        r = AuditResult(score_global=score)
        assert r.diagnostic == expected_diag
        assert r.diagnostic_emoji == expected_emoji


# ── CitationSignalResult ─────────────────────────────────────────


SAMPLE_LLM_REPORT = """\
Score citation global : 75/100

Signaux détectés :
RÉPONSE RAPIDE : 20/25 | Présent et clair
BLOCS EXTRACTIBLES : 18/25 | Bon
DÉFINITIONS : 15/20 | Suffisant
STRUCTURE SNIPPET : 12/15 | À améliorer
COHÉRENCE THÉMATIQUE : 10/15 | Correct

Probabilités de citation :
Google AI Overview : 65 %
Perplexity : 70 %
ChatGPT Browse : 55 %
Bing Copilot : 50 %

Points forts citation :
– Réponse rapide bien structurée
– Données chiffrées présentes

Signaux manquants :
– FAQ schema markup absent
– Pas de bloc définition formel

Recommandations d'optimisation :
1. Ajouter un bloc FAQ avec balisage
2. Créer des blocs définition encadrés
3. Renforcer les données chiffrées
"""


class TestCitationSignalResultDefaults:
    def test_zero_defaults(self):
        r = CitationSignalResult()
        assert r.citation_score == 0
        assert r.signal_reponse_rapide == 0
        assert r.google_ai_overview_pct == 0
        assert r.points_forts == []
        assert r.signaux_manquants == []
        assert r.recommandations == []
        assert r.report == ""
        assert r.optimized is False


class TestCitationSignalResultParse:
    def test_parses_citation_score(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert r.citation_score == 75

    def test_parses_signals(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert r.signal_reponse_rapide == 20
        assert r.signal_blocs_extractibles == 18
        assert r.signal_definitions == 15
        assert r.signal_structure_snippet == 12
        assert r.signal_coherence == 10

    def test_parses_statuses(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert "Présent" in r.status_reponse_rapide

    def test_parses_platform_probabilities(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert r.google_ai_overview_pct == 65
        assert r.perplexity_pct == 70
        assert r.chatgpt_pct == 55
        assert r.bing_pct == 50

    def test_parses_points_forts(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert len(r.points_forts) == 2

    def test_parses_signaux_manquants(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert len(r.signaux_manquants) == 2

    def test_parses_recommandations(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert len(r.recommandations) == 3

    def test_empty_input(self):
        r = CitationSignalResult.parse("")
        assert r.citation_score == 0

    def test_best_platform(self):
        r = CitationSignalResult.parse(SAMPLE_LLM_REPORT)
        assert r.best_platform != ""


class TestCitationSignalResultDiagnostic:
    @pytest.mark.parametrize(
        "score, expected_diag, expected_emoji",
        [
            (85, "Hautement citable", "✅"),
            (90, "Hautement citable", "✅"),
            (70, "Citable — optimisations mineures", "🟡"),
            (80, "Citable — optimisations mineures", "🟡"),
            (50, "Partiellement citable", "🟠"),
            (60, "Partiellement citable", "🟠"),
            (30, "Non optimisé pour les IA", "🔴"),
            (0, "Non optimisé pour les IA", "🔴"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected_diag, expected_emoji):
        r = CitationSignalResult(citation_score=score)
        assert r.diagnostic == expected_diag
        assert r.diagnostic_emoji == expected_emoji


# ── ConversionAuditResult ────────────────────────────────────────


SAMPLE_CONVERSION_REPORT = """\
Score Conversion : 78/100

Détail :
Clarté problème : 16/20
Décision : 15/20
Orientation action : 16/20
CTA : 14/20
Business alignment : 17/20

Points forts :
– Problème bien posé en introduction
– Recommandation contextualisée

Faiblesses :
– CTA principal trop générique
– Pas de lead magnet

Recommandations concrètes :
1. Ajouter un CTA soft après la section principale
2. Intégrer un lead magnet
3. Renforcer l'argument chiffré du CTA
"""


class TestConversionAuditResultDefaults:
    def test_zero_defaults(self):
        r = ConversionAuditResult()
        assert r.score_conversion == 0
        assert r.clarte_probleme == 0
        assert r.decision == 0
        assert r.orientation_action == 0
        assert r.cta == 0
        assert r.business_alignment == 0
        assert r.points_forts == []
        assert r.faiblesses == []
        assert r.recommandations == []
        assert r.report == ""
        assert r.injected is False


class TestConversionAuditResultParse:
    def test_parses_score(self):
        r = ConversionAuditResult.parse(SAMPLE_CONVERSION_REPORT)
        assert r.score_conversion == 78

    def test_parses_blocs(self):
        r = ConversionAuditResult.parse(SAMPLE_CONVERSION_REPORT)
        assert r.clarte_probleme == 16
        assert r.decision == 15
        assert r.orientation_action == 16
        assert r.cta == 14
        assert r.business_alignment == 17

    def test_parses_points_forts(self):
        r = ConversionAuditResult.parse(SAMPLE_CONVERSION_REPORT)
        assert len(r.points_forts) == 2

    def test_parses_faiblesses(self):
        r = ConversionAuditResult.parse(SAMPLE_CONVERSION_REPORT)
        assert len(r.faiblesses) == 2

    def test_parses_recommandations(self):
        r = ConversionAuditResult.parse(SAMPLE_CONVERSION_REPORT)
        assert len(r.recommandations) == 3

    def test_empty_input(self):
        r = ConversionAuditResult.parse("")
        assert r.score_conversion == 0


class TestConversionAuditResultDiagnostic:
    @pytest.mark.parametrize(
        "score, expected_diag",
        [
            (95, "Article business-ready"),
            (85, "Optimisations mineures"),
            (70, "Manque d'orientation action"),
            (50, "SEO sans levier business"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected_diag):
        r = ConversionAuditResult(score_conversion=score)
        assert r.diagnostic == expected_diag


class TestConversionAuditResultWeakestBloc:
    def test_identifies_weakest(self):
        r = ConversionAuditResult(
            clarte_probleme=16,
            decision=15,
            orientation_action=16,
            cta=10,
            business_alignment=17,
        )
        assert "CTA" in r.weakest_bloc

    def test_all_equal(self):
        r = ConversionAuditResult(
            clarte_probleme=15,
            decision=15,
            orientation_action=15,
            cta=15,
            business_alignment=15,
        )
        # Should not crash — any bloc is valid
        assert r.weakest_bloc != ""


# ── TopicalAuditResult ───────────────────────────────────────────


SAMPLE_AUTHORITY_REPORT = """\
Score Autorité : 68/100

Détail :
Couverture : 14/20
Connexions : 12/20
Cohérence : 15/20
Positionnement : 14/20
Potentiel cluster : 13/20

Manques identifiés :
– Comparaison approfondie des alternatives LMS
– Guide de migration entre LMS
– Retours terrain avec chiffres de CA

Opportunités de cluster :
– Article satellite 1 : TutorLMS avis complet 2026 | informationnelle | renforce le pilier LMS
– Article satellite 2 : LearnDash vs LifterLMS | comparative | compare les alternatives
– Article satellite 3 : Première formation WordPress | guide pratique | entrée cluster

Recommandation stratégique : Pilier
Justification : Couvre un sujet central LMS avec potentiel de cluster élevé.
"""


class TestTopicalAuditResultDefaults:
    def test_zero_defaults(self):
        r = TopicalAuditResult()
        assert r.score_autorite == 0
        assert r.couverture == 0
        assert r.connexions == 0
        assert r.coherence == 0
        assert r.positionnement == 0
        assert r.potentiel_cluster == 0
        assert r.manques == []
        assert r.satellites == []
        assert r.recommandation == ""
        assert r.justification == ""
        assert r.report == ""
        assert r.expanded is False


class TestTopicalAuditResultParse:
    def test_parses_score(self):
        r = TopicalAuditResult.parse(SAMPLE_AUTHORITY_REPORT)
        assert r.score_autorite == 68

    def test_parses_blocs(self):
        r = TopicalAuditResult.parse(SAMPLE_AUTHORITY_REPORT)
        assert r.couverture == 14
        assert r.connexions == 12
        assert r.coherence == 15
        assert r.positionnement == 14
        assert r.potentiel_cluster == 13

    def test_parses_manques(self):
        r = TopicalAuditResult.parse(SAMPLE_AUTHORITY_REPORT)
        assert len(r.manques) == 3
        assert "migration" in r.manques[1].lower()

    def test_parses_satellites(self):
        r = TopicalAuditResult.parse(SAMPLE_AUTHORITY_REPORT)
        assert len(r.satellites) == 3
        assert "TutorLMS" in r.satellites[0]

    def test_parses_recommandation(self):
        r = TopicalAuditResult.parse(SAMPLE_AUTHORITY_REPORT)
        assert "Pilier" in r.recommandation

    def test_parses_justification(self):
        r = TopicalAuditResult.parse(SAMPLE_AUTHORITY_REPORT)
        assert "cluster" in r.justification.lower()

    def test_empty_input(self):
        r = TopicalAuditResult.parse("")
        assert r.score_autorite == 0
        assert r.manques == []


class TestTopicalAuditResultDiagnostic:
    @pytest.mark.parametrize(
        "score, expected_diag, expected_emoji",
        [
            (95, "Article pilier", "✅"),
            (85, "Satellite fort", "🟢"),
            (70, "Renforcement cluster nécessaire", "🟡"),
            (50, "Contenu isolé", "🔴"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected_diag, expected_emoji):
        r = TopicalAuditResult(score_autorite=score)
        assert r.diagnostic == expected_diag
        assert r.diagnostic_emoji == expected_emoji


class TestTopicalAuditResultRole:
    @pytest.mark.parametrize(
        "recommandation, expected_role",
        [
            ("Pilier", "Pilier"),
            ("Satellite fort", "Satellite"),
            ("À renforcer", "À renforcer"),
            ("Contenu isolé", "Contenu isolé"),
            ("", "Contenu isolé"),
        ],
    )
    def test_role_mapping(self, recommandation, expected_role):
        r = TopicalAuditResult(recommandation=recommandation)
        assert r.role == expected_role


# ── PipelineResult ───────────────────────────────────────────────


class TestPipelineResultDefaults:
    def test_required_fields(self):
        r = PipelineResult(keyword="test", intent="info")
        assert r.keyword == "test"
        assert r.intent == "info"
        assert r.draft == ""
        assert r.final == ""
        assert r.errors == []
        assert r.v1 == ""
        assert r.v2 == ""
        assert r.v3 == ""
        assert r.v4 == ""

    def test_compute_publish_score_all_present(self):
        r = PipelineResult(
            keyword="k",
            intent="i",
            seo_score=80,
            llm_score=75,
            conversion_score=70,
            authority_score=65,
        )
        expected = 80 * 0.30 + 75 * 0.25 + 70 * 0.25 + 65 * 0.20
        assert r.compute_publish_score() == expected

    def test_compute_publish_score_missing(self):
        r = PipelineResult(keyword="k", intent="i", seo_score=80)
        assert r.compute_publish_score() is None

    def test_errors_accumulate(self):
        r = PipelineResult(keyword="k", intent="i")
        r.errors.append("Error 1")
        r.errors.append("Error 2")
        assert len(r.errors) == 2


# ── PublishReadyResult ───────────────────────────────────────────


class TestPublishReadyResultDefaults:
    def test_defaults(self):
        r = PublishReadyResult()
        assert r.publish_score == 0
        assert r.action_plan == ""
        assert r.ready_to_publish is False
        assert r.fixed_article == ""
        assert r.weakest_module == ""
        assert r.dashboard == ""

    def test_sub_results_are_default_instances(self):
        r = PublishReadyResult()
        assert isinstance(r.seo_result, AuditResult)
        assert isinstance(r.llm_result, CitationSignalResult)
        assert isinstance(r.conversion_result, ConversionAuditResult)
        assert isinstance(r.authority_result, TopicalAuditResult)


class TestPublishReadyResultDiagnostic:
    @pytest.mark.parametrize(
        "score, expected_diag, expected_emoji",
        [
            (90, "Publication immédiate", "✅"),
            (95, "Publication immédiate", "✅"),
            (80, "1–2 optimisations ciblées", "🟡"),
            (85, "1–2 optimisations ciblées", "🟡"),
            (70, "Travail requis sur blocs faibles", "🟠"),
            (75, "Travail requis sur blocs faibles", "🟠"),
            (50, "Révision substantielle", "🔴"),
            (0, "Révision substantielle", "🔴"),
        ],
    )
    def test_diagnostic_thresholds(self, score, expected_diag, expected_emoji):
        r = PublishReadyResult(publish_score=score)
        assert r.publish_diagnostic == expected_diag
        assert r.publish_emoji == expected_emoji


class TestPublishReadyResultScoresSummary:
    def test_aggregates_sub_scores(self):
        r = PublishReadyResult(
            seo_result=AuditResult(score_global=82),
            llm_result=CitationSignalResult(citation_score=75),
            conversion_result=ConversionAuditResult(score_conversion=78),
            authority_result=TopicalAuditResult(score_autorite=68),
        )
        summary = r.scores_summary()
        assert summary["SEO Structure"] == 82
        assert summary["Citabilité IA"] == 75
        assert summary["Conversion"] == 78
        assert summary["Autorité thème"] == 68

    def test_default_scores_are_zero(self):
        r = PublishReadyResult()
        summary = r.scores_summary()
        assert all(v == 0 for v in summary.values())


# ── _compute_publish_score ───────────────────────────────────────


class TestComputePublishScore:
    def test_formula(self):
        result = _compute_publish_score(82, 75, 78, 68)
        expected = round(82 * 0.30 + 75 * 0.25 + 78 * 0.25 + 68 * 0.20)
        assert result == expected

    def test_all_100(self):
        assert _compute_publish_score(100, 100, 100, 100) == 100

    def test_all_zero(self):
        assert _compute_publish_score(0, 0, 0, 0) == 0

    def test_weights_sum_to_100(self):
        # Equal scores should give the same score
        assert _compute_publish_score(80, 80, 80, 80) == 80


# ── _find_weakest ────────────────────────────────────────────────


class TestFindWeakest:
    def test_finds_lowest(self):
        assert _find_weakest(82, 75, 78, 60) == "Autorité Thématique"

    def test_seo_weakest(self):
        assert _find_weakest(50, 75, 78, 68) == "SEO Structure"

    def test_llm_weakest(self):
        assert _find_weakest(82, 40, 78, 68) == "Citabilité IA"

    def test_conversion_weakest(self):
        assert _find_weakest(82, 75, 30, 68) == "Conversion & CTA"

    def test_all_equal(self):
        # Should not crash — any is valid
        result = _find_weakest(80, 80, 80, 80)
        assert result != ""

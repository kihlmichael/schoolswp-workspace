"""
KPI Dashboard Éditorial — Tableau de pilotage stratégique schoolsWP.

Agrège les données de tous les agents (pillar_authority, roi_editorial_plan,
article_pipeline, cocon_builder) en un dashboard unifié sur 5 dimensions :

1. Vue Macro (Vision 360°)
2. Index Autorité par Pilier (/100)
3. KPI ROI Contenu (Score ROI par article)
4. KPI LLM / Citations IA (scores LLM-SEO)
5. KPI Cocon & Maillage (densité cluster)

Score Écosystème schoolsWP =
  (Autorité × 0.3) + (ROI contenu × 0.3) + (SEO croissance × 0.2) + (LLM score × 0.2)
→ Baromètre mensuel /100
"""

from agents.kpi_dashboard.agent import KpiDashboardAgent

__all__ = ["KpiDashboardAgent"]

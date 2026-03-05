"""
ROI Editorial Plan — Plan éditorial auto-priorisé par ROI schoolsWP.

Relie Knowledge Graph + Index d'autorité + Cocon sémantique + Intent SEO + Impact business
pour produire un plan éditorial priorisé par Score ROI réel.

Scoring :
  Score ROI = (SEO × 0.35) + (Business × 0.35) + (Autorité × 0.2) - (Effort × 0.1)
  → Priorité 🔥 A (≥ 7.0) | 🟡 B (5.0–6.9) | 🔵 C (< 5.0)

Output :
  - 15 idées d'articles scorées et classées
  - 3 quick wins
  - 2 piliers à consolider
  - 1 article signature long format
  - Calendrier 3-6 mois
"""
from agents.roi_editorial_plan.agent import RoiEditorialPlanAgent

__all__ = ["RoiEditorialPlanAgent"]

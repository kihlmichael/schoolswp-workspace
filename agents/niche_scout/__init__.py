"""
Niche Scout — Détection & Scoring de niches atteignables vs WPMarmite — schoolsWP.

4 agents complémentaires :

- NicheScoutAgent       : découverte qualitative (Top 5 niches, cartographie WPMarmite)
- NicheScorerAgent      : scoring unitaire /10 (5 variables, calcul explicite)
- BatchNicheScorerAgent : scoring industriel /10 (10-50 niches, 6 variables, 1 passe)
- DataScorerAgent       : scoring basé sur métriques réelles (Ahrefs/DataForSEO/Semrush)
                          3 scores : SEO/10 + Business/10 → Combiné/10

Formule unitaire  : (Volume_norm + Low_Competition + Overlap + Authority + Longtail) / 5 x 10
Formule batch     : (V1 + V2 + V3 + V4 + V5 + V6) / 3   [variables 1-5]
Formule data      : Score_SEO=(Vol*3 + KD_ease*3 + SERP_inv*2 + Overlap*2 + Auth*1)/11*10
                    Score_Biz=(CPC*4 + Intent*4 + ConvVol*2)/10*10
                    Score_Comb=SEO*0.6 + Biz*0.4

Input data scorer : CSV (niche,volume,kd,serp_results,dr_avg_top10,overlap_pct,cpc,intent,notes)
                    ou JSON [{niche, volume, kd, ...}]
                    Générer template : python -m agents.niche_scout.data_scorer_cli --template

Workflow recommandé :
  NicheScoutAgent -> liste de niches candidates
  BatchNicheScorerAgent -> tri rapide
  DataScorerAgent (avec métriques réelles) -> scoring final précis
  ClusterArchitectAgent -> architecture cluster sur la niche n°1
"""
from agents.niche_scout.agent import NicheScoutAgent
from agents.niche_scout.scorer import NicheScorerAgent
from agents.niche_scout.batch_scorer import BatchNicheScorerAgent
from agents.niche_scout.data_scorer import DataScorerAgent, DataScorerInput, NicheMetrics

__all__ = [
    "NicheScoutAgent",
    "NicheScorerAgent",
    "BatchNicheScorerAgent",
    "DataScorerAgent",
    "DataScorerInput",
    "NicheMetrics",
]

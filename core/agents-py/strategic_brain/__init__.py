"""
Strategic Brain — Orchestrateur stratégique central schoolsWP.

Analyse l'état complet de l'écosystème éditorial et prend des décisions data-driven :
- Lit : Knowledge Graph + Index d'autorité + Cocons + Plan ROI + Articles existants
- Détecte : faiblesses critiques, opportunités ROI, zones blanches, dérives
- Décide : quels agents déclencher, dans quel ordre, sur quel contenu
- Produit : Decision Board avec commandes CLI prêtes à l'exécution

Ce n'est pas un agent de contenu.
C'est le cerveau décisionnel qui pilote tous les autres.
"""

from agents.strategic_brain.agent import StrategicBrainAgent

__all__ = ["StrategicBrainAgent"]

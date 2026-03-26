"""
Knowledge Graph Global — Module de cartographie sémantique de l'écosystème schoolsWP.

Analyse et cartographie l'ensemble des entités, relations et zones blanches
du site schoolsWP pour maximiser l'Autorité Thématique Graph :
- Inventaire 25-50 entités (Concept / Produit / Organisation / Cas d'usage / Pilier)
- Relations majeures entre entités
- Zones blanches stratégiques (entités manquantes)
- 5 contenus à créer / 3 piliers à renforcer / 3 clusters à construire
- Score Autorité Graph X/10
"""

from agents.knowledge_graph.agent import KnowledgeGraphAgent

__all__ = ["KnowledgeGraphAgent"]

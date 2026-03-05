"""
Cocon Sémantique Builder — Générateur automatique de cocon sémantique schoolsWP.

Transforme un pilier + Knowledge Graph + scores d'autorité en architecture complète :
- Niveau 1 : Page Pilier stratégique
- Niveau 2 : Sous-clusters logiques
- Niveau 3 : 8-20 Articles Satellites avec scoring (Impact SEO / Impact Business / Effort / Connexion)
- Scoring /12 → Priorité A / B / C
- Ordre de publication stratégique
- Logique de maillage interne
- Opportunités de différenciation schoolsWP
"""
from agents.cocon_builder.agent import CoconBuilderAgent

__all__ = ["CoconBuilderAgent"]

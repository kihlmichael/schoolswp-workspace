"""
Pillar Authority Index — Index d'autorité par pilier schoolsWP.

Mesure la puissance réelle de chaque pilier éditorial selon 6 critères :
1. Couverture thématique     (0-20)
2. Profondeur moyenne        (0-20)
3. Densité d'entités         (0-15)
4. Relations explicites      (0-15)
5. Maillage interne          (0-15)
6. Différenciation           (0-15)

Score total /100 + diagnostic + 3 actions + 2 contenus manquants + 1 angle à renforcer.

Piliers supportés : SEO WordPress | LMS | CRM | Automatisation | Performance | E-commerce
"""
from agents.pillar_authority.agent import PillarAuthorityAgent

__all__ = ["PillarAuthorityAgent"]

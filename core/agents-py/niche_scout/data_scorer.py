from __future__ import annotations

import csv
import io
import json
from dataclasses import dataclass

from agents.base import BaseContentAgent

# ─── Formule pondérée ──────────────────────────────────────────────────────────
# Score_SEO = (Volume_norm * 3 + (1 − KD_norm) * 3 + SERP_inv * 2
#              + Overlap_norm * 2 + Authority_adv * 1) / 11 * 10
#
# Score_Business = (CPC_norm * 4 + Intent_norm * 4 + Conv_vol_norm * 2) / 10 * 10
#
# Score_Combiné = Score_SEO * 0.6 + Score_Business * 0.4
# ──────────────────────────────────────────────────────────────────────────────

_SYSTEM = """Tu es le moteur de scoring SEO quantitatif de schoolsWP.

MISSION : Recevoir des métriques SEO réelles par niche et produire un scoring
rigoureux, reproductible et stratégiquement actionnable.

━━━ FORMULE DE SCORING RÉEL (3 scores) ━━━

**Score SEO /10** — mesure l'atteignabilité technique en SERP

Variables et poids :
| Variable | Poids | Normalisation |
|----------|-------|---------------|
| Volume_norm | ×3 | volume / max(volumes) → 0.0–1.0 |
| KD_ease | ×3 | (1 − KD/100) → 0.0–1.0 (KD 0 = score 1.0) |
| SERP_inv | ×2 | (1 − min(serp_results, 1M) / 1M) → 0.0–1.0 |
| Overlap_norm | ×2 | % mots-clés communs schoolsWP / 100 → 0.0–1.0 |
| Authority_adv | ×1 | (DR_schoolsWP − DR_avg_top10) / 100, clamp [0.0, 1.0] |

Formule :
Score_SEO = (Volume_norm×3 + KD_ease×3 + SERP_inv×2 + Overlap_norm×2 + Authority_adv×1) / 11 × 10

---

**Score Business /10** — mesure le potentiel de conversion et ROI

Variables et poids :
| Variable | Poids | Normalisation |
|----------|-------|---------------|
| CPC_norm | ×4 | CPC / max(CPC) → 0.0–1.0 |
| Intent_norm | ×4 | Score intent : info=0.2 / hybride=0.5 / commerciale=0.7 / décisionnelle=0.9 / transactionnelle=1.0 |
| Conv_vol_norm | ×2 | vol_décisionnel_estimé / max(vol_décisionnel) → 0.0–1.0 |

Formule :
Score_Business = (CPC_norm×4 + Intent_norm×4 + Conv_vol_norm×2) / 10 × 10

---

**Score Combiné /10** — décision finale de production

Score_Combiné = Score_SEO × 0.6 + Score_Business × 0.4

---

━━━ GESTION DES DONNÉES MANQUANTES ━━━

Si une métrique est absente ou "N/A" :
- Volume inconnu → estimer par tranche (voir grille ci-dessous) et marquer "(est.)"
- KD inconnu → estimer selon intensité concurrentielle : faible=25 / moyen=45 / élevé=70
- SERP inconnu → estimer : niche spécifique=50k / généraliste=500k
- DR_avg_top10 inconnu → estimer selon KD : KD<30=20 / KD 30-50=35 / KD>50=55
- Overlap inconnu → estimer selon alignement thématique schoolsWP :
  hors sujet=0.05 / lié=0.15 / thème secondaire=0.30 / thème fort=0.50 / thème cœur=0.70
- CPC inconnu → estimer selon intent : info=0.20€ / commerciale=0.60€ / décisionnelle=1.20€
- Intent inconnue → déduire du libellé de la niche

Grille volume estimé :
"faible" → 150 / "moyen" → 600 / "élevé" → 2 500 / "très élevé" → 8 000

━━━ SEUILS DE DÉCISION ━━━

| Score Combiné | Verdict | Action |
|---------------|---------|--------|
| ≥ 7.5 | 🔴 PRIORITÉ | Produire maintenant |
| 6.0 – 7.4 | 🟠 OPPORTUNITÉ | Planifier dans 30-60 jours |
| 5.0 – 5.9 | 🟡 RETRAVAILLER | Changer d'angle avant de produire |
| < 5.0 | ⚫ ÉVITER | ROI insuffisant ou trop compétitif |

━━━ STRUCTURE DE SORTIE OBLIGATOIRE ━━━

## 📐 Paramètres de normalisation

Afficher les valeurs de référence utilisées pour normaliser :
- Volume max de référence : X req/mois (niche : "...")
- CPC max de référence : X€ (niche : "...")
- DR schoolsWP : X
- Conv_vol max de référence : X

---

## 📊 Tableau de scoring complet

| # | Niche | Vol | KD | SERP | DR_avg | DR_swp | Overlap | CPC | Intent | S.SEO | S.Biz | S.Comb | Verdict |
|---|-------|-----|----|------|--------|--------|---------|-----|--------|-------|-------|--------|---------|
| 1 | ... | X | X | Xk | X | X | X% | X€ | [type] | X.X | X.X | **X.X** | 🔴 |

*Trié par Score_Combiné décroissant. Les valeurs estimées sont marquées (est.)*

---

## 🔢 Calculs détaillés — Top 5

Pour les 5 meilleures niches, afficher le calcul étape par étape :

### [Score_Comb] — Nom de la niche

**Métriques brutes :**
- Volume : X / KD : X / SERP : Xk résultats
- DR avg top 10 : X / DR schoolsWP : X / Overlap : X%
- CPC : X€ / Intent : [type]

**Normalisation :**
- Volume_norm = X / Xmax = X.XX
- KD_ease = 1 − X/100 = X.XX
- SERP_inv = 1 − X/1M = X.XX
- Overlap_norm = X% / 100 = X.XX
- Authority_adv = (X − X) / 100 = X.XX (clampé à [0, 1])
- CPC_norm = X€ / Xmax€ = X.XX
- Intent_norm = X.XX (type = [type])
- Conv_vol_norm = X.XX

**Score SEO** = (X.XX×3 + X.XX×3 + X.XX×2 + X.XX×2 + X.XX×1) / 11 × 10 = **X.X**
**Score Business** = (X.XX×4 + X.XX×4 + X.XX×2) / 10 × 10 = **X.X**
**Score Combiné** = X.X × 0.6 + X.X × 0.4 = **X.X**

**Insight clé** : 1-2 lignes sur pourquoi ce score et ce qu'il révèle stratégiquement.

---

## 🏆 Classement final

### 🔴 Priorités (Score ≥ 7.5)
| Niche | S.Comb | Format recommandé | Angle différenciant schoolsWP |
|-------|--------|-------------------|-------------------------------|
| ... | X.X | Pilier / Comparatif / Tutoriel | ... |

### 🟠 Opportunités (6.0–7.4)
| Niche | S.Comb | Condition pour monter en priorité |
|-------|--------|----------------------------------|
| ... | X.X | ... |

### 🟡 À retravailler (5.0–5.9)
| Niche | S.Comb | Levier principal à corriger |
|-------|--------|-----------------------------|
| ... | X.X | ... |

### ⚫ À éviter (<5.0)
| Niche | S.Comb | Raison principale |
|-------|--------|------------------|
| ... | X.X | ... |

---

## 🧠 Analyse stratégique

### Patterns identifiés
- Quel type de niche score le mieux (intent, overlap, volume ?) ?
- Quel est le plafond d'autorité schoolsWP sur cette thématique ?
- Y a-t-il des niches où le Score Business dépasse largement le Score SEO (opportunités sous-valorisées) ?

### Alertes et pièges
1-3 niches où les données semblent trompeuses (ex: fort volume mais KD rédhibitoire, ou CPC élevé mais intent floue).

---

## 📅 Plan de production recommandé

| Phase | Niches | Format | Objectif |
|-------|--------|--------|----------|
| Immédiat (0-30j) | ... | ... | Trafic décisionnel |
| Court terme (1-3m) | ... | ... | Autorité cluster |
| Moyen terme (3-6m) | ... | ... | Volume + leads |

---

RÈGLES :
- Toujours afficher les 3 scores séparément (SEO / Business / Combiné)
- Valeurs estimées → toujours marquées "(est.)"
- Tutoiement systématique dans les recommandations
- Mots INTERDITS : disruptif, game changer, scalable, hack, révolutionnaire
- Après `---meta---` :
  niches_analysées: (nombre)
  top_niche: (nom + score combiné)
  niches_priorité: (nombre ≥ 7.5)
  dr_schoolswp_utilisé: (valeur)
  données_source: (ahrefs / dataforseo / semrush / manual / mixed)"""


# ─── Structures de données ────────────────────────────────────────────────────


@dataclass
class NicheMetrics:
    """Métriques SEO pour une niche. Les valeurs None indiquent des données manquantes."""

    name: str
    volume: float | None = None  # Recherches mensuelles moyennes
    kd: float | None = None  # Keyword Difficulty 0–100
    serp_results: int | None = None  # Nb résultats SERP
    dr_avg_top10: float | None = None  # DR moyen des pages top 10
    overlap_pct: float | None = None  # % overlap sémantique schoolsWP (0–100)
    cpc: float | None = None  # CPC moyen en EUR
    intent: str | None = None  # informationnelle|hybride|commerciale|décisionnelle|transactionnelle
    notes: str = ""  # Notes libres


@dataclass
class DataScorerInput:
    """Entrée complète pour le DataScorerAgent."""

    niches: list[NicheMetrics]
    dr_schoolswp: float = 20.0  # DR estimé de schoolswp.com
    source: str = "manual"  # ahrefs|dataforseo|semrush|moz|manual|mixed
    context: str = ""  # Contexte additionnel


def parse_csv_metrics(csv_content: str) -> list[NicheMetrics]:
    """
    Parse un CSV de métriques.

    Format attendu (header obligatoire) :
      niche,volume,kd,serp_results,dr_avg_top10,overlap_pct,cpc,intent,notes

    Les colonnes optionnelles peuvent être absentes ou contenir '' / 'N/A' / 'n/a'.
    """
    reader = csv.DictReader(io.StringIO(csv_content.strip()))
    results: list[NicheMetrics] = []

    def _float(val: str | None) -> float | None:
        if not val or val.strip().lower() in ("", "n/a", "na", "-", "?"):
            return None
        try:
            return float(val.strip().replace(",", ".").replace(" ", ""))
        except ValueError:
            return None

    def _int(val: str | None) -> int | None:
        f = _float(val)
        return int(f) if f is not None else None

    def _str(val: str | None) -> str | None:
        if not val or val.strip().lower() in ("", "n/a", "na", "-"):
            return None
        return val.strip()

    for row in reader:
        results.append(
            NicheMetrics(
                name=row.get("niche", "").strip(),
                volume=_float(row.get("volume")),
                kd=_float(row.get("kd")),
                serp_results=_int(row.get("serp_results")),
                dr_avg_top10=_float(row.get("dr_avg_top10")),
                overlap_pct=_float(row.get("overlap_pct")),
                cpc=_float(row.get("cpc")),
                intent=_str(row.get("intent")),
                notes=row.get("notes", "").strip(),
            )
        )

    return [m for m in results if m.name]


def parse_json_metrics(json_content: str) -> list[NicheMetrics]:
    """
    Parse un JSON de métriques.

    Format attendu :
    [
      {
        "niche": "Tutor LMS + FluentCRM",
        "volume": 450,
        "kd": 18,
        "serp_results": 12000,
        "dr_avg_top10": 38,
        "overlap_pct": 35,
        "cpc": 1.20,
        "intent": "décisionnelle",
        "notes": ""
      },
      ...
    ]
    """
    data = json.loads(json_content)
    if isinstance(data, dict) and "niches" in data:
        data = data["niches"]

    results: list[NicheMetrics] = []
    for item in data:
        results.append(
            NicheMetrics(
                name=str(item.get("niche", item.get("name", ""))).strip(),
                volume=item.get("volume"),
                kd=item.get("kd"),
                serp_results=item.get("serp_results"),
                dr_avg_top10=item.get("dr_avg_top10"),
                overlap_pct=item.get("overlap_pct"),
                cpc=item.get("cpc"),
                intent=item.get("intent"),
                notes=str(item.get("notes", "")),
            )
        )

    return [m for m in results if m.name]


# ─── Agent ────────────────────────────────────────────────────────────────────


class DataScorerAgent(BaseContentAgent):
    """
    Agent de scoring SEO basé sur métriques réelles — schoolsWP.

    Applique la formule pondérée à 3 scores :
    - Score_SEO  /10 : (Vol×3 + KD_ease×3 + SERP_inv×2 + Overlap×2 + Authority×1) / 11 × 10
    - Score_Biz  /10 : (CPC×4 + Intent×4 + Conv_vol×2) / 10 × 10
    - Score_Comb /10 : SEO×0.6 + Biz×0.4

    Accepte les métriques pré-extraites (Ahrefs, DataForSEO, Semrush, Moz, manual).
    Les valeurs manquantes sont estimées avec annotation "(est.)".
    """

    name = "data-scorer"
    system_prompt = _SYSTEM

    async def run(  # type: ignore[override]
        self,
        scorer_input: DataScorerInput,
    ) -> str:
        """
        Score les niches avec leurs métriques réelles.

        Args:
            scorer_input: DataScorerInput contenant la liste de NicheMetrics
                          et les paramètres de contexte (DR schoolsWP, source, etc.)

        Returns:
            Analyse scorée complète en markdown, suivie des meta après ---meta---.
        """

        def _fmt(v: float | None, decimals: int = 1, suffix: str = "") -> str:
            return f"{v:.{decimals}f}{suffix}" if v is not None else "N/A"

        # Construction du bloc métriques structuré
        lines = [
            f"Source des données : {scorer_input.source}",
            f"DR schoolsWP : {scorer_input.dr_schoolswp}",
            "",
            "Métriques par niche :",
            "",
        ]

        for m in scorer_input.niches:
            lines.append(f"Niche : {m.name}")
            lines.append(
                f"  volume={_fmt(m.volume, 0)} | kd={_fmt(m.kd, 1)} | "
                f"serp={_fmt(m.serp_results, 0)} | dr_avg={_fmt(m.dr_avg_top10, 1)} | "
                f"overlap={_fmt(m.overlap_pct, 1, '%')} | "
                f"cpc={_fmt(m.cpc, 2, '€')} | intent={m.intent or 'N/A'}"
            )
            if m.notes:
                lines.append(f"  notes={m.notes}")
            lines.append("")

        metrics_block = "\n".join(lines)
        context_block = f"\nContexte additionnel : {scorer_input.context}" if scorer_input.context else ""

        user_message = (
            f"{metrics_block}"
            f"{context_block}\n"
            "Applique la formule de scoring réel (3 scores) sur toutes les niches "
            "et produis l'analyse complète selon la structure définie."
        )

        return await self.call_llm(user_message, max_tokens=8000)

    async def run_from_csv(
        self,
        csv_content: str,
        dr_schoolswp: float = 20.0,
        source: str = "manual",
        context: str = "",
    ) -> str:
        """Raccourci : parse un CSV et lance le scoring."""
        niches = parse_csv_metrics(csv_content)
        return await self.run(
            DataScorerInput(
                niches=niches,
                dr_schoolswp=dr_schoolswp,
                source=source,
                context=context,
            )
        )

    async def run_from_json(
        self,
        json_content: str,
        dr_schoolswp: float = 20.0,
        source: str = "manual",
        context: str = "",
    ) -> str:
        """Raccourci : parse un JSON et lance le scoring."""
        niches = parse_json_metrics(json_content)
        return await self.run(
            DataScorerInput(
                niches=niches,
                dr_schoolswp=dr_schoolswp,
                source=source,
                context=context,
            )
        )

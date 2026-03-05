#!/usr/bin/env python3
"""
CLI — Dashboard KPI Éditorial schoolsWP

Tableau de pilotage stratégique : en 30 secondes, tu sais où tu gagnes,
où tu perds, où publier, où optimiser.

Usage :
  # Minimal (estimation sur contexte)
  python -m agents.kpi_dashboard.cli --context "8200 sessions/mois, CTR 3.2%"

  # Avec les données des agents
  python -m agents.kpi_dashboard.cli \\
    --authority-file audit/piliers/summary.md \\
    --roi-file plans/plan-roi.md \\
    --context "8200 sessions +12%, 45 leads email" \\
    --period "Février 2026" \\
    --output dashboard/kpi-fev-2026.md

  # Export JSON pour Google Sheets / Notion
  python -m agents.kpi_dashboard.cli \\
    --authority-file audit/piliers/summary.md \\
    --roi-file plans/plan-roi.md \\
    --export-json dashboard/kpi.json

  # Scanner un répertoire save-dir pour les scores LLM
  python -m agents.kpi_dashboard.cli \\
    --scan-articles articles/ \\
    --authority-file audit/piliers/summary.md
"""
import argparse
import asyncio
import io
import json
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.kpi_dashboard.agent import KpiDashboardAgent

# ──────────────────────────────────────────────
# Parsers — extraire les données numériques
# ──────────────────────────────────────────────

_PILLAR_KEYS = {
    "seo wordpress": "seo",
    "lms wordpress": "lms",
    "crm wordpress": "crm",
    "automatisation wordpress": "automatisation",
    "performance wordpress": "performance",
    "e-commerce wordpress": "ecommerce",
}


def parse_pillar_scores(text: str) -> dict[str, int]:
    """
    Extrait les scores /100 depuis l'output de pillar_authority.cli.
    Cherche les patterns : | Pilier | XX | et | **Score total** | **XX/100** |
    """
    scores: dict[str, int] = {}

    # Pattern 1 : tableau récapitulatif summary (| SEO WordPress | XX/100 | ... |)
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 4:
            continue
        label = parts[1].lower().strip("* ")
        # Cherche score /100 dans les colonnes suivantes
        for col in parts[2:]:
            m = re.search(r"(\d+)/100", col)
            if m:
                key = _PILLAR_KEYS.get(label)
                if key:
                    scores[key] = int(m.group(1))
                break

    # Pattern 2 : analyse individuelle — cherche "## Pilier : X" + "**Score total** | **X/100**"
    current_pillar: str | None = None
    for line in text.splitlines():
        pillar_match = re.match(r"##\s+Pilier\s*:\s*(.+)", line, re.IGNORECASE)
        if pillar_match:
            label = pillar_match.group(1).strip().lower()
            current_pillar = _PILLAR_KEYS.get(label)

        score_match = re.search(r"\*\*Score total\*\*\s*\|\s*\*\*(\d+)/100\*\*", line)
        if score_match and current_pillar and current_pillar not in scores:
            scores[current_pillar] = int(score_match.group(1))

    return scores


def parse_article_kpis(text: str) -> list[dict]:
    """
    Extrait les KPI articles depuis l'output de roi_editorial_plan.cli.
    Cherche les lignes de tableau : | N | Titre | intent | SEO | Biz | Auth | Effort | X.X | Priorité |
    """
    articles = []
    in_table = False

    for line in text.splitlines():
        if "Tableau de scoring" in line or "Articles Satellites" in line:
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("---") and articles:
            break
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue

        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 9:
            continue

        title = parts[2]
        intent = parts[3] if len(parts) > 3 else "N/D"

        def _int(val: str) -> int | None:
            m = re.search(r"(\d+)", val)
            return int(m.group(1)) if m else None

        def _float(val: str) -> float | None:
            m = re.search(r"(\d+\.\d+|\d+)", val)
            return float(m.group(1)) if m else None

        # Colonnes : # | Titre | Intent | SEO | Biz | Auth | Effort | ROI | Priorité
        seo = _int(parts[4]) if len(parts) > 4 else None
        biz = _int(parts[5]) if len(parts) > 5 else None
        auth = _int(parts[6]) if len(parts) > 6 else None
        effort = _int(parts[7]) if len(parts) > 7 else None
        roi = _float(parts[8]) if len(parts) > 8 else None

        # Priorité — cherche A, B ou C dans la dernière colonne
        priority_col = parts[-2] if len(parts) > 2 else ""
        priority = "A" if "A" in priority_col else ("B" if "B" in priority_col else "C")

        if title and title not in ("Titre", "---"):
            articles.append({
                "title": title,
                "intent": intent,
                "seo": seo,
                "biz": biz,
                "auth": auth,
                "effort": effort,
                "roi": roi,
                "priority": priority,
            })

    return articles


def parse_llm_scores_from_dir(scan_dir: Path) -> list[dict]:
    """
    Scan un répertoire contenant des sous-dossiers save-dir d'article_pipeline.
    Cherche les fichiers v3.md et extrait les scores LLM (après ---llm-scores---).
    """
    results = []

    for v3_file in sorted(scan_dir.rglob("v3.md")):
        text = v3_file.read_text(encoding="utf-8", errors="replace")
        marker = "---llm-scores---"
        if marker not in text:
            continue

        scores_block = text.split(marker, 1)[1]
        article_dir = v3_file.parent.name

        scores: dict[str, float | None] = {
            "extractibilite": None,
            "clarte": None,
            "autorite": None,
            "structure": None,
            "global": None,
        }
        for line in scores_block.splitlines():
            for key in scores:
                m = re.search(rf"{key[:5]}.*?(\d+(?:\.\d+)?)/10", line, re.IGNORECASE)
                if m:
                    scores[key] = float(m.group(1))

        results.append({
            "article": article_dir,
            "extractibilite": scores["extractibilite"],
            "clarte": scores["clarte"],
            "autorite": scores["autorite"],
            "global": scores["global"],
        })

    return results


def compute_ecosystem_score(
    pillar_scores: dict[str, int],
    article_kpis: list[dict],
    llm_scores: list[dict],
    seo_growth: float = 50.0,
) -> dict:
    """
    Score Écosystème = (Auth×0.3) + (ROI_norm×0.3) + (SEO×0.2) + (LLM×0.2)
    Retourne les composantes et le score final /100.
    """
    auth_mean = (
        sum(pillar_scores.values()) / len(pillar_scores)
        if pillar_scores
        else 0.0
    )

    roi_values = [a["roi"] for a in article_kpis if a.get("roi") is not None]
    roi_mean_norm = (
        (sum(roi_values) / len(roi_values) / 9.0) * 100
        if roi_values
        else 0.0
    )

    llm_globals = [s["global"] for s in llm_scores if s.get("global") is not None]
    llm_mean_norm = (
        (sum(llm_globals) / len(llm_globals)) * 10
        if llm_globals
        else 0.0
    )

    score = (
        auth_mean * 0.3
        + roi_mean_norm * 0.3
        + seo_growth * 0.2
        + llm_mean_norm * 0.2
    )

    return {
        "score": round(score, 1),
        "auth_mean": round(auth_mean, 1),
        "roi_norm": round(roi_mean_norm, 1),
        "seo_growth": round(seo_growth, 1),
        "llm_norm": round(llm_mean_norm, 1),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kpi-dashboard",
        description=(
            "Dashboard KPI Éditorial schoolsWP — "
            "Score Écosystème + 5 vues de pilotage stratégique"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Minimal\n"
            "  python -m agents.kpi_dashboard.cli\n\n"
            "  # Avec données contextuelles\n"
            "  python -m agents.kpi_dashboard.cli \\\n"
            '    --context "8 200 sessions/mois +12%, CTR 3.2%, 45 leads email" \\\n'
            '    --period "Février 2026"\n\n'
            "  # Avec tous les fichiers agents\n"
            "  python -m agents.kpi_dashboard.cli \\\n"
            "    --authority-file audit/piliers/summary.md \\\n"
            "    --roi-file plans/plan-roi.md \\\n"
            "    --cocon-file cocons/lms.md \\\n"
            "    --scan-articles articles/ \\\n"
            "    --output dashboard/kpi.md \\\n"
            "    --export-json dashboard/kpi.json\n\n"
            "Flux recommandé :\n"
            "  1. pillar_authority.cli --all → audit/piliers/summary.md\n"
            "  2. roi_editorial_plan.cli     → plans/plan-roi.md\n"
            "  3. article_pipeline (save-dir) → articles/<slug>/\n"
            "  4. kpi_dashboard.cli          ← tu es ici"
        ),
    )
    parser.add_argument(
        "--period",
        default=None,
        metavar="PÉRIODE",
        help="Période d'analyse (ex: 'Février 2026', 'T1 2026')",
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Données macro (trafic, CTR, conversions) non extractibles automatiquement "
            "(ex: '8 200 sessions +12%/mois, CTR 3.2%, 45 leads email, 12 conversions affiliées')"
        ),
    )
    parser.add_argument(
        "--authority-file",
        default=None,
        metavar="FICHIER",
        help="Fichier autorité (.md) — produit par pillar_authority.cli. summary.md recommandé.",
    )
    parser.add_argument(
        "--roi-file",
        default=None,
        metavar="FICHIER",
        help="Fichier plan ROI (.md) — produit par roi_editorial_plan.cli",
    )
    parser.add_argument(
        "--cocon-file",
        default=None,
        metavar="FICHIER",
        help="Fichier cocon sémantique (.md) — produit par cocon_builder.cli",
    )
    parser.add_argument(
        "--scan-articles",
        default=None,
        metavar="RÉPERTOIRE",
        help=(
            "Répertoire contenant des sous-dossiers save-dir d'article_pipeline. "
            "Scan automatique des v3.md pour extraire les scores LLM."
        ),
    )
    parser.add_argument(
        "--seo-growth",
        type=float,
        default=50.0,
        metavar="VALEUR",
        help=(
            "Score SEO croissance /100 pour le calcul Score Écosystème. "
            "50 = neutre, >50 = croissance, <50 = déclin (défaut: 50)"
        ),
    )
    parser.add_argument(
        "--export-json",
        default=None,
        metavar="FICHIER",
        help="Exporter les KPI numériques en JSON (pour Google Sheets / Notion / Looker Studio)",
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
        help="Fichier de sortie (.md). Si absent, affiche dans le terminal.",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    def _load(path_str: str | None, label: str) -> str | None:
        if not path_str:
            return None
        p = Path(path_str)
        if not p.exists():
            print(f"[kpi-dashboard] ⚠ {label} introuvable : {p} — ignoré", flush=True)
            return None
        content = p.read_text(encoding="utf-8", errors="replace")
        print(f"[kpi-dashboard] {label} chargé ({len(content):,} chars)", flush=True)
        return content

    authority_content = _load(args.authority_file, "Autorité piliers")
    roi_content = _load(args.roi_file, "Plan ROI")
    cocon_content = _load(args.cocon_file, "Cocon")

    # Parser les scores numériques depuis les fichiers
    pillar_scores: dict[str, int] = {}
    if authority_content:
        pillar_scores = parse_pillar_scores(authority_content)
        if pillar_scores:
            print(
                f"[kpi-dashboard] Scores piliers extraits : "
                + ", ".join(f"{k}={v}/100" for k, v in pillar_scores.items()),
                flush=True,
            )

    article_kpis: list[dict] = []
    if roi_content:
        article_kpis = parse_article_kpis(roi_content)
        if article_kpis:
            print(
                f"[kpi-dashboard] {len(article_kpis)} articles parsés depuis plan ROI",
                flush=True,
            )

    llm_scores: list[dict] = []
    if args.scan_articles:
        scan_dir = Path(args.scan_articles)
        if scan_dir.exists():
            llm_scores = parse_llm_scores_from_dir(scan_dir)
            if llm_scores:
                print(
                    f"[kpi-dashboard] {len(llm_scores)} scores LLM extraits depuis {scan_dir}",
                    flush=True,
                )

    # Score Écosystème (calculé côté Python pour fiabilité)
    eco = compute_ecosystem_score(
        pillar_scores, article_kpis, llm_scores, args.seo_growth
    )
    print(
        f"[kpi-dashboard] Score Écosystème calculé : {eco['score']}/100 "
        f"(Auth={eco['auth_mean']} ROI={eco['roi_norm']} SEO={eco['seo_growth']} LLM={eco['llm_norm']})",
        flush=True,
    )

    # Export JSON si demandé
    if args.export_json:
        export_data = {
            "period": args.period,
            "ecosystem_score": eco,
            "pillar_scores": pillar_scores,
            "article_kpis": article_kpis,
            "llm_scores": llm_scores,
        }
        json_path = Path(args.export_json)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(
            json.dumps(export_data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[kpi-dashboard] Export JSON → {json_path}", flush=True)

    print("", flush=True)

    # Génération du dashboard avec le LLM
    agent = KpiDashboardAgent(model=args.model)

    dashboard = await agent.run(
        period=args.period,
        context=args.context,
        pillar_scores=pillar_scores if pillar_scores else None,
        article_kpis=article_kpis if article_kpis else None,
        authority_content=authority_content if not pillar_scores else None,
        roi_content=roi_content if not article_kpis else None,
        cocon_content=cocon_content,
        llm_scores=llm_scores if llm_scores else None,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(dashboard, encoding="utf-8")
        print(f"[kpi-dashboard] Dashboard sauvegardé → {output_path}")
    else:
        print(dashboard)


if __name__ == "__main__":
    asyncio.run(main())

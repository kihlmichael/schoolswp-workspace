"""Crée une card FluentBoards quand publish_ready Score < threshold.

Lit FLUENTBOARDS_AUDIT_WEBHOOK_URL depuis .env, POST une task avec :
    - title : [Publish {score}/100] {keyword} — {pillar}
    - description : Markdown (sous-scores + chemin article + bloc le plus faible)
    - stage : "Open" (valeur par défaut du webhook côté FluentBoards)

Skip silencieux si webhook URL absente ou score >= threshold.
Exit code toujours 0 — ne bloque jamais l'audit parent.

Usage standalone :
    python tools/scripts/notify-audit-card.py \\
        --keyword "fluentcrm avis" --pillar CRM --intent informationnelle \\
        --score 65 --threshold 70 \\
        --seo 72 --llm 55 --conv 68 --auth 70 \\
        --file content/articles/crm/fluentcrm-avis.md \\
        --weakest "Citabilité IA"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_env(env_path: Path) -> dict[str, str]:
    if not env_path.exists():
        return {}
    out: dict[str, str] = {}
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def post_json(url: str, payload: dict, timeout: int = 10) -> tuple[int, str]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.reason
    except Exception as exc:
        return 0, str(exc)


def _emoji_for_score(score: int) -> str:
    if score >= 90:
        return "✅"
    if score >= 80:
        return "🟡"
    if score >= 70:
        return "🟠"
    return "🔴"


def build_payload(args: argparse.Namespace) -> dict:
    title = f"[Publish {args.score}/100] {args.keyword}"
    if args.pillar:
        title += f" — {args.pillar}"

    sub_lines = []
    for name, val in [
        ("SEO Structure", args.seo),
        ("Citabilité IA", args.llm),
        ("Conversion", args.conv),
        ("Autorité thème", args.auth),
    ]:
        if val is not None:
            sub_lines.append(f"- **{name}** : {val}/100 {_emoji_for_score(val)}")

    desc_parts = [
        f"## Publish Score : {args.score}/100 {_emoji_for_score(args.score)}",
        f"**Seuil déclencheur** : {args.threshold}/100",
        "",
        "## Contexte",
        f"- **Mot-clé** : `{args.keyword}`",
    ]
    if args.pillar:
        desc_parts.append(f"- **Pillar** : `{args.pillar}`")
    if args.intent:
        desc_parts.append(f"- **Intent** : `{args.intent}`")
    desc_parts.append("")

    if sub_lines:
        desc_parts.append("## Sous-scores")
        desc_parts.extend(sub_lines)
        desc_parts.append("")

    if args.weakest:
        desc_parts.append(f"## Bloc le plus faible\n`{args.weakest}` — à prioriser dans la révision.\n")

    if args.file:
        desc_parts.append(f"## Article\n`{args.file}`")

    return {
        "title": title,
        "description": "\n".join(desc_parts),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Card FluentBoards sur audit fail")
    parser.add_argument("--keyword", required=True)
    parser.add_argument("--pillar", default="")
    parser.add_argument("--intent", default="")
    parser.add_argument("--score", type=int, required=True, help="Publish Score composite /100")
    parser.add_argument("--threshold", type=int, default=70, help="Seuil déclencheur (défaut 70)")
    parser.add_argument("--seo", type=int, default=None, help="Sous-score SEO Structure")
    parser.add_argument("--llm", type=int, default=None, help="Sous-score Citabilité IA")
    parser.add_argument("--conv", type=int, default=None, help="Sous-score Conversion")
    parser.add_argument("--auth", type=int, default=None, help="Sous-score Autorité thème")
    parser.add_argument("--file", default="", help="Chemin du fichier article audité")
    parser.add_argument("--weakest", default="", help="Nom du module le plus faible")
    args = parser.parse_args()

    if args.score >= args.threshold:
        print(f"[audit-card] Score {args.score}/{args.threshold} — pas d'alerte nécessaire")
        return 0

    env = {**load_env(PROJECT_ROOT / ".env"), **os.environ}
    webhook_url = env.get("FLUENTBOARDS_AUDIT_WEBHOOK_URL", "")

    if not webhook_url:
        print("[audit-card] FLUENTBOARDS_AUDIT_WEBHOOK_URL absent — skip")
        return 0

    payload = build_payload(args)
    status, detail = post_json(webhook_url, payload)
    if status >= 300 or status == 0:
        print(f"[audit-card] FluentBoards KO ({status}): {detail[:200]}", file=sys.stderr)
    else:
        print(f"[audit-card] Card créée dans FluentBoards (HTTP {status})")

    return 0


if __name__ == "__main__":
    sys.exit(main())

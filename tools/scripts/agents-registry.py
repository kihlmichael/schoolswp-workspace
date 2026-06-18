"""
Agents Registry — scan .claude/agents/*.md et régénère les sections auto de INDEX.md.

Usage :
  python tools/scripts/agents-registry.py             # rapport (rien n'est écrit)
  python tools/scripts/agents-registry.py --sync      # régénère INDEX.md
  python tools/scripts/agents-registry.py --check     # exit 1 si INDEX.md désynchronisé (CI / pre-commit)

Le script ne régénère QUE les zones marquées :
  <!-- AUTO:HEADER:START --> ... <!-- AUTO:HEADER:END -->
  <!-- AUTO:TABLES:START --> ... <!-- AUTO:TABLES:END -->

Tout le reste de INDEX.md (routing, règles de conflit, maintenance) reste manuel.

Pour ajouter un agent : créer .claude/agents/<nom>.md avec frontmatter, ajouter une ligne
dans GROUPS ci-dessous, lancer `--sync`.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

# Windows + Python: force UTF-8 stdout to support accents and unicode glyphs
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[2]
AGENTS_DIR = REPO_ROOT / ".claude" / "agents"
INDEX_PATH = AGENTS_DIR / "INDEX.md"

# ── Mapping agent -> groupe ─────────────────────────────────────────────────
# Un agent inconnu de ce dict atterrit dans le groupe "unclassified" et
# le script alerte. C'est volontaire : pas d'auto-classification silencieuse.

GROUPS: dict[str, str] = {
    # Stratégie / COMEX (orchestration, ne publie pas)
    "directeur-marketing-ia": "strategy",
    # Contenu éditorial schoolsWP
    "studio": "editorial",
    "radar": "editorial",
    "pulse": "editorial",
    "flow": "editorial",
    "framework-adapter-fr": "editorial",
    "reddit": "editorial",
    "thruuu-article-orchestrator": "editorial",
    # YouTube OS
    "youtube-os-orchestrator": "youtube-os",
    "youtube-strategy-scout": "youtube-os",
    "youtube-script-writer": "youtube-os",
    "youtube-seo-packager": "youtube-os",
    "youtube-thumbnail-director": "youtube-os",
    "youtube-clipper": "youtube-os",
    "youtube-publisher-scheduler": "youtube-os",
    "youtube-analytics-learner": "youtube-os",
    "youtube-quality-auditor": "youtube-os",
    # Spécialistes domaine
    "seo-specialist": "specialists",
    "google-business-expert": "specialists",
    "pinterest-expert": "specialists",
    "aidesigner-frontend": "specialists",
    "ads-operator": "specialists",
    "skoatch-publisher": "specialists",
    # Code review / qualité — read-only
    "code-reviewer": "code-review",
    "adr-writer": "code-review",
    "plan-challenger": "code-review",
    "output-evaluator": "code-review",
    "silent-failure-hunter": "code-review",
    # Harness / infra
    "harness-optimizer": "harness",
    # Hors schoolsWP (projets personnels)
    "ofm-bot": "personal",
}

GROUP_ORDER = [
    "strategy",
    "editorial",
    "youtube-os",
    "specialists",
    "code-review",
    "harness",
    "personal",
    "unclassified",
]

GROUP_LABELS = {
    "strategy": "Stratégie / COMEX (orchestration)",
    "editorial": "Contenu éditorial schoolsWP",
    "youtube-os": "YouTube OS",
    "specialists": "Spécialistes domaine",
    "code-review": "Code review / qualité — read-only",
    "harness": "Harness / infra",
    "personal": "Hors schoolsWP (projets personnels)",
    "unclassified": "Non classé (ajouter au mapping GROUPS du script)",
}

# ── Parsing frontmatter ─────────────────────────────────────────────────────

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parser minimaliste pour les frontmatters d'agents. Gère :
    - `key: value` simple
    - `key: "value"` quoted
    - `key: >\n  multi\n  line` block scalar
    - `tools: [a, b, c]` ou `tools: ["a", "b"]` ou `tools: a, b, c`
    """
    m = _FM_RE.match(text)
    if not m:
        return {}
    body = m.group(1)
    out: dict[str, str] = {}
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        kv = re.match(r"^([A-Za-z_-]+)\s*:\s*(.*)$", line)
        if not kv:
            i += 1
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val == ">" or val == "|":
            # Block scalar : agrège les lignes indentées suivantes
            collected = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  ") or not lines[j].strip()):
                collected.append(lines[j].strip())
                j += 1
            out[key] = " ".join(c for c in collected if c).strip()
            i = j
        else:
            # Valeur sur la même ligne (peut être quoted)
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            out[key] = val
            i += 1
    return out


def normalize_tools(raw: str) -> str:
    """`["Read", "Grep"]` / `[Read, Grep]` / `Read, Grep` → `Read, Grep`."""
    if not raw:
        return "(par défaut)"
    s = raw.strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    parts = [p.strip().strip('"').strip("'") for p in s.split(",")]
    parts = [p for p in parts if p]
    return ", ".join(parts) if parts else "(par défaut)"


def short_description(raw: str, limit: int = 200) -> str:
    """Première phrase ou jusqu'à un marqueur naturel (`Triggers:`, `Do NOT`, `Examples:`).
    Tronque à `limit` caractères max.
    """
    if not raw:
        return ""
    text = raw.replace("\n", " ").strip()
    # Coupe sur premier marqueur naturel
    for marker in ["Triggers:", "Triggers :", "Do NOT use", "Examples:", "Source de vérité"]:
        idx = text.find(marker)
        if idx > 0:
            text = text[:idx].strip().rstrip(".") + "."
            break
    # Coupe sur première phrase si encore long
    if len(text) > limit:
        period = text.rfind(".", 0, limit)
        text = text[: period + 1] if period > 60 else text[:limit].rstrip() + "…"
    return text.strip()


# ── Scan ─────────────────────────────────────────────────────────────────────


def scan_agents() -> list[dict[str, str]]:
    """Retourne la liste des agents avec leurs métadonnées."""
    agents = []
    for path in sorted(AGENTS_DIR.glob("*.md")):
        if path.name == "INDEX.md":
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        name = fm.get("name") or path.stem
        agents.append(
            {
                "file": path.name,
                "name": name,
                "model": fm.get("model", "(défaut)"),
                "tools": normalize_tools(fm.get("tools", "")),
                "description": short_description(fm.get("description", "")),
                "group": GROUPS.get(name, "unclassified"),
            }
        )
    return agents


# ── Génération markdown ──────────────────────────────────────────────────────


def render_header(total: int, today: str) -> str:
    return f"<!-- AUTO:HEADER:START -->\n**Total** : {total} sub-agents | **Mis à jour** : {today}\n<!-- AUTO:HEADER:END -->"


def render_tables(agents: list[dict[str, str]]) -> str:
    """Génère les tables détaillées par groupe."""
    by_group: dict[str, list[dict[str, str]]] = {g: [] for g in GROUP_ORDER}
    for a in agents:
        by_group.setdefault(a["group"], []).append(a)

    blocks = ["<!-- AUTO:TABLES:START -->"]
    for group in GROUP_ORDER:
        items = by_group.get(group, [])
        if not items:
            continue
        blocks.append("")
        blocks.append(f"### {GROUP_LABELS[group]}")
        blocks.append("")
        blocks.append("| Agent | Modèle | Outils | Description |")
        blocks.append("| --- | --- | --- | --- |")
        for a in items:
            desc = a["description"].replace("|", "\\|")
            tools = a["tools"].replace("|", "\\|")
            blocks.append(f"| `{a['name']}` | {a['model']} | {tools} | {desc} |")
    blocks.append("")
    blocks.append("<!-- AUTO:TABLES:END -->")
    return "\n".join(blocks)


def regenerate_index(text: str, header_block: str, tables_block: str) -> str:
    """Remplace les zones marquées dans INDEX.md."""
    out = re.sub(
        r"<!-- AUTO:HEADER:START -->.*?<!-- AUTO:HEADER:END -->",
        header_block,
        text,
        count=1,
        flags=re.DOTALL,
    )
    out = re.sub(
        r"<!-- AUTO:TABLES:START -->.*?<!-- AUTO:TABLES:END -->",
        tables_block,
        out,
        count=1,
        flags=re.DOTALL,
    )
    return out


# ── Rapport ──────────────────────────────────────────────────────────────────


def print_report(agents: list[dict[str, str]]) -> None:
    print(f"Scan : {len(agents)} agents dans {AGENTS_DIR.relative_to(REPO_ROOT)}")
    by_group: dict[str, int] = {}
    for a in agents:
        by_group[a["group"]] = by_group.get(a["group"], 0) + 1
    print("\nRépartition par groupe :")
    for g in GROUP_ORDER:
        if g in by_group:
            label = GROUP_LABELS[g]
            print(f"  {by_group[g]:>3}  {label}")
    unclassified = [a for a in agents if a["group"] == "unclassified"]
    if unclassified:
        print("\n⚠  Agents non classés (ajouter au dict GROUPS du script) :")
        for a in unclassified:
            print(f"   - {a['name']}  ({a['file']})")


# ── Main ─────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sync", action="store_true", help="régénère INDEX.md")
    parser.add_argument("--check", action="store_true", help="exit 1 si INDEX.md désynchronisé (CI / pre-commit)")
    args = parser.parse_args()

    if not AGENTS_DIR.exists():
        print(f"ERREUR : {AGENTS_DIR} introuvable", file=sys.stderr)
        return 2
    if not INDEX_PATH.exists():
        print(f"ERREUR : {INDEX_PATH} introuvable", file=sys.stderr)
        return 2

    agents = scan_agents()
    print_report(agents)

    today = date.today().isoformat()
    header_block = render_header(len(agents), today)
    tables_block = render_tables(agents)
    current = INDEX_PATH.read_text(encoding="utf-8")
    regenerated = regenerate_index(current, header_block, tables_block)

    if args.check:
        # Comparaison qui ignore uniquement la date (sinon --check casse chaque jour)
        norm_current = re.sub(r"\*\*Mis à jour\*\* : \d{4}-\d{2}-\d{2}", "DATE", current)
        norm_regen = re.sub(r"\*\*Mis à jour\*\* : \d{4}-\d{2}-\d{2}", "DATE", regenerated)
        if norm_current != norm_regen:
            print(
                "\n❌ INDEX.md désynchronisé. Lancer : python tools/scripts/agents-registry.py --sync", file=sys.stderr
            )
            return 1
        print("\n✓ INDEX.md à jour")
        return 0

    if args.sync:
        if regenerated == current:
            print("\n✓ INDEX.md déjà à jour (aucune modification)")
            return 0
        INDEX_PATH.write_text(regenerated, encoding="utf-8")
        print(f"\n✓ INDEX.md régénéré ({len(agents)} agents, {today})")
        return 0

    # Mode par défaut : rapport + diff status, pas d'écriture
    if regenerated == current:
        print("\n✓ INDEX.md à jour")
    else:
        print("\nℹ INDEX.md désynchronisé — relancer avec --sync pour régénérer")
    return 0


if __name__ == "__main__":
    sys.exit(main())

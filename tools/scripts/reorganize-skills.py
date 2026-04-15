#!/usr/bin/env python3
"""Reorganize Claude Code skills into category subdirectories.

Usage:
    python reorganize-skills.py --dry-run   # Preview moves
    python reorganize-skills.py --execute   # Actually move
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# ── Locations ──────────────────────────────────────────────────────────
WS_SKILLS = Path(r"d:\VS Code\CLAUDE CODE\.claude\skills")
PJ_SKILLS = Path(r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\skills")

# ── Category mapping ──────────────────────────────────────────────────
# Format: "skill-name": "category"
# -workspace variants auto-follow their parent

WS_MAP = {
    # affiliation — (none in workspace)
    # contenu
    "branding": "contenu",
    "schoolswp-branding-studio": "contenu",
    "schoolswp-content-studio": "contenu",
    "thruuu-content-strategist": "contenu",
    # dev
    "docker-expert": "dev",
    "frontend-design": "dev",
    "web-artifacts-builder": "dev",
    # fichiers
    "csv-excel-report-skill": "fichiers",
    "docx": "fichiers",
    "pdf": "fichiers",
    "xlsx": "fichiers",
    # ia-llm
    "agents": "ia-llm",
    "finetuning": "ia-llm",
    "gemini": "ia-llm",
    "gemini-api-dev": "ia-llm",
    "gemini-interactions-api": "ia-llm",
    "gemini-live-api-dev": "ia-llm",
    "mcp-builder": "ia-llm",
    "prompt-master": "ia-llm",
    "vertex-ai-api-dev": "ia-llm",
    # medias
    "canvas-design": "medias",
    "heygen": "medias",
    "music": "medias",
    "openai-imagegen": "medias",
    "openai-whisper": "medias",
    "openai-whisper-api": "medias",
    "remotion-best-practices": "medias",
    "sound-effects": "medias",
    "speech-to-text": "medias",
    "svg-burger-illustration": "medias",
    "text-to-speech": "medias",
    "video-translate": "medias",
    # n8n
    "n8n-code-javascript": "n8n",
    "n8n-expression-syntax": "n8n",
    "n8n-google-sheets-mapper": "n8n",
    "n8n-mcp-tools-expert": "n8n",
    "n8n-node-configuration": "n8n",
    "n8n-sheets-multi-agent": "n8n",
    "n8n-validation-expert": "n8n",
    "n8n-workflow-architect": "n8n",
    "n8n-workflow-patterns": "n8n",
    # seo
    "schema-markup": "seo",
    "seo-page-audit": "seo",
    # social
    "instagram-strategy": "social",
    "pinterest-strategy": "social",
    "social-content": "social",
    "telegram-claude-bridge": "social",
    "youtube-shorts-schoolswp": "social",
    # wordpress
    "wordpress-pro": "wordpress",
    "wordpress-router": "wordpress",
    "wp-abilities-api": "wordpress",
    "wp-block-development": "wordpress",
    "wp-block-themes": "wordpress",
    "wpds": "wordpress",
    "wp-interactivity-api": "wordpress",
    "wp-performance": "wordpress",
    "wp-phpstan": "wordpress",
    "wp-playground": "wordpress",
    "wp-plugin-development": "wordpress",
    "wp-project-triage": "wordpress",
    "wp-rest-api": "wordpress",
    "wp-wpcli-and-ops": "wordpress",
    # ops
    "brand-guidelines": "ops",
    "consolidation-ops": "ops",
    "firecrawl": "ops",
    "local-prospector": "ops",
    "mini-offer-builder": "ops",
    "schoolswp": "ops",
    "setup-api-key": "ops",
    "skill-creator": "ops",
    "workspace-guardian": "ops",
    # orphan -workspace variants (base skills are in project, not workspace)
    "schoolswp-agent-constitution-workspace": "engines",
    "schoolswp-fast-websearch-workspace": "ops",
    "schoolswp-thumbnail-strategist-workspace": "social",
    "schoolswp-utm-convention-workspace": "ops",
}

PJ_MAP = {
    # affiliation
    "affiliation-article-detector": "affiliation",
    "affiliation-block-system": "affiliation",
    "affiliation-opportunity-scanner": "affiliation",
    "affiliation-optimizer": "affiliation",
    "affiliation-potential-scoring": "affiliation",
    "comparatif-affiliate-engine": "affiliation",
    "comparatif-affilie-template": "affiliation",
    "money-articles-30-plan": "affiliation",
    "money-page-generator": "affiliation",
    "money-pages-framework": "affiliation",
    "strategic-score-combined": "affiliation",
    # authority
    "authority-accelerator": "authority",
    "authority-domination-50p": "authority",
    "authority-domination-roadmap": "authority",
    "authority-email-launch": "authority",
    "authority-launch": "authority",
    "authority-loop": "authority",
    "authority-m1m3-execution": "authority",
    "authority-method": "authority",
    "authority-promise": "authority",
    "authority-proof": "authority",
    "authority-salespage": "authority",
    "authority-system-90": "authority",
    "authority-templates": "authority",
    # contenu
    "article-audit-score": "contenu",
    "article-multiformat": "contenu",
    "brain": "contenu",
    "brain-autonome": "contenu",
    "brain-lite": "contenu",
    "branding": "contenu",
    "clairtexte": "contenu",
    "content-factory-autonome": "contenu",
    "email-to-content": "contenu",
    "formation-pipeline": "contenu",
    "landing-page-factory": "contenu",
    "plugin-email-sequence": "contenu",
    "rewrite-conversion": "contenu",
    "schoolswp-article-workflow": "contenu",
    "thruuu-writer": "contenu",
    # engines
    "agent-constitution": "engines",
    "claude-project-setup": "engines",
    "credo-engine": "engines",
    "decision-engine": "engines",
    "dito-engine": "engines",
    "engine": "engines",
    "os-claude-system": "engines",
    "os-router": "engines",
    "pact-engine": "engines",
    "performance-loop": "engines",
    "race-engine": "engines",
    "specs-engine": "engines",
    # ia-llm
    "ai-brain-audit": "ia-llm",
    "ai-brain-optimization": "ia-llm",
    "ai-brain-production": "ia-llm",
    "ai-brain-transformation": "ia-llm",
    "ai-citation-opportunity": "ia-llm",
    "ai-platform-architect-system": "ia-llm",
    "ai-playbook-schoolswp": "ia-llm",
    "ai-strategic-brain": "ia-llm",
    "intelligence-system-training": "ia-llm",
    "meta-prompt-creator": "ia-llm",
    "mcp-builder": "ia-llm",
    "conversational-query-mapper": "ia-llm",
    # n8n
    "n8n-reverse-engineer": "n8n",
    "n8n-workflow-architect": "n8n",
    # seo
    "cluster-cocon-automatique": "seo",
    "cocon-map-schoolswp": "seo",
    "geo-architect": "seo",
    "geo-gsc-pipeline": "seo",
    "lms-cocon-roi-prioritization": "seo",
    "m1m3-urls-internal-linking": "seo",
    "niche-detector-reachable": "seo",
    "seo-audit": "seo",
    "seo-brief-generator": "seo",
    "seo-competitor-gap-radar": "seo",
    "seo-pipeline": "seo",
    "topical-authority-map": "seo",
    "wpmarmite-business-strategy": "seo",
    "youtube-omnichannel-engine": "seo",
    # social
    "instagram-strategy": "social",
    "linkedin": "social",
    "pinterest-pipeline": "social",
    "reddit": "social",
    "schoolswp-youtube-studio": "social",
    "thumbnail-strategist": "social",
    "youtube": "social",
    "youtube-extractor": "social",
    # wordpress
    "dev-wordpress": "wordpress",
    "wordpress": "wordpress",
    "wp-image-metadata-seo": "wordpress",
    # ops
    "audit": "ops",
    "consolidation-ops": "ops",
    "etude-marche-france": "ops",
    "fast-websearch": "ops",
    "finance-freedom-flow": "ops",
    "firecrawl": "ops",
    "index-manager": "ops",
    "local-prospecting-pipeline": "ops",
    "marketing": "ops",
    "note-to-sop": "ops",
    "publish-repo": "ops",
    "skill-creator": "ops",
    "skills-registry": "ops",
    "task-system": "ops",
    "todo": "ops",
    "utm-convention": "ops",
    "vscode-agent-visual": "ops",
    "workspace-audit": "ops",
    "workspace-guardian": "ops",
    "workflow-debug": "ops",
    "workflow-doc": "ops",
    "workflow-master": "ops",
    "workspace-hygiene": "ops",
}


# ── Category labels (for INDEX.md) ────────────────────────────────────
CATEGORY_LABELS = {
    "affiliation": "Affiliation & Monetisation",
    "authority": "Authority System",
    "contenu": "Contenu & Redaction",
    "dev": "Dev (Backend, Frontend, Outils)",
    "engines": "schoolsWP OS — Moteurs & Frameworks",
    "fichiers": "Fichiers & Bureautique",
    "ia-llm": "IA, LLM & Agents",
    "medias": "Medias (Audio, Video, Image)",
    "n8n": "n8n & Workflows",
    "securite": "Securite",
    "seo": "SEO & Autorite thematique",
    "social": "Social Media",
    "wordpress": "WordPress",
    "ops": "Ops & Outils",
}


def find_workspace_variants(skills_dir: Path, skill_name: str) -> list[Path]:
    """Find -workspace and other variant dirs for a skill."""
    variants = []
    ws_dir = skills_dir / f"{skill_name}-workspace"
    if ws_dir.is_dir():
        variants.append(ws_dir)
    return variants


def plan_moves(skills_dir: Path, mapping: dict) -> list[tuple[Path, Path]]:
    """Plan all directory moves for a skills location."""
    moves = []
    for skill_name, category in sorted(mapping.items()):
        src = skills_dir / skill_name
        if not src.is_dir():
            continue
        dst = skills_dir / category / skill_name
        moves.append((src, dst))
        # Also move -workspace variants
        for variant in find_workspace_variants(skills_dir, skill_name):
            vdst = skills_dir / category / variant.name
            moves.append((variant, vdst))
    return moves


def execute_moves(moves: list[tuple[Path, Path]], dry_run: bool = True):
    """Execute or preview directory moves."""
    # Create category dirs first
    categories = {dst.parent for _, dst in moves}
    for cat_dir in sorted(categories):
        if dry_run:
            print(f"  MKDIR {cat_dir}")
        else:
            cat_dir.mkdir(parents=True, exist_ok=True)

    moved = 0
    skipped = 0
    failed_deletes = []
    for src, dst in moves:
        if not src.is_dir():
            print(f"  SKIP  {src.name} (not found)")
            skipped += 1
            continue
        if dst.is_dir() and not src.is_dir():
            print(f"  SKIP  {src.name} (already in {dst.parent.name}/)")
            skipped += 1
            continue
        if dst.is_dir() and src.is_dir():
            # Source still exists = previous copy succeeded but source wasn't deleted
            print(f"  DONE  {src.name} (already in {dst.parent.name}/, source to trash)")
            failed_deletes.append(src)
            skipped += 1
            continue
        if dry_run:
            print(f"  MOVE  {src.name}  ->  {dst.parent.name}/{dst.name}")
        else:
            try:
                os.rename(str(src), str(dst))
                print(f"  OK    {src.name}  ->  {dst.parent.name}/{dst.name}")
            except (PermissionError, OSError):
                # Windows lock: use robocopy to copy, then mark source for trash
                dst.mkdir(parents=True, exist_ok=True)
                result = subprocess.run(
                    ["robocopy", str(src), str(dst), "/E", "/NFL", "/NDL", "/NJH", "/NJS", "/NP"],
                    capture_output=True,
                )
                # robocopy exit codes: 0-7 = success (various levels)
                if result.returncode <= 7:
                    print(f"  COPY  {src.name}  ->  {dst.parent.name}/{dst.name} (robocopy, source to trash)")
                    failed_deletes.append(src)
                else:
                    print(f"  FAIL  {src.name} (robocopy error {result.returncode})")
                    skipped += 1
                    moved -= 1  # undo the count
        moved += 1

    if failed_deletes:
        print(f"\n  LOCKED sources (delete manually):")
        for p in failed_deletes:
            print(f"    {p}")

    return moved, skipped


def check_unmapped(skills_dir: Path, mapping: dict, label: str):
    """Find skill dirs not in the mapping."""
    unmapped = []
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir():
            continue
        name = d.name
        if name.startswith("_") or name.startswith("."):
            continue
        # Skip if it's a -workspace variant of a mapped skill
        base = name.removesuffix("-workspace")
        if base in mapping:
            continue
        if name in mapping:
            continue
        # Skip if it's already a category dir
        if name in CATEGORY_LABELS:
            continue
        unmapped.append(name)
    if unmapped:
        print(f"\n  UNMAPPED in {label}:")
        for u in unmapped:
            print(f"    - {u}")
    return unmapped


def generate_csv(ws_moves, pj_moves):
    """Generate CSV data for Google Sheet."""
    lines = ["Categorie\tSkill\tEmplacement\tDescription"]
    all_entries = []

    for src, dst in ws_moves:
        if not src.is_dir():
            continue
        cat = dst.parent.name
        name = src.name
        # Read description from SKILL.md
        skill_md = src / "SKILL.md"
        desc = ""
        if skill_md.is_file():
            for line in skill_md.read_text(encoding="utf-8", errors="replace").splitlines()[:15]:
                if line.lower().startswith("description:"):
                    desc = line.split(":", 1)[1].strip().strip('"').strip("'").strip(">").strip()[:200]
                    break
        all_entries.append((CATEGORY_LABELS.get(cat, cat), name, "workspace", desc))

    for src, dst in pj_moves:
        if not src.is_dir():
            continue
        cat = dst.parent.name
        name = src.name
        skill_md = src / "SKILL.md"
        desc = ""
        if skill_md.is_file():
            for line in skill_md.read_text(encoding="utf-8", errors="replace").splitlines()[:15]:
                if line.lower().startswith("description:"):
                    desc = line.split(":", 1)[1].strip().strip('"').strip("'").strip(">").strip()[:200]
                    break
        all_entries.append((CATEGORY_LABELS.get(cat, cat), name, "projet", desc))

    all_entries.sort(key=lambda x: (x[0], x[1]))
    for cat, name, loc, desc in all_entries:
        lines.append(f"{cat}\t{name}\t{loc}\t{desc}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Reorganize skills into category subdirectories")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Preview moves without executing")
    group.add_argument("--execute", action="store_true", help="Execute moves")
    group.add_argument("--csv", action="store_true", help="Output CSV for Google Sheet")
    group.add_argument("--check", action="store_true", help="Check for unmapped skills")
    args = parser.parse_args()

    if args.check:
        print("Checking for unmapped skills...")
        ws_unmapped = check_unmapped(WS_SKILLS, WS_MAP, "WORKSPACE")
        pj_unmapped = check_unmapped(PJ_SKILLS, PJ_MAP, "PROJECT")
        total = len(ws_unmapped) + len(pj_unmapped)
        print(f"\nTotal unmapped: {total}")
        return

    ws_moves = plan_moves(WS_SKILLS, WS_MAP)
    pj_moves = plan_moves(PJ_SKILLS, PJ_MAP)

    if args.csv:
        print(generate_csv(ws_moves, pj_moves))
        return

    print(f"{'DRY RUN' if args.dry_run else 'EXECUTING'}")
    print(f"\n=== WORKSPACE ({WS_SKILLS}) ===")
    ws_moved, ws_skipped = execute_moves(ws_moves, dry_run=args.dry_run)

    print(f"\n=== PROJECT ({PJ_SKILLS}) ===")
    pj_moved, pj_skipped = execute_moves(pj_moves, dry_run=args.dry_run)

    print(f"\nTotal: {ws_moved + pj_moved} moves, {ws_skipped + pj_skipped} skipped")


if __name__ == "__main__":
    main()

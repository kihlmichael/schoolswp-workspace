---
name: wp-project-triage
description: |
  Inspection déterministe d'un dépôt WordPress (plugin, thème, block theme, WP core, Gutenberg) : détection des outils (PHP, Composer, Node, @wordpress/scripts), tests présents (PHPUnit, Playwright, wp-env), indices de version et conventions, rapport JSON structuré pour guider workflows et guardrails. Sortie consommée par les autres skills WP.
  Utilise ce skill quand l'utilisateur dit : "inspecter un repo WordPress", "triage WordPress", "audit dépôt WP", "rapport JSON WordPress", "détecte le type de projet WP", ou pour comprendre la structure d'un repo WP avant intervention.
  NE PAS utiliser pour : router vers un skill domaine après triage (utiliser wordpress-router qui appelle déjà ce triage), inspection runtime ou perfs (utiliser wp-performance), audit sécurité (utiliser cso ou wordpress-pro), ou audit de contenu schoolsWP (utiliser audit-codebase ou skills SEO).
compatibility: "Targets WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI."
---

# WP Project Triage

## When to use

Use this skill to quickly understand what kind of WordPress repo you’re in and what commands/conventions to follow before making changes.

## Inputs required

- Repo root (current working directory).

## Procedure

1. Run the detector (prints JSON to stdout):
   - `node skills/wp-project-triage/scripts/detect_wp_project.mjs`
2. If you need the exact output contract, read:
   - `skills/wp-project-triage/references/triage.schema.json`
3. Use the report to select workflow guardrails:
   - project kind(s)
   - PHP/Node tooling present
   - tests present
   - version hints and sources
4. If the report is missing signals you need, update the detector rather than guessing.

## Verification

- The JSON should parse and include: `project.kind`, `signals`, and `tooling`.
- Re-run after changes that affect structure/tooling (adding `theme.json`, `block.json`, build config).

## Failure modes / debugging

- If it reports `unknown`, check whether the repo root is correct.
- If scanning is slow, add/extend ignore directories in the script.

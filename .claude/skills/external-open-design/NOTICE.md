# NOTICE — external-open-design

This directory contains 3 skills cherry-picked from
[`nexu-io/open-design`](https://github.com/nexu-io/open-design) on 2026-04-30 (Vague 2 import).

- **Upstream commit** : `9b57c22c3849bf16237e99aaf492387a86912f6b` (same as Vague 1)
- **Upstream license** : Apache License 2.0 (see `LICENSE`)
- **Companion library** : `external-design-systems/` (73 DESIGN.md files, Vague 1 import)

## What we kept

3 skills out of 31, each a directory containing `SKILL.md` + `example.html` :

- `email-marketing/` — HTML email visuel premium pour newsletter featured
- `pricing-page/` — pricing 2/3/4 tiers + comparison table + FAQ
- `docs-page/` — page documentation 3 colonnes (nav + body + TOC)

## What we did NOT keep (and why)

| Skill OD | Raison du reject |
|---|---|
| `blog-post` | Redondant avec WordPress + thème Kadence sur schoolswp.com |
| `web-prototype`, `dashboard`, `mobile-app`, `wireframe-sketch` | Couvert par aidesigner (T0) + cc-design (T1) |
| `guizang-ppt`, `replit-deck`, `simple-deck` | Décision déjà actée : decks via cc-design |
| `pm-spec`, `team-okrs`, `weekly-update`, `meeting-notes`, `kanban-board`, `eng-runbook` | Work-products internes, pas urgent |
| `motion-frames`, `sprite-animation` | Couvert par HyperFrames + Remotion |
| `dating-web`, `gamified-app`, `magazine-poster`, `digital-eguide`, `finance-report`, `invoice`, `hr-onboarding`, `mobile-onboarding`, `social-carousel`, `tweaks`, `critique` | Hors scope schoolsWP ou doublon plateforme |

## What we changed

### `SKILL.md` files (3 files)

The frontmatter `description` and `triggers` blocks were rewritten to:

1. Avoid auto-trigger on generic terms ("email", "newsletter", "pricing", "docs") which would conflict with existing schoolsWP skills.
2. Add `[SCHOOLSWP-MODIFIED — see NOTICE.md]` prefix in description.
3. Document explicit anti-conflict routing (when NOT to use this skill, what to use instead).
4. Use schoolsWP-specific French triggers ("newsletter premium", "pricing 3 tiers", "mockup doc technique").
5. Rename `name:` field with `open-design-` prefix to namespace clearly.

The body of each SKILL.md (Workflow, Self-check, Output contract) is **verbatim** from upstream.

### `example.html` files (3 files)

Verbatim from upstream. No changes.

### Added

- This `NOTICE.md`
- `INDEX.md` (routing per schoolsWP use case)

## Apache 2.0 compliance

Per Apache License 2.0 clause 4 ("Redistribution"), modifications to `SKILL.md` files are documented above. Original LICENSE preserved verbatim. No removal of attribution or copyright notices.

## Trademarks

The brand examples in `example.html` files (Filebase, SPORT TEST, etc.) are illustrative and belong to their respective owners (or are fictional products created by the upstream authors).

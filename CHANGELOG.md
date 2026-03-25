# Changelog

Toutes les modifications notables du projet schoolsWP sont documentées ici.
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

## [Unreleased]

### En cours
- Money page FluentCRM (keyword: `fluentcrm`, intent: décisionnelle, pilier: CRM)
- Cluster CRM complet (8 articles satellites)

### Backlog
- Audit pilier LMS (`pillar_authority --all`)
- Knowledge graph mise à jour
- Plan ROI éditorial Q2 2026
- YouTube intro Remotion (85s)

### Changed
- **Réduction surface apps** — 7 apps → 1 active, 4 archivées (`_archive/`), 2 prototypes lourds isolés
- **Classification apps** — README.md de classification ajouté dans `apps/`
- **Gitignore renforcé** — prototypes Remotion (brand-reveal, video-marketing) exclus

---

## [0.1.0] — 2026-03-25

### Added
- **Workspace setup complet** — skills, rules, commands, docs, settings Claude Code (2ae10a0)
- **Git governance** — CONTRIBUTING.md avec branches, commits conventionnels, workflow (323d0fd)
- **Audit workspace** — rapport structuré avec métriques, scores de maturité (data/audits/)

### Security
- **Pentest session 2** — gitignore patch files, WP hardening snippet, rapport (3a71e75)

---

## [0.0.4] — 2026-03-15

### Security
- **Audit sécurité 5 volets** — path traversal, webhook auth, STRIDE, GDPR (5c277ed → 312375d)
- **Path traversal** — protection `safe_read_path` / `safe_write_path` sur les 28 agents CLI (744cc9d, d562abf)
- **OWASP A01+A06+A08** — safe_path coverage, dependabot, pre-commit config (fd8d2dd)
- **OWASP A09** — RotatingFileHandler centralisé dans base.py (423c686)
- **F1+F2** — pip-audit clean, safe_path error handling dans 4 CLIs (0fcfb53)
- **Pentest rapport** — WordPress security snippets (afb43b7)

### Changed
- Nettoyage workflows n8n obsolètes — suppression de 8 fichiers legacy (b8ab0b5 → 211dc34)

---

## [0.0.3] — 2026-03-14

### Security
- **Gitignore fortress** — ccpa.config.json + tokens untracké (b5beaa3)

---

## [0.0.2] — 2026-02-23

### Added
- **Multi-agent system** — 4 agents IA spécialisés avec orchestration Docker (c752e31)
- Docker setup corrigé pour le système multi-agents (958f04e)

---

## [0.0.1] — 2026-02-10 → 2026-02-20

### Added
- **Import initial** du projet schoolsWP (2b8fe36)
- **Workspace setup** — VS Code, conventions, governance (ec18045)
- **Branding** — README schoolsWP, brand rules, QA checklist (b390f0e, 9e4e290)
- **Tooling** — ruff config, pre-commit hook, .gitignore patterns (b7417db, 8976c69)
- **Google Drive** — architecture, scripts de gestion, documentation audit (903ffd4, 8b16598)
- **YouTube Shorts** — workflows d'automatisation n8n (4ddd1df)
- **Brand-reveal** — animation TypeScript Remotion (41c0ca2)
- **Remotion** — vidéo marketing 7 scènes, 2:50 (b326699)
- **Scripts marketing** — vidéo YouTube intro (8f13472)
- **SEO audit** — automatisation mensuelle (e992afe)

#!/usr/bin/env python3
"""
CLI — Module Auto-Audit SEO schoolsWP

Score un article sur 100 points (5 × 20) :
  SEO Structure | Intention | Pédagogie | Valeur Business | Branding schoolsWP

Usage :
  # Audit simple
  python -m agents.seo_auditor.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle

  # Audit + correction automatique si score < 90
  python -m agents.seo_auditor.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --fix \\
    --save-dir content/articles/lms-pilier/

  # Texte direct (sans fichier)
  python -m agents.seo_auditor.cli \\
    --text "# Mon article..." \\
    --keyword "lms wordpress" \\
    --fix --threshold 85

Interprétation des scores :
  95–100  ✅  Publication immédiate
  85–94   🟡  Ajustements mineurs
  70–84   🟠  Optimisation nécessaire
  < 70    🔴  Réécriture stratégique
"""
import argparse
import asyncio
import io
import sys
import time
from pathlib import Path

# Force UTF-8 sur Windows
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path
from agents.seo_auditor.agent import AuditResult, SeoAuditorAgent

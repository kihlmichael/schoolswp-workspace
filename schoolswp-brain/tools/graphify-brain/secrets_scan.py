"""Defense-in-depth scan: refuse to send a file set that looks like it contains secrets."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

PATTERNS: list[tuple[str, re.Pattern]] = [
    ("pem-private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("google-api-key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("openai-key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("slack-token", re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}")),
    ("github-pat", re.compile(r"ghp_[0-9A-Za-z]{36}")),
    ("assigned-secret", re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9/\+_\-]{16,}")),
]


@dataclass
class SecretHit:
    path: str
    line: int
    pattern: str


def scan_files(paths: list[Path]) -> list[SecretHit]:
    hits: list[SecretHit] = []
    for p in paths:
        try:
            lines = Path(p).read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, start=1):
            for name, rx in PATTERNS:
                if rx.search(line):
                    hits.append(SecretHit(path=str(p), line=i, pattern=name))
    return hits

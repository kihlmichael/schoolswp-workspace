"""Heuristic token + USD estimate for a set of files about to reach Gemini.

Pricing is approximate input-token pricing; update PRICE_PER_MTOK_USD as needed.
The real cost is captured later (phase 2); this is a guardrail estimate only.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

CHARS_PER_TOKEN = 4
PRICE_PER_MTOK_USD = {
    "gemini-2.5-flash": 0.30,  # approx input price; adjust to billing reality
    "gemini-2.5-pro": 1.25,
}
DEFAULT_PRICE = 0.30


@dataclass
class CostEstimate:
    files: int
    total_chars: int
    est_tokens: int
    est_usd: float


def estimate(paths: list[Path], model: str) -> CostEstimate:
    total_chars = 0
    n = 0
    for p in paths:
        try:
            total_chars += len(Path(p).read_text(encoding="utf-8", errors="replace"))
            n += 1
        except OSError:
            continue
    est_tokens = total_chars // CHARS_PER_TOKEN
    price = PRICE_PER_MTOK_USD.get(model, DEFAULT_PRICE)
    est_usd = round(est_tokens / 1_000_000 * price, 4)
    return CostEstimate(files=n, total_chars=total_chars, est_tokens=est_tokens, est_usd=est_usd)

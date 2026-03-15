"""Base class for all schoolsWP content agents."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import anthropic
from dotenv import load_dotenv

# Auto-load .env — search order: agents/.env → .env → multi-agent-system/.env
for _env_candidate in [
    Path(__file__).parent.parent / "agents" / ".env",
    Path(__file__).parent.parent / ".env",
    Path(__file__).parent.parent / "multi-agent-system" / ".env",
]:
    if _env_candidate.exists():
        load_dotenv(_env_candidate)
        break

_CWD = Path.cwd().resolve()
_DEFAULT_MODEL = os.environ.get("MODEL_WRITER", "claude-sonnet-4-6")


def safe_read_path(path: str | Path) -> Path:
    """Resolve and validate a read path — must stay within CWD."""
    resolved = Path(path).resolve()
    if not str(resolved).startswith(str(_CWD)):
        raise ValueError(f"Path traversal detected: {path!r} resolves outside CWD ({_CWD})")
    return resolved


def safe_write_path(path: str | Path) -> Path:
    """Resolve and validate a write path — must stay within CWD."""
    resolved = Path(path).resolve()
    if not str(resolved).startswith(str(_CWD)):
        raise ValueError(f"Path traversal detected: {path!r} resolves outside CWD ({_CWD})")
    return resolved


class BaseContentAgent:
    """Base class for all schoolsWP content agents.

    Provides:
    - Anthropic client initialization with auto-loaded API key
    - Default model resolution (MODEL_WRITER env var → claude-sonnet-4-6)
    - Async run() interface returning markdown str
    """

    name: str = "base-agent"
    system_prompt: str = "Tu es un assistant schoolsWP."

    def __init__(self, model: Optional[str] = None) -> None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. Add it to agents/.env or .env"
            )
        self._client = anthropic.AsyncAnthropic(api_key=api_key)
        self.model = model or _DEFAULT_MODEL

    async def run(self, **kwargs) -> str:
        """Override in subclasses. Must return a markdown string."""
        raise NotImplementedError

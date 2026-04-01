# agents/ — namespace redirect to core/agents-py/
# This allows `python -m agents.content_factory.cli` from project root.
from pathlib import Path

__path__ = [str(Path(__file__).resolve().parent.parent / "core" / "agents-py")]

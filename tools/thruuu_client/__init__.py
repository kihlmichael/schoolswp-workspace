"""thruuu API client - client Python reutilisable pour l'API SERP thruuu.

Utilise par :
- tools/mcp-servers/thruuu/server.py (serveur MCP)
- core/agents-py/* (futurs agents qui veulent appeler thruuu en backend)
- tools/thruuu-client/cli.py (test manuel)

Source API : https://thruuu.com/learn/serp-api/
"""

from .client import (
    SerpRequest,
    ThruuuClient,
    ThruuuError,
    ThruuuTimeout,
)

__all__ = [
    "SerpRequest",
    "ThruuuClient",
    "ThruuuError",
    "ThruuuTimeout",
]

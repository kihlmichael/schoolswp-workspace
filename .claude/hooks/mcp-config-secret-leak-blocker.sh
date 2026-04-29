#!/bin/bash
# Wrapper bash : delegue au hook Python pour scanner .mcp.json avant Edit/Write.
# Voir mcp-config-secret-leak-blocker.py pour la logique.

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python "$DIR/mcp-config-secret-leak-blocker.py"

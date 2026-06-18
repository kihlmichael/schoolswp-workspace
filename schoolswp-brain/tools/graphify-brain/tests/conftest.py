import sys
from pathlib import Path

# Make the graphify-brain package modules importable as top-level modules in tests.
PKG_DIR = Path(__file__).resolve().parent.parent
if str(PKG_DIR) not in sys.path:
    sys.path.insert(0, str(PKG_DIR))

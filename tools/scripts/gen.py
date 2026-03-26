import os, textwrap
target = os.path.join("d:", os.sep, "VS Code", "CLAUDE CODE", "gsc_analysis.py")
with open(target, "w", encoding="utf-8") as f:
    f.write("""#!/usr/bin/env python3
import csv, os
from datetime import datetime, timedelta
from collections import defaultdict
""")
print("done")

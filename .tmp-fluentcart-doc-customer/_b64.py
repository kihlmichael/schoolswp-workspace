"""Emit base64 of each consolidated .md file for upload."""
import base64
import sys
from pathlib import Path

OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-customer')

# Files in upload order
order = [
    "00-INDEX-doc-customer.md",
    "01-getting-started.md",
    "02-product-types-creation.md",
    "03-store-management.md",
    "04-payments-checkout.md",
    "05-shipping.md",
    "06-tax-duties.md",
    "07-customer-dashboard.md",
    "08-marketing-sales-tools.md",
    "09-settings-configuration.md",
    "10-customization-themes.md",
    "11-integrations.md",
    "12-migration-edd.md",
    "13-reporting-analytics.md",
    "14-storage.md",
    "15-troubleshooting-support.md",
    "16-changelog-misc.md",
]

target = sys.argv[1] if len(sys.argv) > 1 else None
for f in order:
    p = OUT_DIR / f
    if not p.exists():
        continue
    if target and f != target:
        continue
    data = p.read_bytes()
    b64 = base64.b64encode(data).decode('ascii')
    print(f"=== FILE: {f} | size_bytes={len(data)} | b64_len={len(b64)} ===")
    print(b64)
    print("=== END ===")

"""Upload .md files to Google Drive using gws-cli refresh token.

Refreshes a Google OAuth access_token via oauth2.googleapis.com/token,
then performs Drive multipart uploads (metadata + binary) into a target parent.
"""
import json
import mimetypes
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PARENT_ID = "1kRnfMRmMEVWBXPVb3Jq_tO_y6EX2HaOU"
OUT_DIR = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-doc-customer')

# Map md filename stem -> Drive title
TITLE_MAP = {
    "00-INDEX-doc-customer": "00 - INDEX Doc Customer",
    "01-getting-started": "01 - Getting Started",
    "02-product-types-creation": "02 - Product Types Creation",
    "03-store-management": "03 - Store Management",
    "04-payments-checkout": "04 - Payments Checkout",
    "05-shipping": "05 - Shipping",
    "06-tax-duties": "06 - Tax Duties",
    "07-customer-dashboard": "07 - Customer Dashboard",
    "08-marketing-sales-tools": "08 - Marketing Sales Tools",
    "09-settings-configuration": "09 - Settings Configuration",
    "10-customization-themes": "10 - Customization Themes",
    "11-integrations": "11 - Integrations",
    "12-migration-edd": "12 - Migration EDD",
    "13-reporting-analytics": "13 - Reporting Analytics",
    "14-storage": "14 - Storage",
    "15-troubleshooting-support": "15 - Troubleshooting Support",
    "16-changelog-misc": "16 - Changelog Misc",
}

# Already uploaded (skip) — IDs noted in the final report
ALREADY_UPLOADED = {
    "00-INDEX-doc-customer",      # id=1CcMCWL4Z00qXeYqI5OJ3n4yW4l4fylfa
    "01-getting-started",          # id=18tBx5QiggCaw9X1P8cv669hSZ4QUc_Ac
    "05-shipping",                 # id=1rshRsrWH6dSvlycHjGzn6FH0SBZeQJHY
    "06-tax-duties",               # id=110J7K3RgfGQH8rZP-CpTkylRFbYZqrlp
    "07-customer-dashboard",       # id=1iJUc01QdUi6lr-VEaSsKans38qJPjeHd
    "08-marketing-sales-tools",    # id=1t196_wD7HCaRAxgKhD2P6PS37bqhSNGh
    "14-storage",                  # id=1X8soS9Wa7Qcxbjlbt2doMbfRea0VlkIl
    "15-troubleshooting-support",  # id=1aOMCDuKEh1AY81VEZSQE4vxu69qY6uHN
}
# REMAINING to upload (9 files):
#   02-product-types-creation.md  (153 KB)
#   03-store-management.md        (74 KB)
#   04-payments-checkout.md       (74 KB)
#   09-settings-configuration.md  (98 KB)
#   10-customization-themes.md    (131 KB)
#   11-integrations.md            (78 KB)
#   12-migration-edd.md           (73 KB)
#   13-reporting-analytics.md     (58 KB)
#   16-changelog-misc.md          (57 KB)
# Note: All Google OAuth tokens stored locally are expired/revoked.
# To resume the uploader, run `gws auth login` interactively first, then re-run this script.


def get_creds():
    """Load refresh_token + client creds from tools/scripts/token-gdrive-migration.json."""
    tok_path = Path(r'D:\VS Code\CLAUDE CODE\projects\schoolswp\tools\scripts\token-gdrive-migration.json')
    with open(tok_path) as f:
        return json.load(f)


def refresh_token(creds):
    """Get fresh access_token via oauth2.googleapis.com/token."""
    data = urllib.parse.urlencode({
        'client_id': creds['client_id'],
        'client_secret': creds['client_secret'],
        'refresh_token': creds['refresh_token'],
        'grant_type': 'refresh_token',
    }).encode()
    req = urllib.request.Request(
        'https://oauth2.googleapis.com/token',
        data=data,
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        j = json.loads(resp.read())
    return j['access_token']


def upload_file(access_token, file_path: Path, title: str, parent_id: str) -> str:
    """Multipart upload to Drive. Returns file_id."""
    metadata = {
        "name": title,
        "parents": [parent_id],
        "mimeType": "text/markdown",
    }
    boundary = "boundary_fluentcart_upload_2026"
    content = file_path.read_bytes()

    body = (
        f"--{boundary}\r\n"
        f"Content-Type: application/json; charset=UTF-8\r\n\r\n"
        f"{json.dumps(metadata)}\r\n"
        f"--{boundary}\r\n"
        f"Content-Type: text/markdown\r\n\r\n"
    ).encode('utf-8') + content + f"\r\n--{boundary}--\r\n".encode('utf-8')

    url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name,mimeType"
    req = urllib.request.Request(
        url,
        data=body,
        method='POST',
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': f'multipart/related; boundary={boundary}',
        }
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        j = json.loads(resp.read())
    return j['id']


def main():
    creds = get_creds()
    print(f"Got creds for client_id={creds['client_id'][:20]}...")
    access_token = refresh_token(creds)
    print(f"Got access_token: {access_token[:20]}... (len={len(access_token)})")

    results = []
    md_files = sorted(OUT_DIR.glob('*.md'))
    for f in md_files:
        stem = f.stem
        if stem in ALREADY_UPLOADED:
            print(f"SKIP {f.name} (already uploaded)")
            continue
        title = TITLE_MAP.get(stem, stem)
        try:
            fid = upload_file(access_token, f, title, PARENT_ID)
            print(f"OK   {f.name:50s} -> id={fid}  title={title!r}")
            results.append((f.name, fid, title))
        except Exception as e:
            print(f"FAIL {f.name}: {e}")
            results.append((f.name, None, str(e)))

    print("\n=== Summary ===")
    for name, fid, info in results:
        print(f"  {name:55s} {fid or 'FAILED':<35s} {info}")


if __name__ == '__main__':
    main()

import subprocess
import json
import sys

GWS_CLI = ["node", "C:\\Users\\conta\\AppData\\Roaming\\npm\\node_modules\\@googleworkspace\\cli\\run.js"]
SPREADSHEET_ID = "1FjZgbUdSBVqTuFL2kdHKFKXcO4ZNWehINwfvWpD-vTs"

def run_gws(args):
    cmd = GWS_CLI + args
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"Error executing gws: {res.stderr}")
        return None
    lines = res.stdout.strip().split("\n")
    json_lines = []
    for l in lines:
        if l.startswith("{") or l.startswith("[") or json_lines:
            json_lines.append(l)
    try:
        return json.loads("\n".join(json_lines))
    except Exception as e:
        print("Failed to parse JSON output:", e)
        print("Raw stdout:", res.stdout)
        return None

def write_gws_batch(range_name, values):
    body = {"values": values}
    params = {
        "spreadsheetId": SPREADSHEET_ID,
        "range": range_name,
        "valueInputOption": "USER_ENTERED"
    }
    cmd = GWS_CLI + [
        "sheets", "spreadsheets", "values", "update",
        "--params", json.dumps(params),
        "--json", json.dumps(body)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"Error updating values for range {range_name}: {res.stderr}")
        return False
    return True

print("Fetching current sources values...")
res = run_gws(["sheets", "+read", "--spreadsheet", SPREADSHEET_ID, "--range", "sources!A1:Z250"])
if not res or "values" not in res:
    print("Could not fetch sources sheet!")
    sys.exit(1)

rows = res["values"]
headers = rows[0]
print(f"Found {len(rows)} rows. Current headers: {headers}")

# Check if new columns are present, if not add them
new_cols = ["dernier_status", "dernier_excerpt", "erreur_derniere_execution", "nb_erreurs_consecutives"]
headers_changed = False
for col in new_cols:
    if col not in headers:
        headers.append(col)
        headers_changed = True

# Pad all existing rows to match new header length
for r in rows:
    while len(r) < len(headers):
        r.append("")

# Find index of columns
id_idx = headers.index("id")
actif_idx = headers.index("actif")

target_actives = {"fluent-forms-pricing", "fluentcrm-pricing", "ottokit-pricing"}

# Update actif to 'yes' or 'no'
active_count = 0
inactive_count = 0
for idx, row in enumerate(rows[1:], start=1):
    row_id = row[id_idx] if id_idx < len(row) else ""
    if row_id in target_actives:
        row[actif_idx] = "yes"
        active_count += 1
    else:
        row[actif_idx] = "no"
        inactive_count += 1

print(f"Updating rows: {active_count} active sources, {inactive_count} inactive sources.")

# Batch update rows in chunks of 30 to avoid WinError 206 (command length limit)
chunk_size = 30
total_rows = len(rows)

# Update headers first
headers_range = f"sources!A1:{chr(65 + len(headers) - 1)}1"
if not write_gws_batch(headers_range, [headers]):
    print("Failed to update headers!")
    sys.exit(1)
print("Headers updated successfully.")

# Update the rest in chunks
for i in range(1, total_rows, chunk_size):
    chunk = rows[i:i+chunk_size]
    start_row = i + 1
    end_row = start_row + len(chunk) - 1
    range_name = f"sources!A{start_row}:{chr(65 + len(headers) - 1)}{end_row}"
    print(f"Updating chunk {start_row} to {end_row}...")
    if not write_gws_batch(range_name, chunk):
        print(f"Failed to update chunk {start_row} to {end_row}!")
        sys.exit(1)

print("Google Sheet sources tab successfully prepared in chunks!")

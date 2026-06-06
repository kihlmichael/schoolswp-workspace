"""Update brief v0.3 -> v0.4 on Drive (content + rename) via gws."""
import json
import subprocess

GWS = r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"
MD = r"d:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-brief-v04.md"
FILE_ID = "1o8Dh3rGk9xS_czk-SJ_jPrO3J9DVBTde"
NEW_NAME = "00 - Brief stratégique formation FluentCart v0.4 (pricing arbitré).md"


def run_gws(args):
    p = subprocess.run([GWS] + args, capture_output=True, text=True, encoding="utf-8", shell=False)
    if p.returncode != 0:
        print("EXIT", p.returncode, "STDERR:", p.stderr.strip())
        return None
    out = p.stdout
    i = out.find("{")
    return json.loads(out[i:]) if i != -1 else {}


res = run_gws([
    "drive", "files", "update",
    "--params", json.dumps({"fileId": FILE_ID}),
    "--json", json.dumps({"name": NEW_NAME}),
    "--upload", MD,
    "--upload-content-type", "text/markdown",
])
if res:
    print("UPDATED", res.get("id"), "|", res.get("name"))

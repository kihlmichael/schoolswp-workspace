"""One-shot: update existing Drive .md (lead magnet) with corrected spelling via gws."""
import json
import subprocess

GWS = r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"
MD = r"d:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-leadmagnet-drive.md"
FILE_ID = "1HwUkvh0aPgGj8SU37H7ViFuYkhXYXpz6"


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
    "--upload", MD,
    "--upload-content-type", "text/markdown",
])
if res:
    print("MD_UPDATED", res.get("id"), "|", res.get("name"))

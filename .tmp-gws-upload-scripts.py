"""Upload LAUNCH video scripts to Drive (04 - Scripts video) via gws."""
import json
import subprocess

GWS = r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"
MD = r"d:\VS Code\CLAUDE CODE\projects\schoolswp\content\formations\fluentcart\scripts-launch.md"
PARENT = "1EmqCMwNAS_-qTc9YgSAovjlWnF89Mcyj"  # 04 - Scripts video


def run_gws(args):
    p = subprocess.run([GWS] + args, capture_output=True, text=True, encoding="utf-8", shell=False)
    if p.returncode != 0:
        print("EXIT", p.returncode, "STDERR:", p.stderr.strip())
        return None
    out = p.stdout
    i = out.find("{")
    return json.loads(out[i:]) if i != -1 else {}


meta = {
    "name": "LAUNCH - Scripts video 6 lecons (draft v1).md",
    "parents": [PARENT],
    "mimeType": "text/markdown",
}
res = run_gws([
    "drive", "files", "create",
    "--upload", MD,
    "--upload-content-type", "text/markdown",
    "--json", json.dumps(meta),
])
if res:
    print("SCRIPTS_ID", res.get("id"), "|", res.get("name"))

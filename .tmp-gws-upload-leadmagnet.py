"""One-shot: upload corrected lead magnet PDF to Drive via gws (proven args-list path)."""
import json
import subprocess

GWS = r"C:\Users\conta\AppData\Roaming\npm\gws.cmd"
PDF = r"d:\VS Code\CLAUDE CODE\projects\schoolswp\.tmp-fluentcart-leadmagnet.pdf"
PARENT = "104P9AWvNdovfRYoKDM6-w39ectSKWvoE"  # 03 - Plan de formation


def run_gws(args):
    p = subprocess.run([GWS] + args, capture_output=True, text=True, encoding="utf-8", shell=False)
    if p.returncode != 0:
        print("EXIT", p.returncode, "STDERR:", p.stderr.strip())
        return None
    out = p.stdout
    i = out.find("{")
    return json.loads(out[i:]) if i != -1 else {}


meta = {
    "name": "Lead magnet - Checklist FluentCart Setup en 1 demi-journee (v1).pdf",
    "parents": [PARENT],
    "mimeType": "application/pdf",
}
res = run_gws([
    "drive", "files", "create",
    "--upload", PDF,
    "--upload-content-type", "application/pdf",
    "--json", json.dumps(meta),
])
if res:
    print("PDF_ID", res.get("id"), "|", res.get("name"))

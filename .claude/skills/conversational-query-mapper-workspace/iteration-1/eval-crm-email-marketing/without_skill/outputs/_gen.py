import os

outdir = r"d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/skills/conversational-query-mapper-workspace/iteration-1/eval-crm-email-marketing/without_skill/outputs"
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "result.md")

print("Writing to", outpath)
with open(outpath, "w", encoding="utf-8") as f:
    f.write("test content")
print("Done")

import os

project_dir = r"D:\VS Code\CLAUDE CODE\projects\schoolswp"

# Search for any python files mentioning google, drive, or sheets
for root, dirs, files in os.walk(project_dir):
    if ".venv" in root or "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "google" in content.lower() or "drive" in content.lower() or "sheet" in content.lower():
                    print(f"Match found in: {path}")
            except Exception as e:
                pass

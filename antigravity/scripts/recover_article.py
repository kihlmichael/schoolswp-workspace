import os
import json

transcript_path = r"C:\Users\conta\.gemini\antigravity\brain\da237c9e-3c34-4c74-9a5e-bcf40c14d1fd\.system_generated\logs\transcript.jsonl"
drafts_dir = r"d:\ANTIGRAVITY\drafts"

if not os.path.exists(transcript_path):
    print("Transcript not found")
    exit(1)

intro = ""
part1 = ""
part2 = ""

with open(transcript_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            content = data.get("content", "")
            if not content:
                continue
                
            # Search for specific markers of output
            if "INTRODUCTION GÉNÉRÉE" in content or "INTRODUCTION GÉNÉRÉE (V2)" in content:
                if len(content) > len(intro) and "def generate" not in content:
                    intro = content
            elif "PREMIÈRE PARTIE GÉNÉRÉE" in content:
                if len(content) > len(part1) and "def generate" not in content:
                    part1 = content
            elif "DEUXIÈME PARTIE GÉNÉRÉE" in content:
                if len(content) > len(part2) and "def generate" not in content:
                    part2 = content
        except Exception as e:
            continue

# If not found by exact string, let's search by keywords in the text
if not intro or not part1 or not part2:
    with open(transcript_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            try:
                data = json.loads(line)
                content = data.get("content", "")
                if not content:
                    continue
                if "def generate" in content:
                    continue
                
                # Check for intro
                if "SaaS fatigue" in content and "Pourquoi stocker ses leads" in content:
                    if len(content) > len(intro):
                        intro = content
                # Check for Part 1
                if "Le suivi client" in content and "Imagine que tu cherches un email" in content:
                    if len(content) > len(part1):
                        part1 = content
                # Check for Part 2
                if "La cage dorée" in content and "Plus ta liste de contacts" in content:
                    if len(content) > len(part2):
                        part2 = content
            except Exception as e:
                continue

# Write to files
with open(os.path.join(drafts_dir, "recovered_intro.txt"), "w", encoding="utf-8") as f:
    f.write(intro)
with open(os.path.join(drafts_dir, "recovered_part1.txt"), "w", encoding="utf-8") as f:
    f.write(part1)
with open(os.path.join(drafts_dir, "recovered_part2.txt"), "w", encoding="utf-8") as f:
    f.write(part2)

print("Recovered files written successfully!")

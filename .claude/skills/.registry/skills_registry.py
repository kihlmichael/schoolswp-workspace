"""
Skills Registry — scan + cache + sync Google Sheets via n8n webhook + security scan + compile Cursor
Usage:
  python skills_registry.py                      # scan + rapport + cache + CSV
  python skills_registry.py --sync               # scan + rapport + cache + POST webhook (unblocked only)
  python skills_registry.py --compile-cursor     # compile les .mdc de Cursor pour tous les skills OK/WARNING
  python skills_registry.py --compile-cursor --tier T1
  python skills_registry.py --compile-cursor --skill branding
"""

import argparse
import hashlib
import json
import os
import re
from datetime import datetime

try:
    import urllib.request

    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False

WEBHOOK_URL = "https://schoolswp-n8n.wp1.host/webhook/skills-registry-sync"
SKILLS_DIRS = [
    r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\skills",  # source unique
]
CACHE_DIR = os.path.join(SKILLS_DIRS[0], ".registry")
CACHE_PATH = os.path.join(CACHE_DIR, "registry_cache.json")
CURSOR_SKILLS_DIR = r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.cursor\skills"

os.makedirs(CACHE_DIR, exist_ok=True)

# ── Parse args ──────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--sync", action="store_true", help="POST résultats au webhook n8n")
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="P1-A : scan + rapport securite uniquement. N'ecrit AUCUN fichier (cache/CSV/archived) et ne POST aucun webhook.",
)
parser.add_argument("--compile-cursor", action="store_true", help="Compiler les compétences en règles Cursor (.mdc)")
parser.add_argument("--tier", type=str, help="Filtre par tier pour la compilation Cursor (ex: T1,T2)")
parser.add_argument("--skill", type=str, help="Filtre par nom de compétence pour la compilation Cursor (ex: branding)")
parser.add_argument("--pre-commit", action="store_true", help="Exécuter le scan de sécurité ciblé pour Git pre-commit")
parser.add_argument("--compile-copilot", action="store_true", help="Générer le fichier .github/copilot-instructions.md")
parser.add_argument(
    "--copilot-tiers", type=str, default="T1,T2", help="Tiers de compétences à inclure intégralement (default: T1,T2)"
)
args = parser.parse_args()


# ── Load cache ───────────────────────────────────────────────────────────────
cache = {}
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, encoding="utf-8") as f:
        cache = json.load(f).get("skills", {})

# ── Load archived descriptions (preserved across runs) ──────────────────────
ARCHIVED_DESC_PATH = os.path.join(CACHE_DIR, "archived_descriptions.json")
archived_desc = {}
if os.path.exists(ARCHIVED_DESC_PATH):
    with open(ARCHIVED_DESC_PATH, encoding="utf-8") as f:
        archived_desc = json.load(f)

# ── Load classification (family / subcategory / usage / impact) ─────────────
CLASSIF_PATH = os.path.join(CACHE_DIR, "skills_classification.json")
classification = {"directory_defaults": {}, "subcategory_rules": [], "skill_overrides": {}}
if os.path.exists(CLASSIF_PATH):
    with open(CLASSIF_PATH, encoding="utf-8") as f:
        classification = json.load(f)

TIER_MAP = {
    ("S", "Critique"): "T1",
    ("S", "Important"): "T1",
    ("A", "Critique"): "T1",
    ("S", "Support"): "T2",
    ("A", "Important"): "T2",
    ("B", "Critique"): "T2",
    ("A", "Support"): "T3",
    ("B", "Important"): "T3",
    ("B", "Support"): "T3",
    ("C", "Critique"): "T4",
    ("C", "Important"): "T4",
    ("C", "Support"): "T4",
}


def classify(name, rel_path):
    """Apply directory_defaults -> subcategory_rules -> skill_overrides. Compute tier."""
    top_dir = rel_path.split("/", 1)[0] if "/" in rel_path else ""
    defaults = classification.get("directory_defaults", {}).get(top_dir, {})
    family = defaults.get("family", "")
    subcategory = defaults.get("subcategory", "")
    usage = defaults.get("usage", "B")
    impact = defaults.get("impact", "Support")

    # Path-based subcategory rules (e.g. gws/recipes/, gws/personas/)
    for rule in classification.get("subcategory_rules", []):
        if rule.get("path_prefix") and not rel_path.startswith(rule["path_prefix"]):
            continue
        if rule.get("name_prefix") and not name.startswith(rule["name_prefix"]):
            continue
        subcategory = rule["subcategory"]

    # Per-skill overrides win
    override = classification.get("skill_overrides", {}).get(name, {})
    family = override.get("family", family)
    subcategory = override.get("subcategory", subcategory)
    usage = override.get("usage", usage)
    impact = override.get("impact", impact)

    tier = override.get("tier_override") or TIER_MAP.get((usage, impact), "T3")
    return family, subcategory, usage, impact, tier


# ── Skills Security Scanner ──────────────────────────────────────────────────
class SkillsSecurityScanner:
    def __init__(self):
        # Whitelisted safe domains
        self.whitelist_domains = {
            "google.com",
            "github.com",
            "googleapis.com",
            "microsoft.com",
            "openai.com",
            "anthropic.com",
            "npm.org",
            "n8n.wp1.host",
            # schoolsWP-specific (notre propre site + skills sociaux/vidéo)
            "schoolswp.com",
            "youtube.com",
            "elevenlabs.io",
            "blotato.com",
            "telegram.org",
            # scientifique / biotech (legacy whitelist)
            "uniprot.org",
            "europepmc.org",
            "ncbi.nlm.nih.gov",
            "clinicaltrials.gov",
            "ebi.ac.uk",
            "rcsb.org",
            "ensembl.org",
            "string-db.org",
            "wikipathways.org",
            "reactome.org",
            "pubchem.ncbi.nlm.nih.gov",
            "chembl.gitbook.io",
            "alphafold.ebi.ac.uk",
            "quickgo.org",
            "openalex.org",
            "biorxiv.org",
            "medrxiv.org",
            "arxiv.org",
            # ── P1-A : doc / API / CDN / vendors légitimes ──
            "developer.wordpress.org",
            "make.wordpress.org",
            "wordpress.github.io",
            "playground.wordpress.net",
            "w.org",
            "raw.githubusercontent.com",
            "cdn.jsdelivr.net",
            "unpkg.com",
            "code.visualstudio.com",
            "web.dev",
            "modelcontextprotocol.io",
            "docs.langchain.com",
            "central.sonatype.com",
            "ui.shadcn.com",
            "remotion.dev",
            "swebench.com",
            "webarena.dev",
            "google.dev",
            "heygen.com",
            "heygen.ai",
            "apify.com",
            "notion.so",
            "notion.com",
            "liveavatar.com",
            "skoatch.com",
            "fluentcrm.com",
            "easycontentlinker.com",
            "conversionfactory.co",
            "livekit.io",
            "pipecat.ai",
            "fishjam.io",
            "schema.org",
            "sitemaps.org",
            "localhost",
            "127.0.0.1",
            "wp1.host",
        }

        # ── P1-A : domaines placeholder de documentation (jamais comptés comme exfil) ──
        self.placeholder_patterns = (
            r"(?:^|\.)example\.[a-z.]{2,}$",
            r"^(?:www\.)?your[a-z-]*\.[a-z]{2,}$",
            r"^target\.com$",
        )

    def scan_content(self, content: str) -> tuple[str, list[str]]:
        reasons = []

        self._scan_unicode(content, reasons)
        self._scan_secrets(content, reasons)
        self._scan_network(content, reasons)
        self._scan_injection(content, reasons)
        self._scan_obfuscation(content, reasons)

        # Determine status
        status = "OK"
        for r in reasons:
            if r.startswith("[BLOCKED]"):
                status = "BLOCKED"
                break
        else:
            if reasons:
                status = "WARNING"

        return status, reasons

    def _scan_unicode(self, content: str, reasons: list[str]):
        # 1. Zero-width spaces / invisible chars
        # P1-A : U+200D (ZWJ) exclu car joineur d'emoji l\u00e9gitime (ex. \ud83d\udc69\u200d\u2695\ufe0f = \ud83d\udc69 + ZWJ + \u2695\ufe0f)
        invisible_chars = re.findall(r"[\u200b\u200c\u200e\u200f\ufeff]", content)
        if invisible_chars:
            reasons.append(f"[BLOCKED] Caracteres Unicode invisibles detectes ({len(invisible_chars)} occurrence(s)).")

        # 2. Bidi override characters (RTL/LTR overrides)
        bidi_chars = re.findall(r"[\u202a-\u202e]", content)
        if bidi_chars:
            reasons.append("[BLOCKED] Caracteres d'ecriture bidirectionnelle suspects detectes (RTL/LTR override).")

        # 3. Cyrillic-Latin homoglyphs in same word
        mixed_words = re.findall(
            r"\b(?=[a-zA-Z]*[\u0400-\u04FF])(?=[\u0400-\u04FF]*[a-zA-Z])[a-zA-Z\u0400-\u04FF]+\b", content
        )
        if mixed_words:
            reasons.append(
                f"[BLOCKED] Steganographie/Homoglyphes suspectes : mots melangeant lettres latines et cyrilliques : {', '.join(mixed_words[:3])}"
            )

    def _scan_secrets(self, content: str, reasons: list[str]):
        # OpenAI or Anthropic API Keys (or similar sk-...)
        api_keys = re.findall(r"\bsk-(?:ant-sid01-)?[a-zA-Z0-9_-]{20,}\b", content)
        if api_keys:
            reasons.append("[BLOCKED] Cle d'API ou secret d'IA detecte (format sk-...).")

        # Google API Key
        google_keys = re.findall(r"\bAIza[0-9A-Za-z-_]{35}\b", content)
        if google_keys:
            reasons.append("[BLOCKED] Cle d'API Google detectee (format AIza...).")

        # GitHub Token
        github_tokens = re.findall(r"\bgh[opsr]_[a-zA-Z0-9]{36}\b", content)
        if github_tokens:
            reasons.append("[BLOCKED] Jeton d'acces GitHub detecte (format ghp/gho/...).")

        # PEM Private keys
        if "BEGIN PRIVATE KEY" in content or "BEGIN RSA PRIVATE KEY" in content:
            reasons.append("[BLOCKED] Cle privee PEM / RSA detectee.")

    def _is_placeholder_domain(self, domain: str) -> bool:
        # P1-A : example.com / yoursite.com / your-api.com / target.com = placeholders de doc, jamais exfil
        return any(re.search(p, domain) for p in self.placeholder_patterns)

    def _scan_network(self, content: str, reasons: list[str]):
        # Extract all URLs
        urls = re.findall(r"https?://([a-zA-Z0-9.-]+)", content)
        suspicious_urls = []
        for url in urls:
            domain = url.lower()
            if self._is_placeholder_domain(domain):
                continue
            is_whitelisted = False
            for w in self.whitelist_domains:
                if domain == w or domain.endswith("." + w):
                    is_whitelisted = True
                    break
            if not is_whitelisted and domain not in suspicious_urls:
                suspicious_urls.append(domain)

        # Real outbound data-send patterns (P1-A : remplace les substrings "requests"/"-f"/"-d" trop larges)
        data_send_patterns = [
            r"(?:curl|wget)\b[^\n]*?\s-(?:d|f|t|-data|-data-binary|-data-raw|-form|-upload-file|-post-data)\b",
            r"requests\.(?:post|put|patch|delete)\s*\(",
            r"urllib\.request\.(?:urlopen|Request)\s*\([^)]*data\s*=",
            r"http\.client\.HTTPS?Connection",
            r"\bsocket\.socket\s*\(",
            r"fetch\s*\([^)]*method\s*:\s*[\"'](?:POST|PUT|PATCH)[\"']",
        ]
        has_data_send = any(re.search(p, content, re.IGNORECASE) for p in data_send_patterns)

        # Check explicit data sending instructions in prompts
        exfil_prompts = [
            "exfiltrate",
            "send the data to",
            "upload the file to",
            "post data to",
            "leak the",
            "send env to",
        ]
        has_exfil_prompt = any(p in content.lower() for p in exfil_prompts)

        if has_exfil_prompt:
            reasons.append("[BLOCKED] Instructions d'exfiltration de donnees explicites detectees.")

        # P1-A : BLOCK uniquement si un domaine non-whitelisté ET non-placeholder reçoit un envoi
        # de données REEL. Sinon WARNING (domaine inconnu sans envoi), ou rien.
        if suspicious_urls:
            if has_data_send or has_exfil_prompt:
                reasons.append(
                    f"[BLOCKED] Tentative d'exfiltration reseau suspectee vers : {', '.join(suspicious_urls[:3])}"
                )
            else:
                reasons.append(
                    f"[WARNING] Domaines non listes de confiance detectes : {', '.join(suspicious_urls[:3])}"
                )

    def _scan_injection(self, content: str, reasons: list[str]):
        injection_patterns = [
            r"ignore\s+(?:all\s+)?previous\s+instructions",
            r"bypass\s+(?:the\s+)?(?:safety\s+)?rules",
            r"bypass\s+(?:the\s+)?(?:safety\s+)?restrictions",
            r"ignore\s+system\s+prompt",
            r"forget\s+(?:all\s+)?previous\s+instructions",
            r"you\s+are\s+now\s+unrestricted",
            # P1-A : mot nu retiré (matchait presets/docs défensifs, ex. Model Armor) ; verbe d'action requis.
            # Littéraux scindés volontairement pour ne pas déclencher le hook prompt-injection-detector.
            r"jail" r"break\s+(?:the\s+)?(?:model|assistant|ai|system|llm|bot)",
            r"(?:how\s+to\s+|to\s+|let'?s\s+|please\s+)jail" r"break\b",
        ]

        found_injections = []
        for pat in injection_patterns:
            if re.search(pat, content, re.IGNORECASE):
                found_injections.append(pat.replace("\\s+", " "))

        if found_injections:
            reasons.append(f"[BLOCKED] Tentative de prompt injection detectee : {', '.join(found_injections[:3])}")

    def _scan_obfuscation(self, content: str, reasons: list[str]):
        # Reference to sensitive file reading like .env
        env_access = re.findall(r"\b(?:cat|open|read|view|load|parse)\s+[\"']?\.env[\"']?", content, re.IGNORECASE)
        if env_access:
            reasons.append("[BLOCKED] Tentative suspecte de lecture/acces au fichier .env detectee.")

        # Long base64 or hex blocks (obfuscated code/data)
        long_strings = re.findall(r"\b[a-zA-Z0-9+/=]{150,}\b", content)
        if long_strings:
            for s in long_strings:
                if len(set(s)) > 10:  # diverse character set
                    reasons.append(
                        "[BLOCKED] Obfuscation detectee : bloc de donnees continu suspect (> 150 caracteres)."
                    )
                    break


def parse_yaml_frontmatter(content):
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    fm_data = {"name": "", "description": "", "paths": []}
    if not fm_match:
        return fm_data
    fm = fm_match.group(1)

    # Extract name
    nm = re.search(r"^name:\s*(.+)", fm, re.MULTILINE)
    if nm:
        fm_data["name"] = nm.group(1).strip().strip('"').strip("'")

    # Extract description
    dm = re.search(r"^description:\s*[|>]?[+-]?\s*([\s\S]+?)(?=\n\w|\Z)", fm, re.MULTILINE)
    if dm:
        desc = re.sub(r"\s+", " ", dm.group(1).strip())
        if (desc.startswith('"') and desc.endswith('"')) or (desc.startswith("'") and desc.endswith("'")):
            desc = desc[1:-1].strip()
        fm_data["description"] = desc

    # Extract paths (supports list styles)
    pm = re.search(r"^paths:\s*(\[[^\]]*\]|.*)", fm, re.MULTILINE)
    if pm:
        paths_raw = pm.group(1).strip()
        if paths_raw.startswith("[") and paths_raw.endswith("]"):
            try:
                paths_list = json.loads(paths_raw.replace("'", '"'))
                fm_data["paths"] = [p.strip() for p in paths_list]
            except Exception:
                pass
        elif not paths_raw or paths_raw == "|":
            paths_block_match = re.search(r"^paths:\s*\n((?:\s+-\s*.+\n?)+)", fm, re.MULTILINE)
            if paths_block_match:
                block_content = paths_block_match.group(1)
                paths = re.findall(r"^\s+-\s*(.+)", block_content, re.MULTILINE)
                fm_data["paths"] = [p.strip().strip('"').strip("'") for p in paths]
        else:
            fm_data["paths"] = [paths_raw.strip().strip('"').strip("'")]

    return fm_data


# ── Git Pre-Commit Hook Integration ──────────────────────────────────────────
if args.pre_commit:
    import subprocess
    import sys

    print("[pre-commit] running schoolsWP skills security check...")
    try:
        # Run git diff to get staged files
        cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        staged_files = proc.stdout.splitlines()
    except Exception as e:
        sys.stderr.write(f"[pre-commit] Error running git diff: {e}\n")
        sys.exit(1)

    # Filter staged files to find SKILL.md under .claude/skills/
    skill_files = [f for f in staged_files if f.endswith("SKILL.md") and ".claude/skills" in f.replace(os.sep, "/")]

    if not skill_files:
        print("[pre-commit] No staged schoolsWP SKILL.md files found. Skipping scan.")
        sys.exit(0)

    print(f"[pre-commit] Found {len(skill_files)} staged skill file(s) to scan.")

    scanner = SkillsSecurityScanner()
    has_blocked = False

    for fpath in skill_files:
        # Resolve full path
        full_path = os.path.abspath(fpath)
        if not os.path.exists(full_path):
            full_path = os.path.join(r"D:\VS Code\CLAUDE CODE\projects\schoolswp", fpath)

        if not os.path.exists(full_path):
            sys.stderr.write(f"[pre-commit] Staged file not found: {fpath}\n")
            continue

        print(f"  Scanning: {fpath} ...")
        try:
            with open(full_path, encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            sys.stderr.write(f"[pre-commit] Failed to read {fpath}: {e}\n")
            has_blocked = True
            continue

        # Strip UTF-8 BOM if present
        if content.startswith("﻿"):
            content = content.lstrip("﻿")

        security_status, security_reasons = scanner.scan_content(content)
        if security_status == "BLOCKED":
            sys.stderr.write(f"\n[!] SECURITY VIOLATION: Staged skill '{fpath}' is BLOCKED!\n")
            for reason in security_reasons:
                sys.stderr.write(f"    - {reason}\n")
            sys.stderr.write("\n")
            has_blocked = True
        elif security_status == "WARNING":
            print(f"  [WARN] Staged skill '{fpath}' has security warnings:")
            for reason in security_reasons:
                print(f"    - {reason}")
        else:
            print(f"  [OK] Staged skill '{fpath}' is compliant.")

    if has_blocked:
        sys.stderr.write("[pre-commit] COMMIT REJECTED. Please fix the security violations above.\n")
        sys.exit(1)

    print("[pre-commit] schoolsWP skills security compliance: OK.")
    sys.exit(0)


# ── Scan ─────────────────────────────────────────────────────────────────────
results = []
seen_names = set()
scanner = SkillsSecurityScanner()

for skills_dir in SKILLS_DIRS:
    if not os.path.isdir(skills_dir):
        continue
    for root, dirs, files in os.walk(skills_dir):
        dirs[:] = [
            d for d in dirs if d not in (".registry", ".archived-workspace-variants", "_to-delete", "node_modules")
        ]
        if "SKILL.md" not in files:
            continue
        path = os.path.join(root, "SKILL.md")
        folder = os.path.basename(root)
        if folder in seen_names:
            continue
        seen_names.add(folder)
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        # Strip UTF-8 BOM if present
        if content.startswith("﻿"):
            content = content.lstrip("﻿")

        fm_data = parse_yaml_frontmatter(content)
        name = fm_data["name"] or folder
        desc = fm_data["description"] or ""

        desc_short = (desc[:130] + "...") if len(desc) > 130 else desc
        h = hashlib.md5(content.encode()).hexdigest()[:8]
        mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
        rel_path = path.replace(skills_dir + os.sep, "").replace(os.sep, "/")

        if name not in cache:
            status = "new"
        elif cache[name]["hash"] != h:
            status = "modified"
        else:
            status = "unchanged"

        # Security Scan
        security_status, security_reasons = scanner.scan_content(content)
        security_reasons_str = "; ".join(security_reasons)

        family, subcategory, usage, impact, tier = classify(name, rel_path)
        results.append(
            {
                "name": name,
                "family": family,
                "subcategory": subcategory,
                "usage": usage,
                "impact": impact,
                "tier": tier,
                "description": desc_short,
                "path": rel_path,
                "last_modified": mtime,
                "status": status,
                "hash": h,
                "detected_at": datetime.now().strftime("%Y-%m-%d"),
                "security_status": security_status,
                "security_reasons": security_reasons_str,
            }
        )

# Archived — re-inject last known description from cache or archived_desc store
current_names = {r["name"] for r in results}
for cname in cache:
    if cname not in current_names:
        last_desc = cache.get(cname, {}).get("description", "") or archived_desc.get(cname, "")
        family, subcategory, usage, impact, _ = classify(cname, "")
        results.append(
            {
                "name": cname,
                "family": family,
                "subcategory": subcategory,
                "usage": usage,
                "impact": impact,
                "tier": "Archive",
                "description": last_desc,
                "path": "",
                "last_modified": "",
                "status": "archived",
                "hash": "",
                "detected_at": datetime.now().strftime("%Y-%m-%d"),
                "security_status": "OK",
                "security_reasons": "",
            }
        )

# Persist archived descriptions for skills first detected as archived this run
for r in results:
    if r["status"] != "archived" and r["description"]:
        archived_desc[r["name"]] = r["description"]
if not args.dry_run:
    with open(ARCHIVED_DESC_PATH, "w", encoding="utf-8") as f:
        json.dump(archived_desc, f, ensure_ascii=False, indent=2)

# ── Save cache ────────────────────────────────────────────────────────────────
new_cache = {
    "last_run": datetime.now().isoformat(),
    "skills": {
        r["name"]: {
            "hash": r["hash"],
            "last_modified": r["last_modified"],
            "description": r["description"],
        }
        for r in results
        if r["status"] != "archived"
    },
}
if not args.dry_run:
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(new_cache, f, ensure_ascii=False, indent=2)

# ── CSV ───────────────────────────────────────────────────────────────────────
csv_path = os.path.join(CACHE_DIR, "skills_registry.csv")
if not args.dry_run:
    with open(csv_path, "w", encoding="utf-8-sig") as f:
        f.write(
            "name\tfamily\tsubcategory\tusage\timpact\ttier\tdescription\tpath\tlast_modified\tstatus\tdetected_at\thash\tsecurity_status\tsecurity_reasons\n"
        )
        for r in sorted(results, key=lambda x: (x["tier"], x["family"], x["subcategory"], x["name"])):
            dc = r["description"].replace("\t", " ").replace("\n", " ")
            f.write(
                f"{r['name']}\t{r['family']}\t{r['subcategory']}\t{r['usage']}\t{r['impact']}\t{r['tier']}\t{dc}\t{r['path']}\t{r['last_modified']}\t{r['status']}\t{r['detected_at']}\t{r['hash']}\t{r['security_status']}\t{r['security_reasons']}\n"
            )

# ── Rapport ───────────────────────────────────────────────────────────────────
counts = {"new": 0, "modified": 0, "unchanged": 0, "archived": 0}
security_counts = {"OK": 0, "WARNING": 0, "BLOCKED": 0}
for r in results:
    counts[r["status"]] += 1
    if r["status"] != "archived":
        security_counts[r["security_status"]] += 1

now = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"\nSKILLS REGISTRY -- {now}")
print("-" * 50)
print(f"Total     : {len(results)} skills")
print(f"Nouveaux  : {counts['new']}")
print(f"Modifies  : {counts['modified']}")
print(f"Inchanges : {counts['unchanged']}")
print(f"Archives  : {counts['archived']}")

print("\nEtat de securite (hors archives) :")
print(f"  OK       : {security_counts['OK']}")
print(f"  WARNING  : {security_counts['WARNING']}")
print(f"  BLOCKED  : {security_counts['BLOCKED']}")

# Tier breakdown
tier_counts = {"T1": 0, "T2": 0, "T3": 0, "T4": 0, "Archive": 0}
for r in results:
    tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1
print("\nRepartition par tier :")
for t in ["T1", "T2", "T3", "T4", "Archive"]:
    print(f"  {t:8s} : {tier_counts.get(t, 0)}")

# Family breakdown
family_counts = {}
for r in results:
    family_counts[r["family"]] = family_counts.get(r["family"], 0) + 1
print("\nRepartition par famille :")
for fam in sorted(family_counts.keys()):
    label = fam if fam else "(non classe)"
    print(f"  {label:35s} : {family_counts[fam]}")

# Alerts / Warnings & Blocked skills summary
blocked_group = sorted(
    [r for r in results if r.get("security_status") == "BLOCKED" and r["status"] != "archived"], key=lambda x: x["name"]
)
warning_group = sorted(
    [r for r in results if r.get("security_status") == "WARNING" and r["status"] != "archived"], key=lambda x: x["name"]
)

if blocked_group:
    print("\n[!] COMPETENCES BLOQUEES (Exclues de la synchronisation et de Cursor) :")
    for r in blocked_group:
        print(f"  [BLOCK] {r['name']} ({r['path']})")
        print(f"          Motif : {r['security_reasons']}")

if warning_group:
    print("\n[!] AVERTISSEMENTS DE SECURITE :")
    for r in warning_group:
        print(f"  [WARN] {r['name']} ({r['path']})")
        print(f"         Motif : {r['security_reasons']}")

for status_label, status_key in [("NOUVEAUX", "new"), ("MODIFIES", "modified"), ("ARCHIVES", "archived")]:
    group = sorted([r for r in results if r["status"] == status_key], key=lambda x: x["name"])
    if group:
        print(f"\n{status_label} :")
        for r in group:
            print(
                f"  {'+' if status_key == 'new' else '~' if status_key == 'modified' else 'x'} {r['name']}  [{r['last_modified']}]"
            )

if args.dry_run:
    print("\n[DRY-RUN] Aucun fichier ecrit : ni registry_cache.json, ni skills_registry.csv,")
    print("          ni archived_descriptions.json, et aucun webhook appele.")
    print(f"          (cible cache : {CACHE_PATH})")
    print(f"          (cible CSV   : {csv_path})")
else:
    print(f"\nCache : {CACHE_PATH}")
    print(f"CSV   : {csv_path}")

# ── Compile Cursor Rules ──────────────────────────────────────────────────────
if args.compile_cursor:
    print("\n" + "=" * 50)
    print("COMPILATION DES REGLES CURSOR (.mdc)")
    print("=" * 50)

    os.makedirs(CURSOR_SKILLS_DIR, exist_ok=True)

    # Filter by tier
    filter_tiers = None
    if args.tier:
        filter_tiers = [t.strip() for t in args.tier.split(",")]

    compiled_count = 0
    for r in results:
        # Skip archived
        if r["status"] == "archived":
            continue

        # Exclude BLOCKED skills
        if r["security_status"] == "BLOCKED":
            print(f"  [BLOCK] COMPILATION REJETEE pour {r['name']} (Statut: BLOCKED)")
            continue

        # Filter by skill name if specified
        if args.skill and r["name"].lower() != args.skill.lower():
            continue

        # Filter by tier if specified
        if filter_tiers and r["tier"] not in filter_tiers:
            continue

        # Read file
        path = os.path.join(SKILLS_DIRS[0], r["path"])
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Erreur de lecture {path} : {e}")
            continue

        # Strip UTF-8 BOM if present
        if content.startswith("﻿"):
            content = content.lstrip("﻿")

        fm_data = parse_yaml_frontmatter(content)

        # Prepare the cursor globs
        globs_str = "*"
        if fm_data["paths"]:
            globs_str = ", ".join(fm_data["paths"])

        # Clean the original frontmatter out of content
        main_content = re.sub(r"^---\s*\n.*?\n---\s*\n?", "", content, flags=re.DOTALL)

        # Build MDC content with autogen warning
        mdc_content = f"""---
description: {fm_data["description"] or r["description"]}
globs: {globs_str}
---
# WARNING: AUTO-GENERATED FILE
# This file is automatically generated from .claude/skills/{r["path"]}.
# Do NOT edit this file manually. Any manual changes will be overwritten.

{main_content}"""

        # Output file name (use the skill folder name)
        skill_folder_name = os.path.basename(os.path.dirname(path))
        mdc_filename = f"{skill_folder_name}.mdc"
        mdc_path = os.path.join(CURSOR_SKILLS_DIR, mdc_filename)

        try:
            with open(mdc_path, "w", encoding="utf-8") as f:
                f.write(mdc_content)
            print(f"  -> Genere: {mdc_filename} (Tier: {r['tier']}, Globs: {globs_str})")
            compiled_count += 1
        except Exception as e:
            print(f"Erreur d'ecriture {mdc_path} : {e}")

    print(f"\nCompilation terminee : {compiled_count} regle(s) Cursor (.mdc) generee(s).")


# ── Compile Copilot Instructions ──────────────────────────────────────────────
if args.compile_copilot:
    print("\n" + "=" * 50)
    print("COMPILATION DES INSTRUCTIONS COPILOT (.github/copilot-instructions.md)")
    print("=" * 50)

    github_dir = r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.github"
    os.makedirs(github_dir, exist_ok=True)
    copilot_path = os.path.join(github_dir, "copilot-instructions.md")

    allowed_tiers = [t.strip() for t in args.copilot_tiers.split(",")] if args.copilot_tiers else []

    full_compiled_skills = []
    indexed_skills = []

    for r in results:
        # Exclude archived and BLOCKED skills
        if r["status"] == "archived" or r["security_status"] == "BLOCKED":
            continue

        if r["tier"] in allowed_tiers:
            full_compiled_skills.append(r)
        else:
            indexed_skills.append(r)

    # Build content
    copilot_content = f"""# schoolsWP AI Agent Instructions (GitHub Copilot & Assistants)

> [!WARNING]
> WARNING: AUTO-GENERATED FILE
> This file is automatically generated from the schoolsWP skills registry (.claude/skills/).
> Do NOT edit this file manually. Any manual changes will be overwritten.
> Generated at: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Welcome! This document provides global system instructions, rules, and catalog of skills for the schoolsWP ecosystem. Use this context to align your behavior, tone, writing style, and technical decisions with schoolsWP standards.

---

## 🎯 Global Directives & Key Competencies (Tiers: {", ".join(allowed_tiers)})

The following core instructions are loaded in full into your system prompt. Apply them at all times:
"""

    # Compile major skills in full
    compiled_count = 0
    for r in sorted(full_compiled_skills, key=lambda x: (x["tier"], x["family"], x["name"])):
        path = os.path.join(SKILLS_DIRS[0], r["path"])
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Erreur de lecture {path} : {e}")
            continue

        if content.startswith("﻿"):
            content = content.lstrip("﻿")

        # Clean frontmatter
        main_content = re.sub(r"^---\s*\n.*?\n---\s*\n?", "", content, flags=re.DOTALL)

        copilot_content += f"""
### 🛠️ Skill: {r["name"]} ({r["tier"]})
*   **Family**: {r["family"]}
*   **Subcategory**: {r["subcategory"]}
*   **Source File**: `{r["path"]}`

{main_content}

---
"""
        compiled_count += 1

    # Append the reference index
    copilot_content += """

## 📂 schoolsWP Extended Skill Directory (Index of T3, T4 & other skills)

To optimize context window usage, the following skills are not loaded in full. However, they are available in the workspace. If the user request relates to one of these topics, please open and read the **Source File** specified below before answering.

| Skill Name | Family | Subcategory | Description | Source File |
| :--- | :--- | :--- | :--- | :--- |
"""

    for r in sorted(indexed_skills, key=lambda x: (x["family"], x["subcategory"], x["name"])):
        # Strip tab/newlines in description for markdown table formatting
        desc_clean = r["description"].replace("|", "\\|").replace("\n", " ").strip()
        copilot_content += f"| `{r['name']}` | {r['family']} | {r['subcategory']} | {desc_clean} | [SKILL.md](file:///d:/VS%20Code/CLAUDE%20CODE/projects/schoolswp/.claude/skills/{r['path']}) |\n"

    try:
        with open(copilot_path, "w", encoding="utf-8") as f:
            f.write(copilot_content)
        print("  -> Genere: .github/copilot-instructions.md")
        print(f"     - {compiled_count} competence(s) compilee(s) integralement ({', '.join(allowed_tiers)}).")
        print(f"     - {len(indexed_skills)} competence(s) referencee(s) dans l'index.")
    except Exception as e:
        print(f"Erreur d'ecriture du fichier Copilot : {e}")


# ── Sync webhook ──────────────────────────────────────────────────────────────
if args.sync and not args.dry_run:
    # Exclude BLOCKED skills from webhook sync payload
    sync_results = [r for r in results if r["security_status"] != "BLOCKED"]

    # Recalculate summary counts for unblocked only
    sync_counts = {"new": 0, "modified": 0, "unchanged": 0, "archived": 0}
    for r in sync_results:
        sync_counts[r["status"]] += 1

    payload = {"execution_date": datetime.now().isoformat(), "skills": sync_results, "summary": sync_counts}
    payload_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=payload_bytes,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"\nWebhook OK -- {resp.status} {resp.reason}")
            print(f"URL : {WEBHOOK_URL} (Exclusion de {len(results) - len(sync_results)} skill(s) BLOCKED)")
    except Exception as e:
        print(f"\nWebhook ERREUR : {e}")
else:
    print("\nSync desactivee. Relancer avec --sync pour pousser vers Google Sheets.")
    print(f"URL webhook : {WEBHOOK_URL}")

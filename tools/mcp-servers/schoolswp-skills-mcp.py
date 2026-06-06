import sys
import json
import os

# Set encoding to UTF-8 for stdin/stdout to prevent encoding errors on Windows
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"D:\VS Code\CLAUDE CODE\projects\schoolswp"

def log(msg):
    sys.stderr.write(f"[schoolswp-skills-mcp] {msg}\n")
    sys.stderr.flush()

# Read CSV registry
def load_registry():
    csv_path = os.path.join(BASE_DIR, ".claude", "skills", ".registry", "skills_registry.csv")
    skills = []
    if not os.path.exists(csv_path):
        log(f"Registry CSV not found at {csv_path}")
        return skills
    try:
        with open(csv_path, encoding="utf-8-sig") as f:
            lines = f.readlines()
            if not lines:
                return skills
            headers = lines[0].strip().split("\t")
            for line in lines[1:]:
                parts = line.strip("\n").split("\t")
                if len(parts) < len(headers):
                    continue
                skill = dict(zip(headers, parts))
                # Skip BLOCKED and archived skills
                if skill.get("security_status") == "BLOCKED" or skill.get("status") == "archived":
                    continue
                skills.append(skill)
    except Exception as e:
        log(f"Error loading registry: {e}")
    return skills

def load_skill_content(rel_path):
    path = os.path.join(BASE_DIR, ".claude", "skills", rel_path)
    if not os.path.exists(path):
        log(f"Skill file not found at {path}")
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        log(f"Error reading skill content {rel_path}: {e}")
        return None

def handle_initialize(params):
    return {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "tools": {}
        },
        "serverInfo": {
            "name": "schoolswp-skills",
            "version": "1.0.0"
        }
    }

def handle_tools_list():
    return {
        "tools": [
            {
                "name": "list_all_skills",
                "description": "Retourne la liste de toutes les competences indexees (OK ou WARNING) dans le registre schoolsWP.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "search_skills",
                "description": "Recherche des competences schoolsWP par mot-cle dans leur nom, description ou famille.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Le mot-cle ou pattern de recherche."
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_skill_details",
                "description": "Recupere le contenu complet (instructions SKILL.md) d'une competence specifique par son nom.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Le nom exact de la competence (ex: branding)."
                        }
                    },
                    "required": ["name"]
                }
            }
        ]
    }

def handle_tools_call(name, arguments):
    skills = load_registry()
    if name == "list_all_skills":
        result_skills = []
        for s in skills:
            result_skills.append({
                "name": s["name"],
                "family": s["family"],
                "subcategory": s["subcategory"],
                "tier": s["tier"],
                "description": s["description"],
                "path": s["path"]
            })
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(result_skills, ensure_ascii=False, indent=2)
                }
            ],
            "isError": False
        }
        
    elif name == "search_skills":
        query = arguments.get("query", "").lower()
        matched = []
        for s in skills:
            if (query in s["name"].lower() or 
                query in s["description"].lower() or 
                query in s["family"].lower() or 
                query in s["subcategory"].lower()):
                matched.append({
                    "name": s["name"],
                    "family": s["family"],
                    "subcategory": s["subcategory"],
                    "tier": s["tier"],
                    "description": s["description"],
                    "path": s["path"]
                })
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(matched, ensure_ascii=False, indent=2)
                }
            ],
            "isError": False
        }
        
    elif name == "get_skill_details":
        sname = arguments.get("name", "").strip()
        target_skill = None
        for s in skills:
            if s["name"].lower() == sname.lower():
                target_skill = s
                break
        if not target_skill:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Competence introuvable ou bloquee par la securite : '{sname}'."
                    }
                ],
                "isError": True
            }
        
        content = load_skill_content(target_skill["path"])
        if content is None:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Impossible de charger le fichier de competence a l'emplacement specifie."
                    }
                ],
                "isError": True
            }
            
        return {
            "content": [
                {
                    "type": "text",
                    "text": content
                }
            ],
            "isError": False
        }
        
    else:
        return {
            "content": [
                {
                    "type": "text",
                    "text": f"Outil inconnu : {name}"
                }
            ],
            "isError": True
        }

def main():
    log("Server starting...")
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue
            
            request = json.loads(line)
            req_id = request.get("id")
            method = request.get("method")
            params = request.get("params", {})
            
            # Notifications do not have an ID (e.g. initialized)
            if req_id is None:
                log(f"Received notification: {method}")
                continue
                
            response = {
                "jsonrpc": "2.0",
                "id": req_id
            }
            
            if method == "initialize":
                response["result"] = handle_initialize(params)
            elif method == "tools/list":
                response["result"] = handle_tools_list()
            elif method == "tools/call":
                name = params.get("name")
                arguments = params.get("arguments", {})
                response["result"] = handle_tools_call(name, arguments)
            else:
                response["error"] = {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
                
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()
            
        except Exception as e:
            log(f"Main loop error: {e}")

if __name__ == "__main__":
    main()

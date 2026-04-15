import subprocess
import json
import time

def run_gws(args):
    cmd = ["gws"] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Skip keyring messages if they exist
        output = result.stdout
        # find the start of json
        start_idx = output.find('{')
        if start_idx != -1:
            output = output[start_idx:]
        return json.loads(output)
    except subprocess.CalledProcessError as e:
        print(f"Error running gws: {e.cmd}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        raise

def create_folder(name, parent_id=None):
    payload = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder"
    }
    if parent_id:
        payload["parents"] = [parent_id]
    
    print(f"Creating folder: {name} under {parent_id or 'root'}...")
    # Using python's json.dumps to handle escaping correctly
    json_str = json.dumps(payload)
    args = ["drive", "files", "create", "--json", json_str, "--params", '{"fields": "id,name"}']
    res = run_gws(args)
    time.sleep(1) # Be nice to the API
    return res['id']

def main():
    print("Starting creation of schoolsWP_Ressources architecture...")
    
    # 1. Create Root
    root_id = create_folder("schoolsWP_Ressources")
    print(f"Root ID: {root_id}")

    # 2. Create Level 1
    staging_id = create_folder("00_STAGING", root_id)
    public_id = create_folder("01_PUBLIC_FREEBIES", root_id)
    premium_id = create_folder("02_PREMIUM_MEMBRES", root_id)
    archives_id = create_folder("99_ARCHIVES", root_id)

    # 3. Create Level 2 - Public
    create_folder("01_SEO", public_id)
    create_folder("02_AUTOMATISATION", public_id)
    create_folder("03_WORDPRESS", public_id)
    create_folder("04_FORMATION", public_id)
    create_folder("05_BUSINESS_FREELANCE", public_id)

    # 4. Create Level 2 - Premium
    create_folder("01_FORMATIONS", premium_id)
    create_folder("02_BONUS_CLIENTS", premium_id)
    create_folder("03_TEMPLATES_RESERVES", premium_id)
    create_folder("04_RESSOURCES_PRIVILEGES", premium_id)

    # 5. Create Level 2 - Archives
    create_folder("2026", archives_id)
    create_folder("2027", archives_id)

    print("DONE! Architecture successfully created.")

if __name__ == "__main__":
    main()

import os
import sys
import requests
from requests.auth import HTTPBasicAuth

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def main():
    # Configure stdout to support UTF-8 if available, or just ignore errors
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    print("=== WordPress REST API Page Publisher ===")
    
    # Credentials read from the environment (never hardcode secrets).
    # Set WP_JOACHIM_USERNAME and WP_JOACHIM_APP_PASSWORD in .env (gitignored).
    username = os.environ.get("WP_JOACHIM_USERNAME")
    app_password = os.environ.get("WP_JOACHIM_APP_PASSWORD")
    if not username or not app_password:
        print("Error: set WP_JOACHIM_USERNAME and WP_JOACHIM_APP_PASSWORD in your environment (.env).")
        sys.exit(1)
    api_url = "https://joachimkihl.fr/wp-json/wp/v2/pages"
    
    # Read the Gutenberg blocks file
    blocks_file_path = os.path.join("landing-pages", "club-skoda-grand-est-blocks.txt")
    if not os.path.exists(blocks_file_path):
        print(f"Error: Gutenberg blocks file not found at {blocks_file_path}")
        sys.exit(1)
        
    with open(blocks_file_path, "r", encoding="utf-8") as f:
        blocks_content = f.read()
        
    print(f"Successfully read {len(blocks_content)} characters of block markup.")
    
    # Page data
    payload = {
        "title": "Sortie Club Skoda - Epinal - 4 Juillet 2026",
        "content": blocks_content,
        "status": "draft",
        "slug": "sortie-skoda-grand-est-epinal",
        "template": "", # Default template
    }
    
    # We update the existing page with ID 91
    update_api_url = f"{api_url}/91"
    print(f"Updating page ID 91 on joachimkihl.fr...")
    
    try:
        response = requests.post(
            update_api_url,
            json=payload,
            auth=HTTPBasicAuth(username, app_password),
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code in (200, 201):
            page_data = response.json()
            print("\n[SUCCESS] The page has been updated successfully.")
            print(f"Title: {page_data.get('title', {}).get('rendered')}")
            print(f"Slug: {page_data.get('slug')}")
            print(f"ID: {page_data.get('id')}")
            print(f"Link to view: {page_data.get('link')}")
            print(f"Link to edit: https://joachimkihl.fr/wp-admin/post.php?post={page_data.get('id')}&action=edit")
        else:
            print(f"\n[ERROR] Failed to update page. Status Code: {response.status_code}")
            print("Response text:")
            print(response.text)
            sys.exit(1)
            
    except Exception as e:
        print(f"\n[ERROR] Error during REST API request: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

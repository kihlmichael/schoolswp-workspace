import requests


def upload_media_to_blotato(file_path, api_key):
    """
    Uploads a local video file to Blotato's media library.
    Returns the media_id.
    """
    print(f"[INFO] Upload de la vidéo '{file_path}' vers Blotato...")
    url = "https://backend.blotato.com/v2/media"
    headers = {"Authorization": f"Bearer {api_key}"}

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code not in (200, 201):
        raise requests.HTTPError(f"Blotato Upload Error {response.status_code}: {response.text}")

    data = response.json()
    media_id = data.get("id")
    print(f"[SUCCESS] Vidéo importée sur Blotato. Media ID: {media_id}")
    return media_id


def create_youtube_post_blotato(media_id, title, description, privacy_status, account_id, api_key):
    """
    Creates a YouTube post on Blotato using the uploaded media_id.
    """
    print(
        f"[INFO] Planification de la publication YouTube sur Blotato (Compte: {account_id}, Status: {privacy_status})..."
    )
    url = "https://backend.blotato.com/v2/posts"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {
        "platform": "youtube",
        "accountId": account_id,
        "mediaId": media_id,
        "postContentText": description,
        "youtubeOptions": {"title": title, "privacyStatus": privacy_status, "shouldNotifySubscribers": False},
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code not in (200, 201):
        raise requests.HTTPError(f"Blotato Post Error {response.status_code}: {response.text}")

    data = response.json()
    post_id = data.get("id")
    print(f"[SUCCESS] Vidéo postée avec succès sur YouTube via Blotato. Post ID: {post_id}")
    return post_id


def run_blotato_publishing(file_path, title, description, privacy_status, account_id, api_key):
    """
    Combines upload and posting steps to publish the video on Blotato.
    """
    # En cas de simulation ou de clé de test manquante, on peut mocker
    if api_key == "__A_REMPLIR_CLAY_API_BLOTATO__" or not api_key:
        print("[WARNING] Mode Simulation Blotato activé (Clé d'API non renseignée).")
        return {"media_id": "blotato_media_mock_123", "post_id": "blotato_post_mock_456"}

    media_id = upload_media_to_blotato(file_path, api_key)
    post_id = create_youtube_post_blotato(media_id, title, description, privacy_status, account_id, api_key)
    return {"media_id": media_id, "post_id": post_id}

# --- CONFIGURATION ---
# ID du dossier parent (déjà configuré avec votre ID)
$ParentFolderId = "1D10mjPHE_PEab5ajRUq7spoY4gleTSEY"
# --- FIN CONFIGURATION ---

# Fonction pour afficher les messages avec des couleurs
function Write-HostColored {
    param(
        [string]$Message,
        [string]$Color
    )
    Write-Host $Message -ForegroundColor $Color
}

# 1. Vérifier que gcloud est accessible
if (-not (Get-Command gcloud -ErrorAction SilentlyContinue)) {
    Write-HostColored "Erreur : La commande 'gcloud' est introuvable." -Color Red
    Write-HostColored "Veuillez vous assurer que le Google Cloud SDK est installé et dans votre PATH." -Color Yellow
    exit 1
}

# 2. Récupérer le jeton d'authentification de manière sécurisée
Write-Host "Récupération du token d'accès via gcloud..."
try {
    $accessToken = gcloud auth print-access-token
} catch {
    Write-HostColored "Impossible de récupérer le token d'accès. Avez-vous exécuté 'gcloud auth login --enable-gdrive-access' ?" -Color Red
    exit 1
}

$headers = @{
    "Authorization" = "Bearer $accessToken"
    "Content-Type"  = "application/json"
}

# 3. Obtenir la couleur du dossier parent
$parentUrl = "https://www.googleapis.com/drive/v3/files/$ParentFolderId`?fields=folderColorRgb,name"
try {
    $parentInfo = Invoke-RestMethod -Uri $parentUrl -Method Get -Headers $headers
} catch {
    Write-HostColored "Erreur lors de la récupération des informations du dossier parent. Vérifiez l'ID." -Color Red
    exit 1
}

$parentColor = $parentInfo.folderColorRgb
$parentName = $parentInfo.name

if (-not $parentColor) {
    Write-HostColored "Le dossier racine '$parentName' n'a pas de couleur définie. Veuillez lui en assigner une sur Google Drive." -Color Red
    exit 1
}

Write-HostColored "Couleur cible identifiée : '$parentColor' (provenant du dossier '$parentName')" -Color Green

# 4. Fonction récursive pour synchroniser les couleurs
function Sync-FolderColor {
    param(
        [string]$CurrentFolderId,
        [string]$TargetColor
    )

    $pageToken = $null
    do {
        $query = "'$CurrentFolderId' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        # Encodage de la query pour l'URL
        $encodedQuery = [System.Web.HttpUtility]::UrlEncode($query)
        $listUrl = "https:/`/www.googleapis.com/drive/v3/files``?q=$encodedQuery&fields=nextPageToken,files(id,name,folderColorRgb)&pageSize=100"

        if ($pageToken) {
            $listUrl += "&pageToken=$pageToken"
        }

        $response = Invoke-RestMethod -Uri $listUrl -Method Get -Headers $headers

        if (-not $response.files) { return }

        foreach ($folder in $response.files) {
            if ($folder.folderColorRgb -ne $TargetColor) {
                Write-Host "Mise à jour : $($folder.name)"
                $updateUrl = "https://www.googleapis.com/drive/v3/files/$($folder.id)"
                $body = @{ folderColorRgb = $TargetColor } | ConvertTo-Json
                
                try {
                    Invoke-RestMethod -Uri $updateUrl -Method Patch -Headers $headers -Body $body | Out-Null
                } catch {
                    Write-HostColored "Erreur lors de la mise à jour de '$($folder.name)'." -Color Red
                }
            } else {
                 Write-Host "Déjà à jour : $($folder.name)" -ForegroundColor Gray
            }

            # Appel récursif pour les sous-dossiers
            Sync-FolderColor -CurrentFolderId $folder.id -TargetColor $TargetColor
        }

        $pageToken = $response.nextPageToken
    } while ($pageToken)
}

# 5. Lancement du processus
Write-Host "Démarrage de la synchronisation des couleurs..."
Sync-FolderColor -CurrentFolderId $ParentFolderId -TargetColor $parentColor
Write-HostColored "Synchronisation terminée !" -Color Green

# PowerShell Audit Script for D:\TÉLÉCHARGEMENT
$Path = "D:\TÉLÉCHARGEMENT"

# Get all files and folders recursively (excluding hidden/system if possible, but let's do simple)
$allEntries = Get-ChildItem -Path $Path -Recurse -Force -ErrorAction SilentlyContinue

$files = $allEntries | Where-Object { !$_.PSIsContainer }
$dirs = $allEntries | Where-Object { $_.PSIsContainer }

$totalFiles = $files.Count
$totalDirs = $dirs.Count
$totalSize = ($files | Measure-Object -Property Length -Sum).Sum

# Extensions
$extGroups = $files | Group-Object Extension | Sort-Object Count -Descending | Select-Object -First 20 | ForEach-Object {
    [PSCustomObject]@{
        Extension = $_.Name
        Count = $_.Count
        Size = ($_.Group | Measure-Object -Property Length -Sum).Sum
    }
}

# Largest files
$largestFiles = $files | Sort-Object Length -Descending | Select-Object -First 10 | ForEach-Object {
    [PSCustomObject]@{
        Name = $_.Name
        Path = $_.FullName
        Size = $_.Length
        LastWriteTime = $_.LastWriteTime
    }
}

# Oldest files
$oldestFiles = $files | Sort-Object LastWriteTime | Select-Object -First 10 | ForEach-Object {
    [PSCustomObject]@{
        Name = $_.Name
        Path = $_.FullName
        Size = $_.Length
        LastWriteTime = $_.LastWriteTime
    }
}

# Newest files
$newestFiles = $files | Sort-Object LastWriteTime -Descending | Select-Object -First 10 | ForEach-Object {
    [PSCustomObject]@{
        Name = $_.Name
        Path = $_.FullName
        Size = $_.Length
        LastWriteTime = $_.LastWriteTime
    }
}

# Root folders
$rootFolders = Get-ChildItem -Path $Path -Directory | ForEach-Object { $_.Name }

# Potential duplicates by Name and Size
$duplicates = $files | Group-Object -Property Name, Length | Where-Object { $_.Count -gt 1 } | ForEach-Object {
    $_.Group | Select-Object Name, FullName, Length, LastWriteTime
}

# File classification analysis
# Let's count files by target categories based on rules
$classificationCount = @{
    "DOCUMENTS" = 0
    "IMAGES" = 0
    "VIDEOS" = 0
    "AUDIO" = 0
    "ARCHIVES" = 0
    "INSTALLATEURS" = 0
    "WORDPRESS" = 0
    "IA_PROMPTS_EXPORTS" = 0
    "ADMIN_FACTURES" = 0
    "A_VERIFIER" = 0
}

$sampleClassification = New-Object System.Collections.Generic.List[PSCustomObject]

foreach ($file in $files) {
    # Check if the file is already inside one of the target structures to avoid infinite loop
    # or if we just want root files
    if ($file.Parent.FullName -ne $Path) {
        # Inside subfolders, maybe we don't want to move them or want to analyze them too.
        # Let's check.
    }
    
    $name = $file.Name.ToLower()
    $ext = $file.Extension.ToLower()
    $category = "A_VERIFIER"
    $reason = "Extension non répertoriée ou ambiguë"
    $confidence = "Faible"
    
    if ($ext -in (".pdf", ".doc", ".docx", ".txt", ".md", ".rtf")) {
        $category = "DOCUMENTS"
        $confidence = "Élevé"
        $reason = "Extension document"
    } elseif ($ext -in (".xls", ".xlsx", ".csv")) {
        $category = "DOCUMENTS"
        $confidence = "Moyen"
        $reason = "Tableur (classement par défaut)"
    } elseif ($ext -in (".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif")) {
        $category = "IMAGES"
        $confidence = "Élevé"
        $reason = "Extension image"
    } elseif ($ext -in (".mp4", ".mov", ".avi", ".mkv")) {
        $category = "VIDEOS"
        $confidence = "Élevé"
        $reason = "Extension vidéo"
    } elseif ($ext -in (".mp3", ".wav", ".m4a")) {
        $category = "AUDIO"
        $confidence = "Élevé"
        $reason = "Extension audio"
    } elseif ($ext -in (".zip", ".rar", ".7z", ".tar", ".gz")) {
        $category = "ARCHIVES"
        $confidence = "Élevé"
        $reason = "Extension archive"
    } elseif ($ext -in (".exe", ".msi", ".dmg", ".pkg")) {
        $category = "INSTALLATEURS"
        $confidence = "Élevé"
        $reason = "Extension installateur"
    }
    
    # Text-based routing overrides
    if ($name -match "(wordpress|wp|plugin|theme|woocommerce|fluent|rank-math|kadence|backup|export)") {
        $category = "WORDPRESS"
        $confidence = "Élevé"
        $reason = "Mot-clé WordPress détecté dans le nom"
    } elseif ($name -match "(prompt|chatgpt|claude|gemini|ia|ai|export)") {
        # Check if it was already wordpress export, but IA prompt is fine too.
        if ($category -ne "WORDPRESS") {
            $category = "IA_PROMPTS_EXPORTS"
            $confidence = "Moyen"
            $reason = "Mot-clé IA/Prompt détecté dans le nom"
        }
    } elseif ($name -match "(facture|invoice|devis|contrat|attestation|administratif)") {
        $category = "ADMIN_FACTURES"
        $confidence = "Élevé"
        $reason = "Mot-clé Administratif/Facture détecté dans le nom"
    }
    
    $classificationCount[$category]++
    
    if ($sampleClassification.Count -lt 100) {
        $sampleClassification.Add([PSCustomObject]@{
            Name = $file.Name
            Path = $file.FullName
            Category = $category
            Confidence = $confidence
            Reason = $reason
            Size = $file.Length
        })
    }
}

$report = [PSCustomObject]@{
    TotalFiles = $totalFiles
    TotalDirs = $totalDirs
    TotalSize = $totalSize
    Extensions = $extGroups
    LargestFiles = $largestFiles
    OldestFiles = $oldestFiles
    NewestFiles = $newestFiles
    RootFolders = $rootFolders
    DuplicatesCount = $duplicates.Count
    ClassificationCount = $classificationCount
    SampleClassification = $sampleClassification
}

$report | ConvertTo-Json -Depth 4 | Out-File -FilePath "D:\TÉLÉCHARGEMENT_audit.json" -Encoding utf8

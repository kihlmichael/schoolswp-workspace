#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Drive Common - Module partagé schoolsWP
==============================================
Centralise l'authentification et la configuration pour tous les scripts Drive.

Usage:
    from google_drive_common import get_drive_service, HttpError

    # Lecture seule (audit)
    service = get_drive_service(write_access=False)

    # Écriture (migration)
    service = get_drive_service(write_access=True)
"""

import sys
import io
import os

# Fix encodage Windows pour caractères spéciaux
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Google API imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# === CONFIGURATION CENTRALISÉE ===
CREDENTIALS_FILE = 'credentials.json'
TOKEN_READ_FILE = 'token.json'
TOKEN_WRITE_FILE = 'token_write.json'

SCOPES_READ = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES_WRITE = ['https://www.googleapis.com/auth/drive']


def get_drive_service(write_access: bool = False, verbose: bool = True):
    """
    Obtient un service Google Drive authentifié.

    Args:
        write_access: True pour permissions d'écriture, False pour lecture seule
        verbose: Afficher les messages de progression

    Returns:
        Service Google Drive ou None si échec
    """
    scopes = SCOPES_WRITE if write_access else SCOPES_READ
    token_file = TOKEN_WRITE_FILE if write_access else TOKEN_READ_FILE
    creds = None

    # Charger token existant
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, scopes)

    # Rafraîchir ou créer credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"\n❌ ERREUR: Fichier '{CREDENTIALS_FILE}' introuvable.")
                print("\n📋 Instructions:")
                print("1. Va sur https://console.cloud.google.com/")
                print("2. Crée un projet ou sélectionne un existant")
                print("3. Active l'API Google Drive")
                print("4. Crée des identifiants OAuth 2.0 (Application de bureau)")
                print(f"5. Télécharge le JSON et renomme-le '{CREDENTIALS_FILE}'")
                print(f"6. Place-le dans: {os.getcwd()}")
                return None

            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, scopes)
            creds = flow.run_local_server(port=0)

        # Sauvegarder token pour réutilisation
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    if verbose:
        mode = "ÉCRITURE" if write_access else "LECTURE SEULE"
        print(f"✅ Authentification réussie (mode {mode})")

    return service


# Exports publics
__all__ = [
    'get_drive_service',
    'HttpError',
    'SCOPES_READ',
    'SCOPES_WRITE',
    'CREDENTIALS_FILE',
    'TOKEN_READ_FILE',
    'TOKEN_WRITE_FILE',
]

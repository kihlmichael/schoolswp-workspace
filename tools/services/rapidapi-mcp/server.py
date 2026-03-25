"""
RapidAPI MCP Server — schoolsWP
Serveur MCP générique pour appeler n'importe quelle API RapidAPI.

Usage:
    uv run --with fastmcp --with requests fastmcp run server.py
"""

import os
import json
import requests
from fastmcp import FastMCP

mcp = FastMCP("RapidAPI")

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY", "")


@mcp.tool()
def call_rapidapi(
    host: str,
    endpoint: str,
    method: str = "GET",
    params: str = "{}",
    body: str = "{}",
) -> dict:
    """Call any RapidAPI endpoint.

    Args:
        host: The RapidAPI host (e.g. "linkedin-api8.p.rapidapi.com")
        endpoint: The API path (e.g. "/connection-count?username=johndoe")
        method: HTTP method — GET or POST (default: GET)
        params: JSON string of query parameters (default: "{}")
        body: JSON string of request body for POST requests (default: "{}")

    Returns:
        The API response as a dict with keys: status_code, headers, data
    """
    if not RAPIDAPI_KEY:
        return {"error": "RAPIDAPI_KEY environment variable is not set"}

    url = f"https://{host}{endpoint}"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": host,
    }

    try:
        query_params = json.loads(params) if params != "{}" else {}
        request_body = json.loads(body) if body != "{}" else None
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON: {e}"}

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=query_params,
            json=request_body,
            timeout=30,
        )

        try:
            data = response.json()
        except (json.JSONDecodeError, ValueError):
            data = response.text

        return {
            "status_code": response.status_code,
            "data": data,
        }
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}


@mcp.tool()
def list_rapidapi_examples() -> dict:
    """List example RapidAPI calls for common social media APIs.

    Returns a dict of example configurations for LinkedIn, Twitter/X,
    Instagram, TikTok, and YouTube APIs.
    """
    return {
        "linkedin_connections": {
            "host": "linkedin-api8.p.rapidapi.com",
            "endpoint": "/connection-count?username=micha%C3%ABlkihl",
        },
        "twitter_user_details": {
            "host": "twitter154.p.rapidapi.com",
            "endpoint": "/user/details?username=MichaelKihl",
        },
        "instagram_user_info": {
            "host": "instagram-scraper-api2.p.rapidapi.com",
            "endpoint": "/v1/info?username_or_id_or_url=michaelkihl",
        },
        "tiktok_user_info": {
            "host": "tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com",
            "endpoint": "/user/michaelkihl",
        },
        "youtube_channel_about": {
            "host": "yt-api.p.rapidapi.com",
            "endpoint": "/channel/about?id=UCCkeC6R8e5r5SrDl2hmYmZQ",
        },
    }

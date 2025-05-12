
from urllib.parse import urlencode
import json
import httpx
import os
from dotenv import load_dotenv
load_dotenv()


def generate_auth_url():
    base_url = "https://id.twitch.tv/oauth2/authorize"
    params = {
        "response_type": "token",
        "client_id": os.getenv("CLIENT_ID"),
        "redirect_uri": os.getenv("REDIRECT_URI"),
        "scope": os.getenv("SCOPES"),
        # optional, but very recommended
        "state": os.getenv("STATE")
    }

    return f"{base_url}?{urlencode(params)}"


def open_token():
    with open("./auth_token.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)["access_token"]


async def pegar_user_id(token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": os.getenv("CLIENT_ID")
    }

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.twitch.tv/helix/users",
            headers=headers)
        resp.raise_for_status()
        return resp.json()["data"][0]["id"]

print(generate_auth_url())

import asyncio
import json
import httpx
import os
from dotenv import load_dotenv
load_dotenv()

with open("./auth_token.json", "r", encoding="utf-8") as arquivo:
    token = json.load(arquivo)


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
        return resp.json()["data"][0]

print(asyncio.run(pegar_user_id(token["access_token"])))

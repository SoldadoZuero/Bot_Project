import httpx
import os
from dotenv import load_dotenv
from .utils import open_token

load_dotenv()

TWITCH_API_URL = "https://api.twitch.tv/helix/chat/messages"
CLIENT_ID = os.getenv("CLIENT_ID")
ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN") if os.getenv(
    "BOT_ACCESS_TOKEN") is not None else open_token()
BROADCASTER_ID = os.getenv("BROADCASTER_USER_ID")
SENDER_ID = os.getenv("BOT_USER_ID")


async def send_chat_message(message: str):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Client-Id": CLIENT_ID,
        "Content-Type": "application/json"
    }

    data = {
        "broadcaster_id": BROADCASTER_ID,
        "sender_id": SENDER_ID,
        "message": message
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            TWITCH_API_URL,
            headers=headers,
            json=data
        )
        if response.status_code != 200:
            print(f"[ERRO] Status {response.status_code}: {response.text}")
        else:
            print("[SUCCESS] Message sent!")

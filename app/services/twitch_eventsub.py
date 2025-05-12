import httpx
import os
from dotenv import load_dotenv

from app.utils import open_token
load_dotenv()

EVENTSUB_URL = "https://api.twitch.tv/helix/eventsub/subscriptions"
CLIENT_ID = os.getenv("CLIENT_ID")
BOT_ACCESS_TOKEN = open_token()
BROADCASTER_USER_ID = os.getenv("BROADCASTER_USER_ID")
BOT_USER_ID = os.getenv("BOT_USER_ID")


async def subscribe_to_chat(session_id: str):
    headers = {
        "Authorization": f"Bearer {BOT_ACCESS_TOKEN}",
        "Client-Id": CLIENT_ID,
        "Content-Type": "application/json"
    }

    payload = {
        "type": "channel.chat.message",
        "version": "1",
        "condition": {
            "broadcaster_user_id": BROADCASTER_USER_ID,
            "user_id": BOT_USER_ID
        },
        "transport": {
            "method": "websocket",
            "session_id": session_id
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            EVENTSUB_URL,
            json=payload,
            headers=headers
        )
        print("EventSub Subscription Response:",
              response.status_code, response.text)
        return response.json()

import asyncio
import websockets
import json
from app.services.commands import handle_command
from app.services.twitch_eventsub import subscribe_to_chat

TWITCH_WS_URL = "wss://eventsub.wss.twitch.tv/ws"


class TwitchWebSocketClient:
    async def connect(self):
        async with websockets.connect(TWITCH_WS_URL) as websocket:
            print("[WS] Conectado ao Twitch EventSub WebSocket")

            async for message in websocket:
                try:
                    event = json.loads(message)
                    print("📨 WS Event:", json.dumps(event, indent=2))

                    message_type = event.get(
                        "metadata", {}).get("message_type")

                    # Se for a primeira conexão, pega o session_id e faz a inscrição
                    if message_type == "session_welcome":
                        session_id = event["payload"]["session"]["id"]
                        print(f"[WS] Session ID recebido: {session_id}")
                        await subscribe_to_chat(session_id)

                    # Quando receber uma mensagem de chat
                    elif message_type == "notification":
                        chat_event = event["payload"]["event"]
                        message_text = chat_event["message"]["text"]
                        user_name = chat_event["chatter_user_name"]

                        print(f"💬 [{user_name}]: {message_text}")

                        await handle_command(message_text, user_name)

                except websockets.ConnectionClosed:
                    print("[WS] Conexão encerrada. Tentando reconectar...")
                    await asyncio.sleep(5)
                    return await self.connect()

                except Exception as e:
                    print(f"[WS] Erro inesperado: {e}")

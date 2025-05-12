from fastapi import APIRouter
from pydantic import BaseModel
from app.auth_storage import store_token
from app.chatbot import send_chat_message

router = APIRouter()


class TokenPayload(BaseModel):
    access_token: str


@router.post("/token")
async def receive_token(payload: TokenPayload):
    store_token(payload.access_token)
    return {"message": "Token successfully saved!"}


@router.get("/test-chat")
async def test_chat():
    await send_chat_message("Hello, Twitch! 👋")
    return {"message": "Message sent!"}

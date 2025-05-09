from fastapi import APIRouter
from pydantic import BaseModel
from app.auth_storage import store_token

router = APIRouter()


class TokenPayload(BaseModel):
    access_token: str


@router.post("/token")
async def receive_token(payload: TokenPayload):
    store_token(payload.access_token)
    return {"message": "Token salva com sucesso!"}

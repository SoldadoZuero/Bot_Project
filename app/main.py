from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.auth import router as auth_router
from app.utils import generate_auth_url
from app.services.twitch_ws_client import TwitchWebSocketClient
import asyncio


@asynccontextmanager
async def lifespan(app: FastAPI):
    # App start
    asyncio.create_task(TwitchWebSocketClient().connect())
    yield
    # App end

app = FastAPI(title="Twitch Bot", lifespan=lifespan)

app.include_router(auth_router)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/login")
async def login():
    return RedirectResponse(generate_auth_url())

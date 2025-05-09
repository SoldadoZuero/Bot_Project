from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.auth import router as auth_router
from app.utils import generate_auth_url

app = FastAPI(title="Twitch Bot")

app.include_router(auth_router)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/login")
async def login():
    return RedirectResponse(generate_auth_url())

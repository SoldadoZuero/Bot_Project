import json
from pathlib import Path

TOKEN_FILE = Path("auth_token.json")


def store_token(token: str) -> None:
    with open(TOKEN_FILE, "w") as f:
        json.dump({"access_token": token}, f)
    print("[AuthStorage] Your token has been saved.")


def get_token() -> str | None:
    if not TOKEN_FILE.exists():
        return None
    with open(TOKEN_FILE, "r") as f:
        return json.load(f).get("access_token")


def clear_token() -> None:
    if TOKEN_FILE.exists():
        TOKEN_FILE.unlink()
        print("[AuthStorage] Token removed.")

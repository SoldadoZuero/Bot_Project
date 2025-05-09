import os
from urllib.parse import urlencode
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

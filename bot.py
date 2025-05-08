import asyncio
import httpx
import os


async def get_OAuth():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://id.twitch.tv/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "client_id": os.environ.get('CLIENT_ID'),
                "client_secret": os.environ.get('CLIENT_SECRET'),
                "grant_type": "client_credentials"
            }
        )

        return response.json()

if __name__ == "__main__":
    print(asyncio.run(get_OAuth()))

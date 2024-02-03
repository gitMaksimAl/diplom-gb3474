from fastapi import FastAPI, requests
import httpx
import os

from database import startup, shutdown
from services import set_webhook, del_webhook

uri = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}"
app = FastAPI()
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)
app.add_event_handler("startup", set_webhook)
app.add_event_handler("shutdown", del_webhook)

updates: dict[int, str] = {}
ok = {"ok": True}


async def send_text(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        return await client.post(f"{uri}/sendMessage", content=text)


@app.post("/")
async def receive_update(request: requests.Request):
    update = await request.json()
    response = await send_text(update["message"]["chat"]["id"], update["message"]["text"])
    if response.json()["ok"]:
        return response


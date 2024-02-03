import os
import requests
import json
import logging


uri = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}"
log_file = "./bot.log"

logger = logging.getLogger(__name__)
updates: dict[int, str] = {}


def get_updates():
    response = requests.get(f"{uri}/getUpdates")
    updts = json.loads(response.content.decode("utf-8"))
    if updts["ok"] is True:
        for update in json.loads(response.content.decode("utf-8")):
            updates[update["message"]["chat"]["id"]] = update["message"]["text"]
    print("Error")


def send_text(chat_id: int, text: str):
    requests.post(f"{uri}/sendMessage", data={"chat_id": chat_id, "text": text})


if __name__ == '__main__':
    get_updates()
    for chat_id, text in updates.values():
        send_text(chat_id, text)

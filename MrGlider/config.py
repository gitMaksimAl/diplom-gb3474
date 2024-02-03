import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_URI = f"https://api.telegram.org/bot{BOT_TOKEN}"
LOG_FILE_URL = "./bot.log"

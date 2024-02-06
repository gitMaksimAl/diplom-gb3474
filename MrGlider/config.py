import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_URI = f"https://api.telegram.org/bot{BOT_TOKEN}"
LOG_FILE_URL = "./bot.log"
DATABASE_URI = os.getenv("DATABASE_URI")

SSL_CERT_PATH = os.getenv("SSL_CERT_PATH")
SSL_CERT_FILE = os.getenv("SSL_CERT_FILE")
SSL_KEY = os.getenv("SSL_KEY")

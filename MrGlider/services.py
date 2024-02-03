import httpx
import logging
import socket


from config import BOT_URI, LOG_FILE_URL, BOT_TOKEN


logger = logging.getLogger(__name__)
IP_ADDR = socket.gethostbyname(socket.gethostname())


async def set_webhook(token: str) -> None:
    async with httpx.AsyncClient() as client:
        result = await client.get(
            f"{BOT_URI}/setWebhook",
            headers={"X-Telegram-Bot-Api-Secret-Token": BOT_TOKEN},
            params={
                "url": IP_ADDR,
                "allowed_updates": "message",
            }
        )
        if result.headers["X-Telegram-Bot-Api-Secret-Token"] != BOT_TOKEN \
                or not result.json()["ok"]:
            logger.error("Webhook not set")
            raise ConnectionError("Webhook not set")


async def del_webhook(token: str) -> None:
    async with httpx.AsyncClient() as client:
        result = await client.get(
            f"{BOT_URI}/deleteWebhook",
            params={"url": ""}
        )
        if not result.json()["ok"]:
            logger.info("Webhook not deleted")

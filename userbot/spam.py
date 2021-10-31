from telethon import TelegramClient
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from userbot import bot

APP_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN2 = os.environ.get("BOTTOKEN2", None)
BOT_TOKEN3 = os.environ.get("BOTTOKEN3", None)
BOT_TOKEN4 = os.environ.get("BOTTOKEN4", None)
BOT_TOKEN5 = os.environ.get("BOTTOKEN5", None)
BOT_TOKEN6 = os.environ.get("BOTTOKEN6", None)
BOT_TOKEN7 = os.environ.get("BOTTOKEN7", None)
BOT_TOKEN8 = os.environ.get("BOTTOKEN8", None)
BOT_TOKEN9 = os.environ.get("BOTTOKEN9", None)
BOT_TOKEN10 = os.environ.get("BOTTOKEN10", None)

bot2 = TelegramClient(
    session="Legend-Bot",
    api_id=APP_ID,
    api_hash=API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=BOT_TOKEN2)



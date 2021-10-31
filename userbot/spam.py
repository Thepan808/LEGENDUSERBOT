
from telethon import TelegramClient
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

try:
  from userbot import bot 
except:
  pass


APP_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", None)
BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", None)
BOT_TOKEN4 = os.environ.get("BOT_TOKEN4", None)
BOT_TOKEN5 = os.environ.get("BOT_TOKEN5", None)
BOT_TOKEN6 = os.environ.get("BOT_TOKEN6", None)
BOT_TOKEN7 = os.environ.get("BOT_TOKEN7", None)
BOT_TOKEN8 = os.environ.get("BOT_TOKEN8", None)
BOT_TOKEN9 = os.environ.get("BOT_TOKEN9", None)
BOT_TOKEN10 = os.environ.get("BOT_TOKEN10", None)



bot2 = TelegramClient('LegendBoy2', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 
bot3 = TelegramClient('LegendBoy3', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 
bot4 = TelegramClient('LegendBoy4', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 
bot5 = TelegramClient('LegendBoy5', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 
bot6 = TelegramClient('LegendBoy6', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 
bot7 = TelegramClient('LegendBoy7', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 
bot8 = TelegramClient('LegendBoy8', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 
bot9 = TelegramClient('LegendBoy9', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 
bot10 = TelegramClient('LegendBoy10', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10) 

if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  bot2.run_until_disconnected()
  bot3.run_until_disconnected()
  bot4.run_until_disconnected()
  bot5.run_until_disconnected()
  bot6.run_until_disconnected()
  bot7.run_until_disconnected()
  bot8.run_until_disconnected()
  bot9.run_until_disconnected()
  bot10.run_until_disconnected()

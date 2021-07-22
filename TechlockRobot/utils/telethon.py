from telethon import TelegramClient

from TechlockRobot.utils.conf import get_int_key, get_str_key
from TechlockRobot import TOKEN, APP_ID, APP_HASH


NAME = TOKEN.split(":")[0]

tbot = TelegramClient(
    NAME, APP_ID, APP_HASH
)

# Telethon
tbot.start(bot_token=TOKEN)

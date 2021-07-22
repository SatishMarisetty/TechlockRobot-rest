import sys

from telethon import TelegramClient
from telethon.sessions import StringSession
from TechlockRobot import STRING_SESSION, API_HASH, API_ID

from TechlockRobot.utils.conf import get_int_key, get_str_key

ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot.start()
except BaseException:
    print("Userbot Error ! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)

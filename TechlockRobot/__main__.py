import requests
from pyrogram import Client as Bot
from TechlockRobot import API_HASH, API_ID, TOKEN
from TechlockRobot.utils.pyrogram import pbot

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="TechlockRobot.modules"),
)

bot.start()
pbot()

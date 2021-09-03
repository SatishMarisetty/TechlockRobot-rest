from pyrogram import Client

from TechlockRobot import API_ID, API_HASH, TOKEN


session_name = TOKEN.split(":")[0]
client = Client(session_name, API_ID, API_HASH)
run = client.run

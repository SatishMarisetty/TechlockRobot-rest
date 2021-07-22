from asyncio import Lock

from pyrogram import filters
from pyrogram.types import Message

from TechlockRobot import pbot as app
from TechlockRobot import arq 
from TechlockRobot.utils.dbfunctions import get_trust_db, update_trust_db
from TechlockRobot.utils.filter_groups import trust_group

spam_db = {}

lock_access = Lock()


async def get_spam_data(message: Message, text: str):
    async with lock_access:
        c, m = message.chat.id, message.message_id
        if c not in spam_db:
            spam_db[c] = {}
        if m not in spam_db[c]:
            data = (await arq.nlp(text)).result[0]
            spam_db[c][m] = data
        return spam_db[c][m]


@app.on_message(
    (filters.text | filters.caption)
    & ~filters.me
    & ~filters.private,
    group=trust_group,
)
async def trust_watcher_func(_, message: Message):
    # Sleeping so that we can get cached data created by
    # spam.py with get_spam_data function
    if message.command:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    text = message.text or message.caption
    text = text.strip()
    if not text:
        return
    if len(text) < 2:
        return
    data = await get_spam_data(message, text)
    if isinstance(data, str):
        return
    spam = data.spam
    await update_trust_db(user_id, spam)


async def get_spam_probability(user_id) -> list:
    data = await get_trust_db(user_id)
    if not data:
        return [0, 0]
    mean = lambda x: sum(x) / len(x)
    spam = [i for i in data]
    return [mean(spam), len(spam)]

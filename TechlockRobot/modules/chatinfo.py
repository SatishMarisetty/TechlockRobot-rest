import os

from pyrogram import filters
from pyrogram.types import Message

from pyrogram import Client as app
# from TechlockRobot.modules.trust import get_spam_probability


async def get_chat_info(chat):
    chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type = chat.type
    description = chat.description
    members = chat.members_count
    link = f"[Link](t.me/{username})" if username else None
    photo_id = chat.photo.big_file_id if chat.photo else None
    caption = f"""
**ID:** `{chat_id}`
**Type:** {type}
**Name:** {title}
**Username:** {("@" + username) if username else None}
**Mention:** {link}
**Members:** {members}
**Description:** {description}
"""
    return [caption, photo_id]


@app.on_message(filters.command("chatinfo"))
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text(
                "**Usage:**/chatinfo [USERNAME|ID]"
            )
        elif len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]
        m = await message.reply_text("Processing")
        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(
                info_caption, disable_web_page_preview=True
            )
        photo = await app.download_media(photo_id)
        await message.reply_photo(
            photo, caption=info_caption, quote=False
        )
        await m.delete()
        os.remove(photo)
    except Exception as e:
        await message.reply_text(e)
        print(e)
        await m.delete()

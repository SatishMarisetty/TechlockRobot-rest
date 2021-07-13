import os

from pyrogram import filters
from pyrogram.types import Message

from SaitamaRobot import pbot as app
from SaitamaRobot.utils.errors import capture_err
from SaitamaRobot.modules.trust import get_spam_probability


async def get_user_info(user):
    user = await app.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    photo_id = user.photo.big_file_id if user.photo else None
    spam_probab, n_messages = await get_spam_probability(user_id)
    isSpammer = (
        True
        if spam_probab > 50
        else False
        if spam_probab != 0
        else "Uncertain"
    )
    spam_probab = (
        str(round(spam_probab)) + " %"
        if spam_probab != 0
        else "Uncertain"
    )
    caption = f"""
**ID:** `{user_id}`
**Name:** {first_name}
**Username:** {("@" + username) if username else None}
**Mention:** {mention}
**AI Spam Detection:**
    **Spammer:** {isSpammer}
    **Spam Probability:** {spam_probab}
    `Stats Of Last {n_messages} Messages.`
"""
    return [caption, photo_id]


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


@app.on_message(filters.command("spaminfo"))
@capture_err
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    m = await message.reply_text("Processing")
    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))
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


@app.on_message(filters.command("chat_info"))
@capture_err
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text(
                "**Usage:**/chat_info [USERNAME|ID]"
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

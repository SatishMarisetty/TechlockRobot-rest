
import asyncio

from pyrogram import filters
from pyrogram.types import CallbackQuery, ChatPermissions, Message

from SaitamaRobot import pbot as app
from SaitamaRobot.utils.errors import capture_err




@app.on_message(
    (
        filters.command("everyone")
        | filters.command("all", prefixes="@")
    )
    & ~filters.edited
    & ~filters.private
)
@capture_err
async def report_user(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a message to report user."
        )
    list_of_members = await get_users(message.chat.id)
    user_mention = message.reply_to_message.from_user.mention
    text = f"Mentioned Everyone"
    for all in list_of_members:
        text += f"[\u2063](tg://user?id={all})"
    await message.reply_text(text)

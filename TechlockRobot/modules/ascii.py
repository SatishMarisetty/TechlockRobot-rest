from pyrogram import Client as pbot
from pyrogram import filters
import os

from img2html.converter import Img2HTMLConverter



@pbot.on_message(filters.command("ascii") & ~filters.edited)
async def ascii_func(_, e):
    if not e.reply_to_message:
        return await e.reply_text("`Reply to image.`")
    m = await e.reply_text("`Converting to html...`")
    media = e.reply_to_message.photo
    img = await (media).download_media()
    converter = Img2HTMLConverter(char="■")
    html = converter.convert(img)
    with open("html.html", "w") as t:
        t.write(html)
    await e.reply(file="html.html")
    await m.delete()
    os.remove(img)
    os.remove("html.html")

import random
from asyncio import gather
import os

from SaitamaRobot import pbot as app
from SaitamaRobot import arq
from SaitamaRobot.utils.functions import downloader
from SaitamaRobot.utils.errors import capture_err

from pyrogram import filters
from telegram import ParseMode



@app.on_message(filters.command("tr") & ~filters.edited)
@capture_err
async def tr(_, message):
    if len(message.command) != 2:
        return await message.reply_text("/tr [LANGUAGE_CODE]")
    lang = message.text.split(None, 1)[1]
    if not message.reply_to_message or not lang:
        return await message.reply_text(
            "Reply to a msg with /tr [lang code] \nDon't know Language codes check [here](https://developers.google.com/admin-sdk/directory/v1/languages)", parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True,)
    reply = message.reply_to_message
    text = reply.text or reply.caption
    if not text:
        return await message.reply_text(
            "Reply to a text to translate it"
        )
    result = await arq.translate(text, lang)
    error = f"""**Error occurred!**
Get supported language codes from [here](https://developers.google.com/admin-sdk/directory/v1/languages)"""
    if not result.ok:
        return await message.reply_text(error, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True,)
    await message.reply_text(f"""**Successfully translated to {lang}:**
`{result.result.translatedText}`""")



@app.on_message(filters.command("wall") & ~filters.edited)
@capture_err
async def wall(_, message):
    query = message.text[len("/wall ") :]
    if not query:
        return await message.reply_text("Enter a query to Search!")
    results = await arq.wall(query)
    reslts = results.result[(n):(n)+1]
    for i in reslts:
    wallpaper = await gather(downloader.download(f"{i.url_image}"))

    if not results.ok:
        return await message.reply_text("No wallpaper found! Refine your search.")
    n = random.randint(1,29)
          await message.reply_document(
                document=open(f"{wallpaper}"),
                filename=f"{query}",
                timeout=60,
            )

        os.remove(wallpaper)

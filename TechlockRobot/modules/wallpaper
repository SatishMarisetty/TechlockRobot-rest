from random import randint

import requests as r
from SaitamaRobot import SUPPORT_CHAT, WALL_API, dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot import arq
from telegram import Update
from telegram.ext import CallbackContext, run_async

# Wallpaper module powered by wall.alphacoders.com


@run_async
def wall(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    args = context.args
    msg_id = update.effective_message.message_id
    bot = context.bot
    query = " ".join(args)
    if not query:
        msg.reply_text("Please enter a query!")
        return
    else:
        results = await arq.wall(query)
    if not results.ok:
        return await message.reply_text("No wallpaper found! Refine your search.")
    n = randint(1,29)
    reslts = results.result[(n):(n)+1].url_image
                bot.send_photo(
                    chat_id,
                    photo=reslts,
                    caption="Preview",
                    reply_to_message_id=msg_id,
                    timeout=60,
                )
                bot.send_document(
                    chat_id,
                    document=reslts,
                    filename="wallpaper",
                    caption=query,
                    reply_to_message_id=msg_id,
                    timeout=60,
                )


WALLPAPER_HANDLER = DisableAbleCommandHandler("wall", wall)
dispatcher.add_handler(WALLPAPER_HANDLER)

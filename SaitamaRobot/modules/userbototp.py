
import html
import re
import os
import requests
from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update, MessageEntity
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_html

from SaitamaRobot import (
    DEV_USERS,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
    INFOPIC,
    dispatcher,
    sw,
)
from SaitamaRobot.__main__ import STATS, TOKEN, USER_INFO
import SaitamaRobot.modules.sql.userinfo_sql as sql
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.sql.global_bans_sql import is_user_gbanned
from SaitamaRobot.modules.redis.afk_redis import is_user_afk, afk_reason
from SaitamaRobot.modules.sql.users_sql import get_user_num_chats
from SaitamaRobot.modules.helper_funcs.chat_status import sudo_plus
from SaitamaRobot.modules.helper_funcs.extraction import extract_user





from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types

from SaitamaRobot.events import register as shit
from SaitamaRobot import telethn as tbot
from SaitamaRobot.utils.telethonub import ubot


async def is_register_admin(chat, user):

    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (
            await tbot(functions.messages.GetFullChatRequest(chat.chat_id))
        ).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    return None


async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response


@shit(pattern="^/mybototp ?(.*)")
async def _(event):

    if event.fwd_from:

        return

    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            return
        else:
            return
    if not event.reply_to_msg_id:

        await event.reply("```Reply to any user message.```")

        pass

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.reply("```reply to text message```")

        pass

    bot = context.bot


    chat = bot.get_chat(777000)
    uid = reply_message.sender_id
    reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    lol = await event.reply("```Processing```")

    async with ubot.conversation(chat) as conv:

        try:

            # response = conv.wait_event(
            #   events.NewMessage(incoming=True, from_users=1706537835)
            # )

            await silently_send_message(conv, f"OTP pampu raa!")

            # response = await response
            responses = await silently_send_message(conv, f"OTP pampu raa!")
        except YouBlockedUserError:

            await event.reply("```Bangaram Telegram ni block chesav ammma```")

            return
        await lol.edit(f"{responses.text}")
        # await lol.edit(f"{response.message.message}")

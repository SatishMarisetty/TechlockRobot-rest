
from telegram.ext import CallbackContext

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types
from telegram.ext.dispatcher import run_async

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
# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.


from pyrogram import filters

from SaitamaRobot.pluginhelper import admins_only, get_text
from SaitamaRobot import pbot


@pbot.on_message(filters.command("tagger") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("`Processing.....`")
    sh = get_text(message)
    if not sh:
        sh = "Hi!"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")


__mod_name__ = "TAGALL"
__help__ = """
Only for admins 
- /tagger : Tag everyone in a chat (not stable for big groups)
💡 Suggestion : Pin the msg you want to tag all check the notify all members

This is an essential feature to mention all subscribed members in the group. Any chat members can subscribe to tagger.
- /tagme: registers to the chat tag list.
- /untagme: unsubscribes from the chat tag list.
*Admin only:*
- /tagall: mention all subscribed members.
- /untagall: clears all subscribed members. 
- /addtag <userhandle>: add a user to chat tag list. (via handle, or reply)
- /removetag <userhandle>: remove a user to chat tag list. (via handle, or reply)

"""

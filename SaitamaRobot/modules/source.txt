from SaitamaRobot.utils.pluginhelp import admins_only
from SaitamaRobot import pbot

@pbot.on_message(filters.command("source") & ~filters.edited & ~filters.bot)
@admins_only
async def hmm(client, message):
    j = "🖕"
    await message.reply(j)
    

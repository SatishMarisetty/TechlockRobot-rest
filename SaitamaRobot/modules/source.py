from SaitamaRobot.events import register 

@register(cmds="source")  
async def _(message): 
j = "🖕" 
await message.reply(j)

from emoji import UNICODE_EMOJI
 #from google_trans_new import LANGUAGES, google_translator
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from googletrans import Translator

from TechlockRobot import dispatcher
from TechlockRobot.modules.disable import DisableAbleCommandHandler
from TechlockRobot.events import register


@register(pattern="^/tl ?(.*)")
async def _(event):
    if len(event.text) > 3:
        if not event.text[3] == " ":
            return
    input = event.text[4:6]
    txt = event.text[7:]
    xx = await event.reply("`Translating...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    elif input:
        text = txt
        lan = input or "en"
    else:
        return await xx.edit(f"`/tr LanguageCode` as reply to a message")
    translator = Translator()
    try:
        tt = translator.translate(text, dest=lan)
        output_str = f"**TRANSLATED** from {tt.src} to {lan}\n`{tt.text}`"
        await xx.edit(output_str)
    except Exception as exc:
        await xx.edit(str(exc))


__help__ = """
• `/tr` or `/tl` (language code) as reply to a long message
*Example:*
  `/tr en`*:* translates something to english
  `/tl hi-en`*:* translates hindi to english
            [all available language codes](https://developers.google.com/admin-sdk/directory/v1/languages)
"""
__mod_name__ = "G-TRANS"

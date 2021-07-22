from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
    Filters,
    MessageHandler,
)
from TechlockRobot.modules.helper_funcs.string_handling import markdown_parser
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    ParseMode,
    Update,
)
from TechlockRobot.modules.disable import DisableAbleCommandHandler
from TechlockRobot import dispatcher
from TechlockRobot.modules.helper_funcs.alternate import send_message
from telegram.utils.helpers import mention_html, mention_markdown

@run_async
def me(update: Update, context: CallbackContext):
 if update.effective_chat.type != "private":
    update.effective_message.reply_document(
                document=open(f"./TechlockRobot/shit/sticker.webp", "rb"),
                parse_mode=ParseMode.HTML,
            )




ME_HANDLER = MessageHandler(Filters.regex(r"(?i)@SatishMarisettyTG"), me)
dispatcher.add_handler(ME_HANDLER)

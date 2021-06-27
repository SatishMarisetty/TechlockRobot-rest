from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
)
from SaitamaRobot.modules.helper_funcs.string_handling import markdown_parser
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    ParseMode,
    Update,
)
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.helper_funcs.alternate import send_message
from telegram.utils.helpers import mention_html, mention_markdown

@run_async
def source(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """🖕""",
        parse_mode=ParseMode.MARKDOWN,
    )
@run_async
def source_shit(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            "",
        )
        return
    source(update)



SOURCE_HANDLER = CommandHandler("source", source_shit)
dispatcher.add_handler(SOURCE_HANDLER)

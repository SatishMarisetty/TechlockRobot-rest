from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
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
def source(update: Update, context: CallbackContext):
 if not update.effective_chat.type != "private":
    update.effective_message.reply_text(
        """🖕""",
        parse_mode=ParseMode.MARKDOWN,
    )



SOURCE_HANDLER = CommandHandler("source", source)
dispatcher.add_handler(SOURCE_HANDLER)

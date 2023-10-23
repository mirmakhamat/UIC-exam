"""
python-telegram-bot==20.6
"""

import logging

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonRequestUser
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from config import TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    text = ""
    if update.message.user_shared:
        text += f"User id: <code>{update.message.user_shared.user_id}</code>"
    elif update.message.chat_shared:
        text += f"Chat id: <code>{update.message.chat_shared.chat_id}</code>"
    else:
        if user.username:
            text += f"@{user.username}\n"
        text += f"ID: <code>{user.id}</code>\n"
        text += f"First: {user.first_name}\n"
        if user.last_name:
            text += f"Last: {user.last_name}\n"
        text += f"Lang: {user.language_code}"

    keyboard = [
        [KeyboardButton('User 👤', request_user=KeyboardButtonRequestUser(1, False))],
        [
            KeyboardButton('Super Group 👥', request_chat=KeyboardButtonRequestChat(2, False, chat_has_username=True)),
            KeyboardButton('Group 👥', request_chat=KeyboardButtonRequestChat(3, False, chat_has_username=False)),
        ],
        [
            KeyboardButton('Channel 🔊', request_chat=KeyboardButtonRequestChat(4, True, chat_has_username=True)),
            KeyboardButton('Private Channel 🔊', request_chat=KeyboardButtonRequestChat(5, True, chat_has_username=False)),
        ],
        [
            KeyboardButton('Bot 🤖', request_user=KeyboardButtonRequestUser(6, True)),
            KeyboardButton('Premium 🌟', request_user=KeyboardButtonRequestUser(7, user_is_premium=True)),
        ]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_html(
        text=text,
        reply_markup=markup
    )


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(MessageHandler(filters.ALL, start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

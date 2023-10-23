"""
python-telegram-bot==13.15
"""

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

from config import TOKEN

from kunuz import search_news

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Kun.uz'dan yangiliklarni olish uchun biror bir kalit so'zni kiriting.\n\nMisol uchun: amerika")
    

def news(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    news = search_news(text)
    if news:
        for item in news:
            update.message.reply_text(f"{item['title']}\n\nhttps://kun.uz{item['link']}")
    else:
        update.message.reply_text("Afsuski siz kiritgan kalit so'z bo'yicha yangilik topilmadi.")


def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, news))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

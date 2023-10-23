import logging
from bot.config import TOKEN

from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from bot.handlers import user
from bot.handlers import category
from bot.handlers import product
from bot.handlers import basket
from bot import states
from bot import strings


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def run() -> None:
    """Start the bot."""

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", user.start),
            MessageHandler(Filters.text(strings.BACK_BTN), user.start),
            MessageHandler(Filters.text(strings.ORDER_BTN), user.order),
            MessageHandler(Filters.text(strings.FEEDBACK_BTN), user.feedback),
            MessageHandler(Filters.text(strings.SETTINGS_BTN), user.settings),
            MessageHandler(Filters.text(strings.CONTACT_BTN), user.contact),
            MessageHandler(Filters.text(strings.BASKET_BTN), user.basket)
        ],
        states={
            states.MAIN: [
                MessageHandler(Filters.text(strings.ORDER_BTN), user.order),
                MessageHandler(Filters.text(
                    strings.FEEDBACK_BTN), user.feedback),
                MessageHandler(Filters.text(
                    strings.SETTINGS_BTN), user.settings),
                MessageHandler(Filters.text(
                    strings.CONTACT_BTN), user.contact),
            ],
            states.FEEDBACK: [
                MessageHandler(Filters.text(strings.BACK_BTN), user.start),
                MessageHandler(Filters.text & ~Filters.command, user.feedback_rating)
            ],
            states.CATEGORY: [
                MessageHandler(Filters.text(strings.BASKET_BTN), user.basket),
                MessageHandler(Filters.text(strings.BACK_BTN), user.start),
                MessageHandler(Filters.text & ~Filters.command, category.select_category),
            ],
            states.PRODUCT: [
                MessageHandler(Filters.text(strings.BACK_BTN), user.order),
                MessageHandler(Filters.text & ~Filters.command, product.select_product)
            ],
            states.PRODUCT_COUNT: [
                MessageHandler(Filters.text(strings.BACK_BTN), user.order),
                MessageHandler(Filters.text & ~Filters.command, product.product_count)
            ]
        },
        fallbacks=[
            MessageHandler(Filters.text(strings.BASKET_BTN), user.basket),
            CallbackQueryHandler(basket.order, pattern="order"),
            CallbackQueryHandler(basket.change_product_state)
        ],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

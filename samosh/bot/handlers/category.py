from telegram import Update
from telegram.ext import CallbackContext
from db.functions import category as category_functions
from bot.keyboards import category as category_keyboard
from bot.keyboards import product as product_keyboard

from bot import states

def select_category(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    user = update.effective_user
    category = category_functions.get_category_by_name(text)
    if category:
        context.user_data['category_id'] = category.id
        update.message.reply_text(
            "Bo'limni tanlang.",
            reply_markup=product_keyboard.product_keyboard_markup(category.id)
        )
        return states.PRODUCT
        

    update.message.reply_text(
        "Kategoriyani tanlang.",
        reply_markup=category_keyboard.categories_keyboard_markup(user.id)
    )
    return states.CATEGORY

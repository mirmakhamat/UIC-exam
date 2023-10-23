from telegram import Update
from telegram.ext import CallbackContext
from db.functions import product as product_functions
from db.functions import basket as basket_functions
from bot.keyboards import product as product_keyboard

from bot import states

def select_product(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    product = product_functions.get_product_by_name(text)
    if product:
        context.user_data['product_id'] = product.id
        if product.photo:
            update.message.reply_photo(
                product.photo,
                f"{product.name}\n\nNarxi: {product.price} so'm",
                reply_markup=product_keyboard.product_count_markup()
            )
        else:
            update.message.reply_text(
                f"{product.name}\n\nNarxi: {product.price} so'm",
                reply_markup=product_keyboard.product_count_markup()
            )
        return states.PRODUCT_COUNT
    category_id = context.user_data['category_id']
    update.message.reply_text(
        "Bo'limni tanlang.",
        product_keyboard.product_keyboard_markup(category_id)
    )

    return states.PRODUCT


def product_count(update: Update, context: CallbackContext) -> int:
    text = update.message.text
    user = update.effective_user
    product_id = context.user_data['product_id']
    category_id = context.user_data['category_id']

    if text.isdigit():
        count = int(text)
        basket_functions.add_product_to_basket(user.id, product_id, count)
        update.message.reply_text(
            "Savatchaga qo'shildi.\n\nDavom etamizmi? 😉",
            reply_markup=product_keyboard.product_keyboard_markup(category_id)
        )
        return states.PRODUCT

    update.message.reply_text(
        "Sonini kiriting",
        reply_markup=product_keyboard.product_count_markup()
    )
    return states.PRODUCT_COUNT
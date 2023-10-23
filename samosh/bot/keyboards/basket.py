from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot import strings


def user_basket_markup(basket, user_id) -> InlineKeyboardMarkup:
    keyboard = []
    for item in basket:
        keyboard.append([InlineKeyboardButton(
            item.product.name, callback_data="-")])
        keyboard.append([
            InlineKeyboardButton('➖', callback_data=f"minus-{item.id}"),
            InlineKeyboardButton('❌', callback_data=f"del-{item.id}"),
            InlineKeyboardButton('➕', callback_data=f"plus-{item.id}"),
        ])

    keyboard.append([InlineKeyboardButton(
        strings.ORDER_BTN, callback_data=f"order-{user_id}")])

    return InlineKeyboardMarkup(keyboard)

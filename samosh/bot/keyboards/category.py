from telegram import ReplyKeyboardMarkup, KeyboardButton
from db.functions import category as category_functions
from db.functions import basket as basket_functions

from bot import strings


def categories_keyboard_markup(telegram_id) -> ReplyKeyboardMarkup:
    categories = category_functions.get_all_categories()
    basket = basket_functions.get_user_basket(telegram_id)
    keyboard = []
    if basket:
        keyboard.append([KeyboardButton(strings.BASKET_BTN)])
        
    tmp = []
    for category in categories:
        tmp.append(KeyboardButton(category.name))
        if len(tmp) == 2:
            keyboard.append(tmp)
            tmp = []

    if len(tmp) != 0:
        keyboard.append(tmp)

    keyboard.append([KeyboardButton(strings.BACK_BTN)])

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

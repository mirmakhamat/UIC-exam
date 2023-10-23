from telegram import ReplyKeyboardMarkup
from bot import strings


def main_keyboard_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            strings.CONTACT_BTN, strings.ORDER_BTN
        ],
        [
            strings.FEEDBACK_BTN, strings.SETTINGS_BTN
        ]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def feedback_keyboard_markup() -> ReplyKeyboardMarkup:
    keyboard = [
        ['Hammasi yoqdi ❤️'],
        ['Yaxshi ⭐️⭐️⭐️⭐️'],
        ['Yoqmadi ⭐️⭐️⭐️'],
        ['Yomon ⭐️⭐️'],
        ['Juda yomon 👎'],
        [strings.BACK_BTN]
    ]

    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

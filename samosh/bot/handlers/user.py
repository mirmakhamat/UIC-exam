from bot import states
from bot import config

from telegram import Update
from telegram.ext import CallbackContext

from bot.keyboards import user as user_keyboard
from bot.keyboards import category as category_keyboard
from bot.keyboards import basket as basket_keyboard

from db.functions import user as user_functions
from db.functions import basket as basket_functions


def start(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    user_functions.register(user.id, user.first_name, user.last_name)

    update.message.reply_text(
        "Juda yaxshi birgalikda buyurtma beramizmi? 😃",
        reply_markup=user_keyboard.main_keyboard_markup()
    )

    return states.MAIN


def order(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_text(
        "Kategoriyani tanlang.",
        reply_markup=category_keyboard.categories_keyboard_markup(user.id)
    )

    return states.CATEGORY


def feedback(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "SamOshni tanlaganingiz uchun rahmat.\n\nAgar siz bizning xizmat sifatimizni yaxshilashimizga yordam bersangiz hursand bulardik.\nBuning uchun 5 ball tizim asosida baholang yoki o'z fikr va mulohazalaringizni yozib yuboring",
        reply_markup=user_keyboard.feedback_keyboard_markup()
    )
    return states.FEEDBACK


def feedback_rating(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    text = update.message.text
    context.bot.send_message(
        chat_id=config.GROUP_ID,
        text=f"{user.mention_html('Foydalanuvchi')} fikr yubordi:\n\n{text}",
        parse_mode="HTML"
    )
    update.message.reply_text(
        "Fikr va mulohazalaringiz uchun rahmat.",
        reply_markup=user_keyboard.main_keyboard_markup()
    )
    return states.MAIN


def settings(update: Update, context: CallbackContext) -> None:
    pass


def contact(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Buyurtma va boshqa savollar bo'yicha javob olish uchun murojaat qiling, barchasiga javob beramiz :)",
        reply_markup=user_keyboard.main_keyboard_markup())
        
    return states.MAIN

def basket(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    basket = basket_functions.get_user_basket(user.id)
    if not basket:
        update.message.reply_text("Sizning savatchangiz bo'sh")
        return

    text = "Sizning savatchangizda:\n\n"
    all_sum = 0
    for item in basket:
        product = item.product
        count = item.count
        summa = count * product.price
        all_sum += summa
        text += f"<b>{product.name}</b>\n{count} x {product.price} = {summa} so'm\n\n"

    text += f"Umumiy summa: {all_sum} so'm"

    update.message.reply_text(
        text, parse_mode="HTML", reply_markup=basket_keyboard.user_basket_markup(basket, user.id))

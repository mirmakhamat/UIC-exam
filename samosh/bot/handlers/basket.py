from telegram import Update
from telegram.ext import CallbackContext

from db.functions import basket as basket_functions
from bot.keyboards import basket as basket_keyboard


def change_product_state(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    state, product_id = query.data.split('-')
    ans = False
    if state == 'minus':
        ans = basket_functions.change_product_count(int(product_id), -1)
    elif state == 'plus':
        ans = basket_functions.change_product_count(int(product_id), 1)
    elif state == 'del':
        basket_functions.del_product(int(product_id))
        ans = True

    if not ans:
        return

    user = update.effective_user
    basket = basket_functions.get_user_basket(user.id)
    if not basket:
        query.edit_message_text("Sizning savatchangiz bo'sh.")
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

    query.edit_message_text(
        text, parse_mode="HTML", reply_markup=basket_keyboard.user_basket_markup(basket, user.id))


def order(update: Update, context: CallbackContext) -> None:
    pass

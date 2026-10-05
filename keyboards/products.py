from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

from consts import NAME_PRODUCT, NAME_CLOTHES, NAME_FOOD, ITEMS

def products_keyboard(product_type: str) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    items = ITEMS.get(product_type)
    for item in items:
        keyboard.button(text=item)
    keyboard.adjust(3)
    return keyboard.as_markup(resize_keyboard=True)
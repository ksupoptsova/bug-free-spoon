from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

from consts import FOOD_KEYBOARD, CLOTHES_KEYBOARD, PRODUCT_KEYBOARD

def types_of_product_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text = FOOD_KEYBOARD)
    keyboard.button(text = CLOTHES_KEYBOARD)
    keyboard.button(text = PRODUCT_KEYBOARD)
    keyboard.adjust(3)
    return keyboard.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)


from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

from consts import YES, NO, AGAIN

def answer()->ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text = YES)
    keyboard.button(text = NO)
    keyboard.button(text = AGAIN)
    keyboard.adjust(3)
    return keyboard.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)

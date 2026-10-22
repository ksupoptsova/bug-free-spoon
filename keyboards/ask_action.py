from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

from consts import ADD, DELETE

def action_keyboard()->ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text = ADD)
    keyboard.button(text = DELETE)
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)
import os
from dotenv import load_dotenv
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from repositories.food_repository import print_food
from aiogram import Bot



load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
router = Router()
@router.message(Command('food'))
async def food(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, text = print_food())


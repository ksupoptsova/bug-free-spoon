import os
from dotenv import load_dotenv
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot
from repositories.clothes_repository import print_clothes
from repositories.food_repository import print_food
from repositories.product_repository import print_product

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
router = Router()
@router.message(Command('all_products'))
async def all_products(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, text = print_clothes())
    await bot.send_message(chat_id, text=print_food())
    await bot.send_message(chat_id, text=print_product())
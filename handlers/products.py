import os
from dotenv import load_dotenv
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from repositories.product_repository import print_product
from aiogram import Bot

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
router = Router()
@router.message(Command('products'))
async def products(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, text = print_product())

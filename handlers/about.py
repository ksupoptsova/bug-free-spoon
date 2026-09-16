from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
@router.message(Command("about"))
async def about(message: Message):
    await message.answer(text = "Этот бот создан как онлайн - магазин, где можно приобрести различные товары")


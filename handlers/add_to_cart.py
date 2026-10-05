from states import AddToCartStates
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import Message
from consts import CATEGORIES, NAME_GOODS
from keyboards.category_of_product import types_of_product_keyboard
from keyboards.products import products_keyboard


router = Router()
@router.message(Command('add_product_to_cart'))
async def start(message: Message, state: FSMContext):
    await state.set_state(AddToCartStates.category_of_product)
    await message.answer("Выберите категорию товара",
                         reply_markup=types_of_product_keyboard())


@router.message(AddToCartStates.category_of_product)
async def name_of_product(message: Message, state: FSMContext):
    while True:
        category = CATEGORIES
        if message.text in category:
            break
        else:
            await message.answer("Напишите корректную категорию товара")
            return
    await state.update_data(category_of_product=message.text)
    await state.set_state(AddToCartStates.name_of_product)
    await message.answer("Напишите название товара (с большой буквы)",
                         reply_markup=products_keyboard(message.text))


@router.message(AddToCartStates.name_of_product)
async def quantity(message: Message, state: FSMContext):
    while True:
        name = NAME_GOODS
        if message.text in name:
            break
        else:
            await message.answer("Напишите корректное название товара")
            return
    await state.update_data(name_of_product=message.text)
    await state.set_state(AddToCartStates.quantity)
    await message.answer("Укажите количество товара")

@router.message(AddToCartStates.quantity)
async def finish(message: Message, state: FSMContext):
    while True:
        if message.text.isdigit():
            break
        else:
            await message.answer("Введите число")
            return
    await state.update_data(quantity=message.text)
    data = await state.get_data()
    await message.answer(f"{data.get("category_of_product")}, {data.get("name_of_product")}, {data.get("quantity")}")




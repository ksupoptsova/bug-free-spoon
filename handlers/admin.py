from aiogram.types import Message

from states import AdminStates
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router
from keyboards.category_of_product import types_of_product_keyboard
from keyboards.answer import answer
from consts import CLOTHES_KEYBOARD, FOOD_KEYBOARD, PRODUCT_KEYBOARD, YES, NO, AGAIN
from repositories import clothes_repository, food_repository, product_repository


router = Router()
@router.message(AdminStates.start)
@router.message(Command('admin'))
async def admin(message: Message, state: FSMContext):
    await state.set_state(AdminStates.password)
    await message.answer("Введите пароль")

@router.message(AdminStates.password)
async def finish_login_ask_category(message: Message, state: FSMContext):
    await state.set_state(AdminStates.category_of_product)
    if message.text == "111":
        await message.answer("Вы успешно авторизовались, выберите категорию товара",
                                 reply_markup=types_of_product_keyboard())
    else:
        await message.answer("Вы не админ!")
        return

@router.message(AdminStates.category_of_product)
async def add_name_of_product(message: Message, state: FSMContext):
    await state.update_data(category_of_product=message.text)
    await state.set_state(AdminStates.name_of_product)
    await message.answer("Введите название товара:")

@router.message(AdminStates.name_of_product)
async def add_quantity(message: Message, state: FSMContext):
    await state.update_data(name_of_product=message.text)
    await state.set_state(AdminStates.quantity)
    await message.answer("Введите количество товара:")

@router.message(AdminStates.quantity)
async def add_price(message: Message, state: FSMContext):
    while True:
        if message.text.isdigit():
            break
        else:
            await message.answer("Введите число!")
            return
    await state.update_data(quantity=message.text)
    await state.set_state(AdminStates.price)
    await message.answer("Введите цену:")

@router.message(AdminStates.price)
async def branches(message: Message, state: FSMContext):
    while True:
        if message.text.isdigit():
            break
        else:
            await message.answer("Введите число!")
            return
    await state.update_data(price=message.text)
    data = await state.get_data()
    if data.get("category_of_product") == CLOTHES_KEYBOARD:
        await state.set_state(AdminStates.size)
        await message.answer("Введите размер одежды:")
    elif data.get("category_of_product") == FOOD_KEYBOARD:
        await state.set_state(AdminStates.srok_godnosty)
        await message.answer("Введите срок годости продукта:")
    elif data.get("category_of_product") == PRODUCT_KEYBOARD:
        await message.answer("Товар успешно добавлен!")
    else:
        await message.answer("Вы ввели неверную категорию товара!")
        return

@router.message(AdminStates.size)
async def finish_add_clothes(message: Message, state: FSMContext):
    await state.update_data(size=message.text)
    data = await state.get_data()
    await message.answer(f"Категория товара:{data.get("category_of_product")},\n Название товара: {data.get("name_of_product")},\n Цена: {data.get("price")},\n Количество: {data.get("quantity")},\n Размер: {data.get("size")}")
    await state.set_state(AdminStates.clothes_confirm)
    await message.answer("Добавляем товар?", reply_markup=answer())


@router.message(AdminStates.srok_godnosty)
async def finish_add_food(message: Message, state: FSMContext):
    await state.update_data(srok_godnosty=message.text)
    data = await state.get_data()
    await message.answer(f"Категория товара:{data.get("category_of_product")},\n Название товара: {data.get("name_of_product")},\n Цена: {data.get("price")},\n Количество: {data.get("quantity")},\n Срок годности: {data.get("srok_godnosty")}")
    await state.set_state(AdminStates.food_confirm)
    await message.answer("Добавляем товар?", reply_markup=answer())


@router.message(AdminStates.food_confirm)
async def confirm_food(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == YES:
        food_repository.create(data)
    elif message.text == NO:
        await state.clear()
        await message.answer("Внесенные данные удалены")
    elif message.text == AGAIN:
        await state.set_state(AdminStates.start)
        await message.answer("Начало нового добавления. Выберите категорию товара:",
                             reply_markup=types_of_product_keyboard())

@router.message(AdminStates.product_confirm)
async def confirm_product(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == YES:
        product_repository.create(data)
    elif message.text == NO:
        await state.clear()
        await message.answer("Внесенные данные удалены")
    elif message.text == AGAIN:
        await state.set_state(AdminStates.start)
        await message.answer("Начало нового добавления. Выберите категорию товара:",
                             reply_markup=types_of_product_keyboard())

@router.message(AdminStates.clothes_confirm)
async def confirm_clothes(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == YES:
        clothes_repository.create(data)
    elif message.text == NO:
        await state.clear()
        await message.answer("Внесенные данные удалены")
    elif message.text == AGAIN:
        await state.set_state(AdminStates.start)
        await message.answer("Начало нового добавления. Выберите категорию товара:",
                             reply_markup=types_of_product_keyboard())










from aiogram.fsm.state import State, StatesGroup

class AddToCartStates(StatesGroup):
    category_of_product = State()
    name_of_product = State()
    quantity = State()


class AdminStates(StatesGroup):
    password = State()
    category_of_product = State()
    name_of_product = State()
    quantity = State()
    price = State()
    srok_godnosty = State()
    size = State()
    product_confirm = State()
    food_confirm = State()
    clothes_confirm = State()
    start = State()




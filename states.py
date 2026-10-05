from aiogram.fsm.state import State, StatesGroup

class AddToCartStates(StatesGroup):
    category_of_product = State()
    name_of_product = State()
    quantity = State()
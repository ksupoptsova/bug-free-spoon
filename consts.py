from repositories import clothes_repository, food_repository, product_repository

FOOD = ["Еда"]
CLOTHES = ["Одежда"]
PRODUCT = ["Продукты"]
CATEGORIES = FOOD + CLOTHES + PRODUCT


FOOD_KEYBOARD = "Еда"
CLOTHES_KEYBOARD = "Одежда"
PRODUCT_KEYBOARD = "Продукты"

NAME_CLOTHES_KEYBOARD = ""
NAME_FOOD_KEYBOARD = ""
NAME_PRODUCT_KEYBOARD = ""

ITEMS = {
    FOOD_KEYBOARD: food_repository.get_info_food_from_database(),
    CLOTHES_KEYBOARD: clothes_repository.get_info_clothes_from_database(),
    PRODUCT_KEYBOARD: product_repository.get_info_product_from_database()
    }

YES = "Да"
NO = "Нет"
AGAIN = "Добавить заново"

DELETE = "Удалить товар"
ADD = "Добавить товар"
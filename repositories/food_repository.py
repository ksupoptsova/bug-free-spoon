from sqlalchemy import select
from sqlalchemy.orm import Session
from database.food import Food
from config.db_config import Session

def print_food():
    text = "Тип товара: еда"
    with Session() as session:
        query = select(Food)
        res = session.scalars(query).all()
        for food in res:
            text += "\n" + str(food.id)+ ")" + "Название товара: " + food.name + ", "+ "Цена: " + str(food.price) + ", " + "Количество: " + str(food.quantity) + ", " + "Срок годности: " + food.srok_godnosty + "\n"
    return text

def create(data):
    name = data.get("name_of_product")
    price = data.get("price")
    quantity = data.get("quantity")
    srok_godnosty = data.get("srok_godnosty")
    with Session() as session:
        food = Food(name=name, price=price, quantity=quantity, srok_godnosty = srok_godnosty)
        session.add(food)
        session.commit()
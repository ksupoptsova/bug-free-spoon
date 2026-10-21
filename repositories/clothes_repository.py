from sqlalchemy import select
from sqlalchemy.orm import Session
from database.clothes import Clothes
from config.db_config import Session

def print_clothes():
    text = "Тип товара: одежда"
    with Session() as session:
        query = select(Clothes)
        res = session.scalars(query).all()
        for clothes in res:
            text += "\n" + str(clothes.id)+ ")" + "Название товара: " + clothes.name + ", "+ "Цена: " + str(clothes.price) + ", " + "Количество: " + str(clothes.quantity) + ", " + "Размер: " + clothes.size + "\n"
    return text

def create(data):
    name = data.get("name_of_product")
    price = data.get("price")
    quantity = data.get("quantity")
    size = data.get("size")
    with Session() as session:
        clothes = Clothes(name=name, price=price, quantity=quantity, size=size)
        session.add(clothes)
        session.commit()
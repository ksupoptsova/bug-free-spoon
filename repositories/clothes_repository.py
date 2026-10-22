from sqlalchemy import select
from sqlalchemy.orm import Session
from database.clothes import Clothes
from config.db_config import Session

def get_all_clothes():
    with Session() as session:
        clothes = session.query(Clothes).all()
        return clothes

def print_clothes():
    text = "Тип товара: одежда"
    res = get_all_clothes()
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

def get_info_clothes_from_database():
    with Session() as session:
        query = select(Clothes.name)
        clothes = session.execute(query).scalars().all()
        return clothes

def find_clothes_by_name(name):
    with Session() as session:
        clothes = session.query(Clothes).filter(Clothes.name == name).first()
        return clothes

print(find_clothes_by_name("Футболка"))







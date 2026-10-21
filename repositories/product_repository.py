from sqlalchemy import select
from sqlalchemy.orm import Session
from database.product import Product
from config.db_config import Session

def print_product() -> str:
    text = "Тип товара: продукты\n"
    with Session() as session:
        query = select(Product)
        res = session.scalars(query).all()
        for product in res:
            text += str(product.id)+ ")" + "Название товара: " + product.name + ", "+ "Цена: " + str(product.price) + ", " + "Количество: " + str(product.quantity) + "\n"
    return text

def create(data):
    name = data.get("name_of_product")
    price = data.get("price")
    quantity = data.get("quantity")
    with Session() as session:
        product = Product(name=name, price=price, quantity=quantity)
        session.add(product)
        session.commit()

def get_info_product_from_database():
    with Session() as session:
        query = select(Product.name)
        product = session.execute(query).scalars().all()
        return product
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.product import Product
from config.db_config import Session

def get_all_products():
    with Session() as session:
        product = session.query(Product).all()
        return product

def print_product() -> str:
    text = "Тип товара: продукты\n"
    with Session() as session:
        res = get_all_products()
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

get_all_products()

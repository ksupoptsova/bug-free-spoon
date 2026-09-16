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
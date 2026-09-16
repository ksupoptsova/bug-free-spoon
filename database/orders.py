from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from config.db_config import Base

class Orders(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    customer_name: Mapped[str] = mapped_column(String(50))
    total_price: Mapped[float] = mapped_column(Float)
    shop_name: Mapped[str] = mapped_column(String(50))





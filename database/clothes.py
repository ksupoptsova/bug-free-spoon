import os
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from config.db_config import Base

class Clothes(Base):
    __tablename__ = 'clothes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)
    size: Mapped[str] = mapped_column(String(10))


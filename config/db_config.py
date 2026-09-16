import os
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass


engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(engine, expire_on_commit=False)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = 'sqlite:///dolgoe.db'

Base = declarative_base()

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine, expire_on_commit=False)


def create_tables():
    Base.metadata.create_all(engine)

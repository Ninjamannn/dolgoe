from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = 'sqlite:///:dolgoe:'

Base = declarative_base()
engine = create_engine(DB_URL, echo=True)


Session = sessionmaker(bind=engine, expire_on_commit=False)


def create_tables():
    Base.metadata.create_all(engine)

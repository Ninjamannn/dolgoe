from sqlalchemy import Column, Integer, String

from database.db_session import SessionManager
from database.db_setup import Base


class User(Base, SessionManager):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(
        String(32)
    )

    def __init__(self, name):
        self.name = name

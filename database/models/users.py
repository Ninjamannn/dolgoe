from sqlalchemy import Column, String, Integer

from database.db_session import SessionManager
from database.db_setup import Base


class User(Base, SessionManager):
    __tablename__ = 'users'

    name = Column(String(32), primary_key=True)
    point = Column(Integer)

    def __init__(self, name: str, point: int = 0):
        self.name = name
        self.point = point

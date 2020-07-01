import random

from sqlalchemy import Column, String, Integer

from database.db_session import SessionManager
from database.db_setup import Base


class User(Base, SessionManager):
    __tablename__ = 'users'

    name = Column(String(32), primary_key=True)
    point = Column(Integer)
    secret = Column(String(32), nullable=False)

    def __init__(self, name: str, point: int = 0):
        self.name = name
        self.point = point
        self.secret = get_random_secret()


def get_random_secret():
    gps = ['1/4:55.45', '2/4:9405', '3/4: 26.77', '4/4:0728']
    return random.choice(gps)

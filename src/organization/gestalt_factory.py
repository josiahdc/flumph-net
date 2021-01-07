from sqlalchemy import create_engine

from src.config import DATABASE_URL
from src.organization.gestalt import Gestalt
from src.orm import Session
from src.orm.orm import DeclarativeBase


class GestaltFactory:
    @staticmethod
    def create():
        engine = create_engine(DATABASE_URL)
        Session.configure(bind=engine)
        DeclarativeBase.metadata.create_all(engine)
        return Gestalt()

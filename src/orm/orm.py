import re

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr, declarative_base


class ORM:
    @declared_attr
    def __tablename__(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    id = Column(Integer, primary_key=True)
    version_id = Column(Integer, nullable=False)

    __mapper_args__ = {
        "version_id_col": version_id
    }


DeclarativeBase = declarative_base(cls=ORM)

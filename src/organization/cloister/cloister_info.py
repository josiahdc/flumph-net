from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# noinspection PyUnresolvedReferences
from src.organization.cloister.directive.directive_info import DirectiveInfo
from src.orm.orm import DeclarativeBase
from src.orm.serializable_location import SerializableLocation


class CloisterInfo(DeclarativeBase):
    name = Column(String, nullable=False)
    origin = Column(SerializableLocation, nullable=False)

    directive_info = relationship(
        "DirectiveInfo",
        back_populates="cloister_info",
        uselist=False,
        cascade="all, delete-orphan"
    )
    homes = relationship("Home", back_populates="cloister_info", cascade="all, delete-orphan")
    flumph_info = relationship("FlumphInfo", back_populates="cloister_info")

    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

# noinspection PyUnresolvedReferences
from src.flumph.occupation.occupation_info import OccupationInfo
# noinspection PyUnresolvedReferences
from src.organization.cloister.home import Home
from src.orm.orm import DeclarativeBase
from src.orm.serializable_location import SerializableLocation


class FlumphInfo(DeclarativeBase):
    cloister_id = Column(Integer, ForeignKey("cloister_info.id"), nullable=False)
    name = Column(String, nullable=False)
    location = Column(SerializableLocation, nullable=False)

    occupation_info = relationship(
        "OccupationInfo",
        uselist=False,
        back_populates="flumph_info",
        cascade="all, delete-orphan"
    )
    cloister_info = relationship("CloisterInfo", back_populates="flumph_info")
    home = relationship("Home", uselist=False, back_populates="flumph_info")

    def __init__(self, cloister_info, name, location):
        self.cloister_info = cloister_info
        self.name = name
        self.location = location

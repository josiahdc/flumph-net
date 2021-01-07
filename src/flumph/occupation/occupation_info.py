from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.orm.orm import DeclarativeBase, ORM


class OccupationInfo(DeclarativeBase):
    flumph_id = Column(ForeignKey("flumph_info.id"), nullable=False)
    type = Column(String, nullable=False)

    flumph_info = relationship("FlumphInfo", back_populates="occupation_info")

    __mapper_args__ = {
        "polymorphic_identity": "occupation",
        "polymorphic_on": type,
        **ORM.__mapper_args__
    }

    def __init__(self, flumph_info):
        self.flumph_info = flumph_info

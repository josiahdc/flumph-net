from sqlalchemy import ForeignKey, Integer, Column

from src.flumph.occupation.occupation_info import OccupationInfo


class StripminerInfo(OccupationInfo):
    id = Column(Integer, ForeignKey("occupation_info.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "stripminer"
    }

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.orm.orm import DeclarativeBase, ORM


class TicketInfo(DeclarativeBase):
    directive_id = Column(ForeignKey("directive_info.id"), nullable=False)
    occupation_id = Column(ForeignKey("occupation_info.id"), nullable=True)
    type = Column(String, nullable=False)

    directive_info = relationship("DirectiveInfo", back_populates="ticket_info")
    occupation_info = relationship("OccupationInfo", back_populates="ticket_info")

    __mapper_args__ = {
        "polymorphic_identity": "ticket",
        "polymorphic_on": type,
        **ORM.__mapper_args__
    }

    def __init__(self, cloister_info):
        self.cloister_info = cloister_info

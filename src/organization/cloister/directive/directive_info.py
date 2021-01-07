from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.orm.orm import DeclarativeBase, ORM


class DirectiveInfo(DeclarativeBase):
    cloister_id = Column(ForeignKey("cloister_info.id"), nullable=False)
    type = Column(String, nullable=False)

    cloister_info = relationship("CloisterInfo", back_populates="directive_info")
    ticket_info = relationship("TicketInfo", back_populates="directive_info", cascade="all, delete-orphan")

    __mapper_args__ = {
        "polymorphic_identity": "directive",
        "polymorphic_on": type,
        **ORM.__mapper_args__
    }

    def __init__(self, cloister_info):
        self.cloister_info = cloister_info

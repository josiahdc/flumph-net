from sqlalchemy import ForeignKey, Integer, Column

from src.organization.cloister.directive.ticket.ticket_info import TicketInfo


class StripminingTicketInfo(TicketInfo):
    id = Column(Integer, ForeignKey("ticket_info.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "stripmining"
    }

from abc import ABC

from src.organization.cloister.directive.ticket.ticket_info import TicketInfo


class Ticket(ABC):
    def __init__(self, directive):
        self.directive = directive
        self._info_id = None

    def set_info_id(self, info_id):
        self._info_id = info_id

    def retrieve_self_info(self, db_session):
        return self.retrieve_info(db_session, self._info_id)

    @staticmethod
    def retrieve_info(db_session, info_id):
        return db_session.query(TicketInfo).filter(TicketInfo.id == info_id).one_or_none()

from src.organization.cloister.directive.ticket.stripmining_ticket_info import StripminingTicketInfo
from src.organization.cloister.directive.ticket.ticket import Ticket


class StripminingTicket(Ticket):
    def generate_info(self, db_session):
        return StripminingTicketInfo(self.directive.retrieve_self_info(db_session))

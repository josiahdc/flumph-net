from src.organization.cloister.directive.ticket.stripmining_ticket import StripminingTicket
from src.organization.cloister.directive.ticket.stripmining_ticket_info import StripminingTicketInfo
from src.organization.cloister.directive.ticket.ticket import Ticket
from src.orm.info import Info


class TicketFactory:
    @staticmethod
    def recover(db_session, directive, info_id):
        ticket_info = Ticket.retrieve_info(db_session, info_id)
        if isinstance(ticket_info, StripminingTicketInfo):
            ticket = StripminingTicket(directive)
            ticket.set_info_id(ticket_info.id)
        else:
            raise TypeError(f"unknown TicketInfo type: {type(ticket_info)}")
        return ticket

    @staticmethod
    def create_stripmining_ticket(db_session, directive):
        ticket = StripminingTicket(directive)
        ticket_info = Info.save(db_session, ticket)
        ticket.set_info_id(ticket_info.id)
        return ticket

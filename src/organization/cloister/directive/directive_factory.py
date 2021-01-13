import ujson

from src.common.location import Location
from src.organization.cloister.directive.stripmine_directive import StripmineDirective
from src.organization.cloister.directive.ticket.ticket_factory import TicketFactory


class DirectiveFactory:
    @staticmethod
    def recover(hoard, cloister):
        data = hoard.load_directive_data(cloister)
        directive_id = data["directive_id"]
        if data.get("stripmine_directive_id", None) is not None:
            if data.get("directive_last_ticket_origin", None) is not None:
                last_ticket_origin = Location.deserialize(data["directive_last_ticket_origin"])
            else:
                last_ticket_origin = None
            directive = StripmineDirective(hoard, cloister, last_ticket_origin, directive_id=directive_id)
        else:
            raise TypeError(f"could not discern directive type from data: {ujson.dumps(data)}")
        tickets = TicketFactory.recover_all_tickets(hoard, directive)
        directive.set_tickets(tickets)
        return directive

    @staticmethod
    def create_stripmining_directive(hoard, cloister):
        directive = StripmineDirective(hoard, cloister, None)
        directive_id = hoard.insert_directive(directive)
        directive.set_directive_id(directive_id)
        return directive

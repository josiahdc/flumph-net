import ujson

from src.common.location import Location
from src.organization.cloister.directive.ticket.stripmining_ticket import StripminingTicket


class TicketFactory:
    @staticmethod
    def recover_all_tickets(hoard, directive):
        tickets = []
        ticket_data = hoard.load_all_ticket_data(directive)
        for ticket_row in ticket_data:
            ticket_id = ticket_row["ticket_id"]
            flumph_id = ticket_row["flumph_id"]
            completed = ticket_row["ticket_completed"]
            if ticket_row.get("stripmining_ticket_id", None) is not None:
                origin = Location.deserialize(ticket_row["ticket_origin"])
                x_range = ticket_row["ticket_x_range"]
                z_range = ticket_row["ticket_z_range"]
                y_range = ticket_row["ticket_y_range"]
                ticket = StripminingTicket(
                    directive,
                    flumph_id,
                    completed,
                    origin,
                    x_range,
                    z_range,
                    y_range,
                    ticket_id=ticket_id
                )
                tickets.append(ticket)
            else:
                raise TypeError(f"could not discern ticket type from data: {ujson.dumps(ticket_row)}")
        return tickets

    @staticmethod
    def create_stripmining_ticket(hoard, directive, flumph_id, origin, x_range, z_range, y_range):
        ticket = StripminingTicket(directive, flumph_id, False, origin, x_range, z_range, y_range)
        ticket_id = hoard.insert_ticket(ticket)
        ticket.set_ticket_id(ticket_id)
        return ticket

from src.organization.cloister.directive.ticket.ticket import Ticket


class StripminingTicket(Ticket):
    def __init__(self, directive, flumph_id, completed, origin, x_range, z_range, y_range, ticket_id=None):
        super().__init__(directive, flumph_id, completed, ticket_id=ticket_id)
        self.origin = origin
        self.x_range = x_range
        self.z_range = z_range
        self.y_range = y_range

from src.organization.cloister.directive.ticket.ticket import Ticket


class StripminingTicket(Ticket):
    def __init__(self, directive, flumph_name, origin, x_range, z_range, y_range, completed):
        super().__init__(directive, flumph_name)
        self.origin = origin
        self.x_range = x_range
        self.z_range = z_range
        self.y_range = y_range
        self.completed = completed

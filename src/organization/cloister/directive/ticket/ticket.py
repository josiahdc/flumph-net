from abc import ABC


class Ticket(ABC):
    def __init__(self, directive, flumph_name, ticket_id=None):
        self.directive = directive
        self.flumph_name = flumph_name
        self.ticket_id = ticket_id

    def set_ticket_id(self, ticket_id):
        self.ticket_id = ticket_id

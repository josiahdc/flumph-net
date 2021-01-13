from abc import ABC


class Ticket(ABC):
    def __init__(self, directive, flumph_id, completed, ticket_id=None):
        self.directive = directive
        self.flumph_id = flumph_id
        self.ticket_id = ticket_id
        self.completed = completed

    def set_ticket_id(self, ticket_id):
        self.ticket_id = ticket_id

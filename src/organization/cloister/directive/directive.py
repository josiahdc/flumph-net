from abc import ABC, abstractmethod


class Directive(ABC):
    def __init__(self, hoard, cloister, directive_id):
        self.hoard = hoard
        self.cloister = cloister
        self.tickets = []
        self.directive_id = directive_id

    def set_directive_id(self, directive_id):
        self.directive_id = directive_id

    def set_tickets(self, tickets):
        self.tickets = tickets

    @abstractmethod
    def allocate_ticket(self, flumph):
        pass

    def retrieve_ticket(self, flumph):
        for ticket in self.tickets:
            if ticket.flumph_id == flumph.flumph_id and ticket.completed is False:
                return ticket
        return None

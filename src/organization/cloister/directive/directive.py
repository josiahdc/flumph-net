from abc import ABC, abstractmethod


class Directive(ABC):
    def __init__(self, cloister, directive_id=None):
        self.cloister = cloister
        self.tickets = []
        self.directive_id = directive_id

    def set_directive_id(self, directive_id):
        self.directive_id = directive_id

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    @abstractmethod
    def get_ticket(self, flumph):
        pass
